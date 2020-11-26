# CloudFormation YAML snippets for VS Code

[![Marketplace Version](https://vsmarketplacebadge.apphb.com/version/dsteenman.cloudformation-yaml-snippets.svg 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Current Installs](https://vsmarketplacebadge.apphb.com/installs-short/dsteenman.cloudformation-yaml-snippets.svg 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Rating](https://vsmarketplacebadge.apphb.com/rating-star/dsteenman.cloudformation-yaml-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)

A [Visual Studio Code](https://code.visualstudio.com/) [extension](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets) which contains the complete YAML snippet library for CloudFormation based on the [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)

## New (Nov 2020)

* Added a placeholder functionality so you can quickly jump to the next placeholder in the properties section with `Tab`.
* Added the matching documentation urls in the description of every resource type.

## Features

1. This extension is automatically updated every week when AWS releases/updates CloudFormation resources.
2. It supports all resource types which are available in CloudFormation.
3. Intrinsic functions + conditions are supported.
4. Contains a whole bunch of parameter types.
5. Quickly update the properties of the resource type using `Tab`.
6. Every resource type contains the matching documentation url in it's description.

## Usage

* **Step 1.** Install this extension
* **Step 2.** create a `.yml` file to start working on CloudFormation
* **Step 3.** Check in the bottom right hand corner of the VSCode editor that the file type is listed as "YAML".
* **Step 4.** To start out with the basic template structure, type **cfn** to get the YAML formatted template fragment.
* **Step 5.** Start adding adding resources in the resource section by using their prefix name e.g. ```autoscaling-autoscalinggroup``` equals resource type ```AWS::AutoScaling::AutoScalingGroup```

> **Note:** Once you start typing resource types, the corresponding snippet will show-up in the drowndown window. If this doesn't happen automatically press `ctrl + space` to invoke intellisense and search for the prefix of the resource type that you want to add (as listed in step 5).

![CFN YAML snippet example](https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/images/cfn-yaml-snippet-example.gif)

---

## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dsteenman/cloudformation-yaml-snippets/issues)

## Tips and tricks

 If you want to boost your productivity even more with VS Code and CloudFormation. Check [this article](https://dannys.cloud/level-up-cloudformation-with-vs-code) I wrote to help you level up your templating game!
<br>
<br>

---
<br>

 <p align='center'>
 <a href="https://dannys.cloud"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/icon/homepage.png"></a>&nbsp;&nbsp;
<a href="https://dev.to/dsteenman"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/icon/devto.png"></a>&nbsp;&nbsp;
<a href="https://twitter.com/dannysteenman"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/icon/twitter.png"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/dannysteenman/"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/master/icon/linkedin.png"></a>
</p>
