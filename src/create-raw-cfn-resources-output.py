import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict

import requests

CFN_RESOURCE_SPEC_URL = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"

# Thread-safe printing
log_lock = threading.Lock()


def safe_print(*args, **kwargs):
    with log_lock:
        print(*args, **kwargs)


class RawResourceParser:
    def parse_resource(self, resource_type: str, resource_data: Dict[str, Any]) -> Dict[str, Any]:
        properties = self._parse_properties(resource_data.get("Properties", {}))
        return {"Properties": properties, "Docs": resource_data["Documentation"]}

    def _parse_properties(self, properties: Dict[str, Any]) -> Dict[str, str]:
        result = {}
        for prop, prop_info in properties.items():
            prop_type = self._get_property_type(prop_info)
            result[prop] = prop_type
        return result

    @staticmethod
    def _get_property_type(prop_info: Dict[str, Any]) -> str:
        if "Type" in prop_info:
            if prop_info["Type"] == "List":
                if "ItemType" in prop_info:
                    return f"{prop_info['ItemType']}"
                elif "PrimitiveItemType" in prop_info:
                    return f"{prop_info['PrimitiveItemType']}"
                else:
                    return "List"
            return prop_info["Type"]
        elif "PrimitiveType" in prop_info:
            return prop_info["PrimitiveType"]
        else:
            return "Unknown"


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process CloudFormation Resource Specification")
    parser.add_argument(
        "--local",
        dest="local_path",
        help="Path to local JSON resource specification file (optional)",
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


def process_resource_type(resource_type: str, resource_data: Dict[str, Any]) -> tuple:
    parser = RawResourceParser()
    parsed_resource = parser.parse_resource(resource_type, resource_data)
    safe_print(f"Finished processing {resource_type}")
    return resource_type, parsed_resource


def create_raw_cfn_output(cloudformation_resource_spec: Dict[str, Any], local_path: str = None) -> None:
    output = {}
    resource_types = cloudformation_resource_spec["ResourceTypes"]

    safe_print(f"Total number of resource types: {len(resource_types)}")

    with ThreadPoolExecutor() as executor:
        future_to_resource = {
            executor.submit(process_resource_type, resource_type, resource_data): resource_type
            for resource_type, resource_data in resource_types.items()
        }

        for future in as_completed(future_to_resource):
            resource_type = future_to_resource[future]
            try:
                result = future.result()
                output[resource_type] = result[1]
            except Exception as exc:
                safe_print(f"{resource_type} generated an exception: {exc}")

    if local_path:
        output_directory = os.path.join(os.getcwd(), ".vscode-test")
        output_file_name = "raw-cfn-resources-test-output.json"
    else:
        output_directory = os.path.join(os.getcwd(), "snippets")
        output_file_name = "raw-cfn-resources-output.json"

    os.makedirs(output_directory, exist_ok=True)
    output_file_path = os.path.join(output_directory, output_file_name)

    safe_print(f"Saving raw output in: {output_file_path}")
    with open(output_file_path, "w") as file:
        json.dump(output, file, sort_keys=True, indent=2)


def main():
    args = parse_arguments()
    cloudformation_resource_spec = get_resource_spec(args.local_path)
    create_raw_cfn_output(cloudformation_resource_spec, args.local_path)


if __name__ == "__main__":
    main()
