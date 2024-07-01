import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List

import requests

CFN_RESOURCE_SPEC_URL = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
REDUCED_DEPTH = 4
MAX_DEPTH = 10
MAX_LINES = 400
VALUE_TYPE_MAP = {
    "Boolean": "|false,true|",
    "Double": ":Number",
    "Integer": ":Number",
    "Json": ":JSON",
    "Long": ":Number",
    "String": ":String",
    "Timestamp": ":Timestamp",
}

# Thread-safe printing
log_lock = threading.Lock()


def safe_print(*args, **kwargs):
    with log_lock:
        print(*args, **kwargs)


class ResourceParser:
    def __init__(self, output_format: str, max_depth: int):
        self.output_format = output_format
        self.counter = [1]
        self.nested_types = set()
        self.max_depth = max_depth

    def parse_body(
        self, resource_properties: Dict[str, Any], resource_type: str, response_data: Dict[str, Any]
    ) -> List[str]:
        body = self._init_body(resource_type)
        self.counter[0] = 1
        return getattr(self, f"_parse_body_{self.output_format}")(
            body, resource_properties, resource_type, response_data
        )

    def _init_body(self, resource_type: str) -> List[str]:
        if self.output_format == "yaml":
            return ["${1:LogicalID}:", f"  Type: {resource_type}", "  Properties:"]
        else:
            return ['"${1:LogicalID}": {', f'  "Type": "{resource_type}",', '  "Properties": {']

    def _parse_body_yaml(
        self, body: List[str], resource_properties: Dict[str, Any], resource_type: str, response_data: Dict[str, Any]
    ) -> List[str]:
        for resource_property, property_info in sorted(resource_properties.items()):
            required = property_info.get("Required", False)
            item = self._get_item_type(property_info)

            if "Type" in property_info:
                if property_info["Type"] == "List":
                    body.append(f"    {resource_property}: {'# Required' if required else ''}")
                    if item != "Tag":
                        body.append("      -")
                    self._get_item_type_prop(
                        body,
                        property_info.get("ItemType", item),
                        resource_type,
                        response_data,
                        indent=8,
                        first_item=True,
                    )
                else:
                    body.append(f"    {resource_property}:")
                    self._get_item_type_prop(body, property_info["Type"], resource_type, response_data, indent=6)
            else:
                self._set_value_type(body, resource_property, item, required, indent=4)

        return body

    def _parse_body_json(
        self, body: List[str], resource_properties: Dict[str, Any], resource_type: str, response_data: Dict[str, Any]
    ) -> List[str]:
        for idx, (resource_property, property_info) in enumerate(sorted(resource_properties.items())):
            required = property_info.get("Required", False)
            item = self._get_item_type(property_info)
            is_last = idx == len(resource_properties) - 1

            if "Type" in property_info:
                if property_info["Type"] == "List":
                    line = f'    "{resource_property}": ['
                    if required:
                        line += " // Required"
                    body.append(line)
                    if item != "Tag":
                        body.append("      {")
                    self._get_item_type_prop(
                        body,
                        property_info.get("ItemType", item),
                        resource_type,
                        response_data,
                        indent=8,
                        first_item=True,
                    )
                    if item != "Tag":
                        body.append("      }")
                    body.append("    ]" + ("" if is_last else ","))
                else:
                    line = f'    "{resource_property}": {{'
                    if required:
                        line += " // Required"
                    body.append(line)
                    self._get_item_type_prop(body, property_info["Type"], resource_type, response_data, indent=6)
                    body.append("    }" + ("" if is_last else ","))
            else:
                self._set_value_type(body, resource_property, item, required, indent=4, is_last=is_last)

        body.append("  }")
        body.append("}")
        return body

    def _get_item_type_prop(
        self,
        body: List[str],
        item: str,
        resource_type: str,
        response_data: Dict[str, Any],
        indent: int = 6,
        first_item: bool = False,
        depth: int = 0,
    ) -> List[str]:
        if depth >= self.max_depth:
            return body

        resource_property_name = f"{resource_type}.{item}"

        # Avoid nested repetition of props
        if resource_property_name in self.nested_types:
            if self.output_format == "yaml":
                if body[-1].strip() == "-":
                    body[-1] = f"{body[-1].rstrip()} Children: # Nested repetition"
            else:
                body.append(f'{" " * indent}"Children": "# Nested repetition",')
            return body

        self.nested_types.add(resource_property_name)

        if resource_property_name in response_data.get("PropertyTypes", {}):
            properties = response_data["PropertyTypes"][resource_property_name].get("Properties", {})
            for idx, (property, property_info) in enumerate(sorted(properties.items())):
                is_last = idx == len(properties) - 1
                item_type = self._get_item_type(property_info)

                if "Type" in property_info:
                    if property_info["Type"] == "List":
                        self._handle_list_type(
                            body,
                            property,
                            property_info,
                            resource_type,
                            response_data,
                            indent,
                            first_item,
                            depth,
                            is_last,
                        )
                    elif property_info["Type"] == "Map":
                        self._handle_map_type(body, property, indent, is_last)
                    else:
                        self._handle_other_type(
                            body,
                            property,
                            property_info,
                            resource_type,
                            response_data,
                            indent,
                            first_item,
                            depth,
                            is_last,
                        )
                else:
                    self._set_value_type(body, property, item_type, None, indent, first_item, is_last)
                first_item = False
        elif item == "Tag":
            self._handle_tag_type(body, indent)
        else:
            self._set_value_type(body, "", item, None, indent, first_item, True)

        self.nested_types.remove(resource_property_name)
        return body

    def _handle_list_type(
        self,
        body: List[str],
        property: str,
        property_info: Dict[str, Any],
        resource_type: str,
        response_data: Dict[str, Any],
        indent: int,
        first_item: bool,
        depth: int,
        is_last: bool,
    ):
        if self.output_format == "yaml":
            if first_item:
                body[-1] += f" {property}:"
            else:
                body.append(f"{' ' * indent}{property}:")
            body.append(f"{' ' * (indent + 2)}-")
            if property_info.get("ItemType"):
                self._get_item_type_prop(
                    body,
                    property_info["ItemType"],
                    resource_type,
                    response_data,
                    indent=indent + 4,
                    first_item=True,
                    depth=depth + 1,
                )
            else:
                self._set_value_type(
                    body, "", property_info.get("PrimitiveItemType", ""), None, indent=indent + 4, first_item=True
                )
        else:
            body.append(f'{" " * indent}"{property}": [')
            if property_info.get("PrimitiveItemType") in ["String", "Integer", "Boolean"]:
                self._set_value_type(
                    body, "", property_info["PrimitiveItemType"], None, indent=indent + 2, is_last=True
                )
            else:
                body.append(f"{' ' * (indent + 2)}{{")
                if property_info.get("ItemType"):
                    self._get_item_type_prop(
                        body,
                        property_info["ItemType"],
                        resource_type,
                        response_data,
                        indent=indent + 4,
                        first_item=True,
                        depth=depth + 1,
                    )
                else:
                    self._set_value_type(
                        body,
                        "",
                        property_info.get("PrimitiveItemType", ""),
                        None,
                        indent=indent + 4,
                        first_item=True,
                        is_last=True,
                    )
                body.append(f"{' ' * (indent + 2)}}}")
            body.append(f"{' ' * indent}]" + ("" if is_last else ","))

    def _handle_map_type(self, body: List[str], property: str, indent: int, is_last: bool):
        if self.output_format == "yaml":
            body.append(f"{' ' * indent}{property}:")
            self._set_value_type(body, "", "Json", None, indent=indent + 2, first_item=False)
        else:
            body.append(f'{" " * indent}"{property}": {{')
            self._set_value_type(body, "key", "String", None, indent=indent + 2, is_last=False)
            self._set_value_type(body, "value", "String", None, indent=indent + 2, is_last=True)
            body.append(f"{' ' * indent}}}" + ("" if is_last else ","))

    def _handle_other_type(
        self,
        body: List[str],
        property: str,
        property_info: Dict[str, Any],
        resource_type: str,
        response_data: Dict[str, Any],
        indent: int,
        first_item: bool,
        depth: int,
        is_last: bool,
    ):
        if self.output_format == "yaml":
            if first_item:
                body[-1] += f" {property}:"
            else:
                body.append(f"{' ' * indent}{property}:")
            self._get_item_type_prop(
                body, property_info["Type"], resource_type, response_data, indent=indent + 2, depth=depth + 1
            )
        else:
            body.append(f'{" " * indent}"{property}": {{')
            self._get_item_type_prop(
                body, property_info["Type"], resource_type, response_data, indent=indent + 2, depth=depth + 1
            )
            body.append(f"{' ' * indent}}}" + ("" if is_last else ","))

    def _handle_tag_type(self, body: List[str], indent: int):
        if self.output_format == "yaml":
            body.append(f"{' ' * (indent-2)}- Key: \"${{{self._get_next_counter()}:String}}\"")
            body.append(f"{' ' * indent}Value: \"${{{self._get_next_counter()}:String}}\"")
        else:
            body.append(f'{" " * indent}{{')
            body.append(f'{" " * (indent + 2)}"Key": "${{{self._get_next_counter()}:String}}",')
            body.append(f'{" " * (indent + 2)}"Value": "${{{self._get_next_counter()}:String}}"')
            body.append(f'{" " * indent}}}')

    def _set_value_type(
        self,
        body: List[str],
        property: str,
        item: str,
        required: bool,
        indent: int,
        first_item: bool = False,
        is_last: bool = False,
    ) -> List[str]:
        if item in VALUE_TYPE_MAP:
            value_type = VALUE_TYPE_MAP[item]
            if value_type == ":Number":
                prefix = f'"${{{self._get_next_counter()}:Number}}"'
            else:
                prefix = f"${{{self._get_next_counter()}{value_type}}}"
                if item in ["String", "Json", "Timestamp"]:
                    prefix = f'"{prefix}"'

            if self.output_format == "yaml":
                if first_item:
                    body[-1] += f" {property}{': ' if property else ''}{prefix}"
                else:
                    body.append(f"{' ' * indent}{property}{':' if property else ''} {prefix}")
                if required:
                    body[-1] += " # Required"
            else:
                if property:
                    body.append(f'{" " * indent}"{property}": {prefix}' + ("" if is_last else ","))
                else:
                    body.append(f'{" " * indent}{prefix}' + ("" if is_last else ","))
                if required:
                    body[-1] += " // Required"
        else:
            if self.output_format == "yaml":
                body.append(f"{' ' * indent}{property}{':' if property else ''} ")
            else:
                body.append(f'{" " * indent}"{property}": null' + ("" if is_last else ","))

        return body

    @staticmethod
    def _get_item_type(resource_property: Dict[str, Any]) -> str:
        return resource_property.get(
            "PrimitiveItemType", resource_property.get("PrimitiveType", resource_property.get("ItemType"))
        )

    def _get_next_counter(self) -> int:
        self.counter[0] += 1
        return self.counter[0]


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process CloudFormation Resource Specification")
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
    return parser.parse_args()


