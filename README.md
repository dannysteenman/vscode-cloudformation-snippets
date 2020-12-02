# CloudFormation Resource Snippets for VSCode

[![Marketplace Version](https://vsmarketplacebadge.apphb.com/version/dsteenman.cloudformation-yaml-snippets.svg 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Current Installs](https://vsmarketplacebadge.apphb.com/installs-short/dsteenman.cloudformation-yaml-snippets.svg 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)
[![Rating](https://vsmarketplacebadge.apphb.com/rating-star/dsteenman.cloudformation-yaml-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets)

This [VSCode extension](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets) adds autocompletion for all the resources that AWS CloudFormation supports. It get's updated automatically every week by fetching the resources from the official [AWS CloudFormation resource specification.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)

## New (Nov 2020)

* Added a placeholder functionality so you can quickly jump to the next placeholder in the properties section with `Tab`.
* Added matching documentation URLs in the description of every resource type.

## Features

1. This extension contains snippets for all available CloudFormation resources
2. CloudFormation autocompletion for every resource (includes properties).
3. Automatically updated every week after AWS updates their CloudFormation Resource Specification.
4. Intrinsic functions + conditions are supported.
5. Contains a whole bunch of parameter types.
6. Quickly update the properties of each resource type using `Tab`.
7. Every resource type contains the matching documentation URL in its description.

## Usage

* **Step 1.** Install this extension
* **Step 2.** create a `.yml` file to start working on CloudFormation
* **Step 3.** Check in the bottom right-hand corner of the VSCode editor that the file type is listed as "YAML".
* **Step 4.** To start with the basic template structure, type **cfn** to get the YAML formatted template fragment.
* **Step 5.** Start adding resources in the resource section by using their prefix name e.g. ```autoscaling-autoscalinggroup``` equals resource type ```AWS::AutoScaling::AutoScalingGroup```

> **Note:** Once you start typing a prefix (explained in step 5), the corresponding snippet will show up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 5).

![CFN YAML snippet example](https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/main/images/cfn-yaml-snippet-example.gif)

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
 <a href="https://dannys.cloud"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/main/icon/homepage.png"></a>&nbsp;&nbsp;
<a href="https://dev.to/dsteenman"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/main/icon/devto.png"></a>&nbsp;&nbsp;
<a href="https://twitter.com/dannysteenman"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/main/icon/twitter.png"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/dannysteenman/"><img height="30" src="https://raw.githubusercontent.com/dsteenman/cloudformation-yaml-snippets/main/icon/linkedin.png"></a>
</p>
