---
hide:
  - navigation
  - toc
---

# Kubernetes Distributions & Installers Matrix Table
- [atodorov.me: Comparing Kubernetes managed services across Digital Ocean, Scaleway, OVHCloud and Linode](https://atodorov.me/2020/06/14/comparing-kubernetes-managed-services-across-digital-ocean-scaleway-ovhcloud-and-linode/)
- [Learnk8s: Comparison of Kubernetes Managed Services 🌟](https://docs.google.com/spreadsheets/d/1RPpyDOLFmcgxMCpABDzrsBYWpPYCIBuvAoUQLwOGoQw/) [Learnk8s](https://www.linkedin.com/company/learnk8s/) has compared Managed Kubernetes Services and put up online a nice sheet displaying best-breed cloud services and their Managed K8s offerings. Look for Price, Quotas, Security, etc.

|  Kubernetes Installer or Distribution | Role | Ecosystem | Infra Provider | On-Premise | Licence | HA | Standalone | Runs in Docker | Ingress + Storage <br/>included | Automated <br/>Deployment | Details | 
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| [Ansible role for kubeadm automation](https://github.com/geerlingguy/ansible-role-kubernetes) | SRE / DevOps | Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes (storage?) | No | Ansible role for kubeadm automation |
| [Kops](https://github.com/kubernetes/kops)| SRE / DevOps | Kubernetes Upstream | AWS | No | OSS | Yes | No | No | Yes | Yes | AWS compliant, alpha release <br/>for other providers | 
| [Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/#kubernetes)| Devel | Kubernetes Upstream | Desktop Virtual Machine | Yes | OSS | No | Yes | Yes | No | Yes | Development environment available in <br/>Docker Desktop on Windows | 
| [Rancher 2](https://rancher.com/docs/rancher/v2.x/en/)| SRE / DevOps | Multi-cloud kubernetes <br/>management | Virtual Machine | Yes | OSS | Yes | No | No | No | No | Racher is an enterprise kubernetes installer <br/>that competes with OpenShift. | 
| [K3s](https://k3s.io/)| SRE / DevOps / IoT | Rancher | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes | Yes | Basic kubernetes with automated installer. |
| [K3d](https://github.com/rancher/k3d)| SRE / DevOps / IoT | Rancher | Virtual Machine | Yes | OSS | Yes | Yes | Yes | Yes | Yes | k3s that runs in docker containers. | 
| [Microk8s](https://microk8s.io/)| Devel / IoT | Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes (beta) | Yes | No | Yes | Yes | Ubuntu. It compites with k3s. |
| [OKD](https://github.com/okd-community-install)| SRE / DevOps | OpenShift | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes <br/>(okd-community-install) | Yes <br/>(okd-community-install) | okd-community-install is a standalone cluster <br/>of 1 node valid for small projects. | 
| [AWS EKS](https://aws.amazon.com/en/eks/)| SRE / DevOps | AWS Kubernetes | AWS | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by AWS | 
| [Google kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/)| SRE / DevOps | Google Kubernetes | GCP | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Google Cloud | 
| [Digital Ocean Kubernetes](https://www.digitalocean.com/products/kubernetes/)| SRE / DevOps | Digital Ocean Kubernetes | Digital Ocean | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Digital Ocean Cloud | 
| [Alibaba Container Service for kubernetes (ACK)](https://www.alibabacloud.com/product/kubernetes) | | SRE / DevOps | Alibaba Kubernetes | Alibaba Cloud | No | N/A | Yes | No | No | yes | Yes | Managed kubernetes by Alibaba Cloud |
| [Oracle Kubernetes Engine (OKE)](https://www.oracle.com/cloud/compute/container-engine-kubernetes.html)| SRE / DevOps | Oracle Kubernetes | Oracle Cloud | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Oracle Cloud | 
| [Terraform (kubernetes the hard way)](https://napo.io/posts/kubernetes-the-real-hard-way-on-aws/)| SRE / DevOps | Kubernetes Upstream | AWS EKS, Google GKE, <br/>Azure AKS, Digital Ocean, <br/>Alibaba, Oracle Cloud | No | N/A | Yes | No | No | Yes | No | kubernetes installer compliant with all the major public cloud providers<br/> (the hard way). It does not use the official installers offered by each <br/>cloud provider. | 
| [Kubespray on Public Cloud](https://github.com/kubernetes-sigs/kubespray)| SRE / DevOps | Kubernetes Upstream | AWS, GCE, Azure, <br/>Oracle Cloud (experimental) | Yes | OSS | Yes | Yes | No | Yes | Yes |  | 
| [Kubespray on Private Cloud](https://github.com/kubernetes-sigs/kubespray)| SRE / DevOps | Kubernetes Upstream | OpenStack, vSphere, <br/>Packet (bare metal), or baremetal | Yes | OSS | Yes | Yes | No | Yes | No |  |
| [Conjure-up ](https://conjure-up.io/)| SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | Yes | No | Yes | Yes |  | 
| [WKSctl](https://github.com/weaveworks/wksctl)| SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | Yes | No | Yes | Yes |  |
| [Caravan](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters/)| SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | Yes | No | Yes | Yes |  |
| [k0s](https://k0sproject.io/)| SRE / DevOps | | | Yes | OSS | Yes | Yes | No | Yes | Yes | Developed by Mirantis | 
| [Ubuntu Charmed Kubernetes](https://ubuntu.com/kubernetes/features)| SRE / DevOps / Devel |  Kubernetes Upstream |  | | |  |  | |  |  |  |
| [VMware Pivotal Container Service (PKS)](https://pivotal.io/platform/pivotal-container-service)| SRE / DevOps | PKS / Cloud Foundry PaaS <br/>(no kubernetes) | vSphere, multi-cloud, public-cloud | Yes | Yes | Yes | No | No | Yes | Yes | Pivotal Container Service (PKS) adquired by VMware in 2019. <br/>Cloud Foundry PaaS that compites with kubernetes. | 
| [VMware vSphere 7 with Kubernetes](https://www.vmware.com/products/vsphere.html)| SRE / DevOps | VMware Kubernetes | vSphere | Yes | Yes | Yes | No | No | Yes | Yes | VMware's kubernetes | 
| [VMware Kubernetes Tanzu (PKS renamed)](https://cloud.vmware.com/tanzu)| SRE / DevOps | VMware Kubernetes | vSphere, multi-cloud, public-cloud | Yes | Yes | Yes | No | No | Yes | Yes | Embed kubernetes natively into vSphere. Competes with OpenShift. | 
| [Mirantis Docker Enterprise 3.1+ with Kubernetes](https://www.mirantis.com/software/docker/docker-enterprise/)| SRE / DevOps | Mirantis Kubernetes | multi-cloud, private & public cloud | Yes | Yes | Yes | No | No | Yes | Yes | Istio, Windows and Linux Worker nodes| 
| [Giant Swarm](https://www.giantswarm.io/) | Platform Engineers / SRE / DevOps | Kubernetes Upstream | Multi-platform, multi-cloud (AWS, GCP, Azure, vSphere, VMWare Cloud Director, Openstack) | Yes | OSS | Yes | Yes | No | Yes | Yes | Giant Swarm is a Operate Services Provider enabling your platform team improving platform engineering capabilities and taking over the responsibility of 24x7. Giant Swarm offers out-of-the-box Clound Native Developer Platforms sorley build with Open-Source Tools to manage Kubernetes and all the necessary capabilities around Security, Connectivity, Observability and Developer Experience. | 

|====================================|==================|======================|==========================|  |  |  |  |  |  |  |=============================================|==============================================================================|
