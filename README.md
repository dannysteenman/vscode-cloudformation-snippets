# CloudFormation YAML snippets for VS Code

[![Marketplace Version](https://vsmarketplacebadge.apphb.com/version/dsteenman.cloudformation-yaml-snippets.svg 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Current Installs](https://vsmarketplacebadge.apphb.com/installs-short/dsteenman.cloudformation-yaml-snippets.svg 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Build Status](https://dev.azure.com/dsteenman/Cloudformation%20YAML%20Snippets%20for%20VS%20Code/_apis/build/status/dsteenman.cloudformation-yaml-snippets?branchName=master)](https://dev.azure.com/dsteenman/Cloudformation%20YAML%20Snippets%20for%20VS%20Code/_build/latest?definitionId=1&branchName=master)

A [Visual Studio Code](https://code.visualstudio.com/) [extension](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets) which contains the complete YAML snippet library for CloudFormation based on the [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)

## New

* You can now use intrinsic functions snippets with this plugin in VS Code
* Same goes for condition functions.

## Features

1. This extension is automatically updated every week when AWS releases/updates CloudFormation resources.
2. It supports all resource types which are available in CloudFormation
3. Intrinsic functions + conditions are supported
4. Contains a whole bunch of parameter types

## Usage

* **Step 1.** Install the extension
* **Step 2.** create a YAML file to start working on CloudFormation
* **Step 3.** Type **cfn** to get the basic template in which you can add your resources
* **Step 4.** Start adding adding resources by using their prefix name e.g. ```autoscaling-autoscalinggroup``` equals resource type ```AWS::AutoScaling::AutoScalingGroup```

> **Note:** Once you start typing resource types, the corresponding snippet will show-up in the drowndown window.

![CFN YAML snippet example](https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/images/cfn-yaml-snippet-example.gif)

---

## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dsteenman/cloudformation-yaml-snippets/issues)

## Tips and tricks

 If you want to boost your productivity even more with VS Code and CloudFormation. Check [this article](https://dannys.cloud/level-up-cloudformation-with-vs-code) I wrote to help you level up your templating game!

## Legal

All content of the YAML file has copyright by Amazon Web Services, Inc. or its
affiliates, and was published under the terms that can be found at
https://aws.amazon.com/terms/

[Resource Types Reference]: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html
