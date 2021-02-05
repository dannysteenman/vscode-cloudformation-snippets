Changelog
=========


3.7.0 (2021-02-05)
------------------
- The following resource was updated:
  AWS::ElastiCache::GlobalReplicationGroup. [Github Actions]


3.6.0 (2021-01-29)
------------------
- The following resource was updated: <code
  class="code">AWS::ApiGatewayV2::Stage</code>. [Github Actions]


3.5.0 (2021-01-17)
------------------
- The following resource was updated: AWS::MSK::Cluster. [Github
  Actions]
- Fix syntax. [Danny Steenman]
- Updated git log depth for GH Actions + GH username. [Danny Steenman]


3.4.0 (2021-01-08)
------------------
- The following resource was updated:
  AWS::SSO::InstanceAccessControlAttributeConfiguration. [Github
  Actions]
- Setup gitchangelog config properly. [Danny Steenman]


3.3.0 (2020-12-28)
------------------
- The AWS::ServiceCatalog transform enables Service Catalog users to
  reference outputs from an existing Service Catalog provisioned product
  in their CloudFormation template. [Github Actions]
- Updated changelog, readme, displayName & description. [Danny Steenman]


3.2.0 (2020-12-19)
------------------
- The following resources were updated: AWS::ECR::PublicRepository.
  [Github Actions]
- Add actions/setup-python step at the beginning of the workflow in
  order to fix: '/home/runner/.local/bin' which is not on PATH. [Danny
  Steenman]
- Parsed body in a seperate function, simplified tabbing of properties
  by changing the description and body vars into a list. [Danny
  Steenman]


3.1.0 (2020-12-02)
------------------
- Modules are a way for you to package resource configurations for
  inclusion across stack templates, in a transparent, manageable, and
  repeatable way. Modules can encapsulate common service configurations
  and best practices as modular, customizable building blocks for you to
  include in your stack templates. [Github Actions]
- Updated Github Actions with Python3. [Danny Steenman]
- Updated Github actions in favor of Azure pipelines. [Danny Steenman]


3.0.0 (2020-11-26)
------------------
- Added placeholder functionality + documentation urls in the
  description of every resource type. [Danny Steenman]
- Refactored check_for_update function and sorted the resource-
  types.json. [Danny Steenman]


2.26.0 (2020-11-13)
-------------------
- The following resource was updated:
  AWS::Kendra::DataSource. [Azure Pipeline]


2.25.0 (2020-11-06)
-------------------
- The following resources were updated: AWS::CodeArtifact::Domain and
  AWS::CodeArtifact::Repository. [Azure Pipeline]


2.24.0 (2020-10-23)
-------------------
- The following resources were updated: <code
  class="code">AWS::AppStream::Fleet</code> and <code
  class="code">AWS::AppStream::ImageBuilder</code> [Azure Pipeline]


2.23.0 (2020-10-16)
-------------------
- The following resource was updated: AWS::AmazonMQ::Broker. [Azure
  Pipeline]


2.22.0 (2020-09-18)
-------------------
- The following resource was updated: <code
  class="code">AWS::ApiGatewayV2::DomainName</code>. [Azure Pipeline]


2.21.0 (2020-09-11)
-------------------
- The following resource was updated: <code
  class="code">AWS::ApiGatewayV2::Authorizer</code>. [Azure Pipeline]


2.20.0 (2020-09-04)
-------------------
- The following resource was updated: AWS::CodeCommit::Repository Code.
  [Azure Pipeline]


2.19.0 (2020-08-28)
-------------------
- The following resource was updated: AWS::KMS::Key. [Azure Pipeline]


2.18.0 (2020-08-14)
-------------------
- The following resources were updated: AWS::ECS::TaskDefinition. [Azure
  Pipeline]


2.17.0 (2020-08-07)
-------------------
- The following resources were updated: AWS::ECS::TaskDefinition. [Azure
  Pipeline]


2.16.0 (2020-07-31)
-------------------
- The following resource was updated: AWS::EC2::FlowLog. [Azure
  Pipeline]
- Added homepage icon. [Danny Steenman]
- Updated homepage + added icons. [Danny Steenman]


2.15.0 (2020-07-10)
-------------------
- The following resource was updated: AWS::Amplify::Domain. [Azure
  Pipeline]


2.14.0 (2020-06-26)
-------------------
- The following resources were updated: AWS::AppMesh::VirtualNode and
  AWS::AppMesh::Route. [Azure Pipeline]
- Updated link in README. [Danny Steenman]


2.13.0 (2020-06-19)
-------------------
- The following resource was updated: AWS::EFS::FileSystem. [Azure
  Pipeline]


2.12.0 (2020-06-12)
-------------------
- The following resource was added: AWS::IoT::ProvisioningTemplate.
  [Azure Pipeline]


