# Cloudformation YAML snippets for VS Code

[![Marketplace Version](https://vsmarketplacebadge.apphb.com/version/dsteenman.cloudformation-yaml-snippets.svg 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Current Installs](https://vsmarketplacebadge.apphb.com/installs-short/dsteenman.cloudformation-yaml-snippets.svg 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Build Status](https://dev.azure.com/dsteenman/Cloudformation%20YAML%20Snippets%20for%20VS%20Code/_apis/build/status/dsteenman.cloudformation-yaml-snippets?branchName=master)](https://dev.azure.com/dsteenman/Cloudformation%20YAML%20Snippets%20for%20VS%20Code/_build/latest?definitionId=1&branchName=master)

A [Visual Studio Code](https://code.visualstudio.com/) [extension](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets) which contains the complete YAML snippet library for Cloudformation based on the AWS CloudFormation Resource Specification.

## Features

You now have access to all available resources provided by [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html) in the form of YAML snippets!

## Usage

* **Step 1.** Install the extension
* **Step 2.** create a YAML file for to start working on Cloudformation
* **Step 3.** Type **cfn** to get the basic template in which you can add your resources
* **Step 4.** Start adding adding resources by using their prefix name e.g. ```autoscaling-autoscalinggroup``` equals resource type ```AWS::AutoScaling::AutoScalingGroup```

> **Note:** Once you start typing resource types, the corresponding snippet will show-up in the drowndown window.

![CFN YAML snippet example](https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/images/cfn-yaml-snippet-example.gif)

---

## Credits

The YAML snippets were generated using the following script: [Github](https://github.com/mikegchambers/cfn-yaml-snippet)

## Legal

All content of the YAML file has copyright by Amazon Web Services, Inc. or its
affiliates, and was published under the terms that can be found at
https://aws.amazon.com/terms/

[Resource Types Reference]: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html
