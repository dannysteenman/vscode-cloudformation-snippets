# AWS CloudFormation Snippets for VS Code

[![](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cloudformation-yaml-snippets?color=374151&label=Visual%20Studio%20Marketplace&labelColor=000&logo=visual-studio-code&logoColor=0098FF)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cloudformation-yaml-snippets?color=374151&label=Open%20VSX%20Registry&labelColor=000&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyB2aWV3Qm94PSI0LjYgNSA5Ni4yIDEyMi43IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Ik0zMCA0NC4yTDUyLjYgNUg3LjN6TTQuNiA4OC41aDQ1LjNMMjcuMiA0OS40em01MSAwbDIyLjYgMzkuMiAyMi42LTM5LjJ6IiBmaWxsPSIjYzE2MGVmIi8+CiAgPHBhdGggZD0iTTUyLjYgNUwzMCA0NC4yaDQ1LjJ6TTI3LjIgNDkuNGwyMi43IDM5LjEgMjIuNi0zOS4xem01MSAwTDU1LjYgODguNWg0NS4yeiIgZmlsbD0iI2E2MGVlNSIvPgo8L3N2Zz4=&logoColor=0098FF)](https://open-vsx.org/extension/dannysteenman/cloudformation-yaml-snippets)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/dannysteenman.cloudformation-yaml-snippets 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![Rating](https://img.shields.io/visual-studio-marketplace/stars/dannysteenman.cloudformation-yaml-snippets)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)

This CloudFormation Snippets extension equips Visual Studio Code with JSON and YAML snippets for **all** AWS CloudFormation and SAM resources - over 1250+ in total. It's your complete toolset for efficient CloudFormation template development.

> [!TIP]
> Struggling with AWS complexity or stuck on-premise? Let's transform your cloud journey.
>
> [Schedule a call with me](https://towardsthecloud.com/contact) to find out how I can enhance your existing AWS setup or guide your journey from on-premise to the Cloud.
>
> <details><summary>☁️ <strong>Discover more about my one-person business: Towards the Cloud</strong></summary>
>
> <br/>
>
> Hi, I'm Danny – AWS expert and founder of [Towards the Cloud](https://towardsthecloud.com). With over a decade of hands-on experience, I specialized myself in deploying well-architected, highly scalable and cost-effective AWS Solutions using Infrastructure as Code (IaC).
>
> #### When you work with me, you're getting a package deal of expertise and personalized service:
>
> - **AWS CDK Proficiency**: I bring deep AWS CDK knowledge to the table, ensuring your infrastructure is not just maintainable and scalable, but also fully automated.
> - **AWS Certified**: [Equipped with 7 AWS Certifications](https://www.credly.com/users/dannysteenman/badges), including DevOps Engineer & Solutions Architect Professional, to ensure best practices across diverse cloud scenarios.
> - **Direct Access**: You work with me, not a team of managers. Expect quick decisions and high-quality work.
> - **Tailored Solutions**: Understanding that no two businesses are alike, I Custom-fit cloud infrastructure for your unique needs.
> - **Cost-Effective**: I'll optimize your AWS spending without cutting corners on performance or security.
> - **Seamless CI/CD**: I'll set up smooth CI/CD processes using GitHub Actions, making changes a breeze through Pull Requests.
>
> *My mission is simple: I'll free you from infrastructure headaches so you can focus on what truly matters – your core business.*
>
> Ready to unlock the full potential of AWS Cloud?
>
> <a href="https://towardsthecloud.com/contact"><img alt="Schedule your call" src="https://img.shields.io/badge/schedule%20your%20call-success.svg?style=for-the-badge"/></a>
> </details>

---

## Features

1. **Comprehensive Coverage**: Offers snippets for **all** AWS CloudFormation and AWS SAM resources available - that's over 1250+ resources snippets at your fingertips!
2. **Complete Property Support**: Includes all nested properties for each resource, ensuring you have access to every configurable aspect of your AWS resources.
3. **Flexible Template Support**: Seamlessly works with both YAML and JSON CloudFormation templates.
4. **Efficient Autocomplete**: Simply type the resource name (e.g., `ec2-instance`) to instantly load the corresponding snippet for `AWS::EC2::Instance`.
5. **Rich Feature Set**: Incorporates intrinsic functions, conditions, and diverse parameter types for robust template creation.
6. **Enhanced Navigation**: Features placeholders that enable swift movement through resource properties.
7. **Resource Documentation**: Each snippet is linked to its official AWS documentation, providing quick access to detailed information.
8. **Up-to-Date**: Regularly refreshed on a weekly basis to reflect the latest [CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html).
9. **Gitpod Ready**: Made available on the [Open VSX Registry](https://open-vsx.org/extension/dannysteenman/cloudformation-yaml-snippets) to ensure compatibility with [Gitpod](https://github.com/dannysteenman/vscode-cloudformation-snippets/issues/14).

## Usage

* **Step 1.** Install this extension
* **Step 2.** create a `.yml` file to start working on CloudFormation
* **Step 3.** Check in the bottom right-hand corner of the VS Code editor that the file type is listed as "YAML".
* **Step 4.** To start with the basic template structure, type **cfn** to get the YAML formatted template fragment.
* **Step 5.** Start adding resources in the resource section by using their prefix name e.g. ```autoscaling-autoscalinggroup``` equals resource type ```AWS::AutoScaling::AutoScalingGroup```

![CloudFormation Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cloudformation-snippets/main/images/cfn-snippets-extension-example.gif)

> **Note:** Once you start typing a prefix (explained in step 5), the corresponding snippet will show up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 5).

---
## AWS CloudFormation Attributes Quick Reference

Streamline your CloudFormation workflow with our comprehensive [AWS CloudFormation Attributes cheat sheet](https://towardsthecloud.com/aws-cloudformation-resource-attributes).

Key features:
- Single-table overview of 900+ AWS resource types and their attributes
- Clear "❌" indicators for resources without attributes
- Instantly find the information you need, saving valuable development time

Stop the endless searching. Use this guide to accelerate your CloudFormation projects and boost your productivity.

---
## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dannysteenman/vscode-cloudformation-snippets/issues)

## Author

Danny Steenman

[![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dannysteenman)
[![](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/dannysteenman)
[![](https://img.shields.io/badge/GitHub-2b3137?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dannysteenman)
