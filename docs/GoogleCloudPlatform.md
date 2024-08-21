# Google Cloud Platform

1. [Introduction](#introduction)
2. [Google Cloud](#google-cloud)
3. [Google Landing Zone](#google-landing-zone)
4. [Dev Library](#dev-library)
5. [GCP Samples (Boilerplates)](#gcp-samples-boilerplates)
6. [Managing Cluster Level Configuration](#managing-cluster-level-configuration)
7. [Google Cloud AppSheet](#google-cloud-appsheet)
8. [Cloud Spanner](#cloud-spanner)
9. [Serverless](#serverless)
10. [Anthos. Google's Hybrid And Multi-Cloud Platform](#anthos-googles-hybrid-and-multi-cloud-platform)
11. [Python](#python)
12. [Cloud Code](#cloud-code)
13. [Google Cloud Buildpacks](#google-cloud-buildpacks)
14. [Google Cloud Deploy](#google-cloud-deploy)
15. [Cloud SQL](#cloud-sql)
16. [Apigee](#apigee)
17. [Tools](#tools)
     1. [gcloud](#gcloud)
     2. [Google Sheets](#google-sheets)
18. [Videos](#videos)
19. [Images](#images)
20. [Tweets](#tweets)

## Introduction

- [cloud.google.com](https://cloud.google.com)
- [==console.cloud.google.com/products==](https://console.cloud.google.com/products)
- [==googlecloudcheatsheet.withgoogle.com: Google Cloud Developer cheat sheet==](https://googlecloudcheatsheet.withgoogle.com)
- [cloud.google.com: DevOps](https://cloud.google.com/devops)
- [Cloud Developer Tools](https://cloud.google.com/products/tools)
- [Google Cloud Code](https://cloud.google.com/code)
- [Google Cloud Build](https://cloud.google.com/cloud-build)
- [medium.com/google-cloud/tagged/devops](https://medium.com/google-cloud/tagged/devops)
- [Platform comparisons](https://cloud.google.com/docs/compare)
    - [AWS and GCP comparison](https://cloud.google.com/docs/compare/aws)
    - [Mapping of AWS services to Google Cloud](https://gregsramblings.com/blog/compare-google-cloud-to-aws/)
- [whizlabs.com: Introduction To Google Cloud Platform](https://www.whizlabs.com/blog/google-cloud-platform/)
- [cloud.google.com: Training more than 40 million new people on Google Cloud skills](https://cloud.google.com/blog/topics/training-certifications/google-cloud-to-train-more-than-40-million-with-cloud-skills)
    - [Google Cloud Skills Boost](https://inthecloud.withgoogle.com/free-training-21/register.html)
- [==cloud.google.com: Microservices architecture on Google Cloud==](https://cloud.google.com/blog/topics/developers-practitioners/microservices-architecture-google-cloud)
- [cloud.google.com: How to get started with Google Cloud: Introducing our new learning hub and learning benefits for Innovators](https://cloud.google.com/blog/topics/training-certifications/new-learning-hub-and-benefits-for-google-cloud-innovators)

## Google Cloud

- [New Cloud Shell Editor: Get your first cloud-native app running in minutes](https://cloud.google.com/blog/products/application-development/introducing-cloud-shell-editor)
- [techradar.com: Google Cloud is making it easier for developers to smuggle ‘secrets’ in their code](https://www.techradar.com/news/google-cloud-is-making-it-easier-for-developers-to-smuggle-secrets-in-their-code) Google Cloud wants to make building secure applications simpler
- [venturebeat.com: Google Cloud announces Network Connectivity Center to simplify hybrid cloud management](https://venturebeat.com/2021/03/23/google-cloud-announces-network-connectivity-center-to-simplify-hybrid-cloud-management)
- [cloud.google.com: Demystifying Cloud Spanner multi-region configurations](https://cloud.google.com/blog/topics/developers-practitioners/demystifying-cloud-spanner-multi-region-configurations) Cloud Spanner remains unique as a managed relational database that scales across regions while maintaining strong consistency. How does the regional and multi-regional setup differ?
- [cloud.google.com: Compare AWS and Azure services to Google Cloud](https://cloud.google.com/free/docs/aws-azure-gcp-service-comparison)
- [thecloudgirl.dev: What is Google Cloud Load Balancing?](https://thecloudgirl.dev/CLB.html)
- [cloud.google.com: Secret Manager Best Practices](https://cloud.google.com/secret-manager/docs/best-practices)
- [cloud.google.com: Choose the best way to use and authenticate service accounts on Google Cloud](https://cloud.google.com/blog/products/identity-security/how-to-authenticate-service-accounts-to-help-keep-applications-secure)
- [cloud.google.com: 5 cheat sheets to help you get started on your Google Cloud journey 🌟](https://cloud.google.com/blog/products/gcp/5-google-cloud-product-cheat-sheets-2021) Sometimes a picture is worth a thousand words, and that’s where these cheat sheets come in handy. Cloud Developer Advocate Priyanka Vergadia has built a number of guides that help developers visually navigate critical decisions, whether it’s determining the best way to move to the cloud, or deciding on the best storage options. Below are five of her top cheat sheets in one handy location.
- [thenewstack.io: Configuring the Google Cloud Platform for High Availability](https://thenewstack.io/configuring-for-high-availability-in-google-cloud-platform/)
- [zdnet.com: Google Cloud rolls out new security tools as threat landscape heats up](https://www.zdnet.com/article/google-cloud-rolls-out-new-security-tools-as-threat-landscape-heats-up/) New tools for the public sector will help agencies comply with President Joe Biden's cybersecurity executive order, while other tools give Google Cloud customers more automated security operations and access to Palo Alto Networks' threat detection technologies.
- [cloud.google.com: Consume services faster, privately and securely - Private Service Connect now in GA](https://cloud.google.com/blog/products/networking/private-service-connect-is-now-generally-available)
- [cloud.google.com: VPN network overview](https://cloud.google.com/vpc/docs/vpc) Most VPC products in the public cloud take a regional approach. If you want to interconnect a bunch of regional VPCs later on, it's tricky. Not with googlecloud. A single VPC is global with automatic communication across regions.
- [kinsta.com: Top 7 Advantages of Choosing Google Cloud Hosting](https://kinsta.com/blog/google-cloud-hosting/)
- [cloud.google.com: Monitor and troubleshoot your VMs in context for faster resolution](https://cloud.google.com/blog/products/operations/better-access-to-observability-data-for-virtual-machines)
- [infoq.com: Google Releases Its Certificate Authority Service into General Availability](https://www.infoq.com/news/2021/08/google-cloud-cas-ga/)
- [cloud.google.com: Your Google Cloud database options, explained](https://cloud.google.com/blog/topics/developers-practitioners/your-google-cloud-database-options-explained)
- [cloud.google.com: A container story - Google Kubernetes Engine](https://cloud.google.com/blog/topics/developers-practitioners/container-story-google-kubernetes-engine)
- [cloud.google.com: Save money and time with automated VM management and suspend/resume](https://cloud.google.com/blog/products/compute/guide-to-cost-optimization-through-automated-vm-management)
- [cloud.google.com: Traffic Director explained!](https://cloud.google.com/blog/topics/developers-practitioners/traffic-director-explained)
- [cloud.google.com: How to transfer your data to Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/how-transfer-your-data-google-cloud)
- [cloud.google.com: Cloud DNS explained!](https://cloud.google.com/blog/topics/developers-practitioners/cloud-dns-explained)
- [cloud.google.com: Where should I run my stuff? Choosing a Google Cloud compute option](https://cloud.google.com/blog/topics/developers-practitioners/where-should-i-run-my-stuff-choosing-google-cloud-compute-option)
- [cloud.google.com: What is Cloud Load Balancing?](https://cloud.google.com/blog/topics/developers-practitioners/what-cloud-load-balancing)
- [cloud.google.com: Google Cloud Networking overview 🌟🌟](https://cloud.google.com/blog/topics/developers-practitioners/google-cloud-networking-overview)
- [cloud.google.com: Service orchestration on Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/service-orchestration-google-cloud)
- [cloud.google.com: The next big evolution in serverless computing](https://cloud.google.com/blog/products/serverless/the-next-big-evolution-in-cloud-computing)
- [==cloud.google.com: Enabling keyless authentication from GitHub Actions==](https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions)
- [cloud.google.com: Cloud IDS for network-based threat detection is now generally available](https://cloud.google.com/blog/products/identity-security/announcing-general-availability-of-google-cloud-ids)
- [cloud.google.com: DevOps and CI/CD on Google Cloud explained](https://cloud.google.com/blog/topics/developers-practitioners/devops-and-cicd-google-cloud-explained)
- [cloud.google.com: What is Cloud CDN and how does it work?](https://cloud.google.com/blog/topics/developers-practitioners/what-cloud-cdn-and-how-does-it-work)
- [==networkmanagementsoftware.com: Google Cloud Platform (GCP) Networking Fundamentals==](https://www.networkmanagementsoftware.com/google-cloud-platform-gcp-networking-fundamentals/)
- [==cloud.google.com: Service Directory cheat sheet==](https://cloud.google.com/blog/topics/developers-practitioners/service-directory-cheat-sheet) Fact: Most enterprises have a large number of heterogeneous services deployed across different clouds and on-premises environments. Fact: It is complex to look up, publish, and connect these services. Fact: Service Directory can help.

## Google Landing Zone

- [medium.com/google-cloud: Design your Landing Zone — Design Considerations Part 4— IaC, GitOps and CI/CD (Google Cloud Adoption Series)](https://medium.com/google-cloud/design-your-landing-zone-design-considerations-part-4-iac-gitops-and-ci-cd-google-cloud-ae3f533c6dbd)

## Dev Library

- [devlibrary.withgoogle.com 🌟](https://devlibrary.withgoogle.com/) New open source content library from Google, a showcase of what developers like you have built with Google technologies.

## GCP Samples (Boilerplates)

- [github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- [github.com/GoogleCloudPlatform/cloud-code-samples 🌟](https://github.com/GoogleCloudPlatform/cloud-code-samples)
- [kelseyhightower/cmd-tutorial](https://github.com/kelseyhightower/cmd-tutorial) This tutorial will walk you through provisioning some VMs on GCP so you can kick the tires on Cmd -- Track and Control Users in Production.

## Managing Cluster Level Configuration

- [Config Sync Overview](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/overview) One of the most challenging day two concerns for Kubernetes users is managing cluster level configuration, think namespaces, CRDs, and RBAC rules, across multiple clusters. For GKE customers Config Sync is a game changer.

## Google Cloud AppSheet

- [Google Cloud AppSheet](https://cloud.google.com/appsheet)
- [infoworld.com: Google Cloud AppSheet review: No-code with extras](https://www.infoworld.com/article/3640975/google-cloud-appsheet-review-no-code-with-extras.html) Google’s easy no-code app builder lets you add functionality with spreadsheet formulas and expressions, and even apply machine learning models.

## Cloud Spanner

- https://cloud.google.com/spanner
- https://github.com/cloudspannerecosystem/autoscaler
- [engineering.mercari.com: Kubernetes based autoscaler for Cloud Spanner](https://engineering.mercari.com/en/blog/entry/20211222-kubernetes-based-spanner-autoscaler/)

## Serverless

- [Cloud Functions, meet VPC functionality](https://cloud.google.com/blog/products/serverless/learn-how-to-use-advanced-vpc-functionality-with-your-cloud-functions)

## Anthos. Google's Hybrid And Multi-Cloud Platform

- [Anthos 🌟](https://cloud.google.com/anthos/)
- [Everything You Want To Know About Anthos - Google's Hybrid And Multi-Cloud Platform](https://www.forbes.com/sites/janakirammsv/2019/04/14/everything-you-want-to-know-about-anthos-googles-hybrid-and-multi-cloud-platform/)
- [itnext.io: Anthos — Multi-cluster Management](https://itnext.io/anthos-multi-cluster-management-aa6f2c03120d)
- [itnext.io: Ingress for Anthos — Multi-cluster Ingress and Global Service Load Balancing](https://itnext.io/ingress-for-anthos-multi-cluster-ingress-and-global-service-load-balancing-c56c57b97e82)
- [A hybrid cloud-native DevSecOps pipeline with JFrog Artifactory and GKE on-prem 🌟](https://cloud.google.com/solutions/partners/a-hybrid-cloud-native-devsecops-pipeline-with-jfrog-artifactory-and-gke-on-prem) Running in a hybrid environment means that some of your processing happens on Google Cloud and other processing remains on-premises. Anthos helps you manage both an on-premises Kubernetes cluster and a cluster running on Google Cloud.
- [Bringing Kubernetes’ goodness to Windows Server apps with Anthos](https://cloud.google.com/blog/topics/anthos/windows-server-support-comes-to-anthos-on-prem) Windows container support to GKE on-premises through Anthos.
- [cloud.google.com: Anthos makes multi-cloud easier with new API, support for Azure](https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-anthos-multicloud-api-and-gke-on-azure-ga)
- [medium.com/google-cloud: Anthos-at-Home: Spinning Up a Bare-Metal Anthos Cluster on Dumpster Servers](https://medium.com/google-cloud/anthos-at-home-spinning-up-a-bare-metal-anthos-cluster-on-dumpster-servers-5bcef301cfa5) In this article, you will learn the capabilities of Anthos on bare metal and find a detailed guide and explanation on how to do it yourself

## Python

- [anderfernandez.com: Cómo automatizar un script de Python en Google Cloud](https://anderfernandez.com/blog/automatizar-script-python-google-cloud/)

## Cloud Code

- [Cloud Code 🌟](https://cloud.google.com/code) Everything you need to write, debug, and deploy your cloud-native applications.

## Google Cloud Buildpacks

- [Google Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks)

## Google Cloud Deploy

- [cloud.google.com: Introducing Google Cloud Deploy: Managed continuous delivery to GKE](https://cloud.google.com/blog/products/devops-sre/google-cloud-deploy-automates-deploys-to-gke)
- [cloud.google.com: Google Cloud Deploy, now GA, makes it easier to do continuous delivery to GKE](https://cloud.google.com/blog/products/devops-sre/google-cloud-deploy-now-ga)
- [infoq.com: Google's Managed Continuous Delivery Service for Kubernetes Moves to GA](https://www.infoq.com/news/2022/02/google-cloud-deploy/)

## Cloud SQL

- [Testing Cloud SQL failover: Where to begin](https://cloud.google.com/blog/topics/developers-practitioners/testing-cloud-sql-failover-where-begin)

## Apigee

- [Announcing Apigee Integration: An API-first approach for connecting data and applications](https://cloud.google.com/blog/products/api-management/google-cloud-announces-apigee-integration)

## Tools

- [db-auth-gateway](https://github.com/kloeckner-i/db-auth-gateway) An authentication proxy for Google Cloud managed databases

### gcloud

- [==cloud.google.com: Declarative Export. Build your perfect Google Cloud infrastructure using Terraform and the gcloud CLI==](https://cloud.google.com/blog/products/application-development/google-cloud-cli-declarative-export-preview) **Google Cloud CLI’s preview release of Declarative Export for Terraform. Declarative Export allows you to export the current state of your Google Cloud infrastructure into a descriptive file compatible with Terraform (HCL) or Google’s KRM declarative tooling.**
- [==cloud.google.com: The gcloud tool cheat sheet==](https://cloud.google.com/sdk/docs/cheatsheet?hl=en)
- [github.com/GoogleCloudPlatform/k8s-config-connector: GCP Config Connector](https://github.com/GoogleCloudPlatform/k8s-config-connector) Config Connector is a Kubernetes add-on that allows you to manage GCP resources, such as Cloud Spanner or Cloud Storage, through your Kubernetes cluster's API

### Google Sheets

- [freecodecamp.org: Web Scraping with Google Sheets – How to Scrape Web Pages with Built-in Functions](https://www.freecodecamp.org/news/web-scraping-google-sheets/)

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Zztufl4mFQ4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Images

??? note "Click to expand!"

	<center>

	[![gcp persistent disk](images/gcp_disks.jfif)](https://twitter.com/pvergadia)

    [![google cloud devops flow](images/google_cloud_devops_flow.jfif)](https://cloud.google.com/deploy/docs/deploy-app-run)
	</center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🎟 You want to get a ticket to <a href="https://twitter.com/googlecloud?ref_src=twsrc%5Etfw">@googlecloud</a> networking, it&#39;s really cool!<br>🤓 I take an example company and walk trough the different networking services, take look 👉 <a href="https://t.co/tTwLp7DXH4">https://t.co/tTwLp7DXH4</a><a href="https://twitter.com/hashtag/cloudnetworking?src=hash&amp;ref_src=twsrc%5Etfw">#cloudnetworking</a> <a href="https://twitter.com/hashtag/cloudcomputing?src=hash&amp;ref_src=twsrc%5Etfw">#cloudcomputing</a> <a href="https://t.co/yFVEUpLy1g">pic.twitter.com/yFVEUpLy1g</a></p>&mdash; Priyanka Vergadia (@pvergadia) <a href="https://twitter.com/pvergadia/status/1455233394476998660?ref_src=twsrc%5Etfw">November 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Our new managed continuous service delivery, <a href="https://twitter.com/googlecloud?ref_src=twsrc%5Etfw">@googlecloud</a> Deploy, just became generally available. <br><br>I&#39;m supposed to be working on something else, but I want to check it out. Let&#39;s procrastinate on real-work together, shall we? <br><br>Quick 🧵 as I deploy a <a href="https://twitter.com/hashtag/dotnet?src=hash&amp;ref_src=twsrc%5Etfw">#dotnet</a> app to GKE. <a href="https://t.co/Ve07Gnog7q">pic.twitter.com/Ve07Gnog7q</a></p>&mdash; Richard Seroter (@rseroter) <a href="https://twitter.com/rseroter/status/1484585434432749573?ref_src=twsrc%5Etfw">January 21, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Creating a GCP service account for each running k8s deployment is ugly. Thankfully, good folks working on Workload Identity <a href="https://twitter.com/googlecloud?ref_src=twsrc%5Etfw">@googlecloud</a> have conjured up some dark magic that allows you to bind RBAC directly to Kubernetes service accounts!<br><br>Checkout a short demo 🧵 showing how…</p>&mdash; Nick Eberts (@nicholas_eberts) <a href="https://twitter.com/nicholas_eberts/status/1504860417201520643?ref_src=twsrc%5Etfw">March 18, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
