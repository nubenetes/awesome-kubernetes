# Kubernetes
- [Certified Kubernetes Offerings](#certified-kubernetes-offerings)
- [The State of Cloud-Native Development. Details data on the use of Kubernetes, serverless computing and more](#the-state-of-cloud-native-development-details-data-on-the-use-of-kubernetes-serverless-computing-and-more)
- [Kubernetes open-source container-orchestation](#kubernetes-open-source-container-orchestation)
    - [Templating YAML in Kubernetes with real code. YQ YAML processor](#templating-yaml-in-kubernetes-with-real-code-yq-yaml-processor)
    - [Kubernetes Limits](#kubernetes-limits)
    - [Kubernetes Knowledge Hubs](#kubernetes-knowledge-hubs)
- [Extending Kubernetes](#extending-kubernetes)
    - [Adding Custom Resources. Extending Kubernetes API with Kubernetes Resource Definitions. CRD vs Aggregated API](#adding-custom-resources-extending-kubernetes-api-with-kubernetes-resource-definitions-crd-vs-aggregated-api)
    - [Crossplane, a Universal Control Plane API for Cloud Computing. Crossplane Workloads Definitions](#crossplane-a-universal-control-plane-api-for-cloud-computing-crossplane-workloads-definitions)
- [Kubectl commands](#kubectl-commands)
    - [Kubectl Cheat Sheets](#kubectl-cheat-sheets)
    - [List all resources and sub resources that you can constrain with RBAC](#list-all-resources-and-sub-resources-that-you-can-constrain-with-rbac)
    - [Copy a configMap in kubernetes between namespaces](#copy-a-configmap-in-kubernetes-between-namespaces)
    - [Copy secrets in kubernetes between namespaces](#copy-secrets-in-kubernetes-between-namespaces)
    - [Export resources with kubectl and python](#export-resources-with-kubectl-and-python)
    - [Kubectl Alternatives](#kubectl-alternatives)
        - [Manage Kubernetes (K8s) objects with Ansible Kubernetes Module](#manage-kubernetes-k8s-objects-with-ansible-kubernetes-module)
        - [Jenkins Kubernetes Plugins](#jenkins-kubernetes-plugins)
- [Client Libraries for Kubernetes](#client-libraries-for-kubernetes)
    - [Go Client for Kubernetes](#go-client-for-kubernetes)
    - [Fabric8 Java Client for Kubernetes](#fabric8-java-client-for-kubernetes)
- [Helm Kubernetes Tool](#helm-kubernetes-tool)
- [Lens Kubernetes IDE](#lens-kubernetes-ide)
- [Cluster Autoscaler Kubernetes Tool](#cluster-autoscaler-kubernetes-tool)
    - [HPA and VPA](#hpa-and-vpa)
    - [Cluster Autoscaler and Helm](#cluster-autoscaler-and-helm)
    - [Cluster Autoscaler and DockerHub](#cluster-autoscaler-and-dockerhub)
    - [Cluster Autoscaler in GKE, EKS, AKS and DOKS](#cluster-autoscaler-in-gke-eks-aks-and-doks)
    - [Cluster Autoscaler in OpenShift](#cluster-autoscaler-in-openshift)
- [Kubernetes Special Interest Groups (SIGs). Kubernetes Community](#kubernetes-special-interest-groups-sigs-kubernetes-community)
    - [Kubectl Plugins](#kubectl-plugins)
        - [Kubectl Plugins and Tools](#kubectl-plugins-and-tools)
- [Kubernetes Troubleshooting](#kubernetes-troubleshooting)
- [Kubernetes Tutorials](#kubernetes-tutorials)
    - [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019)
    - [Famous Kubernetes resources of 2020](#famous-kubernetes-resources-of-2020)
- [Kubernetes Patterns](#kubernetes-patterns)
- [e-Books](#e-books)
    - [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019-1)
    - [Kubernetes Patterns eBooks](#kubernetes-patterns-ebooks)
- [Kubernetes Operators](#kubernetes-operators)
    - [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
    - [Writing Kubernetes Operators](#writing-kubernetes-operators)
- [Kubernetes Networking](#kubernetes-networking)
    - [Xposer Kubernetes Controller To Manage Ingresses](#xposer-kubernetes-controller-to-manage-ingresses)
    - [CNI Container Networking Interface](#cni-container-networking-interface)
        - [Project Calico](#project-calico)
- [Kubernetes Sidecars](#kubernetes-sidecars)
- [Kubernetes Security](#kubernetes-security)
    - [Security Best Practices Across Build, Deploy, and Runtime Phases](#security-best-practices-across-build-deploy-and-runtime-phases)
    - [Kubernetes Authentication and Authorization](#kubernetes-authentication-and-authorization)
        - [Kubernetes Authentication Methods](#kubernetes-authentication-methods)
        - [X.509 client certificates](#x509-client-certificates)
        - [Static HTTP Bearer Tokens](#static-http-bearer-tokens)
        - [OpenID Connect](#openid-connect)
        - [Implementing a custom Kubernetes authentication method](#implementing-a-custom-kubernetes-authentication-method)
    - [Pod Security Policies (SCCs - Security Context Constraints in OpenShift)](#pod-security-policies-sccs---security-context-constraints-in-openshift)
    - [EKS Security](#eks-security)
- [Kubernetes Scheduling and Scheduling Profiles](#kubernetes-scheduling-and-scheduling-profiles)
    - [Assigning Pods to Nodes. Pod Affinity and Anti-Affinity](#assigning-pods-to-nodes-pod-affinity-and-anti-affinity)
    - [Pod Topology Spread Constraints and PodTopologySpread Scheduling Plugin](#pod-topology-spread-constraints-and-podtopologyspread-scheduling-plugin)
- [Kubernetes Storage](#kubernetes-storage)
    - [Kubernetes Volumes Guide](#kubernetes-volumes-guide)
    - [ReadWriteMany PersistentVolumeClaims](#readwritemany-persistentvolumeclaims)
- [Non-production Kubernetes Local Installers](#non-production-kubernetes-local-installers)
- [Kubernetes in Public Cloud](#kubernetes-in-public-cloud)
    - [GKE vs EKS vs AKS](#gke-vs-eks-vs-aks)
    - [AWS EKS (Hosted/Managed Kubernetes on AWS)](#aws-eks-hostedmanaged-kubernetes-on-aws)
    - [Tools for multi-cloud Kubernetes management](#tools-for-multi-cloud-kubernetes-management)
- [On-Premise Production Kubernetes Cluster Installers](#on-premise-production-kubernetes-cluster-installers)
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
    - [Kubernetes Distributions](#kubernetes-distributions)
        - [Red Hat OpenShift](#red-hat-openshift)
        - [Weave Kubernetes Platform](#weave-kubernetes-platform)
        - [Ubuntu Charmed Kubernetes](#ubuntu-charmed-kubernetes)
        - [VMware Kubernetes Tanzu and Project Pacific](#vmware-kubernetes-tanzu-and-project-pacific)
        - [Rancher: Enterprise management for Kubernetes](#rancher-enterprise-management-for-kubernetes)
            - [Rancher 2](#rancher-2)
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
        - [Kontena Pharos](#kontena-pharos)
        - [Mirantis Docker Enterprise with Kubernetes and Docker Swarm](#mirantis-docker-enterprise-with-kubernetes-and-docker-swarm)
- [Cloud Development Kit (CDK) for Kubernetes](#cloud-development-kit-cdk-for-kubernetes)
    - [AWS Cloud Development Kit (AWS CDK)](#aws-cloud-development-kit-aws-cdk)
- [SpringBoot with Docker](#springboot-with-docker)
- [Docker in Docker](#docker-in-docker)
- [Serverless with OpenFaas and Knative](#serverless-with-openfaas-and-knative)
- [Kubernetes interview questions](#kubernetes-interview-questions)
- [Container Ecosystem](#container-ecosystem)
- [Container Flowchart](#container-flowchart)
- [Videos](#videos)

## Certified Kubernetes Offerings
* [Certified Kubernetes offerings 🌟](https://www.cncf.io/certification/software-conformance/)

## The State of Cloud-Native Development. Details data on the use of Kubernetes, serverless computing and more
* [Cloud-Native Development Survey Details Kubernetes, Serverless Data 🌟](https://virtualizationreview.com/articles/2020/05/08/cloud-native-dev-survey.aspx)

## Kubernetes open-source container-orchestation
* [Wikipedia.org: Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
* [kubernetes.io](https://kubernetes.io/)
* [unofficial-kubernetes.readthedocs.io](https://unofficial-kubernetes.readthedocs.io/)
* [Awesome kubernetes 🌟](https://github.com/ramitsurana/awesome-kubernetes)
* [https://www.reddit.com/r/kubernetes 🌟](https://www.reddit.com/r/kubernetes) 
* [stackify.com: The Advantages of Using Kubernetes and Docker Together 🌟](https://stackify.com/kubernetes-docker-deployments/)
* [Ansible for devops: Kubernetes](https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes)
* [kubedex.com 🌟](https://kubedex.com/) Discover, Compare and Share Kubernetes Applications
    * [kubedex.com: autoscaling 🌟](https://kubedex.com/autoscaling)
* [medium.com: The Kubernetes Scheduler: this series aims to advance the understanding of Kubernetes and its underlying concepts](https://medium.com/@dominik.tornow/the-kubernetes-scheduler-cd429abac02f)
* [medium.com: A Year Of Running Kubernetes at MYOB, And The Importance Of Empathy](https://medium.com/@jpcontad/a-year-of-running-kubernetes-as-a-product-7eed1204eecd)
* [blogs.mulesoft.com - K8s: 8 questions about Kubernetes](https://blogs.mulesoft.com/dev/resources-dev/k8s-kubernetes/)
* [labs.mwrinfosecurity.com: Attacking Kubernetes through Kubelet](https://labs.mwrinfosecurity.com/blog/attacking-kubernetes-through-kubelet/)
* [blog.doit-intl.com: Kubernetes and Secrets Management in the Cloud](https://blog.doit-intl.com/kubernetes-and-secrets-management-in-cloud-858533c20dca)
* [medium.com: Kubernetes Canary Deployment #1 Gitlab CI](https://medium.com/@wuestkamp/kubernetes-canary-deployment-1-gitlab-ci-518f9fdaa7ed)
* [kubernetes-on-aws.readthedocs.io](https://kubernetes-on-aws.readthedocs.io/ )
* [techbeacon.com: Why teams fail with Kubernetes—and what to do about it 🌟](https://techbeacon.com/enterprise-it/why-teams-fail-kubernetes-what-do-about-it)
* [itnext.io: Kubernetes rolling updates, rollbacks and multi-environments 🌟](https://itnext.io/kubernetes-rolling-updates-rollbacks-and-multi-environments-4ff9912df5)
* [learnk8s.io: Architecting Kubernetes clusters — choosing a worker node size 🌟](https://learnk8s.io/kubernetes-node-size)
* [youtube: Kubernetes 101: Get Better Uptime with K8s Health Checks](https://www.youtube.com/watch?v=D9w3DH1zAc8)
* [learnk8s.io: Load balancing and scaling long-lived connections in Kubernetes 🌟](https://learnk8s.io/kubernetes-long-lived-connections)
* [itnext.io: Successful & Short Kubernetes Stories For DevOps Architects](https://itnext.io/successful-short-kubernetes-stories-for-devops-architects-677f8bfed803)
* [itnext.io: K8s Vertical Pod Autoscaling 🌟](https://itnext.io/k8s-vertical-pod-autoscaling-fd9e602cbf81)
* [medium.com: kubernetes Pod Priority and Preemption](https://medium.com/@mohaamer5/kubernetes-pod-priority-and-preemption-943c58aee07d)
* [returngis.net: Pruebas de vida de nuestros contenedores en Kubernetes](https://www.returngis.net/2020/02/pruebas-de-vida-de-nuestros-contenedores-en-kubernetes/)
* [itnext.io: K8s prevent queue worker Pod from being killed during deployment](https://itnext.io/k8s-prevent-queue-worker-pod-from-being-killed-during-deployment-4252ea7c13f6) How to prevent a Kubernetes (like RabbitMQ) queue worker Pod from being killed during deployment while handling a message?
* [youtube: deployment strategies in kubernetes | recreate | rolling update | blue/green | canary](https://youtu.be/efiMiaFjtn8)
* [kodekloud.com: Kubernetes Features Every Beginner Must Know](https://kodekloud.com/blog/200628/kubernetes-features-every-beginner-must-know)
* [platform9.com: Kubernetes CI/CD Pipelines at Scale](https://platform9.com/blog/kubernetes-ci-cd-pipelines-at-scale/)
* [learnk8s.io: Architecting Kubernetes clusters — how many should you have? 🌟](https://learnk8s.io/how-many-clusters)
* [magalix.com: Capacity Planning 🌟](https://www.magalix.com/blog/kubernetes-patterns-capacity-planning) When we have multiple Pods with different Priority Class values, the admission controller starts by sorting Pods according to their priority. What happens when there are no nodes with available resources to schedule a high-priority pods? 
* [4 trends for Kubernetes cloud-native teams to watch in 2020](https://searchapparchitecture.techtarget.com/tip/4-trends-for-Kubernetes-cloud-native-teams-to-watch-in-2020)
* [enterprisersproject.com: Kubernetes: Everything you need to know (2020) 🌟](https://enterprisersproject.com/article/2020/4/kubernetes-everything-you-need-know)
* [learnk8s.io: Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes 🌟](https://learnk8s.io/cloud-resources-kubernetes)
* [padok.fr: Kubernetes’ Architecture: Understanding the components and structure of clusters 🌟](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)
* [medium.com: Top 15 Online Courses to Learn Docker, Kubernetes, and AWS for Fullstack Developers and DevOps Engineers](https://medium.com/javarevisited/top-15-online-courses-to-learn-docker-kubernetes-and-aws-for-fullstack-developers-and-devops-d8cc4f16e773)
* [Allocatable memory and CPU in Kubernetes Nodes 🌟](https://learnk8s.io/allocatable-resources) Not all CPU and memory in your Kubernetes nodes can be used to run Pods. In this article, you will learn how managed Kubernetes Services such AKS, EKS and GKE reserve resources for workloads, operating systems, daemons and Kubernetes agent.
* [5 open source projects that make Kubernetes even better: Prometheus, Operator framework, Knative, Tekton, Kubeflow 🌟](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve) Open source projects bring many additional capabilities to Kubernetes, such as performance monitoring, developer tools, serverless capabilities, and CI/CD workflows. Check out these five widely used options
* [**Optimize** Kubernetes cluster management with these 5 tips 🌟](https://searchitoperations.techtarget.com/feature/Optimize-Kubernetes-cluster-management-with-these-5-tips) Effective Kubernetes cluster management requires operations teams to balance pod and node deployments with performance and availability needs.
* [medium: How to Deploy a Web Application with Kubernetes 🌟](https://medium.com/swlh/how-to-deploy-an-asp-net-application-with-kubernetes-3c00c5fa1c6e) Learn how to create a Kubernetes cluster from scratch and deploy a web application (SPA+API) in two hours.
* [blog.pipetail.io: 10 most common mistakes using kubernetes 🌟](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)

<center>
[![Kubernetes architecture](images/kubernetes-pod-creation.png)](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)

[![10 most common mistakes](images/10_common_kubernetes_mistakes.jpg){: style="width:60%"}](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s)

[![5 Open-source projects that make #Kubernetes even better](images/five-oss-projects-kubernetes.jpg){: style="width:80%"}](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve)
</center>
<br/>

### Templating YAML in Kubernetes with real code. YQ YAML processor
- [Templating YAML in Kubernetes with real code](https://learnk8s.io/templating-yaml-with-code)
    - TL;DR: You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/). 
    - If you're working on large scale projects, you should consider using **real code** — you can find [hands-on examples on how to programmatically generate Kubernetes resources in Java, Go, Javascript, C# and Python in this repository](https://github.com/learnk8s/templating-kubernetes).

### Kubernetes Limits
* [kubernetes.io Policy Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
* [sysdig.com: Understanding Kubernetes limits and requests by example 🌟](https://sysdig.com/blog/kubernetes-limits-requests/)
* [dev.to/aurelievache: Understanding Kubernetes: part 22 – LimitRange](https://dev.to/aurelievache/understanding-kubernetes-part-22-limitrange-144l)

### Kubernetes Knowledge Hubs
- [k8sref.io 🌟](https://www.k8sref.io/) Kubernetes Reference
- [Kubernetes Research. Research documents on node instance types, managed services, ingress controllers, CNIs, etc. 🌟](https://learnk8s.io/research) A research hub to collect all knowledge around Kubernetes. Those are in-depth reports and comparisons designed to drive your decisions. Should you use GKE, AKS, EKS? How many nodes? What instance type?

## Extending Kubernetes
### Adding Custom Resources. Extending Kubernetes API with Kubernetes Resource Definitions. CRD vs Aggregated API
- [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- Use a custom resource (CRD or Aggregated API) if most of the following apply:
    - You want to use Kubernetes client libraries and CLIs to create and update the new resource.
    - You want top-level support from kubectl; for example, kubectl get my-object object-name.
    - You want to build new automation that watches for updates on the new object, and then CRUD other objects, or vice versa.
    - You want to write automation that handles updates to the object.
    - You want to use Kubernetes API conventions like .spec, .status, and .metadata.
    - You want the object to be an abstraction over a collection of controlled resources, or a summarization of other resources.
- Kubernetes provides two ways to add custom resources to your cluster:
    - CRDs are simple and can be created without any programming.
    - API Aggregation requires programming, but allows more control over API behaviors like how data is stored and conversion between API versions.
- Kubernetes provides these two options to meet the needs of different users, so that neither ease of use nor flexibility is compromised.
- Aggregated APIs are subordinate API servers that sit behind the primary API server, which acts as a proxy. This arrangement is called API Aggregation (AA). To users, it simply appears that the Kubernetes API is extended.
- CRDs allow users to create new types of resources without adding another API server. You do not need to understand API Aggregation to use CRDs.
- Regardless of how they are installed, the new resources are referred to as Custom Resources to distinguish them from built-in Kubernetes resources (like pods).

###  Crossplane, a Universal Control Plane API for Cloud Computing. Crossplane Workloads Definitions
- [crossplane.io 🌟](https://crossplane.io/) Crossplane is an open source Kubernetes add-on that supercharges your Kubernetes clusters enabling you to provision and manage infrastructure, services, and applications from kubectl.
- [Crossplane, a Universal Control Plane API for Cloud Computing](https://www.infoq.com/news/2019/01/upbound-crossplane/)
- [Crossplane as an OpenShift Operator to manage and provision cloud-native services](https://blog.crossplane.io/crossplane-openshift-operator-cloud-native-services/)

## Kubectl commands
### Kubectl Cheat Sheets
* [Kubectl Cheat Sheets](cheatsheets.md)

### List all resources and sub resources that you can constrain with RBAC
* kind of a handy way to see all thing things you can affect with Kubernetes RBAC. This will list all resources and sub resources that you can constrain with RBAC. If you want to see just subresources append "| grep {name}/":

```bash
kubectl get --raw /openapi/v2  | jq '.paths | keys[]'
```

### Copy a configMap in kubernetes between namespaces
* Copy a configMap in kubernetes between namespaces with deprecated "--export" flag:

```bash
kubectl get configmap --namespace=<source> <configmap> --export -o yaml | sed "s/<source>/<dest>/" | kubectl apply --namespace=<dest> -f -
```

* [Flag export deprecated in kubernetes 1.14](https://github.com/kubernetes/kubernetes/pull/73787). Instead following command can be used:

```bash
kubectl get configmap <configmap-name> --namespace=<source-namespace> -o yaml | sed ‘s/namespace: <from-namespace>/namespace: <to-namespace>/’ | kubectl create -f
```

* Reference: [Copy a configMap in kubernetes between namespaces](https://stackoverflow.com/questions/55515594/is-there-a-way-to-share-a-configmap-in-kubernetes-between-namespaces)
  
### Copy secrets in kubernetes between namespaces
* [Copy secrets between namespaces](https://stackoverflow.com/questions/55515594/is-there-a-way-to-share-a-configmap-in-kubernetes-between-namespaces):

```bash
kubectl get secret <secret-name> --namespace=<source> -o yaml | sed ‘s/namespace: <from-namespace>/namespace: <to-namespace>/’ | kubectl create -f
```

### Export resources with kubectl and python
* Export resources with [zoidbergwill/export.sh](https://gist.github.com/zoidbergwill/6af8c80cc5b706e2adcf25df3dc2f7e1#file-export_resources-py), by [zoidbergwill](https://gist.github.com/zoidbergwill)

### Kubectl Alternatives
* [Helm and Kubernetes](#helm-and-kubernetes)
* [Other kubernetes tools](#other-kubernetes-tools)

#### Manage Kubernetes (K8s) objects with Ansible Kubernetes Module
* [Manage Kubernetes (K8s) objects](https://docs.ansible.com/ansible/latest/modules/k8s_module.html)
* [ansibleforkubernetes.com 🌟](https://www.ansibleforkubernetes.com/)

#### Jenkins Kubernetes Plugins
* [Jenkins Kubernetes Plugin](https://plugins.jenkins.io/kubernetes/)
* [Kubernetes Continuous Deploy](https://plugins.jenkins.io/kubernetes-cd/)

## Client Libraries for Kubernetes
### Go Client for Kubernetes
- [Go client for Kubernetes](https://github.com/kubernetes/client-go) Go clients for talking to a kubernetes cluster.

### Fabric8 Java Client for Kubernetes
- [Fabric8](https://fabric8.io/) has been available as a Java client for Kubernetes since 2015, and today is one of the most popular client libraries for Kubernetes (the most popular is [client-go](https://github.com/kubernetes/client-go), which is the client library for the Go programming language on Kubernetes). In recent years, **fabric8 has evolved from a Java client for the Kubernetes REST API to a full-fledged alternative to the kubectl command-line tool for Java-based development**.
* [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client/)
- [developers.redhat.com: How the fabric8 Maven plug-in deploys Java applications to OpenShift](https://developers.redhat.com/blog/2020/05/28/how-the-fabric8-maven-plug-in-deploys-java-applications-to-openshift/)
* [Fabric8.io Microservices Development Platform](https://fabric8.io/) It is an open source microservices platform based on Docker, Kubernetes and Jenkins. It is built by the Red Hat guys.The purpose of the project is to make it easy to create microservices, build, test and deploy them via Continuous Delivery pipelines then run and manage them with Continuous Improvement and ChatOps. Fabric8 installs and configures the following things for you automatically: Jenkins, Gogs, Fabric8 registry, Nexus, SonarQube.

## Helm Kubernetes Tool
* [helm.sh](https://helm.sh/)
    * [helm.sh/docs](https://helm.sh/docs) 
* [GitHub: Helm, the Kubernetes Package Manager](https://github.com/helm/helm) Installing and managing Kubernetes applications
* [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4)
* [Delve into Helm: Advanced DevOps](https://www.youtube.com/watch?v=cZ1S2Gp47ng)
* [Continuously delivering apps to Kubernetes using Helm](https://www.youtube.com/watch?v=CmPK93hg5w8)
* [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w)
* [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o)
* [dzone: the art of the helm chart patterns](https://dzone.com/articles/the-art-of-the-helm-chart-patterns-from-the-offici)
* [dzone: 15 useful helm chart tools](https://dzone.com/articles/15-useful-helm-charts-tools)
* [dzone: create install upgrade and rollback a helm chart - part 1](https://dzone.com/articles/create-install-upgrade-and-rollback-a-helm-chart-p)
* [dzone: create install upgrade and rollback a helm chart - part 2](https://dzone.com/articles/create-install-upgrade-rollback-a-helm-chart-part)
* [dzone: cicd with kubernetes and helm](https://dzone.com/articles/cicd-with-kubernetes-and-helm)
* [dzone: do you need helm?](https://dzone.com/articles/do-you-need-helm)
* [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)
* [codefresh.io: Using Helm 3 with Helm 2 charts](https://codefresh.io/helm-tutorial/taking-helm-3-spin/)
* Helm Charts:
    * [Jenkins](https://github.com/helm/charts/tree/master/stable/jenkins) 
    * [Codecentric Jenkins 🌟](https://github.com/codecentric/helm-charts/tree/master/charts/jenkins) Helm 3 compliant (Simpler and more secure than helm 2)
    * [Nexus3](https://github.com/helm/charts/tree/master/stable/sonatype-nexus)
    * [Choerodon Nexus3 🌟](https://hub.helm.sh/charts/choerodon/nexus3) Helm 3 compliant (Simpler and more secure than helm 2)
    * [Sonar](https://github.com/helm/charts/tree/master/stable/sonarqube)
    * [Selenium](https://github.com/helm/charts/tree/master/stable/selenium)
    * [Jmeter](https://github.com/helm/charts/tree/master/stable/distributed-jmeter)
    * [bitnami: create your first helm chart](https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/)
* Helm Charts repositories:
    * [hub.helm.sh 🌟](http://hub.helm.sh) 
    * [Bitnami Helm Charts](https://bitnami.com/stacks/helm)

## Lens Kubernetes IDE
* [Lens Kubernetes IDE 🌟](https://k8slens.dev/) Lens is the only IDE you’ll ever need to take control of your Kubernetes clusters. It's open source and free. Download it today!

[![lens ide](images/header-lens.png)](https://k8slens.dev/)

## Cluster Autoscaler Kubernetes Tool
* [kubernetes.io: Cluster Management - **Resizing a cluster**](https://kubernetes.io/docs/tasks/administer-cluster/cluster-management/#resizing-a-cluster)
* [github.com/kubernetes: **Kubernetes Cluster Autoscaler**](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)
* [Kubernetes Autoscaling in Production: Best Practices for **Cluster Autoscaler, HPA and VPA**](https://www.replex.io/blog/kubernetes-in-production-best-practices-for-cluster-autoscaler-hpa-and-vpa) In this article we will take a deep dive into Kubernetes autoscaling tools including the cluster autoscaler, the horizontal pod autoscaler and the vertical pod autoscaler. We will also identify best practices that developers, DevOps and Kubernetes administrators should follow when configuring these tools.
* [gitconnected.com: Kubernetes Autoscaling 101: Cluster Autoscaler, Horizontal Pod Autoscaler, and Vertical Pod Autoscaler](https://levelup.gitconnected.com/kubernetes-autoscaling-101-cluster-autoscaler-horizontal-pod-autoscaler-and-vertical-pod-2a441d9ad231)
* [packet.com: Kubernetes Cluster Autoscaler](https://www.packet.com/resources/guides/kubernetes-cluster-autoscaler-on-packet/)
* [itnext.io: Kubernetes Cluster Autoscaler: More than scaling out](https://itnext.io/kubernetes-cluster-autoscaler-more-than-scaling-out-7b2d97f10b27)
* [cloud.ibm.com: Containers Troubleshoot Cluster Autoscaler](https://cloud.ibm.com/docs/containers?topic=containers-troubleshoot_cluster_autoscaler)
* [platform9.com: Kubernetes Autoscaling Options: Horizontal Pod Autoscaler, Vertical Pod Autoscaler and Cluster Autoscaler](https://platform9.com/blog/kubernetes-autoscaling-options-horizontal-pod-autoscaler-vertical-pod-autoscaler-and-cluster-autoscaler/)
* [banzaicloud.com: Autoscaling Kubernetes clusters](https://banzaicloud.com/blog/k8s-cluster-autoscaler/)
* [tech.deliveryhero.com: Dynamically overscaling a Kubernetes cluster with cluster-autoscaler and Pod Priority](https://tech.deliveryhero.com/dynamically-overscaling-a-kubernetes-cluster-with-cluster-autoscaler-and-pod-priority/)

### HPA and VPA
* [HPA: Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
* [VPA: Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)

### Cluster Autoscaler and Helm
* [hub.helm.sh: cluster-autoscaler](https://hub.helm.sh/charts/stable/cluster-autoscaler) The cluster autoscaler scales worker nodes within an AWS autoscaling group (ASG) or Spotinst Elastigroup.

### Cluster Autoscaler and DockerHub
* [bitnami/cluster-autoscaler](https://hub.docker.com/r/bitnami/cluster-autoscaler/)

### Cluster Autoscaler in GKE, EKS, AKS and DOKS
* [Amazon Web Services: EKS Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/cluster-autoscaler.html)
    * [eksworkshop.com: Configure Cluster Autoscaler (CA)](https://eksworkshop.com/scaling/deploy_ca/)
* [Azure: AKS Cluster Autoscaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler)
* [Google Cloud Platform: GKE Cluster Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
* [DigitalOcean Kubernetes: DOKS Cluster Autoscaler](https://www.digitalocean.com/docs/kubernetes/how-to/autoscale/)

### Cluster Autoscaler in OpenShift
* [OpenShift 3.11: Configuring the cluster auto-scaler in AWS](https://docs.openshift.com/container-platform/3.11/admin_guide/cluster-autoscaler.html)
* [OpenShift 4.4: Applying autoscaling to an OpenShift Container Platform cluster](https://docs.openshift.com/container-platform/4.4/machine_management/applying-autoscaling.html)

## Kubernetes Special Interest Groups (SIGs). Kubernetes Community
- [Kubernetes Special Interest Groups (SIGs)](https://github.com/kubernetes/community/blob/master/README.md#special-interest-groups-sig) have been around to support the community of developers and operators since around the 1.0 release. People organized around networking, storage, scaling and other operational areas.
- [SIG Apps: build apps for and operate them in Kubernetes](https://kubernetes.io/blog/2016/08/sig-apps-running-apps-in-kubernetes/)
- [Kubernetes SIGs 🌟](https://github.com/kubernetes-sigs)

### Kubectl Plugins 
* [Available kubectl plugins 🌟](https://github.com/kubernetes-sigs/krew-index/blob/master/plugins.md)
* [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
* [youtube: Welcome to the world of kubectl plugins](https://www.youtube.com/watch?v=_W2qZvQT6XY)

<center>
<iframe src="https://www.youtube.com/embed/_W2qZvQT6XY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br/>

#### Kubectl Plugins and Tools
* [ramitsurana/awesome-kubernetes: Tools 🌟](https://github.com/ramitsurana/awesome-kubernetes#configuration)
* [VMware octant](https://github.com/vmware/octant) A web-based, highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
    * [octant.dev](https://octant.dev/) Visualize your Kubernetes workloads. Octant is an open source developer-centric web interface for Kubernetes that lets you inspect a Kubernetes cluster and its applications.
* [KSS - Kubernetes pod status on steroid](https://github.com/chmouel/kss)
* [kubectl-debug](https://github.com/aylei/kubectl-debug)
* [kubectl-tree](https://github.com/ahmetb/kubectl-tree) kubectl plugin to browse Kubernetes object hierarchies as a tree
* [The Golden Kubernetes Tooling and Helpers list](https://docs.google.com/spreadsheets/d/1WPHt0gsb7adVzY3eviMK2W8LejV0I5m_Zpc8tMzl_2w)
* [kubech (kubectl change)](https://github.com/aabouzaid/kubech) Set kubectl contexts/namespaces per shell/terminal to manage multi Kubernetes cluster at the same time.
* [Kubecle](https://github.com/rydogs/kubecle) is a web ui running locally that provides useful information about your kubernetes clusters. It is an alternative to Kubernetes Dashboard. Because it runs locally, you can access any kubernetes clusters you have access to
* [Permission Manager](https://github.com/sighupio/permission-manager) is a project that brings sanity to Kubernetes RBAC and Users management, Web UI FTW
* [developer.sh: Kubernetes client tools overview](https://developer.sh/posts/kubernetes-client-tools-overview)
* [kubectx](https://github.com/ahmetb/kubectx) Faster way to switch between clusters and namespaces in kubectl 
* [go-kubectx](https://github.com/aca/go-kubectx) 5x-10x faster alternative to kubectx. Uses client-go.
* [kubevious](https://github.com/kubevious/kubevious) is open-source software that provides a usable and highly graphical interface for Kubernetes. Kubevious renders all configurations relevant to the application in one place.
* [Guard](https://github.com/appscode/guard) is a Kubernetes Webhook Authentication server. Using guard, you can log into your Kubernetes cluster using various auth providers. Guard also configures groups of authenticated user appropriately.
* [itnext.io: **arkade** by example — Kubernetes apps, the easy way 🌟](https://itnext.io/kubernetes-apps-the-easy-way-f06d9e5cad3c)
* [**Kubei**](https://github.com/Portshift/kubei) is a flexible Kubernetes runtime scanner, scanning images of worker and Kubernetes nodes providing accurate vulnerabilities assessment.
* [**Tubectl**: a kubectl alternative which adds a bit of magic to your everyday kubectl routines by reducing the complexity of working with contexts, namespaces and intelligent matching resources.](https://github.com/reconquest/tubekit)
* [**Kpt**: Packaging up your Kubernetes configuration with git and YAML since 2014 **(Google)**](https://opensource.googleblog.com/2020/03/kpt-packaging-up-your-kubernetes.html)
    * [kpt](https://googlecontainertools.github.io/kpt/)
* [**Krew** 🌟](https://krew.sigs.k8s.io/) is the plugin manager for kubectl command-line tool.
* [kubernetes-common-services](https://github.com/ManagedKube/kubernetes-common-services) These services help make it easier to manage your applications environment in Kubernetes
* [**k8s-job-notify**](https://github.com/sukeesh/k8s-job-notify) Kubernetes Job/CronJob Notifier. This tool sends an alert to slack whenever there is a Kubernetes cronJob/Job failure/success.
* [**kube-opex-analytics** 🌟](https://github.com/rchakode/kube-opex-analytics) Kubernetes Cost Allocation and Capacity Planning Analytics Tool. Built-in hourly, daily, monthly reports - Prometheus exporter - Grafana dashboard.
* [**kubeletctl**](https://github.com/cyberark/kubeletctl) is a command line tool that implement kubelet's API. Part of kubelet's API is documented but most of it is not. This tool covers all the documented and undocumented APIs. The full list of all kubelet's API can be view through the tool or this [API table](https://github.com/cyberark/kubeletctl/blob/master/API_TABLE.md). What can it do ?:
    * Run any kubelet API call
    * Scan for nodes with opened kubelet API
    * Scan for containers with RCE
    * Run a command on all the available containers by kubelet at the same time
    * Get service account tokens from all available containers by kubelet
    * Nice printing :)
* [**inspektor-gadget**](https://github.com/kinvolk/inspektor-gadget) Collection of gadgets for debugging and introspecting Kubernetes applications using BPF [kinvolk.io](https://kinvolk.io)
* [**K8bit** — the tiny Kubernetes dashboard 🌟](https://github.com/learnk8s/k8bit) K8bit is a tiny dashboard that is meant to demonstrate how to use the Kubernetes API to watch for changes.
    * [learnk8s.io/real-time-dashboard](https://learnk8s.io/real-time-dashboard)
* [**KUbernetes Test TooL (kuttl)** 🌟](https://kuttl.dev/)
    * [Youtube Webinar: The KUbernetes Test TooL (kuttl)](https://www.youtube.com/watch?v=Jh-viBv-D04)
* [Portfall: A desktop k8s port-forwarding portal for easy access to all your cluster UIs 🌟](https://github.com/rekon-oss/portfall)
* [k8s-dt-node-labeller](https://github.com/adaptant-labs/k8s-dt-node-labeller) is a Kubernetes controller for labelling a node with devicetree properties (devicetree is a data structure for describing hardware).
* [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup)  
* [kubedev 🌟](https://relferreira.github.io/kubedev/) is a Kubernetes Dashboard that helps developers in their everyday usage
* [Kubectl SSH Proxy 🌟](https://github.com/little-angry-clouds/kubectl-ssh-proxy) Kubectl plugin to launch a ssh socks proxy and use it. This plugin aims to make your life easier when using kubectl a cluster that's behind a SSH bastion.

## Kubernetes Troubleshooting
* [Kubernetes troubleshooting diagram 🌟](https://github.com/redhatspain/awesome-kubernetes/blob/master/docs/images/kubernetes-troubleshooting.jpg)
* [Understanding Kubernetes cluster events 🌟](https://banzaicloud.com/blog/k8s-cluster-logging/)
* [nigelpoulton.com: Troubleshooting kubernetes service discovery - Part 1](https://nigelpoulton.com/blog/f/troubleshooting-kubernetes-service-discovery---part-1)
* [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)

## Kubernetes Tutorials
* [katacoda.com 🌟](https://www.katacoda.com/) Interactive Learning and Training Platform for Software Engineers 
* [kubernetesbyexample.com 🌟](http://kubernetesbyexample.com/)
* [Play with Kubernetes 🌟](https://labs.play-with-k8s.com/) A simple, interactive and fun playground to learn Kubernetes
* [devopscube.com: Kubernetes Tutorials For Beginners: Getting Started Guide 🌟](https://devopscube.com/kubernetes-tutorials-beginners/)
* [Intoduction to Kubernetes (slides, beginners and advanced) 🌟](https://docs.google.com/presentation/d/1zrfVlE5r61ZNQrmXKx5gJmBcXnoa_WerHEnTxu5SMco)
* [medium.com: Kubernetes 101: Pods, Nodes, Containers, and Clusters](https://medium.com/google-cloud/kubernetes-101-pods-nodes-containers-and-clusters-c1509e409e16)
* [medium.com: Learn Kubernetes in Under 3 Hours: A Detailed Guide to Orchestrating Containers](https://medium.com/free-code-camp/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882)
* [kubernetestutorials.com: Install and Deploy Kubernetes on CentOs 7](https://kubernetestutorials.com/install-and-deploy-kubernetes-on-centos-7/)
* [medium.com: Simplifying orchestration with Kubernetes](https://medium.com/@swapnasagarpradhan/simplifying-orchestration-with-kubernetes-e81015681a85)
* [aquasec.com: 70 Best Kubernetes Tutorials 🌟](https://www.aquasec.com/wiki/display/containers/70+Best+Kubernetes+Tutorials) Valuable Kubernetes tutorials from multiple sources, classified into the following categories: Kubernetes AWS and Azure tutorials, networking tutorials, clustering and federation tutorials and more.
* [cloud.google.com: kubernetes comic 🌟](https://cloud.google.com/kubernetes-engine/kubernetes-comic/) Learn about kubernetes and how you can use it for continuous integration and delivery.
* [magalix.com: Kubernetes 101 - Concepts and Why It Matters](https://www.magalix.com/blog/kubernetes-101-concepts-and-why-it-matters)
* [Google Play: Learning Solution - Learn Kubernetes 🌟](https://play.google.com/store/apps/details?id=com.LearningSolution.LearnKubernetes)
* [Google Play: TomApp - Learn Kubernetes](https://play.google.com/store/apps/details?id=tomtran.learnkubernetes)
    * [apkplz.net: Learn Kubernetes 1 APK](https://apkplz.net/app/com.LearningSolution.LearnKubernetes)
    * [Google Play Search](https://play.google.com/store/search?q=learn+kubernetes)
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
* [wardviaene/kubernetes-course 🌟](https://github.com/wardviaene/kubernetes-course) 
* [wardviaene/advanced-kubernetes-course 🌟](https://github.com/wardviaene/advanced-kubernetes-course) 
* [dzone: The complete kubernetes collection tutorials and tools 🌟](https://dzone.com/articles/the-complete-kubernetes-collection-tutorials-and-tools)
* [dzone: kubernetes in 10 minutes a complete guide to look](https://dzone.com/articles/kubernetes-in-10-minutes-a-complete-guide-to-look)
* [magalix.com: The Best Kubernetes Tutorials 🌟](https://www.magalix.com/blog/the-best-kubernetes-tutorials)
* [35 Advanced Tutorials to Learn Kubernetes 🌟](https://medium.com/faun/35-advanced-tutorials-to-learn-kubernetes-dae5695b1f18)

### Famous Kubernetes resources of 2019
* [Kubernetes for developers](https://www.udemy.com/course/kubernetes-for-developers/)
* [Kubernetes for the Absolute Beginners](https://www.udemy.com/course/learn-kubernetes/)
* [Kubernetes: Getting Started (Free)](https://www.udemy.com/course/kubernetes-getting-started/)
* [Kubernetes Tutorial: Learn the Basics](https://dev.to/scalyr/kubernetes-tutorial-learn-the-basics-and-get-started-5dgh)
* [Complete Kubernetes Course](https://www.youtube.com/watch?v=0KQndcIedeg)
* [Getting started with Kubernetes](https://learn.pluralsight.com/programs/2019/free-course/template4)

### Famous Kubernetes resources of 2020
* [javarevisited.blogspot.com: Top 5 courses to Learn Docker and Kubernetes in 2020 - Best of Lot](https://javarevisited.blogspot.com/2019/05/top-5-courses-to-learn-docker-and-kubernetes-for-devops.html)
* [skillslane.com: 10 Best Kubernetes Courses [2020]: Beginner to Advanced Courses](https://skillslane.com/learn-kubernetes-from-these-best-online-courses/)

## Kubernetes Patterns
* [github.com/k8spatterns/examples 🌟](https://github.com/k8spatterns/examples) Examples for "Kubernetes Patterns - Reusable Elements for Designing Cloud-Native Applications"
* [kubernetes.io: container design patterns](https://kubernetes.io/blog/2016/06/container-design-patterns/)
* [magalix.com: Kubernetes Patterns - The Service Discovery Pattern 🌟](https://www.magalix.com/blog/kubernetes-patterns-the-service-discovery-pattern)
* [gardener.cloud: Kubernetes Antipatterns](https://gardener.cloud/050-tutorials/content/howto/antipattern/)
* [dzone.com: Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1)
* [developers.redhat.com: Top 10 must-know Kubernetes design patterns](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)

[![Top 10 Kubernetes patterns](images/top_10_kubernetes_patterns.png)](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)

## e-Books
### Famous Kubernetes resources of 2019
* [Kubernetes essentials E-book 🌟](https://images.linoxide.com/ebook-kubernetes-essentials.pdf)
* [Cloud-Native DevOps With Kubernetes O'Reilly book (Free) 🌟](https://www.nginx.com/resources/library/cloud-native-devops-with-kubernetes/)

### Kubernetes Patterns eBooks
* [k8spatterns.io: Free Kubernetes Patterns e-book 🌟](https://k8spatterns.io/) , [ref](https://www.redhat.com/en/engage/kubernetes-containers-architecture-s-201910240918)
* [magalix.com: Free Kubernetes Application Architecture Patterns eBook 🌟](https://www.magalix.com/kubernetes-application-patterns-e-book-download)

## Kubernetes Operators
* [kruschecompany.com: What is a Kubernetes Operator and Where it Can be Used?](https://kruschecompany.com/kubernetes-operator/)
* [kruschecompany.com: Prometheus Operator – Installing Prometheus Monitoring Within The Kubernetes Environment](https://kruschecompany.com/kubernetes-prometheus-operator/)
* [redhat.com: Kubernetes operators - Embedding operational expertise side by side with containerized applications](https://www.redhat.com/sysadmin/kubernetes-operators)
* [hashicorp.com: Creating Workspaces with the HashiCorp Terraform Operator for Kubernetes](https://www.hashicorp.com/blog/creating-workspaces-with-the-hashicorp-terraform-operator-for-kubernetes/)
* [banzaicloud.com: Kafka rolling upgrade made easy with Supertubes](https://banzaicloud.com/blog/kafka-rolling-upgrade/)
* [devops.com: Day 2 for the Operator Ecosystem 🌟](https://devops.com/day-2-for-the-operator-ecosystem/)
    * [KUDO: The Kubernetes Universal Declarative Operator 🌟](https://kudo.dev/) KUDO is a toolkit that makes it easy to build Kubernetes Operators, in most cases just using YAML.
- [itnext.io: **Operator Lifecycle Manager (OLM)** 🌟](https://itnext.io/wth-is-a-operator-lifecycle-manager-873cf1661b04)

### Flux. The GitOps Operator for Kubernetes
* [Flux 🌟](https://fluxcd.io/) The GitOps operator for Kubernetes
* [docs.fluxcd.io](https://docs.fluxcd.io/)
* [github: Flux CD](https://github.com/fluxcd/flux)
* [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.

### Writing Kubernetes Operators
* [Kubernetes.io: Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
* [opensource.com: Build a Kubernetes Operator in 10 minutes with Operator SDK](https://opensource.com/article/20/3/kubernetes-operator-sdk)
* [magalix.com: Creating Custom Kubernetes Operators](https://www.magalix.com/blog/creating-custom-kubernetes-operators)
* [medium.com: Writing Your First Kubernetes Operator](https://medium.com/faun/writing-your-first-kubernetes-operator-8f3df4453234)
* [bmc.com: What Is a Kubernetes Operator?](https://www.bmc.com/blogs/kubernetes-operator/)

## Kubernetes Networking
* [dzone: how to setup kubernetes networking](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 1)](https://www.weave.works/blog/introduction-to-kubernetes-pod-networking--part-1)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 2)](https://www.weave.works/blog/aws-networking-overview---part-2)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 3)](https://dzone.com/articles/aws-and-kubernetes-networking-options-and-trade-of) 
* [ovh.com - getting external traffic into kubernetes: clusterip, nodeport, loadbalancer and ingress](https://www.ovh.com/blog/getting-external-traffic-into-kubernetes-clusterip-nodeport-loadbalancer-and-ingress/)
* [youtube: Kubernetes Ingress Explained Completely For Beginners](https://www.youtube.com/watch?v=VicH6KojwCI)
* [stackrox.com: Kubernetes Networking Demystified: A Brief Guide](https://www.stackrox.com/post/2020/01/kubernetes-networking-demystified/)
* [medium.com: Fighting Service Latency in Microservices With Kubernetes](https://medium.com/@sindhujacynixit/fighting-service-latency-in-microservices-with-kubernetes-f5a584f5af36)
* [medium.com: Kubernetes NodePort vs LoadBalancer vs Ingress? When should I use what? 🌟](https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0)
* [blog.alexellis.io: Get a LoadBalancer for your private Kubernetes cluster](https://blog.alexellis.io/ingress-for-your-local-kubernetes-cluster/)
* [dustinspecker.com: How Do Kubernetes and Docker Create IP Addresses?!](https://dustinspecker.com/posts/how-do-kubernetes-and-docker-create-ip-addresses/)

### Xposer Kubernetes Controller To Manage Ingresses
* [Xposer 🌟](https://github.com/stakater/Xposer) A Kubernetes controller to manage (create/update/delete) Kubernetes Ingresses based on the Service
    * Problem: We would like to watch for services running in our cluster; and create Ingresses and generate TLS certificates automatically (optional)
    * Solution: Xposer can watch for all the services running in our cluster; Creates, Updates, Deletes Ingresses and uses certmanager to generate TLS certificates automatically based on some annotations.

### CNI Container Networking Interface 
* [Kubernetes.io: Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
* [rancher.com: Container Network Interface (CNI) Providers](https://rancher.com/docs/rancher/v2.x/en/faq/networking/cni-providers/)
* [github.com/containernetworking 🌟](https://github.com/containernetworking)
    * [CNI](https://github.com/containernetworking/cni)
* [dzone: How to Understand and Set Up Kubernetes Networking](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking) Take a look at this tutorial that goes through and explains the inner workings of Kubernetes networking, including working with multiple networks.
* [medium: Container Networking Interface aka CNI](https://medium.com/@vikram.fugro/container-networking-interface-aka-cni-bdfe23f865cf)

#### Project Calico
* [Project Calico 🌟](https://www.projectcalico.org/) Secure networking for the cloud native era

## Kubernetes Sidecars
* [banzaicloud.com: Sidecar container lifecycle changes in Kubernetes 1.18 🌟](https://banzaicloud.com/blog/k8s-sidecars/)

## Kubernetes Security
* [cilium.io](https://cilium.io/)
* [Dzone - devops security at scale](https://dzone.com/articles/devops-security-at-scale)
* [Dzone - Kubernetes Policy Management with Kyverno](https://dzone.com/articles/kubernetes-policy-management-with-kyverno)
    * [github Kyverno - Kubernetes Native Policy Management](https://github.com/nirmata/kyverno/)
* [Dzone - OAuth 2.0](https://dzone.com/articles/oauth-20-beginners-guide)
* [Kubernetes Security Best Practices 🌟](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire)
* [Kubernetes Certs](https://github.com/jetstack/cert-manager/)
* [jeffgeerling.com: Everyone might be a cluster-admin in your Kubernetes cluster](https://www.jeffgeerling.com/blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster)
* [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 1](https://rancher.com/blog/2020/pod-security-policies-part-1)
    * [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 2](https://rancher.com/blog/2020/pod-security-policies-part-2)
* [Microsoft.com: Attack matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
* [codeburst.io: 7 Kubernetes Security Best Practices You Must Follow](https://codeburst.io/7-kubernetes-security-best-practices-you-must-follow-ae32f1ed6444)

### Security Best Practices Across Build, Deploy, and Runtime Phases
- [Kubernetes Security 101: Risks and 29 Best Practices 🌟](https://www.stackrox.com/post/2020/05/kubernetes-security-101/)
- Build Phase:
    1. Use minimal base images
    2. Don’t add unnecessary components
    3. Use up-to-date images only
    4. Use an image scanner to identify known vulnerabilities
    5. Integrate security into your CI/CD pipeline
    6. Label non-fixable vulnerabilities
- Deploy Phase:
    1. Use namespaces to isolate sensitive workloads
    2. Use Kubernetes network policies to control traffic between pods and clusters
    3. Prevent overly permissive access to secrets
    4. Assess the privileges used by containers
    5. Assess image provenance, including registries
    6. Extend your image scanning to deploy phase
    7. Use labels and annotations appropriately
    8. Enable Kubernetes role-based access control (RBAC)
- Runtime Phase:
    1. Leverage contextual information in Kubernetes
    2. Extend vulnerability scanning to running deployments
    3. Use Kubernetes built-in controls when available to tighten security
    4. Monitor network traffic to limit unnecessary or insecure communication
    5. Leverage process whitelisting
    6. Compare and analyze different runtime activity in pods of the same deployments
    7. If breached, scale suspicious pods to zero

[![kubernetes security controls landscape](images/kubernetes-security-controls-landscape.jpg)](https://www.stackrox.com/post/2020/05/kubernetes-security-101/)

### Kubernetes Authentication and Authorization
* [kubernetes.io: Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)
* [kubernetes.io: Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
* [kubernetes.io: Accesing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/)
* [magalix.com: kubernetes authentication 🌟](https://www.magalix.com/blog/kubernetes-authentication)
* [magalix.com: kubernetes authorization 🌟](https://www.magalix.com/blog/kubernetes-authorization)
* [kubernetes login](https://blog.christianposta.com/kubernetes/logging-into-a-kubernetes-cluster-with-kubectl/)

#### Kubernetes Authentication Methods
Kubernetes supports several authentication methods out-of-the-box, such as X.509 client certificates, static HTTP bearer tokens, and OpenID Connect.

#### X.509 client certificates
* [Kubernetes Authentication and Authorization with X509 client certificates](https://medium.com/@sureshpalemoni/kubernetes-authentication-and-authorization-with-x509-client-certificates-edbc3517c10)

#### Static HTTP Bearer Tokens 
* [kubernetes.io: Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
* [stackoverflow: Accessing the Kubernetes REST end points using bearer token](https://stackoverflow.com/questions/56214715/accessing-the-kubernetes-rest-end-points-using-bearer-token)

#### OpenID Connect
* [OpenID Connect](https://openid.net/)

#### Implementing a custom Kubernetes authentication method 
* [Implementing a custom Kubernetes authentication method](https://learnk8s.io/kubernetes-custom-authentication)

### Pod Security Policies (SCCs - Security Context Constraints in OpenShift)
* [Pod Security Policy (SCC in OpenShift) 🌟](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)

### EKS Security
* [Security Group Rules EKS](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
* [EC2 ENI and IP Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)
* [Calico in EKS](https://docs.aws.amazon.com/eks/latest/userguide/calico.html )

## Kubernetes Scheduling and Scheduling Profiles
* [Kubernetes Scheduling](https://kubernetes.io/docs/reference/scheduling/)
* [Scheduling Profiles](https://kubernetes.io/docs/reference/scheduling/profiles/)

### Assigning Pods to Nodes. Pod Affinity and Anti-Affinity 
* [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)

### Pod Topology Spread Constraints and PodTopologySpread Scheduling Plugin
* [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/)
* [Introducing PodTopologySpread plugin](https://kubernetes.io/blog/2020/05/introducing-podtopologyspread/)

## Kubernetes Storage
[Cloud Native Storage](storage.md)

### Kubernetes Volumes Guide
- [Filesystem vs Volume vs Persistent Volume 🌟](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-volumes-example-nfs-persistent-volume.html)
- This is a guide that covers:
    - How to set up and use volumes in Kubernetes
    - What are persistent volumes, and how to use them
    - How to use an NFS volume
    - Shared data and volumes between pods

### ReadWriteMany PersistentVolumeClaims 
- [Create ReadWriteMany PersistentVolumeClaims on your Kubernetes Cluster 🌟](https://medium.com/asl19-developers/create-readwritemany-persistentvolumeclaims-on-your-kubernetes-cluster-3a8db51f98e3) Kubernetes allows us to provision our PersistentVolumes dynamically using PersistentVolumeClaims. Pods treat these claims as volumes. The access mode of the PVC determines how many nodes can establish a connection to it. We can refer to the resource provider’s docs for their supported access modes.
- [Digital Ocean: Kuberntes PVC ReadWriteMany access mode alternative](https://www.digitalocean.com/community/questions/kuberntes-pvc-readwritemany-access-mode-alternative)

## Non-production Kubernetes Local Installers
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
* [**kind**](https://github.com/kubernetes-sigs/kind) Kubernetes IN Docker - local clusters for testing Kubernetes
* [store.docker.com: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [medium.com: Local Kubernetes for Linux — MiniKube vs MicroK8s](https://medium.com/containers-101/local-kubernetes-for-linux-minikube-vs-microk8s-1b2acad068d3)
* [itnext.io: Run Kubernetes On Your Machine](https://itnext.io/run-kubernetes-on-your-machine-7ee463af21a2) Several options to start playing with K8s in no time

## Kubernetes in Public Cloud
### GKE vs EKS vs AKS
* [medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS](https://medium.com/@Platform9Sys/kubernetes-cloud-services-comparing-gke-eks-and-aks-1fe42770cad3)
* [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.com/post/2020/02/eks-vs-gke-vs-aks/)
* [youtube: Kubernetes Comparison](https://www.youtube.com/watch?v=xM9jpcVGTzY) A beautiful comparison of Kubernetes Services from GCP, AWS and Azure by learnk8s.
    * [learnk8s.io/research:  Comparison of Kubernetes managed services 🌟](https://learnk8s.io/research)

<center>
<iframe src="https://www.youtube.com/embed/xM9jpcVGTzY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

### AWS EKS (Hosted/Managed Kubernetes on AWS)
* [dzone: kops vs EKS](https://dzone.com/articles/kops-vs-eks-a-comparison-guide)
* [udemy.com: amazon eks starter kubernetes on aws](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws/)
* [eksctl: EKS installer](https://github.com/weaveworks/eksctl)
* [medium: Implementing Kubernetes Cluster using AWS EKS (AWS Managed Kubernetes)](https://medium.com/@devopsadvocate/how-to-setup-kubernetes-cluster-using-aws-eks-aws-managed-kubernetes-181d5567a8ef)
* [Amazon EKS Security Best Practices](https://www.stackrox.com/post/2019/09/amazon-eks-security-best-practices/)
* [thenewstack.io: Install and Configure OpenEBS on Amazon Elastic Kubernetes Service](https://thenewstack.io/tutorial-install-and-configure-openebs-on-amazon-elastic-kubernetes-service/)
* [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS 🌟](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks/)
* [magalix.com: Deploying Kubernetes Cluster With EKS 🌟](https://www.magalix.com/blog/deploying-kubernetes-cluster-with-eks) Fargate Deployment vs. Linux Workload

###  Tools for multi-cloud Kubernetes management
[Compare tools for multi-cloud Kubernetes management 🌟](https://searchcloudcomputing.techtarget.com/tip/Compare-tools-for-multi-cloud-Kubernetes-management)

## On-Premise Production Kubernetes Cluster Installers
### Comparative Analysis of Kubernetes Deployment Tools
* [A Comparative Analysis of Kubernetes Deployment Tools: Kubespray, kops, and conjure-up](https://www.altoros.com/research-papers/a-comparative-analysis-of-kubernetes-deployment-tools-kubespray-kops-and-conjure-up-2/)
* [wecloudpro.com: Deploy HA kubernetes cluster in AWS in less than 5 minutes](http://wecloudpro.com/2020/01/13/kube-autp-aws.html)

### Deploying Kubernetes Cluster with Kops
* [GitHub: Kubernetes Cluster with Kops](https://github.com/kubernetes/kops) 
* [Kubernetes.io: Installing Kubernetes with kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/)
* Minikube and docker client are great for local setups, but not for real clusters. **Kops** and **kubeadm** are tools to spin up a production cluster. You don't need both tools, just one of them. 
* On AWS, the best tool is **kops**. Since [AWS EKS (hosted kubernetes)](https://aws.amazon.com/eks) is currently available, this is the preferred option **(you don't need to maintain the masters)**.
* For other installs, or if you can't get kops to work, you can use **kubeadm**.
* Setup **kops** in your windows with **virtualbox.org** and **vagrantup.com** . Once downloaded, to type a new linux VM, just spin up ubuntu via vagrant in cmd/powershell and run kops installer: 

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

### Deploying Kubernetes Cluster with Kubeadm
* [Kubernetes Cluster with **Kubeadm**](https://github.com/kubernetes/kubeadm) It works on any deb / rpm compatible Linux OS, for example Ubuntu, Debian, RedHat or CentOS. This is the main advantage of kubeadm. The tool itself is still in beta (Q1 2018), but is expected to become stable somewhere this year. It's very easy to use and lets you spin kubernetes cluster in just a couple of minutes.
* [medium.com: **Demystifying High Availability in Kubernetes Using Kubeadm**](https://medium.com/velotio-perspectives/demystifying-high-availability-in-kubernetes-using-kubeadm-3d83ed8c458b)
* [Setting Up a Kubernetes Cluster on Ubuntu 18.04](https://loves.cloud/setting-up-a-kubernetes-cluster-on-ubuntu-18-04/)

### Deploying Kubernetes Cluster with Ansible 
- [Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes)

### kube-aws Kubernetes on AWS
- [Kubernetes on AWS (kube-aws)](https://kubernetes-incubator.github.io/kube-aws/) A command-line tool to declaratively manage Kubernetes clusters on AWS

### Kubespray
- [**Kubespray**](https://github.com/kubernetes-sigs/kubespray)

### Conjure up
- [**Conjure up**](https://conjure-up.io/)

### WKSctl
* [**Weave Kubernetes System Control - wksctl**](https://github.com/weaveworks/wksctl) Open Source Weaveworks Kubernetes System
* [WKSctl - A New OSS Kubernetes Manager using GitOps](https://www.weave.works/blog/wksctl-a-new-oss-kubernetes-manager-using-gitops)
* [WKSctl: a Tool for Kubernetes Cluster Management Using GitOps](https://www.infoq.com/news/2020/02/wksctl-kubernetes-gitops/)

### Terraform (kubernetes the hard way)
* [**Kelsey Hightower: kubernetes the hard way**](https://github.com/kelseyhightower/kubernetes-the-hard-way)
* [napo.io: Kubernetes The (real) Hard Way on AWS](https://napo.io/posts/kubernetes-the-real-hard-way-on-aws/)
* [napo.io: Terraform Kubernetes Multi-Cloud (ACK, AKS, DOK, EKS, GKE, OKE)](https://napo.io/posts/terraform-kubernetes-multi-cloud-ack-aks-dok-eks-gke-oke/)

### Caravan
- [linecorp.com: Building Large Kubernetes Clusters with **Caravan**](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters/)

### ClusterAPI
- [**ClusterAPI**](https://cluster-api.sigs.k8s.io/)

### Microk8s
- [**Microk8s**](https://microk8s.io/)

### k8s-tew
- [**k8s-tew**](https://github.com/darxkies/k8s-tew) Kubernetes is a fairly complex project. For a newbie it is hard to understand and also to use. While [Kelsey Hightower’s Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way), on which this project is based, helps a lot to understand Kubernetes, it is optimized for the use with Google Cloud Platform.

### Kubernetes Distributions
#### Red Hat OpenShift 
* [Openshift Container Platform](openshift.md)
* [OKD](https://www.okd.io/) The Community Distribution of Kubernetes that powers Red Hat OpenShift

#### Weave Kubernetes Platform
* [weave.works: Weave Kubernetes Platform](https://www.weave.works/) Automate Enterprise Kubernetes the GitOps way
* [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave)

#### Ubuntu Charmed Kubernetes 
* [Charmed Kubernetes](https://ubuntu.com/kubernetes/features)
* [Kubernetes GitOps with Azure Arc and Charmed Kubernetes](https://ubuntu.com/blog/gitops-with-azure-arc-and-charmed-kubernetes)

#### VMware Kubernetes Tanzu and Project Pacific
* [blogs.vmware.com: Introducing Project Pacific (vSphere with Kubernetes)](https://blogs.vmware.com/vsphere/2019/08/introducing-project-pacific.html)
* [**VMware vSphere 7 with Kubernetes** - Project Pacific](https://www.vmware.com/products/vsphere.html)
* [**VMware Kubernetes Tanzu**](https://cloud.vmware.com/tanzu)
* [cormachogan.com: A first look at vSphere with Kubernetes in action](https://cormachogan.com/2020/04/01/a-first-look-at-vsphere-with-kubernetes-in-action/)
* [cormachogan.com: Building a TKG Cluster in vSphere with Kubernetes](https://cormachogan.com/2020/04/07/building-a-tkg-guest-cluster-in-vsphere-with-kubernetes/)
* [blogs.vmware.com: VMware Tanzu Service Mesh, built on VMware NSX is Now Available!](https://blogs.vmware.com/networkvirtualization/2020/03/vmware-tanzu-service-mesh-built-on-vmware-nsx-is-now-available.html/)

#### Rancher: Enterprise management for Kubernetes
* [rancher.com](https://rancher.com/) Rancher is enterprise management for Kubernetes, an amazing GUI for managing and installing Kubernetes clusters. They have released a number of pieces of software that are part of this ecosystem, for example [Longhorn](https://github.com/longhorn/longhorn) which is a lightweight and reliable distributed block storage system for Kubernetes. 
* [rancher.com: Custom alerts using Prometheus queries](https://rancher.com/blog/2020/custom-monitoring)
* [zdnet.com: Rancher Labs closes $40M funding round to "run Kubernetes everywhere"](https://www.zdnet.com/article/rancher-labs-closes-40m-funding-round-to-run-kubernetes-everywhere/) The six year-old startup is going after new markets that want to run Kubernetes clusters at the edge.

<center>
[![rancher architecture](images/rancher.png)](https://www.youtube.com/watch?v=2LNxGVS81mE) 
</center>
</br>

##### Rancher 2 
- [**Rancher 2**](https://rancher.com/docs/rancher/v2.x/en/) 

##### Rancher 2 RKE
- [**Rancher 2 RKE**](https://rancher.com/products/rke/) Rancher 2 that runs in docker containers. RKE is a CNCF-certified Kubernetes distribution that runs entirely within Docker containers. It solves the common frustration of installation complexity with Kubernetes by removing most host dependencies and presenting a stable path for deployment, upgrades, and rollbacks.
    * [Rancher.com: Setup a basic Kubernetes cluster with ease using RKE](https://rancher.com/blog/2018/2018-09-26-setup-basic-kubernetes-cluster-with-ease-using-rke/)

##### K3S 
* [**k3s**](https://k3s.io/) Basic kubernetes with automated installer. Lightweight Kubernetes Distribution.
* [K8s vs k3s](https://www.civo.com/blog/k8s-vs-k3s) "K3s is designed to be a single binary of less than 40MB that completely implements the Kubernetes API. In order to achieve this, they removed a lot of extra drivers that didn't need to be part of the core and are easily replaced with add-ons. K3s is a fully CNCF (Cloud Native Computing Foundation) [certified Kubernetes](https://www.cncf.io/certification/software-conformance/) offering. This means that you can write your YAML to operate against a regular "full-fat" Kubernetes and they'll also apply against a k3s cluster. Due to its low resource requirements, it's possible to run a cluster on anything from 512MB of RAM machines upwards. This means that we can allow pods to run on the master, as well as nodes. And of course, because it's a tiny binary, it means we can install it in a fraction of the time it takes to launch a regular Kubernetes cluster! We generally achieve sub-two minutes to launch a k3s cluster with a handful of nodes, meaning you can be deploying apps to learn/test at the drop of a hat."   
* [**k3sup (said 'ketchup')**](https://github.com/alexellis/k3sup) is a light-weight utility to get from zero to KUBECONFIG with k3s on any local or remote VM. All you need is ssh access and the k3sup binary to get kubectl access immediately.
* [Install Kubernetes with k3sup and k3s](https://medium.com/@alexellisuk/walk-through-install-kubernetes-to-your-raspberry-pi-in-15-minutes-84a8492dc95a)

###### K3S Use Cases
- [K3S Use Cases](https://www.youtube.com/watch?v=2LNxGVS81mE):
    1. Edge computing and Embedded Systems
    2. IOT Gateway
    3. **CI environments** (i.e. Jenkins with Configuration as Code)
    4. Single-App Clusters

###### K3S in Public Clouds
- [Run Rancher 2.4 in Azure with K3s and MySQL](https://rancher.com/blog/2020/run-rancher-k3s-mysql)

###### K3D
- [**k3d**](https://github.com/rancher/k3d) k3s that runs in docker containers.	

###### K3OS
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

##### K3C 
* [K3C](https://github.com/rancher/k3c) Lightweight local container engine for container development. K3C is a local container engine designed to fill the same gap Docker does in the Kubernetes ecosystem. Specifically k3c focuses on developing and running local containers, basically docker run/build. Currently k3s, the [lightweight Kubernetes distribution](https://github.com/rancher/k3s), provides a great solution for Kubernetes from dev to production. While k3s satisifies the Kubernetes runtime needs, one still needs to run docker (or a docker-like tool) to actually develop and build the container images. k3c is intended to replace docker for just the functionality needed for the Kubernetes ecosystem.

##### Hosted Rancher
* [Announcing **Hosted Rancher** with Rancher 2.4 🌟](https://rancher.com/blog/2020/announcing-hosted-rancher)

##### Rancher on Microsoft Azure
* [rancher.com/blog: Deploy Kubernetes Clusters on Microsoft Azure with Rancher](https://rancher.com/blog/2020/build-kubernetes-clusters-on-azure)

##### Rancher RKE on vSphere
* [rancher.com/blog: Stateful Kubernetes Workloads on vSphere with RKE](https://rancher.com/blog/2020/stateful-kubernetes-workloads)

##### Rancher Kubernetes on Oracle Cloud
* [medium.com: OKE Clusters from Rancher 2.0](https://medium.com/swlh/oke-clusters-from-rancher-2-0-409131ad1293) Part one of a series of articles on creating, monitoring, and managing Kubernetes clusters on OCI using Rancher.
* [medium.com: Rancher deployed Kubernetes on Oracle Cloud Infrastructure](https://medium.com/@jlamillan/rancher-deployed-kubernetes-on-oracle-cloud-infrastructure-6b0656cdaec0) Part two of a multi-part series on creating, monitoring, and managing Kubernetes clusters (hosted and non-hosted) on OCI.

##### Rancher Software Defined Storage with Longhorn 
* [rancher.com/blog: Getting Started with Longhorn Distributed Block Storage and Cloud-Native Distributed SQL](https://rancher.com/blog/2020/yugabyte?utm_content=126950057)

##### Rancher Fleet to manage multiple kubernetes clusters
* [**Fleet** Management for kubernetes](https://rancher.com/blog/2020/fleet-management-kubernetes/) a new open source project from the team at Rancher focused on managing fleets of Kubernetes clusters.
* [itnext.io: Fleet Management of Kubernetes Clusters at Scale — Rancher’s Fleet](https://itnext.io/fleet-management-of-kubernetes-clusters-at-scale-ranchers-fleet-de161cc52325)

#### Kontena Pharos
* [Pharos 🌟](https://k8spharos.dev/) Kubernetes Distribution
* [Stateful Kubernetes-In-a-Box with Kontena Pharos](https://blog.purestorage.com/stateful-kubernetes-pure-service-orchestrator-kontena-pharos/)

#### Mirantis Docker Enterprise with Kubernetes and Docker Swarm
- [Mirantis Docker Enterprise 3.1+ with Kubernetes](https://www.mirantis.com/software/docker/docker-enterprise/)
- Docker Enterprise 3.1 announced. Features:
    - Istio is now built into Docker Enterprise 3.1!
    - Comes with Kubernetes 1.17. Kubernetes on Windows capability.
    - Enable Istio Ingress for a Kubernetes cluster with the click of a button
    - Intelligent defaults to get started quickly
    - Virtual services supported out of the box
    - Inbuilt support for GPU Orchestration
    - Launchpad CLI for Docker Enterprise deployment & upgrades

## Cloud Development Kit (CDK) for Kubernetes 
* [cdk8s.io 🌟](https://cdk8s.io/) Define Kubernetes apps and components using familiar languages. cdk8s is an open-source software development framework for defining Kubernetes applications and reusable abstractions using familiar programming languages and rich object-oriented APIs. cdk8s apps synthesize into standard Kubernetes manifests which can be applied to any Kubernetes cluster.
* [github.com/awslabs/cdk8s](https://github.com/awslabs/cdk8s)

### AWS Cloud Development Kit (AWS CDK)
* [AWS: Introducing CDK for Kubernetes 🌟](https://aws.amazon.com/blogs/containers/introducing-cdk-for-kubernetes/)
* Traditionally, Kubernetes applications are defined with human-readable, static YAML data files which developers write and maintain. Building new applications requires writing a good amount of boilerplate config, copying code from other projects, and applying manual tweaks and customizations. As applications evolve and teams grow, these YAML files become harder to manage. Sharing best practices or making updates involves manual changes and complex migrations.
* YAML is an excellent format for describing the desired state of your cluster, but it is does not have primitives for expressing logic and reusable abstractions. There are [multiple tools](https://github.com/ramitsurana/awesome-kubernetes#configuration) in the Kubernetes ecosystem which attempt to address these gaps in various ways:
    * [kustomize](https://github.com/kubernetes-sigs/kustomize) Customization of kubernetes YAML configurations
    * [jsonnet data templating language](https://github.com/google/jsonnet/tree/master/case_studies/kubernetes)
        * [jsonnet.org](https://jsonnet.org/)
    * [jkcfg](https://github.com/jkcfg/jk) Configuration as Code with ECMAScript
        * [jkcfg.github.io](https://jkcfg.github.io/)
    * [kubecfg](https://github.com/bitnami/kubecfg) A tool for managing complex enterprise Kubernetes environments as code.
    * [kubegen](https://github.com/errordeveloper/kubegen) Simple way to describe Kubernetes resources in a structured way, but without new syntax or magic
    * [Pulumi](https://www.pulumi.com/docs/get-started/kubernetes/) 
* We realized this was exactly the same problem our customers had faced when defining their applications through CloudFormation templates, a problem solved by the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/), and that we could apply the same design concepts from the AWS CDK to help all Kubernetes users.

## SpringBoot with Docker
* [spring.io: spring boot with docker](https://spring.io/guides/gs/spring-boot-docker/)
* [spring.io: Creating Docker images with Spring Boot 2.3.0.M1](https://spring.io/blog/2020/01/27/creating-docker-images-with-spring-boot-2-3-0-m1) 
* [learnk8s.io: Developing and deploying Spring Boot microservices on Kubernetes](https://learnk8s.io/spring-boot-kubernetes-guide)

## Docker in Docker
* [Building Docker images when running Jenkins in Kubernetes](https://www.reddit.com/r/jenkinsci/comments/ctirsc/building_docker_images_when_running_jenkins_in/)
    * [pushbuildtestdeploy.com: jenkins on kubernetes building docker images 🌟](https://pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images/)
    * [ref2](https://github.com/samrocketman/docker-jenkins-jervis/blob/master/README.md#working-with-docker-in-docker)
* [itnext.io: docker in docker](https://itnext.io/docker-in-docker-521958d34efd)
* [code-maze.com: ci jenkins docker](https://code-maze.com/ci-jenkins-docker/)
* [medium: quickstart ci with jenkins and docker in docker](https://medium.com/swlh/quickstart-ci-with-jenkins-and-docker-in-docker-c3f7174ee9ff)
* [getintodevops.com: the simplest way to run docker in docker](https://getintodevops.com/blog/the-simple-way-to-run-docker-in-docker-for-ci#%3A~%3AtargetText=Building+Docker+containers+with+Jenkins+inside+a+container)
* Docker in Docker on EKS:
    * [ref1: docker build --network=host](https://github.com/awslabs/amazon-eks-ami/issues/183)
    * [ref2](https://github.com/weaveworks/eksctl/issues/942)

## Serverless with OpenFaas and Knative
* [Serverless Architectures](serverless.md)

<center>
[![Serverless](images/from-monolith-to-serverless.jpg)](https://www.xenonstack.com/blog/serverless-openfaas-java/) 
</center>

## Kubernetes interview questions
- [Kubernetes Interview Questions and Answers 2019 2020](https://linux.amitmaheshwari.in/2019/11/kubernetes-interview-questions-and.html)
- [intellipaat.com: Top Kubernetes Interview Questions and Answers](https://intellipaat.com/blog/interview-question/kubernetes-interview-questions-answers/)

## Container Ecosystem
* [Author: github.com/rootsongjc](https://github.com/rootsongjc)
  
[![Kubernetes components](images/kubernetes_components_rootsongjc.jpg)](https://github.com/rootsongjc)

## Container Flowchart
* [Assess managed Kubernetes services for your workloads.](https://searchcloudcomputing.techtarget.com/tip/Weigh-the-pros-and-cons-of-managed-Kubernetes-services) Managed services from cloud providers can simplify Kubernetes deployment but create some snags in a multi-cloud model. Follow three steps to see if these services can benefit you.

[![Container flowchart](images/container_flowchart.jpg)](https://searchcloudcomputing.techtarget.com/tip/Weigh-the-pros-and-cons-of-managed-Kubernetes-services)

## Videos

<center>
<iframe src="https://www.youtube.com/embed/PH-2FfFD2PU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe src="https://www.youtube-nocookie.com/embed/9cwjtN3gkD4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/cZ1S2Gp47ng" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/CmPK93hg5w8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br/>
<center>
<iframe src="https://www.youtube.com/embed/9wvEwPLcLcA" width="100%" height="100%" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br/>