2.11.0 (2020-05-29)
-------------------
- The following resources was updated: AWS::CodeBuild::ReportGroup.
  [Azure Pipeline]


2.10.0 (2020-05-15)
-------------------
- The following resource was updated: AWS::IoTEvents::DetectorModel.
  [Azure Pipeline]


2.9.0 (2020-05-08)
------------------
- The following resource was updated: AWS::Synthetics::Canary. [Azure
  Pipeline]


2.8.0 (2020-05-01)
------------------
- The following resource was updated: AWS::FSx::FileSystem. [Azure
  Pipeline]
- Updated readme and package.json. [Danny Steenman]


2.7.0 (2020-04-24)
------------------
- The following resource was updated: AWS::Glue::DevEndpoint. [Azure
  Pipeline]


2.6.0 (2020-04-10)
------------------
- The following resource was updated: AWS::CloudWatch::InsightRule.
  [Azure Pipeline]


2.5.0 (2020-04-03)
------------------
- The following resource was updated: AWS::CloudWatch::InsightRule.
  [Azure Pipeline]


2.4.0 (2020-03-27)
------------------
- The following resource was updated: AWS::DMS::Endpoint. [Azure
  Pipeline]


2.3.0 (2020-03-20)
------------------
- The following resources were added: <code
  class="code">AWS::Cassandra::Keyspace</code> and
  <code class="code">AWS::Cassandra::Table</code>. [Azure Pipeline]


2.2.0 (2020-03-13)
------------------
- The following resources were updated:
  AWS::Greengrass::ResourceDefinition and
  AWS::Greengrass::ResourceDefinitionVersion. [Azure Pipeline]
- Readme. [Danny Steenman]


2.1.0 (2020-03-06)
------------------
- The following resource was added: AWS::CloudWatch::CompositeAlarm.
  [Azure Pipeline]
- Moved vsce package command in pipeline script. [Danny Steenman]


2.0.0 (2020-03-06)
------------------
- The following was added: You can now use intrinsic function snippets!
  [Danny Steenman]


1.30.0 (2020-01-31)
-------------------
- The following resources were updated: AWS::Pinpoint::EmailTemplate,
  AWS::Pinpoint::PushTemplate, and AWS::Pinpoint::SmsTemplate. [Azure
  Pipeline]


1.29.0 (2020-01-24)
-------------------
- The following resource was updated: AWS::Lambda::Function. [Azure
  Pipeline]


1.28.0 (2019-12-27)
-------------------
- The following resources were updated: AWS::MSK::Cluster,
  AWS::RDS::DBInstance, and AWS::SSM::Document. [Azure Pipeline]


1.27.0 (2019-12-13)
-------------------
- The following resources were updated: <code
  class="code">AWS::ApiGatewayV2::Api</code>, <code
  class="code">AWS::ApiGatewayV2::Authorizer</code>, <code
  class="code">AWS::ApiGatewayV2::Integration</code>,  <code
  class="code">AWS::ApiGatewayV2::Stage</code>. [Azure Pipeline]


1.26.0 (2019-12-06)
-------------------
- The following resources were updated: <code
  class="code">AWS::ApiGatewayV2::Api</code>, <code
  class="code">AWS::ApiGatewayV2::Authorizer</code>, <code
  class="code">AWS::ApiGatewayV2::Integration</code>,  <code
  class="code">AWS::ApiGatewayV2::Stage</code>. [Azure Pipeline]


1.25.0 (2019-11-28)
-------------------

Fix
~~~
- Package.json. [Danny Steenman]
- Warning: unable to access git config. [Danny Steenman]

Other
~~~~~
- The following resource was added: AWS::Lambda::EventInvokeConfig.
  [Azure Pipeline]


1.24.0 (2019-11-22)
-------------------
- The following resources were updated: AWS::ECS::Cluster,
  AWS::ECS::Service, and AWS::ECS::TaskDefinition. [Azure Pipeline]
- Updated package.json. [Danny Steenman]


1.21.0 (2019-11-07)
-------------------
- The following resource was updated: AWS::AppMesh::Route. [Azure
  Pipeline]


1.20.0 (2019-10-24)
-------------------
- The following resource was updated: AWS::MSK::Cluster. [Azure
  Pipeline]


1.19.0 (2019-10-10)
-------------------
- The following resource were updated: AWS::Events::EventBusPolicy,
  AWS::Events::Rule. [Azure Pipeline]


1.18.0 (2019-10-03)
-------------------
- The following resource was updated: AWS::Glue::DevEndpoint. [Azure
  Pipeline]


1.17.0 (2019-09-19)
-------------------
- The following resource was updated: AWS::AppMesh::Route. [Azure
  Pipeline]
- Updated homepage and added build status badge. [Danny Steenman]


