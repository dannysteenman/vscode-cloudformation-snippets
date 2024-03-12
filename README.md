# CloudFormation Snippets for VS Code

[![Version](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cloudformation-yaml-snippets 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/dannysteenman.cloudformation-yaml-snippets 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![Rating](https://img.shields.io/visual-studio-marketplace/stars/dannysteenman.cloudformation-yaml-snippets)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)

This extension adds snippets for all the AWS CloudFormation resources into Visual Studio Code.

> [!TIP]
> If you're looking for expertise to elevate your cloud infrastructure, then don't hesitate to get in [touch with me](https://towardsthecloud.com/contact)!
>
> <details><summary>📚 <strong>Discover more about us</strong></summary>
>
> <br/>
>
> Towards the Cloud is a one-person agency with over 9 years of extensive hands-on experience in architecting and building highly scalable distributed systems on AWS Cloud using Infrastructure as Code for startups and enterprises.
>
> *Maximize your development speed by harnessing our expertise in crafting high-performance Cloud infrastructures.*
>
> #### Why Choose Towards the Cloud?
>
> - **Expertise in AWS CDK**: Leverage the full power of AWS Cloud Development Kit (AWS CDK) with our deep expertise. We architect and build infrastructure as code (IaC) solutions that are maintainable, scalable, and fully automated.
> - **Tailored Solutions**: Your business is unique, and so are your cloud needs. We provide personalized consultations and solutions tailored to perfectly align with your project requirements and business goals.
> - **Cost-Effective and Efficient**: Benefit from our streamlined processes and deep AWS knowledge to optimize costs without compromising on performance or security.
> - **One-on-One Attention**: As a one-person agency, Towards the Cloud guarantees you receive dedicated support and expertise directly from an AWS Cloud Engineer. This ensures high-quality deliverables and swift decision-making.<br/>
> - **Seamless CI/CD**: Empower your team to manage infrastructure changes confidently and efficiently through Pull Requests, leveraging the full power of GitHub Actions.
>
> <a href="https://towardsthecloud.com/contact"><img alt="Schedule introduction call" src="https://img.shields.io/badge/schedule%20introduction%20call-success.svg?style=for-the-badge"/></a>
> </details>

---

## New in version 4!

- Support for CloudFormation resource type snippets in JSON format! This means you can now generate CloudFormation resource type snippets in both YAML and JSON formats!
  - To get started: Open up a JSON file, type an AWS Resource `prefix` in the same manner as you do for the YAML snippets and it will show the autocomplete!


## Features

1. Supports all resources that are defined by CloudFormation
2. CloudFormation autocompletion for every resource (includes properties) in both YAML and JSON formats.
3. The CloudFormation snippets are automatically updated every week after AWS updates their [CloudFormation Resource Specification.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
4. Intrinsic functions + conditions are supported.
5. Contains a whole bunch of parameter types.
6. Has builtin support for placeholders. This means you can quickly jump from property to property in each resource by using `Tab`
7. Every resource type contains the matching documentation URL in its description.
8. Support for [Gitpod](https://github.com/dannysteenman/vscode-cloudformation-snippets/issues/14) by publishing this extension to the [Open VSX Registry](https://open-vsx.org/extension/dsteenman/cloudformation-yaml-snippets)

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
