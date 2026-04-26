# AWS Security

1. [Introduction](#introduction)
2. [AWS Security Scanners](#aws-security-scanners)
3. [AWS Security Reference Architecture AWS SRA](#aws-security-reference-architecture-aws-sra)
4. [Application Security](#application-security)
5. [Policy as Code with AWS CDK and Open Policy Agent](#policy-as-code-with-aws-cdk-and-open-policy-agent)
6. [Payment Card Industry Data Security Standard compliance](#payment-card-industry-data-security-standard-compliance)
7. [AWS IAM](#aws-iam)
    1. [Terraform IAM Policy Validator](#terraform-iam-policy-validator)
    2. [AWS IAM Anywhere](#aws-iam-anywhere)
8. [AWS Organizations](#aws-organizations)
9. [AWS Control Tower](#aws-control-tower)
10. [AWS Firewalls](#aws-firewalls)
11. [AWS WAF Web Application Firewall](#aws-waf-web-application-firewall)
12. [AWS Secrets Manager](#aws-secrets-manager)
13. [AWS Vault](#aws-vault)
14. [Tweets](#tweets)

## Introduction

- [AWS Security Blog](http://blogs.aws.amazon.com/security)
- [AWS Security](https://aws.amazon.com/security/)
- [AWS Security docs](https://docs.aws.amazon.com/security/)
- [Tutorial: Configure Apache Web Server on Amazon Linux to use SSL/TLS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html)
- [The Most Popular AWS Security Blog Posts in 2015](http://blogs.aws.amazon.com/security/post/Tx4QX7W51NDSLO/The-Most-Popular-AWS-Security-Blog-Posts-in-2015)
- [Announcing Industry Best Practices for Securing AWS Resources](http://blogs.aws.amazon.com/security/post/Tx3PTTZB14FWPBA/Announcing-Industry-Best-Practices-for-Securing-AWS-Resources)
- [The Most Viewed AWS Security Blog Posts so Far in 2016](http://blogs.aws.amazon.com/security/post/Tx2N52FR8XGJVL3/The-Most-Viewed-AWS-Security-Blog-Posts-so-Far-in-2016)
- [Oracle Database Encryption Options on Amazon RDS](https://aws.amazon.com/es/blogs/apn/oracle-database-encryption-options-on-amazon-rds/)
- [Learn AWS Security Fundamentals with Free and Online Training](https://aws.amazon.com/about-aws/whats-new/2016/06/learn-aws-security-fundamentals-with-free-and-online-training)
- [How to Restrict Amazon S3 Bucket Access to a Specific IAM Role](http://blogs.aws.amazon.com/security/post/TxK5WUJK3DG9G8/How-to-Restrict-Amazon-S3-Bucket-Access-to-a-Specific-IAM-Role)
- [Updated Whitepaper Available: AWS Best Practices for DDoS Resiliency](http://blogs.aws.amazon.com/security/post/Tx6QAIBSQTJPHB/Updated-Whitepaper-Available-AWS-Best-Practices-for-DDoS-Resiliency)
- [AWS Security Blog: In Case You Missed These: AWS Security Blog Posts from June, July, and August 2016](http://blogs.aws.amazon.com/security/post/Tx3KVD6T490MM47/In-Case-You-Missed-These-AWS-Security-Blog-Posts-from-June-July-and-August)
- [Amazon Inspector Announces General Availability for Windows](https://aws.amazon.com/es/about-aws/whats-new/2016/08/amazon-inspector-announces-general-availability-for-windows/)
- [encrypt and decrypt data: Importing Key Material in AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) Use your own encryption keys with AWS Key Management Service.
- [Amazon s2n: AWS’s new Open Source implementation of the SSL/TLS network encryption protocols](http://blogs.aws.amazon.com/security/post/TxLEHNNDPUFDU9/Automated-Reasoning-and-Amazon-s2n)
- [Encrypt global data client-side with AWS KMS multi-Region keys](https://aws.amazon.com/blogs/security/encrypt-global-data-client-side-with-aws-kms-multi-region-keys/) Today, AWS Key Management Service (AWS KMS) is introducing multi-Region keys, a new capability that lets you replicate keys from one Amazon Web Services (AWS) Region into another. Multi-Region keys are designed to simplify management of client-side encryption when your encrypted data has to be copied into other Regions for disaster recovery or is replicated in Amazon DynamoDB global tables.
- [acloudguru.com: How to audit and secure an AWS account](https://acloudguru.com/blog/engineering/how-to-audit-and-secure-an-aws-account)
- [yobyot.com: AWS multi-region KMS keys and Data Lifecycle Manager: better together](https://www.yobyot.com/aws/aws-multi-region-keys-and-ec2-data-lifecycle-manager/2021/08/18/)
- [==How to automate AWS account creation with SSO user assignment==](https://aws.amazon.com/blogs/security/how-to-automate-aws-account-creation-with-sso-user-assignment/)
- [Security practices in AWS multi-tenant SaaS environments](https://aws.amazon.com/blogs/security/security-practices-in-aws-multi-tenant-saas-environments/) Many good tips, from identity management to tenant isolation.
- [How to use AWS Security Hub and Amazon OpenSearch Service for SIEM](https://aws.amazon.com/blogs/security/how-to-use-aws-security-hub-and-amazon-opensearch-service-for-siem/)
- [github.com/aws-samples: How to set up continuous replication from your third-party secrets manager to AWS Secrets Manager](https://github.com/aws-samples/aws-secrets-manager-hybrid-secret-replication-from-hashicorp-vault)
- [linkedin.com: Complexities of AWS Security Groups in the Cloud World](https://www.linkedin.com/pulse/complexities-aws-security-groups-cloud-world-ashish-kar/) Do you feel AWS security groups are hard to implement? Are you tired of reconfiguring IP addresses in security groups whenever workloads get restarted or redeployed?
- [awslabs/cognito-at-edge](https://github.com/awslabs/cognito-at-edge) Serverless authentication solution to protect your website or Amplify application
- [github.com/aws-samples: Service Control Policy examples](https://github.com/aws-samples/service-control-policy-examples) Example AWS Service control policies to get started or mature your usage of AWS SCPs.
- [darryl-ruggles.cloud: AWS SSO Credentials With Multiple Accounts](https://darryl-ruggles.cloud/aws-sso-credentials-with-multiple-accounts)

## AWS Security Scanners

- [github.com/awslabs/sustainability-scanner: Sustainability Scanner (SusScanner)](https://github.com/awslabs/sustainability-scanner) Validate AWS CloudFormation templates against AWS Well-Architected Sustainability Pillar best practices.

## AWS Security Reference Architecture AWS SRA

- [==docs.aws.amazon.com: AWS Security Reference Architecture (AWS SRA)== 🌟](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)
- [aws.amazon.com: Update of AWS Security Reference Architecture is now available](https://aws.amazon.com/blogs/security/update-of-aws-security-reference-architecture-is-now-available/) A set of guidelines for deploying the full complement of AWS security services in a multi-account environment.

## Application Security

- [docs.aws.amazon.com: Application security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/application-security.html) Application security (AppSec) describes the overall process of how you design, build, and test the security properties of the workloads you develop. You should have appropriately trained people in your organization, understand the security properties of your build and release infrastructure, and use automation to identify security issues.

## Policy as Code with AWS CDK and Open Policy Agent

- [Realize Policy-as-Code with AWS Cloud Development Kit through Open Policy Agent 🌟](https://aws.amazon.com/blogs/opensource/realize-policy-as-code-with-aws-cloud-development-kit-through-open-policy-agent/)

## Payment Card Industry Data Security Standard compliance

- [PCI DSS Standardized Architecture on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/05/pci-dss-standardized-architecture-on-the-aws-cloud-quick-start-reference-deployment/)

## AWS IAM

- [AWS Identity and Access Management - Getting Started](http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)
- [AWS Identity and Access Management (IAM) best practices in 2016](http://blogs.aws.amazon.com/security/post/Tx2OB7YGHMB7WCM/Adhere-to-IAM-Best-Practices-in-2016)
- [How to Record and Govern Your IAM Resource Configurations Using AWS Config](http://blogs.aws.amazon.com/security/post/Tx14ADBJOCAT9NS/How-to-Record-and-Govern-Your-IAM-Resource-Configurations-Using-AWS-Config)
- [How to Use SAML to Automatically Direct Federated Users to a Specific AWS Management Console Page](http://blogs.aws.amazon.com/security/post/Tx2CGWIB8SBYW2J/How-to-Use-SAML-to-Automatically-Direct-Federated-Users-to-a-Specific-AWS-Manage)
- [New IAMCTL tool compares multiple IAM roles and policies](https://aws.amazon.com/es/blogs/security/new-iamctl-tool-compares-multiple-iam-roles-and-policies/)
- [Bring your own CLI to Session Manager with configurable shell profiles](https://aws.amazon.com/es/blogs/mt/bring-your-own-cli-session-manager-configurable-shell-profiles/)
- [keepler.io: Gestionando el control de accesos en nuestro data lake en AWS](https://keepler.io/2021/03/gestionando-el-control-de-accesos-en-nuestro-data-lake-en-aws/)
- [aws.amazon.com: IAM Access Analyzer now supports over 100 policy checks with actionable recommendations to help you author secure and functional policies](https://aws.amazon.com/about-aws/whats-new/2021/03/iam-access-analyzer-supports-over-100-policy-checks-with-actionable-recommendations/)
- [aws.amazon.com: IAM Access Analyzer Update – Policy Validation](https://aws.amazon.com/blogs/aws/iam-access-analyzer-update-policy-validation/)
- [cloudkatha.com: Difference between Root User and IAM User in AWS You Need to Know](https://cloudkatha.com/difference-between-root-user-and-iam-user-in-aws-you-need-to-know/)
- [infoq.com: Incorrect IAM Policy Raised Questions About AWS Access to S3 Data](https://www.infoq.com/news/2022/01/aws-iam-s3-access/)
- [==iann0036/iamlive==](https://github.com/iann0036/iamlive) Generate an IAM policy from AWS calls using client-side monitoring (CSM) or embedded proxy
- [daan.fyi: AWS IAM Demystified](https://www.daan.fyi/writings/iam)
- [willdady/cdk-iam-credentials-rotator: IAM Credentials Rotator](https://github.com/willdady/cdk-iam-credentials-rotator) AWS CDK construct for rotating IAM user credentials and sending to a third party.
- [==Organizing Your AWS Environment Using Multiple Accounts (white paper for best practices)==](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) Reasons you should be using multiple accounts in AWS:
    - You can constrain access to sensitive data
    - You'll promote innovation & agility
    - You can more easily manage costs
- [aws.amazon.com: When and where to use IAM permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/) A permissions boundary is an IAM feature that helps your centralized cloud IAM teams to safely empower your application developers to create new IAM roles and policies in Amazon Web Services (AWS).
- [Extend AWS IAM roles to workloads outside of AWS with IAM Roles Anywhere 🌟](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/) **A secure way for on-premises servers, containers, or apps to obtain temporary AWS credentials and remove the need for creating and managing long-term AWS credentials**
- [Use IAM Access Analyzer policy generation to grant fine-grained permissions for your AWS CloudFormation service roles](https://aws.amazon.com/blogs/security/use-iam-access-analyzer-policy-generation-to-grant-fine-grained-permissions-for-your-aws-cloudformation-service-roles/)
- [ermetic.com: Diving Deeply into IAM Policy Evaluation – Highlights from AWS re:Inforce IAM433](https://ermetic.com/blog/aws/diving-deeply-into-iam-policy-evaluation-highlights-from-aws-reinforce-session-iam433/)
- [globaldatanet.com: .AWS IAM Identity Center Permission Management at Scale Part 2](https://globaldatanet.com/tech-blog/aws-iam-identity-center-permission-management-at-scale-part-2)
- [How to monitor and query IAM resources at scale – Part 1](https://aws.amazon.com/blogs/security/how-to-monitor-and-query-iam-resources-at-scale-part-1/) Useful details on how AWS IAM works so that you can use it more effectively.
- [github.com/aws-samples: Visualize AWS IAM Access Analyzer Policy Validation Findings](https://github.com/aws-samples/visualize-iam-access-analyzer-policy-validation-findings)
- [thenewstack.io: A Deep Dive into the Security of IAM in AWS](https://thenewstack.io/a-deep-dive-into-the-security-of-iam-in-aws/) How do you tighten up identity access management when you're using Amazon's cloud? Here are some best practices and useful tools for keeping everything safe.

### Terraform IAM Policy Validator

- [awslabs/terraform-iam-policy-validator](https://github.com/awslabs/terraform-iam-policy-validator) A command line tool that validates AWS IAM Policies in a Terraform template against AWS IAM best practices.

### AWS IAM Anywhere

- [==jimmydqv.com: AWS IAM Anywhere== 🌟](https://jimmydqv.com/iam-anywhere/)
    - Most of us that have worked with cloud long enough has encountered hybrid cloud solutions in one way or another. I often see clients with some parts, or applications, running on-premises that need to call AWS services. I'm working with an client with an application running on-premises. The application gather data from different sources, and then upload the data files to an Amazon S3 Bucket. The data is imported and analyzed in the cloud. Up till now I needed to create an IAM User and generate long lived credentials that the on-premises part could use. That is until the recent release of IAM Anywhere.
    - IAM Anywhere rely on Public key Infrastructure (PKI) and exchange x.509 certificates for temporary AWS IAM credentials. You establish a trust between you AWS account and a Certificate Authority (CA), a trust anchor. Certificates issued by that CA can then be used to get credentials. Fields, like the Common Name (CN), in the certificate can be used as conditions in policies to limit what IAM Roles that can be assumed.

## AWS Organizations

- [Simplifying permissions management at scale using tags in AWS Organizations](https://aws.amazon.com/blogs/mt/simplifying-permissions-management-at-scale-using-tags-in-aws-organizations/)
- [Standardize compliance in AWS using DevOps and a Cloud Center of Excellence (CCOE) approach](https://aws.amazon.com/blogs/mt/standardize-compliance-in-aws-using-devops-and-a-cloud-center-of-excellence-ccoe-approach/)
- [blog.wut.dev: Moving AWS Accounts and OUs Within An Organization - Not So Simple!](https://blog.wut.dev/2024/07/05/moving-aws-accounts-within-organization.html)

## AWS Control Tower

- [==AWS Control Tower==](https://aws.amazon.com/controltower/) The easiest way to set up and govern a secure multi-account AWS environment
- [==aws.amazon.com: New – AWS Control Tower Account Factory for Terraform==](https://aws.amazon.com/blogs/aws/new-aws-control-tower-account-factory-for-terraform/)
- [aws.amazon.com: Automate AWS Control Tower landing zone operations using APIs](https://aws.amazon.com/about-aws/whats-new/2023/11/automate-aws-control-tower-zone-operations-apis/)

## AWS Firewalls

- [Automatically block suspicious traffic with AWS Network Firewall and Amazon GuardDuty](https://aws.amazon.com/es/blogs/security/automatically-block-suspicious-traffic-with-aws-network-firewall-and-amazon-guardduty)

## AWS WAF Web Application Firewall

- [AWS WAF - Web Application Firewall](https://aws.amazon.com/waf/)
- [How to Automatically Update Your Security Groups for Amazon CloudFront and AWS WAF by Using AWS Lambda (boto3 python)](http://blogs.aws.amazon.com/security/post/Tx1LPI2H6Q6S5KC/How-to-Automatically-Update-Your-Security-Groups-for-Amazon-CloudFront-and-AWS-W)
- [How to Use AWS WAF to Block IP Addresses That Generate Bad Requests](http://blogs.aws.amazon.com/security/post/Tx223ZW25YRPRKV/How-to-Use-AWS-WAF-to-Block-IP-Addresses-That-Generate-Bad-Requests)
- [How to Reduce Security Threats and Operating Costs Using AWS WAF and Amazon CloudFront](http://blogs.aws.amazon.com/security/post/Tx1G747SE1R2ZWE/How-to-Reduce-Security-Threats-and-Operating-Costs-Using-AWS-WAF-and-Amazon-Clou)
- [AWS WAF sample rules](https://github.com/awslabs/aws-waf-sample)
- [dev.to: AWS WAF (Web Application Firewall): Deep Dive](https://dev.to/aws-builders/aws-waf-web-application-firewall-deep-dive-15bd)

## AWS Secrets Manager

- [How to replicate secrets in AWS Secrets Manager to multiple Regions](https://aws.amazon.com/blogs/security/how-to-replicate-secrets-aws-secrets-manager-multiple-regions/)
- [AWS Secrets Manager controller POC: an EKS operator for automatic rotation of secrets](https://aws.amazon.com/blogs/containers/aws-secrets-manager-controller-poc-an-eks-operator-for-automatic-rotation-of-secrets/)
- [k21academy.com: AWS Secrets Manager](https://k21academy.com/amazon-web-services/aws-solutions-architect/aws-secrets-manager/)

## AWS Vault

- [AWS Vault](https://github.com/99designs/aws-vault) is a tool to securely store and access AWS credentials in a development environment.

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Do you secure your <a href="https://twitter.com/awscloud?ref_src=twsrc%5Etfw">@awscloud</a> access?<br><br>11 secrets hackers don&#39;t want you to know 📈. <br><br>Number 7 will blow your mind 🤯<br><br>A thread 🔽🔽🔽<a href="https://twitter.com/hashtag/AWSCommunity?src=hash&amp;ref_src=twsrc%5Etfw">#AWSCommunity</a></p>&mdash; Andrea Cavagna (@a_cava94) <a href="https://twitter.com/a_cava94/status/1567168785437659137?ref_src=twsrc%5Etfw">September 6, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>