1.16.0 (2019-09-05)
-------------------
- The following resources were updated:
  AWS::ApplicationAutoScaling::ScalableTarget, AWS::DynamoDB::Table,
  AWS::EC2::Instance,                AWS::ECS::TaskDefinition,
  AWS::ElastiCache::ReplicationGroup, AWS::Events::Rule, AWS::IAM::Role,
  and AWS::Lambda::EventSourceMapping. [Azure Pipeline]


1.15.0 (2019-08-29)
-------------------
- The following resource was updated: Route. [Azure Pipeline]


1.14.0 (2019-08-22)
-------------------
- The following resource was updated: AWS::DMS::ReplicationTask. [Azure
  Pipeline]


1.13.0 (2019-08-15)
-------------------
- The following resources were updated: AWS::AppSync::GraphQLApi,
  AWS::EC2::ClientVpnEndpoint, AWS::Greengrass::Group,
  AWS::Greengrass::ConnectorDefinition,
  AWS::Greengrass::CoreDefinition,
  AWS::Greengrass::DeviceDefinition,
  AWS::Greengrass::FunctionDefinition,
  AWS::Greengrass::LoggerDefinition,
  AWS::Greengrass::ResourceDefinition, and
  AWS::Greengrass::SubscriptionDefinition. [Azure Pipeline]


1.12.0 (2019-08-08)
-------------------
- The following resources were updated: AWS::Batch::JobDefinition,
  AWS::Cognito::UserPool,                AWS::Cognito::UserPoolClient,
  and AWS::Glue::Job. [Azure Pipeline]


1.11.0 (2019-07-25)
-------------------
- The following resource was updated: AWS::AmazonMQ::Broker. [Azure
  Pipeline]


1.10.0 (2019-07-18)
-------------------
- The following resource was added: AWS::CloudWatch::AnomalyDetector.
  [Azure Pipeline]


1.9.0 (2019-07-04)
------------------
- The following resources were updated: AWS::IoTAnalytics::Channel,
  AWS::IoTAnalytics::Datastore. [Azure Pipeline]


1.8.0 (2019-06-27)
------------------
- The following resource was updated: AWS::EC2::LaunchTemplate. [Azure
  Pipeline]


1.7.0 (2019-06-14)
------------------
- The following resources were updated: AWS::AppMesh::VirtualNode,
  AWS::CodeBuild::Project, AWS::EC2::Host, AWS::EC2::Route,
  AWS::EC2::VPNConnection,                AWS::ECS::Cluster,
  AWS::ECS::Service, AWS::ECS::TaskDefinition,
  AWS::EFS::MountTarget, AWS::ElasticLoadBalancingV2::ListenerRule,
  AWS::EMR::Cluster,
  AWS::KinesisFirehose::DeliveryStream, AWS::S3::Bucket. [Azure
  Pipeline]


1.6.0 (2019-05-30)
------------------
- The following resources were updated: AWS::CodeCommit::Repository and
  AWS::EC2::LaunchTemplate. [Azure Pipeline]


1.5.0 (2019-05-23)
------------------
- The following resources were updated: AWS::AppSync::GraphQLApi,
  AWS::Cognito::UserPool, AWS::Glue::Classifier, AWS::Glue::Crawler,
  AWS::Glue::DevEndpoint, AWS::Glue::Job, and AWS::Glue::Trigger. [Azure
  Pipeline]


1.4.0 (2019-05-14)
------------------

Fix
~~~
- Feedparser entry and changelog. [Danny Steenman]

Other
~~~~~
- The following resource was updated:
  AWS::ServiceCatalog::CloudFormationProduct. [Azure Pipeline]


1.3.0 (2019-04-28)
------------------
- The following resources were updated: AWS::ECS::TaskDefinition,
  AWS::ElasticLoadBalancingV2::TargetGroup. [Azure Pipeline]


1.2.0 (2019-04-12)
------------------
- The following resource was added:
  AWS::ServiceCatalog::ResourceUpdateConstraint. [Azure Pipeline]
- Merge e750df96bcfccfc2941ef49ae7b5db8a20f1d0e0 into
  26b5959f29a64166af1496007de3166cbf5daa6d. [Danny]
- Setup automated snippet updater pipeline in Azure. [Danny Steenman]
- Set up CI with Azure Pipelines [skip ci] [Danny]


1.1.0 (2019-03-21)
------------------
- AWS::Greengrass resource added. [Danny Steenman]


1.0.4 (2019-03-08)
------------------
- Added License and update package to 1.0.4. [Danny Steenman]


1.0.3 (2019-03-08)
------------------
- Updated package to 1.0.3. [Danny Steenman]


1.0.2 (2019-03-07)
------------------
- Added .vsix package to .gitignore. [Danny Steenman]


1.0.1 (2019-03-07)
------------------
- Setup instructions and updated package to 1.0.1. [Danny Steenman]
- Updated README.md. [Danny Steenman]
- Initialize VS Code extension including generated CFN snippet file.
  [Danny Steenman]


