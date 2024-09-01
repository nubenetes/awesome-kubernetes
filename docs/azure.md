# Microsoft Azure

1. [Azure](#azure)
2. [Azure Architecture Check List](#azure-architecture-check-list)
3. [Azure Mindmap](#azure-mindmap)
4. [Azure APIOps](#azure-apiops)
5. [Migration](#migration)
6. [Azure Policy](#azure-policy)
    1. [Azure Policy Best Practices](#azure-policy-best-practices)
7. [Azure Cloud Adoption Framework CAF](#azure-cloud-adoption-framework-caf)
8. [Azure Well-Architected Framework WAF](#azure-well-architected-framework-waf)
    1. [Well-Architected Framework Assessments](#well-architected-framework-assessments)
9. [CAF vs WAF](#caf-vs-waf)
10. [Azure Landing Zones](#azure-landing-zones)
11. [Azure Extended Zones](#azure-extended-zones)
12. [Azure Sandbox](#azure-sandbox)
13. [Azure Marketplace](#azure-marketplace)
14. [Microsoft REST API Guidelines](#microsoft-rest-api-guidelines)
15. [Azure Quick Review](#azure-quick-review)
16. [New Features](#new-features)
17. [Blogs](#blogs)
18. [Azure Training and Certifications](#azure-training-and-certifications)
19. [Azure Naming Convention](#azure-naming-convention)
20. [Mission-critical Architecture on Azure](#mission-critical-architecture-on-azure)
21. [Understand Azure Load Balancing](#understand-azure-load-balancing)
22. [Azure Load Testing](#azure-load-testing)
23. [Microsoft Linux Distribution CBL Mariner](#microsoft-linux-distribution-cbl-mariner)
24. [Azure Patterns](#azure-patterns)
25. [ARM Templates](#arm-templates)
26. [DevTest](#devtest)
27. [Azure DevOps](#azure-devops)
     1. [Azure DevOps Backup Tool](#azure-devops-backup-tool)
     2. [Azure DevOps vs GitHub Actions](#azure-devops-vs-github-actions)
     3. [YAML Schema in DevOps Azure Pipelines](#yaml-schema-in-devops-azure-pipelines)
     4. [Azure Pipeline Tasks](#azure-pipeline-tasks)
     5. [Azure DevOps Templates or Snippets](#azure-devops-templates-or-snippets)
     6. [Databricks CI/CD with Azure DevOps](#databricks-cicd-with-azure-devops)
28. [Azure AD and RBAC. Azure Tenant and Azure Subscription. Service Principal SPN. Microsoft Entra](#azure-ad-and-rbac-azure-tenant-and-azure-subscription-service-principal-spn-microsoft-entra)
     1. [Register applications in Azure AD. Authenticate apps and services](#register-applications-in-azure-ad-authenticate-apps-and-services)
     2. [Azure AD Pen Testing](#azure-ad-pen-testing)
29. [Azure Arc. Azure’s Hybrid And Multi-Cloud Platform. GitOps with Azure Arc](#azure-arc-azures-hybrid-and-multi-cloud-platform-gitops-with-azure-arc)
30. [Secure DevOps Kit for Azure](#secure-devops-kit-for-azure)
31. [Azure App Service](#azure-app-service)
32. [Azure Application Gateway](#azure-application-gateway)
33. [Azure Functions](#azure-functions)
34. [Azure Monitor](#azure-monitor)
     1. [Azure Monitor managed service for Prometheus](#azure-monitor-managed-service-for-prometheus)
35. [Azure Log Analytics](#azure-log-analytics)
36. [Azure Grafana](#azure-grafana)
37. [Mobile Apps](#mobile-apps)
38. [Powershell](#powershell)
     1. [Azure Enterprise Policy As Code (EPAC)](#azure-enterprise-policy-as-code-epac)
     2. [Microsoft Graph PowerShell SDK](#microsoft-graph-powershell-sdk)
     3. [Powershell repos](#powershell-repos)
     4. [Crescendo powershell module](#crescendo-powershell-module)
     5. [Secrets Management with Powershell](#secrets-management-with-powershell)
     6. [Azure Resource Inventory](#azure-resource-inventory)
39. [Azure CLI. AZ CLI](#azure-cli-az-cli)
40. [Azure Run Command](#azure-run-command)
41. [IaC with PowerShell DSC Desired State Configuration](#iac-with-powershell-dsc-desired-state-configuration)
42. [Azure Bicep](#azure-bicep)
43. [Azure Verified Modules](#azure-verified-modules)
44. [Azure Cross region Load Balancer](#azure-cross-region-load-balancer)
45. [Azure Traffic Manager](#azure-traffic-manager)
46. [Azure DNS](#azure-dns)
47. [Azure OpenVPN](#azure-openvpn)
48. [Azure Security](#azure-security)
     1. [Azure Microsoft Defender for Cloud](#azure-microsoft-defender-for-cloud)
     2. [Microsoft Sentinel](#microsoft-sentinel)
49. [Microsoft Copilot for Azure](#microsoft-copilot-for-azure)
50. [Azure Virtual WAN. vWAN](#azure-virtual-wan-vwan)
51. [Azure Fleet](#azure-fleet)
52. [Data Ingestion. Azure Data Factory](#data-ingestion-azure-data-factory)
53. [WinGet Windows Package Manager CLI](#winget-windows-package-manager-cli)
54. [Windows 11](#windows-11)
55. [Azure API Management](#azure-api-management)
56. [Azure Container Apps](#azure-container-apps)
57. [Azure Container Instances](#azure-container-instances)
58. [Azure Container Storage](#azure-container-storage)
59. [Windows Server Container Host](#windows-server-container-host)
60. [Disaster Recovery](#disaster-recovery)
61. [Azure Samples (Boilerplates)](#azure-samples-boilerplates)
62. [Azure Healthcare Data Services](#azure-healthcare-data-services)
63. [Office 365](#office-365)
64. [Azure Books](#azure-books)
65. [Azure OpenAI](#azure-openai)
66. [Windows Tools](#windows-tools)
67. [Azure Tools](#azure-tools)
68. [Images](#images)
69. [Videos](#videos)
70. [Tweets](#tweets)

<center>
[![Azure Terraformer](images/azure-terraformer.jpg){: style="width:7%"}](https://www.youtube.com/@azure-terraformer)
</center>

## Azure

- [Microsoft Azure](https://azure.microsoft.com/)
- [Microsoft Docs](https://docs.microsoft.com/)
- [Azure Docs](https://docs.microsoft.com/azure)
- [Azure Updates 🌟](https://azure.microsoft.com/en-us/updates/)
- [Azure Updates AKS 🌟](https://azure.microsoft.com/en-us/updates/?query=AKS)
- [==azurecharts.com: Azure Charts==](https://azurecharts.com/) Live visual exploration environment for Azure Cloud + ecosystem. Cloud representation metrics auto-updated continuously
    - [==azurecharts.com/learning: Azure Learning Explorer==](https://azurecharts.com/learning) Discover published Azure learning modules, paths, videos, certifications, exams for services of your interest.
- [github.com/azure/mission-critical-online: Welcome to Azure Mission-Critical Online Reference Implementation](https://github.com/azure/mission-critical-online) This repository is part of the Azure Mission-Critical open source project that provides a prescriptive architectural approach to building highly-reliable cloud-native applications on Microsoft Azure for mission-critical workloads.
- [techcommunity.microsoft.com: Microsoft Learn - Learning Rooms Directory](https://techcommunity.microsoft.com/t5/custom/page/page-id/learn?product=All)
- [Introducing the third of three Microsoft Clouds: Azure](https://www.catapultsystems.com/blogs/introducing-the-third-of-three-microsoft-clouds-azure/). 4 major sections of the Cloud Models are:
    - On-Premises: As you start on the left in the traditional on-prem configuration you are responsible for all layers of IT from the networking stack all the way up to the applications which are being provided. You may also be responsible for the data center, power, Internet service, and other underlying aspects.
    - Infrastructure as a Service: In IaaS (Take & Bake) the cloud vendor is responsible for the stack from networking through virtualization and your IT team is responsible for the Operating System (OS) through the applications. Common uses of IaaS are testing environments, development environments or hosting of a website.
    - Platform as a Service: In PaaS (Pizza Delivered) the cloud vendor is responsible for the networking layers through the runtime layer and your IT team is responsible for the data and the applications. PaaS is commonly used to test, build and deploy applications for an organization.
    - Software as a Service: In SaaS (Dining Out) the cloud vendor is responsible for all layers from the networking through to the application layer. A common example of SaaS is a web-based email service such as Outlook, Hotmail or Gmail.
- [medium: Scaling Applications in the Cloud](https://medium.com/faun/scaling-applications-in-the-cloud-52bb6dfbac4e)
- [thenewstack.io: Azure Kubernetes Service Replaces Docker with containerd](https://thenewstack.io/azure-kubernetes-service-replaces-docker-with-containerd/)
- [blog.sixeyed.com: You can't always have Kubernetes: running containers in Azure VM Scale Sets](https://blog.sixeyed.com/you-cant-always-have-kubernetes-running-containers-in-azure-vm-scale-sets/)
- [devblogs.microsoft.com: Deploy Spring Boot applications by leveraging enterprise best practices – Azure Spring Cloud Reference Architecture](https://devblogs.microsoft.com/java/deploy-spring-boot-applications-by-leveraging-enterprise-best-practices/)
- [techcommunity.microsoft.com: Non-interactive logins: minimizing the blind spot](https://techcommunity.microsoft.com/t5/azure-sentinel/non-interactive-logins-minimizing-the-blind-spot/ba-p/2287932) In this blog post, we will review the new Azure Sentinel data streams for Azure Active Directory non-interactive, service principal, and managed identity logins. We will also share the new security content we built and updated in the product, which includes analytics rules for the detection part and workbooks to assist our customers to deal with this blind spot.
- [returngis.net: Replicación de blobs entre dos cuentas de Azure Storage en dos tenants diferentes](https://www.returngis.net/2021/06/replicacion-de-blobs-entre-dos-cuentas-de-azure-storage-en-dos-tenants-diferentes/)
- [c-sharpcorner.com: Comparing AWS SQL Server With Azure SQL Database](https://www.c-sharpcorner.com/article/comparing-aws-sql-server-with-azure-sql-database/)
- [techcommunity.microsoft.com: How to create a VPN between Azure and AWS using only managed solutions](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/how-to-create-a-vpn-between-azure-and-aws-using-only-managed/ba-p/2281900)
- [teacdmin.net: How To Enable Multiple RDP Sessions on Windows Server](https://tecadmin.net/how-to-enable-multiple-rdp-sessions-on-windows-server/)
- [k21academy.com: Azure Data Lake Overview For Beginners](https://k21academy.com/microsoft-azure/data-engineer/azure-data-lake/)
- [theregister.com: Microsoft Azure deprecations: API changes will break applications and PowerShell scripts](https://www.theregister.com/2021/09/03/microsoft_azure_deprecations_api_changes/)
- [k21academy.com: Azure RBAC Vs Azure Policies Vs Azure Blueprints](https://k21academy.com/microsoft-azure/azure-rbac-vs-azure-policies-vs-azure-blueprints/)
- [==blog.identitydigest.com: Azure AD workload identity federation with Kubernetes==](https://blog.identitydigest.com/azuread-federate-k8s/) Any k8s cluster, running on any platform, can now securely access Azure resources without keys or secrets through Azure AD Workload Identity Federation.
- [thomasmaurer.ch: How to check the available VM Sizes (SKUs) by Azure Region](https://www.thomasmaurer.ch/2021/02/how-to-check-the-available-vm-sizes-skus-by-azure-region/)
- [docs.microsoft.com: Multi-tenant user management scenarios](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/multi-tenant-user-management-scenarios)
- [docs.microsoft.com: Overview: Cross-tenant access with Azure AD External Identities (Preview)](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/cross-tenant-access-overview) Azure AD organizations can use External Identities cross-tenant access settings to manage how they collaborate with other Azure AD organizations through B2B collaboration. Cross-tenant access settings give you granular control over how external Azure AD organizations collaborate with you (inbound access) and how your users collaborate with external Azure AD organizations (outbound access).
- [==nubesgen.com==](https://nubesgen.com) - [microsoft/NubesGen](https://github.com/microsoft/NubesGen) Going to production on Azure is only one `git push` away. **Kickstart your project on Azure in minutes! Easily generate Terraform and Bicep templates for your project. Automate your infrastructure using GitOps best practices with GitHub Actions. NubesGen is an Open Source project and we are always looking for feedbacks and contributions.**
    - [infoq.com: NubesGen Brings Git Push to Azure Infrastructure](https://www.infoq.com/news/2022/03/nubesgen-azure-infrastructure/)
- [charbelnemnom.com: Move Files Between Azure File Share Tiers and optimize storage costs](https://charbelnemnom.com/move-files-between-azure-file-share-tiers/)
- [==techrepublic.com: What can you do with Azure Files?==](https://www.techrepublic.com/article/what-can-you-do-azure-files/)
- [==satyenkumar.medium.com: Demystifying The Cloud: An Overview of the Microsoft Azure== 🌟🌟🌟](https://satyenkumar.medium.com/demystifying-the-cloud-computing-an-overview-of-the-microsoft-azure-6a5c1fb1799d) Learn how to make the most of the Azure cloud platform in this comprehensive story (Cloud Demystified Series). Go through 80% of Azure in 30 minutes
- [==learn.microsoft.com: Migrate Java applications to Azure== 🌟🌟🌟](https://learn.microsoft.com/en-us/azure/developer/java/migration/migration-overview)
- [blog.cloudtrooper.net: Overlapping IP addresses in a hub-and-spoke network (feat. AVNM & ARS)](https://blog.cloudtrooper.net/2022/11/14/overlapping-ip-addresses-in-a-hub-and-spoke-network-feat-avnm-ars/)
- [blog.cloudtrooper.net: Virtual Network Gateways routing in Azure](https://blog.cloudtrooper.net/2023/02/06/virtual-network-gateways-routing-in-azure/)
- [returngis.net: Monitorizar aplicación Java con Spring Boot con Azure Application Insights](https://www.returngis.net/2023/04/monitorizar-aplicacion-java-con-spring-boot-con-azure-application-insights/)
- [medium.com/awesome-azure: Azure — Most Useful Azure Services Every Developer Must Know](https://medium.com/awesome-azure/azure-most-useful-azure-services-every-developer-must-know-top-azure-paas-serverless-services-developer-c55b829ac6d7)
- [returngis.net: Invitar a usuarios externos a un tenant de Azure AD a través de Microsoft Graph y Azure CLI](https://www.returngis.net/2023/04/invitar-a-usuarios-externos-a-un-tenant-de-azure-ad-a-traves-de-microsoft-graph-y-azure-cli)
- [==learn.microsoft.com: Choose an Azure compute service== 🌟🌟](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)
- [nwktimes.blogspot.com: NVA Part IV: NVA Redundancy with Azure Internal Load Balancer](https://nwktimes.blogspot.com/2023/06/azure-ilb-for-nva-ha.html)
- [==azure.microsoft.com: Choose the best global distribution solution for your applications with Azure==](https://azure.microsoft.com/en-us/blog/choose-the-best-global-distribution-solution-for-your-applications-with-azure/)
- [blog.davesdomain.co.uk: A look at Azure RBAC Constrained Delegation](https://blog.davesdomain.co.uk/posts/azure-rbac-constrained-delegation)
- [linkedin.com: Azure Networking | Filiz Akkaya](https://www.linkedin.com/pulse/azure-networking-filiz-akkaya-wqcuc/)
- [allazureblog.wordpress.com: Azure Bastion vs UDR](https://allazureblog.wordpress.com/2024/01/18/azure-bastion-and-udrs/)
- [medium.com/@mikakrief: Using Azure Service Operator v2](https://medium.com/@mikakrief/using-azure-service-operator-v2-4a1fa1f5e3b8) Azure Service Operator v2 is a Kubernetes operator that enables you to manage Azure resources directly through Kubernetes tooling. It’s designed to simplify the deployment and management of Azure services, allowing developers to use familiar Kubernetes commands (like kubectl apply) to handle Azure resources.
- [blog.cloudtrooper.net: Azure network monitoring with synthetic traffic](https://blog.cloudtrooper.net/2024/01/23/azure-network-monitoring-with-synthetic-traffic/)
- [techcommunity.microsoft.com: Leveraging Azure Event Hub, Microsoft Fabric, and Power BI for Real-Time Data Analytics](https://techcommunity.microsoft.com/t5/educator-developer-blog/leveraging-azure-event-hub-microsoft-fabric-and-power-bi-for/ba-p/4028701)
- [techcommunity.microsoft.com: Azure SQL Managed Instance pools: new features](https://techcommunity.microsoft.com/t5/azure-sql-blog/azure-sql-managed-instance-pools-new-features/ba-p/4044688)
- [github.com/Azure/Enterprise-Scale: ALZ AMA Update](https://github.com/Azure/Enterprise-Scale/wiki/ALZ-AMA-Update) The Log Analytics agent, also known as the Microsoft Monitoring Agent (MMA), is on a deprecation path and won't be supported after August 31, 2024. Any new data centers brought online after January 1 2024 will not support the Log Analytics agent. If you use the Log Analytics agent to ingest data to Azure Monitor, migrate to the new Azure Monitor agent prior to that date.
- [blog.siliconvalve.com: Analysing git commit history using Azure Data Explorer](https://blog.siliconvalve.com/posts/2024/02/06/analysing-git-commit-history-using-azure-data-explorer)
- [azure.microsoft.com: Generally available: Azure Blob Storage Cold Tier support on Change Feed and Object Replication](https://azure.microsoft.com/en-us/updates/generally-available-azure-blob-storage-cold-tier-support-on-change-feed-and-object-replication/)
- [hlokensgard.no: Azure Firewall as DNS Proxy with the new Azure DNS Resolver](https://hlokensgard.no/2023/07/03/azure-firewall-as-dns-proxy-with-the-new-azure-dns-resolver/)
- [linkedin.com/pulse: The Who's Who of the Azure Configuration Management Landscape | Mark Tinderholt](https://www.linkedin.com/pulse/whos-who-azure-configuration-management-landscape-mark-tinderholt-nm7ve/)
- [techcommunity.microsoft.com: Microsoft Fabric - Multi-Tenant Architecture](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/microsoft-fabric-multi-tenant-architecture/ba-p/4119429)
- [build5nines.com: Why do Azure Resource Groups have an Azure Region association?](https://build5nines.com/why-do-azure-resource-groups-have-an-azure-region-association/)
- [build5nines.com: Read and Write Azure Blob Storage with Javascript](https://build5nines.com/read-and-write-azure-blob-storage-with-javascript/)
- [techcommunity.microsoft.com: Azure Orphan Resources](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/azure-orphan-resources/ba-p/3492198)
    - [github.com/dolevshor/azure-orphan-resources](https://github.com/dolevshor/azure-orphan-resources) Centralize orphan resources in Azure environments
- [build5nines.com: Azure CDN POP Locations: Interactive Map of Azure CDN Points of Presence](https://build5nines.com/azure-cdn-endpoint-interactive-map/)

## Azure Architecture Check List

- [luke.geek.nz/azure: Azure Architecture - Solution Requirement Consideration Checklist](https://luke.geek.nz/azure/azure-architecture-solution-requirement-consideration-checklist/)

## Azure Mindmap

- [github.com/sajeetharan/azure-mindmap](https://github.com/sajeetharan/azure-mindmap) Solution Architecture Patterns and Checklists Mind Map for beginners on Azure
    - [Azure Fundamentals: AZ-900.pdf](https://github.com/sajeetharan/azure-mindmap/blob/master/azure-fundamentals/AZ-900.pdf)
- [techcommunity.microsoft.com: Azure Architecture - Course Blueprint](https://techcommunity.microsoft.com/t5/azure-architecture/course-blueprint/m-p/4012399) This blueprint offers a comprehensive guide to the Azure ecosystem, specifically designed to align with the content of a specific course. It encompasses all resources, tools, structures, and connections discussed throughout the course. The layer filtering feature allows for focused study on specific sections of the course, facilitating a more digestible understanding of the information.

## Azure APIOps

- [github.com/Azure/apiops 🌟](https://github.com/Azure/apiops) APIOps applies the concepts of GitOps and DevOps to API deployment. By using practices from these two methodologies, APIOps can enable everyone involved in the lifecycle of API design, development, and deployment with self-service and automated tools to ensure the quality of the specifications and APIs that they’re building.

## Migration

- [github.com/Azure/migration: The Migration Execution Guide.](https://github.com/Azure/migration) This repo contains a Migration Execution Guide, which has been authored and developed by a team of FastTrack for Azure Program Managers and Engineers working with the Microsoft SMC team, the Azure Advanced Cloud Engineering team and the Customer Success Unit. It provides prescriptive guidance for the structure and running of a successful migration project. The guidance includes digital estate discovery, defining the migration scope with common business drivers, selection and implementation of migration tooling, project management, risk management and many other related templates.

## Azure Policy

- [techcommunity.microsoft.com: Azure Policy for Kubernetes releases support for custom policy](https://techcommunity.microsoft.com/t5/azure-governance-and-management/azure-policy-for-kubernetes-releases-support-for-custom-policy/ba-p/2699466) **A tutorial on how to set up Azure Policy for Kubernetes with custom policies.**
- [arinco.com.au: Awesome Azure Policy Chapter 1](https://arinco.com.au/blog/awesome-azure-policy-chapter-1/)
- [arinco.com.au: Awesome Azure Policy Chapter 2](https://arinco.com.au/blog/awesome-azure-policy-chapter-2/)

### Azure Policy Best Practices

- [Azure Policy Recommended Practices](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/azure-policy-recommended-practices/ba-p/3798024)

## Azure Cloud Adoption Framework CAF

- [learn.microsoft.com: What is the Microsoft Cloud Adoption Framework for Azure?](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview)
- [linkedin.com: The Ultimate Guide to Azure Cloud Adoption Framework Lifecycle](https://www.linkedin.com/pulse/ultimate-guide-azure-cloud-adoption-framework-gregor-wohlfarter-hb4sf/)

## Azure Well-Architected Framework WAF

- [learn.microsoft.com: Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) The Azure Well-Architected Framework (WAF) is a set of quality-driven tenets, architectural decision points, and review tools intended to help solution architects build a technical foundation for their workloads.
- [infoq.com: Microsoft Refreshes its Well-Architected Framework](https://infoq.com/news/2023/11/azure-well-architected-framework)
- [==azure.github.io: Azure Proactive Resiliency Library (APRL)==](https://azure.github.io/Azure-Proactive-Resiliency-Library/)
    - This library is built with the intention of being a staging area for guidance and recommendations that can be used by customers, partners and the field in Well-Architected Framework reliability engagements/assessments; with the intent of the guidance and recommendations being promoted, once tested and validated with customers and partners, into the official Well-Architected Framework documentation.
    - The library also contains supporting Azure Resource Graph (ARG) queries, and sometimes Azure PowerShell or Azure CLI scripts, that can help customers, partners and the field identify resources that may or may not be compliant with the guidance and recommendations. The intent for these queries, in the long-term, is to make them part of the Azure Advisor service.
- [learn.microsoft.com: Azure Well-Architected Framework perspective on Azure App Service (Web Apps)](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/app-service-web-apps)

### Well-Architected Framework Assessments

- [learn.microsoft.com: Use Azure WAF assessments](https://learn.microsoft.com/en-us/azure/advisor/advisor-assessments)
- [techcommunity.microsoft.com: Get tailored insights with our Advisor Well-Architected assessments](https://techcommunity.microsoft.com/t5/finops-blog/get-tailored-insights-with-our-advisor-well-architected/ba-p/4218239)

## CAF vs WAF

- [linkedin.com: CAF vs WAF: Which Framework to Use for Your Cloud Migration?](https://www.linkedin.com/pulse/caf-vs-waf-which-framework-use-your-cloud-migration-gregor-wohlfarter-hko0f/)
- [techcommunity.microsoft.com: Infra in Azure for Developers - The What](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/infra-in-azure-for-developers-the-what/ba-p/4026102)

## Azure Landing Zones

- [medium.com/microsoftazure: Ultimate guide for Enterprise-scale landing zone for Azure](https://medium.com/microsoftazure/ultimate-guide-for-azure-cloud-adoption-framework-for-enterprise-scale-landing-zone-bba2a385134d)
- [techcommunity.microsoft.com: Azure Landing Zones Accelerators for Bicep and Terraform. Announcing General Availability!](https://techcommunity.microsoft.com/t5/azure-tools-blog/azure-landing-zones-accelerators-for-bicep-and-terraform/ba-p/4029866)
- [techcommunity.microsoft.com: Azure OpenAI Landing Zone reference architecture](https://techcommunity.microsoft.com/t5/azure-architecture-blog/azure-openai-landing-zone-reference-architecture/ba-p/3882102)
- [techcommunity.microsoft.com: New feature: easily assign regulatory compliance policies to your Azure Landing Zone](https://techcommunity.microsoft.com/t5/azure-architecture-blog/new-feature-easily-assign-regulatory-compliance-policies-to-your/ba-p/4074957)
- [techcommunity.microsoft.com: Azure landing zones custom archetypes using Terraform](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/azure-landing-zones-custom-archetypes-using-terraform/ba-p/3791172)
- [thomasmaurer.ch: Azure Landing Zone Review Assessment](https://www.thomasmaurer.ch/2023/09/azure-landing-zone-review-assessment/)
- [techcommunity.microsoft.com: From Zero to Hero with Azure Landing Zones](https://techcommunity.microsoft.com/t5/startups-at-microsoft/from-zero-to-hero-with-azure-landing-zones/ba-p/4229195)

## Azure Extended Zones

- [Azure Extended Zones: Azure Extended Zones are small-footprint extensions of Azure to serve low latency or data residency workloads](ttps://learn.microsoft.com/en-us/azure/extended-zones/) Azure Extended Zones enable some key Azure services for customers to deploy. The control plane for these services remains in the region and the data plane is deployed at the Extended Zone site, resulting in a smaller Azure footprint.

## Azure Sandbox

- [Azure Sandbox](https://learn.microsoft.com/en-us/azure/architecture/guide/azure-sandbox/azure-sandbox) Azure Sandbox is a collection of interdependent cloud computing configurations for implementing common Azure services on a single subscription. This collection provides a flexible and cost effective sandbox environment for experimenting with Azure services and capabilities.

## Azure Marketplace

- [azuremarketplace.microsoft.com: Firefly](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/gofireflyltd1705083203658.firefly) Firefly's Cloud Asset Management solution enables Cloud teams to rediscover their entire cloud footprint and manage it more efficiently and consistently as a single inventory across multi-cloud, multi-accounts, and Kubernetes deployments. At the same time, it empowers DevOps to quickly ramp Infrastructure-as-code, and to create and deploy cloud infrastructure safely and consistently within organizational policies.

## Microsoft REST API Guidelines

- [==Microsoft REST API Guidelines== 🌟🌟🌟](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md)

## Azure Quick Review

- [==github.com/Azure/azqr==](https://github.com/Azure/azqr) Azure Quick Review (azqr) is a command-line interface (CLI) tool specifically designed to analyze Azure resources and identify whether they comply with Azure's best practices and recommendations. Its primary purpose is to provide users with a detailed overview of their Azure resources, enabling them to easily identify any non-compliant configurations or potential areas for improvement.

## New Features

- [==azure.microsoft.com: General availability: Azure Bastion native client support==](https://azure.microsoft.com/en-gb/updates/general-availability-azure-bastion-native-client-support/)
- [azure.microsoft.com: Generally available: SFTP support for Azure Blob Storage](https://azure.microsoft.com/en-us/updates/sftp-support-for-azure-blob-storage-now-generally-available/)
- [azure.microsoft.com: Generally Available: Durable Functions support of managed identity for Azure Storage](https://azure.microsoft.com/en-gb/updates/generally-available-durable-functions-support-of-managed-identity-for-azure-storage/) Azure Durable Functions support of managed identity for Azure Storage is now generally available! Instead of embedding secrets in connection strings, you can use an identity-based connection to access Azure Storage. The identity is managed by the Azure platform and does not require you to provision or rotate any secrets. See [quickstart](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-configure-durable-functions-with-credentials) on how to configure managed identity for Azure Storage in your Durable Functions app.
- [Generally available: Azure Bastion now support shareable links](https://azure.microsoft.com/en-us/updates/generally-available-azure-bastion-shareable-links/)
- [theregister.com: Microsoft has made Azure Linux generally available. Repeat, Azure Linux](https://www.theregister.com/2023/05/26/microsoft_azure_linux_container/) Come for the Kubernetes, stay for the containers
- [==azure.microsoft.com: Azure Virtual Network Manager topology view now generally available==](https://azure.microsoft.com/en-us/updates/azure-virtual-network-manager-topology-view-now-generally-available/) AVNM is a highly scalable and available network management solution that allows you to simplify network management across subscriptions globally. Azure Resource Topology (ART) allows you to visualize the resources in your network – collaborating with AVNM results in a topology view contextualized by your AVNM connectivity configurations. [==Connectivity configuration in Azure Virtual Network Manager==](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-connectivity-configuration)
- [hlokensgard.no: Azure Virtual Network Manager – A game changer or just a costly upgrade?](https://hlokensgard.no/2024/07/01/azure-virtual-network-manager-a-game-changer-or-just-a-costly-upgrade/)

## Blogs

- [techcommunity.microsoft.com](https://techcommunity.microsoft.com)
- [thomasthornton.cloud: Thomas Thornton](https://thomasthornton.cloud)
- [thomasmaurer.ch](https://www.thomasmaurer.ch)
- [CommandLine Ninja](https://www.commandline.ninja) PowerShell, Active Directory, GPO & Azure Automation. Learn how to automate using PowerShell!
- [dotnetcurry.com](https://www.dotnetcurry.com/)
- [azurebrains.com: Azurebrains](https://www.azurebrains.com) Blog sobre Tecnologias Cloud, Azure, Inteligencia Artificial, etc.
- [rutlandblog.com](https://rutlandblog.com/) All Things Azure

## Azure Training and Certifications

- [johnthebrit/CertificationMaterials](https://github.com/johnthebrit/CertificationMaterials) A collection of materials related to my certification videos
- [thomasmaurer.ch: How To Learn Microsoft Azure in 2022](https://www.thomasmaurer.ch/2022/01/how-to-learn-microsoft-azure-in-2022/)
- [charbelnemnom.com: Exam AZ-305: Microsoft Certified: Azure Solutions Architect Expert](https://charbelnemnom.com/az-305-exam-study-guide-azure-solutions-architect/)
- [==learn.microsoft.com: Browse all courses, learning paths, and modules== 🌟🌟🌟](https://learn.microsoft.com/en-us/training/browse/?resource_type=course&products=azure)
- [freecodecamp.org: Azure Fundamentals Certification (AZ-900) – Pass the Exam With This Free 8-Hour Course](https://www.freecodecamp.org/news/azure-fundamentals-certification-az-900-exam-course/)
- [learn.microsoft.com: Practice Assessments for Microsoft Certifications](https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications)
- [marketplace.visualstudio.com: Learn Cloud 🌟](https://marketplace.visualstudio.com/items?itemName=azurepaas-tools.vscode-learncloud) Guiding first-time cloud users to deploy to Azure PaaS

## Azure Naming Convention

- [docs.microsoft.com: Define your naming convention](https://docs.microsoft.com/en-gb/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- [github.com/microsoft/CloudAdoptionFramework: Azure Naming Tool](https://github.com/microsoft/CloudAdoptionFramework/tree/master/ready/AzNamingTool)
    - [seifbassem.com: Azure Naming Tool](https://www.seifbassem.com/blogs/posts/azure-naming-tool/)
- [justinoconnor.codes: Azure Periodic Table of Resource Naming Convention Shorthands](https://justinoconnor.codes/2022/08/19/azure-periodic-table-of-resource-naming-convention-shorthands/)

## Mission-critical Architecture on Azure

- [==learn.microsoft.com: Mission-critical baseline architecture on Azure==](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-intro)
- [learn.microsoft.com: Mission-critical workloads](https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-overview)

## Understand Azure Load Balancing

- [docs.microsoft.com: Understand Azure Load Balancing. Decision tree for load balancing in Azure](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)
- [mvark.blogspot.com: Comparison of Azure Front Door, Traffic Manager, Application Gateway & Load Balancer](http://mvark.blogspot.com/2019/12/comparison-of-azure-front-door-traffic.html)

## Azure Load Testing

- [Azure Load Testing](https://azure.microsoft.com/en-gb/products/load-testing)
- [azure.microsoft.com: Microsoft Azure Load Testing is now generally available](https://azure.microsoft.com/en-gb/blog/microsoft-azure-load-testing-is-now-generally-available/)
- [github.com/Azure-Samples/azure-load-testing-samples 🌟](https://github.com/Azure-Samples/azure-load-testing-samples) Samples for Azure Load Testing

## Microsoft Linux Distribution CBL Mariner

- [thenewstack.io: Deploying Microsoft’s New Linux Distribution as a VM is Not Easy](https://thenewstack.io/deploying-microsofts-new-linux-distribution-as-a-vm-is-not-easy/)
- [github.com/microsoft/CBL-Mariner](https://github.com/microsoft/CBL-Mariner) Linux OS for Azure 1P services and edge appliances

## Azure Patterns

- [==mattfeltonma/azure-networking-patterns==](https://github.com/mattfeltonma/azure-networking-patterns)
- [==docs.microsoft.com: Cloud Design Patterns== 🌟](https://docs.microsoft.com/en-us/azure/architecture/patterns/)

## ARM Templates

- [==azure.microsoft.com: Azure Quickstart Templates==](https://azure.microsoft.com/en-us/resources/templates/) Deploy Azure resources through the Azure Resource Manager with community contributed templates to get more done. Deploy, learn, fork and contribute back.
- [thomasmaurer.ch: Learn how to deploy and manage Azure resources with ARM templates](https://www.thomasmaurer.ch/2020/12/learn-how-to-deploy-and-manage-azure-resources-with-arm-templates/)
- [techcommunity.microsoft.com: ARM Template Specs now GA!](https://techcommunity.microsoft.com/t5/azure-governance-and-management/arm-template-specs-now-ga/ba-p/2402618)
- [docs.microsoft.com: Azure Resource Manager template specs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-specs)

## DevTest

- [learn.microsoft.com: DevTest and DevOps for microservice solutions](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/dev-test-microservice)

## Azure DevOps

- [Azure DevOps 🌟](https://azure.microsoft.com/services/devops/)
- [Azure DevOps Labs 🌟](https://www.azuredevopslabs.com/)
- [github.com/nnellans/ado-pipelines-guide: Azure DevOps YAML Pipelines Guide 🌟](https://github.com/nnellans/ado-pipelines-guide)
- [==docs.microsoft.com: Build applications with Azure DevOps (Learning Path)==](https://docs.microsoft.com/en-gb/learn/paths/build-applications-with-azure-devops/)
- [==docs.microsoft.com: Azure Pipelines documentation==](https://docs.microsoft.com/en-gb/azure/devops/pipelines/) Implement continuous integration and continuous delivery (CI/CD) for the app and platform of your choice.
- [microsoft/azure-pipelines-tasks](https://github.com/microsoft/azure-pipelines-tasks)
- [info.acloud.guru: Deploying your first kubernetes app with Azure DevOps](https://info.acloud.guru/resources/deploy-kubernetes-app-with-azure-devops)
- [info.acloud.guru: Azure DevOps VS GitHub: Comparing Microsoft's DevOps Twins](https://info.acloud.guru/resources/azure-devops-vs-github-comparing-microsofts-devops-twins)
- [techcommunity.microsoft.com: Building a path to success for microservices and .NET Core - Project Tye + GitHub Actions](https://techcommunity.microsoft.com/t5/apps-on-azure/building-a-path-to-success-for-microservices-and-net-core/ba-p/1502270)
- [medium: Azure DevOps HandBook !](https://medium.com/@arunksingh16/azure-devops-handbook-d6dcd82da1b7)
- [Azure DevOps Tips: “Each” Loops](https://medium.com/@therealjordanlee/azure-devops-tips-each-loops-c082c692d025)
- [cloudskills.io: Getting Started with Git and Azure DevOps: The Ultimate Guide 🌟](https://cloudskills.io/blog/git-azure-devops)
- [zartis.com: Simplify Your SDLC with Azure DevOps](https://www.zartis.com/simplify-your-sdlc-with-azure-devops/)
- [devblogs.microsoft.com: Controlling Release Pipelines with Gates and Azure Policy Compliance 🌟](https://devblogs.microsoft.com/devops/controlling-release-pipelines-with-gates-and-azure-policy-compliance/)
- [youtube: Azure DevOps Pipeline and Image Builder](https://www.youtube.com/watch?v=zL0eLEl2BxI&ab_channel=TravisRoberts)
- [dev.to: Setting up a CI-CD Pipeline Using Azure DevOps 🌟](https://dev.to/gbengelebs/setting-up-a-ci-cd-pipeline-using-azure-devops-4gb)
- [zartis.com: Simplify Your SDLC with Azure DevOps 🌟](https://www.zartis.com/simplify-your-sdlc-with-azure-devops/)
- [thomasthornton.cloud: Scout Suite reports using Azure DevOps Pipeline](https://thomasthornton.cloud/2021/04/29/scout-suite-reports-using-azure-devops-pipeline/) Interesting article on how to fecth az DevOps pipelines reports as a static website
- [Azure DevOps Dashboard](https://github.com/cschotte/Azure-DevOps-Dashboard)
- [cloud.google.com: Crea una canalización de CI/CD con Azure Pipelines y Compute Engine](https://cloud.google.com/architecture/creating-cicd-pipeline-vsts-compute-engine)
- [letsdevops.net: Introduction to Azure DevOps for Beginners - Create CI/CD Pipelines, Setup Repository 🌟](https://www.letsdevops.net/post/letsdevops-introduction-to-azure-devops-for-beginners)
- [kevinrchant.com: Increase in demand for Data Platform automation](https://www.kevinrchant.com/2021/09/16/increase-in-demand-for-data-platform-automation/)
    - [kevinrchant.com: Introducing my Azure DevOps templates for Data Platform deployments](https://www.kevinrchant.com/2021/09/14/t-sql-tuesday-142-introducing-my-azure-devops-templates-for-data-platform-deployments/)
- [dotnetcurry.com: Customization of Work Items in Azure DevOps and Azure DevOps Server 2020](https://www.dotnetcurry.com/devops/workitem-customize-azure-devops-server-2020)
- [thomast1906/DevOps-The-Hard-Way-Azure 🌟](https://github.com/thomast1906/DevOps-The-Hard-Way-Azure) This repository contains free labs for setting up an entire workflow and DevOps environment from a real-world perspective in Azure
- [==thinksys.com: Azure DevOps Pipeline Complete Guide 2022==](https://www.thinksys.com/azure/azure-devops-pipeline-complete-guide/)
- [techcommunity.microsoft.com: CICD in Synapse SQL: How to deliver your database objects across multiple environments](https://techcommunity.microsoft.com/t5/azure-synapse-analytics-blog/cicd-in-synapse-sql-how-to-deliver-your-database-objects-across/ba-p/3267507)
- [==medium.com/geekculture: Provision resources on AWS with Azure DevOps and Terraform — Part I==](https://medium.com/geekculture/provision-resources-on-aws-with-azure-devops-and-terraform-part-i-3c0de6d34fc9)
    - [==medium.com/geekculture: Provision resources on AWS with Azure DevOps and Terraform — Part II==](https://medium.com/geekculture/provision-resources-on-aws-with-azure-devops-and-terraform-part-ii-45ee450139)
- [==medium.com/@sdevsecops: How to implement DevSecOps in a Kubernetes cluster environment-Github Actions and Azure DevOps==](https://medium.com/@sdevsecops/how-to-implement-devsecops-in-a-kubernetes-cluster-environment-github-actions-and-azure-devops-522bdd121e34)
- [==learn.microsoft.com: Azure DevOps Templates - Template types & usage== 🌟🌟](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/templates)
- [medium.com/geekculture: Continuous Deployment with Azure DevOps Pipelines and Kubernetes](https://medium.com/geekculture/continuous-deployment-with-azure-devops-pipelines-and-kubernetes-12fe1c70b343) Create a Continuous Deployment workflow for your application
- [techcommunity.microsoft.com: Azure DevOps Pipelines: If Expressions and Conditions 🌟](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/azure-devops-pipelines-if-expressions-and-conditions/ba-p/3737159)
- [linkedin.com: Complete CI/CD Solution for mS on AKS using Azure DevOps, ArgoCD and External Kubernetes Secretes 🌟](https://www.linkedin.com/pulse/complete-cicd-solution-ms-aks-using-azure-devops-argocd-singh/)
- [techcommunity.microsoft.com: Introduction to Azure DevOps Workload identity federation (OIDC) with Terraform](https://techcommunity.microsoft.com/t5/azure-devops-blog/introduction-to-azure-devops-workload-identity-federation-oidc/ba-p/3908687)
- [==datascientest.com: Azure DevOps Pipeline YAML: why configure CI/CD pipelines with YAML?==](https://datascientest.com/en/azure-devops-pipeline-yaml-why-configure-ci-cd-pipelines-with-yaml)
- [thomasthornton.cloud: Conditional Variables in Azure DevOps Pipelines](https://thomasthornton.cloud/2021/08/04/conditional-variables-in-azure-devops-pipelines/)
- [build5nines.com: Azure Pipeline: Publish Unit Test and Code Coverage Results with .NET 7 Solution using VSTest, Cobertura, and Coverlet](https://build5nines.com/azure-pipeline-publish-unit-test-and-code-coverage-results-with-net-solution-using-vstest-cobertura-and-coverlet/)
- [thomasthornton.cloud: Adding pull-request comments to Azure DevOps Repo from Azure DevOps Pipelines](https://thomasthornton.cloud/2024/01/18/adding-pull-request-comments-to-azure-devops-repo-from-azure-devops-pipelines/)
- [==towardsdev.com: Azure DevOps Project Creation and Setup via Terraform==](https://towardsdev.com/azure-devops-project-creation-and-setup-via-terraform-3444ff985bae)
- [==devtoolhub.com: Authenticate Azure Portal with Azure DevOps==](https://devtoolhub.com/2024/02/authenticate-azure-portal-with-azure-devops/) Azure DevOps allows you to establish a connection with Azure services using Service Connections. In this guide, we’ll explore two authentication methods: Service Principal and Workload Identity Federation. Follow the steps below based on your preference.
- [==thomasthornton.cloud: Deploy Terraform using Azure DevOps==](https://thomasthornton.cloud/2020/07/08/deploy-terraform-using-azure-devops/)
- [blog.johnfolberth.com: Resources and posts for those figuring out DevOps in Azure](https://blog.johnfolberth.com/)
- [medium.com/@muppedaanvesh: Azure DevOps — Self Hosted Agents on Kubernetes — PART-1](https://medium.com/@muppedaanvesh/azure-devops-self-hosted-agents-on-kubernetes-part-1-aa91e7912f79) Unlocking Efficiency and Scalability for Your CI/CD Workflows
- [medium.com/@DevOps-Diva.o: Implementing Security on Azure DevOps Pipelines](https://medium.com/@DevOps-Diva.o/implementing-security-on-azure-devops-pipelines-a653da4862a9)
- [luke.geek.nz/azure: Export Azure DevOps Repositories to Azure Storage Account](https://luke.geek.nz/azure/export-azure-devops-repos-azure-storage-account/)
- [learn.microsoft.com: Managed DevOps Pools documentation](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools) Managed DevOps Pool is a fully managed service where VMs or containers powering the agents will live in a Microsoft Azure subscription and not in your own Azure subscription.
- [youtube: Managed DevOps Pools for Azure DevOps | Full Overview & Demo 🌟](https://www.youtube.com/watch?v=FBAav6OoJlw)

### Azure DevOps Backup Tool

- [https://github.com/michaelmsonne/AzureDevOpsBackupTool](https://github.com/michaelmsonne/AzureDevOpsBackupTool/)
- [blog.sonnes.cloud: Introducing Azure DevOps Backup Tool 1.1.0.0: Major update with new features, bug fixes and enhanced security!](https://blog.sonnes.cloud/introducing-azure-devops-backup-tool-1-1-0-0-major-update-with-new-features-bug-fixes-and-enhanced-security/)

### Azure DevOps vs GitHub Actions

- [==datascientest.com: Azure DevOps vs GitHub Actions: Which is the best CI/CD tool?==](https://datascientest.com/en/azure-devops-vs-github-actions-which-is-the-best-ci-cd-tool)

### YAML Schema in DevOps Azure Pipelines

- [==DevOps Azure Pipelines: YAML Schema==](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/pipeline)

### Azure Pipeline Tasks

- [==Microsoft/azure-pipelines-tasks==](https://github.com/Microsoft/azure-pipelines-tasks) This repo contains the tasks that are provided out-of-the-box with Azure Pipelines and Team Foundation Server. This provides open examples on how we write tasks which will help you write other tasks which can be uploaded to your account or server.
    - [github.com/datakickstart](https://github.com/datakickstart)

### Azure DevOps Templates or Snippets

- [github.com/JFolberth/TheYAMLPipelineOne 🌟](https://github.com/JFolberth/TheYAMLPipelineOne)
- [gist.github.com: This snippet contains the steps to generate a terraform plan and post it as a comment of a pull request in Azure DevOps](https://gist.github.com/GTRekter/51f8be3fbfb13b3696f92e117d956597)

    ```yaml
    - script: |
        terraform plan -out tf.tfplan
    displayName: Generate Terraform plan

    - script: |
        terraform show -no-color tf.tfplan > $(Agent.TempDirectory)/tf.txt
    displayName: Convert Terraform plan to text

    - bash: |
        cd $(Agent.TempDirectory)
        ENCODED_URL=$(echo "$(System.CollectionUri)$(System.TeamProject)/_apis/git/repositories/${{ variables.SourceRepositoryName }}/pullRequests/$(System.PullRequest.PullRequestId)/threads?api-version=7.0" | sed 's/ /%20/g')
        jq --rawfile comment tf.txt '.comments[0].content=$comment' <<< '{"comments": [{"parentCommentId": 0,"content": "","commentType": 1}],"status": 1}' |
        curl --request POST "$ENCODED_URL" \
        --header "Content-Type: application/json" \
        --header "Accept: application/json" \
        --header "Authorization: Bearer $SYSTEM_ACCESSTOKEN" \
        --data @- \
        --verbose
    env:
        SYSTEM_ACCESSTOKEN: $(System.AccessToken)
    displayName: 'Post comment with Terraform Plan'
    ```

### Databricks CI/CD with Azure DevOps

- [youtube: Databricks CI/CD: Azure DevOps Pipeline + DABs](https://www.youtube.com/watch?v=SZM49lGovTg) Many organizations choose Azure DevOps for automated deployments on Azure. When deploying to Databricks you can take similar deploy pipeline code that you use for other projects but use it with Databricks Asset Bundles. This video shows most of the steps involved in setting this up by following along with a blog post that shares example code and steps.

## Azure AD and RBAC. Azure Tenant and Azure Subscription. Service Principal SPN. Microsoft Entra

- [==stackoverflow.com: What is the difference between an Azure tenant and Azure subscription?==](https://stackoverflow.com/questions/47307368/what-is-the-difference-between-an-azure-tenant-and-azure-subscription)
- [==marckean.com: Azure Vs Azure AD – Accounts / Tenants / Subscriptions==](https://marckean.com/2016/06/01/azure-vs-azure-ad-accounts-tenants-subscriptions/)
- [blogit.create.pt: Pros and Cons of Single Tenant vs Multiple Tenants in Office 365](https://blogit.create.pt/miguelisidoro/2019/01/07/pros-and-cons-of-single-tenant-vs-multiple-tenants-in-office-365/)
- [learn.microsoft.com: Classic subscription administrator roles, Azure roles, and Azure AD roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles)
- [learn.microsoft.com: Subscriptions, licenses, accounts, and tenants for Microsoft's cloud offerings](https://learn.microsoft.com/en-us/microsoft-365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings?view=o365-worldwide)
- [learn.microsoft.com: Azure subscription and service limits, quotas, and constraints](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits)
    - [learn.microsoft.com: Azure Active Directory limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-active-directory-limits)
- [itnext.io: Secure Azure Cosmos DB access by using Azure Managed Identities](https://itnext.io/secure-azure-cosmos-db-access-by-using-azure-managed-identities-55f9fdf48fda) Getting rid of passwords (or connection strings) while accessing Azure services and instead making use of Managed Identities is a way to increase the security of your workloads. Learn how to use Managed Identities in this article.
- [youtube.com: Azure Service Principal - SPN | Houssem Dellai](https://www.youtube.com/watch?v=-F9yzj4Kjeo&ab_channel=HoussemDellai)
- [youtube.com: How to create Service Principals in Azure Portal | Raaviblog](https://www.youtube.com/watch?v=Hg-YsUITnck)
- [==techcommunity.microsoft.com: Dynamic user membership rules, Azure Active Directory Administrative Units and password reset!== 🌟](https://techcommunity.microsoft.com/t5/azure/dynamic-user-membership-rules-azure-active-directory/m-p/3281164)
- [learn.microsoft.com: Application registration permissions for custom roles in Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/roles/custom-available-permissions)
- [==learn.microsoft.com: What are Azure Active Directory recommendations?== 🌟🌟](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/overview-recommendations)
- [==learn.microsoft.com: Multi-tenant user management introduction==](https://learn.microsoft.com/en-us/entra/architecture/multi-tenant-user-management-introduction)
- [==learn.microsoft.com: Delegate Azure role assignment management to others with conditions==](https://learn.microsoft.com/nb-no/azure/role-based-access-control/delegate-role-assignments-portal)
- [==codewithme.cloud: Why aren’t you using Managed Identities?!==](https://codewithme.cloud/posts/2024/02/why-arent-you-using-secretless-authentication/)
- [linkedin.com/pulse: No Credentials, No Problem - using Azure Managed Identity](https://www.linkedin.com/pulse/credentials-problem-using-azure-managed-identity-dimitar-iliev--wzzaf/)
- [learn.microsoft.com/nb-no: Delegate Azure role assignment management to others with conditions](https://learn.microsoft.com/nb-no/azure/role-based-access-control/delegate-role-assignments-portal?tabs=template)
- [learn.microsoft.com/en-us: Azure built-in roles 🌟🌟](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
- [==techcommunity.microsoft.com: Azure Permissions 101: How to manage Azure access effectively==](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/azure-permissions-101-how-to-manage-azure-access-effectively/ba-p/4067468)
- [techcommunity.microsoft.com: Important: Azure AD Graph Retirement and Powershell Module Deprecation](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/important-azure-ad-graph-retirement-and-powershell-module/ba-p/3848270)
- [journeyofthegeek.com: Azure Authorization – Azure RBAC Delegation](https://journeyofthegeek.com/2024/05/10/azure-authorization-azure-rbac-delegation/)
- [mattias.engineer: Azure Federated Identity Credentials for GitHub](https://mattias.engineer/blog/2024/azure-federated-credentials-github/)

### Register applications in Azure AD. Authenticate apps and services

- [==agrenpoint.com: Azure AD & Microsoft Graph permission scopes, with Azure CLI==](https://www.agrenpoint.com/azcli-adscope/) In this small post, we will look at a scenario where we want to register an Azure AD Application using specific scopes. When adding scopes for service principals using the Azure CLI we need to use the internal Ids. And one way would be to manually create one registration, get that app and then print out the scopes and then copy and paste.
- [==medium.com/medialesson: Create Azure Active Directory App Registration with Azure CLI==](https://medium.com/medialesson/create-azure-active-directory-app-registration-with-azure-cli-3241aa3824c5)
- [inkoop.io: How to get Azure API Credentials](https://www.inkoop.io/blog/how-to-get-azure-api-credentials/) How to create an application in Azure active directory and get subscription id, tenant id, client id, client secret and generate management certificates. You will need these keys to access Azure API.
- [docs.microsoft.com: Use the portal to create an Azure AD application and service principal that can access resource](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)
- [medium.com/medialesson: Assigning Azure built-in roles vs Azure AD built-in roles with Azure CLI](https://medium.com/medialesson/assigning-azure-built-in-roles-vs-azure-ad-built-in-roles-with-azure-cli-d1cbf56fcdbe) Depending on what action you are trying to perform in Azure you might require either to be member of a certain Azure role or a certain Azure AD role. For example **if we want an identity to create an app registration in Azure AD we need the role Application Administrator which is part of the Azure AD roles.** When we want to create a resource in a certain resource group we need the Contributor role which is part of the Azure AD and typically scoped to a either a subscription, a resource group or a distinct resource.
- [microsoftgraph/msgraph-sdk-powershell/samples: 9-Applications.ps1](https://github.com/microsoftgraph/msgraph-sdk-powershell/blob/dev/samples/9-Applications.ps1)
- [vcloud-lab.com: Get started and configure certificate-based authentication in Azure](http://vcloud-lab.com/entries/microsoft-azure/get-started-and-configure-with-certificate-based-authentication-in-azure)
- [vcloud-lab.com: Create an Azure App registrations in Azure Active Directory using PowerShell & AzureCLI](http://vcloud-lab.com/entries/microsoft-azure/create-an-azure-app-registrations-in-azure-active-directory-using-powershell-azurecli)
- [==nathannellans.com: App Registrations, Enterprise Apps, and Service Principals== 🌟](https://www.nathannellans.com/post/app-registrations-enterprise-apps-and-service-principals)
    - [==nathannellans.com: Application Registrations and Enterprise Apps - Part 2== 🌟](https://www.nathannellans.com/post/app-registration-enterprise-apps-part-2)

### Azure AD Pen Testing

- [==zer1t0.gitlab.io: Attacking Active Directory: 0 to 0.9== 🌟](https://zer1t0.gitlab.io/posts/attacking_ad/)

## Azure Arc. Azure’s Hybrid And Multi-Cloud Platform. GitOps with Azure Arc

- [Azure Arc overview](https://docs.microsoft.com/en-us/azure/azure-arc/overview) Alternative to Google Anthos or RHACM
- [azurearcjumpstart.io](https://azurearcjumpstart.io/) - [microsoft/azure_arc](https://github.com/microsoft/azure_arc)
    - [architecture diagrams and slides](https://github.com/microsoft/azure_arc/tree/main/docs/ppt)
- [techcommunity.microsoft.com: Standardize DevOps practices across hybrid and multicloud environments](https://techcommunity.microsoft.com/t5/itops-talk-blog/standardize-devops-practices-across-hybrid-and-multicloud/ba-p/2795010) With Azure Arc-enabled Kubernetes, you can attach and configure Kubernetes clusters located either inside or outside Azure.
- [docs.microsoft.com: CI/CD workflow using GitOps (Flux v2) - Azure Arc enabled Kubernetes](https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-gitops-flux2-ci-cd)
- [thomasmaurer.ch: Run cloud-native apps on Azure PaaS anywhere](https://www.thomasmaurer.ch/2021/06/run-cloud-native-apps-on-azure-paas-anywhere/)
- [seifbassem.com: SSH into your Azure Arc-enabled servers from anywhere](https://www.seifbassem.com/blogs/posts/azure-arc-ssh/)

## Secure DevOps Kit for Azure

- [Secure DevOps Kit for Azure](https://github.com/azsk/DevOpsKit)
- [DevOpsKit-docs](https://github.com/azsk/DevOpsKit-docs)
- [ismiletechnologies.com: Secure DevOps Kit For Azure(AzSK)](https://www.ismiletechnologies.com/devsecops/secure-devops-kit-azureazsk/)

## Azure App Service

- [learn.microsoft.com: Environment variables and app settings in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings)
- [learn.microsoft.com: Configure a Java app for Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/configure-language-java)
- [learn.microsoft.com: Configure a custom container for Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/configure-custom-container)
- [returngis.net: Acceder a un App Service con Private Endpoint desde otra Vnet](https://www.returngis.net/2021/08/acceder-a-un-app-service-con-private-endpoint-desde-otra-vnet/)
- [youtube: How to run an App Service Web App on Azure Arc-enabled Kubernetes - Part 2 | Azure Tips and Tricks](https://www.youtube.com/watch?v=53-Y_aI0KpE&ab_channel=MicrosoftAzure)
- [azure.github.io/AppService: General availability of Diagnostics tools for App Service on Linux Node.js apps](https://azure.github.io/AppService/2024/01/05/Diagnose-Tools-for-NodeJs-Linux-apps.html)

## Azure Application Gateway

- [==nathannellans.com: Azure Application Gateway - Part 1== 🌟](https://www.nathannellans.com/post/azure-application-gateway-part-1)
- [acethecloud.com: Which is better Azure App Gateway or Nginx configured on Azure VMs](https://acethecloud.com/blog/azure-application-gateway-and-nginx-on-vm/)

## Azure Functions

- [learn.microsoft.com: AZ-204: Implement Azure Functions 🌟](https://learn.microsoft.com/en-us/training/paths/implement-azure-functions/)
- [azurebrains.com: Despliega tu Azure Function App con Terraform y Azure DevOps 🌟](https://www.azurebrains.com/2021/03/25/despliega-azure-function-terraform-azuredevops/)

## Azure Monitor

- [techcommunity.microsoft.com: Azure Monitor Logs Next Evolution: Multi-tier logging](https://techcommunity.microsoft.com/t5/azure-observability-blog/azure-monitor-logs-next-evolution-multi-tier-logging/ba-p/4200871)

### Azure Monitor managed service for Prometheus

- [==techcommunity.microsoft.com: Introducing Azure Monitor managed service for Prometheus== 🌟](https://techcommunity.microsoft.com/t5/azure-observability-blog/introducing-azure-monitor-managed-service-for-prometheus/ba-p/3600185)
- [techcommunity.microsoft.com: How To Monitor Your Multi-Tenant Solution on Azure With Azure Monitor](https://techcommunity.microsoft.com/t5/azure-observability-blog/how-to-monitor-your-multi-tenant-solution-on-azure-with-azure/ba-p/4042140)
- [techcommunity.microsoft.com: Advanced Network Observability for your Azure Kubernetes Service clusters through Azure Monitor](https://techcommunity.microsoft.com/t5/azure-observability-blog/advanced-network-observability-for-your-azure-kubernetes-service/ba-p/4176736)

## Azure Log Analytics

- [havanrijn.wordpress.com: Don’t let Azure Log Analytics break the bank](https://havanrijn.wordpress.com/2024/04/01/dont-let-azure-log-analytics-break-the-bank/)

## Azure Grafana

- [techcommunity.microsoft.com: Azure Orphan Resources Grafana Dashboard](https://techcommunity.microsoft.com/t5/azure-for-isv-and-startups/azure-orphan-resources-grafana-dashboard/ba-p/4120303)

## Mobile Apps

- [Visual Studio App Center VS Azure Pipelines](https://docs.microsoft.com/en-us/appcenter/build/choose-between-services)
- [itnext.io: How to setup CI CD pipelines for Android with Azure DevOps](https://itnext.io/how-to-setup-ci-cd-pipelines-for-android-with-azure-devops-2a4ded0de0e7) At Royale Cheese initially we had setup CI/CD for Android via Microsoft’s Visual Studio App Center (an upgrade of Hockey App), but last year they declared the retirement of MBaas which got us worried about the overall future of VS App Center. That was one of the reasons we wanted to switch away from it. Secondly, the free tier provided around 400 minutes of build time per month per account which would had been sufficient for other technologies, but Android takes around 15 minutes to create a single build and deploy. We all know what gradle is capable of 😉. So having multiple apps (both iOS and Android) in the same account didn’t fare well.
- [arjavdave.com: Continuous Integration: CI/CD for iOS (Part 1)](https://arjavdave.com/2021/03/11/continuous-integration-for-ios-on-azure-devops-part-1/)
- [sahansera.dev: Multi-stage builds for Ionic Apps with Azure Pipeline Templates](https://sahansera.dev/multi-stage-builds-with-azure-pipelines-ionic/)
- [sahansera.dev: Publishing Android Apps to Microsoft App Center from Azure DevOps](https://sahansera.dev/publishing-android-apps-to-microsoft-appcenter/)
- [yoshevski.medium.com: Cost-effective Azure Devops and AppCenter integration](https://yoshevski.medium.com/cost-effective-azuredevops-and-appcenter-integration-fe606725d5d5)
- [youtube: Signing & Versioning iOS & Android Apps | DevOps for Mobile](https://www.youtube.com/watch?v=s1grtSSIRVA&ab_channel=dotNET)

## Powershell

- [PowerShell](https://docs.microsoft.com/powershell/)
- [PowerShell Gallery 🌟](https://www.powershellgallery.com/) The central repository for sharing and acquiring PowerShell code including PowerShell modules, scripts, and DSC resources.
- [PowerShell Community](https://devblogs.microsoft.com/powershell-community/)
- [reddit.com: PowerShell Core yaml support?](https://www.reddit.com/r/PowerShell/comments/flzsx5/powershell_core_yaml_support/)
- [powershellmagazine.com](https://powershellmagazine.com/)
- [dbatools.io](https://dbatools.io/) SQL Server instance migrations and best practice implementation.
- [thomasmaurer.ch: PowerShell: Download script or file from GitHub](https://www.thomasmaurer.ch/2021/07/powershell-download-script-or-file-from-github/)
- [deepinstinct.com: What makes powershell a challenge for cybersecurity solutions? 🌟](https://www.deepinstinct.com/2021/07/01/what-makes-powershell-a-challenge-for-cybersecurity-solutions/)
- [fedoramagazine.org: PowerShell on Linux? A primer on Object-Shells](https://fedoramagazine.org/powershell-on-linux-a-primer-on-object-shells/)
- [sqlservercentral.com: Powershell Day by Day: Adding Help to Scripts](https://www.sqlservercentral.com/articles/powershell-day-by-day-adding-help-to-scripts)
- [dahlbyk/posh-git](https://github.com/dahlbyk/posh-git) A PowerShell environment for Git
- [blog.guybarrette.com: Powershell prompt: How to display your current Kubernetes context using Oh-My-Posh 3 🌟](https://blog.guybarrette.com/powershell-prompt-how-to-display-your-current-kubernetes-context-using-oh-my-posh-3)
- [jinwookim928.medium.com: Automation Script for Git Flow on PowerShell](https://jinwookim928.medium.com/automation-script-for-git-flow-on-powershell-70d0596f6da8)
- [youtube: Azure PowerShell account management with Azure contexts | A Cloud Guru 🌟](https://www.youtube.com/watch?v=PjiJsllKZrI&ab_channel=ACloudGuru) If you've been using Azure PowerShell, you might've noticed that when you launch a script, you'll need to authenticate. When you have multiple Azure subscriptions with their own resources, this makes account management difficult. Mark Mikula demonstrates how you can manage multiple Azure subscriptions through Azure Contexts in PowerShell
- [hackingarticles.in: PowerShell for Pentester: Windows Reverse Shell](https://www.hackingarticles.in/powershell-for-pentester-windows-reverse-shell/) We’ll explore how to acquire a reverse shell using Powershell scripts on the Windows platform.
- [hashicorp.com: Managing Terraform Cloud With PowerShell](https://www.hashicorp.com/resources/managing-terraform-cloud-with-powershell)
- [==acloudguru.com: The Beginner’s Guide to Azure PowerShell: One Shell to Rule Them All==](https://acloudguru.com/blog/engineering/one-shell-to-rule-them-all-5-reasons-to-use-powershell-for-cloud-management)
- [dev.to: PowerShell Snippet System](https://dev.to/sharpninja/powershell-snippet-system-4bk3)
- [techcommunity.microsoft.com: An example why PowerShell is so important!](https://techcommunity.microsoft.com/t5/windows-powershell/an-example-why-powershell-is-so-important/m-p/3041748)
- [jdhitsolutions.com: Profile PowerShell Functions](https://jdhitsolutions.com/blog/powershell-7/8793/profile-powershell-functions/)
- [devblogs.microsoft.com: When PowerShellGet v1 fails to install the NuGet Provider](https://devblogs.microsoft.com/powershell/when-powershellget-v1-fails-to-install-the-nuget-provider/)
- [techcommunity.microsoft.com: An example why PowerShell is so important!](https://techcommunity.microsoft.com/t5/windows-powershell/an-example-why-powershell-is-so-important/m-p/3041748) Create 500 training (test) accounts
- [commandline.ninja: Use Powershell to find windows services configured to run as another user](https://www.commandline.ninja/use-powershell-to-find-windows-svcs-configured-to-run-as-another-user/)
- [techcommunity.microsoft.com: Use PowerShell to retrieve all assigned Intune policies and applications per Azure AD group!](https://techcommunity.microsoft.com/t5/microsoft-intune/use-powershell-to-retrieve-all-assigned-intune-policies-and/m-p/3217498)
- [softzone.es: Por qué me interesa más usar PowerShell en lugar de CMD](https://www.softzone.es/noticias/windows/por-que-interesa-usar-powershell-lugar-cmd/)
- [==mssqltips.com: PowerShell for the DBA - If Else and Switch statements==](https://www.mssqltips.com/sqlservertip/7188/powershell-if-if-else-switch-examples/)
- [4sysops.com: Use PsExec and PowerShell together](https://4sysops.com/archives/use-psexec-and-powershell-together/) **How to run PowerShell commands remotely with PsExec**
- [dotnet-helpers.com: Passing Local Variables to Remote PowerShell session](https://dotnet-helpers.com/powershell/passing-local-variables-to-remote-powershell-session/)
- [techcommunity.microsoft.com: Use PowerShell to search for accounts in Active Directory that have gone stale!](https://techcommunity.microsoft.com/t5/windows-server-for-it-pro/use-powershell-to-search-for-accounts-in-active-directory-that/m-p/3585934)
- [techcommunity.microsoft.com: Azure Storage Blob Count & Capacity usage Calculator](https://techcommunity.microsoft.com/t5/azure-paas-blog/azure-storage-blob-count-amp-capacity-usage-calculator/ba-p/3516855) This PowerShell script allow you to count and calculate Azure Storage blob usage for Soft Deleted / non-Soft Deleted objects, by Container, by Tier, with Prefix, and considering Last Modified Date. Azure Storage blob objects is defined as Base Blobs, Blob Snapshots or Blob Versions.
- [dotnet-helpers.com: Azure KeyVault Set and Retrieve Secrets using Powershell 🌟](https://dotnet-helpers.com/powershell/azure-keyvault-set-and-retrieve-secrets/)
- [thomasmaurer.ch: Enable PowerShell SSH Remoting in PowerShell 7](https://www.thomasmaurer.ch/2020/04/enable-powershell-ssh-remoting-in-powershell-7/)
- [hlokensgard.no: Get started with PowerShell 7.2 in Azure Automation Account](https://hlokensgard.no/2023/12/05/get-started-with-powershell-7-2-in-azure-automation-account/)
- [techcommunity.microsoft.com: Azure PowerShell Tips and Tricks](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/azure-powershell-tips-and-tricks/ba-p/4066848)
- [techcommunity.microsoft.com: Announcing a new login experience with Azure PowerShell and Azure CLI](https://techcommunity.microsoft.com/t5/azure-tools-blog/announcing-a-new-login-experience-with-azure-powershell-and/ba-p/4109357)

### Azure Enterprise Policy As Code (EPAC)

- [azure.github.io/enterprise-azure-policy-as-code: Enterprise Azure Policy as Code Overview](https://azure.github.io/enterprise-azure-policy-as-code/) Enterprise Azure Policy as Code (EPAC for short) is a number of PowerShell scripts which can be used in CI/CD based system or a semi-automated use to deploy Policies, Policy Sets, Policy Assignments, Policy Exemptions and Role Assignments. It also contains operational scripts to simplify operational tasks.

### Microsoft Graph PowerShell SDK

- [==microsoftgraph/msgraph-sdk-powershell==](https://github.com/microsoftgraph/msgraph-sdk-powershell) The Microsoft Graph PowerShell SDK is a collection of PowerShell modules that contain commands for calling Microsoft Graph service.
- [==docs.microsoft.com: Get started witth the Microsoft Graph Powershell SDK==](https://docs.microsoft.com/en-us/graph/powershell/get-started) Microsoft Graph Powershell replaces old powershell modules. It is also cross platform.
- [==microsoftgraph/msgraph-sdk-powershell: samples==](https://github.com/microsoftgraph/msgraph-sdk-powershell/tree/dev/samples)
    - [Samples: how to create a corresponding service principal from an application](https://github.com/microsoftgraph/msgraph-sdk-powershell/blob/dev/samples/9-Applications.ps1)
- [docs.microsoft.com: Microsoft Graph migration](https://docs.microsoft.com/en-us/cli/azure/microsoft-graph-migration?tabs=powershell) Due to the deprecation of Azure Active Directory (Azure AD) Graph, the underlying Active Directory Graph API will be replaced by Microsoft Graph API in Azure CLI 2.37.0.
- [==techtarget.com: Get up to speed with PowerShell and the Microsoft Graph API==](https://www.techtarget.com/searchwindowsserver/tutorial/Get-up-to-speed-with-PowerShell-and-the-Microsoft-Graph-API) **Microsoft plans to retire technologies that admins depend on to handle Office 365 and other cloud services via PowerShell. Learn how to start with this newer management method.**
- [rakhesh.com: Graph cmdlets and Azure AD App Registrations](https://rakhesh.com/azure/graph-cmdlets-and-azure-ad-app-registrations/)
- [blog.yannickreekmans.be: Secretless applications: add permissions to a Managed Identity](https://blog.yannickreekmans.be/secretless-applications-add-permissions-to-a-managed-identity/) Your Managed Identity needs permissions to access other Azure resources or even other Azure AD protected applications and APIs. This is how you do that!
    - [YannickRe/msgraph-utility-scripts](https://github.com/YannickRe/msgraph-utility-scripts)
- [practical365.com: The Ups and Downs of Connecting to the Microsoft Graph Using the PowerShell SDK](https://practical365.com/connect-microsoft-graph-powershell-sdk/)
- [practical365.com: Using Certificate-based Authentication with the Microsoft Graph PowerShell SDK](https://practical365.com/use-certificate-authentication-microsoft-graph-sdk/)

### Powershell repos

- [Abhisheksinhacoder/collection-of-useful-scripts](https://github.com/Abhisheksinhacoder/collection-of-useful-scripts)
- [jrussellfreelance/powershell-scripts](https://github.com/jrussellfreelance/powershell-scripts)
- [github.com/search?l=powershell](https://github.com/search?l=powershell&q=stars%3A%3E1&s=stars&type=Repositories)
- [systemcenterdudes.com: Create Operational SCCM Collection Using Powershell Script](https://systemcenterdudes.com/create-operational-sccm-collection-using-powershell-script/)
    - [prae1809/PowerShell-Scripts: OperationalCollections](https://github.com/prae1809/PowerShell-Scripts/tree/master/OperationalCollections) This script will create a set of 134 SCCM collections for your various needs. These collections can be used for operational tasks afterward.
    - [docs.microsoft.com: Introduction to Collections in Configuration Manager](https://docs.microsoft.com/en-us/previous-versions/system-center/system-center-2012-r2/gg682177(v=technet.10))
- [==github.com/Mr-Un1k0d3r/ATP-PowerShell-Scripts==](https://github.com/Mr-Un1k0d3r/ATP-PowerShell-Scripts) Microsoft Signed PowerShell scripts
- [shudnow.io](https://www.shudnow.io) - [github.com/ElanShudnow/AzureCode](https://github.com/ElanShudnow/AzureCode) A place to share all the Azure Code I am writing. This includes PowerShell, Terraform, ARM, Bicep, Ansible, etc...
    - [github.com/ElanShudnow/AzureCode: AzVNETOverlap.ps1](https://github.com/ElanShudnow/AzureCode/blob/main/PowerShell/AzVNETOverlap/README.md) This script creates will output any VNET that overlaps with another VNET.
- [github.com/admindroid-community/powershell-scripts: PowerShell Scripts for Microsoft 365 Management, Reporting, and Auditing](https://github.com/admindroid-community/powershell-scripts) Office 365 Reporting PowerShell Scripts

### Crescendo powershell module

- [Crescendo](https://devblogs.microsoft.com/powershell/announcing-powershell-crescendo-preview-1/) is an experimental module developed by Jim Truher, one of the main developers of PowerShell. Crescendo provides a framework to rapidly develop PowerShell cmdlets that wrap native commands, regardless of platform. The goal of a Crescendo-based module is to create PowerShell cmdlets that use a native command-line tool, but unlike the tool, return PowerShell objects instead of plain text.
- [devblogs.microsoft.com: My Crescendo journey](https://devblogs.microsoft.com/powershell-community/my-crescendo-journey/)
- [powershellgallery.com: Microsoft.PowerShell.Crescendo](https://www.powershellgallery.com/packages/Microsoft.PowerShell.Crescendo) Module that improves user experience with native commands
- [visualstudiomagazine.com: PowerShell Crescendo Now Generally Available](https://visualstudiomagazine.com/articles/2022/03/10/powershell-crescendo-ga.aspx?m=1)

### Secrets Management with Powershell

- https://www.powershellgallery.com/packages/Microsoft.PowerShell.SecretManagement
- https://www.powershellgallery.com/packages/Microsoft.PowerShell.SecretStore
- [commandline.ninja: Video Intro to Secret Management with Powershell](https://www.commandline.ninja/video-intro-to-secret-management-with-powershell/)

### Azure Resource Inventory

- [==github.com/microsoft/ARI: Azure Resource Inventory== 🌟🌟🌟](https://github.com/microsoft/ARI) Azure Resource Inventory - It's a Powerful tool to create EXCEL inventory from Azure Resources with low effort

## Azure CLI. AZ CLI

- [argonsys.com: How to query Azure resources using the Azure CLI](https://argonsys.com/microsoft-cloud/library/how-to-query-azure-resources-using-the-azure-cli/)
- [docs.microsoft.com: Expand virtual hard disks on a Linux VM with the Azure CLI](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/expand-disks#resize-without-downtime-preview)
- [techcommunity.microsoft.com: Announcing template-based previews of Azure CLI and Azure PowerShell for Key Vault deployments](https://techcommunity.microsoft.com/t5/azure-tools-blog/announcing-template-based-previews-of-azure-cli-and-azure/ba-p/3933802)
- [build5nines.com: Azure Resource Tags: Important Organization Strategies and Tips 🌟](https://build5nines.com/azure-resource-tags-important-organization-strategies-and-tips/)
- [build5nines.com: Azure CLI: Check if Blob Exists in Azure Storage](https://build5nines.com/azure-cli-check-if-blob-exists-in-azure-storage/)

## Azure Run Command

- [mandiant.com: Azure Run Command for Dummies](https://www.mandiant.com/resources/azure-run-command-dummies)
- [docs.microsoft.com: Run scripts in your Linux VM by using action Run Commands](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/run-command)
- [docs.microsoft.com: Run scripts in your Windows VM by using action Run Commands](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/run-command)

## IaC with PowerShell DSC Desired State Configuration

- [docs.microsoft.com: Desired State Configuration overview for decision makers 🌟](https://docs.microsoft.com/en-us/powershell/scripting/dsc/)
- [docs.microsoft.com: Using configuration data in DSC](https://docs.microsoft.com/en-us/powershell/scripting/dsc/configurations/configData)
- [octopus.com: Getting started with PowerShell Desired State Configuration (DSC)](https://octopus.com/blog/getting-started-with-powershell-dsc) PowerShell DSC is an Infrastructure as Code (IaC) technology that uses PowerShell to create Managed Object Format (MOF) files, which Windows Management Instrumentation (WMI) can use to configure a machine. In other words, PowerShell DSC uses PowerShell to programmatically configure your Windows-based computers. Additionally, DSC can monitor the state of the configured resources to make sure your machines stay consistent. Along with monitoring, DSC can also automatically correct the configuration of your system, so it’s always in the desired state. **PowerShell != PowerShell DSC**

## Azure Bicep

- [Bicep](https://github.com/Azure/bicep) Bicep is a Domain Specific Language (DSL) for deploying Azure resources declaratively.
- [github.com/johnlokerse/azure-bicep-cheat-sheet: Azure Bicep Cheat Sheet](https://github.com/johnlokerse/azure-bicep-cheat-sheet) Quick-reference guide on Azure Bicep 💪🏻
- [github.com/nnellans/bicep-guide](https://github.com/nnellans/bicep-guide)
- [faun.pub: From Terraform to Azure Bicep: What You Need to Know about syntax](https://faun.pub/from-terraform-to-azure-bicep-what-you-need-to-know-bb1c404b7603)
- [techcommunity.microsoft.com: How to install an AKS cluster with the Istio service mesh add-on via Bicep](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/how-to-install-an-aks-cluster-with-the-istio-service-mesh-add-on/ba-p/3802069)
- [techcommunity.microsoft.com: (Part-1) Leverage Bicep: Standard model to Automate Azure IaaS deployment](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/part-1-leverage-bicep-standard-model-to-automate-azure-iaas/ba-p/3804348)
- [blog.cloudtrooper.net: Deploy (Azure) Network-as-Code as a champ](https://blog.cloudtrooper.net/2023/06/08/deploy-azure-network-as-code-as-a-champ/)
- [learn.microsoft.com: Discover misconfigurations in Infrastructure as Code (IaC)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/iac-vulnerabilities)
- [insight-services-apac.github.io: Getting Started with Bicep](https://insight-services-apac.github.io/2023/12/04/getting-started-bicep)
- [build5nines.com: Get Started with Azure Bicep – Alternative to ARM Templates](https://build5nines.com/get-started-with-azure-bicep/)
- [linkedin.com/pulse: Exporting and importing variables between Bicep files: compileTimeImports | Freek Berson](https://www.linkedin.com/pulse/exporting-importing-variables-between-bicep-files-freek-berson-n0ske/)
- [luke.geek.nz: Using the Azure Naming Tool API to name your Bicep resources](https://luke.geek.nz/azure/azure-naming-tool-api-bicep-resources/)
- [microsoft.com: Revolutionizing our ARM template deployment at Microsoft with shift from JSON to BICEP](https://www.microsoft.com/insidetrack/blog/revolutionizing-our-arm-template-deployment-at-microsoft-with-shift-from-json-to-bicep/)
- [techcommunity.microsoft.com: Infra in Azure for Developers - The How (Part 2)](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/infra-in-azure-for-developers-the-how-part-2/ba-p/4046385)
- [johnlokerse.dev: Lint Azure Bicep templates in Azure DevOps](https://johnlokerse.dev/2024/02/05/lint-azure-bicep-templates-in-azure-devops/)
- [techcommunity.microsoft.com: Announcing public preview of Bicep templates support for Microsoft Graph](https://techcommunity.microsoft.com/t5/azure-governance-and-management/announcing-public-preview-of-bicep-templates-support-for/ba-p/4141772)
- [github.com/Azure-Samples/azure-ai-studio-secure-bicep](https://github.com/Azure-Samples/azure-ai-studio-secure-bicep) This repository contains a collection of Bicep modules designed to deploy a secure Azure AI Studio environment with robust network and identity security restrictions.
    - [Deploy Secure Azure AI Studio with a managed virtual network](https://github.com/Azure-Samples/azure-ai-studio-secure-bicep/blob/main/bicep/managedvnet/README.md)

## Azure Verified Modules

- [==azure.github.io/Azure-Verified-Modules 🌟==](https://azure.github.io/Azure-Verified-Modules/) Azure Verified Modules (AVM) is an initiative to consolidate and set the standards for what a good Infrastructure-as-Code module looks like. Modules will then align to these standards, across languages (Bicep, Terraform etc.) and will then be classified as AVMs and available from their respective language specific registries.
- [youtube: Code To Cloud - Getting Started With: Azure Verified Modules](https://www.youtube.com/watch?v=y1lOKQOapTw)
- [learn.microsoft.com: Introduction to using Azure Verified Modules for Terraform](https://learn.microsoft.com/en-us/samples/azure-samples/avm-terraform-labs/avm-terraform-labs/) - [github.com/azure-samples/avm-terraform-labs](https://github.com/azure-samples/avm-terraform-labs/)

## Azure Cross region Load Balancer

- [==azure.microsoft.com: How Microsoft Azure Cross-region Load Balancer helps create region redundancy and low latency== 🌟](https://azure.microsoft.com/en-in/blog/how-microsoft-azure-crossregion-load-balancer-helps-create-region-redundancy-and-low-latency/)

## Azure Traffic Manager

- [Azure Traffic Manager](https://docs.microsoft.com/azure/traffic-manager/)

## Azure DNS

- [learn.microsoft.com: What is Azure DNS Private Resolver?](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview) Azure DNS Private Resolver is a new service that enables you to query Azure DNS private zones from an on-premises environment and vice versa without deploying VM based DNS servers. Customers will no longer need to provision IaaS based solutions on their Virtual Networks to resolve names registered on Azure Private DNS Zones and will be able to do conditional forwarding of domains back to on-prem, multi-cloud and public DNS servers.
- [aidanfinn.com: Script – Document All Azure Private DNS Zones](https://aidanfinn.com/?p=23582) This post contains a script that will find all Azure Private DNS Zones in a tenant and export information on screen and as markdown in a file.
- [techcommunity.microsoft.com: Centralized private resolver architecture implementation using Azure private DNS resolver](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/centralized-private-resolver-architecture-implementation-using/ba-p/4132622)

## Azure OpenVPN

- [Create an Azure Active Directory tenant for P2S OpenVPN protocol connections](https://docs.microsoft.com/azure/vpn-gateway/openvpn-azure-ad-tenant)

## Azure Security

- [techcommunity.microsoft.com: Security Control: Implement security best practices](https://techcommunity.microsoft.com/t5/azure-security-center/security-control-implement-security-best-practices/ba-p/2269914)
- [==github.com/Cloud-Architekt: Azure AD - Attack and Defense Playbook==](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) **This publication is a collection of various common attack scenarios on Azure Active Directory and how they can be mitigated or detected.**
- [==devops.com: DevSecOps in Azure==](https://devops.com/devsecops-in-azure/)
- [learn.microsoft.com: SC-100: Design a Zero Trust strategy and architecture](https://learn.microsoft.com/en-us/training/paths/sc-100-design-zero-trust-strategy-architecture/)
    - https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect
- [learn.microsoft.com: Azure network security overview](https://learn.microsoft.com/en-us/azure/security/fundamentals/network-overview)
- [learn.microsoft.com: Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [learn.microsoft.com: Conditional Access architecture and personas](https://learn.microsoft.com/en-us/azure/architecture/guide/security/conditional-access-architecture)

### Azure Microsoft Defender for Cloud

- [github.com/Azure/Microsoft-Defender-for-Cloud](https://github.com/Azure/Microsoft-Defender-for-Cloud/tree/main/Workbooks/Network%20Security%20Dashboard) Network Security Dashboard for Microsoft Defender for Cloud
- [techcommunity.microsoft.com: Microsoft Announces General Availability of Defender for APIs](https://techcommunity.microsoft.com/t5/microsoft-defender-for-cloud/microsoft-announces-general-availability-of-defender-for-apis/ba-p/3981488)
- [techcommunity.microsoft.com: What’s new in Defender: How Copilot for Security can transform your SOC](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/what-s-new-in-defender-how-copilot-for-security-can-transform/ba-p/4084222)

### Microsoft Sentinel

- [techcommunity.microsoft.com: Monitoring Microsoft Sentinel Reports with Dashboard Hub & Power BI](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/monitoring-microsoft-sentinel-reports-with-dashboard-hub-amp/ba-p/4203870)

## Microsoft Copilot for Azure

- [build5nines.com: Introducing Microsoft Copilot for Azure](https://build5nines.com/introducing-microsoft-copilot-for-azure/)

## Azure Virtual WAN. vWAN

- [Azure Virtual WAN introduces its first SaaS offering](https://azure.microsoft.com/en-us/blog/azure-virtual-wan-introduces-its-first-saas-offering/)

## Azure Fleet

- [github.com/azure/fleet](https://github.com/azure/fleet) Multi-cluster core

## Data Ingestion. Azure Data Factory

- [==medium.com/codex: 7 Best Practices for Data Ingestion==](https://medium.com/codex/7-best-practices-for-data-ingestion-f336c6b5128c)
    - Data engineering is the practice of designing and building systems for collecting, storing, and analyzing data at scale.
    - Data Ingestion is defined as the process of absorbing data from a vast multitude of sources, and then transferring it to a target site where it can be analyzed and deposited.
    - A Data Engineer spends more than 50% of his time writing different pipelines that move data from one place to another. There are two basic frameworks to achieve the same:
        - ETL: Extract — Transform — Load
        - ELT: Extract — Load — Transform
    - However, in both the frameworks the common element is to be able to extract the data and load it into another destination. This is Data Ingestion.
    - On a broad categorization, there are mainly 3 types of Data Ingestion:
        - Batch-based Data Ingestion: Batch-based ingestion happens at a regularly scheduled time. The data is ingested in batches. This is important when a business needs to monitor daily reports, ex: sales reports for different stores. This is the most commonly used data ingestion use case.
        - Real-time/Streaming Data Ingestion:
            - The process of gathering and transmitting data from source systems in real-time solutions such as Change Data Capture (CDC) is known as Real-Time Data Ingestion.
            - CDC or Streaming Data captures any changes, new transactions, or rollback in real time and moves changed data to the destination, without impacting the database workload.
            - Real-Time Ingestion is critical in areas like power grid monitoring, operational analytics, stock market analytics, dynamic pricing in airlines, and recommendation engines.
        - Lambda-based Data Ingestion Architecture: Lambda architecture in Data ingestion tries to use the best practices of both batch and real-time ingestion.
            - Batch Layer: Computes the data based on the whole picture. This is more accurate however is slower to compute.
            - Speed Layer: Is used for real-time ingestion, the computed data might not be completely accurate, however, gives a real-time picture of the data.
            - Serving layer: The outputs from the batch layer in the form of batch views and those coming from the speed layer in the form of near real-time views get forwarded to the serving. This layer indexes the batch views so that they can be queried in low latency on an ad-hoc basis.
- [mssqltips.com: Choosing Between SQL Server Integration Services and Azure Data Factory](https://www.mssqltips.com/sqlservertip/7094/azure-data-factory-vs-ssis-similarities-differences/)
- [techcommunity.microsoft.com: Azure Data Factory: How to split a file into multiple output files with Bicep](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/azure-data-factory-how-to-split-a-file-into-multiple-output/ba-p/4039825)

## WinGet Windows Package Manager CLI

- [WinGet: Welcome to the Windows Package Manager Client (aka winget.exe) repository](https://github.com/microsoft/winget-cli/) Windows Package Manager CLI (aka winget)
- [muycomputer.com: WinGet 1.0, ya está aquí el administrador de paquetes para Windows](https://www.muycomputer.com/2021/06/03/winget-1-0-paquetes-windows-10/)
- [thomasmaurer.ch: Getting started with Windows Package Manager WinGet](https://www.thomasmaurer.ch/2021/07/getting-started-with-windows-package-manager-winget/)

## Windows 11

- [thenewstack.io: This Week in Programming: Windows Opens Up to Android Developers](https://thenewstack.io/this-week-in-programming-windows-opens-up-to-android-developers/)

## Azure API Management

- [azure.microsoft.com: Azure API Management](https://azure.microsoft.com/en-us/services/api-management)
- [jmfloreszazo.com: Monetizar un API, con Azure API Management](https://jmfloreszazo.com/monetizar-un-api-con-azure-api-management/)
- [github.com/Azure-Samples/api-management-workspaces-migration: Azure API Management workspaces migration tool](https://github.com/Azure-Samples/api-management-workspaces-migration) Tooling to ease migration of Azure API Management service-level resources to workspaces.

## Azure Container Apps

- [Azure Container Apps](https://azure.microsoft.com/services/container-apps/) Build and deploy modern apps and microservices using serverless containers
- [techcommunity.microsoft.com: Introducing Azure Container Apps: a serverless container service for running modern apps at scale](https://techcommunity.microsoft.com/t5/apps-on-azure/introducing-azure-container-apps-a-serverless-container-service/ba-p/2867265)
- [techcommunity.microsoft.com: Azure Policy for Azure Container Apps? Yes, please](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/azure-policy-for-azure-container-apps-yes-please/ba-p/3775200)
- [denniszielke.medium.com: Using Azure Container Apps at scale instead of your building your own NaaS on top of K8s?](https://denniszielke.medium.com/using-azure-container-apps-at-scale-instead-of-your-building-your-own-naas-on-top-of-k8s-7c4760c2511f)

## Azure Container Instances

- [azure.microsoft.com: Azure Container Instances](https://azure.microsoft.com/en-us/services/container-instances/) Launch containers with hypervisor isolation
- [unit42.paloaltonetworks.com: Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances](https://unit42.paloaltonetworks.com/azure-container-instances/)
- [nedinthecloud.com: Using azure container instances for an azure dev ops self hosted agent](https://nedinthecloud.com/2024/04/15/using-azure-container-instances-for-an-azure-devops-self-hosted-agent/)

## Azure Container Storage

- [techcommunity.microsoft.com: Azure Container Storage in Public Preview](https://techcommunity.microsoft.com/t5/azure-storage-blog/azure-container-storage-in-public-preview/ba-p/3819246)

## Windows Server Container Host

- [thomasmaurer.ch: How to Install a Windows Server Container Host](https://www.thomasmaurer.ch/2020/06/how-to-install-a-windows-server-container-host/)

## Disaster Recovery

- [docs.microsoft.com: Using Policy with Azure Site Recovery](https://docs.microsoft.com/en-us/azure/site-recovery/azure-to-azure-how-to-enable-policy) Disaster Recovery with Azure Policy. Learn how to enable Policy Support to protect your VMs using Azure Site Recovery.

## Azure Samples (Boilerplates)

- [github.com/Azure-Samples 🌟](https://github.com/Azure-Samples) Microsoft Azure code samples and examples in .NET, Java, Python, Node.js, PHP and Ruby
    - [Azure-Samples/azure-pipelines-variable-templates](https://github.com/Azure-Samples/azure-pipelines-variable-templates) This sample Python Web app demonstrates the use of variable template files in Azure Pipelines.
    - [Azure-Samples/jmeter-aci-terraform](https://github.com/Azure-Samples/jmeter-aci-terraform) Scalable cloud load/stress testing pipeline solution with Apache JMeter and Terraform to dynamically provision and destroy the required infrastructure on Azure.
    - [Azure-Samples/azure-pipelines-remote-tasks](https://github.com/Azure-Samples/azure-pipelines-remote-tasks)
    - [Azure-Samples/jenkins-terraform-azure-example](https://github.com/Azure-Samples/jenkins-terraform-azure-example)
    - etc
- [github.com/azure-devops](https://github.com/azure-devops)
- [Azure Quickstart Templates 🌟](https://azure.microsoft.com/en-us/resources/templates/) Deploy Azure resources through the Azure Resource Manager with community contributed templates to get more done. Deploy, learn, fork and contribute back.
    - https://github.com/Azure/azure-quickstart-templates
- [microsoft/azure-pipelines-yaml: Azure Pipelines YAML 🌟](https://github.com/microsoft/azure-pipelines-yaml/) YAML templates, samples, and community interaction for designing Azure Pipelines.
    - [microsoft/azure-pipelines-yaml: maven.yml](https://github.com/microsoft/azure-pipelines-yaml/blob/master/templates/maven.yml)

## Azure Healthcare Data Services

- [Microsoft - DICOM Service](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/)
    - [github.com/microsoft/dicom-server](https://github.com/microsoft/dicom-server) OSS Implementation of DICOMweb standard
    - [github.com/microsoft/fhir-server](https://github.com/microsoft/fhir-server) A service that implements the FHIR standard
- [Project InnerEye – Democratizing Medical Imaging AI](https://www.microsoft.com/en-us/research/project/medical-image-analysis/)
    - [github.com/microsoft/InnerEye-Gateway](https://github.com/microsoft/InnerEye-Gateway) The InnerEye-Gateway is a Windows service that acts as a DICOM end point to run inference on https://github.com/microsoft/InnerEye-DeepLearning models.
- [microsoft.com: Biomedical Research Platform Terra Now Available on Microsoft Azure](https://www.microsoft.com/en-us/research/blog/biomedical-research-platform-terra-now-available-on-microsoft-azure/)

## Office 365

- [o365reports.com: Office 365 Reports](https://o365reports.com)

## Azure Books

- [==azure.microsoft.com: Azure for Architects, Third Edition==](https://azure.microsoft.com/en-us/resources/azure-for-architects/)
- [dev.to/javinpaul: 7 Free Courses to Learn Microsoft Azure Cloud Platform](https://dev.to/javinpaul/7-free-courses-to-learn-microsoft-azure-cloud-platform-bg4)
- [github.com/PacktPublishing/The-Azure-Cloud-Native-Architecture-Mapbook](https://github.com/PacktPublishing/The-Azure-Cloud-Native-Architecture-Mapbook)

## Azure OpenAI

- [infoworld.com: Getting started with Azure OpenAI](https://www.infoworld.com/article/3686694/getting-started-with-azure-openai.html) Microsoft’s Azure-hosted OpenAI language models are now generally available, and it’s surprisingly simple to use them in your code.
- [jamiemaguire.net: First Look: Azure Open AI Studio, Prompt Engineering. What You Can Do and How](https://jamiemaguire.net/index.php/2023/04/22/first-look-azure-open-ai-studio-prompt-engineering-what-you-can-do-and-how/)
- [==techcommunity.microsoft.com: The AI Study Guide: Azure’s top free resources for learning generative AI in 2024==](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/the-ai-study-guide-azure-s-top-free-resources-for-learning/ba-p/4036890)
- [==hashicorp.com: Build secure AI applications on Azure with HashiCorp Terraform and Vault==](https://www.hashicorp.com/blog/build-secure-ai-applications-on-azure-with-hashicorp-terraform-and-vault)
- [techcommunity.microsoft.com: Azure OpenAI Landing Zone reference architecture](https://techcommunity.microsoft.com/t5/azure-architecture-blog/azure-openai-landing-zone-reference-architecture/ba-p/3882102)

## Windows Tools

- [Scoop: A command-line installer for windows](https://scoop.sh)
- [github.com/JPCERTCC/LogonTracer](https://github.com/JPCERTCC/LogonTracer) Investigate malicious Windows logon by visualizing and analyzing Windows event log

## Azure Tools

- [github.com/mspnp/AzureNamingTool - Azure Naming Tool 🌟](https://github.com/mspnp/AzureNamingTool) The Azure Naming Tool is a .NET 8 Blazor application, with a RESTful API. The UI consists of several pages to allow the configuration and generation of Azure Resource names. The API provides a programmatic interface for the functionality.
- [github.com/JulianHayward/AzADServicePrincipalInsights](https://github.com/JulianHayward/AzADServicePrincipalInsights) Insights and change tracking on Azure Active Directory Service Principals (Enterprise Applications and Applications)
- [==github.com/ElanShudnow/AzureCode==](https://github.com/ElanShudnow/AzureCode) A place to share all the Azure Code I am writing. This includes PowerShell, Terraform, ARM, Bicep, Ansible, etc...
    - [github.com/ElanShudnow/AzureCode/tree/main/PowerShell/AzResourceMoveSupport](https://github.com/ElanShudnow/AzureCode/tree/main/PowerShell/AzResourceMoveSupport) This script will take an Azure Usage Report csv file and provide new columns as to whether each resource supports migration to another Resource Group, to another Subscription, or to another Region.
- [github.com/mustafakaya/Azure-Reliability-Checker-Tool](https://github.com/mustafakaya/Azure-Reliability-Checker-Tool) This project contains a PowerShell script that scans Azure resources based on Azure Proactive Resiliency Library. The script clones the library to a local directory and then scans all folders and files and runs KQL queries. Finally, it exports the resources to a CSV file with recommendation ID, subscription ID, and resource ID.
- [github.com/microsoft/finops-toolkit](https://github.com/microsoft/finops-toolkit) Starter kits, scripts, and advanced solutions to accelerate your FinOps journey in the Microsoft Cloud.
- [github.com/BrianCollet/onboard-automator](https://github.com/BrianCollet/onboard-automator) Streamline and automate the onboarding process for new employees using Azure Logic Apps, Azure Function Apps, Azure Blob Storage, Azure Resource Manager, Azure Active Directory, and Outlook
- [github.com/nicolgit/azure-firewall-mon: az-firewall-mon](https://github.com/nicolgit/azure-firewall-mon) A near-real-time Azure Firewall Monitor log viewer

## Images

??? note "Click to expand!"

    <center>
    [![pizza model](images/pizza-model-vert.jpeg)](https://www.catapultsystems.com/blogs/introducing-the-third-of-three-microsoft-clouds-azure/)
    </center>

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/53-Y_aI0KpE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/rC1TV0_sIrM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/4BibQ69MD8c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </center>

## Tweets

??? note "Click to expand!"

    <center>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Cloud Networking concepts you need to know before getting into being a good architect<br><br>⏬Here are the useful link 🧰<br><br>Thread🧵👇</p>&mdash; Satyen Kumar (@SatyenKumar) <a href="https://twitter.com/SatyenKumar/status/1502358421865177088?ref_src=twsrc%5Etfw">March 11, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">PowerShell cheatsheet<a href="https://twitter.com/hashtag/devops?src=hash&amp;ref_src=twsrc%5Etfw">#devops</a> <a href="https://twitter.com/hashtag/devsecops?src=hash&amp;ref_src=twsrc%5Etfw">#devsecops</a> <a href="https://twitter.com/hashtag/kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#kubernetes</a> <a href="https://twitter.com/hashtag/cicd?src=hash&amp;ref_src=twsrc%5Etfw">#cicd</a> <a href="https://twitter.com/hashtag/k8s?src=hash&amp;ref_src=twsrc%5Etfw">#k8s</a> <a href="https://twitter.com/hashtag/linux?src=hash&amp;ref_src=twsrc%5Etfw">#linux</a> <a href="https://twitter.com/hashtag/docker?src=hash&amp;ref_src=twsrc%5Etfw">#docker</a> <a href="https://twitter.com/hashtag/sysadmin?src=hash&amp;ref_src=twsrc%5Etfw">#sysadmin</a> <a href="https://twitter.com/hashtag/automation?src=hash&amp;ref_src=twsrc%5Etfw">#automation</a> <a href="https://twitter.com/hashtag/technology?src=hash&amp;ref_src=twsrc%5Etfw">#technology</a> <a href="https://twitter.com/hashtag/cloudcomputing?src=hash&amp;ref_src=twsrc%5Etfw">#cloudcomputing</a> <a href="https://twitter.com/hashtag/serverless?src=hash&amp;ref_src=twsrc%5Etfw">#serverless</a> <a href="https://twitter.com/hashtag/windows?src=hash&amp;ref_src=twsrc%5Etfw">#windows</a> <a href="https://twitter.com/hashtag/powershell?src=hash&amp;ref_src=twsrc%5Etfw">#powershell</a> <a href="https://t.co/zljv4ikFp3">pic.twitter.com/zljv4ikFp3</a></p>&mdash; Valdemar (@heyValdemar) <a href="https://twitter.com/heyValdemar/status/1541461515802480641?ref_src=twsrc%5Etfw">June 27, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Are you looking to start a career in AI using Microsoft Azure? <br><br>Here are some of the best Azure services to learn:</p>&mdash; Simon (@simonholdorf) <a href="https://twitter.com/simonholdorf/status/1626147296630001667?ref_src=twsrc%5Etfw">February 16, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>
