# Kubernetes solutions or installers matrix table

|  PaaS Candidate | Role | Ecosystem | Infra Provider | On-Premise | Licence | HA | Standalone | Runs in Docker | Ingress + Storage <br/>included | Automated <br/>Deployment | Details | URL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  kubeadm | SRE / DevOps | Kubernetes Upstream | Multi platform | Yes | OSS | Yes | No | No | No | No | Official kubernetes deployment tool | https://github.com/kubernetes/kubeadm |
|  Ansible Role with kubeadm | SRE / DevOps | Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes (storage?) | No | Ansible role for kubeadm automation | https://github.com/geerlingguy/ansible-role-kubernetes |
|  kops | SRE / DevOps | Kubernetes Upstream | AWS | No | OSS | Yes | No | No | Yes | Yes | AWS compliant, alpha release <br/>for other providers | https://github.com/kubernetes/kops |
|  Minikube | Devel | Kubernetes Upstream | Dektop Virtual Machine | Yes | OSS | No | Yes | No | No | Yes | Official development environment | https://github.com/kubernetes/minikube |
|  Docker Desktop on Windows | Devel | Kubernetes Upstream | Desktop Virtual Machine | Yes | OSS | No | Yes | Yes | No | Yes | Development environment available in <br/>Docker Desktop on Windows | https://docs.docker.com/docker-for-windows/#kubernetes |
|  Rancher 2 | SRE / DevOps | Multi-cloud kubernetes <br/>management | Virtual Machine | Yes | OSS | Yes | No | No | No | No | Racher is an enterprise kubernetes installer <br/>that competes with OpenShift. | https://rancher.com/docs/rancher/v2.x/en/ |
|  Rancher 2 RKE | SRE / DevOps | Rancher Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | Yes | no | no | Rancher 2 that runs in docker containers. | https://rancher.com/products/rke/ |
|  k3s | SRE / DevOps / IoT | Rancher Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes | Yes | Basic kubernetes with automated installer. | https://k3s.io/ |
|  k3d | SRE / DevOps / IoT | Rancher Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | Yes | Yes | Yes | k3s that runs in docker containers. | https://github.com/rancher/k3d |
|  k3sup (said ‘ketchup’) | SRE / DevOps / IoT | Rancher Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes | Yes | get from zero to KUBECONFIG with k3s on any local or remote VM | https://github.com/alexellis/k3sup |
|  K3OS | SRE / DevOps / IoT | Rancher Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes | Yes | Linux distribution designed to remove as much OS maintenance as <br/>possible in a Kubernetes cluster | https://github.com/rancher/k3os |
|  Microk8s | Devel / IoT | Kubernetes Upstream | Virtual Machine | Yes | OSS | Yes (beta) | Yes | No | Yes | Yes | Ubuntu. It compites with k3s. | https://microk8s.io/ |
|  OKD | SRE / DevOps | OpenShift | Virtual Machine | Yes | OSS | Yes | Yes | No | Yes <br/>(okd-community-install) | Yes <br/>(okd-community-install) | okd-community-install is a standalone cluster <br/>of 1 node valid for small projects. | https://github.com/okd-community-install |
|  Minishift | Devel | OpenShift | Desktop Virtual Machine | Yes | OSS | No | Yes | No | No | Yes | OpenShift 3 official development environment. | https://www.okd.io/minishift/ |
|  OCP 4 CodeReady Containers | Devel | OpenShift | Desktop Virtual Machine | Yes | OSS | No | Yes | No | No | Yes | OpenShift 4 official development environment | https://try.openshift.com |
|  OCP 4 Public Cloud | SRE / DevOps | OpenShift | AWS, GCP, Azure | No | Yes | Yes | No | No | Yes | Yes | OpenShift in Public Cloud | https://try.openshift.com |
|  OpenShift Dedicated | SRE / DevOps | OpenShift | AWS | No | Yes | Yes | No | No | Yes | Yes | OpenShift In AWS managed by Red Hat | https://try.openshift.com |
|  OCP 4 Private Cloud 1 | SRE / DevOps | OpenShift | OpenStack, <br/>Red Hat Virtualization | Yes | Yes | Yes | No | No | Yes | Yes | OpenShift in private cloud with automated <br/>deployment recommeded by Red Hat. | https://try.openshift.com |
|  OCP 4 Private Cloud 2 | SRE / DevOps | OpenShift | vSphere 6.7 U2, Bare Metal | Yes | Yes | Yes | No | No | Yes | No | OpenShift in private cloud with infra providers <br/>that currently don't support automated <br/>deployments. | https://try.openshift.com |
|  AWS EKS | SRE / DevOps | Kubernetes Upstream | AWS | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by AWS | https://aws.amazon.com/en/eks/ |
|  Azure AKS | SRE / DevOps | Kubernetes Upstream | Azure | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Azure | https://azure.microsoft.com/en-en/services/kubernetes-service/ |
|  Google kubernetes Engine (GKE) | SRE / DevOps | Kubernetes Upstream | GCP | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Google Cloud | https://cloud.google.com/kubernetes-engine/ |
|  Digital Ocean Kubernetes | SRE / DevOps | Kubernetes Upstream | Digital Ocean | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Digital Ocean Cloud | https://www.digitalocean.com/products/kubernetes/ |
|  Alibaba Container Service for kubernetes (ACK) | SRE / DevOps | Kubernetes Upstream | Alibaba Cloud | No | N/A | Yes | No | No | yes | Yes | Managed kubernetes by Alibaba Cloud | https://www.alibabacloud.com/product/kubernetes |
|  Oracle Kubernetes Engine (OKE) | SRE / DevOps | Kubernetes Upstream | Oracle Cloud | No | N/A | Yes | No | No | Yes | Yes | Managed kubernetes by Oracle Cloud | https://www.oracle.com/cloud/compute/container-engine-kubernetes.html |
|  Terraform | SRE / DevOps | Kubernetes Upstream | AWS EKS, Google GKE, <br/>Azure AKS, Digital Ocean, <br/>Alibaba, Oracle Cloud | No | N/A | Yes | No | No | Yes | No | kubernetes installer compliant with all the major public cloud providers<br/> (the hard way). It does not use the official installers offered by each <br/>cloud provider. | https://napo.io/posts/kubernetes-the-real-hard-way-on-aws/ |
|  Kubespray on Public Cloud | SRE / DevOps | Kubernetes Upstream | AWS, GCE, Azure, <br/>Oracle Cloud (experimental) | Yes | OSS | Yes | Yes | No | Yes | Yes |  | https://github.com/kubernetes-sigs/kubespray |
|  Kubespray on Private Cloud | SRE / DevOps | Kubernetes Upstream | OpenStack, vSphere, <br/>Packet (bare metal), or baremetal | Yes | OSS | Yes | Yes | No | Yes | No |  | https://github.com/kubernetes-sigs/kubespray |
|  Conjure-up | SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | Yes | No | Yes | Yes |  | https://conjure-up.io/ |
|  WKSctl | SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | Yes | No | Yes | Yes |  | https://github.com/weaveworks/wksctl |
|  Caravan | SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | Yes | No | Yes | Yes |  | https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters/ |
|  ClusterAPI | SRE / DevOps | Kubernetes Upstream |  | Yes | OSS | Yes | No | No | No |  |  | https://cluster-api.sigs.k8s.io/ |
|  Kind | Devel | Kubernetes Upstream |  | Yes | OSS | No | Yes | Yes | No | Yes | Not designed for production use; it is intended for development and <br/>testing environments. | https://github.com/kubernetes-sigs/kind |
|  VMware Pivotal Container Service (PKS) | SRE / DevOps | PKS / Cloud Foundry PaaS <br/>(no kubernetes) | vSphere, multi-cloud, public-cloud | Yes | Yes | Yes | No | No | Yes | Yes | Pivotal Container Service (PKS) adquired by VMware in 2019. <br/>Cloud Foundry PaaS that compites with kubernetes. | https://pivotal.io/platform/pivotal-container-service |
|  VMware vSphere 7 with Kubernetes | SRE / DevOps | VMware Kubernetes | vSphere | Yes | Yes | Yes | No | No | Yes | Yes | VMware's kubernetes | https://www.vmware.com/products/vsphere.html |
|  VMware Kubernetes Tanzu (PKS renamed) | SRE / DevOps | Kubernetes Upstream ? | vSphere, multi-cloud, public-cloud | Yes | Yes | Yes | No | No | Yes | Yes | Embed kubernetes natively into vSphere. Competes with OpenShift. | https://cloud.vmware.com/tanzu |
|  etc |  |  |  |  |  |  |  |  |  |  |  |  |
