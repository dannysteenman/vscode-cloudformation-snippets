import hashlib

import requests


def get_resource_spec():
    cfn_resource_spec_url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
    # Load the source data and hash it
    response = requests.get(cfn_resource_spec_url)

    return response


# Load the current hash
with open("src/current-cfn-spec-hash", "r+") as file:
    current_hash = file.read()
    # Load the source data and hash it
    new_hash = hashlib.md5(get_resource_spec().content).hexdigest()

    if new_hash == current_hash:
        print(f"The new hash: {new_hash} matches with our current hash: {current_hash}.")
        print("The snippets are up-to-date, stopping the pipeline.")
        exit(1)
    else:
        print(
            f"Found an update in the cfn-resource-specification, let's update the hash to: {new_hash}"
            " and continue with updating the cfn resource snippets!"
        )
        file.seek(0)
        file.write(new_hash)
