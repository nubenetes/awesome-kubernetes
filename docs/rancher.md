# Rancher
- [Rancher: Enterprise management for Kubernetes](#rancher-enterprise-management-for-kubernetes)
- [Rancher Academy (online training)](#rancher-academy-online-training)
- [Rancher 2](#rancher-2)
    - [Rancher Networking and CNI Providers](#rancher-networking-and-cni-providers)
    - [Rancher 2 RKE](#rancher-2-rke)
- [K3S](#k3s)
    - [K3S Use Cases](#k3s-use-cases)
    - [K3S in Public Clouds](#k3s-in-public-clouds)
    - [K3D](#k3d)
    - [K3OS](#k3os)
- [K3C](#k3c)
- [Hosted Rancher](#hosted-rancher)
- [Rancher on Microsoft Azure](#rancher-on-microsoft-azure)
- [Rancher RKE on vSphere](#rancher-rke-on-vsphere)
- [Rancher Kubernetes on Oracle Cloud](#rancher-kubernetes-on-oracle-cloud)
- [Rancher Software Defined Storage with Longhorn](#rancher-software-defined-storage-with-longhorn)
- [Rancher Fleet to manage multiple kubernetes clusters](#rancher-fleet-to-manage-multiple-kubernetes-clusters)

## Rancher: Enterprise management for Kubernetes
* [rancher.com](https://rancher.com/) Rancher is enterprise management for Kubernetes, an amazing GUI for managing and installing Kubernetes clusters. They have released a number of pieces of software that are part of this ecosystem, for example [Longhorn](https://github.com/longhorn/longhorn) which is a lightweight and reliable distributed block storage system for Kubernetes. 
* [rancher.com: Custom alerts using Prometheus queries](https://rancher.com/blog/2020/custom-monitoring)
* [zdnet.com: Rancher Labs closes $40M funding round to "run Kubernetes everywhere"](https://www.zdnet.com/article/rancher-labs-closes-40m-funding-round-to-run-kubernetes-everywhere/) The six year-old startup is going after new markets that want to run Kubernetes clusters at the edge.

<center>
[![rancher architecture](images/rancher.png)](https://www.youtube.com/watch?v=2LNxGVS81mE) 
</center>
</br>

## Rancher Academy (online training)
- [Rancher Academy 🌟](https://academy.rancher.com/) Rancher Academy is a professional, no-cost, zero obligation certification program centered on empowering commercial customers and the open source community to be successful with Kubernetes and Rancher. 
- [Rancher Labs launches free training course to meet surging demand for Kubernetes skills](https://www.computing.co.uk/news/4015423/rancher-labs-launches-free-training-course-meet-surging-demand-kubernetes) Five-week course covers how to deploy Rancher and manage Kubernetes

## Rancher 2 
- [**Rancher 2**](https://rancher.com/docs/rancher/v2.x/en/) 

### Rancher Networking and CNI Providers 
- [Rancher CNI Providers 🌟](https://rancher.com/docs/rancher/v2.x/en/faq/networking/cni-providers/)

### Rancher 2 RKE
- [**Rancher 2 RKE**](https://rancher.com/products/rke/) Rancher 2 that runs in docker containers. RKE is a CNCF-certified Kubernetes distribution that runs entirely within Docker containers. It solves the common frustration of installation complexity with Kubernetes by removing most host dependencies and presenting a stable path for deployment, upgrades, and rollbacks.
    * [Rancher.com: Setup a basic Kubernetes cluster with ease using RKE](https://rancher.com/blog/2018/2018-09-26-setup-basic-kubernetes-cluster-with-ease-using-rke/)

## K3S 
* [**k3s**](https://k3s.io/) Basic kubernetes with automated installer. Lightweight Kubernetes Distribution.
* [K8s vs k3s](https://www.civo.com/blog/k8s-vs-k3s) "K3s is designed to be a single binary of less than 40MB that completely implements the Kubernetes API. In order to achieve this, they removed a lot of extra drivers that didn't need to be part of the core and are easily replaced with add-ons. K3s is a fully CNCF (Cloud Native Computing Foundation) [certified Kubernetes](https://www.cncf.io/certification/software-conformance/) offering. This means that you can write your YAML to operate against a regular "full-fat" Kubernetes and they'll also apply against a k3s cluster. Due to its low resource requirements, it's possible to run a cluster on anything from 512MB of RAM machines upwards. This means that we can allow pods to run on the master, as well as nodes. And of course, because it's a tiny binary, it means we can install it in a fraction of the time it takes to launch a regular Kubernetes cluster! We generally achieve sub-two minutes to launch a k3s cluster with a handful of nodes, meaning you can be deploying apps to learn/test at the drop of a hat."   
* [**k3sup (said 'ketchup')**](https://github.com/alexellis/k3sup) is a light-weight utility to get from zero to KUBECONFIG with k3s on any local or remote VM. All you need is ssh access and the k3sup binary to get kubectl access immediately.
* [Install Kubernetes with k3sup and k3s](https://medium.com/@alexellisuk/walk-through-install-kubernetes-to-your-raspberry-pi-in-15-minutes-84a8492dc95a)
* [k3s-gitlab](https://github.com/apk8s/k3s-gitlab) k3s + Gitlab install notes. Steps for utilizing k3s to manage a self-hosted Gitlab instance.

### K3S Use Cases
- [K3S Use Cases](https://www.youtube.com/watch?v=2LNxGVS81mE):
    1. Edge computing and Embedded Systems
    2. IOT Gateway
    3. **CI environments** (i.e. Jenkins with Configuration as Code)
    4. Single-App Clusters

### K3S in Public Clouds
- [Run Rancher 2.4 in Azure with K3s and MySQL](https://rancher.com/blog/2020/run-rancher-k3s-mysql)

### K3D
- [**k3d**](https://github.com/rancher/k3d) k3s that runs in docker containers.	

### K3OS
- [**k3OS**](https://github.com/rancher/k3os) k3OS is a Linux distribution designed to remove as much OS maintenance as possible in a Kubernetes cluster. It is specifically designed to only have what is needed to run k3s. Additionally the OS is designed to be managed by kubectl once a cluster is bootstrapped. Nodes only need to join a cluster and then all aspects of the OS can be managed from Kubernetes. Both k3OS and k3s upgrades are handled by the k3OS operator.
- [**K3OS Value Add**](https://www.youtube.com/watch?v=2LNxGVS81mE):
    - **Supports multiple architectures**
        - K3OS runs on x86 and ARM processors to give you maximum flexibility.
    - **Runs only the minimum required services**
        - Fewer services means a tiny attack surface, for greater security.
    - **Doesn't require a package manager**
        - The required services are built into the distribution image.
    - **Models infrastructure as code**
        - Manage system configuration with version control systems.

## K3C 
* [K3C](https://github.com/rancher/k3c) Lightweight local container engine for container development. K3C is a local container engine designed to fill the same gap Docker does in the Kubernetes ecosystem. Specifically k3c focuses on developing and running local containers, basically docker run/build. Currently k3s, the [lightweight Kubernetes distribution](https://github.com/rancher/k3s), provides a great solution for Kubernetes from dev to production. While k3s satisifies the Kubernetes runtime needs, one still needs to run docker (or a docker-like tool) to actually develop and build the container images. k3c is intended to replace docker for just the functionality needed for the Kubernetes ecosystem.

## Hosted Rancher
* [Announcing **Hosted Rancher** with Rancher 2.4 🌟](https://rancher.com/blog/2020/announcing-hosted-rancher)

## Rancher on Microsoft Azure
* [rancher.com/blog: Deploy Kubernetes Clusters on Microsoft Azure with Rancher](https://rancher.com/blog/2020/build-kubernetes-clusters-on-azure)

## Rancher RKE on vSphere
* [rancher.com/blog: Stateful Kubernetes Workloads on vSphere with RKE](https://rancher.com/blog/2020/stateful-kubernetes-workloads)

## Rancher Kubernetes on Oracle Cloud
* [medium.com: OKE Clusters from Rancher 2.0](https://medium.com/swlh/oke-clusters-from-rancher-2-0-409131ad1293) Part one of a series of articles on creating, monitoring, and managing Kubernetes clusters on OCI using Rancher.
* [medium.com: Rancher deployed Kubernetes on Oracle Cloud Infrastructure](https://medium.com/@jlamillan/rancher-deployed-kubernetes-on-oracle-cloud-infrastructure-6b0656cdaec0) Part two of a multi-part series on creating, monitoring, and managing Kubernetes clusters (hosted and non-hosted) on OCI.

## Rancher Software Defined Storage with Longhorn 
* [rancher.com/blog: Getting Started with Longhorn Distributed Block Storage and Cloud-Native Distributed SQL](https://rancher.com/blog/2020/yugabyte?utm_content=126950057)

## Rancher Fleet to manage multiple kubernetes clusters
* [**Fleet** Management for kubernetes](https://rancher.com/blog/2020/fleet-management-kubernetes/) a new open source project from the team at Rancher focused on managing fleets of Kubernetes clusters.
* [itnext.io: Fleet Management of Kubernetes Clusters at Scale — Rancher’s Fleet](https://itnext.io/fleet-management-of-kubernetes-clusters-at-scale-ranchers-fleet-de161cc52325)
