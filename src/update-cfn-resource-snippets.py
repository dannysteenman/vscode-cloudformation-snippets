#!/usr/bin/env python3
######################
# Azure pipeline runs on a schedule
# We get md5 hash of Amazon's spec file and compare to previous hash stored in file
# If it matches, exit 1 thus blocking the pipeline from continuing
# If it doesn't, update the file and git the file so next run will/won't be blocked

import hashlib
import json
import requests
import sys

# Specs from us-east-1 https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html
url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"


def check_for_update(url):
    hash_file = "src/current-json-spec-hash"

    # Load the source data and hash it
    response = requests.get(url)
    new_hash = hashlib.md5(response.content).hexdigest()

    # Load the current hash
    with open(hash_file, 'r') as text_file:
        old_hash = text_file.read()

    # If we match previous run, die (blocking the pipeline)
    if new_hash == old_hash:
        print("Hash matches, the snippets are up-to-date")
        exit(1)
        return True
    else:
        print("Going to download the latest resource specification from AWS and publish to vsce")
        with open(hash_file, "w") as text_file:
            text_file.write(new_hash)
        create_cfn_snippet(url)
        return False
# print("Hashes did not match, update git")
# echo out new hash so pipeline script can update azure variable


def create_cfn_snippet(url):
    output_file = "snippets/resource-types.json"
    # specs from us-east-1 https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html
    url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"

    # Load the source data:

    r = requests.get(url)
    data = r.json()

    # Start the output data

    output = {}

    # Add the resources to the output

    for d in data['ResourceTypes']:

        prefix = d.replace('AWS::', "")
        prefix = prefix.replace('::', "-")
        prefix = prefix.lower()

        body = ""
        description = ""
        scope = "source.cloudformation"

        body = body + ('${1:LogicalID}:\r\n')

        # add a name placeholder
        body = body + ('\tType: \"' + d + '\"\r\n')
        body = body + ("\tProperties:\r\n")

        description = "Attributes:\r\n"
        if 'Attributes' in data['ResourceTypes'][d]:
            for a in data['ResourceTypes'][d]['Attributes']:
                # description = description + "Attributes: " + "\r\n\t" + a
                description = description + "  " + a + "\r\n"
        else:
            description = "No Attributes\r\n"

        # for each resources 'properties':
        for p in data['ResourceTypes'][d]['Properties']:

            required = data['ResourceTypes'][d]['Properties'][p]['Required']

            item = ""
            itemList = 0

            if ('PrimitiveType' in data['ResourceTypes'][d]['Properties'][p]):
                item = data['ResourceTypes'][d]['Properties'][p]['PrimitiveType']

            if ('PrimitiveItemType' in data['ResourceTypes'][d]['Properties'][p]):
                item = data['ResourceTypes'][d]['Properties'][p]['PrimitiveItemType']

            if ('ItemType' in data['ResourceTypes'][d]['Properties'][p]):
                item = data['ResourceTypes'][d]['Properties'][p]['ItemType']

            if ('Type' in data['ResourceTypes'][d]['Properties'][p]):
                if (data['ResourceTypes'][d]['Properties'][p]['Type'] == "List"):
                    itemList = 1
                else:
                    itemList = 2
                    item = data['ResourceTypes'][d]['Properties'][p]['Type']

            ###########################

            if (itemList == 0):
                body = body + ("\t\t" + p + ": " + item + "")
                if (required):
                    body = body + (" #required\r\n")
                else:
                    body = body + ("\r\n")

            elif (itemList == 1):
                body = body + ("\t\t" + p + ":" + "")
                if (required):
                    body = body + (" #required\r\n")
                else:
                    body = body + ("\r\n")

                body = body + ("\t\t\t- " + item + "\r\n")

            elif (itemList == 2):
                body = body + ("\t\t" + p + ":" + "")
                if (required):
                    body = body + (" #required\r\n")
                else:
                    body = body + ("\r\n")

                body = body + ("\t\t\t" + item + "\r\n")

            output[d] = {"prefix": prefix, "body": body,
                         "description": description}

    with open(output_file, "w") as text_file:
        text_file.write(json.dumps(output, indent=4))


# Run cfn resource updater
if __name__ == "__main__":
    check_for_update(url)
