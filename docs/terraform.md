# Hashicorp Terraform & Packer. Kubernetes Boilerplates

{==*"It's not controversial to provision resources with code. It shouldn't be controversial to deploy and manage resources with code" (Jaana Dogan)*==}

1. [HashiCorp Learning Resources Reference Guide](#hashicorp-learning-resources-reference-guide)
2. [Packer](#packer)
3. [HashiCorp Cloud Terraform Cloud](#hashicorp-cloud-terraform-cloud)
4. [Blogs and Newsletters](#blogs-and-newsletters)
5. [Terraform](#terraform)
    1. [Antipatterns](#antipatterns)
    2. [Terraform License](#terraform-license)
6. [OpenTOFU vs Terraform](#opentofu-vs-terraform)
7. [Terraform fmt](#terraform-fmt)
8. [terraform taint](#terraform-taint)
9. [terraform stacks](#terraform-stacks)
10. [Terraform and GitHub Actions](#terraform-and-github-actions)
11. [Terraform and GitLab Pipelines](#terraform-and-gitlab-pipelines)
12. [Terraform Testing](#terraform-testing)
13. [Terraform docs](#terraform-docs)
14. [Private Terraform Registries](#private-terraform-registries)
15. [Terraform and Grafana](#terraform-and-grafana)
16. [Terraform and Jenkins](#terraform-and-jenkins)
17. [Alternatives to Terraform](#alternatives-to-terraform)
18. [Managing secrets in your Terraform code](#managing-secrets-in-your-terraform-code)
19. [Terraform Cloud (HCP Terraform)](#terraform-cloud-hcp-terraform)
20. [Hashicorp Infrastructure Cloud](#hashicorp-infrastructure-cloud)
     1. [Alternatives to Terraform Cloud](#alternatives-to-terraform-cloud)
21. [HCL](#hcl)
22. [CDK Cloud Development Kit Terraform](#cdk-cloud-development-kit-terraform)
23. [Providing Terraform with Ansible](#providing-terraform-with-ansible)
24. [Python Boto3 and Terraform](#python-boto3-and-terraform)
25. [Helm Charts in Terraform](#helm-charts-in-terraform)
26. [Terraform Infracost](#terraform-infracost)
27. [Awesome Terraform](#awesome-terraform)
28. [Terraform Cheat Sheets](#terraform-cheat-sheets)
29. [Best Practices](#best-practices)
30. [Terraform and CI/CD. Terraform Workspaces](#terraform-and-cicd-terraform-workspaces)
31. [Terraform Boilerplates](#terraform-boilerplates)
32. [Terraform and Kubernetes](#terraform-and-kubernetes)
33. [Terrafor Cloud Operator](#terrafor-cloud-operator)
34. [Terraform Kubernetes Boilerplates](#terraform-kubernetes-boilerplates)
     1. [Hashicorp Terraform Kubernetes Collection](#hashicorp-terraform-kubernetes-collection)
     2. [Learnk8s Terraform and Managed Kubernetes](#learnk8s-terraform-and-managed-kubernetes)
     3. [OpenShift and Terraform](#openshift-and-terraform)
     4. [Other Boilerplates](#other-boilerplates)
     5. [Terraform Kubernetes Operator](#terraform-kubernetes-operator)
     6. [Terraform K3s Boilerplates](#terraform-k3s-boilerplates)
     7. [Terraform and GCP](#terraform-and-gcp)
         1. [Terraform GKE Boilerplates](#terraform-gke-boilerplates)
     8. [Terraform and AWS](#terraform-and-aws)
         1. [AWS Service Catalog](#aws-service-catalog)
         2. [AWS Observability Accelerator for Terraform](#aws-observability-accelerator-for-terraform)
         3. [Terraform EKS Boilerplates](#terraform-eks-boilerplates)
         4. [AWSCC. Terraform AWS Cloud Control Provider](#awscc-terraform-aws-cloud-control-provider)
         5. [AWS Control Tower Account Factory for Terraform (AFT)](#aws-control-tower-account-factory-for-terraform-aft)
         6. [Porsche Official](#porsche-official)
         7. [AWS Serverless with Terraform](#aws-serverless-with-terraform)
     9. [Terraform with Azure](#terraform-with-azure)
         1. [Azure Terraform Export aztfexport](#azure-terraform-export-aztfexport)
         2. [Azure Landing Zones with Terraform. Azure Network Architecture](#azure-landing-zones-with-terraform-azure-network-architecture)
         3. [Azure Terrafy and AzAPI Terraform Provider](#azure-terrafy-and-azapi-terraform-provider)
         4. [Terraform in Azure DevOps. Azure DevOps with terraform](#terraform-in-azure-devops-azure-devops-with-terraform)
         5. [Terraform Azure Stack Provider](#terraform-azure-stack-provider)
     10. [Terraform for a Data Engineer](#terraform-for-a-data-engineer)
     11. [Terraform AKS Boilerplates](#terraform-aks-boilerplates)
     12. [Terraform and OCI](#terraform-and-oci)
     13. [Terraform and Linode](#terraform-and-linode)
35. [Istio with Terraform](#istio-with-terraform)
36. [Terraform and Minikube](#terraform-and-minikube)
37. [Terraform and Apache Kafka](#terraform-and-apache-kafka)
38. [Terraform and JMeter](#terraform-and-jmeter)
39. [Terraform and OpenVPN on AWS](#terraform-and-openvpn-on-aws)
40. [Terraform Video Tutorials](#terraform-video-tutorials)
41. [CDK for Terraform](#cdk-for-terraform)
42. [Graph Visualization Software](#graph-visualization-software)
43. [Terraform Modules](#terraform-modules)
     1. [Terraform AWS Modules](#terraform-aws-modules)
     2. [Segment AWS Stack Terraform Modules](#segment-aws-stack-terraform-modules)
44. [Terraform Providers](#terraform-providers)
     1. [Terraform AWS Cloud Control Provider](#terraform-aws-cloud-control-provider)
     2. [Terraform Provider for Elastic Cloud](#terraform-provider-for-elastic-cloud)
     3. [Terraform Vault Provider](#terraform-vault-provider)
     4. [Terraform AzureRM](#terraform-azurerm)
45. [Terraform Code Quality. Terraform Quality Checks. Terraform Linters](#terraform-code-quality-terraform-quality-checks-terraform-linters)
46. [Enforce Policy with Sentinel](#enforce-policy-with-sentinel)
47. [Reverse terraform with Terraformer](#reverse-terraform-with-terraformer)
48. [Terraform Tools](#terraform-tools)
49. [Writing Terraform for unsupported resources with TerraCurl](#writing-terraform-for-unsupported-resources-with-terracurl)
50. [Terraform Frameworks](#terraform-frameworks)
     1. [Kubestack Terraform GitOps Framework](#kubestack-terraform-gitops-framework)
     2. [Gruntwork Terragrunt](#gruntwork-terragrunt)
     3. [Terraspace](#terraspace)
51. [Terraform Associate Certification](#terraform-associate-certification)
52. [ChatGPT](#chatgpt)
53. [Images](#images)
54. [Videos](#videos)
55. [Tweets](#tweets)

<center>
<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/468480528&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/raymond-mnt" title="RAYMOND MNT" target="_blank" style="color: #cccccc; text-decoration: none;">RAYMOND MNT</a> · <a href="https://soundcloud.com/raymond-mnt/jimmy-sax-parga-oriental-sax" title="Jimmy Sax - Parga (Oriental sax ).mp3" target="_blank" style="color: #cccccc; text-decoration: none;">Jimmy Sax - Parga (Oriental sax ).mp3</a></div>
</center>

## HashiCorp Learning Resources Reference Guide

- [techbeatly.com: 10 Free Courses to Learn Terraform](https://www.techbeatly.com/terraform-free-courses/)
- [learn.hashicorp.com: What is Infrastructure as Code with Terraform? 🌟](https://learn.hashicorp.com/tutorials/terraform/infrastructure-as-code)

## Packer

- [packer.io](https://packer.io/)
- [packer.io docs](https://www.packer.io/docs/index.html)
- [computingforgeeks.com: Build AWS EC2 Machine Images (AMI) With Packer and Ansible](https://computingforgeeks.com/build-aws-ec2-machine-images-with-packer-and-ansible/)
- [learn.hashicorp.com: Write Packer template for AWS](https://learn.hashicorp.com/tutorials/packer/aws-get-started-build-image)

## HashiCorp Cloud Terraform Cloud


## Blogs and Newsletters

- [weekly.tf: Terraform Weekly](https://weekly.tf)
    - [weekly.tf: Issue #171 - Terramate, Using LLMs to generate Terraform, API Gateway with Lambda, GuardDuty, IMDSv2 at Slack, Azure DevOps Pipelines](https://www.weekly.tf/p/issue-171-terramate-using-llms-to-generate-terraform-api-gateway-with-lambda-guardduty-imdsv2)
- [build5nines.com](https://build5nines.com)
- [nedinthecloud.com](https://nedinthecloud.com)

## Terraform

- [roadmap.sh/terraform 🌟](https://roadmap.sh/terraform)
- [terraform.io](https://www.terraform.io/)
- [Terraform Registry - registry.terraform.io: Terraform Providers and Modules 🌟](https://registry.terraform.io/)
- [terraform-infraestructura.readthedocs.io](https://terraform-infraestructura.readthedocs.io)
- [Why we use Terraform and not Chef, Puppet, Ansible, SaltStack, or CloudFormation](https://blog.gruntwork.io/why-we-use-terraform-and-not-chef-puppet-ansible-saltstack-or-cloudformation-7989dad2865c)
- [Terraform, can you keep a secret?](https://cloudonaut.io/terraform-can-you-keep-a-secret/) Did you know that Terraform state can - and most likely does - contain sensitive data?
- [Terraform 0.13 Beta released!](https://discuss.hashicorp.com/t/terraform-0-13-beta-released)
- [Bridgecrew: Misconfigured Terraform Modules Are a Security Issue](https://thenewstack.io/bridgecrew-all-these-misconfigured-terraform-modules-are-a-security-issue/)
- [Terraform Feature Flags & Environment Toggle Design Patterns](https://build5nines.com/terraform-feature-flags-environment-toggle-design-patterns/)
- [Announcing Databricks Labs Terraform integration on AWS and Azure](https://databricks.com/blog/2020/09/11/announcing-databricks-labs-terraform-integration-on-aws-and-azure.html)
- [learn.hashicorp.com: Call APIs with Terraform Providers. Learn how to use and create custom Terraform Providers in a new collection of tutorials on HashiCorp Learn 🌟](https://learn.hashicorp.com/collections/terraform/providers)
- [devblogs.microsoft.com: What is infrastructure as code? 🌟](https://devblogs.microsoft.com/devops/what-is-infrastructure-as-code/)
- [k21academy.com: Why Terraform? Not Chef, Ansible, Puppet, CloudFormation? 🌟](https://k21academy.com/terraform-iac/why-terraform-not-chef-ansible-puppet-cloudformation/)
- [AWS Lambda the Terraform Way](https://github.com/nsriram/lambda-the-terraform-way) The objective of this tutorial is to understand AWS Lambda in-depth, beyond executing functions, using Terraform. This tutorial walks through setting up Terraform, dependencies for AWS Lambda, getting your first Lambda function running, many of its important features & finally integrating with other AWS services.
- [K3s Private Cluster 🌟](https://github.com/sagittaros/terraform-k3s-private-cloud)
- [trek10.com: Beginner's Guide to Using Terraform with AWS 🌟](https://www.trek10.com/blog/beginners-guide-to-using-terraform-with-aws) Beginner tips for Terraform on AWS, common problem areas and misunderstandings that we coach and train internally.
- [env0.com: We’re Opensourcing Terratag to Make Multicloud Resource Tagging Easier](https://www.env0.com/blog/were-opensourcing-terratag-to-make-multicloud-resource-tagging-easier)
- [terraform.io: Cloud Adoption Framework for Azure - Terraform module](https://registry.terraform.io/modules/aztfmod/caf/azurerm/latest)
- [arnaudlheureux.io: Migrating Azure CAF landing zones to Terraform 0.13](https://www.arnaudlheureux.io/2020/10/02/migrating-azure-caf-landing-zones-on-terraform-0-13/)
- [tfenv](https://github.com/tfutils/tfenv) Terraform version manager inspired by rbenv
- [dev.to: Packer and Terraform with Immutable Infrastructure](https://dev.to/cloudskills/packer-and-terraform-with-immutable-infrastructure-47ja)
- [cloudify.co: Ansible, Terraform And Cloudify](https://cloudify.co/blog/ansible-terraform-and-cloudify/)
- [deloitte.com: Infrastructure as Code (IaC) con Terraform](https://www2.deloitte.com/es/es/blog/todo-tecnologia/2021/infrastructure-as-code-iac-con-terraform.html) Automatización, escalado, optimización y ahorro en tu factura cloud
- [accurics.com: Terraform Security: Improving IaC Scans with Terraform Plan Output](https://www.accurics.com/blog/terrascan-blog/terraform-security-improving-iac-scans-with-terraform-plan-output)
- [freecodecamp.org: What is Terraform? Learn Terraform and Infrastructure as Code](https://www.freecodecamp.org/news/what-is-terraform-learn-infrastructure-as-code/)
- [acloudguru.com: Securing your multi-cloud Terraform pipelines with policy-as-code](https://acloudguru.com/blog/engineering/securing-your-multi-cloud-terraform-pipelines-with-policy-as-code)
- [prcode.co.uk: Connect Azure MySQL to Private Endpoint with Terraform](https://prcode.co.uk/2021/04/29/connect-azure-mysql-to-private-endpoint-with-terraform/)
- [infoq.com: Cloudflare Improves Automated Terraform Generation Tool 🌟](https://www.infoq.com/news/2021/04/cloudflare-terraform/) Cloudflare recently released an updated version of their [cf-terraforming](https://github.com/cloudflare/cf-terraforming) tool. This tool streamlines generating Terraform HCL from existing Cloudflare resources. The new release simplifies the generation process and introduces changes to better future proof the tool.
- [acloudguru.com: How to use Terraform outputs and inputs](https://acloudguru.com/blog/engineering/how-to-use-terraform-inputs-and-outputs)
- [infoq.com: Managing Infrastructure from Kubernetes with the HashiCorp Terraform Operator](https://www.infoq.com/news/2020/04/terraform-operator-kubernetes/)
- [acloudguru.com: What does the Terraform 1.0 release mean for you?](https://acloudguru.com/blog/engineering/what-does-the-terraform-1-0-release-mean-for-you)
- [thenewstack.io: Terraform 1.0 Reflects What HashiCorp Has Learned About Infrastructure-as-Code](https://thenewstack.io/terraform-1-0-reflects-what-hashicorp-has-learned-about-infrastructure-as-code/)
- [learn.hashicorp.com: y Serverless Applications with AWS Lambda and API Gateway 🌟](https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway)
- [harness.io: Terraform 201: What It Is, Tutorial, and More 🌟](https://harness.io/blog/devops/terraform-201-tutorial)
- [learn.hashicorp.com: Configure Default Tags for AWS Resources 🌟](https://learn.hashicorp.com/tutorials/terraform/aws-default-tags)
- [terraform-hcloud-dualstack-k8s: Hetzner Dual-Stack Kubernetes Cluster](https://github.com/tibordp/terraform-hcloud-dualstack-k8s) (Unofficial) Terraform module for a dual-stack Kubernetes cluster on Hetzner Cloud
- [opensource.com: My top 5 tips for setting up Terraform 🌟](https://opensource.com/article/21/8/terraform-tips) These are the lessons I've learned after five years with Terraform.
- [rpadovani.com: How to make Terraform waiting for cloud-init to finish on EC2 without SSH](https://rpadovani.com/terraform-cloudinit) Terraform is a powerful tool. However, it has some limitations: since it uses AWS APIs, it doesn’t have a native way to check if an EC2 instance has completed to run cloud-init before marking it as ready. A possible workaround is asking Terraform to SSH on the instance, and wait until it is able to perform a connection before marking the instance as ready.
- [terraform-best-practices.com 🌟](https://www.terraform-best-practices.com/)
- [hub.qovery.com: Terraform is Not the Golden Hammer](https://hub.qovery.com/guides/engineering/terraform-not-the-golden-hammer/)
- [scalefactory.com: Failing faster with terraform](https://scalefactory.com/blog/2021/10/13/failing-faster-with-terraform/) **Terraform validation rules**. Terraform is an extremely powerful tool, but with great power comes great opportunity to break stuff, or whatever Uncle Ben said. With a single command a developer can deploy hundreds of resources in an instant, and when that developer inevitably configured the inputs wrong Terraform makes it easy to patch or rollback that mistake. But you know what’s better than recovering from mistakes? Never making the mistake in the first place.
- [shipa.io: Terraform meets AppOps 🌟](https://shipa.io/development/terraform-meets-appops) Terraform is the popular choice among teams
- [bitslovers.com: Terraform Output – What you should know](https://www.bitslovers.com/terraform-output/)
- [terraform.io: Refactoring](https://www.terraform.io/docs/language/modules/develop/refactoring.html)
- [serhii.vasylenko.info: Some Techniques to Enhance Your Terraform Proficiency](https://serhii.vasylenko.info/2022/01/16/some-techniques-to-enhance-your-terraform-proficiency/) Learn what cool things Terraform can do with its built-in functionality
- [thenewstack.io: Better Together: Hyper-Converged Kubernetes with Terraform](https://thenewstack.io/better-together-hyper-converged-kubernetes-with-terraform/)
- [==AdminTurnedDevOps/Terraform-The-Hard-Way==](https://github.com/AdminTurnedDevOps/Terraform-The-Hard-Way) The most efficient way to learn Terraform for beginners and intermediate practitioners
- [acloudguru.com: 5 things we love about Terraform](https://acloudguru.com/blog/engineering/5-things-we-love-about-terraform)
- [==middlewareinventory.com: Terraform import All AWS Security Groups – How to==](https://www.middlewareinventory.com/blog/terraform-import-securitygroup-aws/) In this post, we are going to see how to manage existing and already created AWS Security groups with Terraform. The new era of Infrastructure revolution has begun already and we already started provisioning, managing, administrating our Infra as a code with help of Configuration management tools like Ansible, Terraform, SaltStack etc.
- [==middlewareinventory.com: Terraform For Each Examples – How to use for_each | Devops Junction==](https://www.middlewareinventory.com/blog/terraform-for-each-examples)
- [terrateam.io: Terraform Pre-Commit Hooks](https://www.terrateam.io/blog/posts/terraform-pre-commit-hooks/) Terraform Code Improvements. There are many tools that can make sure your Terraform repo remains well-formated and tested. Using Git pre-commit hooks, one can easily incorporate these tools into everyday Terraform workflow.
- [dev.to/kubestack: A Better Way to Provision Kubernetes Resources Using Terraform 🌟](https://dev.to/kubestack/a-better-way-to-provision-kubernetes-resources-using-terraform-355n) In this tutorial, you will learn how to create Kubernetes resources using Terraform via the Helm and Kustomize providers. The resource will be created/destroyed as part of the usual terraform apply command.
- [youtube: Terrraform + Ansible: Automating configuration in infrastructure](https://www.youtube.com/watch?v=DeNflzdjxVM)
- [==terraform.io: Provisioners==](https://www.terraform.io/language/resources/provisioners/syntax) **Provisioners can be used to model specific actions on the local machine or on a remote machine in order to prepare servers or other infrastructure objects for service.**
- [infoq.com: Terraform 1.3 Release Introduces Simplified Refactoring Experience 🌟](https://www.infoq.com/news/2022/09/terraform-simplified-refactoring/) This release introduces optional object type attributes with defaults and expands the capabilities of moved blocks.
- [buildkite.com: Manage your CI/CD resources as Code with Terraform](https://buildkite.com/blog/manage-your-ci-cd-resources-as-code-with-terraform)
- [==blog.gruntwork.io: Terraform tips & tricks: loops, if-statements, and gotchas==](https://blog.gruntwork.io/terraform-tips-tricks-loops-if-statements-and-gotchas-f739bbae55f9)
- [dev.to: Using Terraform To Manage Infrastructure Resources | Pavan Belagatti](https://dev.to/pavanbelagatti/using-terraform-to-manage-infrastructure-resources-32da)
- [spectrocloud.com: Deploying complex infrastructure with a Terraform state machine](https://www.spectrocloud.com/blog/deploying-complex-infrastructure-with-a-terraform-state-machine/)
- [==tekanaid.com: Terraform for Beginners – A Beginner’s Guide to Automating Cloud Infrastructure== 🌟](https://tekanaid.com/posts/terraform-for-beginners-course-and-training)
- [==digitalocean.com: How To Structure a Terraform Project== 🌟](https://www.digitalocean.com/community/tutorials/how-to-structure-a-terraform-project) **Learn about structuring Terraform projects according to their general purpose and complexity. Then, you’ll create a project with a simple structure using the more common features of Terraform: variables, locals, data sources, and provisioners.**
- [==getbetterdevops.io: How To Deploy Helm Charts With Terraform== 🌟](https://getbetterdevops.io/terraform-with-helm/) Do you know you can deploy HelmCharts as any other Terraform resources? It's possible with the official Helm provider.
- [github.com/DhruvinSoni30/Terraform_multiple_modules](https://github.com/DhruvinSoni30/Terraform_multiple_modules) **How to work with multiple terraform modules?**
- [spacelift.io: Terraform Files – How to Structure a Terraform Project](https://spacelift.io/blog/terraform-files)
- [==youtube - freecodecamp.org: Learn Terraform with Azure by Building a Dev Environment – Full Course for Beginners==](https://youtu.be/V53AHWun17s?si=zB9HD1MCp3SbLQwL)
- [==youtube - freecodecamp.org: Learn Terraform (and AWS) by Building a Dev Environment – Full Course for Beginners==](https://www.youtube.com/watch?v=iRaai1IBlB0&t=3s)
- [devdosvid.blog: Hello Terraform Data; Goodbye Null Resource](https://devdosvid.blog/2023/04/16/hello-terraform-data-goodbye-null-resource/) Native built-in replacement for null_resource with Terraform 1.4
- [==build5nines.com: Why HashiCorp Terraform is Essential for SREs and DevOps Engineers==](https://build5nines.com/why-hashicorp-terraform-is-essential-for-sres-and-devops-engineers/)
- [infoq.com: CDK for Terraform Improves HCL Conversion and Terraform Cloud Interactions](https://www.infoq.com/news/2023/04/cdk-terraform-convert/)
- [==dev.to/pwd9000: Terraform Pro Tips Series' Articles== 🌟🌟](https://dev.to/pwd9000/series/16567)
    - [dev.to/pwd9000: Connect Terraform to Azure DevOps Git Repos over SSH](https://dev.to/pwd9000/connect-terraform-to-azure-devops-git-repos-over-ssh-163c)
    - [dev.to/pwd9000: Terraform - Complex Variable Types](https://dev.to/pwd9000/terraform-complex-variable-types-173e)
    - [dev.to/pwd9000: Terraform - Understanding the Lifecycle Block](https://dev.to/pwd9000/terraform-understanding-the-lifecycle-block-4f6e)
    - etc
- [blog.ogenki.io: Applying GitOps Principles to Infrastructure: An overview of tf-controller](https://blog.ogenki.io/post/terraform-controller/)
    - Terraform can be considered a "semi-declarative" tool as there is no built-in automatic reconciliation feature. There are several solutions to address this issue, but generally speaking, a modification will be applied using terraform apply. The code is actually written using the HCL configuration files (declarative), but the execution is done imperatively. As a result, there can be a drift between the declared and actual state (for example, a colleague who would have changed something directly into the console 😉).
    - ❓❓ So, how can I ensure that what is committed using Git is really applied. How to be notified if there is a change compared to the desired state and how to automatically apply what is in my code (GitOps)?
    - This is the promise of tf-controller, an Open Source Kubernetes operator from Weaveworks, tightly related to Flux (a GitOps engine from the same company). Flux is one of the solutions I really appreciate, that's why I invite you to have a look on my previous article
- [gravitydevops.com: Terraform: A Step-by-Step Guide from Basics to Advanced Techniques](https://gravitydevops.com/terraform-tutorials-basic-to-advanced/)
- [blog.gruntwork.io: How to use Terraform as a team](https://blog.gruntwork.io/how-to-use-terraform-as-a-team-251bc1104973) Collaboration, coding guidelines, and workflow for Terraform projects
- [overmind.tech: Is Observability relevant for Terraform?](https://overmind.tech/blog/is-observability-relevant-for-terraform)
- [thenewstack.io: Automating Retry for Failed Terraform Launches](https://thenewstack.io/automating-retry-for-failed-terraform-launches) Quali Torque orchestrates YAML files — which can be thought of as blueprints — for application environments directly from the IaC modules defined in Git.
- [theburningmonk.com: Making Terraform and Serverless framework work together](https://theburningmonk.com/2019/03/making-terraform-and-serverless-framework-work-together/)
- [nedinthecloud.com: Replacing The Template Cloudinit Config Data Source](https://nedinthecloud.com/2022/01/18/replacing-the-template_cloudinit_config-data-source/)
- [==youtube: Stop using shared secrets! CI/CD authentication the proper way==](https://www.youtube.com/watch?v=sd2wuAVush4)
- [==youtube.com: Terraform Basics | Ned in the Cloud==](https://www.youtube.com/playlist?list=PLXb5972EMl4BfKVDMaJH6Pg9SI6q_HqMg)
- [youtube: How to Deploy an E-Commerce Website to AWS With Terraform || Terraform Hands-on Project | Tech with Helen](https://www.youtube.com/watch?v=iLgEK6A31HM)
- [build5nines.com: Terraform: Code Project Organization Strategies (based on team, workload, or monolithic)](https://build5nines.com/terraform-code-project-organization-strategies-based-on-team-workload-or-monolithic/)
- [dev.to/grrywlsn: Self-service infrastructure as code](https://dev.to/grrywlsn/self-service-infrastructure-as-code-23bl)
- [youtube: Transforma tu EMPRESA con Terraform: Catálogo de Servicios | Nito Moreno](https://www.youtube.com/watch?v=IORvnr4u8z8)
- [build5nines.com: Should .terraform.lock.hcl file be added to .gitignore or committed to Git repo?](https://build5nines.com/should-terraform-lock-hcl-file-be-added-to-gitignore-or-committed-to-git-repo/)
- [build5nines.com: Terraform: How to for_each through a list(objects)](https://build5nines.com/terraform-how-to-for_each-through-a-listobjects/)
- [build5nines.com: Terraform: Modules using Git Branch as Source](https://build5nines.com/terraform-modules-using-git-branch-as-source/)
- [build5nines.com: Terraform: Split main.tf into seperate files](https://build5nines.com/terraform-split-main-tf-into-seperate-files/)
- [==pod.chaoslever.com: HashiCorp Under IBM’s Wing==](https://pod.chaoslever.com/hashicorp-under-ibms-wing/)
- [build5nines.com: Analyzing IBM’s Acquisition of HashiCorp: A Game-Changer in Hybrid Cloud Management](https://build5nines.com/analyzing-ibms-acquisition-of-hashicorp-a-game-changer-in-hybrid-cloud-management/)
- [dev.to/bhanufyi: Effective Terraform Variable Management in GitHub Actions](https://dev.to/bhanufyi/effective-terraform-variable-management-in-github-actions-488l)
- [dev.to/env0: Terraform Destroy Command: A Guide to Controlled Infrastructure Removal](https://dev.to/env0/terraform-destroy-command-a-guide-to-controlled-infrastructure-removal-4af8)
- [build5nines.com: Terraform IP Functions for Managing IP Addresses, CIDR Blocks, and Subnets](https://build5nines.com/terraform-ip-functions-for-managing-ip-addresses-cidr-blocks-and-subnets/)
- [masterpoint.io: Three Terraform Use-cases You Need to Start Implementing](https://masterpoint.io/updates/terraform-use-cases/) Engineering orgs that use IaC tools like Terraform aren’t typically maximizing their leverage. This article highlights at least three uses of Terraform and IaC automation that don’t necessarily center around traditional application workload infrastructure.
- [build5nines.com: Terraform: Remove Resource from State File (.tfstate)](https://build5nines.com/terraform-remove-resource-from-state-file-tfstate/)
- [build5nines.com: Terraform: How are Data Sources used?](https://build5nines.com/terraform-how-are-data-sources-used/)
- [build5nines.com: Terraform: Conditional If Variable Does Not Exist (try function)](https://build5nines.com/terraform-conditional-if-variable-does-not-exist-try-function/)
- [build5nines.com: Terraform: Output URL to Azure Portal for Azure Resources](https://build5nines.com/output-link-to-azure-resources-from-terraform-project/)
- [build5nines.com: Terraform State Management Explained](https://build5nines.com/terraform-state-management-explained/)
- [build5nines.com: Working with YAML in Terraform using the `yamldecode` and `yamlencode` Functions](https://build5nines.com/working-with-yaml-in-terraform-using-the-yamldecode-and-yamlencode-functions/)
- [mattias.engineer: Terraform Variable Cross Validation](https://mattias.engineer/blog/2024/terraform-variable-cross-validation/)
- [nilebits.com: Understanding Terraform Drift Detection and Remediation 🌟](https://www.nilebits.com/blog/2024/07/terraform-drift-detection/)
- [spacelift.io/blog/terraform-backends](https://spacelift.io/blog/terraform-backends) Terraform Backends – Local and Remote Explained
- [dev.to/spacelift: Using Terraform YAML Functions](https://dev.to/spacelift/using-terraform-yaml-functions-3ade)
- [howdykloudy.in: Implementing Shift Left for Terraform: An Introductory Guide 🌟](https://www.howdykloudy.in/blog/implementing-shift-left-for-terraform-an-introductory-guide/)
- [==bejarano.io/terraform-plan-light: terraform plan -light== 🌟](https://www.bejarano.io/terraform-plan-light/) **Add a terraform plan -light flag such that only resources modified in code are targeted for planning.**

### Antipatterns

- [==acloudguru.com: How to troubleshoot 5 common Terraform errors==](https://acloudguru.com/blog/engineering/how-to-troubleshoot-5-common-terraform-errors)
- [==dronov.net: Terraform, the terrible==](https://www.dronov.net/2024/02/22/terraform-the-terrible-en.html)

### Terraform License

- [opencoreventures.com: HashiCorp switching to BSL shows a need for open charter companies](https://opencoreventures.com/blog/2023-08-23-hashicorp-switching-bsl-shows-need-for-open-charter-companies/)

## OpenTOFU vs Terraform

- [nedinthecloud.com: Comparing Open TOFU And Terraform](https://nedinthecloud.com/2024/01/22/comparing-opentofu-and-terraform/)

## Terraform fmt

- [thomasthornton.cloud: Ensuring Your Terraform is Correctly Formatted Using Terraform fmt and GitHub Actions](https://thomasthornton.cloud/2024/02/15/ensuring-your-terraform-is-correctly-formatted-using-terraform-fmt-and-github-actions/)

## terraform taint

- ["Have you used the taint command in Terraform yet?"](https://www.youtube.com/watch?v=v_T1fuYGjV0&ab_channel=NedintheCloud) "It marks a resource in the Terraform state data as tainted, meaning the next time you run terraform apply, that resource will be destroyed and recreated. The configuration for the resource will not change, but the resource will be replaced. HashiCorp is trying to move away from imperative commands and towards a declarative model for all operations that affect state. Terraform taint makes direct alterations to state data in an imperative fashion with no way to preview the changes. If you run a terraform taint command, you are altering the state data without making a change to the configuration. In a collaborative environment, this can cause problems."

## terraform stacks


## Terraform and GitHub Actions

- [learn.hashicorp.com: Automate Terraform with GitHub Actions](https://learn.hashicorp.com/tutorials/terraform/github-actions) Automate infrastructure deployments with CI/CD using Terraform and GitHub Actions
- [==acloudguru.com: How to use GitHub Actions to automate Terraform==](https://acloudguru.com/blog/engineering/how-to-use-github-actions-to-automate-terraform)
- [==youtube: AWS Backup Set Up Using Terraform cloud and GitHub Actions | Cloud Quick Labs==](https://www.youtube.com/watch?v=4niy0_ZpQ1w&ab_channel=CloudQuickLabs)
- [thomasthornton.cloud: Deploy Terraform using GitHub Actions to Azure](https://thomasthornton.cloud/2021/03/19/deploy-terraform-using-github-actions-into-azure/)
- [build5nines.com: Terraform: GitHub Actions Automated Deployment](https://build5nines.com/terraform-github-actions-automated-deployment/)
- [thomasthornton.cloud: Displaying Terraform Plans in GitHub PRs with GitHub Actions](https://thomasthornton.cloud/2024/01/11/displaying-terraform-plans-in-github-prs-with-github-actions/)
- [dev.to/spacelift: How to Manage Terraform with GitHub Actions](https://dev.to/spacelift/how-to-manage-terraform-with-github-actions-5b10)

## Terraform and GitLab Pipelines

- [about.gitlab.com: How to use a push-based approach for GitOps with Terraform and AWS ECS and EC2](https://about.gitlab.com/blog/2021/08/10/how-to-agentless-gitops-aws/)

## Terraform Testing

- [==mattias.engineer: A Comprehensive Guide to Testing in Terraform: Keep your tests, validations, checks, and policies in order== 🌟](https://mattias.engineer/posts/terraform-testing-and-validation/)

## Terraform docs

- [terraform-docs.io](https://terraform-docs.io/user-guide/introduction/) terraform-docs is a utility to generate documentation from Terraform modules in various output formats.

## Private Terraform Registries

- [github.com/PacoVK/tapir](https://github.com/PacoVK/tapir) A Private Terraform Registry

## Terraform and Grafana

- [youtube HashiCorp: Telemetry transformed: Terraforming Grafana for next-gen dashboards](https://www.youtube.com/watch?v=qGdGMnQ83SA)

## Terraform and Jenkins

- [dev.to: Provisioning AWS Infrastructure using Terraform and Jenkins CI/CD](https://dev.to/aws-builders/provisioning-aws-infrastructure-using-terraform-and-jenkins-cicd-pgj)
- [github.com/vijaykedar/jenkins-setup-using-terraform](https://github.com/vijaykedar/jenkins-setup-using-terraform) This Terraform configuration automates the setup of a Jenkins server on an AWS EC2 instance. It provisions the necessary infrastructure and installs Jenkins along with its dependencies.
- [github.com/reneaudain/jenkins_tf_repo: Jenkins Server and S3 Artifact Storage on AWS using Terraform](https://github.com/reneaudain/jenkins_tf_repo)

## Alternatives to Terraform


## Managing secrets in your Terraform code

- [==blog.gruntwork.io: A comprehensive guide to managing secrets in your Terraform code== 🌟🌟🌟](https://blog.gruntwork.io/a-comprehensive-guide-to-managing-secrets-in-your-terraform-code-1d586955ace1)

## Terraform Cloud (HCP Terraform)

- [learn.hashicorp.com: Manage Private Environments with Terraform Cloud Agents](https://learn.hashicorp.com/tutorials/terraform/cloud-agents)
- [youtube: GitOps for infrastructure using GitHub and Terraform Cloud 🌟](https://www.youtube.com/watch?v=W_PmtDm4IXk&ab_channel=RobertdeBock)
- [scalr.com: An alternative to Terraform Cloud and Terraform Enterprise](https://scalr.com/) Scalr is a remote state & operations backend for Terraform with full CLI support, integration with OPA, a hierarchical configuration model, and quality of life features.
- [devclass.com: Terraform 1.1 moves forward with refactoring helpers and native Terraform Cloud integration](https://devclass.com/2021/12/09/terraform_-_1/)
- [==blog.gruntwork.io: How to manage multiple environments with Terraform== 🌟](https://blog.gruntwork.io/how-to-manage-multiple-environments-with-terraform-32c7bc5d692) **A comparison of using workspaces, branches, and Terragrunt**
- [spacelift.io: Terraform Cloud – Overview, Key Features & Tutorial](https://spacelift.io/blog/what-is-terraform-cloud)

## Hashicorp Infrastructure Cloud

- [build5nines.com: What is The HashiCorp Infrastructure Cloud?](https://build5nines.com/what-is-the-hashicorp-infrastructure-cloud/)

### Alternatives to Terraform Cloud

- [digger.dev](https://digger.dev) Open-source Terraform Cloud alternative. Run Terraform plan / apply jobs in your CI
- [spacelift.io](https://spacelift.io) Spacelift is a sophisticated CI/CD platform for OpenTofu, Terraform, Terragrunt, CloudFormation, Pulumi, Kubernetes, and Ansible

## HCL

- [github.com/hashicorp/hcl: HCL](https://github.com/hashicorp/hcl) HCL is the HashiCorp configuration language.
- [octopus.com: Introduction to HCL and HCL tooling](https://octopus.com/blog/introduction-to-hcl-and-hcl-tooling)

## CDK Cloud Development Kit Terraform

- [terraform-cdk 🌟](https://github.com/hashicorp/terraform-cdk) CDK (Cloud Development Kit) for Terraform allows developers to use familiar programming languages to define cloud infrastructure and provision it through HashiCorp Terraform.
- [infoq.com: cdk-terraform - Cloud Development Kit Can Now Generate Terraform Configurations Using TypeScript and Python](https://www.infoq.com/news/2020/07/cdk-terraform/)

## Providing Terraform with Ansible

- [==ansible.com: Providing Terraform with that Ansible Magic== 🌟🌟](https://www.ansible.com/blog/providing-terraform-with-that-ansible-magic)

## Python Boto3 and Terraform



## Helm Charts in Terraform

- [opensource.com: How I use Terraform and Helm to deploy the Kubernetes Dashboard 🌟](https://opensource.com/article/21/8/terraform-deploy-helm) Terraform can deploy Helm Charts. Is it right for you?

## Terraform Infracost

- [Infracost 🌟](https://github.com/infracost/infracost) If you use Terraform to provision your Kubernetes clusters, you might find infracost interesting. Infracost estimates hourly and monthly costs for a Terraform project. It helps you to see the cost breakdown and compare different deployment options upfront.
- [pratapreddypilaka.blogspot.com: Azure FinOps using Terraform and Infracost - Finding the hourly or monthly cost before Azure DevOps Deployments](https://pratapreddypilaka.blogspot.com/2023/11/azure-finops-using-terraform-and.html)
- [linkedin.com/pulse: How to Estimate Cloud Costs with Terraform (Azure, AWS, GCP, etc.) via Azure DevOps Pipelines](https://www.linkedin.com/pulse/how-estimate-cloud-costs-terraform-azure-aws-gcp-etc-via-kaan-turgut-msexc/)

## Awesome Terraform

- [github.com/shuaibiyy/awesome-terraform](https://github.com/shuaibiyy/awesome-terraform)
- [github.com/Azure/awesome-terraform](https://github.com/Azure/awesome-terraform)

## Terraform Cheat Sheets

- [Terraform Cheat Sheets](cheatsheets.md)

## Best Practices

- [github.com/ozbillwang/terraform-best-practices](https://github.com/ozbillwang/terraform-best-practices)
- [globaldatanet.com: Terraform CI/CD Best Practices](https://globaldatanet.com/blog/terraform-cicd-best-practices)
- [developer.hashicorp.com: Part 3: How to Evolve Your Provisioning Practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices/part3) This section describes the steps necessary to move an organization from manual provisioning processes to a collaborative infrastructure as code workflow. For each stage of operational maturity, we give instructions for moving your organization to the next stage, eventually arriving at our recommended workflow.
- [thenewstack.io: Terraform’s Best Practices and Pitfalls](https://thenewstack.io/terraforms-best-practices-and-pitfalls/) If you want to scale your infrastructure, you need to use Terraform in a way that will allow you to do that.
- [spacelift.io: 20 Terraform Best Practices to Improve your TF workflow 🌟](https://spacelift.io/blog/terraform-best-practices)
- [blog.coderco.io: Terraform Best Practices Series - Lessons from the Battlefield: Part 1](https://blog.coderco.io/p/terraform-best-practices-series-lessons)
    - [blog.coderco.io: Terraform Best Practices Series - Lessons from the Battlefield: Part 2](https://blog.coderco.io/p/terraform-best-practices-series-lessons-0cd)
    - They should be as simple as possible.
    - Root modules should manage very few resources and not depend heavily on many other modules or remote states.
    - Don't ever design with the intention of overriding tf variables with environment variables, using -target, etc. Hard code as many values as you can into tfvars files.
    - Use the lock files and pin versions everywhere. Module versions, Git tag versions, provider versions, Terraform versions.
    - Use asdf to install and run the pinned version of Terraform for each root module deployed.
    - Try to keep modules cohesive and loosely coupled. If updating one module or tfvars file creates plan changes in 20 different root modules, that's not great. Sometimes unavoidable, but creates a large operational burden.
    - Reuse public modules. There's a shit ton of weird subtle magic knowledge you need to use a resource that isn't documented and you won't find out until something breaks.
    - Test creating, changing, and then destroying, every resource. You will probably find a few need hacks to work as you expect.
    - Use semver and version/release all your modules and repos. Keep Changelogs of changes.
    - Keep a file in the root dir of repos that documents the owner or SME of the module and how to contact them.
    - For commonly referenced variables, store them in JSON, export them with `output`s, publish the module in its own repo somewhere, version it. Modules can reference that module to get the values, pin to versions of it so unexpected changes don't blow things up.
    - Use the CloudPosse Terraform modules / architecture / framework. Take the time to figure out how they work, use them. I swear you will end up reinventing it over time if you don't start now. In particular, you should apply a standard AWS tagging scheme with all your resources, which the CloudPosse modules support inherently. They also let you enable/disable functionality by variables, which is nice, cuz otherwise you have to comment out code.
    - Run your Terraform from CI/CD. Really you will be doing it from both your desktop and CI/CD, but assume you'll be running in CI/CD. Once you have 3 people working on the same TF code at once, you'll need the CI/CD to not bump into each other all the time. The rule of thumb is, if it's brand new code, you can run it locally, but if it's already in production and other things depend on it, run it from ci/cd. `apply`s anyway.
    - Separate modules by separation of concern; networking in network modules, clusters in cluster modules, apps in app modules, iam in security modules, etc. Also try to separate modules by AWS architectural paradigms, like "global" resources in their own modules. You'll want different teams to maintain and run their own modules independently, even though it all applies to the same AWS account/product stack.
    - Don't force authentication options into the provider configs. Allow whatever's running terraform to authenticate first, and the module will just detect the auth method automatically through the provider's sdk.
    - Don't make a module for a module's sake. Whereas with regular app code you might make a bunch of abstractions to try to make the code more manageable, that just makes Terraform suck more. Use the least number of abstractions possible to achieve what you want.
- [thomasthornton.cloud: Using Terraform tfvars for environment-agnostic deployments 🌟](https://thomasthornton.cloud/2024/04/25/using-terraform-tfvars-for-environment-agnostic-deployments/)

## Terraform and CI/CD. Terraform Workspaces

- [build5nines.com: Best Practices to Promote from DEV to PROD Environments with HashiCorp Terraform using Workspaces and Folders 🌟](https://build5nines.com/best-practices-to-promote-from-dev-to-prod-environments-with-hashicorp-terraform-using-workspaces-and-folders/)

## Terraform Boilerplates

- https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples
- https://github.com/hashicorp/terraform-provider-aws/tree/main/examples
- https://github.com/hashicorp/terraform-provider-awscc/tree/main/examples/resources
- [github.com/cloudposse?q=terraform-](https://github.com/cloudposse?q=terraform-)
- [devopshubproject/azure-terraform-ansible](https://github.com/devopshubproject/azure-terraform-ansible) This repo contains script which will help you to provision full functioning ansible lab environment on azure using terraform
- etc

## Terraform and Kubernetes

- [hodovi.cc: Creating a Low Cost Managed Kubernetes Cluster for Personal Development using Terraform](https://hodovi.cc/blog/creating-low-cost-managed-kubernetes-cluster-personal-development-terraform/)
- [kubernetes.io blog: Working with Terraform and Kubernetes](https://kubernetes.io/blog/2020/06/working-with-terraform-and-kubernetes/)
- [phillipsj.net: Dynamically Loaded Terraform Providers 🌟](https://www.phillipsj.net/posts/dynamically-loaded-terraform-providers/) Have you ever been faced with some situations where you need information from your Terraform execution to configure a provider ? Like spinning up a kubernetes cluster and dynamically deploying to it with Terraform? Check this short article for more !
- [learnk8s.io/kubernetes-terraform: Creating Kubernetes clusters with Terraform](https://learnk8s.io/kubernetes-terraform)
- [thenewstack.io: A Better Way to Provision Kubernetes Using Terraform](https://thenewstack.io/a-better-way-to-provision-kubernetes-using-terraform/)
- [==learn.hashicorp.com: Deploy Federated Multi-Cloud Kubernetes Clusters==](https://learn.hashicorp.com/tutorials/terraform/multicloud-kubernetes) In this tutorial, you will provision Kubernetes clusters in both Azure and AWS environments using their respective providers, configure Consul federation with mesh gateways across the two clusters using the Helm provider, and deploy microservices across the two clusters to verify federation, all using the same Terraform workflow.
- [architect.io: Get started with the Terraform Kubernetes provider](https://www.architect.io/blog/2021-02-17/terraform-kubernetes-tutorial/) In this tutorial, you'll learn how to define Kubernetes resources using HCL and apply the configuration to the cluster using Terraform
- [releasehub.com: Terraform Kubernetes Deployment: A Detailed Walkthrough](https://releasehub.com/blog/terraform-kubernetes-deployment-a-detailed-walkthrough) It is possible to combine both. Terraform can be used to deploy Kubernetes clusters. It's quite common, and it lets you deploy K8s just like the rest of your infrastructure.
    - Setting Up a Kubernetes Cluster with Terraform
    - Deploying Kubernetes Resources with Terraform
    - Managing Kubernetes Configurations
    - Terraform providers
    - Best Practices

## Terrafor Cloud Operator

- [hashicorp/terraform-k8s: Terraform Cloud Operator for Kubernetes](https://github.com/hashicorp/terraform-k8s) The Terraform Cloud Operator for Kubernetes provides first-class integration between Kubernetes and Terraform Cloud by extending the Kubernetes control plane to enable lifecycle management of cloud and on-prem infrastructure.

{==

## Terraform Kubernetes Boilerplates


### Hashicorp Terraform Kubernetes Collection

- https://github.com/hashicorp/learn-terraform-provision-aks-cluster
- https://github.com/hashicorp/learn-terraform-provision-eks-cluster
    - [spacelift.io: How to Provision an AWS EKS Kubernetes Cluster with Terraform](https://spacelift.io/blog/how-to-provision-aws-eks-kubernetes-cluster-with-terraform)
- https://github.com/hashicorp/learn-terraform-provision-gke-cluster
- https://github.com/hashicorp/learn-terraform-deploy-nginx-kubernetes-provider
- https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/kubernetes 🌟
- https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/kubernetes/nodes-on-internal-network 🌟

### Learnk8s Terraform and Managed Kubernetes

- [learnk8s.io/terraform-gke: Provisioning Kubernetes clusters on AWS with Terraform and GKE 🌟](https://learnk8s.io/terraform-gke) Fully automated dev, staging, prod clusters with GKE and the GKE Ingress in a single click.
- [learnk8s.io/terraform-eks: Provisioning Kubernetes clusters on AWS with Terraform and EKS 🌟](https://learnk8s.io/terraform-eks) Fully automated dev, test, prod environments with EKS, Terraform and the ALB Ingress Controller.
- [learnk8s.io/terraform-aks: Provisioning Kubernetes clusters on AWS with Terraform and AKS 🌟](https://learnk8s.io/terraform-aks) Fully automated dev and prod clusters complete with an Ingress controller in a single command.
- [learnk8s.io/terraform-lke: Provisioning Kubernetes clusters on Linode with Terraform 🌟](https://learnk8s.io/terraform-lke)

==}

### OpenShift and Terraform

- [==techcommunity.microsoft.com: Can I create an Azure Red Hat OpenShift cluster in Terraform? Yes, you can!==](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/can-i-create-an-azure-red-hat-openshift-cluster-in-terraform-yes/ba-p/3670889)

### Other Boilerplates

- [gist.github.com/chadmcrowell: AKS w/Virtual Nodes (ACI)](https://gist.github.com/chadmcrowell/4d11b8a56aba3bdc32ea73c31104357b)
- [garutilorenzo/k3s-aws-terraform-cluster](https://github.com/garutilorenzo/k3s-aws-terraform-cluster) Deploy an high available K3s cluster on Amazon AWS
- [poseidon/typhoon](https://github.com/poseidon/typhoon) **Typhoon is a minimal and free Kubernetes distribution with Terraform.**

### Terraform Kubernetes Operator


{==

### Terraform K3s Boilerplates

- [Global K3s Deployment on Packet Baremetal 🌟](https://github.com/c0dyhi11/k3s-linkerd) This repository contains Terraform scripts to deploy K3s and LinkerD on Packet baremetal servers spanning the globe.

### Terraform and GCP

- [==cloud.google.com: Terraform blueprints and modules for Google Cloud== 🌟](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
- [linkedin.com/pulse: GCP-Advanced-Terraform-Interactive-Learning-Challenge](https://www.linkedin.com/pulse/gcp-advanced-terraform-interactive-learning-challeng-kaan-turgut-guipc/)

#### Terraform GKE Boilerplates

    - The creation of 3 environments (dev, test, prod) automated
    - A cluster that can handle live traffic with the GKE Ingress controller.
    - GKE Ingress enabled with container-native load balancing.
    - All source code and knowledge to build your own infra.
- [circleci.com: Infrastructure as Code, part 1: create a Kubernetes cluster with Terraform](https://circleci.com/blog/learn-iac-part1/)
    - [circleci.com: Infrastructure as Code, part 2: build Docker images and deploy to Kubernetes with Terraform](https://circleci.com/blog/learn-iac-part02/)
    - [circleci.com: Infrastructure as Code, part 3: automate Kubernetes deployments with CI/CD and Terraform](https://circleci.com/blog/learn-iac-part3/)
- [hackernoon.com: Exporting Your GKE Cluster to Terraform Cloud: A Guide with Challenges and Solutions](https://hackernoon.com/exporting-your-gke-cluster-to-terraform-cloud-a-guide-with-challenges-and-solutions)
- [github.com/roib20: Terraform - Provision a GKE Cluster with Cloudflare Ingress and ArgoCD](https://github.com/roib20/terraform-provision-gke-cloudflare) This repo contains three Terraform modules to provision a GKE cluster, and then deploy Helm charts and Kubernetes manifests. The included deployments are designed for a fully-functioning Ingress controller that works with Cloudflare.

==}

### Terraform and AWS

- [==github.com/terraform-aws-modules/terraform-aws-solutions==](https://github.com/terraform-aws-modules/terraform-aws-solutions) **Set of standalone and reusable AWS/DevOps solutions implemented as Terraform modules**
- [thenewstack.io: Terraform on AWS: Multi-Account Setup and Other Advanced Tips](https://thenewstack.io/terraform-on-aws-multi-account-setup-and-other-advanced-tips/)
- [infoq.com: HashiCorp Terraform AWS Provider Introduces Significant Changes to Amazon S3 Bucket Resource](https://www.infoq.com/news/2022/02/terraform-aws-provider-s3/)
- [dev.to/arpanadhikari: Reusable AWS iam role for service-accounts (IRSA for k8s ) terraform module](https://dev.to/arpanadhikari/reusable-aws-iam-role-for-service-accounts-irsa-for-k8s-terraform-module-2og2) AWS supports authenticating your pods using an identity provider that your account is configured to trust. This tutorial will guide you through the process of creating an IAM role that your kubernetes pods will be able to assume.
- [aws.amazon.com: Save time with automated security checks of your Terraform scripts](https://aws.amazon.com/blogs/infrastructure-and-automation/save-time-with-automated-security-checks-of-terraform-scripts/) Looking for a way to automate security checks of your Terraform scripts directly into your continuous integration and continuous delivery (CI/CD) pipeline? How about a way to view the results of those security checks and address issues before deployment, all with built-in notifications? Then check out our solution using Checkov, a static code analysis tool for flagging security and compliance problems.
- [dev.to: How to deploy a serverless website with Terraform](https://dev.to/aws-builders/how-to-deploy-a-serverless-website-with-terraform-5677)
- [==github.com/aws-samples: AWS Service Catalog Engine for Terraform==](https://github.com/aws-samples/service-catalog-engine-for-terraform-os) The AWS Service Catalog Terraform Reference Engine (TRE) provides an example for you to configure and install a Terraform engine in your AWS Service Catalog administrator account. With the engine installed into your account, you can use Service Catalog as a single tool to organize, govern, and distribute your Terraform configurations within AWS.
- [dev.to: Terraforming AWS RDS : Scaling Postgres](https://dev.to/yet_anotherdev/aws-rds-scaling-postgres-30ic)
- [numericaideas.com: Auto Scaling Group on AWS with Terraform](https://numericaideas.com/blog/auto-scaling-group-on-aws-with-terraform/)
- [devopscube.com: AWS Terraform Autoscaling Group With ALB Deployment Tutorial](https://devopscube.com/terraform-autoscaling-group/)
- [dev.to/monarene: Dynamic Volume Provisioning in Kubernetes with AWS and Terraform](https://dev.to/monarene/dynamic-volume-provisioning-in-kubernetes-with-aws-and-terraform-3m6h) In this article, you'll learn about Persistent Volumes and how they are provisioned, managed, and configured in AWS. You'll compare Static and Dynamic volume provisioning, how they overlap, and which provisioning mechanism you should employ
- [blog.awsfundamentals.com: Mastering AWS Lambda with Terraform: A Comprehensive Guide](https://blog.awsfundamentals.com/aws-lambda-with-terraform)
- [github.com/squareops/terraform-aws-vpc](https://github.com/squareops/terraform-aws-vpc) Terraform Module to create an AWS VPC network with VPN and configure Peering b/w multiple VPCs
- [dev.to/aws-builders: Deploying a Containerized App to ECS Fargate Using a Private ECR Repo & Terragrunt](https://dev.to/aws-builders/deploying-a-containerized-app-to-ecs-fargate-using-a-private-ecr-repo-terragrunt-5b8a)
- [youtube: Three tier architecture using Terraform in AWs](https://www.youtube.com/watch?v=3uDxwNOtilU)
- [github.com/tokarev-artem/auto-ec2-setup](https://github.com/tokarev-artem/auto-ec2-setup) This project was created for automatic and 5 minutes setup ec2 instances for hosting php applications
- [dev.to/chinmay13: AWS Networking with Terraform: VPC Transit Gateway between VPCs](https://dev.to/chinmay13/aws-networking-with-terraform-vpc-transit-gateway-between-vpcs-1ne4)
- [dev.to/aws-builders: My Service Mesh journey with Terraform on AWS Cloud - Part 1](https://dev.to/aws-builders/my-service-mesh-journey-with-terraform-on-aws-cloud-part-1-3hee)
- [dev.to/aws-builders: My Service Mesh journey with Terraform on AWS Cloud - Part 2](https://dev.to/aws-builders/my-service-mesh-journey-with-terraform-on-aws-cloud-part-2-58fd)
- [github.com/infrahouse/terraform-aws-ecs](https://github.com/infrahouse/terraform-aws-ecs) Module that runs service in ECS
- [dev.to/bennyfmo_237: Deploying Basic Infrastructure on AWS with Terraform](https://dev.to/bennyfmo_237/deploying-basic-infrastructure-on-aws-with-terraform-1k68)

{==

#### AWS Service Catalog

- [==New – Self-Service Provisioning of Terraform Open-Source Configurations with AWS Service Catalog== 🌟🌟🌟](https://aws.amazon.com/blogs/aws/new-self-service-provisioning-of-terraform-open-source-configurations-with-aws-service-catalog/) With AWS Service Catalog, you can create, govern, and manage a catalog of infrastructure as code (IaC) templates that are approved for use on AWS. These IaC templates can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. You can control which IaC templates and versions are available, what is configured by each version, and who can access each template based on individual, group, department, or cost center. End users such as engineers, database administrators, and data scientists can then quickly discover and self-service provision approved AWS resources that they need to use to perform their daily job functions.

#### AWS Observability Accelerator for Terraform

- [github.com/aws-observability](https://github.com/aws-observability)
- [==aws-observability.github.io: AWS Observability Accelerator for Terraform== 🌟](https://aws-observability.github.io/terraform-aws-observability-accelerator/) The AWS Observability Accelerator for Terraform is a set of opinionated modules to help you set up observability for your AWS environments with AWS-managed observability services such as Amazon Managed Service for Prometheus, Amazon Managed Grafana, AWS Distro for OpenTelemetry (ADOT) and Amazon CloudWatch. We provide curated metrics, logs, traces collection, alerting rules and Grafana dashboards for your EKS infrastructure, Java/JMX, NGINX based workloads and your custom applications. [github.com/aws-observability/terraform-aws-observability-accelerator](https://github.com/aws-observability/terraform-aws-observability-accelerator)
- [aws-observability.github.io: Tracing on Amazon EKS](https://aws-observability.github.io/terraform-aws-observability-accelerator/eks/tracing/)

#### Terraform EKS Boilerplates

- [github.com/maddevsio/aws-eks-base: Boilerplate for a basic AWS infrastructure with EKS cluster 🌟](https://github.com/maddevsio/aws-eks-base) This boilerplate contains the know-how of the Mad Devs team for the rapid deployment of a Kubernetes cluster, supporting services, and the underlying infrastructure in the Amazon cloud.
- [github.com/aws-samples/aws-eks-accelerator-for-terraform: AWS EKS Accelerator for Terraform 🌟](https://github.com/aws-samples/aws-eks-accelerator-for-terraform) The AWS EKS Accelerator for Terraform is a framework designed to help deploy and operate secure multi-account, multi-region AWS environments. The power of the solution is the configuration file which enables the users to provide a unique terraform state for each cluster and manage multiple clusters from one repository.
- [dev.to: Creating an EKS Cluster and Node Group with Terraform](https://dev.to/aws-builders/creating-an-eks-cluster-and-node-group-with-terraform-1lf6)
    - [dev.to: Install & Manage Amazon EKS Add-ons with Terraform](https://dev.to/aws-builders/install-manage-amazon-eks-add-ons-with-terraform-2dea)
        - Amazon VPC CNI
        - CoreDNS
        - Amazon EBS CSI
- [garutilorenzo/k8s-aws-terraform-cluster](https://github.com/garutilorenzo/k8s-aws-terraform-cluster) Deploy an high available Kubernetes (k8s) cluster on Amazon AWS. The scope of this repo is to show all the AWS components needed to deploy a high available Kubernetes cluster. The final infrastructure includes:
    - 2 ASGs
    - 1 Internal LB
    - 1 External LB
    - 1 SG (VPC)
    - 1 SG (external traffic)
    - 1 IAM role
    - 1 S3
- [github.com/terraform-aws-modules/terraform-aws-eks: AWS EKS Terraform module](https://github.com/terraform-aws-modules/terraform-aws-eks) Terraform module which creates AWS EKS (Kubernetes) resources
    - ExternalDNS
    - AWS Load Balancer controller
- [platformwale.blog: Create Amazon EKS Cluster within its VPC using Terraform](https://platformwale.blog/2023/07/15/create-amazon-eks-cluster-within-its-vpc-using-terraform/)
- [dev.to/aws-builders: Navigating AWS EKS with Terraform: Understanding VPC Essentials for EKS Cluster Management](https://dev.to/aws-builders/navigating-aws-eks-with-terraform-understanding-vpc-essentials-for-eks-cluster-management-51e3)
- [dev.to/verifacrew: How to assume an AWS IAM role from a Service Account in EKS with Terraform](https://dev.to/verifacrew/how-to-assume-an-aws-iam-role-from-a-service-account-in-eks-with-terraform-28gd)

==}

#### AWSCC. Terraform AWS Cloud Control Provider

- [awscc](https://registry.terraform.io/providers/hashicorp/awscc/latest) Lifecycle management of AWS resources powered by the AWS Cloud Control API. This provider is fully generated from the available CloudFormation resource definitions and is maintained internally by the HashiCorp AWS Provider team.

#### AWS Control Tower Account Factory for Terraform (AFT)

- [==aws.amazon.com: New – AWS Control Tower Account Factory for Terraform==](https://aws.amazon.com/blogs/aws/new-aws-control-tower-account-factory-for-terraform/)
- [==aws.amazon.com: AWS Control Tower==](https://aws.amazon.com/controltower/) The easiest way to set up and govern a secure multi-account AWS environment
- [trek10.com: Control Tower: Then vs Now](https://www.trek10.com/blog/control-tower-then-vs-now) Control Tower today is not the same Control Tower that you may have been introduced to in the past.

#### Porsche Official

- [porscheofficial/terraform-aws-ecr-watch](https://github.com/porscheofficial/terraform-aws-ecr-watch) Terraform module that configures an Amazon ECR dashboard that shows container image ownership and usage metrics by account.

#### AWS Serverless with Terraform

- [==serverless.tf: Doing serverless with Terraform==](https://serverless.tf) serverless.tf is an opinionated open-source framework for developing, building, deploying, and securing serverless applications and infrastructures on AWS using Terraform.

### Terraform with Azure

- [registry.terraform.io: Terraform Azure Resources 🌟](https://registry.terraform.io/modules/azurerm/resources/azure/latest) This set of terraform modules will help you to create and manage a Azure Resources.
- [build5nines.com: Get Started with Terraform on Azure](https://build5nines.com/get-started-with-terraform-on-microsoft-azure/)
- [github.com/kuhlman-labs/terraform-azurerm-landing-zone](https://github.com/kuhlman-labs/terraform-azurerm-landing-zone) A curated collection of Terraform azurerm modules
- [cloudbuild.co.uk: Part 1: Terraform with Azure - How to install Terraform](https://cloudbuild.co.uk/how-to-install-terraform/)
    - [cloudbuild.co.uk: Part 2: Terraform with Azure - How to install Azure CLI](https://cloudbuild.co.uk/part-2-terraform-with-azure-how-to-install-azure-cli/)
    - [cloudbuild.co.uk: Part 3: Terraform with Azure - How to install Visual Studio Code](https://cloudbuild.co.uk/part-3-terraform-with-azure-how-to-install-visual-studio-code/)
    - [cloudbuild.co.uk: Part 4: Terraform with Azure - How to install Azure Terraform Plugin in Visual Studio Code](https://cloudbuild.co.uk/part-4-terraform-with-azure-how-to-install-azure-terraform-plugin-in-visual-code/)
    - [cloudbuild.co.uk: Part 5: Terraform with Azure - Install Git and initialise repository](https://cloudbuild.co.uk/part-5-terraform-with-azure-install-git-and-enable-in-visual-studio-code/)
    - [cloudbuild.co.uk: Part 6: Terraform with Azure - Deploy resources in Azure](https://cloudbuild.co.uk/part-6-terraform-with-azure-deploy-resources-in-azure/)
    - [cloudbuild.co.uk: Part 7: Terraform with Azure - Deploy a variables file in Terraform](https://cloudbuild.co.uk/part-7-terraform-with-azure-deploy-a-variables-file-in-terraform/)
    - [cloudbuild.co.uk: Part 8: Terraform with Azure - Deploy terraform.tfvars file](https://cloudbuild.co.uk/part-8-terraform-with-azure-deploy-a-terraform-tfvars-file/)
- [techcommunity.microsoft.com: Implement Azure landing zones with HashiCorp Terraform](https://techcommunity.microsoft.com/t5/azure-migration-and/implement-azure-landing-zones-with-hashicorp-terraform/ba-p/3241071)
- [azureviking.com: Terraform module: Azure DNS Private Resolver](https://www.azureviking.com/post/terraform-module-azure-dns-private-resolver) - [haflidif/terraform-azurerm-dns-private-resolver](https://github.com/haflidif/terraform-azurerm-dns-private-resolver)
- [==github.com/thomast1906/terraform-on-azure==](https://github.com/thomast1906/terraform-on-azure) A repo self-lead to give you an understanding on deploying Terraform on Azure
- [blog.cloudtrooper.net: DRY Terraform code for Private Link and DNS](https://blog.cloudtrooper.net/2023/08/19/dry-terraform-code-for-private-link-and-dns/)
- [azureway.cloud: Azure Container Apps – Creating using Terraform [part 1]](https://azureway.cloud/azure-container-apps-creating-using-terraform-part-1/)
    - [azureway.cloud: Azure Container Apps – traffic splitting [part 4]](https://azureway.cloud/azure-container-apps-traffic-splitting-part-4/)
- [build5nines.com: Terraform: Deploy Azure Function App with Consumption Plan](https://build5nines.com/terraform-deploy-azure-function-app-with-consumption-plan/)
- [techcommunity.microsoft.com: Simplifying Onboarding to Microsoft Defender for Cloud with Terraform](https://techcommunity.microsoft.com/t5/microsoft-defender-for-cloud/simplifying-onboarding-to-microsoft-defender-for-cloud-with/ba-p/3974789)
- [techcommunity.microsoft.com: Create an Azure OpenAI, LangChain, ChromaDB, and Chainlit chat app in AKS using Terraform](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/create-an-azure-openai-langchain-chromadb-and-chainlit-chat-app/ba-p/4024070)
- [build5nines.com: Terraform: Deploy Azure App Service with Key Vault Secret Integration](https://build5nines.com/terraform-deploy-azure-app-service-with-key-vault-secret-integration)
- [youtube: Using Azure Storage for Terraform State - Best Practices | Ned in the cloud](https://www.youtube.com/watch?v=iVyKvopGnrQ&t=737s)
- [==techcommunity.microsoft.com: Introducing Azure Verified Modules!== 🌟](https://techcommunity.microsoft.com/t5/azure-tools-blog/introducing-azure-verified-modules/ba-p/4045946)
    - [youtube: Introducing Azure Verified Modules for Terraform | Ned in the Cloud](https://www.youtube.com/watch?v=6OeRByC-sBs)
- [linkedin.com/pulse: Deploying Microsoft Sentinel via - ARM Template vs Terraform](https://www.linkedin.com/pulse/deploying-microsoft-sentinel-via-arm-template-vs-debac-manikandan-ychnc/)
- [==blog.xmi.fr: Terraform vs Bicep: the differences you should really know== 🌟](https://blog.xmi.fr/posts/terraform-vs-bicep/)
- [techcommunity.microsoft.com: Terraform on Azure February 2024 Update](https://techcommunity.microsoft.com/t5/azure-tools-blog/terraform-on-azure-february-2024-update/ba-p/4070567)
- [azureviking.com: Terraform Module: azurerm-alz-subnet](https://www.azureviking.com/post/terraform-module-azurerm-alz-subnet)
- [hlokensgard.no/knowledge-sharing: Miro Mind map over Azure Landing Zones element, Terraform modules, GitHub Code](https://hlokensgard.no/knowledge-sharing/)
- [learn.microsoft.com: Introduction to using Azure Verified Modules for Terraform](https://learn.microsoft.com/en-us/samples/azure-samples/avm-terraform-labs/avm-terraform-labs/) - [github.com/azure-samples/avm-terraform-labs](https://github.com/azure-samples/avm-terraform-labs/)
- [thomasthornton.cloud: Enabling PostgreSQL flexible server logs and configuring a retention period using Terraform](https://thomasthornton.cloud/2024/03/28/enabling-postgresql-flexible-server-logs-and-configuring-a-retention-period-using-terraform/)
- [build5nines.com: Terraform: Import Existing Azure Resources into State (.tfstate)](https://build5nines.com/terraform-import-existing-azure-resources-into-state-tfstate/)
- [build5nines.com: What is Azure Private Link and How to Deploy with Terraform](https://build5nines.com/what-is-azure-private-link-and-how-to-deploy-with-terraform/)
- [thomasthornton.cloud: Writing reusable Terraform modules (azure)](https://thomasthornton.cloud/2022/06/02/writing-reusable-terraform-modules/)

#### Azure Terraform Export aztfexport

- [github.com/Azure/aztfexport](https://github.com/Azure/aztfexport)
- [learn.microsoft.com: Overview of Azure Export for Terraform](https://learn.microsoft.com/en-us/azure/developer/terraform/azure-export-for-terraform/export-terraform-overview)
- [learn.microsoft.com: Using Azure Export for Terraform in advanced scenarios](https://learn.microsoft.com/en-us/azure/developer/terraform/azure-export-for-terraform/export-advanced-scenarios)
- [spacelift.io: Azure Terraform Export: Importing Resources with Aztfexport](https://spacelift.io/blog/azure-terraform-export)
- [scalr.com: Getting Started with the Azure Terraform Export Tool](https://www.scalr.com/blog/getting-started-with-the-azure-terraform-export-tool)

#### Azure Landing Zones with Terraform. Azure Network Architecture

- [==github.com/Azure/terraform-azurerm-caf-enterprise-scale==](https://github.com/Azure/terraform-azurerm-caf-enterprise-scale)
- [registry.terraform.io/modules/Azure/lz-vending](https://registry.terraform.io/modules/Azure/lz-vending) Terraform module to deploy landing zone subscriptions (and much more) in Azure
- [==techcommunity.microsoft.com: Azure Landing Zones Accelerators for Bicep and Terraform. Announcing General Availability!==](https://techcommunity.microsoft.com/t5/azure-tools-blog/azure-landing-zones-accelerators-for-bicep-and-terraform/ba-p/4029866)
- [blog.cloud63.fr: Landing Zone networking using Terraform](https://blog.cloud63.fr/landing-zone-networking-using-terraform/)
- [==github.com/kaysalawu/azure-network-terraform: Azure Network Architecture - Terraform Examples== 🌟](https://github.com/kaysalawu/azure-network-terraform) Collection of terraform codes for various Azure network topologies.
- [==build5nines.com: Deploying Hub-and-Spoke Network Topology in Microsoft Azure using Terraform==](https://build5nines.com/deploying-hub-and-spoke-network-topology-in-microsoft-azure-using-terraform/)
- [registry.terraform.io/modules/Azure/avm-ptn-alz: ALZ Terraform Module](https://registry.terraform.io/modules/Azure/avm-ptn-alz) Terraform module to deploy Azure Landing Zones

#### Azure Terrafy and AzAPI Terraform Provider

- [==Announcing Azure Terrafy and AzAPI Terraform Provider Previews==](https://techcommunity.microsoft.com/t5/azure-tools-blog/announcing-azure-terrafy-and-azapi-terraform-provider-previews/ba-p/3270937) On Azure, businesses may choose many flavors of IaC tooling to manage their Azure resources including HashiCorp Terraform, Bicep, ARM templates, Ansible and many more. We encourage you to choose the IaC tool that best suits your needs. Our mission is to ensure that no matter which tool you choose, you have the best experience and integration with Azure.
- [techcommunity.microsoft.com: Azure Terrafy – Import your existing Azure infrastructure into Terraform HCL](https://techcommunity.microsoft.com/t5/itops-talk-blog/azure-terrafy-import-your-existing-azure-infrastructure-into/ba-p/3357653)
- [techcommunity.microsoft.com: Announcing AzAPI Dynamic Properties](https://techcommunity.microsoft.com/t5/azure-tools-blog/announcing-azapi-dynamic-properties/ba-p/4121855)
- [build5nines.com: Using AzAPI Terraform Provider Dynamic Properties Feature instead of jsonencode](https://build5nines.com/using-azapi-terraform-provider-dynamic-properties-feature-instead-of-jsonencode/)

#### Terraform in Azure DevOps. Azure DevOps with terraform

- [==adamtheautomator.com: How to Build Infrastructure with Terraform in Azure DevOps== 🌟](https://adamtheautomator.com/terraform-azure-devops/)
- [==build5nines.com: Deploy Terraform using Azure DevOps YAML Pipelines==](https://build5nines.com/deploy-terraform-using-azure-devops-yaml-pipelines/)
- [==thomasthornton.cloud: Deploy Terraform using Azure DevOps==](https://thomasthornton.cloud/2020/07/08/deploy-terraform-using-azure-devops/)
- [registry.terraform.io/modules: azure-terraformer - azuredevops provider](https://registry.terraform.io/modules/markti/azure-terraformer/azuredevops) A collection of Terraform modules that provision to Azure DevOps
- [devblogs.microsoft.com/devops: Introduction to Azure DevOps Workload identity federation (OIDC) with Terraform](https://devblogs.microsoft.com/devops/introduction-to-azure-devops-workload-identity-federation-oidc-with-terraform/)
- [github.com/microsoft/terraform-provider-azuredevops/releases/tag/v1.0.0](https://github.com/microsoft/terraform-provider-azuredevops/releases/tag/v1.0.0)
- [thomasthornton.cloud: Error: spawn terraform ENOENT when running Terraform in Azure DevOps Pipeline](https://thomasthornton.cloud/2022/01/24/error-spawn-terraform-enoent-when-running-terraform-in-azure-devops-pipeline/)

#### Terraform Azure Stack Provider


### Terraform for a Data Engineer


{==

### Terraform AKS Boilerplates

- [github.com/Azure/terraform-azurerm-aks](https://github.com/Azure/terraform-azurerm-aks) Terraform Module for deploying an AKS cluster
- [github.com/stacksimplify/azure-aks-kubernetes-masterclass 🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass)
    - [==stacksimplify.com/azure-aks: Kubernetes On Cloud Roadmap==](https://stacksimplify.com/azure-aks/)
    - [**Boilerplate: 25-Azure-DevOps-Terraform-Azure-AKS** 🌟🌟🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass/tree/master/25-Azure-DevOps-Terraform-Azure-AKS)
    - [PDF presentation 🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass/tree/master/ppt-presentation)

	``` tf
	# 07-aks-cluster.tf

	# Network Profile
	# Kubenet is a kubernetes network configuration plugin for your AKS cluster. Nodes get an IP address from
	# the AKS subnet, and pods receive an IP address from a separate address space entirely. The source IP address
	# of the traffic is NAT'd to the node's IP address.

	# With kubenet there's NO Pod-to-Pod communication because they don't have their own public IPs.
	# User Defined Routing (UDR) and IP forwarding is used for communication between pods across nodes.

	# Kubenet is the preferred method since you get more pods per node and the AKS Cluster scales to a bigger number.
	# With kubenet Max Number of Pods per Node: 110
	# With Kubenet and CIDR =/24 : 251 nodes * 110 pods per node = 27.610 pods
    # With Azure CNI (instead of kubenet) and CIDR =/24 : 8 nodes * 30 pods per node = 240 pods

	# If we have limited IP addresses to work with, we can fit more pods in the limited IP address space because we can
	# fit more pods per node.

	# The Service CIDR, Pod CIDR, and Docker Bridge Access can be any address range.
	# The DNS Service IP must be any IP address that's within the Service CIDR address range.

	# Network settings (service_cidr, pod_cidr, docker_bridge_cidr, dns_service_ip) are commented. The below values
	# correspond to the applied default values when these settings are note set up.

	# Default network settings with kubenet when they are not configured:
    # Azure AKS VNet      = "10.0.0.0/8"
	# Azure AKS Subnet    = "10.240.0.0/16"
    # service_cidr        = "10.0.0.0/16"
	# pod_cidr            = "10.244.0.0/16"
	# docker_bridge_cidr  = "172.17.0.1/16" # Default. You can reuse this range across different AKS Clusters
	# dns_service_ip      = "10.0.0.10"

	network_profile {  # (1)
	load_balancer_sku = "Standard"
	network_plugin = "kubenet"  # use Azure CNI network plugin when windows node pools are required (not supported by kubenet)
	#service_cidr = "10.0.0.0/16"
	#dns_service_ip = "10.0.0.10"
	#docker_bridge_cidr = "172.17.0.1/16" # Default. You can reuse this range across different AKS clusters.
	}
	```

	1. :man_raising_hand: Network Profile

- [build5nines.com: Terraform: Create an AKS Cluster 🌟](https://build5nines.com/terraform-create-an-aks-cluster/)
- [thomasthornton.cloud: Building and deploying to an AKS cluster using Terraform and Azure DevOps with Kubernetes and Helm providers](https://thomasthornton.cloud/2022/11/09/building-and-deploying-to-an-aks-cluster-using-terraform-and-azure-devops-with-kubernetes-and-helm-providers/)
- In this 6-part tutorial series, you will explore how to set up a production-ready cluster on AKS:
    - Setting up ACR
    - Managing costs
    - Databases and migrations
    - Handling static files
- [thomasthornton.cloud: Deploying Azure AKS GitOps Flux extension with Terraform](https://thomasthornton.cloud/2023/12/03/deploying-azure-aks-gitops-flux-extension-with-terraform/)
- [github.com/amitmavgupta/azure-terraform](https://github.com/amitmavgupta/azure-terraform) Create AKS clusters with Cilium and Isovalent
- [==github.com/Azure-Samples/aks-platform-engineering Building a Platform Engineering Environment on Azure Kubernetes Service (AKS)== 🌟](https://github.com/Azure-Samples/aks-platform-engineering)
- [techcommunity.microsoft.com: How to deploy a production-ready AKS cluster with Terraform verified module](https://techcommunity.microsoft.com/t5/azure-for-isv-and-startups/how-to-deploy-a-production-ready-aks-cluster-with-terraform/ba-p/4122013)

### Terraform and OCI

- https://github.com/oracle-quickstart/oci-quickstart-template
- https://github.com/oracle-quickstart/oci-oke

==}

### Terraform and Linode


## Istio with Terraform


## Terraform and Minikube

- [dev.to: Deploy Kubernetes Resources in Minikube cluster using Terraform](https://dev.to/chefgs/deploy-kubernetes-resources-in-minikube-cluster-using-terraform-1p8o)

## Terraform and Apache Kafka


## Terraform and JMeter


## Terraform and OpenVPN on AWS

- [github.com/infrahouse/terraform-aws-openvpn](https://github.com/infrahouse/terraform-aws-openvpn) Terraform module that deploys OpenVPN server.

## Terraform Video Tutorials

- [youtube: Terraform Tutorial for beginners | AWS Infrastructure as Code | Github Actions 🌟](https://www.youtube.com/playlist?list=PLlvAxgO7JdIXAzHx887zl-4no4X-CtiFu)

## CDK for Terraform

    - https://www.terraform.io/cdktf
- [dev.to/aws-builders: Unleashing the Power of CDK and Terraform in Cloud Deployments](https://dev.to/aws-builders/unleashing-the-power-of-cdk-and-terraform-in-cloud-deployments-5680)

## Graph Visualization Software

- The [terraform graph command](https://www.terraform.io/docs/cli/commands/graph.html) is used to generate a visual representation of either a configuration or execution plan. The output is in the DOT format, which can be used by [GraphViz](https://graphviz.org) to generate charts.
- [graphviz.org](https://graphviz.org/)
- [edotor.net](https://edotor.net/)
- [dreampuf.github.io/GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/)
- [graphviz.online](https://graphviz.online/)

## Terraform Modules

- [offensive-terraform.github.io: Offensive Terraform Modules 🌟](https://offensive-terraform.github.io/offensive-terraform.github.io/) Automated multi step offensive attack modules with Infrastructure as Code(IAC)
- [digitalocean.com: How To Build a Custom Terraform Module](https://www.digitalocean.com/community/tutorials/how-to-build-a-custom-terraform-module)
- [dev.to: Terraform Modules for Advanced Users](https://dev.to/gofirefly/terraform-modules-for-advanced-users-4n56)

### Terraform AWS Modules

- [==github.com/terraform-aws-modules==](https://github.com/terraform-aws-modules) **Collection of Terraform AWS modules supported by the community**

### Segment AWS Stack Terraform Modules

- [The Segment AWS Stack](https://segment.com/blog/the-segment-aws-stack/)
- [segmentio/stack](https://github.com/segmentio/stack) A set of Terraform modules for configuring production infrastructure with AWS

## Terraform Providers

- [Junos-terraform: JUNOS Terraform Automation Framework (JTAF)](https://github.com/Juniper/Junos-terraform)
- [mitchellh/terraform-provider-multispace](https://github.com/mitchellh/terraform-provider-multispace) Terraform Provider for cascading runs across multiple workspaces.
- [kyma-incubator/terraform-provider-kind: Terraform Provider for kind (Kubernetes IN Docker)](https://github.com/kyma-incubator/terraform-provider-kind) The Terraform Provider for kind enables Terraform to provision local Kubernetes clusters on base of Kubernetes IN Docker (kind).
- [github.com/circa10a/terraform-provider-mailform](https://github.com/circa10a/terraform-provider-mailform) A terraform provider to send physical mail via https://mailform.io
- [env0.com: How to Use Terraform Providers](https://www.env0.com/blog/how-to-use-terraform-providers)
- [github.com/tlkamp/terraform-provider-validation: Validation Provider](https://github.com/tlkamp/terraform-provider-validation) Extended validation for Terraform in the form of a custom provider.

### Terraform AWS Cloud Control Provider


### Terraform Provider for Elastic Cloud

- https://github.com/elastic/terraform-provider-ec
- [infoq.com: Elastic Releases Terraform Providers for the Elastic Stack and Elastic Cloud](https://www.infoq.com/news/2022/01/elastic-terraform/)

### Terraform Vault Provider

- [learn.hashicorp.com: Codify Management of Vault Enterprise Using Terraform](https://learn.hashicorp.com/tutorials/vault/codify-mgmt-enterprise)

### Terraform AzureRM

- [registry.terraform.io: Data Source: azurerm_ip_groups (new)](https://registry.terraform.io/providers/hashicorp/Azurerm/latest/docs/data-sources/ip_groups)
- [registry.terraform.io/modules/hlokensgard/rbac-administrator](https://registry.terraform.io/modules/hlokensgard/rbac-administrator/azure/latest) A Terraform module that will help you create role assignment for the role Role Based Access Control Administrator.

## Terraform Code Quality. Terraform Quality Checks. Terraform Linters

- [==prcode.co.uk: Terraform Code Quality==](https://prcode.co.uk/2022/02/08/terraform-code-quality/)
- [github.com/terraform-linters/tflint](https://github.com/terraform-linters/tflint/releases/tag/v0.51.0)

## Enforce Policy with Sentinel

- [learn.hashicorp.com: Enforce Policy with Sentinel](https://learn.hashicorp.com/collections/terraform/policy#sentinel)

## Reverse terraform with Terraformer

- [github.com/GoogleCloudPlatform/terraformer 🌟](https://github.com/GoogleCloudPlatform/terraformer) A CLI tool that generates tf/json and tfstate files based on existing infrastructure (reverse Terraform).
- @ryanhos' process: "If it’s anything reasonably complex, my process is:"
	1. Build w/ UI
	2. Gen w/ **Terraformer** (local state)
	3. Fix crazy codegen-ed names
	4. Import TF, verify Cloud == State == Terraform
	5. rm -rf the manual version
	6. Recreate from TF
	7. Test and iterate w/ IaC

## Terraform Tools

- [Brainboard 🌟](https://www.brainboard.co/) Interesting solution for building infrastructure visually before generating terraform code automatically from the designed architecture
- [terrascan 🌟](https://runterrascan.io/) Use terrascan to detect compliance and security violations
    - [youtube: Using tfsec and Jenkins to Secure Your Terraform Code](https://www.youtube.com/watch?v=hbMVGEw0HpE&ab_channel=CloudBeesTV)
    - https://github.com/darinpope/jenkins-example-terraform
    - https://www.jenkins.io/changelog-stable/#v2.289.3
- [Rover - Terraform Visualizer 🌟](https://github.com/im2nguyen/rover) Interactive Terraform visualization. State and configuration explorer.
- [cloudify.co: Cloudify and Terraform Integration. Supercharge Your Terraform Templates](https://cloudify.co/terraform-integration/) Significantly extend Terraform usability with Cloudify's plugin and enjoy end-to-end automation and avoid costly blueprint transformation.
- [cloudquery.io: Announcing CloudQuery Terraform Drift Detection](https://www.cloudquery.io/blog/announcing-cloudquery-terraform-drift-detection)
- [run-x/opta: Opta - Supercharge DevOps on any cloud](https://github.com/run-x/opta) Infrastructure-as-code where you work with high-level constructs instead of getting lost in low level cloud configuration
- [mineiros-io/terramate](https://github.com/mineiros-io/terramate) Terramate is a tool for managing multiple Terraform stacks that comes with support for change detection and code generation.
- [==cycloidio/inframap: Inframap== 🌟](https://github.com/cycloidio/inframap) Read your tfstate or HCL to generate a graph specific for each provider, showing only the resources that are most important/relevant.
    - AWS/Terraform Tip 💛: Visualize your existing ecosystem by creating diagrams from a state file or HCL via 𝗜𝗻𝗳𝗿𝗮𝗠𝗮𝗽. "Why not just 𝘵𝘦𝘳𝘳𝘢𝘧𝘰𝘳𝘮 𝘨𝘳𝘢𝘱𝘩"? InfraMap reduces the resources to the most important ones - making it human-readable 🤖
- [bridgecrewio/AirIAM](https://github.com/bridgecrewio/AirIAM) AirIAM is an AWS IAM to least privilege Terraform execution framework. It compiles AWS IAM usage and leverages that data to create a least-privilege IAM Terraform that replaces the exiting IAM management method. AirIAM was created to promote immutable and version-controlled IAM management to replace today's manual and error prone methods.
- [badarsebard/terraforge](https://github.com/badarsebard/terraforge) Graphical Terraform configuration generator. Terraforge is an application for generating Terraform code visually. Users select providers and then add resources as nodes to a graph that can be edited and arranged. Links between nodes appear automatically as the configuration of a node makes references to other nodes. When finished the design can be exported as Terraform HCL. The configuration will include all settings and configurations entered for the nodes.
- [infracloud.io: 5 Tools to Auto-Generate Terraform Configuration Files 🌟](https://www.infracloud.io/blogs/auto-generate-terraform-configuration-files/)
- [spacelift.io: 18 Most Useful Terraform Tools to Use in 2023](https://spacelift.io/blog/terraform-tools)
- [github.com/idoavrah/terraform-tui: TFTUI - The Terraform textual UI](https://github.com/idoavrah/terraform-tui) TFTUI is a powerful textual UI that empowers users to effortlessly view and interact with their Terraform state. With its latest version you can easily visualize the complete state tree, gaining deeper insights into your infrastructure's current configuration. Additionally, the ability to search the tree and inspect individual resource states allows you to focus on specific details for better analysis and management. It's also possible to select specific resources and perform actions such as tainting, untainting and deleting them. Finally, you are now able to create and apply plans directly from the UI.
- [github.com/jamesw4/confirm-tfvars](https://github.com/jamesw4/confirm-tfvars) Cross platform PowerShell module to validate tfvars files.
- [github.com/inkdrop-org/inkdrop-visualizer](https://github.com/inkdrop-org/inkdrop-visualizer) Terraform Visualizer. Inkdrop is a CLI tool that creates interactive diagrams to visualize your Terraform. It helps you onboard engineers generate documentation and understand dependencies faster.
- [github.com/seal-io/tap: Terraform Advanced Patcher (TAP)](https://github.com/seal-io/tap) Patch Terraform Resource As Your Mind.
- [==github.com/RoseSecurity/Terramaid==](https://github.com/RoseSecurity/Terramaid) **A utility for generating Mermaid diagrams from Terraform configurations**
- [github.com/cloudposse/atmos](https://github.com/cloudposse/atmos) Terraform Orchestration Tool for DevOps. Keep environment configuration DRY with hierarchical imports of configurations, inheritance, and WAY more. Native support for Terraform and Helmfile.
- [github.com/leg100/pug: PUG](https://github.com/leg100/pug) Drive terraform at terminal velocity. A terminal user interface for terraform power users.
    - Perform tasks in parallel (plan, apply, init, etc)
    - Interactively manage state resources (targeted plans, move, delete, etc)
    - Supports terraform, tofu and terragrunt
    - Supports terragrunt dependencies
    - Supports workspaces
    - Automatically loads workspace variable files
    - Backend agnostic (s3, cloud, etc)

## Writing Terraform for unsupported resources with TerraCurl


## Terraform Frameworks

### Kubestack Terraform GitOps Framework

- [==Kubestack: Terraform GitOps Framework== 🌟](https://www.kubestack.com/)

### Gruntwork Terragrunt

- [gruntwork.io](https://gruntwork.io/) Build your infrastructure on top of a collection of over 300,000 lines of reusable, battle-tested infrastructure code written in Terraform, Go, Python, and Bash that has been proven in production at hundreds of companies and is maintained and supported by DevOps experts.
- [==terragrunt.gruntwork.io==](https://terragrunt.gruntwork.io) DRY and maintainable Terraform code. Terragrunt is a thin wrapper that provides extra tools for keeping your configurations DRY, working with multiple Terraform modules, and managing remote state.
- [blog.gruntwork.io: Introducing: The Gruntwork Module, Service, and Architecture Catalogs](https://blog.gruntwork.io/introducing-the-gruntwork-module-service-and-architecture-catalogs-eb3a21b99f70)
- [pie-r/terragrunt-vs-terraspace](https://github.com/pie-r/terragrunt-vs-terraspace)
- [gruntwork-io/terragrunt-infrastructure-live-example](https://github.com/gruntwork-io/terragrunt-infrastructure-live-example) A repo used to show examples file/folder structures you can use with Terragrunt and Terraform
- [infoq.com: Patcher, a Tool to Keep Updating Infrastructure as a Code](https://www.infoq.com/news/2023/04/patcher-iac-upgrade/)

### Terraspace

- [Terraspace.cloud](https://terraspace.cloud/) Terraspace is a Terraform Framework that optimizes for infrastructure-as-code happiness. It provides an organized structure, conventions over configurations, keeps your code DRY, and adds convenient tooling. Terraspace makes working with Terraform easier and more fun.

## Terraform Associate Certification

- [tomwechsler/HashiCorp_Certified_Terraform_Associate](https://github.com/tomwechsler/HashiCorp_Certified_Terraform_Associate) All about HashiCorp Certified: Terraform Associate and exam preparation!

## ChatGPT


## Images

??? note "Click to expand!"

	<center>
	[![developer responsibility vs opta iac responsibility](images/opta_iac_responsibility_vs_developer_.png)](https://www.cncf.io/blog/2022/02/18/introducing-opta-terraform-on-rails/)
	</center>

## Videos

??? note "Click to expand!"

	<center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/PxyyY7TsCqs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/l5k1ai_GBDE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/gxPykhPxRW0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/2Zwrtn-QPk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/C3ptdKC9-EQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/kFt0OGd_LhI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/DeNflzdjxVM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/1Fl25dR01pw?si=Nr_cPtotnts5jO2B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/V53AHWun17s?si=2A3e3qkC7DEbDUnr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/iRaai1IBlB0?si=_yvEAIc2qvZusFKj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/v_T1fuYGjV0?si=W6dxmoEzTxZ1Mxq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/sd2wuAVush4?si=vWkSEsB2-B9TJmlw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/t9flUkifAsE?si=ONNtQzJOKsadtjMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/iVyKvopGnrQ?si=myjkeOO96PvEwNI2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/hBmcwtVQkPM?si=ujDH50fqShdYz9LT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/3pjEcflsSL8?si=xHj3WCDI1C3p4GLN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=_pQAOw0pSqmysSRh&amp;list=PLXb5972EMl4BfKVDMaJH6Pg9SI6q_HqMg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/iLgEK6A31HM?si=3tiTieL4AyBSaZJX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/6OeRByC-sBs?si=uyx7m2z8Gn2EFwZ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/rnSzfaWShGU?si=Kxrfq-7wzny0XR1v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/6OeRByC-sBs?si=4OjYNsUSptbjtEGf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/IORvnr4u8z8?si=uWpAmpeuEhBh2vVn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/3uDxwNOtilU?si=QMSvjjS_DYxEX8T3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	</center>

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

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Yes. If it’s anything reasonably complex, my process is:<br>1.) Build w/ UI<br>2.) Gen w/ <a href="https://twitter.com/hashtag/Terraformer?src=hash&amp;ref_src=twsrc%5Etfw">#Terraformer</a> (local state)<br>3.) Fix crazy codegen-ed names<br>4.) Import TF, verify Cloud == State == <a href="https://twitter.com/hashtag/Terraform?src=hash&amp;ref_src=twsrc%5Etfw">#Terraform</a> <br>5.) rm -rf the manual version<br>6.) Recreate from TF<br>7.) Test and iterate w/ IaC</p>&mdash; Ryan Hochstetler (@ryanhos) <a href="https://twitter.com/ryanhos/status/1483831027709657096?ref_src=twsrc%5Etfw">January 19, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Let&#39;s continue to Terraform🚀<br> <br>The value of a Terraform variable can be set multiple ways, including setting a default value, interactively passing a value when executing a terraform plan and apply, using an environment variable, or setting the value in a .tfvars file. <br><br>(1/2)</p>&mdash; Vrukshali 🦥 (@vrukshali26) <a href="https://twitter.com/vrukshali26/status/1505766330984771588?ref_src=twsrc%5Etfw">March 21, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🏗 AWS/Terraform Tip 💛<br><br>Get an estimate of your costs &amp; a detailed overview of the pricing of each of your AWS resources via 𝗶𝗻𝗳𝗿𝗮𝗰𝗼𝘀𝘁<br><br>You can even preview increased costs estimates for changed or added infrastructure in pull requests 📈 🤩<br><br>Link below ↓ <a href="https://t.co/lyPUiDhWy5">pic.twitter.com/lyPUiDhWy5</a></p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1537455518326956032?ref_src=twsrc%5Etfw">June 16, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🏗 AWS/Terraform Tip 💛<br><br>Visualize your existing ecosystem by creating diagrams from a state file or HCL via 𝗜𝗻𝗳𝗿𝗮𝗠𝗮𝗽<br><br>&quot;Why not just 𝘵𝘦𝘳𝘳𝘢𝘧𝘰𝘳𝘮 𝘨𝘳𝘢𝘱𝘩&quot;?<br>=&gt; InfraMap reduces the resources to the most important ones - making it human-readable 🤖<br><br>Link below ↓ <a href="https://t.co/N43vWyaNjj">pic.twitter.com/N43vWyaNjj</a></p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1539644646959333377?ref_src=twsrc%5Etfw">June 22, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<iframe width="560" height="315" src="https://www.youtube.com/embed/wNllmEAuCTg?si=xyKNxoi-Diu_m5yh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>
</details>