# Hashicorp Packer & Terraform. K8s Boilerplates 

{=="It's not controversial to provision resources with code. It shouldn't be controversial to deploy and manage resources with code" (Jaana Dogan)==}

- [HashiCorp Learning Resources Reference Guide](#hashicorp-learning-resources-reference-guide)
- [Packer](#packer)
- [Terraform](#terraform)
	- [HCL](#hcl)
	- [CDK Cloud Development Kit Terraform](#cdk-cloud-development-kit-terraform)
	- [Terraform Infracost](#terraform-infracost)
	- [Awesome Terraform](#awesome-terraform)
	- [Terraform Cheat Sheets](#terraform-cheat-sheets)
	- [Best Practices](#best-practices)
	- [Terraform and CI/CD](#terraform-and-cicd)
	- [Terraform Boilerplates](#terraform-boilerplates)
	- [Terraform and Kubernetes](#terraform-and-kubernetes)
	- [Terraform Kubernetes Boilerplates](#terraform-kubernetes-boilerplates)
		- [Hashicorp Terraform Kubernetes Collection](#hashicorp-terraform-kubernetes-collection)
		- [Learnk8s Terraform and Managed Kubernetes](#learnk8s-terraform-and-managed-kubernetes)
		- [OpenShift and Terraform](#openshift-and-terraform)
		- [Other Boilerplates](#other-boilerplates)
	- [Terraform Kubernetes Operator](#terraform-kubernetes-operator)
	- [Terraform K3s Boilerplates](#terraform-k3s-boilerplates)
	- [Terraform GKE Boilerplates](#terraform-gke-boilerplates)
	- [Terraform and AWS](#terraform-and-aws)
		- [Terraform EKS Boilerplates](#terraform-eks-boilerplates)
		- [AWSCC. Terraform AWS Cloud Control Provider](#awscc-terraform-aws-cloud-control-provider)
		- [AWS Control Tower Account Factory for Terraform (AFT)](#aws-control-tower-account-factory-for-terraform-aft)
	- [Terraform with Azure](#terraform-with-azure)
		- [Terraform AKS Boilerplates](#terraform-aks-boilerplates)
	- [Terraform and Apache Kafka](#terraform-and-apache-kafka)
	- [Terraform Video Tutorials](#terraform-video-tutorials)
- [CDK for Terraform](#cdk-for-terraform)
- [Graph Visualization Software](#graph-visualization-software)
- [Terraform Modules](#terraform-modules)
	- [Segment AWS Stack Terraform Modules](#segment-aws-stack-terraform-modules)
- [Terraform Providers](#terraform-providers)
- [Terraform Quality Checks](#terraform-quality-checks)
- [Enforce Policy with Sentinel](#enforce-policy-with-sentinel)
- [Reverse terraform with Terraformer](#reverse-terraform-with-terraformer)
- [Terraform Tools](#terraform-tools)
- [Terraform Frameworks](#terraform-frameworks)
	- [Kubestack Terraform GitOps Framework](#kubestack-terraform-gitops-framework)
	- [Gruntwork Terragrunt](#gruntwork-terragrunt)
	- [Terraspace](#terraspace)
- [Tweets](#tweets)

## HashiCorp Learning Resources Reference Guide
- [hashicorp.com: HashiCorp Learning Resources Reference Guide 🌟](https://www.hashicorp.com/blog/hashicorp-learning-resources-reference-guide) Read this curated list of HashiCorp learning resources to help practitioners and organizations better understand the cloud operating model.
## Packer
* [packer.io](https://packer.io/)
* [packer.io docs](https://www.packer.io/docs/index.html)
* [computingforgeeks.com: Build AWS EC2 Machine Images (AMI) With Packer and Ansible](https://computingforgeeks.com/build-aws-ec2-machine-images-with-packer-and-ansible/)

## Terraform
* [Wikipedia.org: Terraform Software](https://en.wikipedia.org/wiki/Terraform_(software))
* [terraform.io](https://www.terraform.io/)
* [Terraform Registry - registry.terraform.io: Terraform Providers and Modules 🌟](https://registry.terraform.io/)
* [medium.com: Why should Terraform be one of your DevOps tools?](https://medium.com/devopslinks/why-should-terraform-be-one-of-your-devops-tools-29ae15861b1f)
* [Dzone: intro to terraform](https://dzone.com/articles/intro-to-terraform-way-of-infra-as-code)
* [blog.teemo.co: Terraform in 10 commands](https://blog.teemo.co/terraform-in-10-commands-e737dfd8bf31)
* [dzone: Terraform - IAC Tool](https://dzone.com/articles/terraform-iac-tool) See why Terraform's declarative approach to automation makes it a competitive tool for automating the creation of your infrastructure.
* [udemy.com: Learn DevOps: Infrastructure Automation With Terraform](https://www.udemy.com/learn-devops-infrastructure-automation-with-terraform/)
* [Dzone: managing infrastructure at scale with terraform](https://dzone.com/articles/managing-infrastructure-at-scale-with-terraform)
* [Dzone: What's new in Terraform v0.12](https://dzone.com/articles/whats-new-in-terraform-v012)
* [terraform-infraestructura.readthedocs.io](https://terraform-infraestructura.readthedocs.io)
* [Testing Infrastructure as Code on Localhost](https://www.hashicorp.com/resources/testing-infrastructure-as-code-on-localhost/)
* [Why we use Terraform and not Chef, Puppet, Ansible, SaltStack, or CloudFormation](https://blog.gruntwork.io/why-we-use-terraform-and-not-chef-puppet-ansible-saltstack-or-cloudformation-7989dad2865c)
* [Terraform, can you keep a secret?](https://cloudonaut.io/terraform-can-you-keep-a-secret/) Did you know that Terraform state can - and most likely does - contain sensitive data?
* [Terraform 0.13 Beta released!](https://discuss.hashicorp.com/t/terraform-0-13-beta-released)
* [medium: AWS API Gateway](https://medium.com/@hashiroulap/terraform-aws-api-gateway-6d86a010f359)
* [medium: Integration of AWS, Terraform, and GitHub for Automated Deployment Infrastructure](https://medium.com/@akshayavb99/integration-of-aws-terraform-and-github-for-automated-deployment-infrastructure-da0a19ff4e86)
* [medium: Automation of Cloud-Terraform](https://medium.com/@sandupatlaabhilash1747/automation-of-cloud-terraform-5a299fb785bb)
* [hashicorp.com: Custom Variable Validation in Terraform 0.13](https://www.hashicorp.com/blog/custom-variable-validation-in-terraform-0-13/)
* [medium: Terraform for Network Engineers: Should you be implementing Infrastructure as Code?](https://medium.com/hashicorp-engineering/terraform-for-network-engineers-should-you-be-implementing-infrastructure-as-code-73667d27d3b8)
* [hashicorp.com: Learn How to Import Infrastructure Into Terraform](https://www.hashicorp.com/blog/import-infrastructure-into-terraform)
* [Bridgecrew: Misconfigured Terraform Modules Are a Security Issue](https://thenewstack.io/bridgecrew-all-these-misconfigured-terraform-modules-are-a-security-issue/)
* [medium - Infrastructure-As-Code: But You Don’t Have to Write That Code](https://medium.com/@duplocloud/infrastructure-as-code-but-you-dont-have-to-write-that-code-87ec4fe94863)
* [Manage Active Directory Objects with the New Windows AD Provider for HashiCorp Terraform](https://www.hashicorp.com/blog/manage-active-directory-objects-new-windows-ad-provider-hashicorp-terraform) Official HashiCorp-maintained Active Directory provider for Terraform. Terraform is a great way to bring some sanity to AD management so we’re excited to make this official. 
* [Terraform Feature Flags & Environment Toggle Design Patterns](https://build5nines.com/terraform-feature-flags-environment-toggle-design-patterns/)
* [dzone: Immutable Infrastructure CI/CD Using Hashicorp Terraform and Jenkins](https://dzone.com/articles/immutable-infrastructure-cicd-using-hashicorp-terr) This extensive article should leave few questions unanswered about creating your infrastructure.
* [Announcing Databricks Labs Terraform integration on AWS and Azure](https://databricks.com/blog/2020/09/11/announcing-databricks-labs-terraform-integration-on-aws-and-azure.html)
* [hashicorp.com: Announcing 11 Verified Providers for Terraform](https://www.hashicorp.com/blog/announcing-11-verified-providers-for-terraform)
* [learn.hashicorp.com: Call APIs with Terraform Providers. Learn how to use and create custom Terraform Providers in a new collection of tutorials on HashiCorp Learn 🌟](https://learn.hashicorp.com/collections/terraform/providers)
* [globaldatanet.com: Terraform CI/CD Best Practices](https://globaldatanet.com/blog/terraform-cicd-best-practices)
* [devblogs.microsoft.com: What is infrastructure as code? 🌟](https://devblogs.microsoft.com/devops/what-is-infrastructure-as-code/)
* [k21academy.com: Why Terraform? Not Chef, Ansible, Puppet, CloudFormation? 🌟](https://k21academy.com/terraform-iac/why-terraform-not-chef-ansible-puppet-cloudformation/)
* [hashicorp.com: New Terraform Tutorial: Sensitive Input Variables 🌟](https://www.hashicorp.com/blog/terraform-sensitive-input-variables) A new tutorial on HashiCorp Learn shows how to protect sensitive data with Terraform.
* [AWS Lambda the Terraform Way](https://github.com/nsriram/lambda-the-terraform-way) The objective of this tutorial is to understand AWS Lambda in-depth, beyond executing functions, using Terraform. This tutorial walks through setting up Terraform, dependencies for AWS Lambda, getting your first Lambda function running, many of its important features & finally integrating with other AWS services.
* [adinermie.com: Publishing TFSec Terraform Quality Controls to Azure DevOps Pipelines 🌟](https://adinermie.com/publishing-tfsec-terraform-quality-controls-to-azure-devops-pipelines/)
* [medium: Don’t Forget to Restrict Outbound Traffic with Terraform and Sentinel](https://medium.com/hashicorp-engineering/dont-forget-to-restrict-outbound-traffic-with-terraform-and-sentinel-c74a99129dae)
* [K3s Private Cluster 🌟](https://github.com/sagittaros/terraform-k3s-private-cloud)
* [hashicorp.com: New Terraform Tutorial: Terraform Outputs 🌟](https://www.hashicorp.com/blog/tutorial-terraform-outputs) Learn how to output data about your infrastructure.
* [trek10.com: Beginner's Guide to Using Terraform with AWS 🌟](https://www.trek10.com/blog/beginners-guide-to-using-terraform-with-aws) Beginner tips for Terraform on AWS, common problem areas and misunderstandings that we coach and train internally.
* [env0.com: We’re Opensourcing Terratag to Make Multicloud Resource Tagging Easier](https://www.env0.com/blog/were-opensourcing-terratag-to-make-multicloud-resource-tagging-easier)
* [hashicorp.com: Terraform Mono Repo vs. Multi Repo: The Great Debate](https://www.hashicorp.com/blog/terraform-mono-repo-vs-multi-repo-the-great-debate) Learn about the pros and cons of using mono repositories and multi repositories along with the most logical use case for each.
* [terraform.io: Cloud Adoption Framework for Azure - Terraform module](https://registry.terraform.io/modules/aztfmod/caf/azurerm/latest)
* [arnaudlheureux.io: Migrating Azure CAF landing zones to Terraform 0.13](https://www.arnaudlheureux.io/2020/10/02/migrating-azure-caf-landing-zones-on-terraform-0-13/)
* [tfenv](https://github.com/tfutils/tfenv) Terraform version manager inspired by rbenv
* [dev.to: Packer and Terraform with Immutable Infrastructure](https://dev.to/cloudskills/packer-and-terraform-with-immutable-infrastructure-47ja)
* [medium: Terraform: How to Use Conditionals to Dynamically Create Resources](https://medium.com/swlh/terraform-how-to-use-conditionals-for-dynamic-resources-creation-6a191e041857) …don’t struggle looking for if/else statements, you won’t find them…
* [hashicorp.com: Testing HashiCorp Terraform 🌟](https://www.hashicorp.com/blog/testing-hashicorp-terraform) Learn testing strategies for HashiCorp Terraform modules and configuration, and learn how to run tests against infrastructure.
* [cloudify.co: Ansible, Terraform And Cloudify](https://cloudify.co/blog/ansible-terraform-and-cloudify/)
* [automateinfra.com: How to Launch multiple EC2 instances on AWS using Terraform count and for_each](https://automateinfra.com/2021/03/22/how-to-launch-multiple-ec2-instances-on-aws-using-terraform/)
* [morethancertified.com: More Consistent Terraform Runs With Docker](https://morethancertified.com/terraform-in-docker)
* [deloitte.com: Infrastructure as Code (IaC) con Terraform](https://www2.deloitte.com/es/es/blog/todo-tecnologia/2021/infrastructure-as-code-iac-con-terraform.html) Automatización, escalado, optimización y ahorro en tu factura cloud
* [docs.gitlab.com: GitLab managed Terraform State 🌟](https://docs.gitlab.com/ee/user/infrastructure/terraform_state.html) Gitlab Terraform now share tfstate directly on gitlab.
* [flowfactor.be: What do you know about Terraform modules?](https://www.flowfactor.be/2021/03/18/what-do-you-know-about-terraform-modules/)
* [medium: How to manage infrastructure as code (IaC) with Terraform on AWS? 🌟](https://medium.com/workfall/how-to-manage-infrastructure-as-code-iac-with-terraform-on-aws-1fa6cd6bccfe)
* [accurics.com: Terraform Security: Improving IaC Scans with Terraform Plan Output](https://www.accurics.com/blog/terrascan-blog/terraform-security-improving-iac-scans-with-terraform-plan-output)
* [hashicorp.com: Modern Infrastructure Automation with Packer, Terraform, and Consul (video)](https://www.hashicorp.com/resources/modern-infrastructure-automation-with-packer-terraform-and-consul)
* [hashicorp.com: New Terraform Tutorials: Getting Started with the Helm and Datadog Providers 🌟](https://www.hashicorp.com/blog/getting-started-with-the-helm-and-datadog-terraform-providers)
* [hashicorp.com: How can I prevent configuration drift?](https://www.hashicorp.com/resources/how-can-i-prevent-configuration-drift) What causes our infrastructure's configuration to drift over time away from our original intended state? And how does Terraform help?
* [hashicorp.com: New Terraform Tutorials: Getting Started with the Helm and Datadog Providers](https://www.hashicorp.com/blog/getting-started-with-the-helm-and-datadog-terraform-providers)
* [hashicorp.com: Share Modules Across Organizations with Terraform Enterprise](https://www.hashicorp.com/blog/share-modules-across-organizations-terraform-enterprise) Terraform Enterprise now offers users the ability to consume private modules across organizations, providing greater management consistency. 
* [freecodecamp.org: What is Terraform? Learn Terraform and Infrastructure as Code](https://www.freecodecamp.org/news/what-is-terraform-learn-infrastructure-as-code/)
* [hashicorp.com: Announcing HashiCorp Terraform 0.15 General Availability](https://www.hashicorp.com/blog/announcing-hashicorp-terraform-0-15-general-availability)
* [learn.hashicorp.com: Manage Private Environments with Terraform Cloud Agents](https://learn.hashicorp.com/tutorials/terraform/cloud-agents)
* [itnext.io: How to use Terraform to create a small-scale Cloud Infrastructure 🌟](https://itnext.io/how-to-use-terraform-to-create-a-small-scale-cloud-infrastructure-abf54fabc9dd)
* [acloudguru.com: Securing your multi-cloud Terraform pipelines with policy-as-code](https://acloudguru.com/blog/engineering/securing-your-multi-cloud-terraform-pipelines-with-policy-as-code)
* [youtube: GitOps for infrastructure using GitHub and Terraform Cloud 🌟](https://www.youtube.com/watch?v=W_PmtDm4IXk&ab_channel=RobertdeBock)
* [medium: Terraform — Remote States Overview 🌟](https://medium.com/devops-mojo/terraform-remote-states-overview-what-is-terraform-remote-state-storage-introduction-936223a0e9d0) What is Terraform Remote State — Introduction to Terraform Remote Storage!
* [prcode.co.uk: Connect Azure MySQL to Private Endpoint with Terraform](https://prcode.co.uk/2021/04/29/connect-azure-mysql-to-private-endpoint-with-terraform/)
* [infoq.com: Cloudflare Improves Automated Terraform Generation Tool 🌟](https://www.infoq.com/news/2021/04/cloudflare-terraform/) Cloudflare recently released an updated version of their [cf-terraforming](https://github.com/cloudflare/cf-terraforming) tool. This tool streamlines generating Terraform HCL from existing Cloudflare resources. The new release simplifies the generation process and introduces changes to better future proof the tool.
* [hashicorp.com: Building Azure Resources with TypeScript Using the CDK for Terraform](https://www.hashicorp.com/blog/building-azure-resources-with-typescript-using-the-cdk-for-terraform) Learn a quick method for getting started with the Cloud Development Kit (CDK) for Terraform using TypeScript as infrastructure code and provisioning on Microsoft Azure.
* [acloudguru.com: How to use Terraform outputs and inputs](https://acloudguru.com/blog/engineering/how-to-use-terraform-inputs-and-outputs)
* [scalr.com: An alternative to Terraform Cloud and Terraform Enterprise](https://scalr.com/) Scalr is a remote state & operations backend for Terraform with full CLI support, integration with OPA, a hierarchical configuration model, and quality of life features.
* [itnext.io: My Journey to HashiCorp Certified: Terraform Associate](https://itnext.io/my-journey-to-hashicorp-certified-terraform-associate-f91f397a01e0)
* [infoq.com: Managing Infrastructure from Kubernetes with the HashiCorp Terraform Operator](https://www.infoq.com/news/2020/04/terraform-operator-kubernetes/)
* [medium: Protect your Terraform State](https://medium.com/the-innovation/protect-your-terraform-state-a974027a4bb0) The right way!
* [hashicorp.com: Terraform AzureAD Provider Now Supports Microsoft Graph](https://www.hashicorp.com/blog/terraform-azuread-provider-now-supports-microsoft-graph) Version 1.5.0 of the Terraform AzureAD provider lets you manage your Azure Active Directory resources using the Microsoft Graph API.
* [nitheeshp.dev: Practical CI/CD Guide to Deploying AWS Infrastructure 🌟](https://nitheeshp.dev/series/terraform)
	* [nitheeshp.dev: Practical CI/CD Guide to Deploying AWS Infrastructure through Terraform - Multi Environment Deployment - Part 1 🌟](https://nitheeshp.dev/practical-cicd-guide-to-deploying-aws-infrastructure-through-terraform-part-1-1) Introduction
	* [nitheeshp.dev: Practical CI/CD Guide to Deploying AWS Infrastructure through Terraform - Multi Environment Deployment - Part 2 🌟](https://nitheeshp.dev/practical-cicd-guide-to-deploying-aws-infrastructure-through-terraform-multi-environment-deployment-part-2) Terraform Directory Structure
	* [nitheeshp.dev: Practical CI/CD Guide to Deploying AWS Infrastructure through Terraform - Multi Environment Deployment - Part 3 🌟](https://nitheeshp.dev/practical-cicd-guide-to-deploying-aws-infrastructure-through-terraform-multi-environment-deployment-part-3) Terraform Cloud Configurations
	* [nitheeshp.dev: Practical CI/CD Guide to Deploying AWS Infrastructure through Terraform - Multi Environment Deployment - Part 4 🌟](https://nitheeshp.dev/practical-cicd-guide-to-deploying-aws-infrastructure-through-terraform-multi-environment-deployment-part-4) GitOps
* [hashicorp.com: New Apply User Interface for Terraform Cloud](https://www.hashicorp.com/blog/new-apply-user-interface-for-terraform-cloud) The redesigned interface for HashiCorp Terraform Cloud brings clarity to how your resources, state, and infrastructure operations are represented during a Terraform run.
* [hashicorp.com: New Terraform Tutorials on HashiCorp Learn](https://www.hashicorp.com/blog/new-terraform-tutorials-on-hashicorp-learn) From working with providers, to managing resources, to working with Terraform on AWS, we have a lot of new hands-on Terraform exercises to try.
* [hashicorp.com: Announcing Support for Amazon ECS Anywhere in the Terraform AWS Provider](https://www.hashicorp.com/blog/announcing-launch-day-support-for-amazon-ecs-anywhere-terraform-aws-provider) The Terraform AWS provider now supports ECS Anywhere, a new capability in Amazon ECS that supports running and managing container-based applications on customers’ on-premises servers.
* [automateinfra.com: Terraform (Series-1) 🌟](https://automateinfra.com/terraform-series1/) 
	* [automateinfra.com: Terraform (Series-2)](https://automateinfra.com/terraform-series2/)
	* [automateinfra.com: Terraform (Series-3)](https://automateinfra.com/terraform-series3/)
	* [automateinfra.com: Terraform (Series-4)](https://automateinfra.com/terraform-series-5/)
* [hashicorp.com: Announcing HashiCorp Terraform 1.0 General Availability 🌟](https://www.hashicorp.com/blog/announcing-hashicorp-terraform-1-0-general-availability)
* [acloudguru.com: What does the Terraform 1.0 release mean for you?](https://acloudguru.com/blog/engineering/what-does-the-terraform-1-0-release-mean-for-you)
* [thenewstack.io: Terraform 1.0 Reflects What HashiCorp Has Learned About Infrastructure-as-Code](https://thenewstack.io/terraform-1-0-reflects-what-hashicorp-has-learned-about-infrastructure-as-code/)
* [medium: terraform | git commit -m “all the secrets” | sops tool for managing secrets 🌟](https://medium.com/cloudandthings/terraform-git-commit-m-all-the-secrets-5dfea9b111de) - [sops: Simple and flexible tool for managing secrets 🌟](https://github.com/mozilla/sops)
* [fsgeorgee.medium.com: Growing out of Heroku to Terraform, Docker and AWS](https://fsgeorgee.medium.com/growing-out-of-heroku-to-terraform-docker-and-aws-69e66df4132d) Heroku is great, but how about using Terraform, AWS, Docker and have full control over the entire stack?
* [learn.hashicorp.com: y Serverless Applications with AWS Lambda and API Gateway 🌟](https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway)
* [harness.io: Terraform 201: What It Is, Tutorial, and More 🌟](https://harness.io/blog/devops/terraform-201-tutorial)
* [medium: Terraform Zero to Hero](https://medium.com/tech-guides/terraform-zero-to-hero-733f6860bb9a)
* [learn.hashicorp.com: Configure Default Tags for AWS Resources 🌟](https://learn.hashicorp.com/tutorials/terraform/aws-default-tags)
* [terraform-hcloud-dualstack-k8s: Hetzner Dual-Stack Kubernetes Cluster](https://github.com/tibordp/terraform-hcloud-dualstack-k8s) (Unofficial) Terraform module for a dual-stack Kubernetes cluster on Hetzner Cloud
* [hashicorp.com: Beta Support for CRDs in the Terraform Provider for Kubernetes](https://www.hashicorp.com/blog/beta-support-for-crds-in-the-terraform-provider-for-kubernetes)
* [opensource.com: How I use Terraform and Helm to deploy the Kubernetes Dashboard 🌟](https://opensource.com/article/21/8/terraform-deploy-helm) Terraform can deploy Helm Charts. Is it right for you?
* [about.gitlab.com: How to use a push-based approach for GitOps with Terraform and AWS ECS and EC2](https://about.gitlab.com/blog/2021/08/10/how-to-agentless-gitops-aws/)
* [opensource.com: My top 5 tips for setting up Terraform 🌟](https://opensource.com/article/21/8/terraform-tips) These are the lessons I've learned after five years with Terraform.
* [==bridgecrew.io: Terraform security 101: Best practices for secure infrastructure as code== 🌟](https://bridgecrew.io/blog/terraform-security-101-best-practices-for-secure-infrastructure-as-code/)
* [rpadovani.com: How to make Terraform waiting for cloud-init to finish on EC2 without SSH](https://rpadovani.com/terraform-cloudinit) Terraform is a powerful tool. However, it has some limitations: since it uses AWS APIs, it doesn’t have a native way to check if an EC2 instance has completed to run cloud-init before marking it as ready. A possible workaround is asking Terraform to SSH on the instance, and wait until it is able to perform a connection before marking the instance as ready.
* [hashicorp.com: Cisco, Citrix, and Fortinet Among New Verified Terraform Providers](https://www.hashicorp.com/blog/cisco-citrix-fortinet-among-new-verified-terraform-providers)
* [terraform-best-practices.com 🌟](https://www.terraform-best-practices.com/)
* [bridgecrew.io: Advanced Terraform security: Pro tips for secure infrastructure as code](https://bridgecrew.io/blog/advanced-terraform-security-pro-tips-for-secure-infrastructure-as-code)
* [hub.qovery.com: Terraform is Not the Golden Hammer](https://hub.qovery.com/guides/engineering/terraform-not-the-golden-hammer/)
* [scalefactory.com: Failing faster with terraform](https://scalefactory.com/blog/2021/10/13/failing-faster-with-terraform/) **Terraform validation rules**. Terraform is an extremely powerful tool, but with great power comes great opportunity to break stuff, or whatever Uncle Ben said. With a single command a developer can deploy hundreds of resources in an instant, and when that developer inevitably configured the inputs wrong Terraform makes it easy to patch or rollback that mistake. But you know what’s better than recovering from mistakes? Never making the mistake in the first place.
* [medium.com/geekculture: Managing Infra with Terraform](https://medium.com/geekculture/managing-infra-with-terraform-275968590fa4)
* [hashicorp.com: AWS and HashiCorp Collaborate on New Terraform Modules](https://www.hashicorp.com/blog/aws-hashicorp-collaborate-new-terraform-modules)
* [learn.hashicorp.com: Automate Terraform with GitHub Actions](https://learn.hashicorp.com/tutorials/terraform/github-actions) Automate infrastructure deployments with CI/CD using Terraform and GitHub Actions
* [shipa.io: Terraform meets AppOps 🌟](https://shipa.io/development/terraform-meets-appops) Terraform is the popular choice among teams
* [bitslovers.com: Terraform Output – What you should know](https://www.bitslovers.com/terraform-output/)
* [hashicorp.com: Terraform Cloud Variable Sets Beta Now Available](https://www.hashicorp.com/blog/terraform-cloud-variable-sets-beta-now-available) HashiCorp Terraform Cloud variable sets let you simplify the management of reusable variables across an entire organization. This feature is now available in public beta.
* [devops.com: Building on Terraform: Evolution, not Revolution](https://devops.com/building-on-terraform-evolution-not-revolution/)
* [==acloudguru.com: How to use GitHub Actions to automate Terraform==](https://acloudguru.com/blog/engineering/how-to-use-github-actions-to-automate-terraform)

### HCL
* [github.com/hashicorp/hcl: HCL](https://github.com/hashicorp/hcl) HCL is the HashiCorp configuration language.
* [octopus.com: Introduction to HCL and HCL tooling](https://octopus.com/blog/introduction-to-hcl-and-hcl-tooling)

### CDK Cloud Development Kit Terraform
* [terraform-cdk 🌟](https://github.com/hashicorp/terraform-cdk) CDK (Cloud Development Kit) for Terraform allows developers to use familiar programming languages to define cloud infrastructure and provision it through HashiCorp Terraform.
* [infoq.com: cdk-terraform - Cloud Development Kit Can Now Generate Terraform Configurations Using TypeScript and Python](https://www.infoq.com/news/2020/07/cdk-terraform/)
* [hashicorp.com: CDK for Terraform: Enabling Python & TypeScript Support](https://www.hashicorp.com/blog/cdk-for-terraform-enabling-python-and-typescript-support)
* [hashicorp.com: Announcing CDK for Terraform 0.1](https://www.hashicorp.com/blog/announcing-cdk-for-terraform-0-1)

### Terraform Infracost
- [Infracost 🌟](https://github.com/infracost/infracost) If you use Terraform to provision your Kubernetes clusters, you might find infracost interesting. Infracost estimates hourly and monthly costs for a Terraform project. It helps you to see the cost breakdown and compare different deployment options upfront. 
- [A Guide to Cloud Cost Optimization with HashiCorp Terraform 🌟](https://www.hashicorp.com/blog/a-guide-to-cloud-cost-optimization-with-hashicorp-terraform) The Terraform AWS provider now supports Code Signing for AWS Lambda, which involves digitally signing code artifacts and verifying at deployment.

### Awesome Terraform
* [github.com/shuaibiyy/awesome-terraform](https://github.com/shuaibiyy/awesome-terraform)
* [github.com/Azure/awesome-terraform](https://github.com/Azure/awesome-terraform)

### Terraform Cheat Sheets
* [Terraform Cheat Sheets](cheatsheets.md)

### Best Practices
* [github.com/ozbillwang/terraform-best-practices](https://github.com/ozbillwang/terraform-best-practices)

### Terraform and CI/CD
* [dzone: Manage Multiple Environments With Terraform Workspaces](https://dzone.com/articles/manage-multiple-environments-with-terraform-worksp) Read this tutorial to learn about easily setting up Terraform to manage your CI/CD environments and create workspaces.
* [hashicorp.com: Announcing Support for Code Signing for AWS Lambda in the Terraform AWS Provider](https://www.hashicorp.com/blog/announcing-support-for-aws-lambda-code-signing-in-the-terraform-aws-provider)

### Terraform Boilerplates
- https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples
- https://github.com/hashicorp/terraform-provider-aws/tree/main/examples
- https://github.com/hashicorp/terraform-provider-awscc/tree/main/examples/resources
- [awesomeopensource.com: Terraform Aws Multi Az Subnets](https://awesomeopensource.com/project/cloudposse/terraform-aws-multi-az-subnets)
- [github.com/cloudposse?q=terraform-](https://github.com/cloudposse?q=terraform-)
- [devopshubproject/azure-terraform-ansible](https://github.com/devopshubproject/azure-terraform-ansible) This repo contains script which will help you to provision full functioning ansible lab environment on azure using terraform
- etc
### Terraform and Kubernetes
* [hashicorp.com: New Terraform Tutorials on Provisioning and Managing Kubernetes Clusters 🌟](https://www.hashicorp.com/blog/new-terraform-tutorials-on-provisioning-and-managing-kubernetes-clusters) Explore a new collection of Terraform tutorials that can help you through your Kubernetes adoption journey.
* [hodovi.cc: Creating a Low Cost Managed Kubernetes Cluster for Personal Development using Terraform](https://hodovi.cc/blog/creating-low-cost-managed-kubernetes-cluster-personal-development-terraform/)
* [Deploying and Managing a Minimal App in a Kubernetes Cluster with Terraform and Ansible](https://www.hashicorp.com/resources/deploying-managing-minimal-app-kubernetes-cluster-terraform-ansible/)
* [Deploy Any Resource With The New Kubernetes Provider for HashiCorp Terraform](https://www.hashicorp.com/blog/deploy-any-resource-with-the-new-kubernetes-provider-for-hashicorp-terraform/)
* [kubernetes.io blog: Working with Terraform and Kubernetes](https://kubernetes.io/blog/2020/06/working-with-terraform-and-kubernetes/)
* [phillipsj.net: Dynamically Loaded Terraform Providers 🌟](https://www.phillipsj.net/posts/dynamically-loaded-terraform-providers/) Have you ever been faced with some situations where you need information from your Terraform execution to configure a provider ? Like spinning up a kubernetes cluster and dynamically deploying to it with Terraform? Check this short article for more !
* [hashicorp.com: Announcing Version 2.0 of the Kubernetes and Helm Providers for HashiCorp Terraform 🌟](https://www.hashicorp.com/blog/announcing-version-2-0-kubernetes-and-helm-providers-for-hashicorp-terraform)
* [hashicorp.com: Wait Conditions in the Kubernetes Provider for HashiCorp Terraform](https://www.hashicorp.com/blog/wait-conditions-in-the-kubernetes-provider-for-hashicorp-terraform)
* [itnext.io: Terraform: don’t use kubernetes provider with your cluster resource! 🌟](https://itnext.io/terraform-dont-use-kubernetes-provider-with-your-cluster-resource-d8ec5319d14a)
* [hashicorp.com: Announcing General Availability of the HashiCorp Terraform Cloud Operator for Kubernetes 🌟](https://www.hashicorp.com/blog/announcing-general-availability-hashicorp-terraform-cloud-operator-for-kubernetes)
* [learnk8s.io/kubernetes-terraform: Creating Kubernetes clusters with Terraform](https://learnk8s.io/kubernetes-terraform)
* [blog.kasten.io: Working with Kubernetes and Terraform Part 1: Concepts Behind Terraform and Kubernetes](https://blog.kasten.io/concepts-behind-terraform-and-kubernetes)
* [thenewstack.io: A Better Way to Provision Kubernetes Using Terraform](https://thenewstack.io/a-better-way-to-provision-kubernetes-using-terraform/)
* [medium: Deploy Infrastructure with the Terraform Cloud Operator for Kubernetes 🌟](https://medium.com/avmconsulting-blog/deploy-infrastructure-with-the-terraform-cloud-operator-for-kubernetes-a179ea4dbbfe)

{==

### Terraform Kubernetes Boilerplates
#### Hashicorp Terraform Kubernetes Collection
- https://github.com/hashicorp/learn-terraform-provision-aks-cluster
- https://github.com/hashicorp/learn-terraform-provision-eks-cluster
	- [spacelift.io: How to Provision an AWS EKS Kubernetes Cluster with Terraform](https://spacelift.io/blog/how-to-provision-aws-eks-kubernetes-cluster-with-terraform) 
- https://github.com/hashicorp/learn-terraform-provision-gke-cluster
- https://github.com/hashicorp/learn-terraform-deploy-nginx-kubernetes-provider
- https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/kubernetes 🌟
- https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/kubernetes/nodes-on-internal-network 🌟

#### Learnk8s Terraform and Managed Kubernetes
* [learnk8s.io/terraform-gke: Provisioning Kubernetes clusters on AWS with Terraform and GKE 🌟](https://learnk8s.io/terraform-gke) Fully automated dev, staging, prod clusters with GKE and the GKE Ingress in a single click.
* [learnk8s.io/terraform-eks: Provisioning Kubernetes clusters on AWS with Terraform and EKS 🌟](https://learnk8s.io/terraform-eks) Fully automated dev, test, prod environments with EKS, Terraform and the ALB Ingress Controller. 
* [learnk8s.io/terraform-aks: Provisioning Kubernetes clusters on AWS with Terraform and AKS 🌟](https://learnk8s.io/terraform-aks) Fully utomated dev and prod clusters complete with an Ingress controller in a single command.
* [learnk8s.io/terraform-lke: Provisioning Kubernetes clusters on Linode with Terraform 🌟](https://learnk8s.io/terraform-lke)

==}

#### OpenShift and Terraform
* [Dzone: Platform as Code With Openshift and Terraform](https://dzone.com/articles/platform-as-code-with-openshift-amp-terraform) Learn how to set up a pipeline workflow with Openshift and the Terraform infrastructure-as-code tool to configure builds and deployments.

#### Other Boilerplates
- [gist.github.com/chadmcrowell: AKS w/Virtual Nodes (ACI)](https://gist.github.com/chadmcrowell/4d11b8a56aba3bdc32ea73c31104357b)
- [ahgraber/homelab-terraform](https://github.com/ahgraber/homelab-terraform) Bootstrap VMs with Terraform & vSphere provider. Use Terraform to provision VMs in vsphere and call ansible to configure hosts. The second half of this project (deploying a k3s cluster via gitops) is [here](https://github.com/ahgraber/homelab-gitops-k3s).
- [garutilorenzo/k3s-aws-terraform-cluster](https://github.com/garutilorenzo/k3s-aws-terraform-cluster) Deploy an high available K3s cluster on Amazon AWS
- [poseidon/typhoon](https://github.com/poseidon/typhoon) **Typhoon is a minimal and free Kubernetes distribution with Terraform.**

### Terraform Kubernetes Operator
* [infoq.com: Managing Infrastructure from Kubernetes with the HashiCorp Terraform Operator](https://www.infoq.com/news/2020/04/terraform-operator-kubernetes/)

{==

### Terraform K3s Boilerplates
* [Global K3s Deployment on Packet Baremetal 🌟](https://github.com/c0dyhi11/k3s-linkerd) This repository contains Terraform scripts to deploy K3s and LinkerD on Packet baremetal servers spanning the globe.

### Terraform GKE Boilerplates
* [learnk8s.io/terraform-gke  🌟](https://learnk8s.io/terraform-gke) Provisioning Kubernetes clusters on GCP with Terraform and GKE. Fully automated dev, test, prod environments with Google Kubernetes Engine (GKE) + container-native load balancing? The guide goes into the details of how you can provision your infrastructure with Terraform and how you can route live traffic with the GKE Ingress controller. By the end Kristijan M. will teach you how you can have: 
	- The creation of 3 environments (dev, test, prod) automated
	- A cluster that can handle live traffic with the GKE Ingress controller.
	- GKE Ingress enabled with container-native load balancing.
	- All source code and knowledge to build your own infra.
* [circleci.com: Infrastructure as Code, part 1: create a Kubernetes cluster with Terraform](https://circleci.com/blog/learn-iac-part1/)
    - [circleci.com: Infrastructure as Code, part 2: build Docker images and deploy to Kubernetes with Terraform](https://circleci.com/blog/learn-iac-part02/)
    - [circleci.com: Infrastructure as Code, part 3: automate Kubernetes deployments with CI/CD and Terraform](https://circleci.com/blog/learn-iac-part3/)

==}

### Terraform and AWS
* [Dzone: terraform and AWS](https://dzone.com/articles/terraform-and-aws)
* [Dzone: terraform with AWS](https://dzone.com/articles/terraform-with-aws)
* [hashicorp.com: Terraforming RDS: What Instacart Learned Managing Over 50 AWS RDS PostgreSQL Instances with Terraform](https://www.hashicorp.com/resources/terraform-what-instacart-learned-managing-over-50-aws-rds-postgresql-instances)
* [Dzone: provisioning servers in cloud with terraform](https://dzone.com/articles/provisioning-servers-in-cloud-with-terraform)
* [Dzone: how to deploy apps effortlessly with **packer and terraform**](https://dzone.com/articles/how-to-deploy-apps-effortlessly-with-packer-and-te)
* [stories.schubergphilis.com: (Terraform) AWS management using your Google account](https://stories.schubergphilis.com/terraform-aws-management-using-your-google-account-cfe5ea70c75)
* [thenewstack.io: Terraform on AWS: Multi-Account Setup and Other Advanced Tips](https://thenewstack.io/terraform-on-aws-multi-account-setup-and-other-advanced-tips/)
* [medium: How to Provision AWS Infrastructure with Terraform? 🌟](https://medium.com/faun/provisioning-aws-infrastructure-with-terraform-6ab885fb3fcb)
* [middlewareinventory.com: Terraform import All AWS Security Groups – How to 🌟](https://www.middlewareinventory.com/blog/terraform-import-securitygroup-aws/)
* [hashicorp.com: Terraform AWS Provider Continues to Expand Coverage](https://www.hashicorp.com/blog/terraform-aws-provider-continues-to-expand-coverage) During 2021, HashiCorp and Amazon Web Services have partnered to bring hundreds of new services and features to the Terraform providers for AWS and AWS Cloud Control.

{==

#### Terraform EKS Boilerplates
* [learnk8s.io/terraform-eks 🌟](https://learnk8s.io/terraform-eks) Fully automated dev, test, prod environments with EKS, Terraform and the ALB Ingress Controller. 
* [github.com/maddevsio/aws-eks-base: Boilerplate for a basic AWS infrastructure with EKS cluster 🌟](https://github.com/maddevsio/aws-eks-base) This boilerplate contains the know-how of the Mad Devs team for the rapid deployment of a Kubernetes cluster, supporting services, and the underlying infrastructure in the Amazon cloud.
* [github.com/aws-samples/aws-eks-accelerator-for-terraform: AWS EKS Accelerator for Terraform 🌟](https://github.com/aws-samples/aws-eks-accelerator-for-terraform) The AWS EKS Accelerator for Terraform is a framework designed to help deploy and operate secure multi-account, multi-region AWS environments. The power of the solution is the configuration file which enables the users to provide a unique terraform state for each cluster and manage multiple clusters from one repository.

==}

#### AWSCC. Terraform AWS Cloud Control Provider
* [awscc](https://registry.terraform.io/providers/hashicorp/awscc/latest) Lifecycle management of AWS resources powered by the AWS Cloud Control API. This provider is fully generated from the available CloudFormation resource definitions and is maintained internally by the HashiCorp AWS Provider team.
* [hashicorp.com: Announcing Terraform AWS Cloud Control Provider Tech Preview](https://www.hashicorp.com/blog/announcing-terraform-aws-cloud-control-provider-tech-preview) This new provider for HashiCorp Terraform — built around the AWS Cloud Control API — is designed to bring new services to Terraform faster.

#### AWS Control Tower Account Factory for Terraform (AFT)
* [==aws.amazon.com: New – AWS Control Tower Account Factory for Terraform==](https://aws.amazon.com/blogs/aws/new-aws-control-tower-account-factory-for-terraform/)
* [hashicorp.com: HashiCorp Teams with AWS on New Control Tower Account Factory for Terraform](https://www.hashicorp.com/blog/hashicorp-teams-with-aws-on-new-control-tower-account-factory-for-terraform) AWS Control Tower Account Factory for HashiCorp Terraform (AFT), the evolution of Terraform Landing Zones, offers an easy way to set up and govern a secure, multi-account AWS environment.
* [==aws.amazon.com: AWS Control Tower==](https://aws.amazon.com/controltower/) The easiest way to set up and govern a secure multi-account AWS environment

### Terraform with Azure
- [medium: Using Terraform with Azure — the right way](https://medium.com/01001101/using-terraform-with-azure-the-right-way-35af3b51a6b0)
- [thomasthornton.cloud: Deploy Terraform using GitHub Actions to Azure](https://thomasthornton.cloud/2021/03/19/deploy-terraform-using-github-actions-into-azure/)
- [github.com/kuhlman-labs/terraform-azurerm-landing-zone](https://github.com/kuhlman-labs/terraform-azurerm-landing-zone) A curated collection of Terraform azurerm modules

{==

#### Terraform AKS Boilerplates
- [learnk8s.io/terraform-aks 🌟](https://learnk8s.io/terraform-aks)
- [itnext.io: How We Used Terraform to Create and Manage a HA AKS Kubernetes Cluster in Azure](https://itnext.io/how-we-used-terraform-to-create-and-manage-a-ha-aks-kubernetes-cluster-in-azure-812f64896c08) Learn how to use Terraform to manage a highly-available Azure AKS Kubernetes cluster with Azure AD integration and Calico network policies enabled.
- [medium: Using Terraform with Azure — the right way](https://medium.com/01001101/using-terraform-with-azure-the-right-way-35af3b51a6b0)
- [thomasthornton.cloud: Deploy Terraform using GitHub Actions to Azure](https://thomasthornton.cloud/2021/03/19/deploy-terraform-using-github-actions-into-azure/)
- [github.com/kuhlman-labs/terraform-azurerm-landing-zone](https://github.com/kuhlman-labs/terraform-azurerm-landing-zone) A curated collection of Terraform azurerm modules
- [github.com/stacksimplify/azure-aks-kubernetes-masterclass 🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass)
	- [**Boilerplate: 25-Azure-DevOps-Terraform-Azure-AKS** 🌟🌟🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass/tree/master/25-Azure-DevOps-Terraform-Azure-AKS)
	- [PDF presentation 🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass/tree/master/ppt-presentation)
<!--
	```terraform="01-main.tf"
resource "azurerm_virtual_network" "example" { # (1) 
name                = "${var.environment}-network"
location            = azurerm_resource_group.aks_rg.location
resource_group_name = azurerm_resource_group.aks_rg.name
address_space       = ["10.x.x.0/22"]
}
resource "azurerm_subnet" "internal" { # (2) 
name                 = "internal"
virtual_network_name = azurerm_virtual_network.example.name
resource_group_name  = azurerm_resource_group.aks_rg.name
address_prefixes     = ["10.x.x.0/24"]
}
```

```terraform="07-aks-cluster.tf"
network_profile {  # (3)
load_balancer_sku = "Standard"
network_plugin = "azure"  # Azure CNI because windows node pools arenot supported by kubenet (unfortunately)
service_cidr = "10.x.x.0/24"
dns_service_ip = "10.x.x.10"
docker_bridge_cidr = "172.17.0.1/16" # Default. You can reuse this range across different AKS clusters.  
}
```

1.  VNet
2.  Subnet nodes (and pods with Azure CNI network plugin)
3.  Network Profile
-->
- [Azure-Samples/private-aks-cluster-terraform-devops 🌟](https://github.com/Azure-Samples/private-aks-cluster-terraform-devops) **This sample shows how to create a private AKS cluster using Terraform and Azure DevOps.**
- [build5nines.com: Terraform: Create an AKS Cluster 🌟](https://build5nines.com/terraform-create-an-aks-cluster/)

==}

### Terraform and Apache Kafka
- [medium: From AWS CloudFormation to Terraform: Migrating Apache Kafka](https://medium.com/riskified-technology/from-aws-cloudformation-to-terraform-migrating-apache-kafka-32bdabdbaa59)

### Terraform Video Tutorials
- [youtube: Terraform Tutorial for beginners | AWS Infrastructure as Code | Github Actions 🌟](https://www.youtube.com/playlist?list=PLlvAxgO7JdIXAzHx887zl-4no4X-CtiFu)

## CDK for Terraform
- [CDK for Terraform 🌟](https://github.com/hashicorp/terraform-cdk) CDK (Cloud Development Kit) for Terraform allows developers to use familiar programming languages to define cloud infrastructure and provision it through HashiCorp Terraform.
- [hashicorp.com: GKE Cluster Setup with CDK for Terraform](https://www.hashicorp.com/blog/gke-cluster-setup-with-cdk-for-terraform) Learn how to provision a Google Kubernetes Engine (GKE) cluster and prepare it for application deployment using TypeScript via CDK for Terraform.

## Graph Visualization Software
- The [terraform graph command](https://www.terraform.io/docs/cli/commands/graph.html) is used to generate a visual representation of either a configuration or execution plan. The output is in the DOT format, which can be used by [GraphViz](https://graphviz.org) to generate charts.
- [graphviz.org](https://graphviz.org/) 
- [edotor.net](https://edotor.net/)
- [dreampuf.github.io/GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/)
- [graphviz.online](https://graphviz.online/)

## Terraform Modules 
- [offensive-terraform.github.io: Offensive Terraform Modules 🌟](https://offensive-terraform.github.io/offensive-terraform.github.io/) Automated multi step offensive attack modules with Infrastructure as Code(IAC)
- [digitalocean.com: How To Build a Custom Terraform Module](https://www.digitalocean.com/community/tutorials/how-to-build-a-custom-terraform-module)

### Segment AWS Stack Terraform Modules
- [The Segment AWS Stack](https://segment.com/blog/the-segment-aws-stack/)
- [segmentio/stack](https://github.com/segmentio/stack) A set of Terraform modules for configuring production infrastructure with AWS


## Terraform Providers
- [Junos-terraform: JUNOS Terraform Automation Framework (JTAF)](https://github.com/Juniper/Junos-terraform) 
- [mitchellh/terraform-provider-multispace](https://github.com/mitchellh/terraform-provider-multispace) Terraform Provider for cascading runs across multiple workspaces.

## Terraform Quality Checks
- [adinermie.com: Publishing GitHub Super-Linter Terraform Quality Checks to Azure DevOps Pipelines](https://adinermie.com/publishing-github-super-linter-terraform-quality-checks-to-azure-devops-pipelines/)

## Enforce Policy with Sentinel
- [learn.hashicorp.com: Enforce Policy with Sentinel](https://learn.hashicorp.com/collections/terraform/policy#sentinel)

## Reverse terraform with Terraformer 
- [github.com/GoogleCloudPlatform/terraformer 🌟](https://github.com/GoogleCloudPlatform/terraformer) A CLI tool that generates tf/json and tfstate files based on existing infrastructure (reverse Terraform).

## Terraform Tools
- [Brainboard 🌟](https://www.brainboard.co/) Interesting solution for building infrastructure visually before generating terraform code automatically from the designed architecture 
- [terrascan 🌟](https://runterrascan.io/) Use terrascan to detect compliance and security violations
- [tfsec 🌟](https://tfsec.dev) a static analysis security scanner for your Terraform code
	- [youtube: Using tfsec and Jenkins to Secure Your Terraform Code](https://www.youtube.com/watch?v=hbMVGEw0HpE&ab_channel=CloudBeesTV)
	- https://github.com/darinpope/jenkins-example-terraform
	- https://www.jenkins.io/changelog-stable/#v2.289.3 
- [Rover - Terraform Visualizer 🌟](https://github.com/im2nguyen/rover) Interactive Terraform visualization. State and configuration explorer.
	- [hashicorp.com: Rover - Terraform Visualizer](https://www.hashicorp.com/resources/terraform-plan-interactive-configuration-and-state-visualization-with-rover) 
- [cloudify.co: Cloudify and Terraform Integration. Supercharge Your Terraform Templates](https://cloudify.co/terraform-integration/) Significantly extend Terraform usability with Cloudify's plugin and enjoy end-to-end automation and avoid costly blueprint transformation.
- [cloudquery.io: Announcing CloudQuery Terraform Drift Detection](https://www.cloudquery.io/blog/announcing-cloudquery-terraform-drift-detection)

## Terraform Frameworks
### Kubestack Terraform GitOps Framework
- [==Kubestack: Terraform GitOps Framework== 🌟](https://www.kubestack.com/)
### Gruntwork Terragrunt 
- [gruntwork.io](https://gruntwork.io/) Build your infrastructure on top of a collection of over 300,000 lines of reusable, battle-tested infrastructure code written in Terraform, Go, Python, and Bash that has been proven in production at hundreds of companies and is maintained and supported by DevOps experts.
- [towardsdatascience.com: State of the Art Infrastructure as Code. Terragrunt](https://towardsdatascience.com/state-of-the-art-infrastructure-as-code-4fbd59d92462) The newest layer of abstraction by Gruntwork that’ll make your life easier. **Gruntwork’s Terragrunt** is a wrapper over Terraform which concentrates on solving your problems of Terraform state management and configuration. It also solves some of the problems around having similar infrastructure deployed in different environments.
- [blog.gruntwork.io: Introducing: The Gruntwork Module, Service, and Architecture Catalogs](https://blog.gruntwork.io/introducing-the-gruntwork-module-service-and-architecture-catalogs-eb3a21b99f70)
- [medium: Terragrunt cheat sheet](https://medium.com/geekculture/terragrunt-cheat-sheet-bedafbf9d61f) **What is Terragrunt?** Terragrunt is a framework on top of Terraform with some new tools out-of-the-box. Thanks to some new files *.hcl and new keywords, you can share variables across terraform modules very easily.
- [pie-r/terragrunt-vs-terraspace](https://github.com/pie-r/terragrunt-vs-terraspace)
- [gruntwork-io/terragrunt-infrastructure-live-example](https://github.com/gruntwork-io/terragrunt-infrastructure-live-example) A repo used to show examples file/folder structures you can use with Terragrunt and Terraform
### Terraspace
- [Terraspace.cloud](https://terraspace.cloud/) Terraspace is a Terraform Framework that optimizes for infrastructure-as-code happiness. It provides an organized structure, conventions over configurations, keeps your code DRY, and adds convenient tooling. Terraspace makes working with Terraform easier and more fun.

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m getting questions about Terraform vs Kubernetes for managing infrastructure resources.<br><br>I make the distinction by treating Terraform as a frontend tool that interacts with control planes that present **its** resources through a declarative interface. Ownership is key.</p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1329552116638117889?ref_src=twsrc%5Etfw">November 19, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">1/ Yesterday we released v2.1.0 of the <a href="https://twitter.com/HashiCorp?ref_src=twsrc%5Etfw">@HashiCorp</a> Terraform provider for <a href="https://twitter.com/HelmPack?ref_src=twsrc%5Etfw">@HelmPack</a> with a cool new feature: diffs of the <a href="https://twitter.com/kubernetesio?ref_src=twsrc%5Etfw">@kubernetesio</a> manifests that Helm is sending to the cluster!<br><br>So, what does this look like? Let&#39;s see ...</p>&mdash; Phil, in the 🏜️ of Arizona (@PhilipSautter) <a href="https://twitter.com/PhilipSautter/status/1378071256969355265?ref_src=twsrc%5Etfw">April 2, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">This is very common. Terraform doesnt give workload portability. It gives workflow portability<br><br>By keeping the same workflow it improves adoption because it doesn’t matter if your managing EC2 or Pagerduty the same lang and tools work. It lowers switching costs through workflow <a href="https://t.co/wSOZYjZMm3">https://t.co/wSOZYjZMm3</a></p>&mdash; Justin Garrison (@rothgar) <a href="https://twitter.com/rothgar/status/1420766310334484480?ref_src=twsrc%5Etfw">July 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Unfortunately I think this is the biggest misconception that orgs have when deciding to adopt Terraform. It&#39;s &quot;cloud agnostic&quot; in the same way that Python is cloud agnostic. You still need vendor specific libraries. The only thing you standardize on is syntax and workflow</p>&mdash; Noah Mercado (@noah_mercado) <a href="https://twitter.com/noah_mercado/status/1420797838129340417?ref_src=twsrc%5Etfw">July 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">It&#39;s not controversial to provision resources with code. It shouldn&#39;t be controversial to deploy and manage resources with code.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1436064355339030540?ref_src=twsrc%5Etfw">September 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Using Terraform with Co-pilot. <a href="https://t.co/0hhbqmMGW1">pic.twitter.com/0hhbqmMGW1</a></p>&mdash; Alex Jones 🚀 (@AlexJonesax) <a href="https://twitter.com/AlexJonesax/status/1457648604768780290?ref_src=twsrc%5Etfw">November 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>