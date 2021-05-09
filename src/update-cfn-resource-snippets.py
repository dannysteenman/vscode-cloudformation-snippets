import hashlib
import json
import requests


def get_resource_spec():
    cfn_resource_spec_url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
    # Load the source data and hash it
    response = requests.get(cfn_resource_spec_url)

    return response


def check_for_update():
    """This function checks the resource spec file for it's md5 hash to see if it has been updated.

    Args:
        url (string): This contains the resource spec from us-east-1
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

    Returns:
        boolean: Indicates if the resource spec has been updated by Amazon or not.
        If it matches, exit 1 thus blocking the pipeline from continuing
        If it doesn't, update the file and git the file so next run will/won't be blocked
    """

    # Load the current hash
    with open("src/current-json-spec-hash", "r+") as file:
        current_hash = file.read()
        # Load the source data and hash it
        new_hash = hashlib.md5(get_resource_spec().content).hexdigest()

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
            create_cfn_snippet(get_resource_spec().json())


def parse_body(body, counter, resource_properties, resource_property, resource_type):
    required = resource_properties[resource_property]["Required"]
    item = types(resource_properties[resource_property])

    if "Type" in resource_properties[resource_property]:
        if resource_properties[resource_property]["Type"] == "List":
            body.append(
                " " * 4 + f"{resource_property}:" + (" # Required" if required else "")
            )
            body.append(" " * 6 + resource_property[:-1])
        else:
            item = resource_properties[resource_property]["Type"]
            body.append(" " * 4 + resource_property + ":")
            get_item_type_prop(body, item, resource_type, counter)
    else:
        set_value_type(body, resource_property, item, counter, required, indent=4)

    return body


def get_item_type_prop(body, item, resource_type, counter, indent=6):
    # Get cfn resource spec
    response_data = get_resource_spec().json()
    # Create item type property e.g. AWS::Backup::BackupPlan.BackupRuleResourceType
    resource_property_name = resource_type + "." + item

    for property_type in response_data["PropertyTypes"]:
        properties = response_data["PropertyTypes"][property_type].get("Properties")
        if resource_property_name == property_type and properties:
            for updated_counter, property in enumerate(
                sorted(properties), start=counter
            ):
                item = types(properties[property])
                if "Type" in properties[property]:
                    if properties[property]["Type"] == "List":
                        body.append(" " * indent + property + ":")
                        body.append(" " * (indent + 2) + "-")
                        # get_item_type_prop(
                        #     body, item, resource_type, updated_counter, indent=10
                        # )
                    elif property == (properties[property]["Type"] or None):
                        continue
                else:
                    set_value_type(
                        body,
                        property,
                        item,
                        updated_counter,
                        required=None,
                        indent=indent,
                    )
    return body


def set_value_type(body, property, item, counter, required, indent):
    try:
        value_type = {
            "Boolean": "|false,true|",
            "Double": ":Number",
            "Integer": ":Number",
            "Json": ":JSON",
            "Long": ":Number",
            "String": ":String",
            "Timestamp": ":Timestamp",
        }

        body.append(
            " " * indent
            + property
            + ": "
            + ('"${' if item == "String" else "${")
            + f"{str(counter)}{value_type[item]}"
            + ('}"' if item == "String" else "}")
            + ","
            + (" # Required" if required else "")
        )
    except KeyError:
        print(f"This property: {property} has an unsupported value: {item}")

    return body


def types(property):
    if "PrimitiveItemType" in property:
        return property["PrimitiveItemType"]
    if "PrimitiveType" in property:
        return property["PrimitiveType"]
    if "ItemType" in property:
        return property["ItemType"]


def fetch_description(resource_type):
    description = [resource_type["Documentation"].replace("http://", "https://")]

    # Adding resource type attributes next to the documantation url if it's available.
    if "Attributes" in resource_type:
        description.append("Attributes: ")
        for attribute in resource_type["Attributes"]:
            description.append(f"  {attribute}")

    return description


def create_cfn_snippet(response_data):
    # Start the output data
    output = {}

    # Add the resources to the output
    for resource_type in response_data["ResourceTypes"]:
        prefix = resource_type.replace("AWS::", "").replace("::", "-")
        description = fetch_description(response_data["ResourceTypes"][resource_type])
        body = ["${1:LogicalID}:", "  Type: " + resource_type, "  Properties:"]

        # for each resources 'properties'
        resource_properties = response_data["ResourceTypes"][resource_type][
            "Properties"
        ]

        updated_body = []
        for counter, resource_property in enumerate(
            sorted(resource_properties), start=2
        ):
            updated_body = parse_body(
                body, counter, resource_properties, resource_property, resource_type
            )

        output[resource_type] = {
            "body": updated_body,
            "description": description,
            "prefix": prefix.lower(),
            "scope": "yaml",
        }

    with open("snippets/resource-types.json", "w") as file:
        file.write(json.dumps(output, sort_keys=True, indent=4))


# Run cfn resource updater
if __name__ == "__main__":
    check_for_update()
