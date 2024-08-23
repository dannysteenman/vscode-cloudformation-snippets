import hashlib
from datetime import datetime, timezone

import requests


def get_resource_spec():
    # Add a cache buster using a timezone-aware datetime object
    cfn_resource_spec_url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
    current_time = datetime.now(timezone.utc).timestamp()
    response = requests.get(cfn_resource_spec_url, params={"nocache": current_time})
    response.raise_for_status()
    return response


def calculate_hash(content):
    return hashlib.sha256(content).hexdigest()


# Load the current hash
with open("src/current-cfn-spec-hash", "r+") as file:
    current_hash = file.read().strip()
    new_hash = calculate_hash(get_resource_spec().content)

    if new_hash == current_hash:
        print(f"The new hash: {new_hash} matches with our current hash: {current_hash}.")
        print("The snippets are up-to-date, stopping the pipeline.")
        exit(1)
    else:
        print(
            f"Found an update in the cfn-resource-specification, let's update the hash to: {new_hash} "
            "and continue with updating the cfn resource snippets!"
        )
        file.seek(0)
        file.write(new_hash)
        file.truncate()
