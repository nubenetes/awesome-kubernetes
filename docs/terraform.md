# Hashicorp Packer & Terraform 
- [Packer](#packer)
- [Terraform](#terraform)
    - [Terraform Infracost](#terraform-infracost)
    - [Awesome Terraform](#awesome-terraform)
    - [Terraform Cheat Sheets](#terraform-cheat-sheets)
    - [Best Practices](#best-practices)
    - [Terraform and CI/CD](#terraform-and-cicd)
    - [OpenShift and Terraform](#openshift-and-terraform)
    - [Terraform Kubernetes Operator](#terraform-kubernetes-operator)
    - [Terraform and AWS](#terraform-and-aws)
- [Gruntwork](#gruntwork)

## Packer
* [packer.io](https://packer.io/)
* [packer.io docs](https://www.packer.io/docs/index.html)

## Terraform
* [Wikipedia.org: Terraform Software](https://en.wikipedia.org/wiki/Terraform_(software))
* [terraform.io](https://www.terraform.io/)
* [medium.com: Why should Terraform be one of your DevOps tools?](https://medium.com/devopslinks/why-should-terraform-be-one-of-your-devops-tools-29ae15861b1f)
* [Dzone: intro to terraform](https://dzone.com/articles/intro-to-terraform-way-of-infra-as-code)
* [blog.teemo.co: Terraform in 10 commands](https://blog.teemo.co/terraform-in-10-commands-e737dfd8bf31)
* [dzone: Terraform - IAC Tool](https://dzone.com/articles/terraform-iac-tool) See why Terraform's declarative approach to automation makes it a competitive tool for automating the creation of your infrastructure.
* [udemy.com: Learn DevOps: Infrastructure Automation With Terraform](https://www.udemy.com/learn-devops-infrastructure-automation-with-terraform/)
* [Dzone: managing infrastructure at scale with terraform](https://dzone.com/articles/managing-infrastructure-at-scale-with-terraform)
* [Dzone: What's new in Terraform v0.12](https://dzone.com/articles/whats-new-in-terraform-v012)
* [terraform-infraestructura.readthedocs.io](https://terraform-infraestructura.readthedocs.io)
* [Deploying and Managing a Minimal App in a Kubernetes Cluster with Terraform and Ansible](https://www.hashicorp.com/resources/deploying-managing-minimal-app-kubernetes-cluster-terraform-ansible/)
* [Deploy Any Resource With The New Kubernetes Provider for HashiCorp Terraform](https://www.hashicorp.com/blog/deploy-any-resource-with-the-new-kubernetes-provider-for-hashicorp-terraform/)
* [Testing Infrastructure as Code on Localhost](https://www.hashicorp.com/resources/testing-infrastructure-as-code-on-localhost/)
* [Why we use Terraform and not Chef, Puppet, Ansible, SaltStack, or CloudFormation](https://blog.gruntwork.io/why-we-use-terraform-and-not-chef-puppet-ansible-saltstack-or-cloudformation-7989dad2865c)
* [Terraform, can you keep a secret?](https://cloudonaut.io/terraform-can-you-keep-a-secret/) Did you know that Terraform state can - and most likely does - contain sensitive data?
* [Terraform 0.13 Beta released!](https://discuss.hashicorp.com/t/terraform-0-13-beta-released)
* [medium: AWS API Gateway](https://medium.com/@hashiroulap/terraform-aws-api-gateway-6d86a010f359)
* [medium: Integration of AWS, Terraform, and GitHub for Automated Deployment Infrastructure](https://medium.com/@akshayavb99/integration-of-aws-terraform-and-github-for-automated-deployment-infrastructure-da0a19ff4e86)
* [medium: Automation of Cloud-Terraform](https://medium.com/@sandupatlaabhilash1747/automation-of-cloud-terraform-5a299fb785bb)
* [kubernetes.io blog: Working with Terraform and Kubernetes](https://kubernetes.io/blog/2020/06/working-with-terraform-and-kubernetes/)
* [hashicorp.com: Custom Variable Validation in Terraform 0.13](https://www.hashicorp.com/blog/custom-variable-validation-in-terraform-0-13/)
* [medium: Terraform for Network Engineers: Should you be implementing Infrastructure as Code?](https://medium.com/hashicorp-engineering/terraform-for-network-engineers-should-you-be-implementing-infrastructure-as-code-73667d27d3b8)
* [hashicorp.com: Learn How to Import Infrastructure Into Terraform](https://www.hashicorp.com/blog/import-infrastructure-into-terraform)
* [Bridgecrew: Misconfigured Terraform Modules Are a Security Issue](https://thenewstack.io/bridgecrew-all-these-misconfigured-terraform-modules-are-a-security-issue/)
* [medium - Infrastructure-As-Code: But You Don’t Have to Write That Code](https://medium.com/@duplocloud/infrastructure-as-code-but-you-dont-have-to-write-that-code-87ec4fe94863)
* [cdk-terraform - Cloud Development Kit Can Now Generate Terraform Configurations Using TypeScript and Python](https://www.infoq.com/news/2020/07/cdk-terraform/)
* [Manage Active Directory Objects with the New Windows AD Provider for HashiCorp Terraform](https://www.hashicorp.com/blog/manage-active-directory-objects-new-windows-ad-provider-hashicorp-terraform) Official HashiCorp-maintained Active Directory provider for Terraform. Terraform is a great way to bring some sanity to AD management so we’re excited to make this official. 
* [Infracost](https://github.com/infracost/infracost) Infracost shows hourly and monthly cost estimates for a Terraform project. This helps developers, DevOps et al. quickly see the cost breakdown and compare different deployment options upfront.
* [Terraform Feature Flags & Environment Toggle Design Patterns](https://build5nines.com/terraform-feature-flags-environment-toggle-design-patterns/)
* [dzone: Immutable Infrastructure CI/CD Using Hashicorp Terraform and Jenkins](https://dzone.com/articles/immutable-infrastructure-cicd-using-hashicorp-terr) This extensive article should leave few questions unanswered about creating your infrastructure.
* [Announcing Databricks Labs Terraform integration on AWS and Azure](https://databricks.com/blog/2020/09/11/announcing-databricks-labs-terraform-integration-on-aws-and-azure.html)
* [hashicorp.com: New Terraform Tutorials on Provisioning and Managing Kubernetes Clusters](https://www.hashicorp.com/blog/new-terraform-tutorials-on-provisioning-and-managing-kubernetes-clusters) Explore a new collection of Terraform tutorials that can help you through your Kubernetes adoption journey.
* [hodovi.cc: Creating a Low Cost Managed Kubernetes Cluster for Personal Development using Terraform](https://hodovi.cc/blog/creating-low-cost-managed-kubernetes-cluster-personal-development-terraform/)
* [hashicorp.com: Announcing 11 Verified Providers for Terraform](https://www.hashicorp.com/blog/announcing-11-verified-providers-for-terraform)

### Terraform Infracost
- [Infracost](https://github.com/infracost/infracost) If you use Terraform to provision your Kubernetes clusters, you might find infracost interesting. Infracost estimates hourly and monthly costs for a Terraform project. It helps you to see the cost breakdown and compare different deployment options upfront

### Awesome Terraform
* [github.com/shuaibiyy/awesome-terraform](https://github.com/shuaibiyy/awesome-terraform)
* [github.com/Azure/awesome-terraform](https://github.com/Azure/awesome-terraform)

### Terraform Cheat Sheets
* [Terraform Cheat Sheets](cheatsheets.md)

### Best Practices
* [github.com/ozbillwang/terraform-best-practices](https://github.com/ozbillwang/terraform-best-practices)

### Terraform and CI/CD
* [dzone: Manage Multiple Environments With Terraform Workspaces](https://dzone.com/articles/manage-multiple-environments-with-terraform-worksp) Read this tutorial to learn about easily setting up Terraform to manage your CI/CD environments and create workspaces.

### OpenShift and Terraform
* [Dzone: Platform as Code With Openshift and Terraform](https://dzone.com/articles/platform-as-code-with-openshift-amp-terraform) Learn how to set up a pipeline workflow with Openshift and the Terraform infrastructure-as-code tool to configure builds and deployments.

### Terraform Kubernetes Operator
* [infoq.com: Managing Infrastructure from Kubernetes with the HashiCorp Terraform Operator](https://www.infoq.com/news/2020/04/terraform-operator-kubernetes/)

### Terraform and AWS
* [Dzone: terraform and AWS](https://dzone.com/articles/terraform-and-aws)
* [Dzone: terraform with AWS](https://dzone.com/articles/terraform-with-aws)
* [hashicorp.com: Terraforming RDS: What Instacart Learned Managing Over 50 AWS RDS PostgreSQL Instances with Terraform](https://www.hashicorp.com/resources/terraform-what-instacart-learned-managing-over-50-aws-rds-postgresql-instances)
* [Dzone: provisioning servers in cloud with terraform](https://dzone.com/articles/provisioning-servers-in-cloud-with-terraform)
* [Dzone: how to deploy apps effortlessly with **packer and terraform**](https://dzone.com/articles/how-to-deploy-apps-effortlessly-with-packer-and-te)

## Gruntwork
- [gruntwork.io](https://gruntwork.io/)
- [towardsdatascience.com: State of the Art Infrastructure as Code](https://towardsdatascience.com/state-of-the-art-infrastructure-as-code-4fbd59d92462) The newest layer of abstraction by Gruntwork that’ll make your life easier. Gruntwork’s Terragrunt is a wrapper over Terraform which concentrates on solving your problems of Terraform state management and configuration. It also solves some of the problems around having similar infrastructure deployed in different environments.
- [blog.gruntwork.io: Introducing: The Gruntwork Module, Service, and Architecture Catalogs](https://blog.gruntwork.io/introducing-the-gruntwork-module-service-and-architecture-catalogs-eb3a21b99f70)