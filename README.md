# AWS CloudFormation Snippets for VS Code

[![](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cloudformation-yaml-snippets?color=374151&label=Visual%20Studio%20Marketplace&labelColor=000&logo=visual-studio-code&logoColor=0098FF)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cloudformation-yaml-snippets?color=374151&label=Open%20VSX%20Registry&labelColor=000&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyB2aWV3Qm94PSI0LjYgNSA5Ni4yIDEyMi43IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Ik0zMCA0NC4yTDUyLjYgNUg3LjN6TTQuNiA4OC41aDQ1LjNMMjcuMiA0OS40em01MSAwbDIyLjYgMzkuMiAyMi42LTM5LjJ6IiBmaWxsPSIjYzE2MGVmIi8+CiAgPHBhdGggZD0iTTUyLjYgNUwzMCA0NC4yaDQ1LjJ6TTI3LjIgNDkuNGwyMi43IDM5LjEgMjIuNi0zOS4xem01MSAwTDU1LjYgODguNWg0NS4yeiIgZmlsbD0iI2E2MGVlNSIvPgo8L3N2Zz4=&logoColor=0098FF)](https://open-vsx.org/extension/dannysteenman/cloudformation-yaml-snippets)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/dannysteenman.cloudformation-yaml-snippets 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)
[![Rating](https://img.shields.io/visual-studio-marketplace/stars/dannysteenman.cloudformation-yaml-snippets)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets)

This CloudFormation Snippets extension equips Visual Studio Code with JSON and YAML snippets for **all** AWS CloudFormation and SAM resources - over 1250+ in total. It's your complete toolset for efficient CloudFormation template development.

> [!TIP]
> **AWS Done Right: Ship Faster, More Securely, at Lower Cost!** Our [AWS CDK Landing Zone Service](https://towardsthecloud.com) helps B2B startups & enterprises achieve SOC 2 compliance 90% faster, reclaim 30% of developer capacity for product innovation while eliminating six-figure Cloud Engineering costs.
>
> Discover how we deliver 10x AWS infrastructure value while cutting costs.
>
> <a href="https://towardsthecloud.com/contact"><img alt="Book your free intro call" src="https://img.shields.io/badge/book%20your%20free%20intro%20call-success.svg?style=for-the-badge"/></a>
>
> <details><summary>☁️ <strong>Learn more how we help businesses succeed on AWS Cloud...</strong></summary>
>
><br/>
>
> AWS promises simplicity but delivers complexity. Businesses struggle with security risks and compliance requirements that divert developers from core product work.
>
> Without AWS expertise, you face vulnerabilities, technical debt, and market delays while competitors race ahead.
>
> Traditional consultancies worsen this by prioritizing billable hours over outcomes.
>
> We take the opposite approach, focusing exclusively on business outcomes by eliminating AWS complexity, accelerating your developers, and securing your infrastructure through:
>
> ### Deploying a [Secure Landing Zone](https://towardsthecloud.com/services/aws-landing-zone)
> - Multi-account architecture with strict security boundaries
>   - **100% score** on [CIS AWS Foundation Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html)
>   - **96% rating** on [AWS foundational security best practices](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html)
> - Manage user access securely on AWS via Single Sign-On (SSO)
> - Full AWS CDK implementation (Infrastructure as Code)
> - Multi-region deployments supported
> - Cross-account monitoring and security alerts
> - View our [Roadmap](https://github.com/towardsthecloud/aws-cdk-landing-zone-roadmap) for all implemented and upcoming features
>
> ### Upskilling and accelerating your developers
> - They get access to our production-ready, security-hardened AWS CDK components
> - They receive AWS best practices guidance to prevent technical debt
>
> ### Providing support and maintenance
> - Landing Zone gets updates and security patches
> - Priority Slack/Teams support for infrastructure challenges
> - Quarterly [security](https://towardsthecloud.com/services/aws-security-review) and [cost optimization](https://towardsthecloud.com/services/aws-cost-optimization) assessments to stay compliant and reduce AWS costs
>
> ## What This Means For Your Business
> - **30% Lower TCO**: Cut Total Cost by 40% through right-sized resources while eliminating the $150K+ cost of a specialized AWS hire.
> - **Accelerate Development**: Redirect 30% of engineering time from infrastructure to revenue-generating features with pre-built, compliant CDK components.
> - **Compliance-Ready Infrastructure**: Meet security requirements from day one with architecture that [speeds up audit preparation by 90%](https://towardsthecloud.com/blog/aws-landing-zone-case-study-accolade) for SOC 2, HIPAA, and other security frameworks.
>
> All of this is included in a [fixed monthly subscription](https://towardsthecloud.com/pricing). No lock-in, no large upfront costs, just predictable monthly pricing.
>
> Book a free call to see how we deliver 10x AWS infrastructure value at a fraction of a Cloud Engineer's cost.
>
> <a href="https://towardsthecloud.com/contact"><img alt="Book your free introduction call" src="https://img.shields.io/badge/book%20your%20free%20introduction%20call-success.svg?style=for-the-badge"/></a>
> </details>

---

## Features

1. **Comprehensive Coverage**: Offers snippets for **all** AWS CloudFormation and AWS SAM resources available - that's over 1250+ resources snippets at your fingertips!
2. **Complete Property Support**: Includes all nested properties for each resource, ensuring you have access to every configurable aspect of your AWS resources.
3. **Documentation Hover Links**: Quickly access AWS CloudFormation resource and property documentation by hovering over resource types and property names in your templates.
4. **Flexible Template Support**: Seamlessly works with both YAML and JSON CloudFormation templates.
5. **Efficient Autocomplete**: Simply type the resource name (e.g., `ec2-instance`) to instantly load the corresponding snippet for `AWS::EC2::Instance`.
6. **Rich Feature Set**: Incorporates intrinsic functions, conditions, and diverse parameter types for robust template creation.
7. **Enhanced Navigation**: Features placeholders that enable swift movement through resource properties.
8. **Resource Documentation**: Each snippet is linked to its official AWS documentation, providing quick access to detailed information.
9. **Up-to-Date**: Regularly refreshed on a weekly basis to reflect the latest [CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html).
10. **Gitpod Ready**: Made available on the [Open VSX Registry](https://open-vsx.org/extension/dannysteenman/cloudformation-yaml-snippets) to ensure compatibility with [Gitpod](https://github.com/towardsthecloud/vscode-cloudformation-snippets/issues/14).

## Usage

1. Install the [CloudFormation Snippets extension](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cloudformation-yaml-snippets) in VS Code.
2. Create a new `.yml` or `.json` file.
3. Ensure the file type is set to "YAML" or "JSON" in the bottom right corner of VS Code.
4. Type cfn to insert the basic CloudFormation template structure.
5. Add resources using their short prefix (e.g. `s3-bucket` for `AWS::S3::Bucket`).

Example of auto-completion in action:

![CloudFormation Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cloudformation-snippets/main/images/cfn-snippets-extension-example.gif)

and an example of the hover information:

![IAM Actions Snippets Hover Example](https://raw.githubusercontent.com/dannysteenman/vscode-cloudformation-snippets/main/images/cfn-snippets-hover-example.gif)

> **Note:** Once you start typing a prefix (explained in step 5), the corresponding snippet will show up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 5).

---
## AWS CloudFormation Starterkit

We've developed the [AWS CloudFormation Starterkit](https://github.com/towardsthecloud/aws-cloudformation-starterkit) to streamline your infrastructure setup using CloudFormation.

It comes with pre-configured templates, automated validation scripts, and seamless integration with CI/CD pipelines, you'll be able to deploy robust, scalable, and secure AWS environments with ease.

The starterkit empowers you to adopt best practices effortlessly. By leveraging tools like Checkov for security compliance and cfn-lint for template validation, you ensure that your infrastructure is both reliable and secure.

---
## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/towardsthecloud/vscode-cloudformation-snippets/issues)

## Author

[Danny Steenman](https://towardsthecloud.com/about)

[![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/towardsthecloud)
[![](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/dannysteenman)
[![](https://img.shields.io/badge/GitHub-2b3137?style=for-the-badge&logo=github&logoColor=white)](https://github.com/towardsthecloud)
