from concurrent.futures import ThreadPoolExecutor
import argparse
import concurrent.futures
import hashlib
import json
import os
import requests

parser = argparse.ArgumentParser(
    description="Process CloudFormation Resource Specification"
)
parser.add_argument(
    "--local",
    dest="local_path",
    help="Path to local JSON resource specification file (optional)",
)
parser.add_argument(
    "--format",
    dest="output_format",
    choices=["json", "yaml"],
    default="yaml",
    help="Output format for the snippets (default: %(default)s)",
)
args = parser.parse_args()


def get_resource_spec(local_path=None):
    if local_path:
        abs_path = os.path.abspath(local_path)
        if os.path.exists(abs_path):
            with open(abs_path, "r") as f:
                response = json.load(f)
        else:
            raise FileNotFoundError(f"File not found: {abs_path}")
    else:
        cfn_resource_spec_url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
        response = requests.get(cfn_resource_spec_url).json()

    return response


def parse_body_yaml(
    body, counter, resource_properties, resource_property, resource_type
):
    property_info = resource_properties[resource_property]
    required = property_info["Required"]
    item = get_item_type(property_info)

    if "Type" in property_info:
        if property_info["Type"] == "List":
            body.extend(
                [
                    f"    {resource_property}: {'# Required' if required else ''}",
                    f"      {resource_property}",
                ]
            )
        else:
            item = property_info["Type"]
            body.append(f"    {resource_property}:")
            get_item_type_prop(body, item, resource_type, counter)
    else:
        set_value_type(body, resource_property, item, counter, required, indent=4)

    return body


def get_item_type(resource_property):
    return resource_property.get(
        "PrimitiveItemType",
        resource_property.get("PrimitiveType", resource_property.get("ItemType")),
    )


def get_item_type_prop(body, item, resource_type, counter, indent=6):
    response_data = get_resource_spec()
    resource_property_name = f"{resource_type}.{item}"

    for property_type, property_data in response_data["PropertyTypes"].items():
        properties = property_data.get("Properties")
        if resource_property_name == property_type and properties:
            for updated_counter, property in enumerate(
                sorted(properties), start=counter
            ):
                property_info = properties[property]
                item = get_item_type(property_info)

                if "Type" in property_info:
                    if property_info["Type"] == "List":
                        body.extend(
                            [f"{' ' * indent}{property}:", f"{' ' * (indent + 2)}-"]
                        )
                    elif property == (property_info["Type"] or None):
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
    value_type = {
        "Boolean": "|false,true|",
        "Double": ":Number",
        "Integer": ":Number",
        "Json": ":JSON",
        "Long": ":Number",
        "String": ":String",
        "Timestamp": ":Timestamp",
    }

    if item in value_type:
        prefix = f"${{{counter}{value_type[item]}}}"
        if item == "String":
            prefix = f'"{prefix}"'
        body.append(
            f"{' ' * indent}{property}: {prefix}{' # Required' if required else ''}"
        )
    else:
        print(f"This property: {property} has an unsupported value: {item}")

    return body


def parse_body_json(
    body, counter, resource_properties, resource_property, resource_type
):
    property_info = resource_properties[resource_property]
    item = get_item_type(property_info)

    is_last_property = resource_property == sorted(resource_properties)[-1]

    if "Type" in property_info:
        if property_info["Type"] == "List":
            body.extend(
                [
                    f'    "{resource_property}": [',
                    f'      "{resource_property}"',
                    "    ]" + ("," if not is_last_property else ""),
                ]
            )
        else:
            item = property_info["Type"]
            body.append(f'    "{resource_property}": {{')
            get_item_type_prop_json(body, item, resource_type, counter)
    else:
        set_value_type_json(
            body,
            resource_property,
            item,
            counter,
            indent=4,
            is_last=is_last_property,
        )

    return body


