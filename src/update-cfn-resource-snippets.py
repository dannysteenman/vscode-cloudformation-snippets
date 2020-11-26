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


def create_cfn_snippet(response_data):
    # Start the output data
    output = {}

    scope = "source.cloudformation"

    # Add the resources to the output
    # print(response_data)
    for resource_type in response_data["ResourceTypes"]:
        prefix = resource_type.replace("AWS::", "").replace("::", "-")
        prefix = prefix.lower()

        body = ""
        description = ""
        body += "${1:LogicalID}:\r\n"

        # add a name placeholder
        body += '\tType: "' + resource_type + '"\r\n'
        body += "\tProperties:\r\n"

        description = "Attributes:\r\n"
        if "Attributes" in response_data["ResourceTypes"][resource_type]:
            for a in response_data["ResourceTypes"][resource_type]["Attributes"]:
                # description = description + "Attributes: " + "\r\n\t" + a
                description = description + "  " + a + "\r\n"
        else:
            description = "No Attributes\r\n"

        # for each resources 'properties':
        for p in response_data["ResourceTypes"][resource_type]["Properties"]:

            required = response_data["ResourceTypes"][resource_type]["Properties"][p][
                "Required"
            ]

            item = ""
            itemList = 0

            if (
                "PrimitiveType"
                in response_data["ResourceTypes"][resource_type]["Properties"][p]
            ):
                item = response_data["ResourceTypes"][resource_type]["Properties"][p][
                    "PrimitiveType"
                ]

            if (
                "PrimitiveItemType"
                in response_data["ResourceTypes"][resource_type]["Properties"][p]
            ):
                item = response_data["ResourceTypes"][resource_type]["Properties"][p][
                    "PrimitiveItemType"
                ]

            if (
                "ItemType"
                in response_data["ResourceTypes"][resource_type]["Properties"][p]
            ):
                item = response_data["ResourceTypes"][resource_type]["Properties"][p][
                    "ItemType"
                ]

            if "Type" in response_data["ResourceTypes"][resource_type]["Properties"][p]:
                if (
                    response_data["ResourceTypes"][resource_type]["Properties"][p][
                        "Type"
                    ]
                    == "List"
                ):
                    itemList = 1
                else:
                    itemList = 2
                    item = response_data["ResourceTypes"][resource_type]["Properties"][
                        p
                    ]["Type"]

            ###########################

            if itemList == 0:
                body += "\t\t" + p + ": " + item + ""
                body += " #required\r\n" if required else "\r\n"
            elif itemList == 1:
                body += "\t\t" + p + ":" + ""
                body += " #required\r\n" if required else "\r\n"
                body += "\t\t\t- " + item + "\r\n"

            elif itemList == 2:
                body += "\t\t" + p + ":" + ""
                body += " #required\r\n" if required else "\r\n"
                body += "\t\t\t" + item + "\r\n"

            output[resource_type] = {
                "prefix": prefix,
                "body": body,
                "description": description,
            }

    with open("snippets/resource-types.json", "w") as text_file:
        text_file.write(json.dumps(output, sort_keys=True, indent=4))


# Run cfn resource updater
if __name__ == "__main__":
    check_for_update(cfn_resource_spec_url)
