# Infrastructure Provisioning. Infra Management Tools. IaC Infrastructure as Code

1. [Introduction](#introduction)
2. [Local Environment as Code](#local-environment-as-code)
3. [Comparing the Tools](#comparing-the-tools)
4. [Tools](#tools)
5. [Infrastructure as Code using Kubernetes](#infrastructure-as-code-using-kubernetes)
    1. [Config Connector](#config-connector)
6. [Videos](#videos)
7. [Tweets](#tweets)

## Introduction
  - [Platform Engineering Guide - 5 Key Use Cases of Internal Developer Platforms](https://www.techworld-with-nana.com/post/platform-engineering-guide) - *(Related to devops topic)*

- [stackoverflow.blog: Infrastructure as code: Create and configure infrastructure elements in seconds](https://stackoverflow.blog/2021/03/08/infrastructure-as-code-create-and-configure-infrastructure-elements-in-seconds) IaC allows developers to supply IT environments with multiple lines of code and can be deployed in a matter of minutes (in contrast to manual infrastructure, which can take hours if not days to be deployed).
- [invensislearning.com: Infrastructure as a Code Tutorial: How it Works, Types, and Best Practices](https://www.invensislearning.com/blog/infrastructure-as-a-code-tutorial)
- [agileconnection.com: Infrastructure as Code: The Foundation of Effective DevOps](https://www.stickyminds.com/?utm_source=d7ac)
- [cloudify.co: Infrastructure As Code – Is It REALLY Enough For DevOps? IAC DevOps Best Practices 🌟](https://docs.cloudify.co)
- [bridgecrew.io: 5 tips for securely adopting infrastructure as code](https://bridgecrew.io/blog/5-tips-for-securely-adopting-infrastructure-as-code)
- [redhat.com: Pull vs. push in automated VM provisioning: What you need to know](https://www.redhat.com/en/blog/pull-push-provisioning-cicd) Understanding the different techniques for provisioning virtual machines in the CI/CD process is essential for enterprise architects planning deployment automation into their designs.
- [itnext.io: Platform-as-Code: how it relates to Infrastructure-as-Code and what it enables](https://itnext.io/platform-as-code-how-it-compares-with-infrastructure-as-code-and-what-it-enables-2684b348be2e)
- [daffodilsw.medium.com: What is Infrastructure Automation in DevOps?](https://daffodilsw.medium.com/what-is-infrastructure-automation-in-devops-d9681870b07d)
- [thenewstack.io: IaC Cloud Misconfiguration Tools too Noisy without Context](https://thenewstack.io/iac-cloud-misconfiguration-tools-too-noisy-without-context)
- [==freecodecamp.org: Infrastructure as Code - Full Course== 🌟🌟](https://www.freecodecamp.org/news/what-is-infrastructure-as-code)
- [faun.pub: The best Infrastructure as Code tools for 2021](https://faun.pub/the-best-infrastructure-as-code-tools-for-2021-b37c323e89f0)
- [==alpacked.io: Infrastructure as Code in DevOps== 🌟](https://alpacked.io/blog/infrastructure-as-code-for-devops) Key driving force of efficient application delivery.
- [devops.com: Updating and Managing Infrastructure-as-Code (IaC)](https://devops.com/updating-and-managing-infrastructure-as-code-iac)
- [thenewstack.io: GUIs, CLI, APIs: Learn Basic Terms of Infrastructure-as-Code](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code)
- [thenewstack.io: Infrastructure-as-Code: Increase Security, Scale Development](https://thenewstack.io/infrastructure-as-code-increase-security-scale-development)
- [==thenewstack.io: Struggling with IT Staff Leaving? Try Infrastructure as Code== 🌟](https://thenewstack.io/struggling-with-it-staff-leaving-try-infrastructure-as-code) With IaC, the organization retains critical knowledge of deployment and updates in code repositories, lessening the impact of any one expert leaving
- [devopscube.com: Immutable Infrastructure Explained For Beginners](https://devopscube.com/immutable-infrastructure)
- [medium.com/@bunnyshell: How to Overcome Infrastructure as Code (IaC) Challenges](https://medium.com/@bunnyshell/how-to-overcome-infrastructure-as-code-iac-challenges-f4947be7cde2)
- [dzone.com/articles: A Beginner's Guide to Infrastructure as Code 🌟](https://dzone.com/articles/a-beginners-guide-to-infrastructure-as-code) In this article, take an in-depth look at how Infrastructure as Code (IaC) works, its benefits, and common challenges.
- [javacodegeeks.com: Infrastructure as Code: Best Tools For 2023 Included](https://www.javacodegeeks.com/2023/03/infrastructure-as-code-best-tools-for-2023-included.html)
- [thenewstack.io: Infrastructure as Code or Cloud Platforms — You Decide!](https://thenewstack.io/infrastructure-as-code-or-cloud-platforms-you-decide)
- [infoworld.com: 5 priorities that cut cloud costs and improve IT ops](https://www.infoworld.com/article/2338245/5-priorities-that-cut-cloud-costs-and-improve-it-ops.html) With infrastructure as code, virtual desktop infrastructure, and a proactive approach to incident management, you can help keep cloud costs reasonable.
- [spacelift.io: Why Generic CI/CD Tools Will Not Deliver Successful IaC](https://spacelift.io/blog/infrastructure-as-code-with-generic-ci-cd)
- [matt-rickard.com: Infrastructure as Code Will be Written by AI](https://mattrickard.com/infrastructure-as-code-will-be-written-by-ai)
- [thenewstack.io: Achieve GitOps on Day One with IaC Automation](https://thenewstack.io/achieve-gitops-on-day-one-with-iac-automation) GitOps helps redefine how we manage infrastructure and application deployments in environments where precision, automation and transparency are vital.
- [medium.com/@faisalkuzhan: DAY_43/90 => Infrastructure as Code(IaC)](https://medium.com/@faisalkuzhan/day-43-90-infrastructure-as-code-iac-5a826258ee4b)
- [build5nines.com: Benefits of Convention over Configuration for IaC Deployment Projects](https://build5nines.com/benefits-of-convention-over-configuration-for-iac-deployment-projects)
- [levelup.gitconnected.com: Short: Using IaC over Clickops](https://levelup.gitconnected.com/short-using-iac-over-clickops-229e919b5373)

## Local Environment as Code

- [thenewstack.io: Local Environment-as-Code: Is It Possible Yet?](https://thenewstack.io/local-environment-as-code-is-it-possible-yet)

## Comparing the Tools

- [clickittech.com: Infrastructure as Code Tools, what are the best IaC tools? 🌟](https://www.clickittech.com/devops/infrastructure-as-code-tools)
- [intellipaat.com: Terraform vs Ansible: Key Differences Between Terraform and Ansible 🌟](https://intellipaat.com/blog/terraform-vs-ansible-difference)
- [clickittech.com: Terraform vs CloudFormation: The Final battle 🌟](https://www.clickittech.com/devops/terraform-vs-cloudformation)
- [k21academy.com: Terraform vs Ansible: Working, Difference, Provisioning 🌟](https://k21academy.com/devops/terraform-vs-ansible)
- [cncf.io: Cloudformation vs. Terraform: Which is better?](https://www.cncf.io/blog/2021/04/06/cloudformation-vs-terraform-which-is-better)
- [cloudify.co: Ansible Vs Terraform 🌟](https://docs.cloudify.co)
- [techcommunity.microsoft.com: Infrastructure as Code (IaC): Comparing the Tools](https://techcommunity.microsoft.com/blog/itopstalkblog/infrastructure-as-code-iac-comparing-the-tools/3205045)
- [spacelift.io: Terraform vs. Ansible : Key Differences and Comparison of Tools](https://spacelift.io/blog/ansible-vs-terraform)
- [env0.com: Ansible vs Terraform: Choose One or Use Both?](https://www.env0.com/blog/ansible-vs-terraform-when-to-choose-one-or-use-them-together)
- [awstrainingwithjagan.com: Comprehensive Comparison of Top Infrastructure as Code (IaC) Tools](https://awstrainingwithjagan.com/infrastructure-as-code-tool-comparison)

## Tools
  - [Pulumi: Infrastructure as Code in Any Programming Language](https://github.com/pulumi/pulumi) 🌟 - Pulumi is an open-source Infrastructure as Code (IaC) tool that allows users to define and manage cloud infrastructure using familiar programming languages like Python, JavaScript, TypeScript, Go, C#, and Java. It enables developers to provision and manage resources across various cloud providers and services with the power of general-purpose programming languages, offering benefits like code reuse, testing, and better developer workflows.
  - [Terraform 1.15: Flexible Module Management, Deprecation Warnings, and Windows ARM64 Support](https://t.co/C6uicr7ZPS) - *(Related to terraform topic)*
  - [IBM IAM for AI Agents](https://t.co/EKsVgKA4xn) - *(Related to ai-agents-mcp topic)*
  - [Terraform Enterprise 2.0](https://t.co/UmacHpStqI) - *(Related to terraform topic)*
  - [Scale with Confidence Using Terraform: Better Cost Visibility, Stronger Governance, and Less Operational Overhead](https://t.co/y414rbxM7l) - *(Related to terraform topic)*
  - [Terraform for Standardizing AWS Deployments](https://t.co/5E4FLUyh98) - *(Related to terraform topic)*
  - [Terraform & OpenTofu Skill for AI Agents](https://github.com/antonbabenko/terraform-skill) - *(Related to terraform topic)*
  - [Enterprise-Scale Azure Subscription Vending Using Azure Verified Modules (AVM)](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/enterprise%e2%80%91scale-azure-subscription-vending-using-azure-verified-modules-avm/4507751) - *(Related to azure topic)*
  - [CloudCanvas - Diagramming for Cloud Infrastructure](https://cloudcanvas.co) - *(Related to cloud-arch-diagrams topic)*
  - [AZVerify: Bridging Azure Resources, Bicep Templates, and Diagrams with GitHub Copilot](https://github.com/Azure/AZVerify) - *(Related to azure topic)*
  - [Azure Landing Zone IaC Accelerator Release Notes](https://azure.github.io/Azure-Landing-Zones/accelerator/accelerator-release-notes) 🌟 - Official release notes for the Azure Landing Zone Infrastructure as Code (IaC) Accelerator, detailing changes, particularly breaking changes that may require user action. It also links to release notes for individual components like PowerShell modules and Terraform/Bicep starter modules, and highlights new features such as a local management group for Azure Local/Sovereign workloads.
  - [Terraform 2.0 in Practice: Using AI to Generate Infrastructure as Code](https://markaicode.com/terraform-ai-infrastructure-as-code) - *(Related to terraform topic)*
  - [Transitioning an Existing Azure Environment to the Azure Landing Zone Reference Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/transition) - *(Related to azure topic)*
  - [Terraform Provider for Google Cloud 7.0 is now GA](https://www.hashicorp.com/en/blog/terraform-provider-for-google-cloud-7-0-is-now-ga) - *(Related to terraform topic)*
  - [AWS Organizations: The Key to Managing Your Cloud Infrastructure Effectively](https://awsfundamentals.com/blog/aws-organizations-the-key-to-managing-your-cloud-infrastructure-effectively) - *(Related to aws topic)*
  - [Terraform Azure Resource IPAM Module](https://registry.terraform.io/modules/hlokensgard/res-ipam/azure/latest) - *(Related to terraform topic)*
  - [Ephemeral Values in Terraform](https://nedinthecloud.com/2025/07/01/ephemeral-values-in-terraform) - *(Related to terraform topic)*
  - [Deploying Virtual Networks Across Tenants Using Azure Virtual Network Manager](https://techcommunity.microsoft.com/blog/azurenetworkingblog/deploying-virtual-networks-across-tenants-using-azure-virtual-network-manager-ip/4410161) - *(Related to azure topic)*
  - [Announcing Public Preview of Terraform Export from the Azure Portal](https://techcommunity.microsoft.com/blog/AzureToolsBlog/announcing-public-preview-of-terraform-export-from-the-azure-portal/4409889) - *(Related to terraform topic)*
  - [Announcing Public Preview of Terraform Export from the Azure Portal](https://techcommunity.microsoft.com/blog/azuretoolsblog/announcing-public-preview-of-terraform-export-from-the-azure-portal/4409889) - *(Related to terraform topic)*
  - [ClusterClass: Experimental Feature for Streamlined Cluster Lifecycle Management in Cluster API](https://cluster-api.sigs.k8s.io/tasks/experimental-features/cluster-class) - *(Related to kubernetes topic)*
  - [Enhancing Infrastructure as Code Generation with GitHub Copilot for Azure](https://techcommunity.microsoft.com/blog/AzureDevCommunityBlog/enhancing-infrastructure-as-code-generation-with-github-copilot-for-azure/4388514) 🌟 - This blog post introduces an updated experience for GitHub Copilot for Azure, simplifying the generation and updating of Infrastructure as Code (IaC) files using Bicep or Terraform. The new release allows users to directly update project details, hosting, services, configurations, and environment variables through a streamlined UI, improving workflow efficiency and reducing errors compared to previous methods relying solely on Copilot Chat.
  - [Subscription Vending Implementation Guidance](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) - *(Related to azure topic)*
  - [DevOps Roadmap for 2026](https://github.com/milanm/DevOps-Roadmap) - *(Related to devops topic)*
  - [Awesome Sysadmin](https://github.com/awesome-foss/awesome-sysadmin) - *(Related to devops-tools topic)*
  - [Terraform Best Practices](https://github.com/antonbabenko/terraform-best-practices) - *(Related to terraform topic)*
  - [Enhanced Local IDE Experience for AWS Step Functions](https://aws.amazon.com/blogs/compute/introducing-an-enhanced-local-ide-experience-for-aws-step-functions) - *(Related to aws topic)*
  - [TerraSchema: Generate JSON Schema from Terraform Configurations](https://github.com/HewlettPackard/terraschema) - *(Related to terraform topic)*
  - [Terraform Module Releaser GitHub Action](https://github.com/techpivot/terraform-module-releaser) - A GitHub Action designed to automate the versioning, release process, and documentation generation for Terraform modules, particularly useful in monorepo environments.
  - [The Maester - Terraform Module](https://cloudtips.nl/the-maester-terraform-module-8c68b2b68c51) - *(Related to terraform topic)*
  - [Azure Landing Zone IaC Accelerator](https://azure.github.io/Azure-Landing-Zones/accelerator) 🌟 - The Azure Landing Zone IaC Accelerator provides opinionated modules for deploying and managing Azure landing zone architecture core platform capabilities using Bicep or Terraform. It supports Azure DevOps and GitHub for version control and bootstraps a continuous delivery environment, guiding users through planning, prerequisites, bootstrapping, and running the deployment.
  - [Azure Landing Zone Technical Documentation](https://azure.github.io/Azure-Landing-Zones) - *(Related to azure topic)*
  - [Announcing General Availability of Terraform Azure Verified Modules for Platform Landing Zone (ALZ)](https://techcommunity.microsoft.com/blog/azuretoolsblog/announcing-general-availability-of-terraform-azure-verified-modules-for-platform/4366027) - *(Related to terraform topic)*
  - [Azure Landing Zone - Microsoft Cloud Adoption Framework](https://learn.microsoft.com/nb-no/azure/cloud-adoption-framework/ready/landing-zone) - *(Related to azure topic)*
  - [The Beginner’s Guide to the Ansible Inventory](https://www.packetcoders.io/the-beginners-guide-to-the-ansible-inventory) - *(Related to ansible topic)*
  - [Terraform Provider for Azure IPAM](https://github.com/XtratusCloud/terraform-provider-azureipam) - *(Related to terraform topic)*
  - [AWS Well-Architected IaC Analyzer](https://github.com/aws-samples/well-architected-iac-analyzer) - *(Related to aws-architecture topic)*

- [==Checkmarx/kics==](https://github.com/Checkmarx/kics) Find security vulnerabilities, compliance issues, and infrastructure misconfigurations early in the development cycle of your infrastructure-as-code with KICS by Checkmarx. KICS stands for Keeping Infrastructure as Code Secure, it is open source and is a must-have for any cloud native project.
- [==gofireflyio/aiac== 🌟](https://github.com/gofireflyio/aiac) **Artificial Intelligence Infrastructure-as-Code Generator.**
- [==github.com/gofireflyio/aiac: AIaC==](https://github.com/gofireflyio/aiac) Artificial Intelligence Infrastructure-as-Code Generator.

## Infrastructure as Code using Kubernetes
  - [The Definitive Guide to Importing Your Cloud Resources into IaC](https://blog.cloudgeni.ai/the-definitive-guide-to-importing-your-cloud-resources-into-iac) 🌟 - This guide provides a comprehensive approach to migrating existing cloud infrastructure, built manually via portals or CLI commands, into an Infrastructure as Code (IaC) format, specifically mentioning Terraform. It highlights the importance of IaC for auditability, security, access control, documentation, and disaster recovery, contrasting it with the limitations of 'clickOps'.
  - [How Kubernetes Operators Fit into Platform Building and When Traditional IaC Isn't Enough](https://www.thestack.technology/how-kubernetes-operators-fit-into-to-platform-building-and-when-traditional-iac-isnt-enough) - *(Related to kubernetes-operators-controllers topic)*
  - [The DevOps Bottleneck: Why IaC Orchestration is the Missing Piece](https://devops.com/the-devops-bottleneck-why-iac-orchestration-is-the-missing-piece) 🌟 - This article discusses how the increasing pace of feature development in DevOps often strains infrastructure teams, creating a bottleneck. It argues that Infrastructure as Code (IaC) orchestration is crucial for scaling DevOps practices effectively and preventing team burnout, moving beyond just automation to true orchestration.
  - [Azure Cloud Adoption Framework: Platform Landing Zone Implementation Options](https://learn.microsoft.com/en-gb/azure/cloud-adoption-framework/ready/landing-zone/implementation-options) - *(Related to azure topic)*

- [medium.com/nerd-for-tech: Kubernetes: Declaratively Deploying Infrastructure (IaC)](https://medium.com/nerd-for-tech/kubernetes-declaratively-deploying-infrastructure-iac-789f14d999c6) “Declaring the Kubes”

### Config Connector

- [==cloud.google.com/config-connector==](https://docs.cloud.google.com/config-connector/docs/overview) Config Connector is an open source Kubernetes addon that allows you to manage Google Cloud resources through Kubernetes.
- [medium.com/globant: Infrastructure as Code using Kubernetes](https://medium.com/globant/infrastructure-as-code-using-kubernetes-d3d329446517)
    - Config Connector (KCC) is a solution to maintain Cloud Resources as Infrastructure as Code. It is built as an Open Source initiative and runs on Kubernetes clusters. As such, it leverages YAML files to maintain and operate such resources.
    - Config Connector has two versions: an Add-On for Google Kubernetes Engine (GKE) clusters and a manual installation for other Kubernetes distributions.

## Videos

- [youtube: Mitchell Hashimoto: The Inside Story of HashiCorp's IaC Journey | The IaC Podcast](https://www.youtube.com/watch?v=--RRpw_6onA)

??? note "Click to expand!"

	<center markdown="1">

	<iframe width="560" height="315" src="https://www.youtube.com/embed/POPP2WTJ8es" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/EIOuIwKS0P0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/--RRpw_6onA?si=UNaIShD8z-_ZLCwt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

	</center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center markdown="1">

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Jeez, people in my timeline arguing about the merits of CDK vs. Pulumi and I&#39;m just waiting for you all to get on my level. <a href="https://t.co/S3PU7FGuw2">pic.twitter.com/S3PU7FGuw2</a></p>&mdash; Corey Quinn (@QuinnyPig) <a href="https://twitter.com/QuinnyPig/status/1470810573298274307?ref_src=twsrc%5Etfw">December 14, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Do you use the AWS, GCP, or Azure web consoles beyond getting started with a new cloud provider? If so, why not an automation tool such as Terraform or Cloud Formation? <a href="https://t.co/5LIZSTcNpG">pic.twitter.com/5LIZSTcNpG</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1483820927402004484?ref_src=twsrc%5Etfw">January 19, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

</center>
</details>
  - [IaC and OpenShift Virtualization handshake (using Terraform for VMs on OCP)](https://medium.com/@nidhibansal26/iac-and-openshift-virtualization-handshake-c0a4ada79af5) 🌟 - Explora la integración de Infraestructura como Código (IaC) con Terraform para gestionar Máquinas Virtuales (VMs) en OpenShift Virtualization, demostrando un 'handshake' efectivo entre ambas tecnologías.
  - [Building a FinOps-Ready Azure Landing Zone: Infrastructure Foundations for Cost Optimization](https://techcommunity.microsoft.com/blog/AzureInfrastructureBlog/building-a-finops-ready-azure-landing-zone-infrastructure-foundations-for-cost-o/4411706) - *(Related to finops topic)*