def get_item_type_prop_json(body, item, resource_type, counter, indent=6):
    response_data = get_resource_spec()
    resource_property_name = f"{resource_type}.{item}"

    for property_type, property_data in response_data["PropertyTypes"].items():
        properties = property_data.get("Properties")
        if resource_property_name == property_type and properties:
            sorted_properties = sorted(properties)
            last_property = sorted_properties[-1]

            for updated_counter, property in enumerate(
                sorted_properties, start=counter
            ):
                property_info = properties[property]
                item = get_item_type(property_info)
                is_last = property == last_property

                if "Type" in property_info:
                    if property_info["Type"] == "List":
                        body.extend(
                            [
                                f'{" " * indent}"{property}": []'
                                + ("," if not is_last else ""),
                                # f'{" " * (indent + 2)}{{',
                            ]
                        )
                    elif property == (property_info["Type"] or None):
                        continue
                else:
                    set_value_type_json(
                        body,
                        property,
                        item,
                        updated_counter,
                        indent=indent,
                        is_last=is_last,
                    )

                # if property == last_property:
                #     body.append(
                #         f'{" " * (indent + 2)}}}{"," if property != last_property else ""}'
                #     )
            body.append(f'{" " * 4 }}}{"," if resource_type != last_property else ""}')
            break

    return body


def set_value_type_json(body, property, item, counter, indent, is_last=False):
    value_type = {
        "Boolean": "|false,true|",
        "Double": ":Number",
        "Integer": ":Number",
        "Json": ":JSON",
        "Long": ":Number",
        "String": ":String",
        "Timestamp": ":Timestamp",
    }

    if item in value_type:
        prefix = f"${{{counter}{value_type[item]}}}"
        prefix = f'"{prefix}"'
        body.append(
            f'{" " * indent}"{property}": {prefix}' + ("," if not is_last else "")
        )
    else:
        print(f"This property: {property} has an unsupported value: {item}")

    return body


def fetch_description(resource_type):
    description = [resource_type["Documentation"].replace("http://", "https://")]

    if "Attributes" in resource_type:
        attributes = "\n".join(
            f"  {attribute}" for attribute in resource_type["Attributes"]
        )
        description.append(f"Attributes:\n{attributes}")

    return description


def process_resource_type(resource_type, resource_data, output_format):
    prefix = resource_type.replace("AWS::", "").replace("::", "-")
    description = fetch_description(resource_data)
    resource_properties = resource_data["Properties"]

    updated_body = []
    if output_format == "yaml":
        body = ["${1:LogicalID}:", f"  Type: {resource_type}", "  Properties:"]
        for counter, resource_property in enumerate(
            sorted(resource_properties), start=2
        ):
            updated_body = parse_body_yaml(
                body, counter, resource_properties, resource_property, resource_type
            )
    elif output_format == "json":
        body = [
            '"${1:LogicalID}": {',
            f'  "Type": "{resource_type}",',
            f'  "Properties": {{',
        ]
        for counter, resource_property in enumerate(
            sorted(resource_properties), start=2
        ):
            updated_body = parse_body_json(
                body, counter, resource_properties, resource_property, resource_type
            )
        updated_body.append("  }")
        updated_body.append("}")

    return resource_type, {
        "body": updated_body,
        "description": description,
        "prefix": prefix.lower(),
        "scope": "json" if output_format == "json" else "yaml",
    }


def create_cfn_snippet(
    cloudformation_resource_spec, local_path=None, output_format="yaml"
):
    output = {}
    resource_types = cloudformation_resource_spec["ResourceTypes"]

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(
                process_resource_type, resource_type, resource_data, output_format
            )
            for resource_type, resource_data in resource_types.items()
        ]

        for future in concurrent.futures.as_completed(futures):
            resource_type, result = future.result()
            output[resource_type] = result

    output_file_name = (
        f"resource-types-{output_format}-test.json"
        if local_path
        else f"resource-types-{output_format}.json"
    )

    snippet_directory = f"{os.getcwd()}/snippets"
    output_file_path = os.path.join(snippet_directory, output_file_name)

    print(f"Saving snippets in: {output_file_path}")
    with open(output_file_path, "w") as file:
        file.write(json.dumps(output, sort_keys=True, indent=4))


if __name__ == "__main__":
    # Load the current hash
    with open("src/current-json-spec-hash", "r+") as file:
        current_hash = file.read()
        # Load the source data and hash it
        new_hash = hashlib.md5(
            json.dumps(get_resource_spec()).encode("utf-8")
        ).hexdigest()

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

            cloudformation_resource_spec = get_resource_spec(args.local_path)
            create_cfn_snippet(
                cloudformation_resource_spec, args.local_path, args.output_format
            )
