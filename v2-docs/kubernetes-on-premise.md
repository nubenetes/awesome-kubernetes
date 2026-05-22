# Kubernetes On Premise

!!! info "Architectural Context"
    Detailed reference for Kubernetes On Premise in the context of The Container Stack.

## Cloud Infrastructure

### Application Platforms

#### VMware Tanzu Ecosystem

  - **(2022)** [zdnet.com: VMware brings Tanzu Application Platform into GA to ease Kubernetes adoption](https://www.zdnet.com/article/vmware-brings-tanzu-application-platform-into-ga-to-ease-kubernetes-adoption) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Documents the GA release of Tanzu Application Platform (TAP), which provides pre-configured templates to streamline code-to-production pipelines, automating cluster deployment steps and accelerating build compliance.
### Hardware Acceleration

#### VMware Tanzu Ecosystem (1)

  - **(2021)** [dev.to/saintdle: Deploying Nvidia GPU enabled Tanzu Kubernetes Clusters](https://dev.to/saintdle/deploying-nvidia-gpu-enabled-tanzu-kubernetes-clusters-40ma) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An in-depth guide detailing how to provision Nvidia GPU acceleration inside Tanzu Kubernetes Grid (TKG) guest clusters. Covers configuration of GPU operators, vSphere passthrough, and driver deployment parameters for intensive workload computing.
### Kubernetes Distributions

#### Bare-Metal and Edge

  - **(2026)** [**poseidon/typhoon**](https://github.com/poseidon/typhoon) <span class='md-tag md-tag--info'>⭐ 2042</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Typhoon is a bare-metal and multi-cloud Kubernetes distribution focused on simplicity. Built entirely with Terraform and running on Flatcar Container Linux, it provides a stable setup that operates efficiently without heavy proprietary layers.
#### Comparison

  - **(2021)** [acloudguru.com: Which Kubernetes distribution is right for you?](https://www.pluralsight.com/resources/blog/cloud/which-kubernetes-distribution-is-right-for-you) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A strategic comparison of various Kubernetes distributions across managed cloud services, enterprise-on-prem deployments, and lightweight edge environments. It outlines key trade-offs in administrative overhead, ecosystem compatibility, and operational costs to help organizations select the correct engine.
#### Custom Installers

  - **(2026)** [**kurl.sh**](https://kurl.sh) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An automated web-based tool from Replicated for creating custom Kubernetes installers. It generates a single shell script containing your chosen mix of Kubernetes core packages, CNI layers, and custom operators, designed for offline and air-gapped environments.
#### Edge and IoT

  - **(2026)** [==k0s==](https://k0sproject.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — k0s is a zero-friction, highly secure Kubernetes distribution compiled into a single static binary. It separates the control plane from node processes, reducing operational overhead and memory usage, making it an excellent match for edge, bare metal, and embedded systems.
  - **(2026)** [**K0s - Zero Friction Kubernetes**](https://github.com/k0sproject/k0s) <span class='md-tag md-tag--info'>⭐ 6161</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The main GitHub repository for k0s, the lightweight zero-overhead Kubernetes distribution. It includes active developer paths, and provides built-in components like Calico CNI, Kube-router, and support for running multiple control planes.
  - **(2022)** [xiaods/k8e](https://github.com/xiaods/k8e) <span class='md-tag md-tag--info'>⭐ 444</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight community-driven Kubernetes distribution modeled after K3s but using standard upstream components. It offers an easy install track for edge nodes and test networks looking for low operational footprints.
#### Enterprise Platforms

  - **(2022)** [infoworld.com: 6 Kubernetes distributions leading the container revolution](https://www.infoworld.com/article/2266054/6-kubernetes-distributions-leading-the-container-revolution.html) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Reviews the leading container platforms guiding the market shift towards hybrid and multi-cloud Kubernetes orchestration. Evaluates enterprise-grade capabilities of tools like Red Hat OpenShift, VMware Tanzu, Rancher, and Mirantis, analyzing their management interfaces and security controls.
#### Industry News

  - **(2020)** [infoq.com: Mirantis Announces k0s, a New Kubernetes Distribution](https://www.infoq.com/news/2020/12/k0s-kubernetes-distribution) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry report covering Mirantis' launch of k0s. Details the project's architecture, showing how it solves common challenges like packaging components cleanly, maintaining small binary sizes, and removing reliance on complex OS libraries.
### Training Platforms

#### Ecosystem Portals

  - **(2020)** [kube.academy/pro 🌟](https://kube.academy/pro) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An interactive curriculum platform for Kubernetes engineers. Includes tracks covering cluster diagnostics, policy configuration, service mesh integrations, and overall infrastructure hardening strategies.
#### Sandbox Environments

  - **(2026)** [VMware hands-on Labs 🌟](https://labs.hol.vmware.com/HOL) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A premium sandbox platform allowing cloud engineers and enterprise architects to test VMware Tanzu and vSphere configurations without local hardware limitations. Includes pre-configured networks, clusters, and detailed training modules.
### VMware Tanzu Ecosystem (2)

#### Hypervisor Kubernetes

  - **(2020)** [**VMware vSphere 7 with Kubernetes** - Project Pacific](https://www.vmware.com/products/cloud-infrastructure/vsphere) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Official product landing for VMware vSphere's container execution engine, which allows traditional virtual machine management tools to deploy and monitor container runtimes. Provides a centralized solution to govern both VM and container topologies.
  - **(2019)** [blogs.vmware.com: Introducing Project Pacific (vSphere with Kubernetes)](https://blogs.vmware.com/vsphere/2019/08/introducing-project-pacific.html) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — The original deep-dive announcement introducing Project Pacific, which natively refactored VMware vSphere 7 around the Kubernetes control plane. Provided the architectural bridge that enables operations teams to provision containerized infrastructure via ESXi hypervisors.
#### Tutorials

  - **(2020)** [cormachogan.com: A first look at vSphere with Kubernetes in action](https://cormachogan.com/2020/04/01/a-first-look-at-vsphere-with-kubernetes-in-action) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed technical review showing vSphere with Kubernetes in a live environment. Reviews how the Supervisor Cluster exposes Kubernetes native primitives natively within vCenter, allowing developers to consume storage and compute via standard YAML.
  - **(2020)** [cormachogan.com: Building a TKG Cluster in vSphere with Kubernetes](https://cormachogan.com/2020/04/07/building-a-tkg-guest-cluster-in-vsphere-with-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical walk-through detailing how to construct and deploy a Tanzu Kubernetes Grid (TKG) guest cluster. Covers configuration details including Cluster API controllers, control-plane load balancers, and persistent virtual storage.
## Database

### Cloud-Native Databases

#### VMware Tanzu Ecosystem (3)

  - **(2020)** [tanzu.vmware.com: VMware Tanzu SQL: MySQL at Scale Made Easy for Kubernetes](https://tanzu.vmware.com/content/blog/vmware-tanzu-sql-mysql-at-scale-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Highlights VMware Tanzu SQL, an automated relational database engine managed natively within Kubernetes clusters. Outlines automated operations including point-in-time recovery, seamless scaling, high-availability setups, and security patching.
## Infrastructure

### Air-Gapped

#### Delivery and Curation

  - **(2026)** [**defenseunicorns/zarf**](https://github.com/zarf-dev/zarf) <span class='md-tag md-tag--info'>⭐ 1896</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly resilient open-source developer tool from Defense Unicorns built to package, deploy, and manage continuous delivery of cloud-native platforms in strictly air-gapped or secure zero-trust environments. Automates the bundling of containers, Helm charts, files, and static configs into single, self-sufficient, and cryptographically signed archive files.
### Bare Metal

#### Architecture

  - **(2022)** [containerjournal.com: Deploying Kubernetes on Bare Metal](https://cloudnativenow.com/features/deploying-kubernetes-on-bare-metal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural guide exploring the benefits and challenges of deploying production-grade Kubernetes directly onto bare-metal servers. It details how bypassing hypervisor virtualization layers reduces operational overhead and enhances I/O performance. Crucial for low-latency, high-throughput edge nodes and data-intensive database deployments.
#### Case Studies

  - **(2020)** [linecorp.com: Building Large Kubernetes Clusters with **Caravan**](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed engineering case study by Line Corporation explaining Caravan, their custom internal platform designed to build and maintain thousands of Kubernetes clusters on bare-metal infrastructure. Provides deep insights into enterprise lifecycle scale and custom provisioning control planes.
#### Strategic Decisions

  - **(2021)** [containerjournal.com: When Kubernetes-as-a-Service Doesn’t Cut It](https://cloudnativenow.com/features/when-kubernetes-as-a-service-doesnt-cut-it) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A strategic critique detailing scenarios where managed cloud Kubernetes services fall short of enterprise requirements, necessitating custom bare-metal or on-premises solutions. Key factors analyzed include strict regulatory compliance, low-latency requirements, and specialized hardware acceleration (GPUs, TPUs). Useful for infrastructure architects designing hybrid-cloud topologies.
### Bare Metal vs VMs

#### Architectural Decisions

  - **(2021)** [thenewstack.io: Kubernetes on Bare Metal vs. VMs: It’s Not Just Performance](https://thenewstack.io/kubernetes-on-bare-metal-vs-vms-its-not-just-performance)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comparative technical analysis evaluating the operational trade-offs between deploying Kubernetes on bare metal versus traditional virtual machines. While bare metal minimizes CPU/memory virtualization tax, VMs offer stronger isolation, easier live migration, and mature lifecycle management APIs. The article guides decision-makers in balancing pure hardware efficiency against administrative convenience.
### Cluster API

#### Architecture (1)

  - **(2019)** [thenewstack.io: Cluster API Offers a Way to Manage Multiple Kubernetes Deployments](https://thenewstack.io/cluster-api-offers-a-way-to-manage-multiple-kubernetes-deployments)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analysis of the early design goals of Cluster API. It outlines the architectural advantages of treating clusters as managed custom resources within a Kubernetes management cluster, establishing unified fleet control plane patterns.
#### ArgoCD

  - **(2021)** [piotrminkowski.com: Create and Manage Kubernetes Clusters with Cluster API and ArgoCD](https://piotrminkowski.com/2021/12/03/create-kubernetes-clusters-with-cluster-api-and-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An excellent tutorial detailing how to build a unified GitOps pipeline for cluster provisioning by combining Cluster API and ArgoCD. Shows how to store cluster manifests in a git repository and let ArgoCD reconcile cluster infrastructure as standard Kubernetes apps.
#### Bare Metal (1)

  - **(2021)** [thenewstack.io: Provision Bare-Metal Kubernetes with the Cluster API](https://thenewstack.io/provision-bare-metal-kubernetes-with-the-cluster-api) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates the mechanics of using Cluster API providers (such as Metal3) to provision bare-metal hardware declaratively. Details the transformation of raw physical bare metal nodes into standard, managed Kubernetes control-planes and workers.
#### Declarative Management

  - **(2026)** [==ClusterAPI==](https://cluster-api.sigs.k8s.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Kubernetes Special Interest Group (SIG) project extending Kubernetes with declarative, Kubernetes-style APIs to manage the lifecycle of Kubernetes clusters. It implements custom resources (e.g., Clusters, Machines) and controllers across numerous cloud providers, introducing standard Infrastructure-as-Code paradigms to cluster fleet administration.
#### GitOps

  - **(2021)** [weave.works: Manage Thousands of Clusters with GitOps and the Cluster API](https://ambking1234.biz/?action=register&marketingRef=6788b227da9499f55f6ea745/blog/manage-thousands-of-clusters-with-gitops-and-the-cluster-api) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Historical reference documenting the intersection of GitOps deployment paradigms and Cluster API (CAPI) for planetary-scale multi-cluster environments. Note: Original domain has redirected to an registration portal, reflecting legacy status.
#### Helm

  - **(2021)** [github.com: Cluster API Helm Chart](https://github.com/kgamanji/cluster-api-helm-chart) <span class='md-tag md-tag--info'>⭐ 58</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A community Helm chart designed to packages and deploy Cluster API resources and operators easily inside a management cluster. Simplifies the installation of CAPI components via standard Helm deployment pipelines. Note: Inactive, as official tooling increasingly uses clusterctl.
#### Legacy Provider

  - **(2021)** [weaveworks/cluster-api-provider-existinginfra](https://github.com/weaveworks/cluster-api-provider-existinginfra) <span class='md-tag md-tag--info'>⭐ 45</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A Cluster API provider designed to enable cluster deployment over pre-existing infra (such as bare-metal or legacy VMs) via SSH. Archived following Weaveworks' wrap-up, serving now as a reference for custom SSH-based control loops.
#### Multi-Cloud

  - **(2020)** [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural guide walking through the declarative provisioning of multi-cloud cluster setups using Cluster API (CAPI). Explores bootstrap providers, control-plane management, and target cluster life cycle configurations across AWS and Azure environments.
### Cluster Provisioning

#### AWS

  - **(2022)** [Kubernetes The Hard Way: AWS Edition](https://github.com/prabhatsharma/kubernetes-the-hard-way-aws) <span class='md-tag md-tag--info'>⭐ 668</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly specific community adaptation of Kelsey Hightower's educational guide, focusing entirely on AWS infrastructure including VPCs, IAM roles, security groups, and EC2 provisioning. Valuable reference for understanding low-level networking and control plane setup on AWS.
#### Automation

  - **(2024)** [krd](https://github.com/electrocucaracha/krd) <span class='md-tag md-tag--info'>⭐ 40</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubernetes Reference Deployment (KRD) utilizes Ansible playbooks and shell scripts to automate the installation of multi-node Kubernetes clusters with extensive integration of Cloud Native network elements, virtualization engines, and storage provisioners. Designed for prototyping comprehensive environments rapidly.
#### Automation Tools

  - **(2021)** [**k8s-tew**](https://github.com/darxkies/k8s-tew) <span class='md-tag md-tag--info'>⭐ 311</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubernetes The Easy Way (k8s-tew) provides a collection of wrapper scripts and declarative configuration structures designed to ease the bootstrap complexities of kubeadm. Inactive, replaced by more mature standard declarative APIs.
#### Azure

  - **(2020)** [Kubernetes the Hard Way: Azure Edition](https://github.com/carlosonunez/kubernetes-the-hard-way-on-azure) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An adapted tutorial of Kelsey Hightower's 'Kubernetes the Hard Way' mapped directly onto Azure cloud infrastructure. Details setting up VNets, Azure NSGs, load balancers, and virtual machine scale sets manually to better understand control plane placement.
#### Community Videos

  - **(2021)** [youtube: OpenShift Commons En Vivo - KubeInit con Maria Bracho, Scott McCarty, and Carlos Camacho (Red Hat, Spanish) 🌟](https://www.youtube.com/watch?v=9_6H7Ahsdm4&ab_channel=OpenShift) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video presentation exploring KubeInit, its architecture, and practical use cases for bootstrapping cloud-native platforms like OpenShift and Kubernetes on local hardware. Conducted in Spanish with Red Hat experts. [SPANISH CONTENT]
#### Containerd

  - **(2021)** [thenewstack.io: How to Deploy Kubernetes with Kubeadm and containerd](https://thenewstack.io/how-to-deploy-kubernetes-with-kubeadm-and-containerd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the modern approach to cluster provisioning by leveraging the containerd CRI runtime directly with kubeadm. Explains how to drop docker-shim and configure systemic dependencies, systemd cgroup drivers, and network configurations for maximum efficiency.
#### Developer Environments

  - **(2024)** [github.com/bluxmit: Kubespray Workspace](https://github.com/bluxmit/alnoda-workspaces) <span class='md-tag md-tag--info'>⭐ 1362</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized development workspace designed to streamline the execution of Kubespray and Ansible operations. It bundles critical tools, CLI utilities, and playbooks in a containerized sandbox to prevent local dependency conflicts during large-scale cluster provisioning.
#### Education

  - **(2026)** [==**Kelsey Hightower: kubernetes the hard way**==](https://github.com/kelseyhightower/kubernetes-the-hard-way) <span class='md-tag md-tag--info'>⭐ 48360</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The legendary, standard-setting educational guide for bootstrap-configuring high-availability Kubernetes clusters without installers. Details direct certificate generation, control plane components installation, systemd configuration, and CNI initialization. Crucial for establishing a deeply technical foundation of internal cluster mechanics.
#### Kops

  - **(2026)** [==GitHub: Kubernetes Cluster with Kops==](https://github.com/kubernetes/kops) <span class='md-tag md-tag--info'>⭐ 16614</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> — The official Kubernetes Operations tool for deploying, scaling, and managing highly available, production-grade Kubernetes clusters on public cloud environments (specifically AWS, with alpha/beta support for GCE, DigitalOcean, and OpenStack). Built on a declarative configuration model, Kops manages the underlying VM resources, networking, and DNS required for the control plane.
#### Kops Security

  - **(2020)** [blog.ivnilv.com: Rotating Kops Etcd Certificates](https://blog.ivnilv.com/posts/rotating-kops-etcd-certificates) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dive operational guide detailing how to safely rotate etcd certificates within an AWS-based cluster provisioned by Kops. It walks through the sequence of configuration modifications, rolling updates, and verification checks. Critical reading for system administrators managing long-lived Kops deployments without downtime.
#### Kubeadm

  - **(2026)** [==Kubernetes Cluster with **Kubeadm**==](https://github.com/kubernetes/kubeadm) <span class='md-tag md-tag--info'>⭐ 3977</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The standard bootstrapping engine for establishing conformant Kubernetes clusters. Kubeadm abstracts the complex mechanics of configuring etcd, control plane API components, and node registration into clean `init` and `join` workflows. Designed to serve as the building block for higher-level platform orchestration engines.
#### Kubeadm Guides

  - **(2021)** [mirantis.com: How to install Kubernetes with Kubeadm: A quick and dirty guide](https://www.mirantis.com/blog/how-install-kubernetes-kubeadm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A simplified deployment checklist for running containerized workloads on Kubernetes via kubeadm. Demonstrates manual package installation, initialization commands, and standard validation tests. Good starting point for spinning up fast staging clusters.
  - **(2020)** [Set up a Bare Metal Kubernetes cluster with](https://www.padok.fr/en/blog/kubeadm-kubernetes-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural walk-through showing how to configure a multi-node bare-metal Kubernetes cluster from scratch using kubeadm. Highlights operational choices regarding container runtimes, networking (CNI), and load balancers to simulate cloud-like elasticity on physical hardware.
  - **(2019)** [Setting Up a Kubernetes Cluster on Ubuntu 18.04](https://loves.cloud/setting-up-a-kubernetes-cluster-on-ubuntu-18-04)  <span class='md-tag md-tag--info'>[LEGACY]</span> — Step-by-step tutorial for building a Kubernetes control plane and node infrastructure on Ubuntu 18.04 VMs using kubeadm. Explores Docker runtime configuration and basic CNI setups. Highly legacy given newer Ubuntu releases and containerd/CRI-O standard transition.
#### Kubespray

  - **(2026)** [==**Kubespray**==](https://github.com/kubernetes-sigs/kubespray) <span class='md-tag md-tag--info'>⭐ 18493</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An industry-standard provisioning tool combining Ansible playbooks and kubeadm to deliver highly configurable, multi-cloud, production-grade Kubernetes deployments. Supports declarative definition of CNI plugins, container runtimes (containerd/CRI-O), ingress controllers, and storage drivers, making it the preferred choice for on-premise and bare-metal enterprise automation.
#### Kubespray Guides

  - **(2021)** [adamtheautomator.com/kubespray: Conquer Kubernetes Clusters with Ansible Kubespray](https://adamtheautomator.com/kubespray)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on, practical guide demonstrating step-by-step how to deploy a fully functioning Kubernetes cluster using Kubespray on custom virtual environments. Details preparing host inventories, updating variables, and executing core Ansible playbooks.
  - **(2020)** [redhat.com: An introduction to Kubespray](https://www.redhat.com/en/blog/kubespray-deploy-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory conceptual article published on Red Hat's blog explaining how Kubespray leverages Ansible to deploy and manage cluster lifecycles. Discusses deployment target flexibility and explains why it serves as a powerful alternative for enterprise on-premises platforms.
#### Legacy Tooling

  - **(2018)** [A Comparative Analysis of Kubernetes Deployment Tools: Kubespray, kops, and conjure-up](https://www.altoros.com/blog/404-page-doesnt-exist)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical comparative study of older-generation Kubernetes provisioning tools (Kubespray, Kops, and Conjure-Up). Note: The link has expired, reflecting the rapid evolution and deprecation of early multi-cloud orchestration scripts.
#### Virtualization

  - **(2023)** [Kubeinit 🌟](https://github.com/kubeinit/kubeinit) <span class='md-tag md-tag--info'>⭐ 222</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — An Ansible-based automation tool to deploy Kubernetes, OKD, or OpenShift on bare-metal or VM hosts using KVM/libvirt and nested virtualization. Helps automate clean network definitions, hypervisor provisioning, and cluster bootstrapping. Note: Repo has seen minimal recent activity, indicating transition towards LEGACY status.
### Edge and IoT (1)

#### MicroK8s

  - **(2026)** [****Microk8s****](https://canonical.com/microk8s) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A lightweight, production-grade, single-package Kubernetes distribution by Canonical. It features automatic updates, high-availability cluster builds, and instant addon enablement (e.g., GPU support, Linkerd, Istio). Highly optimized for developer environments, Edge workloads, and IoT gateways.
#### MicroK8s Guides

  - **(2021)** [thenewstack.io: Deploy Microk8s and the Kubernetes Dashboard for K8s Development](https://thenewstack.io/deploy-microk8s-and-the-kubernetes-dashboard-for-k8s-development)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Teaches developers how to install MicroK8s on local workstations and spin up the native visual Kubernetes Dashboard. Demonstrates rapid local testing cycles for testing deployment patterns without external cloud dependencies.
  - **(2021)** [thenewstack.io: Deploy a Kubernetes Cluster on Ubuntu Server with Microk8s](https://thenewstack.io/deploy-a-kubernetes-cluster-on-ubuntu-server-with-microk8s)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines the quick process of setting up single or multi-node Kubernetes infrastructures on Ubuntu Server leveraging MicroK8s' native snap packages. Perfect guide for rapid physical hardware staging or home labs.
#### Sandbox Runtimes

  - **(2020)** [Kata Containers on MicroK8s](https://github.com/didier-durand/microk8s-kata-containers) <span class='md-tag md-tag--info'>⭐ 34</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A community project showcasing how to configure and run Kata Containers inside a Canonical MicroK8s environment for hardware-assisted, hypervisor-isolated container sandboxing. Inactive but serves as a solid blueprint for secure multi-tenant lightweight virtualization.
#### Security Benchmarking

  - **(2020)** [MicroK8s & Kubernetes security benchmark from CIS](https://github.com/didier-durand/microk8s-kube-bench) <span class='md-tag md-tag--info'>⭐ 17</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A validation utility adapting aquasecurity's kube-bench to run structured CIS security benchmarks directly against canonical MicroK8s clusters. Confirms cluster configuration conformance to standard security profiles.
### GitOps (1)

#### Cluster Provisioning (1)

  - **(2022)** [Weave Kubernetes System Control - wksctl](https://github.com/weaveworks/wksctl) <span class='md-tag md-tag--info'>⭐ 389</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — An early GitOps-driven Kubernetes cluster manager from Weaveworks that provisioned clusters from a declared state stored in git. Following Weaveworks' operational shutdown, this project is considered legacy but remains highly influential in GitOps control-loop architecture history.
### Infrastructure as Code

#### Ansible

  - **(2025)** [Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes) <span class='md-tag md-tag--info'>⭐ 625</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly popular and actively maintained Ansible role written by Jeff Geerling that automates the installation and configuration of Kubernetes on Debian/Ubuntu and RedHat/CentOS servers. It simplifies installing kubeadm, kubelet, and kubectl, managing system configurations, and bootstrapping clusters cleanly via playbooks.
#### Terraform

  - **(2020)** [Autoscalable Kubernetes cluster at Exoscale, using Packer and Terraform](https://github.com/PhilippeChepy/exoscale-kubernetes-crio) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A prototype repository demonstrating how to deploy an auto-scalable Kubernetes cluster on Exoscale utilizing Packer to build customized CRI-O images and Terraform for resource provisioning. Inactive, representing historical cloud-specific infrastructure designs.
### Local Clusters

#### Single Node

  - **(2021)** [blog.radwell.codes: Provisioning Single-node Kubernetes Cluster using kubeadm on Ubuntu 20.04](https://blog.radwell.codes/2021/05/provisioning-single-node-kubernetes-cluster-using-kubeadm-on-ubuntu-20-04)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides the reader through a slimmed-down kubeadm installation tailored for developer testing environments on a single Ubuntu VM. Includes the crucial command to untaint the control plane node, allowing user workloads to be scheduled locally without worker nodes.
#### VirtualBox

  - **(2021)** [kosyfrances.com: Using kubeadm to create a Kubernetes 1.20 cluster on VirtualBox with Ubuntu](https://kosyfrances.com/kubernetes-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A local lab guide explaining how to spin up a Kubernetes 1.20 multi-node environment on Oracle VirtualBox using kubeadm. Outlines setting up host-only networking, static IP mapping, and configuring containerd manually. Tailored for software testing and network topology validation.
## Networking

### Container Network Interface

#### CNI Plugins

  - **(2024)** [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave) <span class='md-tag md-tag--info'>⭐ 6613</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Weave Net is a resilient container CNI designed to create peer-to-peer overlay networks without external databases or configurations. The project was officially archived by Weaveworks in 2024, prompting teams to migrate to more modern CNI plugins like Cilium and Calico.
### Service Mesh

#### VMware Tanzu Ecosystem (4)

  - **(2020)** [blogs.vmware.com: VMware Tanzu Service Mesh, built on VMware NSX is Now Available!](https://blogs.vmware.com/networkvirtualization/2020/03/vmware-tanzu-service-mesh-built-on-vmware-nsx-is-now-available.html) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Introduces VMware Tanzu Service Mesh, engineered on NSX technology to support high-performance secure traffic, global load-balancing, and end-to-end telemetry. It enables multi-cluster configurations and unified security policy enforcement across cloud boundaries.
## Observability

### Dashboards and UIs

#### Legacy Tools

  - **(2023)** [vmware-tanzu/octant](https://github.com/vmware-archive/octant) <span class='md-tag md-tag--info'>⭐ 6249</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Octant was a widely used extensible, developer-focused dashboard for exploring Kubernetes structures. It was archived in 2023 and has been succeeded by more modern and active alternatives like Lens and K9s.
## Storage

### Stateful Workloads

#### Legacy Tools (1)

  - **(2019)** [Stateful Kubernetes-In-a-Box with Kontena Pharos](https://blog.purestorage.com/stateful-kubernetes-pure-service-orchestrator-kontena-pharos) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical look at combining the Kontena Pharos Kubernetes distribution with Pure Storage orchestrators to run heavy database workloads. Useful for documenting the evolution of early volume mount drivers before CSI stabilization.

---
💡 **Explore Related:** [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md) | [Ocp4](./ocp4.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md)

