# Microsoft Azure
- [Azure](#azure)
- [Azure DevOps](#azure-devops)
- [Azure Bicep](#azure-bicep)
- [AKS Azure Kubernetes Service](#aks-azure-kubernetes-service)
- [Azure Red Hat OpenShift ARO](#azure-red-hat-openshift-aro)
- [Azure Traffic Manager](#azure-traffic-manager)
- [Azure OpenVPN](#azure-openvpn)
- [Azure Security](#azure-security)

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
- [thomasmaurer.ch: Learn how to deploy and manage Azure resources with ARM templates](https://www.thomasmaurer.ch/2020/12/learn-how-to-deploy-and-manage-azure-resources-with-arm-templates/)
- [blog.sixeyed.com: You can't always have Kubernetes: running containers in Azure VM Scale Sets](https://blog.sixeyed.com/you-cant-always-have-kubernetes-running-containers-in-azure-vm-scale-sets/)
- [devblogs.microsoft.com: Deploy Spring Boot applications by leveraging enterprise best practices – Azure Spring Cloud Reference Architecture](https://devblogs.microsoft.com/java/deploy-spring-boot-applications-by-leveraging-enterprise-best-practices/)
- [Azure Key Vault to Kubernetes](https://github.com/SparebankenVest/azure-key-vault-to-kubernetes) Azure Key Vault to Kubernetes (akv2k8s for short) makes it simple and secure to use Azure Key Vault secrets, keys and certificates in Kubernetes.

## Azure DevOps
- [Azure DevOps 🌟](https://azure.microsoft.com/services/devops/)
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

## Azure Bicep
- [Bicep](https://github.com/Azure/bicep) Bicep is a Domain Specific Language (DSL) for deploying Azure resources declaratively. 

## AKS Azure Kubernetes Service 
- [trstringer.com: Run Kubernetes Pods on Specific VM Types in AKS](https://trstringer.com/run-kubernetes-pods-on-vm-types/)
- [docs.microsoft.com: AKS-managed Azure Active Directory integration](https://docs.microsoft.com/en-us/azure/aks/managed-aad)
- [build5nines.com: Terraform: Create an AKS Cluster 🌟](https://build5nines.com/terraform-create-an-aks-cluster/)
- [github.com: AKS: Use AAD identity for pods and make your SecOps happy](https://github.com/dfrappart/articles/blob/master/podidentityjourney.md)
- [docs.microsoft.com: Microservices architecture on Azure Kubernetes Service (AKS) 🌟](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices)
- [techcommunity.microsoft.com: Containerize and migrate applications to AKS with the Azure Migrate’s new App Containerization tool](https://techcommunity.microsoft.com/t5/azure-migration/containerize-and-migrate-applications-to-aks-with-the-azure/ba-p/2178551)
- [mehmetozkaya.medium.com: Deploying .Net Microservices to Azure Kubernetes Services(AKS) and Automating with Azure DevOps](https://mehmetozkaya.medium.com/deploying-net-microservices-to-azure-kubernetes-services-aks-and-automating-with-azure-devops-c50bdd51b702)
- [faun.pub: How to implement Azure Kubernetes Service (AKS) in Cloud?](https://faun.pub/azure-kubernetes-service-aks-d1e71c7ecbe6)
- [adamrushuk.github.io: Increasing the volumeClaimTemplates Disk Size in a Statefulset on AKS](https://adamrushuk.github.io/increasing-the-volumeclaimtemplates-disk-size-in-a-statefulset-on-aks/)
- [nillsf.com: Running Windows containers on the Azure Kubernetes Service (AKS)](https://nillsf.com/index.php/2020/11/17/running-windows-containers-on-the-azure-kubernetes-service-aks)
- [itnext.io: Running Your Microservices Securely on AKS](https://itnext.io/running-your-microservices-securely-on-aks-417a110b2e76)
- [docs.microsoft.com: Create an HTTPS ingress controller on Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/ingress-tls)
- [blog.nillsf.com: Customize core dump in Azure Kubernetes](https://blog.nillsf.com/index.php/2020/12/06/customize-core-dump-in-azure-kubernetes/)
- [medium: Secure your Microservices on AKS — Part 1 🌟](https://itnext.io/running-your-microservices-securely-on-aks-417a110b2e76)
    - [medium: Secure your Microservices on AKS — Part 2 🌟](https://medium.com/microsoftazure/secure-your-microservices-on-aks-part-2-5496bf2ba00c)
- [zartis.com: How To Save A Fortune On Azure Kubernetes Service](https://www.zartis.com/minimizing-costs-aks/)
- [itnext.io: AKS Performance: Limit Ranges](https://itnext.io/aks-performance-limit-ranges-8e18cbebe351) Limit Ranges can be used to fine tune your resource consumption by limiting your min/max requests/limits in namespaces.

## Azure Red Hat OpenShift ARO
- [ARO](https://www.openshift.com/products/azure-openshift)
- [aroworkshop.io 🌟](http://aroworkshop.io/) 

## Azure Traffic Manager
- [Azure Traffic Manager](https://docs.microsoft.com/azure/traffic-manager/)

## Azure OpenVPN
- [Create an Azure Active Directory tenant for P2S OpenVPN protocol connections](https://docs.microsoft.com/azure/vpn-gateway/openvpn-azure-ad-tenant)

## Azure Security
- [techcommunity.microsoft.com: Security Control: Implement security best practices](https://techcommunity.microsoft.com/t5/azure-security-center/security-control-implement-security-best-practices/ba-p/2269914)

<center>
[![pizza model](images/pizza-model-vert.jpeg)](https://www.catapultsystems.com/blogs/introducing-the-third-of-three-microsoft-clouds-azure/)
</center>