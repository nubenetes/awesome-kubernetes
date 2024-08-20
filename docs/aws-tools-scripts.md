# AWS Tools and Scripts

1. [AWS Scripts](#aws-scripts)
2. [AWS Samples (Boilerplates)](#aws-samples-boilerplates)
3. [Open Source at AWS](#open-source-at-aws)
4. [AWS Tools](#aws-tools)
    1. [AWS CI/CD Tools](#aws-cicd-tools)
5. [AWS Toolkits](#aws-toolkits)
6. [AWS Management Tools Blog](#aws-management-tools-blog)
7. [AWS CLI and AWS SDK](#aws-cli-and-aws-sdk)
8. [Amazon CodeWhisperer](#amazon-codewhisperer)
9. [AWS S3 Sync](#aws-s3-sync)
10. [Third Party Tools](#third-party-tools)

## AWS Scripts

- [AWS IP inventory](https://github.com/okelet/awsipinventory) Tool to generate an inventory of all IP addresses in use in an account, one or multiple VPC, or one or multiple subnet.
- [dev.to: How to Copy a Security Group with Rules from one AWS Account to Another account](https://dev.to/dineshrathee12/how-to-copy-a-security-group-with-rules-from-one-aws-account-to-another-account-36mb)
    - [CopySGFromOneAWSAccountToAnotherScript.py](https://github.com/dineshrathee12/CopySecurityGroupWithRulesFromOneAWSAccountToAnotherAWSAccount/blob/main/CopySGFromOneAWSAccountToAnotherScript.py)
- [github.com/awslabs/assisted-log-enabler-for-aws: Assisted Log Enabler - Find resources that are not logging, and turn them on](https://github.com/awslabs/assisted-log-enabler-for-aws)
- https://github.com/dannysteenman/aws-toolbox A collection of useful Shell & Python scripts that make your DevOps life easier in AWS. Furthermore you'll also find a list of links that point to awesome DevOps tools from other creators.
- [saml-to/assume-aws-role-action](https://github.com/saml-to/assume-aws-role-action) Assume AWS IAM Roles using SAML.to in GitHub Actions. This action enables workflows to obtain AWS Access Credentials for a desired IAM Role using AWS IAM SAML and a GitHub Actions Repository Token.
- [github.com/Levi-Michael/boto3-ec2-s3-management: A python tools base on AWS boto3 for manage ec2 and s3 buckets](https://github.com/Levi-Michael/boto3-ec2-s3-management)
- [github.com/cavaliercoder/vpc-free](https://github.com/cavaliercoder/vpc-free) Find free IP address blocks in AWS EC2.

## AWS Samples (Boilerplates)

- [==AWS Samples (Boilerplates)==](demos.md#aws-samples-boilerplates)

## Open Source at AWS

- [OpenSource at AWS](https://aws.github.io/)

## AWS Tools

- [github.com/awslabs](https://github.com/awslabs)
- [==steampipe== 🌟](https://steampipe.io) Steampipe is an open source tool for querying cloud APIs in a universal way and reasoning about the data in SQL.
    - [==Querying AWS at scale across APIs, Regions, and accounts==](https://aws.amazon.com/blogs/opensource/querying-aws-at-scale-across-apis-regions-and-accounts/)
- [==awslabs/aws-cloudsaga: AWS CloudSaga - Simulate security events in AWS==](https://github.com/awslabs/aws-cloudsaga) AWS CloudSaga is for customers to test security controls and alerts within their Amazon Web Services (AWS) environment, using generated alerts based on security events seen by the AWS Customer Incident Response Team (CIRT).
    - New Open Source tool alert! Introducing AWS CloudSaga, a open source tool for generating events within AWS to be investigated by blue teams & incident responders.
    - AWS CloudSaga is based on basic scenarios related to security events. Using AWS CloudSaga, you can safely generate events via the AWS API, and then use these events to test your team's investigation capabilities and responses in order to identify gaps and areas of improvement.
- [willdady/aws-resource-based-policy-collector: AWS resource-based policy collector](https://github.com/willdady/aws-resource-based-policy-collector) Utility for collecting resource-based policies from an AWS account
- [ermetic/access-undenied-aws 🌟](https://github.com/ermetic/access-undenied-aws) Ermetic is launching a new open-source tool: Access Undenied on AWS. The tool parses AWS AccessDenied CloudTrail events, explains the reasons for them and offers actionable fixes.
    - [ermetic.com: Access Undenied on AWS](https://ermetic.com/blog/aws/access-undenied-on-aws/)
- [github.com/ualter: AwsBe](https://github.com/ualter/awsbe-site) A tool to help handle AWS Session connections on terminals, using your configured AWS Shared Config and Credentials files. It manages Roles to Assume, MFA Token requests, AWS SSO Sign-in, AWS SSO Tokens and the expiration of opened sessions.
- [github.com/awslabs/amazon-s3-tar-tool: Amazon S3 Tar Tool](https://github.com/awslabs/amazon-s3-tar-tool) A utility tool to create a tarball of existing objects in Amazon S3
- [==github.com/aws-samples/aws-cdk-stack-builder-tool==](https://github.com/aws-samples/aws-cdk-stack-builder-tool) AWS CDK Builder is a browser-based tool designed to streamline bootstrapping of Infrastructure as Code (IaC) projects using the AWS Cloud Development Kit (CDK).
- [github.com/containerscrew/aws-sso-auth](https://github.com/containerscrew/aws-sso-auth) Fetch your local ~/.aws/credentials using AWS SSO
- [==cloudcatalog.dev==](https://www.cloudcatalog.dev) Documentation tool for AWS Architectures. CloudCatalog is an Open Source project that helps you document your AWS resources, services and assign owners.
- [==spacelift.io/blog/aws-s3-cp: AWS S3 Cp [Copy] Command Overview with Examples==](https://spacelift.io/blog/aws-s3-cp) Effectively working with S3 requires moving data in and out of S3 buckets efficiently, supporting use cases such as web hosting, content distribution, backups, archiving, media storage and streaming, and more. In this article, we will explore how to use the aws s3 cp command to transfer data between your local filesystem and the S3 buckets.
- [github.com/infrahouse/infrahouse-toolkit](https://github.com/infrahouse/infrahouse-toolkit) A collection of tools for building infrastructure

### AWS CI/CD Tools

- [==dev.to: Continuous Integration and Deployment on AWS - and a wishlist for CI/CD Tools on AWS==](https://dev.to/aws-builders/continuous-integration-and-deployment-on-aws-and-a-wishlist-for-cicd-tools-on-aws-5a13)

## AWS Toolkits

- [AWS Toolkits for Cloud9, JetBrains and VS Code now support interaction with over 200 new resource types 🌟](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-toolkits-cloud9-jetbrains-vs-code/)

## AWS Management Tools Blog

- [AWS Management Tools Blog](https://aws.amazon.com/blogs/mt/)
- [Metabadger](https://github.com/salesforce/metabadger) Prevent SSRF attacks on AWS EC2 via automated upgrades to the more secure Instance Metadata Service v2 (IMDSv2).

## AWS CLI and AWS SDK

- [Amazon CLI Documentation](https://aws.amazon.com/cli)
- [AWS CLI Command Reference](http://docs.aws.amazon.com/cli/latest/index.html)
- [New usage examples have been added to the CLI for CodePipeline API Reference](http://docs.aws.amazon.com/cli/latest/reference/codepipeline/index.html)
- [ec2-ssh-yplan: A pair of command line utilities for finding and SSH-ing into your Amazon EC2 instances by tag (such as ‘Name’)](https://pypi.python.org/pypi/ec2-ssh-yplan/)
- List running instances using 'awscli':

```bash
aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query 'Reservations[].Instances[].[InstanceID]'
```

- List all AWS instances in a table format using 'awscli':

```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].[Placement.AvailabilityZone, State.Name, InstanceID,InstanceType,Platform,Tags.Value,State.Code,Tags.Values]' --output table
```

- [Announcing the end of support for Python 2.7 in the AWS SDK for Python and AWS CLI v1](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-python-2-7-in-aws-sdk-for-python-and-aws-cli-v1/)
- [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/)
- [medium: AWS CLI with jq and Bash](https://medium.com/circuitpeople/aws-cli-with-jq-and-bash-9d54e2eabaf1) The CLI is utilitarian, but a little jq sauce makes it beautiful
- [aws.plainenglish.io: Lessons Learned From Switching to AWS SDK v3](https://aws.plainenglish.io/lessons-learned-from-switching-to-aws-sdk-v3-6babe1530a59) Dive into some lessons learned before you switch your Node.js lambda functions over to the latest and greatest
- [blog.awsfundamentals.com: Step-By-Step: Emptying S3 Buckets and Directories Using the AWS CLI with S3 RM](https://blog.awsfundamentals.com/aws-s3-rm-removing-files)
- [==dev.to/franciscogm: AWS CLI SSO made easy==](https://dev.to/franciscogm/aws-cli-sso-made-easy-3bh9)

## Amazon CodeWhisperer

- [Amazon CodeWhisperer 🌟](https://aws.amazon.com/codewhisperer/) Amazon CodeWhisperer is a machine learning (ML)–powered service that helps improve developer productivity by generating code recommendations based on developers’ comments in natural language and their code in the integrated development environment (IDE). During preview, CodeWhisperer is available for Java, JavaScript, and Python programming languages. The service integrates with multiple IDEs, including JetBrains (IntelliJ, PyCharm, and WebStorm), Visual Studio Code, AWS Cloud9, and the AWS Lambda console.
- [genbeta.com: Amazon lanza CodeWhisperer, su propia alternativa a GitHub Copilot… que no insertará código ya licenciado sin avisar](https://www.genbeta.com/desarrollo/amazon-lanza-codewhisperer-su-propia-alternativa-a-github-copilot-que-no-insertara-codigo-licenciado-avisar)
- [hashicorp.com: Accelerate your Terraform development with Amazon CodeWhisperer](https://www.hashicorp.com/blog/accelerate-your-terraform-development-with-amazon-codewhisperer)
- [aws.amazon.com/blogs: Introducing Amazon CodeWhisperer for command line](https://aws.amazon.com/blogs/devops/introducing-amazon-codewhisperer-for-command-line/)

## AWS S3 Sync

- [==blog.awsfundamentals.com: AWS S3 Sync - An Extensive Guide==](https://blog.awsfundamentals.com/aws-s3-sync) Learn all about AWS S3 sync - covering download, upload, synchronize buckets, file selection patterns, dry-run, and more - examples included. The CLI is a daily tool for every DevOps engineer working with AWS. A deep-dive for the 𝗮𝘄𝘀 𝘀𝟯 𝘀𝘆𝗻𝗰 command & its powerful options.

## Third Party Tools

- [ec2-spot-converter](https://github.com/jcjorel/ec2-spot-converter) This tool converts existing EC2 instances back and forth from on-demand and 'persistent' Spot billing models while preserving instance attributes (Launch configuration, Tags..), network attributes (existing Private IP addresses, Elastic IP), storage (Volumes), Elastic Inference accelerators and Elastic GPUs. It also allows replacement of existing Spot instances with new "identical" ones to update the instance type and cpu options.
- [techcrunch.com: Vantage makes managing AWS easier](https://techcrunch.com/2021/01/12/vantage-makes-managing-aws-easier/)
- [vantage.sh](https://www.vantage.sh/)
- [github.com/one2nc/cloudlens 🌟](https://github.com/one2nc/cloudlens) k9s like CLI for AWS
- [Amazon CodeCatalyst](https://codecatalyst.aws/explore) Quickly build and deliver apps at scale on AWS.
- [github.com/Reaimua/AWS-CLI-Uploader-Project](https://github.com/Reaimua/AWS-CLI-Uploader-Project/) Simple bash scripts that uploads a local file to an Amazon S3 bucket
- [github.com/welldone-cloud/aws-list-resources](https://github.com/welldone-cloud/aws-list-resources) Uses the AWS Cloud Control API to list resources that are present in a given AWS account and region(s). Discovered resources are written to a JSON output file.