# CloudFormation Snippets for VS Code

[![Version](https://vsmarketplacebadge.apphb.com/version/dannysteenman.cloudformation-yaml-snippets.svg 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![Installs](https://vsmarketplacebadge.apphb.com/installs-short/dannysteenman.cloudformation-yaml-snippets.svg 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![Rating](https://vsmarketplacebadge.apphb.com/rating-star/dannysteenman.cloudformation-yaml-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)

This extension adds snippets for all the AWS CloudFormation resources into Visual Studio Code.

---

## New

- Added support for [Gitpod](https://github.com/dannysteenman/vscode-cloudformation-snippets/issues/14) by publishing this extension to the [Open VSX Registry](https://open-vsx.org/extension/dsteenman/cloudformation-yaml-snippets)


## Features

1. Supports all resources that are defined by CloudFormation
2. CloudFormation autocompletion for every resource (includes properties).
3. The CloudFormation snippets are automatically updated every week after AWS updates their [CloudFormation Resource Specification.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
4. Intrinsic functions + conditions are supported.
5. Contains a whole bunch of parameter types.
6. Has builtin support for placeholders. This means you can quickly jump from property to property in each resource by using `Tab`
7. Every resource type contains the matching documentation URL in its description.

## Usage

* **Step 1.** Install this extension
* **Step 2.** create a `.yml` file to start working on CloudFormation
* **Step 3.** Check in the bottom right-hand corner of the VS Code editor that the file type is listed as "YAML".
* **Step 4.** To start with the basic template structure, type **cfn** to get the YAML formatted template fragment.
* **Step 5.** Start adding resources in the resource section by using their prefix name e.g. ```autoscaling-autoscalinggroup``` equals resource type ```AWS::AutoScaling::AutoScalingGroup```

![CloudFormation Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cloudformation-snippets/main/images/cfn-snippets-extension-example.gif)

> **Note:** Once you start typing a prefix (explained in step 5), the corresponding snippet will show up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 5).

---
## AWS CloudFormation Attributes (GetAtt) Cheat Sheet

It can be difficult to find out which attributes are available for each AWS CloudFormation resource type. Therefore I made an [AWS CloudFormation Attributes cheat sheet](https://towardsthecloud.com/aws-cloudformation-resource-attributes) that lists the attributes in a single table overview to easily find the attributes.

---
## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dannysteenman/vscode-cloudformation-snippets/issues)

## Contributing

If you want to add more snippets, your contribution is more than welcome!

Review the [Contributing Guidelines](https://github.com/dannysteenman/vscode-cloudformation-snippets/blob/main/.github/CONTRIBUTING.md).

---
## Author

**[Danny Steenman](https://towardsthecloud.com)**

<p align="left">
  <a href="https://twitter.com/dannysteenman"><img src="https://img.shields.io/twitter/follow/dannysteenman?label=%40dannysteenman&style=social"></a>
</p>

## Support my work

If you found this VS Code extension helpful, please consider showing your support by buying me a coffee.

<a href="https://www.buymeacoffee.com/dannysteenman" target="_blank"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=dannysteenman&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff"></a>
