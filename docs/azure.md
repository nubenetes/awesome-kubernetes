# Microsoft Azure
- [Azure](#azure)
- [Understand Azure Load Balancing](#understand-azure-load-balancing)
- [Microsoft Linux Distribution CBL Mariner](#microsoft-linux-distribution-cbl-mariner)
- [Azure Patterns](#azure-patterns)
- [ARM Templates](#arm-templates)
- [Azure DevOps](#azure-devops)
- [Azure Arc. Azure’s Hybrid And Multi-Cloud Platform. GitOps with Azure Arc](#azure-arc-azures-hybrid-and-multi-cloud-platform-gitops-with-azure-arc)
- [Secure DevOps Kit for Azure](#secure-devops-kit-for-azure)
- [Mobile Apps](#mobile-apps)
- [Powershell](#powershell)
    - [Powershell repos](#powershell-repos)
    - [Crescendo powershell module](#crescendo-powershell-module)
- [Azure Run Command](#azure-run-command)
- [IaC with PowerShell DSC Desired State Configuration](#iac-with-powershell-dsc-desired-state-configuration)
- [Azure Bicep](#azure-bicep)
- [Azure Traffic Manager](#azure-traffic-manager)
- [Azure OpenVPN](#azure-openvpn)
- [Azure Security](#azure-security)
- [WinGet Windows Package Manager CLI](#winget-windows-package-manager-cli)
- [Windows 11](#windows-11)
- [Azure API Management](#azure-api-management)
- [Azure Container Apps](#azure-container-apps)
- [Azure Container Instances](#azure-container-instances)
- [Windows Server Container Host](#windows-server-container-host)
- [Azure Samples (Boilerplates)](#azure-samples-boilerplates)
- [Office 365](#office-365)
- [Images](#images)
- [Videos](#videos)

## Azure
- [Microsoft Azure](https://azure.microsoft.com/)
- [Microsoft Docs](https://docs.microsoft.com/)
- [Azure Docs](https://docs.microsoft.com/azure)
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
- [returngis.net: Acceder a un App Service con Private Endpoint desde otra Vnet](https://www.returngis.net/2021/08/acceder-a-un-app-service-con-private-endpoint-desde-otra-vnet/)
- [theregister.com: Microsoft Azure deprecations: API changes will break applications and PowerShell scripts](https://www.theregister.com/2021/09/03/microsoft_azure_deprecations_api_changes/)
- [k21academy.com: Azure RBAC Vs Azure Policies Vs Azure Blueprints](https://k21academy.com/microsoft-azure/azure-rbac-vs-azure-policies-vs-azure-blueprints/)
- [==blog.identitydigest.com: Azure AD workload identity federation with Kubernetes==](https://blog.identitydigest.com/azuread-federate-k8s/) Any k8s cluster, running on any platform, can now securely access Azure resources without keys or secrets through Azure AD Workload Identity Federation. 
- [thomasmaurer.ch: How to check the available VM Sizes (SKUs) by Azure Region](https://www.thomasmaurer.ch/2021/02/how-to-check-the-available-vm-sizes-skus-by-azure-region/)

## Understand Azure Load Balancing
- [docs.microsoft.com: Understand Azure Load Balancing. Decision tree for load balancing in Azure](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)
- [mvark.blogspot.com: Comparison of Azure Front Door, Traffic Manager, Application Gateway & Load Balancer](http://mvark.blogspot.com/2019/12/comparison-of-azure-front-door-traffic.html) 

## Microsoft Linux Distribution CBL Mariner
- [thenewstack.io: Deploying Microsoft’s New Linux Distribution as a VM is Not Easy](https://thenewstack.io/deploying-microsofts-new-linux-distribution-as-a-vm-is-not-easy/)
- [github.com/microsoft/CBL-Mariner](https://github.com/microsoft/CBL-Mariner) Linux OS for Azure 1P services and edge appliances

## Azure Patterns
- [==mattfeltonma/azure-networking-patterns==](https://github.com/mattfeltonma/azure-networking-patterns)
- [docs.microsoft.com: Cloud Design Patterns](https://docs.microsoft.com/en-us/azure/architecture/patterns/)

## ARM Templates
- [==azure.microsoft.com: Azure Quickstart Templates==](https://azure.microsoft.com/en-us/resources/templates/) Deploy Azure resources through the Azure Resource Manager with community contributed templates to get more done. Deploy, learn, fork and contribute back.
- [thomasmaurer.ch: Learn how to deploy and manage Azure resources with ARM templates](https://www.thomasmaurer.ch/2020/12/learn-how-to-deploy-and-manage-azure-resources-with-arm-templates/)
- [techcommunity.microsoft.com: ARM Template Specs now GA!](https://techcommunity.microsoft.com/t5/azure-governance-and-management/arm-template-specs-now-ga/ba-p/2402618)
- [docs.microsoft.com: Azure Resource Manager template specs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-specs)

## Azure DevOps
- [Azure DevOps 🌟](https://azure.microsoft.com/services/devops/)
- [Azure DevOps Labs 🌟](https://www.azuredevopslabs.com/)
- [info.acloud.guru: Deploying your first kubernetes app with Azure DevOps](https://info.acloud.guru/resources/deploy-kubernetes-app-with-azure-devops)
- [info.acloud.guru: Azure DevOps VS GitHub: Comparing Microsoft's DevOps Twins](https://info.acloud.guru/resources/azure-devops-vs-github-comparing-microsofts-devops-twins)
- [techcommunity.microsoft.com: Building a path to success for microservices and .NET Core - Project Tye + GitHub Actions](https://techcommunity.microsoft.com/t5/apps-on-azure/building-a-path-to-success-for-microservices-and-net-core/ba-p/1502270)
- [medium: Azure DevOps HandBook !](https://medium.com/@arunksingh16/azure-devops-handbook-d6dcd82da1b7)
- [Azure DevOps Tips: “Each” Loops](https://medium.com/@therealjordanlee/azure-devops-tips-each-loops-c082c692d025)
- [cloudskills.io: Getting Started with Git and Azure DevOps: The Ultimate Guide 🌟](https://cloudskills.io/blog/git-azure-devops)
- [zartis.com: Simplify Your SDLC with Azure DevOps](https://www.zartis.com/simplify-your-sdlc-with-azure-devops/)
- [azurebrains.com: Despliega tu Azure Function App con Terraform y Azure DevOps 🌟](https://www.azurebrains.com/2021/03/25/despliega-azure-function-terraform-azuredevops/)
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

## Azure Arc. Azure’s Hybrid And Multi-Cloud Platform. GitOps with Azure Arc 
- [Azure Arc overview](https://docs.microsoft.com/en-us/azure/azure-arc/overview) Alternative to Google Anthos or RHACM
- [azurearcjumpstart.io](https://azurearcjumpstart.io/) - [microsoft/azure_arc](https://github.com/microsoft/azure_arc)
    - [architecture diagrams and slides](https://github.com/microsoft/azure_arc/tree/main/docs/ppt)
- [techcommunity.microsoft.com: Standardize DevOps practices across hybrid and multicloud environments](https://techcommunity.microsoft.com/t5/itops-talk-blog/standardize-devops-practices-across-hybrid-and-multicloud/ba-p/2795010) With Azure Arc-enabled Kubernetes, you can attach and configure Kubernetes clusters located either inside or outside Azure.
- [youtube: How to run an App Service Web App on Azure Arc-enabled Kubernetes - Part 2 | Azure Tips and Tricks](https://www.youtube.com/watch?v=53-Y_aI0KpE&ab_channel=MicrosoftAzure)
- [docs.microsoft.com: CI/CD workflow using GitOps (Flux v2) - Azure Arc enabled Kubernetes](https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-gitops-flux2-ci-cd)

## Secure DevOps Kit for Azure
- [Secure DevOps Kit for Azure](https://github.com/azsk/DevOpsKit)
- [DevOpsKit-docs](https://github.com/azsk/DevOpsKit-docs)
- [ismiletechnologies.com: Secure DevOps Kit For Azure(AzSK)](https://www.ismiletechnologies.com/devsecops/secure-devops-kit-azureazsk/)

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

### Powershell repos
- [Abhisheksinhacoder/collection-of-useful-scripts](https://github.com/Abhisheksinhacoder/collection-of-useful-scripts)
- [jrussellfreelance/powershell-scripts](https://github.com/jrussellfreelance/powershell-scripts)
- [github.com/search?l=powershell](https://github.com/search?l=powershell&q=stars%3A%3E1&s=stars&type=Repositories)
- [systemcenterdudes.com: Create Operational SCCM Collection Using Powershell Script](https://systemcenterdudes.com/create-operational-sccm-collection-using-powershell-script/)
    - [prae1809/PowerShell-Scripts: OperationalCollections](https://github.com/prae1809/PowerShell-Scripts/tree/master/OperationalCollections) This script will create a set of 134 SCCM collections for your various needs. These collections can be used for operational tasks afterward.
    - [docs.microsoft.com: Introduction to Collections in Configuration Manager](https://docs.microsoft.com/en-us/previous-versions/system-center/system-center-2012-r2/gg682177(v=technet.10))

### Crescendo powershell module
- [Crescendo](https://devblogs.microsoft.com/powershell/announcing-powershell-crescendo-preview-1/) is an experimental module developed by Jim Truher, one of the main developers of PowerShell. Crescendo provides a framework to rapidly develop PowerShell cmdlets that wrap native commands, regardless of platform. The goal of a Crescendo-based module is to create PowerShell cmdlets that use a native command-line tool, but unlike the tool, return PowerShell objects instead of plain text.
- [devblogs.microsoft.com: My Crescendo journey](https://devblogs.microsoft.com/powershell-community/my-crescendo-journey/)

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

## Azure Traffic Manager
- [Azure Traffic Manager](https://docs.microsoft.com/azure/traffic-manager/)

## Azure OpenVPN
- [Create an Azure Active Directory tenant for P2S OpenVPN protocol connections](https://docs.microsoft.com/azure/vpn-gateway/openvpn-azure-ad-tenant)

## Azure Security
- [techcommunity.microsoft.com: Security Control: Implement security best practices](https://techcommunity.microsoft.com/t5/azure-security-center/security-control-implement-security-best-practices/ba-p/2269914)

## WinGet Windows Package Manager CLI
- [WinGet: Welcome to the Windows Package Manager Client (aka winget.exe) repository](https://github.com/microsoft/winget-cli/) Windows Package Manager CLI (aka winget)
- [muycomputer.com: WinGet 1.0, ya está aquí el administrador de paquetes para Windows](https://www.muycomputer.com/2021/06/03/winget-1-0-paquetes-windows-10/)
- [thomasmaurer.ch: Getting started with Windows Package Manager WinGet](https://www.thomasmaurer.ch/2021/07/getting-started-with-windows-package-manager-winget/)

## Windows 11
- [thenewstack.io: This Week in Programming: Windows Opens Up to Android Developers](https://thenewstack.io/this-week-in-programming-windows-opens-up-to-android-developers/)

## Azure API Management
- [azure.microsoft.com: Azure API Management](https://azure.microsoft.com/en-us/services/api-management)
- [jmfloreszazo.com: Monetizar un API, con Azure API Management](https://jmfloreszazo.com/monetizar-un-api-con-azure-api-management/)

## Azure Container Apps
- [Azure Container Apps](https://azure.microsoft.com/services/container-apps/) Build and deploy modern apps and microservices using serverless containers
- [techcommunity.microsoft.com: Introducing Azure Container Apps: a serverless container service for running modern apps at scale](https://techcommunity.microsoft.com/t5/apps-on-azure/introducing-azure-container-apps-a-serverless-container-service/ba-p/2867265)

## Azure Container Instances
- [azure.microsoft.com: Azure Container Instances](https://azure.microsoft.com/en-us/services/container-instances/) Launch containers with hypervisor isolation
- [unit42.paloaltonetworks.com: Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances](https://unit42.paloaltonetworks.com/azure-container-instances/)

## Windows Server Container Host
- [thomasmaurer.ch: How to Install a Windows Server Container Host](https://www.thomasmaurer.ch/2020/06/how-to-install-a-windows-server-container-host/)

## Azure Samples (Boilerplates)
- [github.com/Azure-Samples 🌟](https://github.com/Azure-Samples) Microsoft Azure code samples and examples in .NET, Java, Python, Node.js, PHP and Ruby
    - [Azure-Samples/azure-pipelines-variable-templates](https://github.com/Azure-Samples/azure-pipelines-variable-templates) This sample Python Web app demonstrates the use of variable template files in Azure Pipelines.
    - [Azure-Samples/jmeter-aci-terraform](https://github.com/Azure-Samples/jmeter-aci-terraform) Scalable cloud load/stress testing pipeline solution with Apache JMeter and Terraform to dynamically provision and destroy the required infrastructure on Azure.
    - [Azure-Samples/azure-pipelines-remote-tasks](https://github.com/Azure-Samples/azure-pipelines-remote-tasks)
    - [Azure-Samples/jenkins-terraform-azure-example](https://github.com/Azure-Samples/jenkins-terraform-azure-example)
    - etc

## Office 365
- [o365reports.com: Office 365 Reports](https://o365reports.com)

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
    </center>