def get_resource_spec(local_path: str = None) -> Dict[str, Any]:
    if local_path:
        abs_path = os.path.abspath(local_path)
        if os.path.exists(abs_path):
            with open(abs_path, "r") as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"File not found: {abs_path}")
    else:
        response = requests.get(CFN_RESOURCE_SPEC_URL)
        response.raise_for_status()
        return response.json()


def fetch_description(resource_type: Dict[str, Any]) -> List[str]:
    description = [resource_type["Documentation"].replace("http://", "https://")]

    if "Attributes" in resource_type:
        attributes = "\n".join(f"  {attribute}" for attribute in resource_type["Attributes"])
        description.append(f"Attributes:\n{attributes}")

    return description


def process_resource_type(
    resource_type: str, resource_data: Dict[str, Any], output_format: str, response_data: Dict[str, Any]
) -> tuple:
    prefix = resource_type.replace("AWS::", "").replace("::", "-")
    description = fetch_description(resource_data)
    resource_properties = resource_data.get("Properties", {})

    # First pass with maximum depth
    parser = ResourceParser(output_format, MAX_DEPTH)
    updated_body = parser.parse_body(resource_properties, resource_type, response_data)

    line_count = len(updated_body)
    safe_print(f"Resource type {resource_type} initially has {line_count} lines")

    if line_count > MAX_LINES:
        safe_print(
            f"Warning: {resource_type} exceeded the maximum number of lines ({MAX_LINES}). Reducing parsing depth to {REDUCED_DEPTH}."
        )
        # Second pass with reduced depth
        parser = ResourceParser(output_format, REDUCED_DEPTH)
        updated_body = parser.parse_body(resource_properties, resource_type, response_data)
        line_count = len(updated_body)
        safe_print(f"After depth reduction, {resource_type} now has {line_count} lines")

    safe_print(f"Finished processing {resource_type}")
    return resource_type, {
        "body": updated_body,
        "description": description,
        "prefix": prefix.lower(),
        "scope": "json" if output_format == "json" else "yaml",
    }


