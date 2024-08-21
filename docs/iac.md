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

- [stackoverflow.blog: Infrastructure as code: Create and configure infrastructure elements in seconds](https://stackoverflow.blog/2021/03/08/infrastructure-as-code-create-and-configure-infrastructure-elements-in-seconds/) IaC allows developers to supply IT environments with multiple lines of code and can be deployed in a matter of minutes (in contrast to manual infrastructure, which can take hours if not days to be deployed).
- [invensislearning.com: Infrastructure as a Code Tutorial: How it Works, Types, and Best Practices](https://www.invensislearning.com/blog/infrastructure-as-a-code-tutorial/)
- [agileconnection.com: Infrastructure as Code: The Foundation of Effective DevOps](https://www.agileconnection.com/article/infrastructure-code-foundation-effective-devops)
- [cloudify.co: Infrastructure As Code – Is It REALLY Enough For DevOps? IAC DevOps Best Practices 🌟](https://cloudify.co/blog/infrastructure-as-code-is-it-really-enough-for-devops/)
- [bridgecrew.io: 5 tips for securely adopting infrastructure as code](https://bridgecrew.io/blog/5-tips-for-securely-adopting-infrastructure-as-code/)
- [dzone: Why Should You Leverage Infrastructure as Code?](https://dzone.com/articles/reasons-to-leverage-infrastructure-as-code) Learn the essentials of Infrastructure as Code (IaC) and how engineers can utilize its many benefits.
- [redhat.com: Pull vs. push in automated VM provisioning: What you need to know](https://www.redhat.com/architect/pull-push-provisioning-cicd) Understanding the different techniques for provisioning virtual machines in the CI/CD process is essential for enterprise architects planning deployment automation into their designs.
- [itnext.io: Platform-as-Code: how it relates to Infrastructure-as-Code and what it enables](https://itnext.io/platform-as-code-how-it-compares-with-infrastructure-as-code-and-what-it-enables-2684b348be2e)
- [dzone.com: How to Start an Infrastructure as Code Project 🌟](https://dzone.com/articles/how-to-start-an-infrastructure-as-code-project) Learn the best practices to properly start an infrastructure as code project, from the source code to collaboration exercises and tools.
- [daffodilsw.medium.com: What is Infrastructure Automation in DevOps?](https://daffodilsw.medium.com/what-is-infrastructure-automation-in-devops-d9681870b07d)
- [thenewstack.io: IaC Cloud Misconfiguration Tools too Noisy without Context](https://thenewstack.io/iac-cloud-misconfiguration-tools-too-noisy-without-context/)
- [==freecodecamp.org: Infrastructure as Code - Full Course== 🌟🌟](https://www.freecodecamp.org/news/what-is-infrastructure-as-code/)
- [faun.pub: The best Infrastructure as Code tools for 2021](https://faun.pub/the-best-infrastructure-as-code-tools-for-2021-b37c323e89f0)
- [==alpacked.io: Infrastructure as Code in DevOps== 🌟](https://alpacked.io/blog/infrastructure-as-code-for-devops/) Key driving force of efficient application delivery.
- [devops.com: Updating and Managing Infrastructure-as-Code (IaC)](https://devops.com/updating-and-managing-infrastructure-as-code-iac/)
- [thenewstack.io: GUIs, CLI, APIs: Learn Basic Terms of Infrastructure-as-Code](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/)
- [thenewstack.io: Infrastructure-as-Code: Increase Security, Scale Development](https://thenewstack.io/infrastructure-as-code-increase-security-scale-development/)
- [==thenewstack.io: Struggling with IT Staff Leaving? Try Infrastructure as Code== 🌟](https://thenewstack.io/struggling-with-it-staff-leaving-try-infrastructure-as-code/) With IaC, the organization retains critical knowledge of deployment and updates in code repositories, lessening the impact of any one expert leaving
- [devopscube.com: Immutable Infrastructure Explained For Beginners](https://devopscube.com/immutable-infrastructure/)
- [medium.com/@bunnyshell: How to Overcome Infrastructure as Code (IaC) Challenges](https://medium.com/@bunnyshell/how-to-overcome-infrastructure-as-code-iac-challenges-f4947be7cde2)
- [dzone.com/articles: A Beginner's Guide to Infrastructure as Code 🌟](https://dzone.com/articles/a-beginners-guide-to-infrastructure-as-code) In this article, take an in-depth look at how Infrastructure as Code (IaC) works, its benefits, and common challenges.
- [javacodegeeks.com: Infrastructure as Code: Best Tools For 2023 Included](https://www.javacodegeeks.com/2023/03/infrastructure-as-code-best-tools-for-2023-included.html)
- [thenewstack.io: Infrastructure as Code or Cloud Platforms — You Decide!](https://thenewstack.io/infrastructure-as-code-or-cloud-platforms-you-decide/)
- [infoworld.com: 5 priorities that cut cloud costs and improve IT ops](https://www.infoworld.com/article/3692296/5-priorities-that-cut-cloud-costs-and-improve-it-ops.html) With infrastructure as code, virtual desktop infrastructure, and a proactive approach to incident management, you can help keep cloud costs reasonable.
- [spacelift.io: Why Generic CI/CD Tools Will Not Deliver Successful IaC](https://spacelift.io/blog/infrastructure-as-code-with-generic-ci-cd)
- [matt-rickard.com: Infrastructure as Code Will be Written by AI](https://matt-rickard.com/infrastructure-as-code-will-be-written-by-ai)
- [thenewstack.io: Achieve GitOps on Day One with IaC Automation](https://thenewstack.io/achieve-gitops-on-day-one-with-iac-automation/) GitOps helps redefine how we manage infrastructure and application deployments in environments where precision, automation and transparency are vital.
- [medium.com/@faisalkuzhan: DAY_43/90 => Infrastructure as Code(IaC)](https://medium.com/@faisalkuzhan/day-43-90-infrastructure-as-code-iac-5a826258ee4b)
- [build5nines.com: Benefits of Convention over Configuration for IaC Deployment Projects](https://build5nines.com/benefits-of-convention-over-configuration-for-iac-deployment-projects/)
- [levelup.gitconnected.com: Short: Using IaC over Clickops](https://levelup.gitconnected.com/short-using-iac-over-clickops-229e919b5373)

## Local Environment as Code

- [thenewstack.io: Local Environment-as-Code: Is It Possible Yet?](https://thenewstack.io/local-environment-as-code-is-it-possible-yet/)

## Comparing the Tools

- [clickittech.com: Infrastructure as Code Tools, what are the best IaC tools? 🌟](https://www.clickittech.com/devops/infrastructure-as-code-tools/)
- [intellipaat.com: Terraform vs Ansible: Key Differences Between Terraform and Ansible 🌟](https://intellipaat.com/blog/terraform-vs-ansible-difference)
- [clickittech.com: Terraform vs CloudFormation: The Final battle 🌟](https://www.clickittech.com/devops/terraform-vs-cloudformation/)
- [k21academy.com: Terraform vs Ansible: Working, Difference, Provisioning 🌟](https://k21academy.com/ansible/terraform-vs-ansible)
- [cncf.io: Cloudformation vs. Terraform: Which is better?](https://www.cncf.io/blog/2021/04/06/cloudformation-vs-terraform-which-is-better/)
- [cloudify.co: Ansible Vs Terraform 🌟](https://cloudify.co/blog/ansible-vs-terraform/)
- [techcommunity.microsoft.com: Infrastructure as Code (IaC): Comparing the Tools](https://techcommunity.microsoft.com/t5/itops-talk-blog/infrastructure-as-code-iac-comparing-the-tools/ba-p/3205045)
- [spacelift.io: Terraform vs. Ansible : Key Differences and Comparison of Tools](https://spacelift.io/blog/ansible-vs-terraform)
- [env0.com: Ansible vs Terraform: Choose One or Use Both?](https://www.env0.com/blog/ansible-vs-terraform-when-to-choose-one-or-use-them-together)
- [awstrainingwithjagan.com: Comprehensive Comparison of Top Infrastructure as Code (IaC) Tools](https://awstrainingwithjagan.com/infrastructure-as-code-tool-comparison/)

## Tools

- [==Checkmarx/kics==](https://github.com/Checkmarx/kics) Find security vulnerabilities, compliance issues, and infrastructure misconfigurations early in the development cycle of your infrastructure-as-code with KICS by Checkmarx. KICS stands for Keeping Infrastructure as Code Secure, it is open source and is a must-have for any cloud native project.
- [==gofireflyio/aiac== 🌟](https://github.com/gofireflyio/aiac) **Artificial Intelligence Infrastructure-as-Code Generator.**
- [==github.com/gofireflyio/aiac: AIaC==](https://github.com/gofireflyio/aiac) Artificial Intelligence Infrastructure-as-Code Generator.

## Infrastructure as Code using Kubernetes

- [medium.com/nerd-for-tech: Kubernetes: Declaratively Deploying Infrastructure (IaC)](https://medium.com/nerd-for-tech/kubernetes-declaratively-deploying-infrastructure-iac-789f14d999c6) “Declaring the Kubes”

### Config Connector

- [==cloud.google.com/config-connector==](https://cloud.google.com/config-connector/docs/overview) Config Connector is an open source Kubernetes addon that allows you to manage Google Cloud resources through Kubernetes.
- [medium.com/globant: Infrastructure as Code using Kubernetes](https://medium.com/globant/infrastructure-as-code-using-kubernetes-d3d329446517)
    - Config Connector (KCC) is a solution to maintain Cloud Resources as Infrastructure as Code. It is built as an Open Source initiative and runs on Kubernetes clusters. As such, it leverages YAML files to maintain and operate such resources.
    - Config Connector has two versions: an Add-On for Google Kubernetes Engine (GKE) clusters and a manual installation for other Kubernetes distributions.

## Videos

- [youtube: Mitchell Hashimoto: The Inside Story of HashiCorp's IaC Journey | The IaC Podcast](https://www.youtube.com/watch?v=--RRpw_6onA)

??? note "Click to expand!"

	<center>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/POPP2WTJ8es" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/EIOuIwKS0P0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/--RRpw_6onA?si=UNaIShD8z-_ZLCwt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	</center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Jeez, people in my timeline arguing about the merits of CDK vs. Pulumi and I&#39;m just waiting for you all to get on my level. <a href="https://t.co/S3PU7FGuw2">pic.twitter.com/S3PU7FGuw2</a></p>&mdash; Corey Quinn (@QuinnyPig) <a href="https://twitter.com/QuinnyPig/status/1470810573298274307?ref_src=twsrc%5Etfw">December 14, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Do you use the AWS, GCP, or Azure web consoles beyond getting started with a new cloud provider? If so, why not an automation tool such as Terraform or Cloud Formation? <a href="https://t.co/5LIZSTcNpG">pic.twitter.com/5LIZSTcNpG</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1483820927402004484?ref_src=twsrc%5Etfw">January 19, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>