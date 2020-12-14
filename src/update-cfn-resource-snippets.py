import hashlib
import json
import requests

cfn_resource_spec_url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"


def check_for_update(url):
    """This function checks the resource spec file for it's md5 hash to see if it has been updated.

    Args:
        url (string): This contains the resource spec from us-east-1
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

    Returns:
        boolean: Indicates if the resource spec has been updated by Amazon or not.
        If it matches, exit 1 thus blocking the pipeline from continuing
        If it doesn't, update the file and git the file so next run will/won't be blocked
    """

    # Load the source data and hash it
    response = requests.get(url)

    # Load the current hash
    with open("src/current-json-spec-hash", "r+") as file:
        current_hash = file.read()
        new_hash = hashlib.md5(response.content).hexdigest()

        if new_hash == current_hash:
            print(
                f"The new hash: {new_hash} matches with our current hash: {current_hash}."
            )
            print("The snippets are up-to-date, stopping the pipeline.")
            exit(1)
        else:
            print(
                "Found an update in the cfn-resource-specification, let's update the resource snippets!"
            )
            file.seek(0)
            file.write(new_hash)
            create_cfn_snippet(response.json())


def parse_body(body, counter, resource_properties, resource_property):
    required = resource_properties[resource_property]["Required"]

    item = ""

    if "PrimitiveItemType" in resource_properties[resource_property]:
        item = resource_properties[resource_property]["PrimitiveItemType"]
    if "PrimitiveType" in resource_properties[resource_property]:
        item = resource_properties[resource_property]["PrimitiveType"]
    if "ItemType" in resource_properties[resource_property]:
        item = resource_properties[resource_property]["ItemType"]

    if "Type" in resource_properties[resource_property]:
        body.append(
            " " * 4 + resource_property + ":" + (" #required" if required else "")
        )
        # If the Type is a List, the body should be adapted so that the user knows the property is of type list.
        if resource_properties[resource_property]["Type"] == "List":
            body.append(" " * 6 + "- " + "${" + str(counter) + ":" + item + "}")
        else:
            item = resource_properties[resource_property]["Type"]
            body.append(" " * 6 + "${" + str(counter) + ":" + item + "}")
    else:
        body.append(
            " " * 4
            + resource_property
            + ": "
            + "${"
            + str(counter)
            + ":"
            + item
            + "}"
            + (" #required" if required else "")
        )

    return body


def fetch_description(resource_type):
    description = [resource_type["Documentation"].replace("http://", "https://")]

    # Adding resource type attributes next to the documantation url if it's available.
    if "Attributes" in resource_type:
        description.append("Attributes: ")
        for attribute in resource_type["Attributes"]:
            description.append("  " + attribute)

    return description


def create_cfn_snippet(response_data):
    # Start the output data
    output = {}

    # Add the resources to the output
    for resource_type in response_data["ResourceTypes"]:
        description = fetch_description(response_data["ResourceTypes"][resource_type])
        prefix = resource_type.replace("AWS::", "").replace("::", "-")
        body = ["${1:LogicalID}:", "  Type: " + resource_type, "  Properties:"]

        # for each resources 'properties'
        resource_properties = response_data["ResourceTypes"][resource_type][
            "Properties"
        ]

        for counter, resource_property in enumerate(
            sorted(resource_properties), start=2
        ):
            updated_body = parse_body(
                body, counter, resource_properties, resource_property
            )

            output[resource_type] = {
                "body": updated_body,
                "description": description,
                "prefix": prefix.lower(),
                "scope": "source.cloudformation",
            }

    with open("snippets/resource-types.json", "w") as file:
        file.write(json.dumps(output, sort_keys=True, indent=4))


# Run cfn resource updater
if __name__ == "__main__":
    check_for_update(cfn_resource_spec_url)