def create_cfn_snippet(
    cloudformation_resource_spec: Dict[str, Any], local_path: str = None, output_format: str = "yaml"
) -> None:
    output = {}
    resource_types = cloudformation_resource_spec["ResourceTypes"]

    safe_print(f"Total number of resource types: {len(resource_types)}")

    with ThreadPoolExecutor() as executor:
        future_to_resource = {
            executor.submit(
                process_resource_type, resource_type, resource_data, output_format, cloudformation_resource_spec
            ): resource_type
            for resource_type, resource_data in resource_types.items()
        }

        for future in as_completed(future_to_resource):
            resource_type = future_to_resource[future]
            try:
                result = future.result()
                output[resource_type] = result[1]
            except Exception as exc:
                safe_print(f"{resource_type} generated an exception: {exc}")

    output_file_name = (
        f"{output_format}-cfn-resource-types-test-output.json"
        if local_path
        else f"{output_format}-cfn-resource-types.json"
    )

    snippet_directory = f"{os.getcwd()}/test" if local_path else f"{os.getcwd()}/snippets"
    output_file_path = os.path.join(snippet_directory, output_file_name)

    os.makedirs(snippet_directory, exist_ok=True)

    safe_print(f"Saving snippets in: {output_file_path}")
    with open(output_file_path, "w") as file:
        json.dump(output, file, sort_keys=True, indent=4)


def main():
    args = parse_arguments()
    cloudformation_resource_spec = get_resource_spec(args.local_path)

    create_cfn_snippet(cloudformation_resource_spec, args.local_path, args.output_format)


if __name__ == "__main__":
    main()
