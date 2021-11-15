# On-Premise Production Kubernetes Cluster Installers
- [Introduction](#introduction)
- [Comparative Analysis of Kubernetes Deployment Tools](#comparative-analysis-of-kubernetes-deployment-tools)
- [Deploying Kubernetes Cluster with Kops](#deploying-kubernetes-cluster-with-kops)
- [Deploying Kubernetes Cluster with Kubeadm](#deploying-kubernetes-cluster-with-kubeadm)
- [Deploying Kubernetes Cluster with Ansible](#deploying-kubernetes-cluster-with-ansible)
- [kube-aws Kubernetes on AWS](#kube-aws-kubernetes-on-aws)
- [Kubespray](#kubespray)
- [Conjure up](#conjure-up)
- [WKSctl](#wksctl)
- [Terraform (kubernetes the hard way)](#terraform-kubernetes-the-hard-way)
- [Caravan](#caravan)
- [ClusterAPI](#clusterapi)
- [Microk8s](#microk8s)
- [k8s-tew](#k8s-tew)
- [Kubernetes Operating Systems](#kubernetes-operating-systems)
- [Kubernetes Distributions](#kubernetes-distributions)
    - [Red Hat OpenShift](#red-hat-openshift)
    - [Rancher](#rancher)
    - [Weave Kubernetes Platform](#weave-kubernetes-platform)
    - [Ubuntu Charmed Kubernetes](#ubuntu-charmed-kubernetes)
    - [VMware Kubernetes Tanzu and Project Pacific](#vmware-kubernetes-tanzu-and-project-pacific)
        - [KubeAcademy Pro (free training)](#kubeacademy-pro-free-training)
    - [Kontena Pharos](#kontena-pharos)
    - [Mirantis Docker Enterprise with Kubernetes and Docker Swarm](#mirantis-docker-enterprise-with-kubernetes-and-docker-swarm)
    - [Mirantis k0s](#mirantis-k0s)
    - [K0s](#k0s)
    - [K8e](#k8e)
    - [Typhoon](#typhoon)

## Introduction
- [containerjournal.com: Deploying Kubernetes on Bare Metal](https://containerjournal.com/features/deploying-kubernetes-on-bare-metal/)
## Comparative Analysis of Kubernetes Deployment Tools
* [A Comparative Analysis of Kubernetes Deployment Tools: Kubespray, kops, and conjure-up](https://www.altoros.com/research-papers/a-comparative-analysis-of-kubernetes-deployment-tools-kubespray-kops-and-conjure-up-2/)
* [wecloudpro.com: Deploy HA kubernetes cluster in AWS in less than 5 minutes](http://wecloudpro.com/2020/01/13/kube-autp-aws.html)

## Deploying Kubernetes Cluster with Kops
* [GitHub: Kubernetes Cluster with Kops](https://github.com/kubernetes/kops) 
* [Kubernetes.io: Installing Kubernetes with kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/)
* Minikube and docker client are great for local setups, but not for real clusters. **Kops** and **kubeadm** are tools to spin up a production cluster. You don't need both tools, just one of them. 
* On AWS, the best tool is **kops**. Since [AWS EKS (hosted kubernetes)](https://aws.amazon.com/eks) is currently available, this is the preferred option **(you don't need to maintain the masters)**.
* For other installs, or if you can't get kops to work, you can use **kubeadm**.
* Setup **kops** in your windows with **virtualbox.org** and **vagrantup.com** . Once downloaded, to type a new linux VM, just spin up ubuntu via vagrant in cmd/powershell and run kops installer: 
* [blog.ivnilv.com: Rotating Kops Etcd Certificates](https://blog.ivnilv.com/posts/rotating-kops-etcd-certificates/)

```
C:\ubuntu> vagrant init ubuntu/xenial64
C:\ubuntu> vagrant up
C:\ubuntu> vagrant ssh-config
C:\ubuntu> vagrant ssh
```

```bash
$ curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
$ chmod +x kops-linux-amd64
$ sudo mv kops-linux-amd64 /usr/local/bin/kops
```

## Deploying Kubernetes Cluster with Kubeadm
* [Kubernetes Cluster with **Kubeadm**](https://github.com/kubernetes/kubeadm) It works on any deb / rpm compatible Linux OS, for example Ubuntu, Debian, RedHat or CentOS. This is the main advantage of kubeadm. The tool itself is still in beta (Q1 2018), but is expected to become stable somewhere this year. It's very easy to use and lets you spin kubernetes cluster in just a couple of minutes.
* [medium.com: **Demystifying High Availability in Kubernetes Using Kubeadm**](https://medium.com/velotio-perspectives/demystifying-high-availability-in-kubernetes-using-kubeadm-3d83ed8c458b)
* [Setting Up a Kubernetes Cluster on Ubuntu 18.04](https://loves.cloud/setting-up-a-kubernetes-cluster-on-ubuntu-18-04/)
* [itnext.io: Up and running out of the cloud — How to setup the Masters using kubeadm bootstrap](https://itnext.io/kubernetes-journey-up-and-running-out-of-the-cloud-how-to-setup-the-masters-using-kubeadm-9a496a14fbc1) In this article, you’ll see how to make use of kubeadm bootstrap to set up and join 3 master instances as members of our cluster.
* [Set up a Bare Metal Kubernetes cluster with ](https://www.padok.fr/en/blog/kubeadm-kubernetes-cluster)
* [blog.tobias-huebner.org: Low-budget self-hosted Kubernetes 🌟](https://blog.tobias-huebner.org/low-budget-kubernetes-self-hosted-series/)
* [mirantis.com: How to install Kubernetes with Kubeadm: A quick and dirty guide](https://www.mirantis.com/blog/how-install-kubernetes-kubeadm)
* [kosyfrances.com: Using kubeadm to create a Kubernetes 1.20 cluster on VirtualBox with Ubuntu](https://kosyfrances.com/kubernetes-cluster/)
* [blog.radwell.codes: Provisioning Single-node Kubernetes Cluster using kubeadm on Ubuntu 20.04](https://blog.radwell.codes/2021/05/provisioning-single-node-kubernetes-cluster-using-kubeadm-on-ubuntu-20-04/)

## Deploying Kubernetes Cluster with Ansible 
- [Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes)
- [krd](https://github.com/electrocucaracha/krd) offers a reference for deploying a Kubernetes cluster. Its ansible playbooks allow to provision a deployment on Bare-metal or Virtual Machines
- [Kubeinit 🌟](https://github.com/kubeinit/kubeinit) KubeInit provides Ansible playbooks and roles for the deployment and configuration of multiple Kubernetes distributions. KubeInit's mission is to have a fully automated way to deploy in a single command a curated list of prescribed architectures.
    - [youtube: OpenShift Commons En Vivo - KubeInit con Maria Bracho, Scott McCarty, and Carlos Camacho (Red Hat, Spanish) 🌟](https://www.youtube.com/watch?v=9_6H7Ahsdm4&ab_channel=OpenShift)
- [itwonderlab.com: Kubernetes Cluster using Vagrant and Ansible with Containerd (in 3 minutes) 🌟](https://www.itwonderlab.com/en/ansible-kubernetes-vagrant-tutorial/)

## kube-aws Kubernetes on AWS
- [Kubernetes on AWS (kube-aws)](https://kubernetes-incubator.github.io/kube-aws/) A command-line tool to declaratively manage Kubernetes clusters on AWS

## Kubespray
- [**Kubespray**](https://github.com/kubernetes-sigs/kubespray)
- [redhat.com: An introduction to Kubespray](https://www.redhat.com/sysadmin/kubespray-deploy-kubernetes) By combining Ansible and Kubernetes, Kubespray can deploy Kubernetes clusters on multiple machines.

## Conjure up
- [**Conjure up**](https://conjure-up.io/)

## WKSctl
* [**Weave Kubernetes System Control - wksctl**](https://github.com/weaveworks/wksctl) Open Source Weaveworks Kubernetes System
* [WKSctl - A New OSS Kubernetes Manager using GitOps](https://www.weave.works/blog/wksctl-a-new-oss-kubernetes-manager-using-gitops)
* [WKSctl: a Tool for Kubernetes Cluster Management Using GitOps](https://www.infoq.com/news/2020/02/wksctl-kubernetes-gitops/)

## Terraform (kubernetes the hard way)
* [**Kelsey Hightower: kubernetes the hard way**](https://github.com/kelseyhightower/kubernetes-the-hard-way)
* [napo.io: Kubernetes The (real) Hard Way on AWS](https://napo.io/posts/kubernetes-the-real-hard-way-on-aws/)
* [napo.io: Terraform Kubernetes Multi-Cloud (ACK, AKS, DOK, EKS, GKE, OKE)](https://napo.io/posts/terraform-kubernetes-multi-cloud-ack-aks-dok-eks-gke-oke/)
* [medium: Upgrading Kubernetes The Hard Way](https://medium.com/nordcloud-engineering/upgrading-kubernetes-the-hard-way-ac533cfb4ff2)
* [Monzo: we learned a lot from self-hosting Kubernetes, but we wouldn't do it again](https://www.computing.co.uk/news/4019233/monzo-learned-lot-self-hosting-kubernetes-wouldn%E2%80%99) Don't need to do it the hard way anymore
* [medium: Kubernetes the hard way on Docker](https://medium.com/@brightzheng100/kubernetes-the-hard-way-on-docker-f512bae734af)
* [Autoscalable Kubernetes cluster at Exoscale, using Packer and Terraform](https://github.com/PhilippeChepy/exoscale-kubernetes-crio)
* [Kubernetes the Hard Way: Azure Edition](https://github.com/carlosonunez/kubernetes-the-hard-way-on-azure) teaches you how to deploy Kubernetes from scratch on Azure based on the legendary Kubernetes the Hard Way.
* [Kubernetes The Hard Way: AWS Edition](https://github.com/prabhatsharma/kubernetes-the-hard-way-aws) AWS version of Kelsey's kubernetes-the-hard-way

## Caravan
- [linecorp.com: Building Large Kubernetes Clusters with **Caravan**](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters/)

## ClusterAPI
- [**ClusterAPI**](https://cluster-api.sigs.k8s.io/)
- [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89)
- [medium: ClusterOps: 1-Line Commit to Upgrade Your Kubernetes Clusters 🌟](https://medium.com/swlh/clusterops-1-line-commit-to-upgrade-your-kubernetes-clusters-de3548124d04)
- [cncf.io webinar: Deploying Kubernetes to bare metal using cluster API](https://www.cncf.io/webinars/deploying-kubernetes-to-bare-metal-using-cluster-api/)
- [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89)
- [github.com: Cluster API Helm Chart](https://github.com/kgamanji/cluster-api-helm-chart) - [youtube: Cluster API & FluxCD - the power of GitOps](https://www.youtube.com/watch?v=QbSw8dPhHGM&ab_channel=KatieGamanji) A Helm chart to install Cluster API manifests
- [weave.works: Manage Thousands of Clusters with GitOps and the Cluster API](https://www.weave.works/blog/manage-thousands-of-clusters-with-gitops-and-the-cluster-api)
- [thenewstack.io: Cluster API Offers a Way to Manage Multiple Kubernetes Deployments](https://thenewstack.io/cluster-api-offers-a-way-to-manage-multiple-kubernetes-deployments/)
- [thenewstack.io: Provision Bare-Metal Kubernetes with the Cluster API](https://thenewstack.io/provision-bare-metal-kubernetes-with-the-cluster-api/)
- [cncf.io: Kubernetes Cluster API reaches production readiness with version 1.0](https://www.cncf.io/blog/2021/10/06/kubernetes-cluster-api-reaches-production-readiness-with-version-1-0/)

## Microk8s
- [**Microk8s**](https://microk8s.io/)
- [Kata Containers on MicroK8s](https://github.com/didier-durand/microk8s-kata-containers) This repository encompasses a fully scripted Github workflow to test the transparent use of the runtime for Kata Containers (Katas) on MicroK8s
- [MicroK8s & Kubernetes security benchmark from CIS](https://github.com/didier-durand/microk8s-kube-bench)
- [cloudsavvyit.com: How to run your own kubernetes cluster with Microk8s](https://www.cloudsavvyit.com/13024/how-to-run-your-own-kubernetes-cluster-with-microk8s)

## k8s-tew
- [**k8s-tew**](https://github.com/darxkies/k8s-tew) Kubernetes is a fairly complex project. For a newbie it is hard to understand and also to use. While [Kelsey Hightower’s Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way), on which this project is based, helps a lot to understand Kubernetes, it is optimized for the use with Google Cloud Platform.

## Kubernetes Operating Systems 
- [kubedex.com: Kubernetes Operating Systems 🌟](https://kubedex.com/kubernetes-operating-systems/)

## Kubernetes Distributions
- [acloudguru.com: Which Kubernetes distribution is right for you?](https://acloudguru.com/blog/engineering/which-kubernetes-distribution-is-right-for-you)
### Red Hat OpenShift 
* [Openshift Container Platform](openshift.md)
* [OKD](https://www.okd.io/) The Community Distribution of Kubernetes that powers Red Hat OpenShift
* [itprotoday.com: Who's Winning in the Container Software Market 🌟](https://www.itprotoday.com/containers/whos-winning-container-software-market) Thanks to its container customer training, the $1 billion container software market is Red Hat’s to lose. Where do the other players stand?

### Rancher
* [Rancher: Enterprise management for Kubernetes](rancher.md)

### Weave Kubernetes Platform
* [weave.works: Weave Kubernetes Platform](https://www.weave.works/) Automate Enterprise Kubernetes the GitOps way
* [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave)

### Ubuntu Charmed Kubernetes 
* [Charmed Kubernetes](https://ubuntu.com/kubernetes/features)
* [Kubernetes GitOps with Azure Arc and Charmed Kubernetes](https://ubuntu.com/blog/gitops-with-azure-arc-and-charmed-kubernetes)

### VMware Kubernetes Tanzu and Project Pacific
* [blogs.vmware.com: Introducing Project Pacific (vSphere with Kubernetes)](https://blogs.vmware.com/vsphere/2019/08/introducing-project-pacific.html)
* [**VMware vSphere 7 with Kubernetes** - Project Pacific](https://www.vmware.com/products/vsphere.html)
* [**VMware Kubernetes Tanzu**](https://cloud.vmware.com/tanzu)
* [cormachogan.com: A first look at vSphere with Kubernetes in action](https://cormachogan.com/2020/04/01/a-first-look-at-vsphere-with-kubernetes-in-action/)
* [cormachogan.com: Building a TKG Cluster in vSphere with Kubernetes](https://cormachogan.com/2020/04/07/building-a-tkg-guest-cluster-in-vsphere-with-kubernetes/)
* [blogs.vmware.com: VMware Tanzu Service Mesh, built on VMware NSX is Now Available!](https://blogs.vmware.com/networkvirtualization/2020/03/vmware-tanzu-service-mesh-built-on-vmware-nsx-is-now-available.html/)
* [tanzu.vmware.com: VMware Tanzu SQL: MySQL at Scale Made Easy for Kubernetes](https://tanzu.vmware.com/content/blog/vmware-tanzu-sql-mysql-at-scale-kubernetes)
* [VMware hands-on Labs 🌟](https://labs.hol.vmware.com/)
* [wecloudpro.com: VMware Tanzu Community Edition 🌟](https://www.wecloudpro.com/2021/11/13/Tanzu-Community-Edition.html)
* [vmware-tanzu/octant](https://github.com/vmware-tanzu/octant) Highly extensible platform for developers to better understand the complexity of Kubernetes clusters. Octant is a tool for developers to understand how applications run on a Kubernetes cluster. It aims to be part of the developer's toolkit for gaining insight and approaching complexity found in Kubernetes. Octant offers a combination of introspective tooling, cluster navigation, and object management along with a plugin system to further extend its capabilities.

#### KubeAcademy Pro (free training)
* [tanzu.vmware.com: Introducing KubeAcademy Pro: In-Depth Kubernetes Training, Totally Free](https://tanzu.vmware.com/content/blog/introducing-kubeacademy-pro-in-depth-kubernetes-training-totally-free)
* [kube.academy/pro 🌟](https://kube.academy/pro)

### Kontena Pharos
* [Pharos 🌟](https://k8spharos.dev/) Kubernetes Distribution
* [Stateful Kubernetes-In-a-Box with Kontena Pharos](https://blog.purestorage.com/stateful-kubernetes-pure-service-orchestrator-kontena-pharos/)

### Mirantis Docker Enterprise with Kubernetes and Docker Swarm
- [Mirantis Docker Enterprise 3.1+ with Kubernetes](https://www.mirantis.com/software/docker/docker-enterprise/)
- Docker Enterprise 3.1 announced. Features:
    - Istio is now built into Docker Enterprise 3.1!
    - Comes with Kubernetes 1.17. Kubernetes on Windows capability.
    - Enable Istio Ingress for a Kubernetes cluster with the click of a button
    - Intelligent defaults to get started quickly
    - Virtual services supported out of the box
    - Inbuilt support for GPU Orchestration
    - Launchpad CLI for Docker Enterprise deployment & upgrades

### Mirantis k0s
- [k0s](https://k0sproject.io/)
- [infoq.com: Mirantis Announces k0s, a New Kubernetes Distribution](https://www.infoq.com/news/2020/12/k0s-kubernetes-distribution/)
- [medium: K0s Supports Kubernetes 1.22](https://medium.com/k0sproject/k0s-supports-kubernetes-1-22-a498e41bf5af)

### K0s
- [K0s - Zero Friction Kubernetes](https://github.com/k0sproject/k0s) k0s is an all-inclusive Kubernetes distribution with all the required bells and whistles preconfigured to make building a Kubernetes clusters a matter of just copying an executable to every host and running it.
- [medium: k0s Ready for Production](https://medium.com/k0sproject/k0s-ready-for-production-20255c4b0791)
- [medium: k0s Optimizes Start Time, Adds Cluster Level Backup/Restore and More](https://medium.com/k0sproject/k0s-optimizes-start-time-adds-cluster-level-backup-restore-and-more-8ffef894a1ae)

### K8e
- [xiaods/k8e](https://github.com/xiaods/k8e) K8e 🚀 (said 'kuber easy') - Simple Kubernetes Distribution. Builds on upstream project K3s as codebase, remove Edge/IoT features and extend enterprise features with best practices. 

### Typhoon
- [poseidon/typhoon](https://github.com/poseidon/typhoon) **Typhoon is a minimal and free Kubernetes distribution with Terraform.** [typhoon.psdn.io](https://typhoon.psdn.io/)

