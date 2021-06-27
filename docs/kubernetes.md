# Kubernetes. "Kubernetes is not for application development but for platform development" (Kelsey Hightower) 
- [Certified Kubernetes Offerings](#certified-kubernetes-offerings)
- [Channel based messaging platform](#channel-based-messaging-platform)
- [The State of Cloud-Native Development. Details data on the use of Kubernetes, serverless computing and more](#the-state-of-cloud-native-development-details-data-on-the-use-of-kubernetes-serverless-computing-and-more)
- [Kubernetes Failure Stories](#kubernetes-failure-stories)
- [Kubernetesbyexample](#kubernetesbyexample)
- [Kubernetes open-source container-orchestation](#kubernetes-open-source-container-orchestation)
    - [Kubernetes API](#kubernetes-api)
    - [Kubernetes Releases](#kubernetes-releases)
    - [Namespaces](#namespaces)
    - [Kubernetes Best Practices and Tips](#kubernetes-best-practices-and-tips)
    - [Disruptions](#disruptions)
    - [Cost Estimation Strategies](#cost-estimation-strategies)
        - [kubecost](#kubecost)
    - [Kubernetes Resource and Capacity Management. Capacity Planning](#kubernetes-resource-and-capacity-management-capacity-planning)
    - [Kubernetes Monitoring](#kubernetes-monitoring)
        - [Logging in Kubernetes](#logging-in-kubernetes)
        - [ECK Elastic Cloud on Kubernetes](#eck-elastic-cloud-on-kubernetes)
    - [Health Checks](#health-checks)
    - [Architecting Kubernetes clusters](#architecting-kubernetes-clusters)
    - [Templating YAML in Kubernetes with real code. YQ YAML processor](#templating-yaml-in-kubernetes-with-real-code-yq-yaml-processor)
    - [Kubernetes Limits](#kubernetes-limits)
    - [Kube Scheduler](#kube-scheduler)
    - [Kubernetes Knowledge Hubs](#kubernetes-knowledge-hubs)
- [Kubectl commands](#kubectl-commands)
    - [Kubectl Cheat Sheets](#kubectl-cheat-sheets)
    - [Kubectl explain](#kubectl-explain)
    - [Kubectl Autocomplete](#kubectl-autocomplete)
    - [List all resources and sub resources that you can constrain with RBAC](#list-all-resources-and-sub-resources-that-you-can-constrain-with-rbac)
    - [Copy a configMap in kubernetes between namespaces](#copy-a-configmap-in-kubernetes-between-namespaces)
    - [Copy secrets in kubernetes between namespaces](#copy-secrets-in-kubernetes-between-namespaces)
    - [Export resources with kubectl and python](#export-resources-with-kubectl-and-python)
    - [Buildkit CLI for kubectl a drop in replacement for docker build](#buildkit-cli-for-kubectl-a-drop-in-replacement-for-docker-build)
    - [Kubectl Alternatives](#kubectl-alternatives)
        - [Manage Kubernetes (K8s) objects with Ansible Kubernetes Module](#manage-kubernetes-k8s-objects-with-ansible-kubernetes-module)
        - [Jenkins Kubernetes Plugins](#jenkins-kubernetes-plugins)
- [Self Service Kubernetes Namespaces](#self-service-kubernetes-namespaces)
- [Client Libraries for Kubernetes](#client-libraries-for-kubernetes)
- [Helm Kubernetes Tool](#helm-kubernetes-tool)
- [Kubernetes Development Tools. Kubernetes clients and dashboards](#kubernetes-development-tools-kubernetes-clients-and-dashboards)
    - [Okteto local kubernetes development](#okteto-local-kubernetes-development)
    - [Lens Kubernetes IDE](#lens-kubernetes-ide)
    - [Kubenav](#kubenav)
    - [Cloud Manager](#cloud-manager)
    - [Skaffold. Local Kubernetes Development](#skaffold-local-kubernetes-development)
    - [Kind](#kind)
- [Autoscaling](#autoscaling)
    - [Cluster Autoscaler Kubernetes Tool](#cluster-autoscaler-kubernetes-tool)
    - [HPA and VPA](#hpa-and-vpa)
    - [Cluster Autoscaler and Helm](#cluster-autoscaler-and-helm)
    - [Cluster Autoscaler and DockerHub](#cluster-autoscaler-and-dockerhub)
    - [Cluster Autoscaler in GKE, EKS, AKS and DOKS](#cluster-autoscaler-in-gke-eks-aks-and-doks)
    - [Cluster Autoscaler in OpenShift](#cluster-autoscaler-in-openshift)
    - [Kubernetes Load Testing and High Load Tuning](#kubernetes-load-testing-and-high-load-tuning)
- [Extending Kubernetes](#extending-kubernetes)
    - [Adding Custom Resources. Extending Kubernetes API with Kubernetes Resource Definitions. CRD vs Aggregated API](#adding-custom-resources-extending-kubernetes-api-with-kubernetes-resource-definitions-crd-vs-aggregated-api)
    - [Krew, a plugin manager for kubectl plugins](#krew-a-plugin-manager-for-kubectl-plugins)
    - [OpenKruise/Kruise](#openkruisekruise)
    - [Crossplane, a Universal Control Plane API for Cloud Computing. Crossplane Workloads Definitions](#crossplane-a-universal-control-plane-api-for-cloud-computing-crossplane-workloads-definitions)
- [Kubernetes Community](#kubernetes-community)
    - [Community Forums](#community-forums)
    - [Kubernetes Special Interest Groups (SIGs)](#kubernetes-special-interest-groups-sigs)
        - [Kubernetes SIG's Repos](#kubernetes-sigs-repos)
        - [Kubectl Plugins](#kubectl-plugins)
- [Enforcing Policies and governance for kubernetes workloads with Conftest](#enforcing-policies-and-governance-for-kubernetes-workloads-with-conftest)
- [Kubernetes Backup and Migrations](#kubernetes-backup-and-migrations)
    - [Kubernetes Volume Snapshot](#kubernetes-volume-snapshot)
    - [Backup with Trillio Cloud-Native Data Protection for Kubernetes, OpenStack and Virtualization](#backup-with-trillio-cloud-native-data-protection-for-kubernetes-openstack-and-virtualization)
    - [Backup with Kasten K10](#backup-with-kasten-k10)
    - [Backup with Velero](#backup-with-velero)
    - [Konveyor Open Source Migration Tool for Kubernetes](#konveyor-open-source-migration-tool-for-kubernetes)
- [Kubernetes Troubleshooting](#kubernetes-troubleshooting)
    - [Debugging Techniques and Strategies. Debugging with ephemeral containers](#debugging-techniques-and-strategies-debugging-with-ephemeral-containers)
- [Kubernetes Tutorials](#kubernetes-tutorials)
    - [Online Training](#online-training)
    - [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019)
    - [Famous Kubernetes resources of 2020](#famous-kubernetes-resources-of-2020)
    - [K8s Diagrams](#k8s-diagrams)
- [Kubernetes Patterns and Antipatterns. Service Discovery](#kubernetes-patterns-and-antipatterns-service-discovery)
- [Books and e-Books](#books-and-e-books)
    - [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019-1)
    - [Kubernetes Patterns eBooks](#kubernetes-patterns-ebooks)
- [Kubernetes Operators](#kubernetes-operators)
    - [Operator Capability Levels](#operator-capability-levels)
    - [Cluster Addons](#cluster-addons)
    - [K8Spin Operator. Kubernetes multi-tenant operator](#k8spin-operator-kubernetes-multi-tenant-operator)
    - [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
    - [K8s KPIs with Kuberhealthy Operator](#k8s-kpis-with-kuberhealthy-operator)
    - [Writing Kubernetes Operators](#writing-kubernetes-operators)
- [Kubernetes Networking](#kubernetes-networking)
    - [Gateway API](#gateway-api)
    - [Multicloud communication for Kubernetes](#multicloud-communication-for-kubernetes)
    - [Kubernetes Network Policy](#kubernetes-network-policy)
        - [Cilium](#cilium)
    - [Kubernetes Ingress Specification](#kubernetes-ingress-specification)
    - [Xposer Kubernetes Controller To Manage Ingresses](#xposer-kubernetes-controller-to-manage-ingresses)
    - [Software-Defined IP Address Management (IPAM)](#software-defined-ip-address-management-ipam)
    - [CNI Container Networking Interface](#cni-container-networking-interface)
        - [List of existing CNI Plugins (IPAM)](#list-of-existing-cni-plugins-ipam)
        - [Project Calico](#project-calico)
    - [DNS Service with CoreDNS](#dns-service-with-coredns)
    - [Kubernetes Node Local DNS Cache](#kubernetes-node-local-dns-cache)
- [Kubernetes Sidecars](#kubernetes-sidecars)
- [Kubernetes Security](#kubernetes-security)
    - [Service Accounts](#service-accounts)
    - [Kubernetes Secrets](#kubernetes-secrets)
    - [Encrypting the certificate for Kubernetes. SSL certificates with Let's Encrypt in Kubernetes Ingress via cert-manager](#encrypting-the-certificate-for-kubernetes-ssl-certificates-with-lets-encrypt-in-kubernetes-ingress-via-cert-manager)
    - [RBAC](#rbac)
    - [Admission Control](#admission-control)
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
- [Kubernetes etcd](#kubernetes-etcd)
- [Kubernetes Storage](#kubernetes-storage)
    - [Kubernetes Volumes Guide](#kubernetes-volumes-guide)
    - [ReadWriteMany PersistentVolumeClaims](#readwritemany-persistentvolumeclaims)
- [Non-production Kubernetes Local Installers. Kubernetes distributions for local environments](#non-production-kubernetes-local-installers-kubernetes-distributions-for-local-environments)
    - [Telepresence local development for k8s and openshift microservices](#telepresence-local-development-for-k8s-and-openshift-microservices)
- [Managed Kubernetes in Public Cloud](#managed-kubernetes-in-public-cloud)
    - [GKE vs EKS vs AKS](#gke-vs-eks-vs-aks)
    - [Other Managed Kubernetes](#other-managed-kubernetes)
    - [AWS EKS (Hosted/Managed Kubernetes on AWS)](#aws-eks-hostedmanaged-kubernetes-on-aws)
    - [Kubesphere](#kubesphere)
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
        - [Rancher](#rancher)
        - [Weave Kubernetes Platform](#weave-kubernetes-platform)
        - [Ubuntu Charmed Kubernetes](#ubuntu-charmed-kubernetes)
        - [VMware Kubernetes Tanzu and Project Pacific](#vmware-kubernetes-tanzu-and-project-pacific)
            - [KubeAcademy Pro (free training)](#kubeacademy-pro-free-training)
        - [Kontena Pharos](#kontena-pharos)
        - [Mirantis Docker Enterprise with Kubernetes and Docker Swarm](#mirantis-docker-enterprise-with-kubernetes-and-docker-swarm)
        - [Mirantis k0s](#mirantis-k0s)
        - [K0s](#k0s)
- [Cloud Development Kit (CDK) for Kubernetes](#cloud-development-kit-cdk-for-kubernetes)
    - [AWS Cloud Development Kit (AWS CDK)](#aws-cloud-development-kit-aws-cdk)
- [SpringBoot with Docker](#springboot-with-docker)
- [Docker in Docker](#docker-in-docker)
- [Serverless with OpenFaas and Knative](#serverless-with-openfaas-and-knative)
- [Multi-Cluster Federation. Hybrid Cloud Setup Tools](#multi-cluster-federation-hybrid-cloud-setup-tools)
    - [KubeFed](#kubefed)
    - [KubeCarrier](#kubecarrier)
    - [Red Hat Operator Lifecycle Manager (OLM)](#red-hat-operator-lifecycle-manager-olm)
    - [Crossplane](#crossplane)
    - [Istio Service Mesh](#istio-service-mesh)
- [Kubernetes interview questions](#kubernetes-interview-questions)
- [Spanish Kubernetes Blogs](#spanish-kubernetes-blogs)
- [Container Ecosystem](#container-ecosystem)
- [Container Flowchart](#container-flowchart)
- [Kubernetes Scripts](#kubernetes-scripts)
- [Spot instances in Kubernetes](#spot-instances-in-kubernetes)
- [Pixie. Instantly troubleshoot applications on Kubernetes](#pixie-instantly-troubleshoot-applications-on-kubernetes)
- [Videos](#videos)

## Certified Kubernetes Offerings
* [Certified Kubernetes offerings 🌟](https://www.cncf.io/certification/software-conformance/)

## Channel based messaging platform
- [kubernetes.slack.com](https://kubernetes.slack.com)

## The State of Cloud-Native Development. Details data on the use of Kubernetes, serverless computing and more
* [Cloud-Native Development Survey Details Kubernetes, Serverless Data 🌟](https://virtualizationreview.com/articles/2020/05/08/cloud-native-dev-survey.aspx)

## Kubernetes Failure Stories
- [k8s.af 🌟](https://k8s.af/)

## Kubernetesbyexample
- [kubernetesbyexample.com 🌟🌟🌟](https://www.kubernetesbyexample.com) A free learning platform covering the fundamentals of how to develop, deploy, manage, and automate containers in cloud-native environments. 

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
* [opensource.com: How the Kubernetes scheduler works 🌟](https://opensource.com/article/20/11/kubernetes-scheduler) Understand how the Kubernetes scheduler discovers new pods and assigns them to nodes.
* [medium.com: A Year Of Running Kubernetes at MYOB, And The Importance Of Empathy](https://medium.com/@jpcontad/a-year-of-running-kubernetes-as-a-product-7eed1204eecd)
* [blogs.mulesoft.com - K8s: 8 questions about Kubernetes](https://blogs.mulesoft.com/dev/resources-dev/k8s-kubernetes/)
* [labs.mwrinfosecurity.com: Attacking Kubernetes through Kubelet](https://labs.mwrinfosecurity.com/blog/attacking-kubernetes-through-kubelet/)
* [medium.com: Kubernetes Canary Deployment #1 Gitlab CI](https://medium.com/@wuestkamp/kubernetes-canary-deployment-1-gitlab-ci-518f9fdaa7ed)
* [kubernetes-on-aws.readthedocs.io](https://kubernetes-on-aws.readthedocs.io/ )
* [techbeacon.com: Why teams fail with Kubernetes—and what to do about it 🌟](https://techbeacon.com/enterprise-it/why-teams-fail-kubernetes-what-do-about-it)
* [itnext.io: Kubernetes rolling updates, rollbacks and multi-environments 🌟](https://itnext.io/kubernetes-rolling-updates-rollbacks-and-multi-environments-4ff9912df5)
* [learnk8s.io: Load balancing and scaling long-lived connections in Kubernetes 🌟](https://learnk8s.io/kubernetes-long-lived-connections)
* [itnext.io: Successful & Short Kubernetes Stories For DevOps Architects](https://itnext.io/successful-short-kubernetes-stories-for-devops-architects-677f8bfed803)
* [itnext.io: K8s Vertical Pod Autoscaling 🌟](https://itnext.io/k8s-vertical-pod-autoscaling-fd9e602cbf81)
* [medium.com: kubernetes Pod Priority and Preemption](https://medium.com/@mohaamer5/kubernetes-pod-priority-and-preemption-943c58aee07d)
* [returngis.net: Pruebas de vida de nuestros contenedores en Kubernetes](https://www.returngis.net/2020/02/pruebas-de-vida-de-nuestros-contenedores-en-kubernetes/)
* [itnext.io: K8s prevent queue worker Pod from being killed during deployment](https://itnext.io/k8s-prevent-queue-worker-pod-from-being-killed-during-deployment-4252ea7c13f6) How to prevent a Kubernetes (like RabbitMQ) queue worker Pod from being killed during deployment while handling a message?
* [youtube: deployment strategies in kubernetes | recreate | rolling update | blue/green | canary](https://youtu.be/efiMiaFjtn8)
* [kodekloud.com: Kubernetes Features Every Beginner Must Know](https://kodekloud.com/blog/200628/kubernetes-features-every-beginner-must-know)
* [platform9.com: Kubernetes CI/CD Pipelines at Scale](https://platform9.com/blog/kubernetes-ci-cd-pipelines-at-scale/)
* [4 trends for Kubernetes cloud-native teams to watch in 2020](https://searchapparchitecture.techtarget.com/tip/4-trends-for-Kubernetes-cloud-native-teams-to-watch-in-2020)
* [enterprisersproject.com: Kubernetes: Everything you need to know (2020) 🌟](https://enterprisersproject.com/article/2020/4/kubernetes-everything-you-need-know)
* [learnk8s.io: Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes 🌟](https://learnk8s.io/cloud-resources-kubernetes)
* [padok.fr: Kubernetes’ Architecture: Understanding the components and structure of clusters 🌟](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)
* [Allocatable memory and CPU in Kubernetes Nodes 🌟](https://learnk8s.io/allocatable-resources) Not all CPU and memory in your Kubernetes nodes can be used to run Pods. In this article, you will learn how managed Kubernetes Services such AKS, EKS and GKE reserve resources for workloads, operating systems, daemons and Kubernetes agent.
* [5 open source projects that make Kubernetes even better: Prometheus, Operator framework, Knative, Tekton, Kubeflow 🌟](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve) Open source projects bring many additional capabilities to Kubernetes, such as performance monitoring, developer tools, serverless capabilities, and CI/CD workflows. Check out these five widely used options
* [medium: How to Deploy a Web Application with Kubernetes 🌟](https://medium.com/swlh/how-to-deploy-an-asp-net-application-with-kubernetes-3c00c5fa1c6e) Learn how to create a Kubernetes cluster from scratch and deploy a web application (SPA+API) in two hours.
* [blog.pipetail.io: 10 most common mistakes using kubernetes 🌟](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)
* [4 trends for Kubernetes cloud-native teams to watch in 2020 🌟](https://searchapparchitecture.techtarget.com/tip/4-trends-for-Kubernetes-cloud-native-teams-to-watch-in-2020) Today's software architectural landscape seems to change like the weather. Stay ahead of the curve with these cloud-related trends, including GitOps and service meshes.
* [opensource.com: A beginner's guide to Kubernetes container orchestration](https://opensource.com/article/20/6/container-orchestration) Understanding the building blocks of container orchestration makes it easier to get started with Kubernetes.
* [thenewstack.io: 5 Best Practices for Configuring Kubernetes Pods Running in Production](https://thenewstack.io/5-best-practices-for-configuring-kubernetes-pods-running-in-production/)
* [Creating a Kubernetes cloud provider, doesn't required boiling the ocean 🌟](https://thebsdbox.co.uk/2020/03/18/Creating-a-Kubernetes-cloud-doesn-t-required-boiling-the-ocean/)
* [medium: How to configure and manage Pod in Kubernetes Cluster (K8s)](https://medium.com/faun/pod-in-kubernetes-cluster-k8s-adeb5b901153) There are two types of Pods: Single container pod & Multi container pod. 
* [opensource.com: 5 ways to boost your Kubernetes knowledge](https://opensource.com/article/20/6/kubernetes-anniversary)
* [kinvolk.io: Investigating Kubernetes performance issues with BPF 🌟](https://kinvolk.io/blog/2020/04/inside-kinvolk-labs-investigating-kubernetes-performance-issues-with-bpf/)
* [blog.container-solutions.com: 7 Cloud Native Trends to Watch in 2020 🌟](https://blog.container-solutions.com/7-cloud-native-trends-to-watch-in-2020)
* [snyk.io: Shipping Kubernetes-native applications with confidence](https://snyk.io/blog/shipping-kubernetes-native-applications-with-confidence/)
* [medium: Delivering value on Kubernetes](https://medium.com/@dius_au/delivering-value-on-kubernetes-8d5c5655c1b4)
* [medium: 10 Most Common Mistakes When Using Kubernetes 🌟](https://medium.com/devops-dudes/10-most-common-mistakes-when-using-kubernetes-8a07abb8e850) Avoid your cluster from falling over in production by implementing these best practices
* [dev.to: Open a command prompt in a Kubernetes cluster](https://dev.to/eldadak/open-a-command-prompt-in-a-kubernetes-cluster-206g) This starts up a pod (in the default namespace by default) and opens a command line in the given container. As I'm running as root, I can install anything I need for debugging and testing right in my cluster.
* [medium: 5 Things We Overlooked When Deploying Our First App on Kubernetes 🌟](https://medium.com/gumgum-tech/5-things-we-overlooked-when-putting-our-first-app-on-kubernetes-58583c1783e4)
* [opensource.com: Explaining Kubernetes in 10 minutes using an analogy](https://opensource.com/article/20/7/kubernetes-analogy)
* [itnext.io: Kubernetes is Hard!](https://itnext.io/kubernetes-is-hard-190f1d0c6d36)
* [medium: The Kubernetes Cloud Controller Manager](https://medium.com/@m.json/the-kubernetes-cloud-controller-manager-d440af0d2be5)
* [howtoforge.com: How to create Multi-Container Pods in Kubernetes](https://www.howtoforge.com/multi-container-pods-in-kubernetes/)
* [blocksandfiles.com: Kubernetes is in a bit of state about state](https://blocksandfiles.com/2020/07/21/kubernetes-stateful-status/) Kubernetes is “four to five years away” from being a stable distribution capable of running stateful apps, according to Redis Labs chief product officer Alvin Richards.
* [10 most common mistakes when using Kubernetes 🌟🌟](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)
    * resources - requests and limits
    * liveness and readiness probes
    * LoadBalancer for every http service
    * non-kubernetes-aware cluster autoscaling
    * Not using the power of IAM/RBAC
* [Architecting Kubernetes clusters — choosing a cluster size 🌟](https://itnext.io/architecting-kubernetes-clusters-choosing-a-cluster-size-92f6feaa2908)
* [medium: Deploying Kubernetes — Deciding the size of your nodes 🌟](https://medium.com/swlh/deploying-kubernetes-deciding-the-size-of-your-nodes-a115e770e09)
* [medium: A Practical Step-by-Step Guide to Understanding Kubernetes](https://medium.com/better-programming/a-practical-step-by-step-guide-to-understanding-kubernetes-d8be7f82e533) Deploy a distributed application and understand key underlying concepts.
* [medium: Kubernetes, a practical introduction](https://medium.com/nexton/kubernetes-a-practical-introduction-18a5b69e7763)
* [medium: Kubernetes Deployment: Connect Your Front End to Your Back End With Nginx](https://medium.com/better-programming/kubernetes-deployment-connect-your-front-end-to-your-back-end-with-nginx-7e4e7cfef177)
* [learnk8s.iod: Kubernetes production best practices 🌟🌟](https://learnk8s.io/production-best-practices) A curated checklist of best practices designed to help you release to production.
* [itnext.io: Automating System Updates for Kubernetes Clusters using Ansible](https://itnext.io/automating-system-updates-for-kubernetes-clusters-using-ansible-94a70f4e1972)
* [medium: Starting with kubernetes](https://medium.com/@thomaspoignant/starting-with-kubernetes-db121b09fd4)
* [Discovering Running Pods By Using DNS and Headless Services in Kubernetes](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4) When retrieving all service’s connected pods is desired
* [itnext.io: Kubernetes is Hard! 🌟](https://itnext.io/kubernetes-is-hard-190f1d0c6d36) But, where there’s Kubernetes, there’s a way!
* [How we learned to improve Kubernetes CronJobs at Scale (Part 1 of 2)](https://eng.lyft.com/improving-kubernetes-cronjobs-at-scale-part-1-cf1479df98d4)
    * [How we learned to improve Kubernetes CronJobs at Scale (Part 2 of 2)](https://eng.lyft.com/how-we-learned-to-improve-kubernetes-cronjobs-at-scale-part-2-of-2-dad0c973ffca)
* [thenewstack.io: Kubernetes Is the New Standard for Computing, Including the Edge](https://thenewstack.io/kubernetes-is-the-new-standard-for-computing-including-the-edge/)
* [enterprisersproject.com: Managing Kubernetes resources: 5 things to remember](https://enterprisersproject.com/article/2020/8/managing-kubernetes-resources-5-things-remember) Kubernetes automates much of the work of managing containers at scale. But containerized applications commonly share pooled resources, so you need to allocate and manage them properly
* [Kubernetes Tip: What Happens To Pods Running On Node That Become Unreachable?](https://medium.com/tailwinds-navigator/kubernetes-tip-what-happens-to-pods-running-on-node-that-become-unreachable-3d409f734e5d)
* [hackernoon.com: How To Deploy Code Faster Using Kubernetes](https://hackernoon.com/how-to-deploy-code-faster-using-kubernetes-jh1y3ul0)
* [How to handle environment variables with Kubernetes? 🌟](https://humanitec.com/blog/handling-environment-variables-with-kubernetes)
* [Liveness and Readiness Probes for Kubernetes in Phoenix application](https://blog.lelonek.me/liveness-and-readiness-probes-for-kubernetes-in-phoenix-application-890e24d0737e)
* [Kubernetes Liveness and Readiness Probes](https://theithollow.com/2020/05/18/kubernetes-liveness-and-readiness-probes/)
* [learnk8s.io: Graceful shutdown and zero downtime deployments in Kubernetes 🌟🌟](https://learnk8s.io/graceful-shutdown)
* [kubernetes.io: Introducing Hierarchical Namespaces](https://kubernetes.io/blog/2020/08/14/introducing-hierarchical-namespaces/)
* [medium: Kubernetes Pod Redundancy Strategies](https://medium.com/better-programming/kubernetes-pod-redundancy-strategies-a6d9b560749a)
* [sbg.technology: Zero-Downtime Kubernetes Deployments](https://sbg.technology/2020/08/21/zero-downtime-kubernetes-deployments/)
* [medium: Then he asked me “Is Kubernetes right for us?”](https://medium.com/@alexellisuk/then-he-asked-me-is-kubernetes-right-for-us-78695ee35289)
* [thenewstack.io: How does kubernetes work?](https://thenewstack.io/how-does-kubernetes-work/)
* [elmanytas.es: Kubernetes para impostores III](http://elmanytas.es/?q=node/358)
* [loft.sh: Kubernetes: Virtual Clusters For CI/CD & Testing](https://loft.sh/blog/kubernetes-virtual-clusters-for-ci-cd-testing/)
* [medium: Mastering the KUBECONFIG file](https://medium.com/@ahmetb/mastering-kubeconfig-4e447aa32c75)
* [luminousmen.com: Kubernetes 101](https://luminousmen.com/post/kubernetes-101)
* [thenewstack.io: How do applications run on kubernetes? 🌟](https://thenewstack.io/how-do-applications-run-on-kubernetes/)
* [deepsource.io: Breaking down zero downtime deployments in Kubernetes 🌟](https://deepsource.io/blog/zero-downtime-deployment/) An in-depth analysis of deployments in Kubernete
* [ronaknathani.com: How a Kubernetes Pod Gets an IP Address 🌟](https://ronaknathani.com/blog/2020/08/how-a-kubernetes-pod-gets-an-ip-address/)
* [eevans.co: Deconstructing Kubernetes Networking](https://eevans.co/blog/deconstructing-kubernetes-networking/)
* [externalTrafficPolicy=local on kubernetes. How to preserve the source IP in kubernetes](https://blog.getambassador.io/externaltrafficpolicy-local-on-kubernetes-e66e498212f9) externalTrafficPolicy=local is an annotation on the Kubernetes service resource that can be set to preserve the client source IP. When it is set, the actual IP address of a client is propagated to the K8s service instead of the IP address of the node.
* [medium: Single Sign-On in Kubernetes 🌟](https://medium.com/@andriisumko/single-sign-on-in-kubernetes-1ad9528350ed)
* [jfrog.com: Kubernetes in Production with Jessica Deen at swampUP 2020](https://jfrog.com/blog/kubernetes-in-production-with-jessica-deen-at-swampup-2020/)
* [itnext.io: Writing a Kubernetes CLI in Go](https://itnext.io/writing-a-kubernetes-cli-in-go-a3970ad58299)
* [medium: Discovering Running Pods By Using DNS and Headless Services in Kubernetes 🌟](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4) When retrieving all service’s connected pods is desired.
* [semaphoreci.com: Continuous Blue-Green Deployments With Kubernetes 🌟](https://semaphoreci.com/blog/continuous-blue-green-deployments-with-kubernetes)
* [iximiuz.com: Service proxy, pod, sidecar, oh my!](https://iximiuz.com/en/posts/service-proxy-pod-sidecar-oh-my/)
* [medium: 3 Years of Kubernetes in Production–Here’s What We Learned 🌟](https://medium.com/better-programming/3-years-of-kubernetes-in-production-heres-what-we-learned-44e77e1749c8)
* [linuxadvise.com: Kubernetes Node Selectors](https://www.linuxadvise.com/post/kubernetes-node-selectors)
* [linuxadvise.com: Kubernetes Node Affinity](https://www.linuxadvise.com/post/kubernetes-node-affinity)
* [linuxadvise.com: Kubernetes Daemon Sets](https://www.linuxadvise.com/post/kubernetes-daemon-sets)
* [linuxadvise.com: Kubernetes Static Pods](https://www.linuxadvise.com/post/kubernetes-static-pods)
* [linuxadvise.com: Kubernetes Config Maps](https://www.linuxadvise.com/post/kubernetes-config-maps)
* [linuxadvise.com: Kubernetes Rolling Updates and Rollbacks](https://www.linuxadvise.com/post/kubernetes-rolling-updates-and-rollbacks)
* [linuxadvise.com: Kubernetes Secrets](https://www.linuxadvise.com/post/kubernetes-secrets)
* [linuxadvise.com: Kubernetes Pod Security Policy](https://www.linuxadvise.com/post/kubernetes-pod-security-policy)
* [thenewstack.io: How do applications run on kubernetes?](https://thenewstack.io/how-do-applications-run-on-kubernetes/)
* [medium: Kubernetes — Learn Init Container Pattern](https://medium.com/bb-tutorials-and-thoughts/kubernetes-learn-init-container-pattern-7a757742de6b) Understanding Init Container Pattern With an Example Project.
* [Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere/) This tutorial shows you how to expose your private Kubernetes API server to the Internet, so that you can manage your cluster from anywhere, just like you would with a cloud offering.
* [Zero-Downtime Kubernetes Deployments](https://sbg.technology/2020/08/21/zero-downtime-kubernetes-deployments)
* [enterprisersproject.com: How to explain Kubernetes in plain English](https://enterprisersproject.com/article/2017/10/how-explain-kubernetes-plain-english) How do you explain Kubernetes and orchestration to non-technical people? Listen to the experts
* [medium: How to setup Hetzner load balancer on a Kubernetes cluster](https://medium.com/@jmrobles/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)
* [revistacloudcomputing.com: Los mejores proveedores de Kubernetes](https://www.revistacloudcomputing.com/2020/09/los-mejores-proveedores-de-kubernetes/)
* [Virtual Clusters for Kubernetes — Benefits and Use Cases](https://medium.com/better-programming/virtual-clusters-for-kubernetes-benefits-use-cases-a4eee1c5c5a5) Virtual Kubernetes clusters could be the next driver for Kubernetes adoption.
* [medium: Kubernetes Tip: How Statefulsets Behave Differently Than Deployments When Node Fails? 🌟](https://medium.com/tailwinds-navigator/kubernetes-tip-how-statefulsets-behave-differently-than-deployments-when-node-fails-d29e36bca7d5) What happens to the Pods when a node fails in Kubernetes?
* [thenewstack.io: 4 ways to run kubernetes in production 🌟](https://thenewstack.io/4-ways-to-run-kubernetes-in-production/)
* [linuxtechi.com: How to Setup Private Docker Registry in Kubernetes (k8s)](https://www.linuxtechi.com/setup-private-docker-registry-kubernetes/)
* [Hierarchical namespaces](https://github.com/kubernetes-sigs/multi-tenancy/tree/master/incubator/hnc) make it easier to share your Kubernetes cluster. For example, you can create additional namespaces under your team's namespace, even if you don't have cluster-level permission to create namespaces
* [Our Journey to Zero Downtime Rolling Updates with Ambassador](https://eng.lifion.com/journey-to-zero-downtime-rolling-updates-with-ambassador-badda6a7d450) In this article you will cover: How Kubernetes lifecycle hooks can be used to shutdown applications gracefully. How pods are removed from the system and why it is necessary to understand and carefully handle the shutdown sequence appropriately.
* [k21academy.com: Kubernetes Architecture. An Introduction to Kubernetes Components](https://k21academy.com/docker-kubernetes/kubernetes-architecture-components-overview-for-beginners/)
* [thenewstack.io: How do applications run on kubernetes](https://thenewstack.io/how-do-applications-run-on-kubernetes/)
* [blog.mayadata.io: Kubernetes storage basics: PV, PVC and StorageClass 🌟](https://blog.mayadata.io/kubernetes-storage-basics-pv-pvc-and-storageclass)
* [itnexst.io: Docker and Kubernetes — root vs. privileged](https://itnext.io/docker-and-kubernetes-root-vs-privileged-9d2a37453dec)
* [medium: ConfigMaps in Kubernetes: how they work and what you should remember 🌟](https://medium.com/flant-com/configmaps-in-kubernetes-f9f6d0081dcb)
* [medium: Individual Kubernetes Clusters vs. Shared Kubernetes Clusters for Development](https://medium.com/faun/individual-kubernetes-clusters-vs-shared-kubernetes-clusters-for-development-3399576b0f1f)
* [medium: Kubernetes Multi-Tenancy — A Best Practices Guide 🌟](https://medium.com/faun/kubernetes-multi-tenancy-a-best-practices-guide-88e37ef2b709)
* [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
* [Getting a shell on each node](https://gist.github.com/xandout/8d24558c75c53f3cb8bf0a97ec25fcfc) Learn how you can use a **DaemonSet to expose an SSH shell on each node** of your cluster (even if you don't have SSH installed)
* [medium: Virtual Clusters for Kubernetes — Benefits and Use Cases](https://medium.com/better-programming/virtual-clusters-for-kubernetes-benefits-use-cases-a4eee1c5c5a5) Virtual Kubernetes clusters could be the next driver for Kubernetes adoption
* [devcentral.f5.com: What is Kubernetes?](https://devcentral.f5.com/s/articles/What-is-Kubernetes)
* [docs.google.com: Kubernetes For Everyone 🌟🌟](https://docs.google.com/document/d/1p4ZYQYM2VrMCR8K3T68JOMzWHlV-C8Jogrl9Ces77OA)  A consolidated document on Kubernetes by: Pavan Belagatti
* [blog.sighup.io: Hierarchical Namespace Controller (HNC): a look into the future of Kubernetes Multitenancy](https://blog.sighup.io/an-introduction-to-hierarchical-namespace-controller-hnc/) Hierarchical Namespace Controller (HNC) is bringing a better multi-tenancy model to Kubernetes. In this article we are exploring the current state of the project and useful use-cases.
* [thenewstack.io: Who Needs a Dashboard? Why the Kubernetes Command Line Is Not Enough](https://thenewstack.io/who-needs-a-dashboard-why-the-kubernetes-command-line-is-not-enough/)
* [medium: Discovering Running Pods By Using DNS and Headless Services in Kubernetes](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4)
* [itnext.io: Writing a Kubernetes CLI in Go](https://itnext.io/writing-a-kubernetes-cli-in-go-a3970ad58299)
* [medium: Create a Custom Annotation for the Kubernetes ingress-nginx Controller](https://medium.com/better-programming/creating-a-custom-annotation-for-the-kubernetes-ingress-nginx-controller-444e9d486192)
* [containerjournal.com: Overcoming Kubernetes Infrastructure Challenges](https://containerjournal.com/topics/container-management/overcoming-kubernetes-infrastructure-challenges/)
* [gravitational.com: How to Set Up Kubernetes SSO with SAML](https://gravitational.com/blog/kubernetes-sso-saml/)
* [redhat.com: Kubernetes basics for sysadmins](https://www.redhat.com/sysadmin/kubernetes-basics-sysadmins) Learn when Kubernetes can be effectively used and how the containers it manages might be better than virtual machines.
* [blog.newrelic.com: Kubernetes Fundamentals 🌟](https://blog.newrelic.com/tag/kubernetes-fundamentals/)
  * https://blog.newrelic.com/engineering/kubernetes-request-and-limits/
  * https://blog.newrelic.com/engineering/kubernetes-health-checks/
  * https://blog.newrelic.com/engineering/how-to-use-kubernetes-secrets/
  * https://blog.newrelic.com/engineering/how-to-organize-kubernetes-clusters/
  * https://blog.newrelic.com/engineering/how-to-use-kubernetes-volumes/
* [erkanerol.github.io: I wish pods were fully restartable](https://erkanerol.github.io/post/restartable-pods/) Why are Pod not fully restartable in Kubernetes? Why is Kubernetes not restarting the Pod in CrashLoopBackOff?
* [loginradius.com: Understanding Basics of Kubernetes](https://www.loginradius.com/engineering/blog/understanding-kubernetes/)
* [Kubernetes Horror Stories](https://thenewstack.io/kubernetes-horror-stories/)
* [lambda.grofers.com: Learnings From Two Years of Kubernetes in Production 🌟](https://lambda.grofers.com/learnings-from-two-years-of-kubernetes-in-production-b0ec21aa2814)
* [devopsunlocked.com: Kubernetes: Learning Material 🌟](https://devopsunlocked.com/kubernetes-learning-material/)
* [magalix.com: **Team Productivity: Resource Management** 🌟](https://www.magalix.com/blog/team-productivity-1) Resource Requests, Limits and Quota
* [opensource.com: A beginner's guide to Kubernetes Jobs and CronJobs](https://opensource.com/article/20/11/kubernetes-jobs-cronjobs) Use Jobs and CronJobs to control and manage Kubernetes pods and containers.
* [learnsteps.com: How Kubernetes works on reconciler pattern 🌟](https://www.learnsteps.com/how-kubernetes-works-on-a-reconciler-pattern/)
* [redhat.com: Kubernetes Components - A sysadmin's guide to basic Kubernetes components 🌟](https://www.redhat.com/sysadmin/kubernetes-components) Kubernetes control plane nodes and worker nodes, their features, and how they interact.
* [medium: How Rolling and Rollback Deployments work in Kubernetes](https://medium.com/@yankee.exe/how-rolling-and-rollback-deployments-work-in-kubernetes-8db4c4dce599)
* [medium: Installing cf-for-k8s on a Kubernetes Cluster Running on Digital Ocean](https://medium.com/cloud-foundry-foundation/installing-cf-for-k8s-on-a-kubernetes-cluster-running-on-digitalocean-acffdc652dcf) If you want to install Cloud Foundry on Kubernetes on Digital Ocean, you might find this article relevant.
* [itnext.io: Lessons learned from managing a Kubernetes cluster for side projects (GKE) 🌟](https://itnext.io/lessons-learned-from-managing-a-kubernetes-cluster-for-side-projects-780fbbacf36c)
* [projectcalico.org: Using Kubernetes to orchestrate VMs 🌟](https://www.projectcalico.org/using-kubernetes-to-orchestrate-vms/)
* [cncf.io: Kubernetes 101: An Introduction 🌟](https://www.cncf.io/blog/2020/12/14/kubernetes-101-an-introduction/)
* [millionvisit.blogspot.com: Kubernetes for Developers #1: Kubernetes Architecture and Features 🌟](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-1-kubernetes-architecture.html)
* [lastweekinaws.com: Is ECS deprecated? Has Kubernetes won?](https://www.lastweekinaws.com/blog/reader-mailbag-is-ecs-deprecated/)
* [redhat.com: Start learning Kubernetes from your local machine](https://www.redhat.com/sysadmin/start-learning-kubernetes)
* [medium: Pratyush Mathur - Kubernetes Architecture](https://medium.com/@pratyush.mathur/kubernetes-architecture-82e9bc8324f1)
* [medium: Deployment types in Kubernetes 🌟](https://medium.com/avmconsulting-blog/deployment-types-in-kubernetes-14b70ca7ef93)
* [platform9.com: Difference Between multi-cluster, multi-master, multi-tenant & federated Kubernetes 🌟](https://platform9.com/blog/difference-between-multi-cluster-multi-master-multi-tenant-federated-kubernetes/)
* [opensource.com: 8 Kubernetes insights for 2021 🌟](https://opensource.com/article/21/1/kubernetes) Review the top five Kubernetes articles of 2020, then preview three tools you should learn about in 2021.
* [thoughtbot.com: Zero Downtime Rails Deployments with Kubernetes](https://thoughtbot.com/blog/zero-downtime-rails-deployments-with-kubernetes)
* [medium: Kubernetes Resources 🌟](https://medium.com/@pratyush.mathur/kubernetes-resources-c09d172dbdc5)
* [medium: Notes on Graceful Shutdown in Kubernetes 🌟](https://medium.com/@pleasingsmoke/graceful-shutdown-of-pods-in-kubernetes-6da5588b5356)
* [loft.sh: Kubernetes Readiness Probes - Examples & Common Pitfalls 🌟](https://loft.sh/blog/kubernetes-readiness-probes-examples-common-pitfalls/)
* [srcco.de: Many Kubernetes Clusters instead of 1 huge cluster 🌟](https://srcco.de/posts/many-kubernetes-clusters.html)
* [engineering.salesforce.com: Project Agumbe: Share Objects Across Namespaces in Kubernetes 🌟](https://engineering.salesforce.com/project-agumbe-share-objects-across-namespaces-in-kubernetes-1fc2e1ddb3eb)
* [didil.medium.com: Building a Kubernetes Mutating Admission Webhook](https://didil.medium.com/building-a-kubernetes-mutating-admission-webhook-7e48729523ed) A “magic” way to inject a file into Pod Containers
* [platform9.com: The Gorilla Guide to Kubernetes in the Enterprise 🌟](https://platform9.com/lp/ultimate-guide-enterprise-kubernetes/) Discover key capabilities for Kubernetes at scale. 
    * A complete Enterprise Kubernetes infrastructure needs proper DNS, load balancing, Ingress, stateful services, K8’s role-based access control (RBAC), integration with LDAP and authentication systems, and more. Once Kubernetes is deployed, day-2 operational challenges and life-cycle management comes into play: monitoring, alerting, troubleshooting, upgrades, security patching, compliance checking and much more.
    * The Gorilla guide to Kubernetes in the Enterprise is your resource to ensure the success of your Enterprise Kubernetes projects by thinking through critical decisions around deployment options, day-2 operational considerations, use cases, and choosing your Kubernetes implementation solutions.
* [thenewstack.io: A Deep Dive into Architecting a Kubernetes Infrastructure 🌟](https://thenewstack.io/a-deep-dive-into-architecting-a-kubernetes-infrastructure/)
* [thenewstack.io: Manage Multicluster Kubernetes with Operators](https://thenewstack.io/manage-multicluster-kubernetes-with-operators/)
* [kubernetes.io: Out of the Clouds onto the Ground: How to Make Kubernetes Production Grade Anywhere 🌟](https://kubernetes.io/blog/2018/08/03/out-of-the-clouds-onto-the-ground-how-to-make-kubernetes-production-grade-anywhere/)
* [opensourcerers.org: How to go from Docker to Kubernetes the right way 🌟](https://www.opensourcerers.org/2021/02/01/how-to-go-from-docker-to-kubernetes-the-right-way/)
* [magalix.com: Influencing Kubernetes Scheduler Decisions](https://www.magalix.com/blog/influencing-kubernetes-scheduler-decisions) To ensure maximum possible performance and availability given the infrastructure at hand, the scheduler uses complex algorithms to ensure the most efficient Pod placement. In this article, we discuss how the scheduler selects the best node to host the Pod and how we can influence its decision.
* [openshift.com: The Hidden Dangers of Terminating Namespaces 🌟](https://www.openshift.com/blog/the-hidden-dangers-of-terminating-namespaces)
* [learndevops.substack.com: Hitting prometheus API with curl and jq 🌟](https://learndevops.substack.com/p/hitting-prometheus-api-with-curl) Determine offending pods that use more RAM than requested, causing OOM, with Prometheus and jq.
* [nginx.com: Reduce Complexity with Production-Grade Kubernetes](https://www.nginx.com/blog/reduce-complexity-with-production-grade-kubernetes/)
* [medium: Making Sense of Taints and Tolerations in Kubernetes](https://medium.com/kubernetes-tutorials/making-sense-of-taints-and-tolerations-in-kubernetes-446e75010f4e)
* [ronaknathani.com: How a Kubernetes Pod Gets an IP Address](https://ronaknathani.com/blog/2020/08/how-a-kubernetes-pod-gets-an-ip-address/)
* [medium: ConfigMaps in Kubernetes (K8s)](https://medium.com/faun/configmaps-in-kubernetes-k8s-2f2ce79d7e66)
* [devopscube.com: 10 Key Considerations for Kubernetes Cluster Design & Setup 🌟](https://devopscube.com/key-considerations-kubernetes-cluster-design-setup/)
* [sysdig.com: Kubernetes admission controllers in 5 minutes](https://sysdig.com/blog/kubernetes-admission-controllers/)
* [blog.pixielabs.ai: Building Kubernetes Native SaaS applications: iterating quickly by deploying in-cluster data planes](https://blog.pixielabs.ai/hybrid-architecture/hybrid-architecture/)
* [datacenterknowledge.com: The Pros and Cons of Kubernetes-Based Hybrid Cloud 🌟](https://www.datacenterknowledge.com/cloud/pros-and-cons-kubernetes-based-hybrid-cloud) 
* [itnext.io: CKS Exam Series #9 RBAC v2](https://itnext.io/cks-exam-series-9-rbac-v2-23ee24dd77cd) Kubernetes CKS Example Exam Question Series
* [dzone: Scale to Zero With Kubernetes with KEDA and/or Knative 🌟](https://dzone.com/articles/scale-to-zero-with-kubernetes) This article reviews how Kubernetes provides the platform capabilities for dynamic deployment, scaling, and management in Cloud-native applications.
* [elastisys.com: What do I need to add on top of Kubernetes?](https://elastisys.com/what-do-i-need-to-add-on-top-of-kubernetes/)
* [infoq.com: Experts Discuss Top Kubernetes Trends and Production Challenges](https://www.infoq.com/articles/kubernetes-trends-and-challenges/)
* [zhimin-wen.medium.com: Sticky Sessions in Kubernetes 🌟](https://zhimin-wen.medium.com/sticky-sessions-in-kubernetes-56eb0e8f257d)
* [maximilianmichels.com: Kubernetes in a Nutshell: 10 Things You Need to Know](https://maximilianmichels.com/2021/kubernetes-what-you-need-to-know/)
* [vamsitalkstech.com: Introduction to Kubernetes Multi-tenancy..(1/2)](https://www.vamsitalkstech.com/architecture/a-deepdive-into-kubernetes-multitenancy-1-2/)
* [vamsitalkstech.com: Kubernetes Multi-tenancy Best Practices & Architecture Model..(2/2)](https://www.vamsitalkstech.com/architecture/kubernetes-multitenancy-best-practices-architecture-models-2-2/)
* [itnext.io: Breaking down and fixing etcd cluster](https://itnext.io/breaking-down-and-fixing-etcd-cluster-d81e35b9260d)
* [brennerm.github.io: Kubernetes Overview Diagrams 🌟](https://brennerm.github.io/posts/kubernetes-overview-diagrams.html#architecture)
* [blog.appstack.one: How to run Ghost blog inside Kubernetes](https://blog.appstack.one/how-to-run-ghost-blog-inside-kubernetes/)
* [If you have a livenessProbe that takes over one second, it’ll fail when you update to kubernetes 1.20, because a long-standing bug with how the default was handled has been fixed. You must override the ExecProbeTimeout if your probe takes more than 1s](https://github.com/kubernetes/kubernetes/pull/97057)
* [thenewstack.io: Kubernetes Is Not Just About Containers — It’s About the API 🌟](https://thenewstack.io/kubernetes-is-not-just-about-containers-its-about-the-api/)
* [dzone refcard: Advanced kubernetes 🌟](https://dzone.com/refcardz/advanced-kubernetes)
* [dzone refcard: Kubernetes Multi-Cluster Management and Governance 🌟](https://dzone.com/refcardz/kubernetes-multi-cluster-management-and-governance)
* [tech2fun.net: Using Service Endpoints and Alias for accessing External Service in K8s](https://tech2fun.net/using-k8s-service-resource-for-enabling-clients-discovering-talking-to-pods/)
* [learnk8s.io: Scaling Celery workers with RabbitMQ on Kubernetes 🌟](https://learnk8s.io/scaling-celery-rabbitmq-kubernetes) In this article, you will explore how to use Kubernetes and KEDA to scale Celery workers based on the number of messages in a RabbitMQ queue.
    1. Learn how to set up a metrics pipeline
    2. How you can drive autoscaling based on metrics from RabbitMQ.
    3. Why KEDA might be an alternative to prometheus+adapters
* [cloudsavvyit.com: How Does Kubernetes Work?](https://www.cloudsavvyit.com/10110/how-does-kubernetes-work/)
* [github.com/PacktPublishing: Kubernetes in Production Best Practices](https://github.com/PacktPublishing/Kubernetes-in-Production-Best-Practices)
* [arabitnetwork.com: K8S – Enabling Auditing Logs | Step-by-Step](https://arabitnetwork.com/2021/03/13/k8s-enabling-auditing-logs-step-by-step/)
* [thenewstack.io: Kubernetes Lifecycle Management! So Important! (Day 0, Day 1, Day 2) 🌟](https://thenewstack.io/kubernetes-lifecycle-management-so-important-what-does-it-mean)
* [kruyt.org: Migrate from Docker to Containerd in Kubernetes](https://kruyt.org/migrate-docker-containerd-kubernetes)
* [lemoncode.net: Hola Kubernetes: Definiciones 🌟](https://lemoncode.net/lemoncode-blog/2021/3/17/hola-kubernetes-definiciones)
* [superuser.openstack.org: Run Your Kubernetes Cluster on OpenStack in Production](https://superuser.openstack.org/articles/run-your-kubernetes-cluster-on-openstack-in-production/)
* [medium: How to deploy StatefulSets in Kubernetes (K8s)?](https://medium.com/avmconsulting-blog/deploying-statefulsets-in-kubernetes-k8s-5924e701d327)
* [sandeepbaldawa.medium.com: K8s Labels & Selectors 🌟](https://sandeepbaldawa.medium.com/k8s-labels-selectors-9ad2fcf78a4e) In this post, we will look at What Kubernetes(K8s) Labels and Selectors are, Why do we need them, How to use them.
* [developers.redhat.com: Using Dekorate to generate Kubernetes manifests for Java applications 🌟](https://developers.redhat.com/blog/2021/03/17/using-dekorate-to-generate-kubernetes-manifests-for-java-applications/)
    * [dekorate.io 🌟](http://dekorate.io/)
* [thenucleargeeks.com: Introduction to Kubernetes Pods](https://thenucleargeeks.com/2021/03/22/introduction-to-pods-in-kubernetes/)
* millionvisit.blogspot.com: Kubernetes for Developers Journey 🌟:
    * [millionvisit.blogspot.com: Kubernetes for Developers #1: Kubernetes Architecture and Features](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-1-kubernetes-architecture.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #2: Kubernetes for Local Development](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-2-Local-development.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #3: kubectl CLI](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-3-kubectl-cli.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #4: Enable kubectl bash autocompletion](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-4-kubectl-autocompletion.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #5: Kubernetes Web UI Dashboard](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-5-webui-dashboard.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #6: Kubernetes Objects](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-6-KubernetesObjects.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #7: Imperative vs. Declarative Kubernetes Objects](http://millionvisit.blogspot.com/2021/01/kubernetes-for-developers-7-imperative-vs-Declarative.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #8: Kubernetes Object Name, Labels, Selectors and Namespace](http://millionvisit.blogspot.com/2021/02/kubernetes-for-developers-8-Object%20Name-Labels-Selectors-Namespace.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #9: Kubernetes Pod Lifecycle](http://millionvisit.blogspot.com/2021/03/kubernetes-for-developers-9-Kubernetes-Pod-Lifecycle.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #10: Kubernetes Pod YAML manifest in-detail ](http://millionvisit.blogspot.com/2021/03/kubernetes-for-developers-10-kubernetes-Pod-YAML-manifest.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #11: Pod Organization using Labels](http://millionvisit.blogspot.com/2021/03/kubernetes-for-developers-11-pod-organization-using-labels.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #12: Effective way of using K8 Liveness Probe](http://millionvisit.blogspot.com/2021/04/kubernetes-for-developers-12-effective-way-of-using-k8-liveness-probe.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #13: Effective way of using K8 Readiness Probe](http://millionvisit.blogspot.com/2021/04/kubernetes-for-developers-13-effective-way-of-using-k8-readiness-probe.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #14: Kubernetes Deployment YAML manifest in-detail 🌟](http://millionvisit.blogspot.com/2021/05/kubernetes-for-developers-14-Kubernetes-Deployment-YAML-manifest.html)
* [thenewstack.io: Scaling Microservices on Kubernetes 🌟](https://thenewstack.io/scaling-microservices-on-kubernetes)
* [andrewlock.net: Series: Deploying ASP.NET Core applications to Kubernetes 🌟](https://andrewlock.net/series/deploying-asp-net-core-applications-to-kubernetes/)
    * [andrewlock.net: Deploying ASP.NET Core applications to Kubernetes - Part 6 - Adding health checks with Liveness, Readiness, and Startup probes 🌟](https://andrewlock.net/deploying-asp-net-core-applications-to-kubernetes-part-6-adding-health-checks-with-liveness-readiness-and-startup-probes/)
* [infoq.com: The Evolution of Distributed Systems on Kubernetes](https://www.infoq.com/articles/distributed-systems-kubernetes)
* [cloud.ibm.com: Tutorial - Scalable webapp 🌟](https://cloud.ibm.com/docs/solution-tutorials?topic=solution-tutorials-scalable-webapp-kubernetes)
* [hackernoon.com: The Ultimate Beginners Guide To Kubernetes and Container Orchestration](https://hackernoon.com/the-ultimate-beginners-guide-to-kubernetes-and-container-orchestration-5d83354y)
* [thenucleargeeks.com: Taints and Tolerations in Kubernetes](https://thenucleargeeks.com/2021/03/28/taints-and-tolerations-in-kubernetes/)
* [fosstechnix.com: Rolling out and Rolling back updates with Zero Downtime on Kubernetes Cluster 🌟](https://www.fosstechnix.com/rolling-out-and-rolling-back-updates-with-zero-downtime-on-kubernetes-cluster/)
* [rcarrata.github.io: Regenerating Kubeconfig for system:admin user in OpenShift clusters 🌟](https://rcarrata.github.io/openshift/regenerate-kubeconfig/) You missed your kubeconfig file of your OpenShift cluster? Your dog ate your kubeconfig file? No worries! Let’s regenerate it in a easy and automated way!
* [medium: Kubernetes — Difference between Deployment and StatefulSet in K8s](https://medium.com/devops-mojo/kubernetes-difference-between-deployment-and-statefulset-in-k8s-deployments-vs-statefulsets-855f9e897091)
* [medium: Jobs & Cronjobs in Kubernetes Cluster](https://medium.com/avmconsulting-blog/jobs-cronjobs-in-kubernetes-cluster-d0e872e3c8c8)
* [devopscube.com: How To Create Kubernetes Jobs/Cron Jobs – Getting Started Guide](https://devopscube.com/create-kubernetes-jobs-cron-jobs/)
* [speakerdeck.com: Kubernetes Pod internals with the fundamentals of Containers 🌟](https://speakerdeck.com/devinjeon/kubernetes-pod-internals-with-the-fundamentals-of-containers)
* [thenewstack.io: Avoiding the Pitfalls of Multitenancy in Kubernetes](https://thenewstack.io/avoiding-the-pitfalls-of-multitenancy-in-kubernetes/)
* [zhimin-wen.medium.com: Sticky Sessions in Kubernetes](https://zhimin-wen.medium.com/sticky-sessions-in-kubernetes-56eb0e8f257d)
* [medium: Graceful shutdown of fpm and nginx in Kubernetes](https://medium.com/inside-personio/graceful-shutdown-of-fpm-and-nginx-in-kubernetes-f362369dff22)
* [medium: Kubernetes Fundamentals For Absolute Beginners: Architecture & Components](https://medium.com/the-programmer/kubernetes-fundamentals-for-absolute-beginners-architecture-components-1f7cda8ea536)
* [bsucaciu.com: What is a Sidecar?](https://www.bsucaciu.com/architecture/what-is-a-sidecar/)
* [thenewstack.io: Scaling Microservices on Kubernetes 🌟](https://thenewstack.io/scaling-microservices-on-kubernetes/)
* [fairwinds.com: Over-Provisioned and Over-Permissioned Containers & Kubernetes](https://www.fairwinds.com/blog/over-provisioned-and-over-permissioned-containers-kubernetes)
* [learn.hashicorp.com: Integrate a Kubernetes Cluster with an External Vault 🌟](https://learn.hashicorp.com/tutorials/vault/kubernetes-external-vault)
* [kubernetes.io: PodSecurityPolicy Deprecation: Past, Present, and Future 🌟](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
* [betterprogramming.pub: How to Implement Your Distributed Filesystem With GlusterFS And Kubernetes](https://betterprogramming.pub/how-to-implement-your-distributed-filesystem-with-glusterfs-and-kubernetes-83ee7f5f834f) Learn the advantages of using GlusterFS and how can it help in achieving a highly-scalable, distributed filesystem.
* [compliantkubernetes.io: Compliant Kubernetes is a Certified Kubernetes distribution, that complies with: HIPAA, GDPR, PCI DSS, FFFS 2014:7, ISO 27001, etc. 🌟](https://compliantkubernetes.io)
* [blog.gopaddle.io: Strange things you never knew about Kubernetes ConfigMaps on day one 🌟🌟](https://blog.gopaddle.io/2021/04/01/strange-things-you-never-knew-about-kubernetes-configmaps-on-day-one/)
* [medium: Scaling Kubernetes with Assurance at Pinterest](https://medium.com/pinterest-engineering/scaling-kubernetes-with-assurance-at-pinterest-a23f821168da)
* [platform9.com: Kubernetes Cluster Sizing – How Large Should a Kubernetes Cluster Be? 🌟](https://platform9.com/blog/kubernetes-cluster-sizing-how-large-should-a-kubernetes-cluster-be/)
* [learnsteps.com: What is a control plane? Basics on Kubernetes](https://www.learnsteps.com/what-is-a-control-plane-what-do-people-mean-by-this-basics-on-kubernetes/)
* [infoworld.com: No one wants to manage Kubernetes anymore 🌟](https://www.infoworld.com/article/3614850/no-one-wants-to-manage-kubernetes-anymore.html) The availability of solid and varied managed kubernetes options has seen more and more companies shy away from managing their own clusters. 
* [dzone: Introduction To Kubernetes 🌟](https://dzone.com/articles/introduction-to-kubernetes-part-1) An orchestration tool takes care of provisioning and deployment, allocation of resources, load balancing, and many other important aspects of any system.
* [fairwinds.com: Never Should You Ever In Kubernetes: #1 Do K8S The Hard Way](https://www.fairwinds.com/blog/never-should-you-ever-in-kubernetes-1-do-k8s-the-hard-way)
* [blog.flant.com: How we enjoyed upgrading a bunch of Kubernetes clusters from v1.16 to v1.19](https://blog.flant.com/how-we-enjoyed-upgrading-kubernetes-clusters-from-v1-16-to-v1-19/)
* [eximiaco.tech: when to choose Kubernetes? 🌟](https://www.eximiaco.tech/en/2020/06/03/3-facts-to-consider-before-adopting-kubernetes/)
* [kubernetes.io: Three Tenancy Models For Kubernetes 🌟](https://kubernetes.io/blog/2021/04/15/three-tenancy-models-for-kubernetes/) What are your tenancy options with Kubernetes? This post calls out three: by namespace, by cluster, by control plane.
* [thenewstack.io: Living with Kubernetes: Cluster Upgrades 🌟](https://thenewstack.io/living-with-kubernetes-cluster-upgrades/)
* [openshift.com: Topology Aware Scheduling in Kubernetes Part 1: The High Level Business Case](https://www.openshift.com/blog/topology-aware-scheduling-in-kubernetes-part-1-the-high-level-business-case)
    * [openshift.com: Topology Awareness in Kubernetes Part 2: Don’t we already have a Topology Manager?](https://www.openshift.com/blog/topology-awareness-in-kubernetes-part-2-dont-we-already-have-a-topology-manager)
* [Kubernetes setup with CRI-O Runtime](https://github.com/msfidelis/kubernetes-with-cri-o) Example to build Kubernetes Clusters using CRI-O runtime instead of Docker
* [kubernetes.io: Graceful Node Shutdown Goes Beta 🌟](https://kubernetes.io/blog/2021/04/21/graceful-node-shutdown-beta/)
* [blog.min.io: Kubernetes, Consistency and Commoditization - The Way of the Cloud](https://blog.min.io/the_way_of_the_cloud/)
* [hjrocha.medium.com: Add a Custom Host to Kubernetes](https://hjrocha.medium.com/add-a-custom-host-to-kubernetes-a06472cedccb)
* [rancher.com: The Three Pillars of Kubernetes Container Orchestration 🌟](https://rancher.com/three-pillars-kubernetes-container-orchestration)
* [qwinix.io: What Is Kubernetes? K8s Uses, Benefits, & More](https://www.qwinix.io/blog-what-is-kubernetes/)
* [thenewstack.io: Governance, Risk and Compliance with Kubernetes](https://thenewstack.io/governance-risk-and-compliance-with-kubernetes/)
* [itnext.io: Kubernetes Probes: Startup, Liveness, Readiness 🌟](https://itnext.io/kubernetes-probes-startup-liveness-readiness-a9fc9ccff4b2)
* [containerjournal.com: Best of 2020: How Docker and Kubernetes Work Together](https://containerjournal.com/topics/container-ecosystems/how-docker-and-kubernetes-work-together/)
* [zhimin-wen.medium.com: Custom Notifications with Alert Manager’s Webhook Receiver in Kubernetes](https://zhimin-wen.medium.com/custom-notifications-with-alert-managers-webhook-receiver-in-kubernetes-8e1152ba2c31)
* [harness.io: Introducing Recommendations API: Find Potential Cost Savings Programmatically](https://harness.io/blog/product-updates/recommendations-api/)
* [blog.harbur.io: Demystifying stateful apps on Kubernetes by deploying an etcd cluster](https://blog.harbur.io/demystifying-stateful-apps-on-kubernetes-by-deploying-an-etcd-cluster-b85bf8c16fea) In this tutorial you will learn how to deploy an etcd cluster in Kubernetes
* [blog.kintone.io: Rebooting a LOT of Kubernetes nodes in a declarative way](https://blog.kintone.io/entry/2021/01/14/160935)
* [ithands-on.com: Kubernetes 101 : Performing tasks in kubernetes - Jobs](https://www.ithands-on.com/2021/05/kubernetes-101-performing-tasks-in.html)
* [ithands-on.com: Kubernetes 101 : Deployments, replicaSets, services, pods and endpoints](https://www.ithands-on.com/2021/05/kubernetes-101-deployment-replicasets.html)
* [ithands-on.com: Kubernetes 101 : Changing a Pod's label on the fly](https://www.ithands-on.com/2021/04/kubernetes-101-changing-pods-label-on.html)
* [ithands-on.com: Kubernetes 101 : An overview of StatefulSets and Deployments](https://www.ithands-on.com/2021/05/kubernetes-101-overview-of-statefulsets.html)
* [ithands-on.com: Kubernetes 101 : Resource Quotas (ResourceQuota) and Limit Ranges (LimitRange)](https://www.ithands-on.com/2021/05/kubernetes-101-resource-quotas.html)
* [ithands-on.com: Kubernetes 101 : Deployments and Rolling updates - maxSurge, maxUnavailable](https://www.ithands-on.com/2021/06/kubernetes-101-deployments-and-rolling.html)
* [ithands-on.com: Kubernetes 101 : The externalName service](https://www.ithands-on.com/2021/06/kubernetes-101-externalname-service.html)
* [infoworld.com: How Kubernetes works](https://www.infoworld.com/article/3617008/how-kubernetes-works.html) If you want to understand containers, microservices architecture, modern application development, and cloud native computing, you need to understand Kubernetes.
* [infoq.com: Cloud Native and Kubernetes Observability: Expert Panel](https://www.infoq.com/articles/cloud-native-observability/)
* [kubernetes.io: Don't Panic: Kubernetes and Docker](https://kubernetes.io/blog/2020/12/02/dont-panic-kubernetes-and-docker/)
* [thenewstack.io: Exploring the New Kubernetes Maturity Model](https://thenewstack.io/exploring-the-new-kubernetes-maturity-model/)
* [blog.bandowski.eu: Tools that should be used in every Kubernetes cluster 🌟](https://blog.bandowski.eu/tools-that-should-be-used-in-every-kubernetes-cluster-38969ed3e603) 
    * [ArgoCD](https://argoproj.github.io/) for deploying your resources the GitOps way
    * [MetalLB](https://metallb.universe.tf/) in case you need a load balancer when running Kubernetes on-prem and not in a cloud
    * [external-secrets](https://github.com/external-secrets/kubernetes-external-secrets) to easily sync the secrets of your external secret manager with your Kubernetes cluster
    * [cert-manager](https://cert-manager.io/) to easily retrieve and/or generate new certificates on the fly
    * [external-dns](https://github.com/kubernetes-sigs/external-dns) to manage your DNS entries automatically
* [redhat.com: Building containers by hand: The PID namespace](https://www.redhat.com/sysadmin/pid-namespace) The PID namespace is an important one when it comes to building isolated environments. Find out why and how to use it.
* [cncf.io: Simplifying multi-clusters in Kubernetes](https://www.cncf.io/blog/2021/04/12/simplifying-multi-clusters-in-kubernetes/)
* [infoq.com: The Kubernetes Effect](https://www.infoq.com/articles/kubernetes-effect/)
* [dustinspecker.com: iptables: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/iptables-how-kubernetes-services-direct-traffic-to-pods/)
* [dustinspecker.com: Scaling Kubernetes Pods using Prometheus Metrics 🌟](https://dustinspecker.com/posts/scaling-kubernetes-pods-prometheus-metrics/) one of Kubernetes many features is auto-scaling workloads. Typically, Horizontal Pod Autoscalers scale pods based on CPU or memory usage. During other times we could better scale by using custom metrics that Prometheus is already scraping. Fortunately, Horizontal Pod Autoscalers can support using custom metrics. I’m a fan of the [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) project, but it wasn’t apparent how to set up a Horizontal Pod Autoscaler using custom metrics. This post walks through:
    * Deploying kube-prometheus (Prometheus operator, Prometheus adapter, Grafana, and more)
    * Creating a custom metrics APIService
    * Configuring Prometheus adapter to support our custom metrics
    * Deploying a Horizontal Pod Autoscaler for Grafana using a custom metric
* [dustinspecker.com: IPVS: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/ipvs-how-kubernetes-services-direct-traffic-to-pods/)
* [dev.to: How to switch container runtime in a Kubernetes cluster](https://dev.to/stack-labs/how-to-switch-container-runtime-in-a-kubernetes-cluster-1628)
* [digizoo.com.au: How to Master Admission Webhooks In Kubernetes (GKE) (Part One)](https://digizoo.com.au/1376/mastering-admission-webhooks-in-kubernetes-gke-part-1/) Admission webhooks are HTTP callbacks that receive admission requests (for resources in a K8s cluster) and do something with them. You can define two types of admission webhooks, validating admission webhook and mutating admission webhook. 
* [asonisg.medium.com: Multi-tenancy with Kubernetes (Part-1)](https://asonisg.medium.com/multi-tenancy-with-kubernetes-part-1-8ac4e5083e31)
* [infoq.com: The Evolution of Distributed Systems on Kubernetes](https://www.infoq.com/articles/distributed-systems-kubernetes/)
* [itnext.io: Breaking down and fixing etcd cluster](https://itnext.io/breaking-down-and-fixing-etcd-cluster-d81e35b9260d)
* [learnsteps.com: Basics on Kubernetes: What exactly is a deployment?](https://www.learnsteps.com/basics-on-kubernetes-what-exactly-is-a-deployment/)
* [itnext.io: Kubernetes: what are Endpoints](https://itnext.io/kubernetes-what-are-endpoints-3cc9e769b614)
* [medium.com: Using kubernetes custom resources to manage our ephemeral environments](https://medium.com/beamdental/using-kubernetes-custom-resources-to-manage-our-ephemeral-environments-f298610893e1) Building a Kubernetes operator with **kubebuilder** to manage ephemeral environments.
* [medium: Running Apache Flink on Kubernetes](https://medium.com/empathyco/running-apache-flink-on-kubernetes-10815a26559e)
* [learnsteps.com: How exactly kube-proxy works: Basics on Kubernetes](https://www.learnsteps.com/how-exactly-kube-proxy-works-basics-on-kubernetes/)
* [kubernetes.io: Annotating Kubernetes Services for Humans 🌟](https://kubernetes.io/blog/2021/04/20/annotating-k8s-for-humans/) A Convention for annotations in Kubernetes.
* [medium.com: Connect services across Kubernetes clusters using Teleproxy](https://medium.com/flare-systems/connect-services-across-kubernetes-clusters-using-teleproxy-3f317cfd8da) [Teleproxy](https://github.com/flared/teleproxy) is a shell script that lets you quickly replace a Kubernetes deployment by a single pod that forwards incoming traffic to another pod running in a destination Kubernetes cluster.
* [medium: Kubernetes DNS for Services and Pods](https://medium.com/kubernetes-tutorials/kubernetes-dns-for-services-and-pods-664804211501)
* [edgehog.blog: Getting Started with K8s: Core Concepts](https://edgehog.blog/getting-started-with-k8s-core-concepts-135fb570462e)
* [itnext.io: Working with kubernetes configmaps, part 1: volume mounts](https://itnext.io/working-with-kubernetes-configmaps-part-1-volume-mounts-f0ace283f5aa)
    * [itnext.io: Working with kubernetes configmaps, part 2: Watchers](https://itnext.io/working-with-kubernetes-configmaps-part-2-watchers-b6dd0e583d71)
* [talos-systems.com: Is Vanilla Kubernetes Really Too Heavy For The Raspberry Pi?]()
* [infoq.com: Kubernetes Workloads in the Serverless Era: Architecture, Platforms, and Trends](https://www.infoq.com/articles/kubernetes-workloads-serverless-era/)
* [blog.kintone.io: Tolerating failures in container image registries](https://blog.kintone.io/entry/neco-registry) This article will show you several ways to ensure your Kubernetes clusters can always pull images even while an upstream registry is failing.
* [blog.px.dev: How etcd works and 6 tips to keep in mind](https://blog.px.dev/etcd-6-tips/)
* [containerjournal.com: Kubernetes’ True Superpower is its Control Plane](https://containerjournal.com/kubeconcnc/kubernetes-true-superpower-is-its-control-plane/)
* [itnext.io: Kubernetes Readiness Probes — Examples & Common Pitfalls](https://itnext.io/kubernetes-readiness-probes-examples-common-pitfalls-136e3a9a058d)
* [k21academy.com: Kubernetes ConfigMaps and Secrets: Guide to Create and Update 🌟](https://k21academy.com/docker-kubernetes/configmaps-secrets/)  
* [dev.to: A Deep Dive Into Kubernetes Schema Validation](https://dev.to/datreeio/a-deep-dive-into-kubernetes-schema-validation-39ll)
* [tremolosecurity.com: Pipelines and Kubernetes Authentication](https://www.tremolosecurity.com/post/pipelines-and-kubernetes-authentication) The Right Way To Authenticate to Your Clusters From Your CI/CD Pipelines:
    * Don't use ServiceAccount tokens outside of your cluster
    * Create service accounts inside of your authentication identity provider, assign RBAC privileges
    * Easy with Okta and OpenUnison
* [usepine.com: Improving cert-manager HTTP01 self-check speed](https://www.usepine.com/blog/en/improving-cert-manager-self-check-speed-when-issuing-certificates/) This post describes how to improve cert-manager self-check speed, by pointing the cluster to Google nameservers, and disabling DNS caching
* [talkingquickly.co.uk: Kubernetes Single Sign On - A detailed guide 🌟](http://www.talkingquickly.co.uk/kubernetes-sso-a-detailed-guide)
* [datree.io: A Deep Dive Into Kubernetes Schema Validation 🌟](https://www.datree.io/resources/kubernetes-schema-validation)
* [community.suse.com: Stupid Simple Kubernetes — Deployments, Services and Ingresses Explained](https://community.suse.com/posts/stupid-simple-kubernetes-deployments-services-and-ingresses-explained)
* [elastisys.com: PCI DSS compliance in Kubernetes-based platforms](https://elastisys.com/pci-dss-compliance-in-kubernetes-based-platforms/)
* [infracloud.io: Avoiding Kubernetes Cluster Outages with Synthetic Monitoring](https://www.infracloud.io/blogs/avoiding-kubernetes-cluster-outages-synthetic-monitoring/) Synthetic monitoring consists of pre-defined checks to proactively monitor the critical elements in your infrastructure. These checks simulate the functionality of the elements. We can also simulate the communication between the elements to ensure end-to-end connectivity. Continuous monitoring of these checks also helps to measure overall performance in terms of availability and response times.
* [linkedin.com/pulse: What are Kubernetes Persistent Volumes?](https://www.linkedin.com/pulse/what-kubernetes-persistent-volumes-gyan-prakash-1f/)
* [talos-systems.com: Is Vanilla Kubernetes Really Too Heavy For The Raspberry Pi?](https://www.talos-systems.com/blog/is-vanilla-kubernetes-really-too-heavy-for-the-raspberry-pi/)
* [towardsdatascience.com: Kubernetes 101: Cluster Architecture](https://towardsdatascience.com/kubernetes-101-cluster-architecture-d79995785563) They say a picture is worth a thousand (or a million) words
* [blog.kintone.io: Tolerating failures in container image registries 🌟](https://blog.kintone.io/entry/neco-registry)
* [thenucleargeeks.com: Taints and Tolerations in Kubernetes](https://thenucleargeeks.com/2021/06/26/taints-and-tolerations-in-kubernetes-edit/)
* [humanitec.com: Benchmark your Kubernetes setup against 500+ other teams and find out how well (or not) you are doing](https://humanitec.com/kubernetes-team-setup-test)

<center>
[![Kubernetes architecture](images/kubernetes-pod-creation.png)](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)

[![10 most common mistakes](images/10_common_kubernetes_mistakes.jpg){: style="width:60%"}](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s)

[![5 Open-source projects that make #Kubernetes even better](images/five-oss-projects-kubernetes.jpg){: style="width:80%"}](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve)

[![kubernetes arch multicloud hybrid](images/kubernetes_architecture_multicloud_hybride.jpg){: style="width:70%"}](https://www.journaldunet.com/web-tech/cloud/1492047-comment-kubernetes-perce-les-frontieres-du-cloud/)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Can you change an application without changing any code in Kubernetes?<br><br>You can when you use multiple containers in a single Pod.<br><br>Here’s a visual recap of <a href="https://twitter.com/EmanuelMEvans?ref_src=twsrc%5Etfw">@EmanuelMEvans</a> ’s article on extending apps on Kubernetes with multi-container pods <a href="https://t.co/afS3pPj4zb">https://t.co/afS3pPj4zb</a> <a href="https://t.co/LS5zOZErbE">pic.twitter.com/LS5zOZErbE</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1366373443780808707?ref_src=twsrc%5Etfw">March 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
<br/>

### Kubernetes API
- [kubernetes.io: Kubernetes API 🌟](https://kubernetes.io/docs/reference/kubernetes-api/)
- [thenewstack.io: Living with Kubernetes: API Lifecycles and You](https://thenewstack.io/living-with-kubernetes-api-lifecycles-and-you/)
- [blog.tilt.dev: Kubernetes is so Simple You Can Explore it with Curl](https://blog.tilt.dev/2021/03/18/kubernetes-is-so-simple.html)

### Kubernetes Releases
* [sysdig.com: What’s new in Kubernetes 1.20?](https://sysdig.com/blog/whats-new-kubernetes-1-20/)
* [magalix: What You Should Know about Kubernetes 1.20](https://www.magalix.com/blog/what-you-should-know-about-kubernetes-1.20)
* [towardsdatascience.com: Kubernetes is deprecating Docker in the upcoming release](https://towardsdatascience.com/kubernetes-is-deprecating-docker-in-the-upcoming-release-2a03d607934a) Kubernetes and Docker will part ways; what does that mean to you?
* [zdnet.com: Kubernetes dropping Docker is not that big of a deal](https://www.zdnet.com/article/kubernetes-dropping-docker-is-not-that-big-of-a-deal/) Chill, people. Your Docker skills haven't suddenly become useless. Here's what's really going on.
* [thenewstack.io: Kubernetes 1.20 Lands with 44 Enhancements](https://thenewstack.io/kubernetes-1-20-lands-with-44-enhancements/)
* [thenewstack.io: Kubernetes 1.20 Enhances the Operator Experience and Brings New Features to the Container Runtime](https://thenewstack.io/kubernetes-1-20-enhances-the-operator-experience-and-brings-new-features-to-the-container-runtime/)
* [openshift.com: Kubernetes is Removing Docker Support, Kubernetes is Not Removing Docker Support](https://www.openshift.com/blog/kubernetes-is-removing-docker-support-kubernetes-is-not-removing-docker-support)
* [sysdig.com: What’s new in Kubernetes 1.21?](https://sysdig.com/blog/whats-new-kubernetes-1-21/)
* [devopscube.com: Kubernetes v1.21 Released: Here is What you should know](https://devopscube.com/kubernetes-v1-21-released/)
* [thenewstack.io: Kubernetes 1.21 Brings a New Memory Manager, More Flexible Scheduling](https://thenewstack.io/kubernetes-1-21-brings-a-new-memory-manager-more-flexible-scheduling/)
* [kubernetes.io: kubernetes 1.21: CronJob Reaches GA](https://kubernetes.io/blog/2021/04/09/kubernetes-release-1.21-cronjob-ga/)
* [kubernetes.io: Kubernetes 1.21: Power to the Community](https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/)
* [devclass.com: Kubernetes 1.21 unloads pod security, adds dual IPv4/IPv6 networking, and shuts down gracefully](https://devclass.com/2021/04/09/kubernetes-1-21-unloads-pod-security-adds-dual-ipv4-ipv6-networking-and-shuts-down-gracefully/)
* [kubernetes.io: Introducing Suspended Jobs in Kubernetes 1.21](https://kubernetes.io/blog/2021/04/12/introducing-suspended-jobs/)
* [analyticsindiamag.com: Kubernetes v1.21 Released: Major Updates & Latest Features](https://analyticsindiamag.com/kubernetes-v1-21-released-major-updates-latest-features/)
* [openshift.com: Kubernetes 1.21 Grows Innovative New Features](https://www.openshift.com/blog/kubernetes-1.21-grows-innovative-new-features)
* [Kubernetes v1.16 API deprecation testing](https://gist.github.com/jimangel/0014770713cdca8b363816930ef2520f) Examples of how to test the impact of the v1.16 API deprecations and ways to debug early!
* [kubernetes.io: Kubernetes 1.21: Metrics Stability hits GA](https://kubernetes.io/blog/2021/04/23/kubernetes-release-1.21-metrics-stability-ga/)
* [blog.gopaddle.io: Strange things you never knew about Kubernetes ConfigMaps on day one 🌟🌟](https://blog.gopaddle.io/2021/04/01/strange-things-you-never-knew-about-kubernetes-configmaps-on-day-one/)

### Namespaces
* [qvault.io: How to Restart All Pods in a Kubernetes Namespace 🌟](https://qvault.io/2020/10/26/how-to-restart-all-pods-in-a-kubernetes-namespace/)
* [medium: How to create Namespaces in Kubernetes? 🌟](https://medium.com/faun/namespaces-in-kubernetes-4bac49414770)
* [starwindsoftware.com: Remove a Kubernetes namespace blocked with Terminating status](https://www.starwindsoftware.com/blog/remove-a-kubernetes-namespace-blocked-with-terminating-status)
* [opensource.com: Configure multi-tenancy with Kubernetes namespaces 🌟](https://opensource.com/article/21/2/kubernetes-namespaces) Namespaces provide basic building blocks of access control for applications, users, or groups of users.

### Kubernetes Best Practices and Tips
* [**Optimize** Kubernetes cluster management with these 5 tips 🌟](https://searchitoperations.techtarget.com/feature/Optimize-Kubernetes-cluster-management-with-these-5-tips) Effective Kubernetes cluster management requires operations teams to balance pod and node deployments with performance and availability needs.
* [techradar.com: Three tips to implement Kubernetes with open standards](https://www.techradar.com/news/three-tips-to-implement-kubernetes-with-open-standards)
* [geekflare.com: 10 Kubernetes Best Practices for Better Container Orchestration 🌟](https://geekflare.com/kubernetes-best-practices/)
* [wideops.com: Kubernetes best practices: Setting up health checks with readiness and liveness probes](https://wideops.com/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes/)
* [containerjournal.com: 10 Best Practices Worth Implementing to Adopt Kubernetes](https://containerjournal.com/topics/container-management/10-best-practices-worth-implementing-to-adopt-kubernetes/)
* [medium: Kubernetes Tip: How Does OOMKilled Work?](https://medium.com/tailwinds-navigator/kubernetes-tip-how-does-oomkilled-work-ba71b135993b)
* [cloud.google.com: Kubernetes Best Practices 🌟](https://cloud.google.com/blog/topics/kubernetes-best-practices) A collection of blog posts aimed at guide you through the Kubernetes best practices
* [releasehub.com: Kubernetes Health Checks - 2 Ways to Improve Stability in Your Production Applications](https://releasehub.com/blog/kubernetes-health-checks-2-ways-to-improve-stability)
* [stackpulse.com: Kubernetes and SRE: 5 Best Practices for K8s Reliability in Production 🌟](https://stackpulse.com/blog/https-stackpulse-com-blog-kubernetes-production-best-practices/)
* [fairwinds.com: Never Should You Ever In Kubernetes: #1 Do K8S The Hard Way](https://www.fairwinds.com/blog/never-should-you-ever-in-kubernetes-1-do-k8s-the-hard-way)
* [fairwinds.com: Never Should You Ever In Kubernetes Part 2: Kubernetes Security Mistakes](https://www.fairwinds.com/blog/never-should-you-ever-in-kubernetes-part-2-kubernetes-security-mistakes)
* [fairwinds.com: Never Should You Ever In Kubernetes Part 3: 6 K8s Reliability Mistakes](https://www.fairwinds.com/blog/6-kubernetes-reliability-mistakes)
* [fairwinds.com: Never Should You Ever In Kubernetes Part 4: Three K8s Efficiency Mistakes](https://www.fairwinds.com/blog/3-kubernetes-efficiency-mistakes)
* [stackpulse.com: Challenges of Running Services With K8s Reliably](https://stackpulse.com/blog/challenges-of-running-services-with-k8s-reliably/)
* [blog.lukechannings.com: Mistakes made and lessons learned with Kubernetes and GitOps 🌟](https://blog.lukechannings.com/2020-05-10-kubernetes-gitops-lessons.html)
  
### Disruptions
- [thenewstack.io: Kubernetes: Use PodDisruptionBudgets for Application Maintenance and Upgrades](https://thenewstack.io/kubernetes-use-poddisruptionbudgets-for-application-maintenance-and-upgrades/)

### Cost Estimation Strategies
- [cncf.io: 5 Problems with Kubernetes Cost Estimation Strategies](https://www.cncf.io/blog/2020/09/18/5-problems-with-kubernetes-cost-estimation-strategies)
- [loft.sh: How To Reduce Your Kubernetes Cost](https://loft.sh/blog/reduce-kubernetes-cost/)
- [harness.io: Getting Started with Cloud Cost Optimization](https://harness.io/2020/09/getting-started-with-cloud-cost-optimization/)
- [rancher.com: Gain Better Visibility into Kubernetes Cost Allocation](https://rancher.com/blog/2020/gain-better-visibility-kubernetes-cost-allocation)
- [loft.sh: Kubernetes Cost Savings By Reducing The Number Of Clusters](https://loft.sh/blog/kubernetes-cost-savings/)
- [thenewstack.io: 5 Essential Tips to Manage Kubernetes Costs 🌟](https://thenewstack.io/5-essential-tips-to-manage-kubernetes-costs/)
- [opensource.com: 3 ways Kubernetes optimizes your IT budget 🌟](https://opensource.com/article/20/12/it-budget-kubernetes) Automation is not only good for IT, it's also beneficial to your company's bottom line.
- [thenewstack.io: 5 Expensive Kubernetes Cost Traps and How to Deal with Them](https://thenewstack.io/5-expensive-kubernetes-cost-traps-and-how-to-deal-with-them/)

#### kubecost
- [How to track costs in multi-tenant Amazon EKS clusters using Kubecost 🌟](https://aws.amazon.com/blogs/containers/how-to-track-costs-in-multi-tenant-amazon-eks-clusters-using-kubecost/)
- [infracloud.io: Kubernetes Cost Reporting using Kubecost 🌟](https://www.infracloud.io/blogs/kubernetes-cost-reporting-using-kubecost/)
- [github.com/kubecost: kubecost-exporter - Running Kubecost as a Prometheus metric exporter 🌟](https://github.com/kubecost/cost-model/blob/develop/kubecost-exporter.md)
- [blog.kubecost.com: Kubecost raises $5.5 million to help teams monitor and reduce their Kubernetes spend](http://blog.kubecost.com/blog/announcing-kubecost-first-round/)
- [kubectl-cost 🌟](https://github.com/kubecost/kubectl-cost) is a kubectl plugin that provides easy CLI access to Kubernetes cost allocation metrics via the kubecost APIs. It allows developers, devops, and others to quickly determine the cost & efficiency for any Kubernetes workload
- [blog.kubecost.com: AKS Cost Monitoring and Governance With Kubecost](https://blog.kubecost.com/blog/aks-cost/)
- [thenewstack.io: KubeCost: Monitor Kubernetes Costs with kubectl](https://thenewstack.io/kubecost-monitor-kubernetes-costs-with-kubectl/)

### Kubernetes Resource and Capacity Management. Capacity Planning
* [itnext.io: Kubernetes Resource Management in Production 🌟](https://itnext.io/kubernetes-resource-management-in-production-d5382c904ed1) Requests, Limits, Overcommitment, Slack/Waste, Throttling
* [medium: Ultimate Kubernetes Resource Planning Guide 🌟](https://medium.com/dev-genius/ultimate-kubernetes-resource-planning-guide-449a4fddd1d6)
* [learnk8s.io: Setting the right requests and limits in Kubernetes 🌟🌟](https://learnk8s.io/setting-cpu-memory-limits-requests) By far the best read on requests and limits in Kubernetes.
* [openshift.com: Sizing Applications in Kubernetes 🌟](https://www.openshift.com/blog/sizing-applications-in-kubernetes)
* [magalix.com: Capacity Planning 🌟](https://www.magalix.com/blog/kubernetes-patterns-capacity-planning) When we have multiple Pods with different Priority Class values, the admission controller starts by sorting Pods according to their priority. What happens when there are no nodes with available resources to schedule a high-priority pods? 
* [sysdig.com: Kubernetes capacity planning: How to rightsize your cluster 🌟](https://sysdig.com/blog/kubernetes-capacity-planning)

### Kubernetes Monitoring
* [kube-prometheus 🌟](https://github.com/prometheus-operator/kube-prometheus) Use Prometheus to monitor Kubernetes and applications running on Kubernetes
* [medium: Kubernetes Monitoring: Kube-State-Metrics](https://medium.com/@chrisedrego/kubernetes-monitoring-kube-state-metrics-df6546aea324)
* [Kubernetes Monitoring 101 — Core pipeline & Services Pipeline 🌟](https://levelup.gitconnected.com/kubernetes-monitoring-101-core-pipeline-services-pipeline-a34cd4cc9627)
* [medium: Utilizing and monitoring kubernetes cluster resources more effectively](https://medium.com/@martin.schneppenheim/utilizing-and-monitoring-kubernetes-cluster-resources-more-effectively-using-this-tool-df4c68ec2053)
* [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://sysdig.com/blog/kubernetes-monitoring-best-practices/)
* [magalix.com: Best Practices And Tools For Monitoring Your Kubernetes Cluster](https://www.magalix.com/blog/best-practices-and-tools-for-monitoring-your-kubernetes-cluster)
* [sysdig.com: Monitoring Kubernetes in Production](https://sysdig.com/blog/monitoring-kubernetes/)
* [sysdig.com: How to monitor Kubernetes control plane 🌟](https://sysdig.com/blog/monitor-kubernetes-control-plane/)
* [thenewstack.io: 12 Critical Kubernetes Health Conditions You Need to Monitor 🌟](https://thenewstack.io/12-critical-kubernetes-health-conditions-you-need-to-monitor/)
* [devopscurry.com: Best  Open-Source Monitoring Tools for Kubernetes in 2021 🌟](https://devopscurry.com/best-open-source-monitoring-tools-for-kubernetes-in-2021/)
* [circonus.com: 12 Critical Kubernetes Health Conditions You Need to Monitor and Why](https://www.circonus.com/2020/12/12-critical-kubernetes-health-conditions-you-need-to-monitor-and-why/)
* [circonus.com: Guide to Kubernetes Monitoring: Part 1](https://www.circonus.com/2020/09/guide-to-kubernetes-monitoring-part-1/)
    * [circonus.com: Guide to Monitoring Kubernetes, Part 2: Which Metrics and Health Conditions You Should be Monitoring](https://www.circonus.com/2021/01/guide-to-monitoring-kubernetes-part-2-which-metrics-and-health-conditions-you-should-be-monitoring/)
* [infracloud.io: Monitoring Kubernetes cert-manager Certificates with BotKube 🌟](https://www.infracloud.io/blogs/monitoring-kubernetes-cert-manager-certificates/) - [botkube.io 🌟](https://www.botkube.io/)

#### Logging in Kubernetes
- [cncf.io: Logging in Kubernetes: EFK vs PLG Stack 🌟](https://www.cncf.io/blog/2020/07/27/logging-in-kubernetes-efk-vs-plg-stack/)
- [medium: How to Deploy an EFK stack to Kubernetes](https://medium.com/avmconsulting-blog/how-to-deploy-an-efk-stack-to-kubernetes-ebc1b539d063)
- [digitalocean.com: How To Set Up an Elasticsearch, Fluentd and Kibana (EFK) Logging Stack on Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes)
- [portworx.com: How to backup and restore Elasticsearch on Kubernetes](https://portworx.com/how-to-backup-and-restore-elasticsearch-on-kubernetes/)
- [elastic.co: Elastic Stack Monitoring with Elastic Cloud on Kubernetes (ECK - official operator) 🌟](https://www.elastic.co/es/blog/elastic-stack-monitoring-with-elastic-cloud-on-kubernetes) In this blog post, we'll explore how the official **ElasticCloud** on **Kubernetes operator** can be used to easily deploy and manage **ElasticStack Monitoring** using the new **Beat CRD**.
* [papertrail.com: Quick and Easy Way to Implement Kubernetes Logging](https://www.papertrail.com/blog/quick-and-easy-way-to-implement-kubernetes-logging/) The SolarWinds® Papertrail™ team is excited to announce SolarWinds rKubeLog, an open-source project designed to streamline Kubernetes logging. rKubeLog allows you to forward logs to Papertrail from within a Kubernetes cluster without using a daemon or setting up application-level logging or a logging sidecar.
* [qlinh.com: Leveraging Kubernetes audit logs for threat detection 🌟](https://qlinh.com/infosec/2020/09/30/threat-detection-with-kubernetes-audit-logs.html) Kubernetes audit logs can provide great visibility into the operation and inner workings of your cluster. Learn how to leverage Kubernetes audit logs for threat detection

#### ECK Elastic Cloud on Kubernetes 
- [elastic.co: How to configure Elastic Cloud on Kubernetes with SAML and hot-warm-cold architecture](https://www.elastic.co/es/blog/how-to-configure-elastic-cloud-on-kubernetes-with-saml-and-hot-warm-cold-architecture) Elastic Cloud on Kubernetes (ECK) is an easy way to get the Elastic Stack up and running on top of Kubernetes. That’s because ECK automates the deployment, provisioning, management, and setup of Elasticsearch, Kibana, Beats, and more. 

### Health Checks
* [medium: How to Perform Health checks in Kubernetes (K8s)](https://medium.com/faun/how-to-perform-health-checks-in-kubernetes-k8s-a4e5300b1f9d)
* [youtube: Kubernetes 101: Get Better Uptime with K8s Health Checks](https://www.youtube.com/watch?v=D9w3DH1zAc8)

### Architecting Kubernetes clusters
* [learnk8s.io: Architecting Kubernetes clusters — how many should you have?](https://learnk8s.io/how-many-clusters)
* [learnk8s.io: Architecting Kubernetes clusters — choosing a worker node size](https://learnk8s.io/kubernetes-node-size)
* [itnext.io: Architecting Kubernetes clusters — choosing a worker node size](https://itnext.io/architecting-kubernetes-clusters-choosing-a-worker-node-size-b3729cc0c78f)

### Templating YAML in Kubernetes with real code. YQ YAML processor
- [Templating YAML in Kubernetes with real code](https://learnk8s.io/templating-yaml-with-code)
    - TL;DR: You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/). 
    - If you're working on large scale projects, you should consider using **real code** — you can find [hands-on examples on how to programmatically generate Kubernetes resources in Java, Go, Javascript, C# and Python in this repository](https://github.com/learnk8s/templating-kubernetes).

### Kubernetes Limits
* [kubernetes.io Policy Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
* [sysdig.com: Understanding Kubernetes limits and requests by example 🌟](https://sysdig.com/blog/kubernetes-limits-requests/)
* [dev.to/aurelievache: Understanding Kubernetes: part 22 – LimitRange](https://dev.to/aurelievache/understanding-kubernetes-part-22-limitrange-144l)
* [dzone: Dive Deep Into Resource Requests and Limits in Kubernetes](https://dzone.com/articles/dive-deep-into-resource-requests-and-limits-in-kub) This article will be helpful for you to understand how Kubernetes requests and limits work, and why they can work in an expected way.
* [sysdig.com: How to rightsize the Kubernetes resource limits](https://sysdig.com/blog/kubernetes-resource-limits/)

### Kube Scheduler
- [All you need to know to get started with the Kube Scheduler](https://gist.github.com/luisalfonsopreciado/40a0fc2319241d517832affdce2bc1ff)

### Kubernetes Knowledge Hubs
- [k8sref.io 🌟](https://www.k8sref.io/) Kubernetes Reference
- [Kubernetes Research. Research documents on node instance types, managed services, ingress controllers, CNIs, etc. 🌟](https://learnk8s.io/research) A research hub to collect all knowledge around Kubernetes. Those are in-depth reports and comparisons designed to drive your decisions. Should you use GKE, AKS, EKS? How many nodes? What instance type?

## Kubectl commands
* [itnext.io: Boosting your kubectl productivity](https://itnext.io/boosting-your-kubectl-productivity-b348f7c25712)
* [medium: 4 Simple Kubernetes Terminal Customizations to Boost Your Productivity](https://medium.com/better-programming/4-simple-kubernetes-terminal-customizations-to-boost-your-productivity-deda60a19924)
* [medium: Ready-to-use commands and tips for kubectl](https://medium.com/flant-com/kubectl-commands-and-tips-7b33de0c5476)
* [medium: Be fast with Kubectl 1.19 CKAD/CKA 🌟](https://medium.com/faun/be-fast-with-kubectl-1-18-ckad-cka-31be00acc443) Collection of the fastest ways to create k8s resources using kubectl ≥ 1.18
* [developers.redhat.com: Kubectl: Developer tips for the Kubernetes command line 🌟](https://developers.redhat.com/blog/2020/11/20/kubectl-developer-tips-for-the-kubernetes-command-line/)
* [ibm.com: 8 Kubernetes Tips and Tricks 🌟](https://www.ibm.com/cloud/blog/8-kubernetes-tips-and-tricks) Most of the tips given below are using kubectl, a powerful command-line tool that allows you to execute commands against Kubernetes clusters.
    * Set default namespaces
    * Helpful aliases to save time
    * YAML editing with vi
    * Create YAML from kubectl commands 
    * Switching between Kubernetes namespaces
    * Shell auto-completion
    * Viewing resource utilization
    * Extend kubectl and create your own commands using raw outputs
* [pixelstech.net: Update & Delete Kubernetes resources in one-line command](https://www.pixelstech.net/article/1604225312-Update-&amp-Delete-Kubernetes-resources-in-one-line-command)

### Kubectl Cheat Sheets
* [Kubectl Cheat Sheets](cheatsheets.md)

### Kubectl explain
- [kubectl explain](https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl_explain/)
- [itnext.io: Using ‘kubectl explain’ for Custom Resources](https://itnext.io/understanding-kubectl-explain-9d703396cc8) Goal: Explore if ‘kubectl explain’ can be used to discover static information about Custom Resources

```for r in $(kubectl api-resources|grep -v ^N|awk '{print $1}');do kubectl explain $r --recursive;done```

### Kubectl Autocomplete
* [Kubectl Autocomplete](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
* [kubectl Shell Autocomplete](https://blog.heptio.com/kubectl-shell-autocomplete-heptioprotip-48dd023e0bf3)
* [Kubernetes productivity tips and tricks 🌟](https://www.padok.fr/en/blog/kubernetes-productivity-tips)
* [complete-alias](https://github.com/cykerway/complete-alias) Automagical shell alias completion.

```bash
source <(kubectl completion bash) # setup autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.
```

You can also use a shorthand alias for kubectl that also works with completion:

```bash
alias k=kubectl
complete -F __start_kubectl k
```

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

### Buildkit CLI for kubectl a drop in replacement for docker build
- [container-registry.com: Lifting Developers’ Productivity 🌟](https://container-registry.com/posts/productivity-lift-buildkit-cli-for-kubectl/) With BuildKit CLI for kubectl a drop in replacement for docker build. In this post, you will learn how to build container images with BuildKit CLI for kubectl (a replacement for the `docker build` command)
- [vmware-tanzu/buildkit-cli-for-kubectl (kubectl plugin)](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl) BuildKit CLI for kubectl is a tool for building container images with your Kubernetes cluster.

### Kubectl Alternatives
* [Helm and Kubernetes](#helm-kubernetes-tool)
* [Kubectl plugins and tools](#kubectl-plugins)

#### Manage Kubernetes (K8s) objects with Ansible Kubernetes Module
* [Manage Kubernetes (K8s) objects](https://docs.ansible.com/ansible/latest/modules/k8s_module.html)
* [ansibleforkubernetes.com 🌟](https://www.ansibleforkubernetes.com/)

#### Jenkins Kubernetes Plugins
* [Jenkins Kubernetes Plugin](https://plugins.jenkins.io/kubernetes/)
* [Kubernetes Continuous Deploy](https://plugins.jenkins.io/kubernetes-cd/)

## Self Service Kubernetes Namespaces
- [Self-Service Kubernetes Namespaces Are A Game-Changer 🌟](https://loft.sh/blog/self-service-kubernetes-namespaces-are-a-game-changer/)

## Client Libraries for Kubernetes
- [Client Libraries for Kubernetes](kubernetes-client-libraries.md)

## Helm Kubernetes Tool
- [Helm](helm.md)

## Kubernetes Development Tools. Kubernetes clients and dashboards
- [ordina-jworks.github.io: A comparison of Kubernetes clients and dashboards](https://ordina-jworks.github.io/cloud/2020/08/28/kubernetes-clients-comparison.html)
- [loft.sh: Kubernetes Development Environments – A Comparison](https://loft.sh/blog/kubernetes-development-environments-comparison/)
- [yitaek.medium.com: Useful Tools for Better Kubernetes Development 🌟](https://yitaek.medium.com/useful-tools-for-better-kubernetes-development-87820c2b9435) Lens, Polaris, kube-hunter, kube-bench, Trivy, Goldilocks, Kyverno, kube-ps1, kubectx + kubens , krew, kubectl-neat, kube-no-trouble, helm-mapkubeapis, kube-diff + helm-diff , kube forwarder, kubecost, kubespy.
- [kccncna20.sched.com: A Walk Through the Kubernetes UI Landscape](https://kccncna20.sched.com/event/ekAd/a-walk-through-the-kubernetes-ui-landscape-joaquim-rocha-kinvolk-henning-jacobs-zalando-se) Working with Kubernetes clusters and workloads can be overwhelming, both for operators, as well as application developers. While kubectl is the de-facto standard interface to interact with Kubernetes' API, a graphical user interface can provide a better experience for newcomers and advanced users alike. This talk will look at the current landscape of Open Source Kubernetes web and desktop UIs, including Kubernetes Dashboard, Lens, Octant, Kubernetes Web View, and Headlamp. Particularly, how different dashboards are built, for what purpose they can be used, and how they compare in terms of functionality, so attendees can get the most out of the vast landscape of Kubernetes UIs.
    - [PDF](https://static.sched.com/hosted_files/kccncna20/02/A%20Walk%20Through%20the%20Kubernetes%20UI%20Landscape%20%28KubeCon%20Talk%202020%29.pdf)
- [tilt.dev 🌟](https://tilt.dev) You can use Tilt to easily build and run your application on Kubernetes. In comparison with similar tools, it provides [UI for managing the process and cloud platform](https://cloud.tilt.dev) to share data with your team.
- [microcks.io 🌟](https://microcks.io) K8s-based API mock/test tool. 
    - [microcks.io: Podman Compose support in Microcks](https://microcks.io/blog/podman-compose-support)
- [kinvolk.io: Shining a light on the Kubernetes User Experience with Headlamp](https://kinvolk.io/blog/2020/11/shining-a-light-on-the-kubernetes-user-experience-with-headlamp/)
- [kubevious](https://github.com/kubevious/kubevious)
- [cncf.io: Tools to develop apps on Kubernetes 🌟](https://www.cncf.io/blog/2021/05/10/tools-to-develop-apps-on-kubernetes)

### Okteto local kubernetes development
- [okteto.com: How to Develop and Debug Java Applications on Kubernetes](https://okteto.com/blog/how-to-develop-java-apps-in-kubernetes/)
- [codefresh.io: Tutorial - Local Kubernetes Development with Okteto 🌟](https://codefresh.io/kubernetes-tutorial/okteto/)

### Lens Kubernetes IDE
- [Lens Kubernetes IDE 🌟](https://k8slens.dev/) Lens is the only IDE you’ll ever need to take control of your Kubernetes clusters. It's open source and free. Download it today!

[![lens ide](images/header-lens.png)](https://k8slens.dev/)

### Kubenav
- [kubenav](https://github.com/kubenav/kubenav) is the navigator for your Kubernetes clusters right in your pocket. kubenav is a mobile, desktop and web app to manage Kubernetes clusters and to get an overview of the status of your resources.

### Cloud Manager
- [thenewstack.io: Cloud Manager: A New Multicloud PaaS Platform Built on Kubernetes](https://thenewstack.io/cloud-manager-a-new-multicloud-paas-platform-built-on-kubernetes/)
- [medium: Do It All Kubernetes Dashboard](https://medium.com/faun/do-it-all-kubernetes-dashboard-81375833e01c)

### Skaffold. Local Kubernetes Development
- [Skaffold 🌟](https://skaffold.dev/)
- [infracloud.io: Build and deploy Kubernetes apps with Skaffold](https://www.infracloud.io/blogs/skaffold-usecases/)
- [testingclouds.wordpress.com: Migrating from Docker Compose to Skaffold 🌟](https://testingclouds.wordpress.com/2021/03/09/migrating-from-docker-compose-to-skaffold/)

### Kind
- [Kind](https://kind.sigs.k8s.io/) is a tool for running local Kubernetes clusters using Docker container “nodes”. kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

## Autoscaling
* [levelup.gitconnected.com: Effects of Docker Image Size on AutoScaling w.r.t Single and Multi-Node Kube Cluster](https://levelup.gitconnected.com/effects-of-docker-image-size-on-autoscaling-w-r-t-single-and-multi-node-kube-cluster-29c4f689cd99)
* [infracloud.io: 3 Autoscaling Projects to Optimise Kubernetes Costs](https://www.infracloud.io/blogs/3-autoscaling-projects-optimising-kubernetes-costs/) Three autoscaling use cases:
    * Autoscaling Event-driven workloads
    * Autoscaling real-time workloads
    * Autoscaling Nodes/Infrastructure 
* [blog.scaleway.com: Understanding Kubernetes Autoscaling](https://blog.scaleway.com/understanding-kubernetes-autoscaling/)
* [infracloud.io: Kubernetes Autoscaling with Custom Metrics (updated) 🌟](https://www.infracloud.io/blogs/kubernetes-autoscaling-custom-metrics/)
* [sysdig.com: Kubernetes pod autoscaler using custom metrics](https://sysdig.com/blog/kubernetes-autoscaler/)
* [learnk8s.io: Architecting Kubernetes clusters — choosing the best autoscaling strategy 🌟](https://learnk8s.io/kubernetes-autoscaling-strategies) How to configure multiple autoscalers in Kubernetes to minimise scaling time and found out that 4 factors affect scaling: 
    1. HPA reaction time.
    2. CA reaction time.
    3. Node provisioning time.
    4. Pod creation time.
* [thenewstack.io: Reduce Kubernetes Costs Using Autoscaling Mechanisms](https://thenewstack.io/reduce-kubernetes-costs-using-autoscaling-mechanisms/)
* [cast.ai: Guide to Kubernetes autoscaling for cloud cost optimization 🌟](https://cast.ai/blog/guide-to-kubernetes-autoscaling-for-cloud-cost-optimization)
### Cluster Autoscaler Kubernetes Tool
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
* [medium: Build Kubernetes Autoscaling for Cluster Nodes and Application Pods 🌟](https://medium.com/better-programming/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07)
* [Auto-Scaling Your Kubernetes Workloads (K8s) 🌟](https://medium.com/faun/autoscaling-in-kubernetes-cluster-bc55b8393a19)
* [medium: Cluster Autoscaler in Kubernetes](https://medium.com/avmconsulting-blog/cluster-autoscaler-type-in-kubernetes-part2-f2ae432eefbb)
* [itnext.io: Kubernetes Resources and Autoscaling — From Basics to Greatness 🌟](https://itnext.io/kubernetes-resources-and-autoscaling-from-basics-to-greatness-7cae17fbf27b)

### HPA and VPA
* [HPA: Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
* [VPA: Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)
* [returngis.net: Escalado vertical de tus pods en Kubernetes con VerticalPodAutoscaler](https://www.returngis.net/2020/07/escalado-vertical-de-tus-pods-en-kubernetes/)
* [partlycloudy.blog: Horizontal Autoscaling in Kubernetes #3 – KEDA](https://partlycloudy.blog/2020/05/29/horizontal-autoscaling-in-kubernetes-3-keda/)
    * [thenewstack.io: CNCF KEDA 2.0 Scales up Event-Driven Programming on Kubernetes](https://thenewstack.io/microsoft-keda-2-0-scales-up-event-driven-programming-on-kubernetes/)
* [medium: Build Kubernetes Autoscaling for Cluster Nodes and Application Pods](https://medium.com/better-programming/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07) Via the Cluster Autoscaler, Horizontal Pod Autoscaler, and Vertical Pod Autoscaler
* [itnext.io: Horizontal Pod Autoscaling with Custom Metric from Different Namespace](https://itnext.io/horizontal-pod-autoscaling-with-custom-metric-from-different-namespace-f19f8446143b)
* [Kubernetes autoscaling with Istio metrics 🌟](https://medium.com/google-cloud/kubernetes-autoscaling-with-istio-metrics-76442253a45a) Scaling based on traffic is not something new to Kubernetes, an ingress controllers such as NGINX can expose Prometheus metrics for HPA. **The difference in using Istio is that you can autoscale backend services as well, apps that are accessible only from inside the mesh.**
* [medium: 1/3 Autoscaling in Kubernetes: A Primer on Autoscaling](https://medium.com/expedia-group-tech/autoscaling-in-kubernetes-a-primer-on-autoscaling-7b8f0f95a928)
    * [medium: 2/3 Autoscaling in Kubernetes: Options, Features, and Use Cases](https://medium.com/expedia-group-tech/autoscaling-in-kubernetes-options-features-and-use-cases-c8a6ce145957) 
    * [medium: 3/3 Autoscaling in Kubernetes: Why doesn’t the Horizontal Pod Autoscaler work for me?](https://medium.com/expedia-group-tech/autoscaling-in-kubernetes-why-doesnt-the-horizontal-pod-autoscaler-work-for-me-5f0094694054)
* [around25.com: Horizontal Pod Autoscaler in Kubernetes 🌟](https://around25.com/blog/horizontal-pod-autoscaler-in-kubernetes/)
* [superawesome.com: Scaling pods with HPA using custom metrics. How we scale our kid-safe technology using Kubernetes 🌟](https://www.superawesome.com/blog/how-we-scale-our-kid-safe-technology-using-auto-scaling-on-kubernetes/)
* [velotio.com: Autoscaling in Kubernetes using HPA and VPA](https://www.velotio.com/engineering-blog/autoscaling-in-kubernetes-using-hpa-vpa)
* [kubectl-vpa](https://github.com/ninlil/kubectl-vpa) Tool to manage VPAs (vertical-pod-autoscaler) resources in a kubernetes-cluster 

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

### Kubernetes Load Testing and High Load Tuning
- [itnext.io: Kubernetes: load-testing and high-load tuning — problems and solutions](https://itnext.io/kubernetes-load-testing-and-high-load-tuning-problems-and-solutions-244d869a9791)
- [engineering.zalando.com: Building an End to End load test automation system on top of Kubernetes](https://engineering.zalando.com/posts/2021/03/building-an-end-to-end-load-test-automation-system-on-top-of-kubernetes.html) Learn how we built an end-to-end load test automation system to make load tests a routine task.

## Extending Kubernetes
### Adding Custom Resources. Extending Kubernetes API with Kubernetes Resource Definitions. CRD vs Aggregated API
- [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [itnext.io: CRD is just a table in Kubernetes](https://itnext.io/crd-is-just-a-table-in-kubernetes-13e15367bbe4)
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

### Krew, a plugin manager for kubectl plugins
* [Krew 🌟](https://krew.sigs.k8s.io/) is the plugin manager for kubectl command-line tool.
* [itnext.io: Extending Kubernetes Cluster; Kubectl Plugins and Krew](https://itnext.io/extending-kubernetes-cluster-kubectl-plugins-and-krew-547a8bc839a3)
* [darumatic.com: Improve Kubectl Command with Krew 🌟](https://darumatic.com/blog/improve_kubectl_command_with_krew) Krew is a tool that aims to ease plugin discovery, installation, upgrade, and removal on multiple operating systems. This article will show you how easy it is to grab and experiment with existing plugins.
* kubectl trace is now on the krew index!! Go install it now!
    ```bash
    kubectl krew install trace
    ```
    And then just try to snoop into all the file openings:

    ```bash
    kubectl trace run -a  <yournode>  -e 'kprobe:do_sys_open { printf("%s: %s\n", comm, str(arg1)) }'
    ```

### OpenKruise/Kruise
- [openkruise.io](https://openkruise.io/)
- [OpenKruise/Kruise](https://github.com/openkruise/kruise)
- [thenewstack.io: Introducing CloneSet: A Production-Grade Kubernetes Deployment CRD](https://thenewstack.io/introducing-cloneset-production-grade-kubernetes-deployment-crd/)

###  Crossplane, a Universal Control Plane API for Cloud Computing. Crossplane Workloads Definitions
- [crossplane.io 🌟](https://crossplane.io/) Crossplane is an open source Kubernetes add-on that supercharges your Kubernetes clusters enabling you to provision and manage infrastructure, services, and applications from kubectl.
- [Crossplane, a Universal Control Plane API for Cloud Computing](https://www.infoq.com/news/2019/01/upbound-crossplane/)
- [Crossplane as an OpenShift Operator to manage and provision cloud-native services](https://blog.crossplane.io/crossplane-openshift-operator-cloud-native-services/)
- [Crossplane: A Kubernetes Control Plane to Roll Your Own PaaS](https://thenewstack.io/crossplane-a-kubernetes-control-plane-to-roll-your-own-paas/)

## Kubernetes Community
### Community Forums
- [Community Forums 🌟🌟](https://discuss.kubernetes.io/)

### Kubernetes Special Interest Groups (SIGs)
- [Kubernetes Special Interest Groups (SIGs)](https://github.com/kubernetes/community/blob/master/README.md#special-interest-groups-sig) have been around to support the community of developers and operators since around the 1.0 release. People organized around networking, storage, scaling and other operational areas.
- [SIG Apps: build apps for and operate them in Kubernetes](https://kubernetes.io/blog/2016/08/sig-apps-running-apps-in-kubernetes/)

#### Kubernetes SIG's Repos
- [Kubernetes SIGs 🌟](https://github.com/kubernetes-sigs) Org for Kubernetes SIG-related work.
- [ExternalDNS: Configure external DNS servers (AWS Route53, Google CloudDNS and others) for Kubernetes Ingresses and Services](https://github.com/kubernetes-sigs/external-dns)
- [Kubernetes-Secrets-Store-CSI-Driver: Secrets Store CSI driver for Kubernetes secrets](https://github.com/kubernetes-sigs/secrets-store-csi-driver) Integrates secrets stores with Kubernetes via a CSI volume.
- [kustomize](https://github.com/kubernetes-sigs/kustomize) Customization of kubernetes YAML configurations.

#### Kubectl Plugins 
* [Available kubectl plugins 🌟](https://github.com/kubernetes-sigs/krew-index/blob/master/plugins.md)
* [Awesome Kubectl plugins 🌟](https://github.com/ishantanu/awesome-kubectl-plugins)
* [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
* [youtube: Welcome to the world of kubectl plugins](https://www.youtube.com/watch?v=_W2qZvQT6XY)
* [padok.fr: Getting started with kubectl plugins 🌟](https://www.padok.fr/en/blog/kubectl-plugins) 5 useful kubectl plugins:
    * whoami
    * access-matrix
    * neat
    * tree
    * node-shell
* [kubectl-trace 🌟](https://github.com/iovisor/kubectl-trace) kubectl trace is a kubectl plugin that allows you to schedule the execution of bpftrace programs in your Kubernetes cluster.
* [pixelstech.net: Build a Kubectl Plugin from Scratch](https://www.pixelstech.net/article/1606901393-Build-a-Kubectl-Plugin-from-Scratch)

<center>
<iframe src="https://www.youtube.com/embed/_W2qZvQT6XY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br/>

## Enforcing Policies and governance for kubernetes workloads with Conftest
* [Accelerated Feedback Loops when Developing for Kubernetes with Conftest](https://engineering.plex.com/posts/kubernetes-policy-conftest) Learn how to validate Kubernetes resources with Conftest for faster feedback loops
    * [open-policy-agent/conftest](https://github.com/open-policy-agent/conftest)
    * [Enforcing policies and governance for Kubernetes workloads 🌟](https://learnk8s.io/kubernetes-policies)
* [Deprek8ion](https://github.com/swade1987/deprek8ion) is a set of rego policies to monitor Kubernetes APIs deprecations and designed to work with conftest.
* [k8s-worker-pod-autoscaler](https://github.com/practo/k8s-worker-pod-autoscaler) scales the replicas in a deployment based on observed queue length.
* [kubectl-prune / kubectl-reap 🌟](https://github.com/micnncim/kubectl-reap) is a kubectl plugin that prunes unused Kubernetes resources.
* [kconnect - The Kubernetes Connection Manager CLI 🌟](https://github.com/fidelity/kconnect) kconnect is a CLI utility that can be used to discover and securely access Kubernetes clusters across multiple operating environments. Based on the authentication mechanism chosen the CLI will discover Kubernetes clusters you are allowed to access in a target hosting environment (i.e. EKS, AKS, Rancher) and generate a kubeconfig for a chosen cluster.
* [konstraint](https://github.com/plexsystems/konstraint) is a CLI tool to assist with the creation and management of templates and constraints when using [Gatekeeper](https://github.com/open-policy-agent/gatekeeper).
* [Draino 🌟](https://github.com/planetlabs/draino) Draino automatically drains Kubernetes nodes based on labels and node conditions. Nodes that match all of the supplied labels and any of the supplied node conditions will be cordoned immediately and drained after a configurable drain-buffer time.

## Kubernetes Backup and Migrations
* [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup)  
* [Stash](https://github.com/stashed/stash) If you are running production workloads in Kubernetes, you might want to take backup of your disks, databases etc. Stash is a cloud native data backup and recovery solution for Kubernetes workloads
* [thenewstack.io: Cloud Native Backups, Disaster Recovery and Migrations on Kubernetes](https://thenewstack.io/cloud-native-backups-disaster-recovery-and-migrations-on-kubernetes/)
* [rancher.com: The No. 1 Rule of Disaster Recovery](https://rancher.com/blog/2020/number-one-rule-disaster-recovery)
* [rancher.com: Disaster Recovery Preparedness for Your Kubernetes Clusters 🌟](https://rancher.com/blog/2020/disaster-recovery-preparedness-kubernetes-clusters)
* [k8s-snapshots: Automatic Volume Snapshots on Kubernetes](https://github.com/miracle2k/k8s-snapshots) is an operator that creates and expires snapshots according to annotations to your PersistentVolume or PersistentVolumeClaim resources.
* [infracloud.io: Protecting Kubernetes applications data using Kanister](https://www.infracloud.io/blogs/protecting-kubernetes-applications-with-kanister)
    * [kanister.io](https://kanister.io/)
* [thenewstack.io: DevSecOps Teams Need Application-Consistent Backups for Kubernetes Workloads](https://thenewstack.io/devsecops-teams-need-application-consistent-backups-for-kubernetes-workloads/)
* [percona.com: Using Volume Snapshot/Clone in Kubernetes (GKE & Percona Kubernetes Operator for XtraDB Cluster)](https://www.percona.com/blog/2020/10/22/using-volume-snapshot-clone-in-kubernetes/)
* [kasten.io: Kubernetes Application Mobility](https://www.kasten.io/kubernetes/application-mobility/) Reliable and Powerful Migration of Complete Applications Across Kubernetes Clusters.
* [longhorn issue: Move replica to a different server](https://github.com/longhorn/longhorn/issues/292) 
* [aithority.com: Bacula Systems Announces World’s First Enterprise-Class Backup and Recovery Solution for Red Hat OpenShift](https://aithority.com/it-and-devops/cloud/bacula-systems-announces-worlds-first-enterprise-class-backup-and-recovery-solution-for-red-hat-openshift/)
* [cloudify.co: Migrating Pods With Containerized Applications Between Nodes In The Same Kubernetes Cluster Using Cloudify 🌟](https://cloudify.co/blog/migrating-pods-containerized-applications-nodes-kubernetes-cluster-using-cloudify/)
* [thenewstack.io: Red Hat Brings Backup, Snapshots to OpenShift Container Storage](https://thenewstack.io/red-hat-brings-backup-snapshots-to-openshift-container-storage/)
* [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes)
* [Bacula Enterprise for OpenShift and Kubernetes 🌟](https://www.baculasystems.com/)
* [dani-izquierdo95.medium.com: Batch processing using Cron Jobs. MySQL automated backup on Openshift/K8s](https://dani-izquierdo95.medium.com/mysql-automated-backup-on-openshift-k8s-3690280d304f)
* [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)

### Kubernetes Volume Snapshot
* [kubernetes.io: Kubernetes 1.20: Kubernetes Volume Snapshot Moves to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga/)
* [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)
* [blocksandfiles.com: Red Hat OpenShift now does container storage backup 🌟](https://blocksandfiles.com/2021/01/27/red-hat-openshift-container-storage-backup/) Red Hat has teamed up with three container backup suppliers to integrate their services with the company’s OpenShift Kubernetes distribution. The Red Hat-certified backup products for OpenShift container storage are parent company IBM’s [Spectrum Protect Plus](https://blocksandfiles.com/2020/06/05/ibm-spectrum-protect-plus/); [TrilioVault](https://blocksandfiles.com/2020/12/10/trilio-funding/) for Kubernetes; and Veeam-owned Kasten’s [K10](https://blocksandfiles.com/2020/01/30/kasten-k10-kubernetes-container-protection/). 

### Backup with Trillio Cloud-Native Data Protection for Kubernetes, OpenStack and Virtualization
* [Trillio](http://trilio.io)
* [TrillioVault for Kubernetes](https://www.trilio.io/triliovault-for-kubernetes/)
* [redhat.com: OpenShift Backup and Cluster failover with Triliovault 🌟](https://www.redhat.com/es/about/videos/openshift-backup-and-cluster-failover-triliovault)

### Backup with Kasten K10
* [Kasten](https://www.kasten.io/)
* [redhat.com: OpenShift Backup and Recovery with Kasten K10](https://www.redhat.com/es/about/videos/openshift-backup-and-recovery-kasten-k10)

### Backup with Velero
* [akomljen.com: Kubernetes Backup and Restore with Velero 🌟](https://akomljen.com/kubernetes-backup-and-restore-with-velero/?utm_sq=ggwzo8xdd8)
* [wecloudpro.com: Kubernetes Disaster Recovery with Velero 🌟](https://www.wecloudpro.com/2020/08/22/kubernetes-disaster-recovery-with-velero.html)
* [medium: Backup,Restore & Migrate Kubernetes cluster with Velero](https://medium.com/@maheshd7878/restore-backup-migrate-kubernetes-cluster-with-velero-434fa151f1e8)
* [medium: Velero backup/restore for K8s Stateful Applications managed by Operators](https://medium.com/@Sandeepkallazhi/velero-backup-restore-for-k8s-stateful-applications-managed-by-operators-8fd9c732ffcc?utm_sq=gi0vbpxxa3)

### Konveyor Open Source Migration Tool for Kubernetes
- [github.com/konveyor 🌟](https://github.com/konveyor) - [konveyor.io](https://www.konveyor.io/) A community to build tools and document best practices to modernize workloads and bring them to Kubernetes.
- [containerjournal.com: Red Hat, IBM Launch Konveyor to Aggregate Kubernetes Tools](https://containerjournal.com/features/red-hat-ibm-launch-konveyor-to-aggregate-kubernetes-tools/)
- [engineering.konveyor.io: Konveyor Engineering Knowledgebase](https://engineering.konveyor.io/) Engineers working on Konveyor have started putting their own kbase articles here.

## Kubernetes Troubleshooting
* [Kubernetes troubleshooting diagram 🌟](https://github.com/redhatspain/awesome-kubernetes/blob/master/docs/images/kubernetes-troubleshooting.jpg)
* [Understanding Kubernetes cluster events 🌟](https://banzaicloud.com/blog/k8s-cluster-logging/)
* [nigelpoulton.com: Troubleshooting kubernetes service discovery - Part 1](https://nigelpoulton.com/blog/f/troubleshooting-kubernetes-service-discovery---part-1)
* [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)
* [medium.com: Kubernetes Tip: How To Disambiguate A Pod Crash To Application Or To Kubernetes Platform? (CrashLoopBackOff)](https://medium.com/tailwinds-navigator/kubernetes-tip-how-to-disambiguate-a-pod-crash-to-application-or-to-kubernetes-platform-f6c1395a8d09)
* [veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status “Terminating”](https://veducate.co.uk/kubernetes-pvc-terminating/)
* [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes/)
* [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples/)
* [levelup.gitconnected.com: 5 tips for troubleshooting apps on Kubernetes](https://levelup.gitconnected.com/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)

### Debugging Techniques and Strategies. Debugging with ephemeral containers
- [kubectl-debug](https://github.com/aylei/kubectl-debug)
- [kubesandclouds.com: Debugging with ephemeral containers in K8s (v1.18+)](https://kubesandclouds.com/index.php/2020/05/30/ephemeral-containers-in-k8s/)
- [How to quarantine pods 🌟](https://www.reddit.com/r/kubernetes/comments/gt3uvg/how_to_quarantine_pods/)
- [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg) KDBG (Kubernetes Debuger) is a small docker container based on lastest Alpine Linux image, used for debugging Kubernetes clusters from inside a pod.
- [inspektor-gadget](https://github.com/kinvolk/inspektor-gadget) Collection of gadgets for debugging and introspecting Kubernetes applications using BPF 
    - [kinvolk.io](https://kinvolk.io)
- [learnk8s.io: A visual guide on troubleshooting Kubernetes deployments 🌟](https://learnk8s.io/troubleshooting-deployments)
- [StatusBay 🌟](https://github.com/similarweb/statusbay) is a tool that provides the missing visibility into the K8S deployment process. The main goal is to ease the experience of troubleshooting and debugging services in K8S and provide confidence while making changes.
- [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
- [codefresh.io: Using Telepresence 2 for Kubernetes debugging and local development](https://codefresh.io/kubernetes-tutorial/telepresence-2-local-development/)
- [towardsdatascience.com: The Easiest Way to Debug Kubernetes Workloads](https://towardsdatascience.com/the-easiest-way-to-debug-kubernetes-workloads-ff2ff5e3cc75) The fastest and easiest way to debug and troubleshoot any application running on Kubernetes

<center>
[![learnk8s debug your pods](images/learnk8s_debug_your_pods.png){: style="width:30%"}](https://learnk8s.io/troubleshooting-deployments)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: How to quarantine a Pod in Kubernetes.<br><br>This technique helps you with debugging running Pods in production.<br><br>The Pod is detached from the Service (no traffic), and you can troubleshoot it live.<br><br>Let&#39;s get started! <a href="https://t.co/E7AUh2ylM7">pic.twitter.com/E7AUh2ylM7</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1275786970610843648?ref_src=twsrc%5Etfw">June 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: How to gracefully shut down Pods without dropping production traffic in Kubernetes<br><br>If you&#39;ve ever noticed dropped connection after a rolling upgrade, this thread digs into the details.<br><br>Let&#39;s start: 𝘸𝘩𝘢𝘵 𝘩𝘢𝘱𝘱𝘦𝘯𝘴 𝘸𝘩𝘦𝘯 𝘢 𝘗𝘰𝘥 𝘪𝘴 𝘥𝘦𝘭𝘦𝘵𝘦𝘥? <a href="https://t.co/jS5litVUlw">pic.twitter.com/jS5litVUlw</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1280087657968627713?ref_src=twsrc%5Etfw">July 6, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: How does the scheduler work in Kubernetes?<br><br>The scheduler is in charge of deciding where your pods are deployed in the cluster.<br><br>It might sound like an easy job, but it&#39;s rather complicated!<br><br>Let&#39;s dive into it. <a href="https://t.co/iC1vnargc4">pic.twitter.com/iC1vnargc4</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1309090938673868801?ref_src=twsrc%5Etfw">September 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

## Kubernetes Tutorials
* [kubernetes.io: Kubernetes Tutorials 🌟](https://kubernetes.io/docs/tutorials/) Official documentation from Kubernetes. One can go through this official documentation and can learn much more about Kubernetes.
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
* [dzone: The complete kubernetes collection tutorials and tools 🌟](https://dzone.com/articles/the-complete-kubernetes-collection-tutorials-and-tools)
* [dzone: kubernetes in 10 minutes a complete guide to look](https://dzone.com/articles/kubernetes-in-10-minutes-a-complete-guide-to-look)
* [magalix.com: The Best Kubernetes Tutorials 🌟](https://www.magalix.com/blog/the-best-kubernetes-tutorials)
* [35 Advanced Tutorials to Learn Kubernetes 🌟](https://medium.com/faun/35-advanced-tutorials-to-learn-kubernetes-dae5695b1f18)
* [geekflare.com: 14 Kubernetes Tutorials for Beginner to Master](https://geekflare.com/learn-kubernetes/)
* [freecodecamp.org: The Kubernetes Handbook 🌟](https://www.freecodecamp.org/news/the-kubernetes-handbook/)
* [youtube: Kubernetes Pods and ReplicaSets explained 🌟](https://www.youtube.com/playlist?list=PLy0Gle4XyvbGhGpX0CXAuiEsfL-MD-rND)
* [medium: DraftKings Kubernetes Workshop: Hands-on Learning in K8s (with Video Walkthrough)](https://medium.com/draftkings-engineering/draftkings-workshop-demystifying-kubernetes-4ce86c187408)
* [100 Days Of Kubernetes: 100daysofkubernetes.io 🌟](https://100daysofkubernetes.io/) 100 Days of Kubernetes is the challenge in which we aim to learn something new related to Kubernetes each day across 100 Days!!!
* [youtube playlist: Thetips4you - Kubernetes Tutorial for Beginners 🌟](https://www.youtube.com/playlist?app=desktop&list=PLVx1qovxj-akr_3XqQQgpqRyQw4GYuS4h) HPA, Deployments, YAML, Jenkins, etc.
* [youtube playlist: DevNation Lessons: Kubernetes Fundamentals 🌟](https://www.youtube.com/playlist?list=PLf3vm0UK6HKpOqIY2fcu_M0sCSpluyXMW)

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: What happens when you create a Pod in Kubernetes?<br><br>Spoiler: a surprisingly simple task reveals a complicated workflow that touches several components in the cluster. <a href="https://t.co/SNEufo0lBe">pic.twitter.com/SNEufo0lBe</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1291371746801545219?ref_src=twsrc%5Etfw">August 6, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

### Online Training
* [katacoda.com 🌟](https://www.katacoda.com/) Interactive Learning and Training Platform for Software Engineers 
* [kubernetesbyexample.com 🌟](http://kubernetesbyexample.com/)
* [Play with Kubernetes 🌟](https://labs.play-with-k8s.com/) A simple, interactive and fun playground to learn Kubernetes
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
    * [wardviaene/kubernetes-course 🌟](https://github.com/wardviaene/kubernetes-course) 
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
    * [wardviaene/advanced-kubernetes-course 🌟](https://github.com/wardviaene/advanced-kubernetes-course) 
* [Certified Kubernetes Administrator CKA course notes — diagrams for each subject area and use as reference for future refresher 🌟](https://drive.google.com/file/d/1RhPULD1IAVgCo1KD857iCoaNKuJjQKa1/view)
* [javarevisited.blogspot.com: Top 5 Free Courses to Learn Kubernetes for Developers and DevOps Engineers](https://javarevisited.blogspot.com/2019/01/top-5-free-kubernetes-courses-for-DevOps-Engineer.html)

### Famous Kubernetes resources of 2019
* [Kubernetes for developers](https://www.udemy.com/course/kubernetes-for-developers/)
* [Kubernetes for the Absolute Beginners](https://www.udemy.com/course/learn-kubernetes/)
* [Kubernetes: Getting Started (Free)](https://www.udemy.com/course/kubernetes-getting-started/)
* [Kubernetes Tutorial: Learn the Basics](https://dev.to/scalyr/kubernetes-tutorial-learn-the-basics-and-get-started-5dgh)
* [Complete Kubernetes Course](https://www.youtube.com/watch?v=0KQndcIedeg)
* [Getting started with Kubernetes](https://learn.pluralsight.com/programs/2019/free-course/template4)

### Famous Kubernetes resources of 2020
* [javarevisited.blogspot.com: Top 5 courses to Learn Docker and Kubernetes in 2020 - Best of Lot](https://javarevisited.blogspot.com/2019/05/top-5-courses-to-learn-docker-and-kubernetes-for-devops.html)
* [medium.com: Top 15 Online Courses to Learn Docker, Kubernetes, and AWS for Fullstack Developers and DevOps Engineers](https://medium.com/javarevisited/top-15-online-courses-to-learn-docker-kubernetes-and-aws-for-fullstack-developers-and-devops-d8cc4f16e773)
* [medium.com: 7 Free Online Courses to Learn Kubernetes in 2020](https://medium.com/javarevisited/7-free-online-courses-to-learn-kubernetes-in-2020-3b8a68ec7abc)
* [skillslane.com: 10 Best Kubernetes Courses [2020]: Beginner to Advanced Courses](https://skillslane.com/learn-kubernetes-from-these-best-online-courses/)

### K8s Diagrams
- [k8s-diagrams 🌟](https://github.com/cloudogu/k8s-diagrams) A collection of diagrams explaining kubernetes by cloudogu, written in [PlantUML](https://twitter.com/PlantUML).

## Kubernetes Patterns and Antipatterns. Service Discovery
- [github.com/k8spatterns/examples 🌟](https://github.com/k8spatterns/examples) Examples for "Kubernetes Patterns - Reusable Elements for Designing Cloud-Native Applications"
- [kubernetes.io: container design patterns](https://kubernetes.io/blog/2016/06/container-design-patterns/)
- [magalix.com: Kubernetes Patterns - The Service Discovery Pattern 🌟](https://www.magalix.com/blog/kubernetes-patterns-the-service-discovery-pattern)
- [gardener.cloud: Kubernetes Antipatterns](https://gardener.cloud/050-tutorials/content/howto/antipattern/)
- [dzone.com: Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1)
- [developers.redhat.com: Top 10 must-know Kubernetes design patterns](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)
- [medium: 10 Anti-Patterns for Kubernetes Deployments 🌟](https://medium.com/better-programming/10-antipatterns-for-kubernetes-deployments-e97ce1199f2d) Common practices in Kubernetes deployments that have better solutions
- [learnsteps.com: How Kubernetes works on reconciler pattern](https://www.learnsteps.com/how-kubernetes-works-on-a-reconciler-pattern/)
- [learncloudnative.com: Sidecar Container Pattern](https://www.learncloudnative.com/blog/2020-09-30-sidecar-container/)
- [towardsdatascience.com: Kubernetes pattern for applications with external environment configuration 🌟](https://towardsdatascience.com/kubernetes-pattern-for-applications-with-external-environment-configuration-a42d7bdd7e97) Learn how to decouple configuration from the application using git-sync, Kubernetes init-containers, ConfigMaps and volumes.
- [codefresh.io: Kubernetes Deployment Antipatterns – part 1 🌟](https://codefresh.io/kubernetes-tutorial/kubernetes-antipatterns-1/)
- [codefresh.io: Kubernetes Deployment Antipatterns – part 2 🌟](https://codefresh.io/kubernetes-tutorial/kubernetes-antipatterns-2/)
- [iximiuz.com: Service discovery in Kubernetes - combining the best of two worlds 🌟](https://iximiuz.com/en/posts/service-discovery-in-kubernetes/)
- [github.com/sharadbhat/KubernetesPatterns: YAML and Golang implementations of common Kubernetes patterns](https://github.com/sharadbhat/KubernetesPatterns)
- [developers.redhat.com: Kubernetes configuration patterns, Part 1: Patterns for Kubernetes primitives 🌟](https://developers.redhat.com/blog/2021/04/28/kubernetes-configuration-patterns-part-1-patterns-for-kubernetes-primitives)
    - [developers.redhat.com: Kubernetes configuration patterns, Part 2: Patterns for Kubernetes controllers 🌟](https://developers.redhat.com/blog/2021/05/05/kubernetes-configuration-patterns-part-2-patterns-for-kubernetes-controllers/)
- [learnk8s.io: Extending applications on Kubernetes with multi-container pods 🌟](https://learnk8s.io/sidecar-containers-patterns) Can you change an application without changing any code in Kubernetes? You can when you use multiple containers in a single Pod. Developing and deploying new apps in Kubernetes is easy. But what about legacy apps? In Kubernetes, you can use multiple containers in a Pod to change how your application works.
- [dev.to: Kubernetes Deployment Antipatterns – part 1 🌟🌟](https://dev.to/codefreshio/kubernetes-deployment-antipatterns-part-1-2116)

[![Top 10 Kubernetes patterns](images/top_10_kubernetes_patterns.png)](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)

## Books and e-Books
- [developers.redhat.com: Kubernetes Operators 🌟](https://developers.redhat.com/books/kubernetes-operators)
- [Kubernetes 101](https://leanpub.com/kubernetes-101)
- [learnk8s.io/first-steps](https://learnk8s.io/first-steps)
- [ubuntuask.com: Best New Kubernetes Books](https://ubuntuask.com/blog/best-new-kubernetes-books)
### Famous Kubernetes resources of 2019
* [Kubernetes essentials E-book 🌟](https://images.linoxide.com/ebook-kubernetes-essentials.pdf)
* [Cloud-Native DevOps With Kubernetes O'Reilly book (Free) 🌟](https://www.nginx.com/resources/library/cloud-native-devops-with-kubernetes/)
* [Kubernetes: Up and Running, 2nd Edition🌟](http://shop.oreilly.com/product/0636920223788.do) Dive into the Future of Infrastructure. By Brendan Burns, Kelsey Hightower, Joe Beda
* [Container Security](https://www.amazon.com/gp/product/1492056707)
    * [Don't make this container security mistake](https://bitfieldconsulting.com/blog/container-security)
* [digitalocean.com: From Containers to Kubernetes with Node.js eBook](https://www.digitalocean.com/community/books/from-containers-to-kubernetes-with-node-js-ebook)

<center>
[![Kubernetes: Up and Running](images/kubernetes_up_running_kelsey_hightower.gif)](http://shop.oreilly.com/product/0636920223788.do)
</center>

### Kubernetes Patterns eBooks
* [k8spatterns.io: Free Kubernetes Patterns e-book 🌟](https://k8spatterns.io/) , [ref](https://www.redhat.com/en/engage/kubernetes-containers-architecture-s-201910240918)
* [magalix.com: Free Kubernetes Application Architecture Patterns eBook 🌟](https://www.magalix.com/kubernetes-application-patterns-e-book-download)

## Kubernetes Operators
- [kruschecompany.com: What is a Kubernetes Operator and Where it Can be Used?](https://kruschecompany.com/kubernetes-operator/)
- [kruschecompany.com: Prometheus Operator – Installing Prometheus Monitoring Within The Kubernetes Environment](https://kruschecompany.com/kubernetes-prometheus-operator/)
- [redhat.com: Kubernetes operators - Embedding operational expertise side by side with containerized applications](https://www.redhat.com/sysadmin/kubernetes-operators)
- [hashicorp.com: Creating Workspaces with the HashiCorp Terraform Operator for Kubernetes](https://www.hashicorp.com/blog/creating-workspaces-with-the-hashicorp-terraform-operator-for-kubernetes/)
- [banzaicloud.com: Kafka rolling upgrade made easy with Supertubes](https://banzaicloud.com/blog/kafka-rolling-upgrade/)
- [devops.com: Day 2 for the Operator Ecosystem 🌟](https://devops.com/day-2-for-the-operator-ecosystem/)
    - [KUDO: The Kubernetes Universal Declarative Operator 🌟](https://kudo.dev/) KUDO is a toolkit that makes it easy to build Kubernetes Operators, in most cases just using YAML.
- [itnext.io: **Operator Lifecycle Manager (OLM)** 🌟](https://itnext.io/wth-is-a-operator-lifecycle-manager-873cf1661b04)
- [kube-fluentd-operator 🌟](https://github.com/vmware/kube-fluentd-operator) is a sane, no-brainer Kubernetes+Helm distribution of Fluentd with batteries included, config validation, no needs to restart, with sensible defaults and best practices built-in. You can use Kubernetes labels to filter/route logs!
- [Domain-harvester](https://github.com/shurshun/domain-harvester) is an operator that collects domains from all Ingress resources in a Kubernetes cluster and provides its expiry information
- [Cass Operator](https://github.com/datastax/cass-operator) The DataStax Kubernetes Operator for Apache Cassandra®
- [Kotal operator](https://github.com/kotalco/kotal) is cloud agnostic blockchain deployer that make it easy to deploy highly available, self-managing, self-healing blockchain infrastructure (networks, nodes, storage clusters ...) on any cloud.
- [Speculator: Redis Operator](https://github.com/OT-CONTAINER-KIT/redis-operator) A Golang based redis operator that will make/oversee Redis standalone/cluster mode setup on top of the Kubernetes. It can create a redis cluster setup with best practices on Cloud as well as the Bare metal environment. Also, it provides an in-built monitoring capability using redis-exporter.
- [github.com/carlosedp/lbconfig-operator: External Load Balancer Operator 🌟](https://github.com/carlosedp/lbconfig-operator) a Kubernetes/openshift Operator to dynamically configure external load-balancers distributing the traffic to the cluster nodes. It's not 100% (will it ever be?) but already configures the F5 BigIP. The idea is to have multiple LB backends soon.
- [Sentry Operator](https://github.com/jace-ys/sentry-operator) A Kubernetes operator for automating the provisioning and management of Sentry resources via Kubernetes CRDs.
- [thenewstack.io: When to Use, and When to Avoid, the Operator Pattern 🌟](https://thenewstack.io/kubernetes-when-to-use-and-when-to-avoid-the-operator-pattern/)
- [infoq.com: Kubernetes Operators in Depth](https://www.infoq.com/articles/kubernetes-operators-in-depth/)
- [DB Operator 🌟](https://github.com/kloeckner-i/db-operator) is a Kubernetes Operator for the management of cloud databases, primarily Google Cloud SQL(GCSQL). It is designed to support the on demand creation of test environments in CI/CD pipelines.
- [cncf.io: Kubernetes Operators 101](https://www.cncf.io/blog/2020/10/02/kubernetes-operators-101/)
- [container-solutions.com: Kubernetes Operators Explained](https://blog.container-solutions.com/kubernetes-operators-explained)
- [kubeload - load testing](https://github.com/Efrat19/kubeload) is a Kubernetes operator that lets you configure your load-test initial load, max load, interval and hatch-rate. You can use CRD to define all the parameters and repeat your load testing experiments.
- [contentful.com: Open-sourcing kube-secret-syncer: A Kubernetes operator to sync secrets from AWS Secrets Manager](https://www.contentful.com/blog/2020/10/20/open-source-kube-secret-syncer/)
    - [contentful-labs/kube-secret-syncer 🌟](https://github.com/contentful-labs/kube-secret-syncer)
- [registry-creds](https://github.com/alexellis/registry-creds) is a Kubernetes operator that can be used to propagate a single ImagePullSecret to all namespaces within your cluster. The primary reason for creating this operator is to make it easier to consume images from Docker Hub.
- [gemini](https://github.com/FairwindsOps/gemini) is a Kubernetes CRD and operator for managing VolumeSnapshots. This allows you to back up your PersistentVolumes on a regular schedule, retire old backups, and restore backups with minimal downtime.
- [Kdo: deployless development on Kubernetes 🌟](https://kdo.dev/) Kdo is a command line tool that enables developers to run, develop and test code changes in a realistic deployed setting without having to deal with the complexity of Kubernetes deployment and configuration.
- [HostPort Operator](https://github.com/rmb938/hostport-allocator) is a Kubernetes Operator to allocate host ports
- [iximiuz.com: Exploring Kubernetes Operator Pattern 🌟](https://iximiuz.com/en/posts/kubernetes-operator-pattern/)
- [isaaguilar/terraform-operator: Terraform Operator](https://github.com/isaaguilar/terraform-operator) A Kubernetes CRD and Controller to handle Terraform operations by generating k8s jobs catered to perform Terraform workflows
- [hashicorp/terraform-k8s: Terraform Cloud Operator for Kubernetes](https://github.com/hashicorp/terraform-k8s) The Terraform Cloud Operator for Kubernetes provides first-class integration between Kubernetes and Terraform Cloud by extending the Kubernetes control plane to enable lifecycle management of cloud and on-prem infrastructure.
- [didil/autobucket-operator](https://github.com/didil/autobucket-operator) The autobucket operator is a Kubernetes operator that automatically creates and manages Cloud Buckets (Object Storage) for k8s Deployments.
- [openshift.com: Is your Operator Air-Gap Friendly?](https://www.openshift.com/blog/is-your-operator-air-gap-friendly)
- [kuberhealthy 🌟](https://github.com/Comcast/kuberhealthy) An operator for synthetic monitoring on Kubernetes. Write your own tests in your own container and Kuberhealthy will manage everything else. Automatically creates and sends metrics to Prometheus and InfluxDB. Included simple JSON status page. Supplements other solutions like Prometheus very nicely!
- [Bare Metal Operator](https://github.com/metal3-io/baremetal-operator) The Bare Metal Operator implements a Kubernetes API for managing bare metal hosts. It maintains an inventory of available hosts as Custom Resource Definitions.
- [Meerkat](https://github.com/borchero/meerkat) Meerkat is a Kubernetes Operator that facilitates the deployment of OpenVPN in a Kubernetes cluster. By leveraging Hashicorp Vault, Meerkat securely manages the underlying PKI.
- [Logging Operator](https://github.com/OT-CONTAINER-KIT/logging-operator) A golang based CRD operator to setup and manage logging stack (Elasticsearch, Fluentd, and Kibana) in the Kubernetes cluster. It helps to setup each component of the EFK stack separately.
- [gst-pipeline-operator: A Kubernetes operator for running audio/video processing pipelines](https://github.com/tinyzimmer/gst-pipeline-operator)
- [uptimerobot-operator](https://github.com/brennerm/uptimerobot-operator) A Kubernetes operator that creates UptimeRobot monitors for your ingresses
- [medium.com: Getting Started With Kubernetes Operators (Helm Based) - Part 1](https://www.velotio.com/engineering-blog/getting-started-with-kubernetes-operators-helm-based-part-1)
    - [medium.com: Getting Started With Kubernetes Operators (Ansible Based) — Part 2](https://medium.com/velotio-perspectives/getting-started-with-kubernetes-operators-ansible-based-part-2-472eb0d453b7)
    - [velotio.com: Getting Started With Kubernetes Operators (Golang Based) - Part 3](https://www.velotio.com/engineering-blog/getting-started-with-kubernetes-operators-golang-based-part-3)
- [IngressMonitorController (Deprecated)](https://github.com/stakater/IngressMonitorController) A Kubernetes controller to watch ingresses and create liveness alerts for your apps/microservices in UptimeRobot, StatusCake, Pingdom, etc. 

### Operator Capability Levels
- [Operator Capability Levels](https://operatorframework.io/operator-capabilities/) Operators come in different maturity levels in regards to their lifecycle management capabilities for the application or workload they deliver. The capability models aims to provide guidance in terminology to express what features users can expect from an Operator.

### Cluster Addons
- [Cluster Addons 🌟](https://github.com/kubernetes-sigs/cluster-addons) With cluster addon operators, we are exploring a kubernetes-native way of managing addons using CRDs(Custom Resource Definitions) and controllers where the controllers encode how best to manage the addon. Installing and managing an addon could be as simple as creating a custom resource.

### K8Spin Operator. Kubernetes multi-tenant operator
- [K8Spin Operator 🌟](https://github.com/k8spin/k8spin-operator) Kubernetes multi-tenant operator. Enables multi-tenant capabilities in your Kubernetes Cluster. [We defined some small features to implement](https://github.com/k8spin/k8spin-operator/projects/1). If you know python & Kubernetes and want to contribute to this project, ping us!
- [thenewstack.io: K8Spin Provides Multitenant Isolation for Kubernetes](https://thenewstack.io/k8spin-provides-multitenant-isolation-for-kubernetes/) 
- [Discover K8Spin open source software](https://k8spin.cloud/oss-projects/)

### Flux. The GitOps Operator for Kubernetes
* [Flux 🌟](https://fluxcd.io/) The GitOps operator for Kubernetes
* [docs.fluxcd.io](https://docs.fluxcd.io/)
* [github: Flux CD](https://github.com/fluxcd/flux)
* [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.
* [alicegg.tech: Managing a Kubernetes cluster with Helm and FluxCD](https://alicegg.tech/2020/11/09/helm.html)

### K8s KPIs with Kuberhealthy Operator
- [K8s KPIs with Kuberhealthy 🌟](https://kubernetes.io/blog/2020/05/29/k8s-kpis-with-kuberhealthy/) transforming Kuberhealthy into a Kubernetes operator for synthetic monitoring. This new ability granted developers the means to create their own Kuberhealthy check containers to synthetically monitor their applications and clusters. Additionally, we created a guide on how to easily install and use Kuberhealthy in order to capture some helpful synthetic [KPIs](https://kpi.org/KPI-Basics).

### Writing Kubernetes Operators
* [Kubernetes.io: Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
* [opensource.com: Build a Kubernetes Operator in 10 minutes with Operator SDK](https://opensource.com/article/20/3/kubernetes-operator-sdk)
* [itnext.io: Testing the Operator SDK and making a prefetch mechanism for Kubernetes](https://itnext.io/testing-the-operator-sdk-and-making-a-prefetch-mechanism-for-kubernetes-7508577efdd7)
* [magalix.com: Creating Custom Kubernetes Operators](https://www.magalix.com/blog/creating-custom-kubernetes-operators)
* [medium.com: Writing Your First Kubernetes Operator](https://medium.com/faun/writing-your-first-kubernetes-operator-8f3df4453234)
* [bmc.com: What Is a Kubernetes Operator?](https://www.bmc.com/blogs/kubernetes-operator/)
* [Writing a Kubernetes Operator in Java Cheat Sheet](https://developers.redhat.com/cheat-sheets/writing-kubernetes-operator-java/)
* [linuxera.org: Writing Operators using the Operator Framework SDK](https://linuxera.org/writing-operators-using-operator-framework/)
* [openshift.com: 7 Best Practices for Writing Kubernetes Operators: An SRE Perspective](https://www.openshift.com/blog/7-best-practices-for-writing-kubernetes-operators-an-sre-perspective)
* [medium: From Zero to Kubernetes Operator](https://medium.com/@victorpaulo/from-zero-to-kubernetes-operator-dd06436b9d89) In this post you will learn how to build a simple Kubernetes Operator. The article starts with the main concepts and then continues with hands-on labs where you will create a Kubernetes Operator from the ground up.
* [openshift.com: Build Your Kubernetes Operator With the Right Tool 🌟](https://www.openshift.com/blog/build-your-kubernetes-operator-with-the-right-tool) **Go-based operators are by far the most popular. That is why Go is probably the first option to consider.** The other good choice is Helm, especially if you already have a Helm chart for your software or you want to build your operator quickly and you don't need any complex [capability levels](https://operatorframework.io/operator-capabilities/). I'd leave Operator Frameworks or Bare Programming Language implementations only for the cases when keeping a single programming language in your organization is a priority.
* [codilime.com: How to create a custom resource with Kubernetes Operator](https://codilime.com/how-to-create-a-custom-resource-with-kubernetes-operator/) Implementing DaemonJob from scratch learn how to create a custom resource with the Kubernetes Operator Framework.
* [rookout.com: Lessons Learned When Building A Kubernetes Operator](https://www.rookout.com/blog/lessons-learned-when-building-a-kubernetes-operator)
* [pavel.cool: Oxidizing the Kubernetes operator](https://www.pavel.cool/rust/rust-kubernetes-operators/)
* [brennerm.github.io: Kubernetes operators with Python #1: Creating CRDs](https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html)
* [vivilearns2code.github.io: Writing Controllers For Kubernetes Resources](https://vivilearns2code.github.io/k8s/2021/03/11/writing-controllers-for-kubernetes-custom-resources.html)

## Kubernetes Networking
* [kubernetes.io: The Kubernetes network model. How to implement the Kubernetes networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
* [ovh.com - getting external traffic into kubernetes: clusterip, nodeport, loadbalancer and ingress](https://www.ovh.com/blog/getting-external-traffic-into-kubernetes-clusterip-nodeport-loadbalancer-and-ingress/)
* [stackrox.com: Kubernetes Networking Demystified: A Brief Guide](https://www.stackrox.com/post/2020/01/kubernetes-networking-demystified/)
* [medium.com: Fighting Service Latency in Microservices With Kubernetes](https://medium.com/@sindhujacynixit/fighting-service-latency-in-microservices-with-kubernetes-f5a584f5af36)
* [medium.com: Kubernetes NodePort vs LoadBalancer vs Ingress? When should I use what? 🌟](https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0)
* [blog.alexellis.io: Get a LoadBalancer for your private Kubernetes cluster](https://blog.alexellis.io/ingress-for-your-local-kubernetes-cluster/)
* [dustinspecker.com: How Do Kubernetes and Docker Create IP Addresses?!](https://dustinspecker.com/posts/how-do-kubernetes-and-docker-create-ip-addresses/)
* [youtube: Kubernetes Ingress Explained Completely For Beginners](https://www.youtube.com/watch?v=VicH6KojwCI)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 1)](https://www.weave.works/blog/introduction-to-kubernetes-pod-networking--part-1)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 2)](https://www.weave.works/blog/aws-networking-overview---part-2)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 3)](https://dzone.com/articles/aws-and-kubernetes-networking-options-and-trade-of) 
* [medium: Service Types in Kubernetes? 🌟](https://medium.com/faun/service-types-in-kubernetes-24a1587677d6) A Service enables network access to a set of Pods in Kubernetes.
* [containo.us: Kubernetes Ingress & Service API Demystified](https://containo.us/blog/kubernetes-ingress-service-api-demystified/)
* [speakerdeck.com: Kubernetes and networks. Why is this so dan hard? 🌟](https://speakerdeck.com/thockin/kubernetes-and-networks-why-is-this-so-dang-hard)
* [opensource.com: Why I use Ingress Controllers to expose Kubernetes services](https://opensource.com/article/20/8/ingress-controllers-kubernetes) Kubernetes ingress controllers will make or break your cloud architecture.
* [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification/)
* [infoq.com: Kubernetes Ingress Is Now Generally Available](https://www.infoq.com/news/2020/09/kubernetes-ingress-ga/)
* [Learnk8s: Comparison of Kubernetes Ingress Controllers 🌟🌟](https://docs.google.com/spreadsheets/d/191WWNpjJ2za6-nbG4ZoUMXMpUK8KlCIosvQB0f-oq3k/edit#gid=907731238) How do you choose the *right* Kubernetes Ingress controller when: Not all Ingress controllers support UDP, Only Kong has a free LDAP integration, Nginx Ingress and HAProxy are the only two ingress without CRDs.
* [blog.alexellis.io: Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere/)
* [jmrobles.medium.com: How to setup Hetzner load balancer on a Kubernetes cluster](https://jmrobles.medium.com/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)
* [kubernetes.io: Scaling Kubernetes Networking With EndpointSlices](https://kubernetes.io/blog/2020/09/02/scaling-kubernetes-networking-with-endpointslices/) EndpointSlices are a new Kubernetes API that provides a scalable and extensible alternative to the Endpoints API.
* [haproxy.com: Announcing HAProxy Kubernetes Ingress Controller 1.5 🌟](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-5/)
* [devclass.com: HAProxy Ingress Controller 1.5 introduces mTLS support, gives load balancing experts more power](https://devclass.com/2021/01/26/haproxy-ingress-controller-1_5/)
* [thenewstack.io: HAProxy Kubernetes Ingress Controller Moves Outside the Cluster](https://thenewstack.io/haproxy-kubernetes-ingress-controller-moves-outside-the-cluster/)
* [suse.com: NGINX Guest Blog: NGINX Kubernetes Ingress Controller 🌟](https://www.suse.com/c/nginx-guest-blog-kubernetes-ingress-controller)
* [dustinspecker.com: iptables: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/iptables-how-kubernetes-services-direct-traffic-to-pods) In this article you will learn how Kubernetes's kube-proxy uses iptables to direct traffic to pods randomly. You'll focus on the ClusterIP type of Kubernetes services.
* [blog.cloudflare.com: Moving k8s communication to gRPC](https://blog.cloudflare.com/moving-k8s-communication-to-grpc/)
* [tech2fun.net: K8s Nginx Ingress Handling TLS Traffic and Using Pod Readiness Probes](https://tech2fun.net/k8s-nginx-ingress-handling-tls-traffic-and-using-pod-readiness-probes/)
* [K8GB - Kubernetes Global Balancer](https://github.com/AbsaOSS/k8gb) - [openshift.com: K8GB - Kubernetes Global Balancer ](https://www.openshift.com/blog/openshift-commons-briefing-k8gb-kubernetes-global-balancer-with-yuri-tsarev-absa-and-paul-morie-red-hat)
* [altoros.com: Kubernetes Networking: How to Write Your Own CNI Plug-in with Bash](https://www.altoros.com/blog/kubernetes-networking-writing-your-own-simple-cni-plug-in-with-bash/)
* [Network Node Manager](https://github.com/kakao/network-node-manager) network-node-manager is a kubernetes controller that controls the network configuration of a node to resolve network issues of kubernetes. By simply deploying and configuring network-node-manager, you can solve kubernetes network issues that cannot be resolved by kubernetes or resolved by the higher kubernetes Version. Below is a list of kubernetes's issues to be resolved by network-node-manager. network-node-manager is based on kubebuilder v2.3.1.
* [getenroute.io: Drive API Security At Kubernetes Ingress Using Helm And Envoy 🌟](https://getenroute.io/docs/ingress-filter-legos-secure-microservices-apis-using-helm-envoy/)
* [ithands-on.com: Kubernetes 101 : External services - ExternalName, DNS and Endpoints](https://www.ithands-on.com/2021/04/kubernetes-101-external-services.html)
* [ibm.com: Multizone Kubernetes and VPC Load Balancer Setup](https://www.ibm.com/cloud/blog/multizone-kubernetes-and-vpc-load-balancer-setup) Securely expose your Kubernetes app by setting up a Load Balancer for VPC in a different zone.
* [opensource.googleblog.com: Kubernetes: Efficient Multi-Zone Networking with Topology Aware Routing](https://opensource.googleblog.com/2020/11/kubernetes-efficient-multi-zone.html)
* [nbailey.ca: Domesticated Kubernetes Networking](https://nbailey.ca/post/k8s-networking/)
* [sookocheff.com: A Guide to the Kubernetes Networking Model 🌟](https://sookocheff.com/post/kubernetes/understanding-kubernetes-networking-model/)
* [build.thebeat.co: A curious case of AWS NLB timeouts in Kubernetes](https://build.thebeat.co/a-curious-case-of-aws-nlb-timeouts-in-kubernetes-522bd88a3399) A debugging adventure that allowed us to solve the tail latencies our Kubernetes applications were experiencing when talking with our AWS NLB.
* [dzone: Multizone Kubernetes and VPC Load Balancer Setup](https://dzone.com/articles/multizone-kubernetes-and-vpc-load-balancer-setup) Securely expose your Kubernetes app by setting up a Load Balancer for VPC in a different zone.
* [ingressbuilder.jetstack.io 🌟🌟](https://ingressbuilder.jetstack.io) Ingress Builder allows users to select any annotation from the list of available controllers, to add to the ingress manifest.
* [itnext.io: Generating Kubernetes Network Policies Automatically By Sniffing Network Traffic 🌟](https://itnext.io/generating-kubernetes-network-policies-by-sniffing-network-traffic-6d5135fe77db) This blog post is about an experiment to automate creation of Kubernetes Network Policies based on actual network traffic captured from applications running on a Kubernetes cluster - [code](https://github.com/mcelep/blog/tree/master/automated-networkpolicy-generation)
* [medium: Using nginx-ingress controller to restrict access by IP (ip whitelisting) for a service deployed to a Kubernetes (AKS) cluster](https://medium.com/@maninder.bindra/using-nginx-ingress-controller-to-restrict-access-by-ip-ip-whitelisting-for-a-service-deployed-to-bd5c86dc66d6)
* [openshift.com: gRPC or HTTP/2 Ingress Connectivity in OpenShift 🌟](https://www.openshift.com/blog/grpc-or-http/2-ingress-connectivity-in-openshift)

### Gateway API
* [gateway-api.sigs.k8s.io 🌟](https://gateway-api.sigs.k8s.io/) Gateway API is an open source project managed by the SIG-NETWORK community. It's is a collection of resources that model service networking in Kubernetes. These resources - GatewayClass,Gateway, HTTPRoute, TCPRoute, Service, etc - aim to evolve Kubernetes service networking through expressive, extensible, and role-oriented interfaces that are implemented by many vendors and have broad industry support.
* [kubernetes.io: Evolving Kubernetes networking with the Gateway API](https://kubernetes.io/blog/2021/04/22/evolving-kubernetes-networking-with-the-gateway-api/)
* [thenewstack.io: Unifying Kubernetes Service Networking (Again) with the Gateway API 🌟](https://thenewstack.io/unifying-kubernetes-service-networking-again-with-the-gateway-api/) The [Gateway API](https://gateway-api.sigs.k8s.io/), formerly known as the Services API and before that Ingress V2, was first discussed in detail — and in-person — at Kubecon 2019 in San Diego. There were already many well-known and [well-documented](https://dave.cheney.net/paste/ingress-is-dead-long-live-ingressroute.pdf) limitations of Ingress and Kubernetes networking APIs. The [Gateway API](https://www.youtube.com/watch?v=GiFQNevrxYA) was intended as a redo of these APIs, built on the lessons from Services, Ingress and the service mesh community.

### Multicloud communication for Kubernetes
* [developers.redhat.com: Use Skupper to connect multiple Kubernetes clusters 🌟](https://developers.redhat.com/blog/2021/04/20/use-skupper-to-connect-multiple-kubernetes-clusters/) - [skupper.io](https://skupper.io/) Multicloud communication for Kubernetes. Skupper is a layer 7 service interconnect. It enables secure communication across Kubernetes clusters with no VPNs or special firewall rules. With Skupper, your application can span multiple cloud providers, data centers, and regions.

### Kubernetes Network Policy
* [howtoforge.com: Network Policy in Kubernetes 🌟](https://www.howtoforge.com/kubernetes_network_policy/) By default, pods accept traffic from any source. A network policy helps to specify how a group of pods can communicate with each other and other network endpoints.
* [medium: How to Provision Network Policies in Kubernetes | AWS 🌟](https://medium.com/avmconsulting-blog/exploring-network-policies-in-kubernetes-c8a3d8ed00cb)
* [learncloudnative.com: Kubernetes Network Policy](https://www.learncloudnative.com/blog/2020-10-07-network-policies)
* [bionconsulting.com: Kubernetes Network Policies](https://www.bionconsulting.com/blog/kubernetes-network-policies)
    * [bionconsulting.com: Kubernetes Network Policies - Part 2](https://www.bionconsulting.com/blog/kubernetes-network-policies-part-2)
* [thenewstack.io: The Kubernetes Network Security Effect 🌟](https://thenewstack.io/the-kubernetes-network-security-effect/) Kubernetes has a built-in object for managing network security: NetworkPolicy. While it allows the user to define the relationship between pods with ingress and egress policies, it is basic and requires very precise IP mapping of a solution — which changes constantly, so most users I’ve talked to are not using it.
* [faun.pub: Control traffic flow to and from Kubernetes pods with Network Policies](https://faun.pub/control-traffic-flow-to-and-from-kubernetes-pods-with-network-policies-bc384c2d1f8c)
* [openshift.com: Network Policies: Controlling Cross-Project Communication on OpenShift](https://www.openshift.com/blog/network-policies-controlling-cross-project-communication-on-openshift)

#### Cilium 
* [cilium.io 🌟](https://cilium.io/) eBPF-based Networking, Observability, and Security
* [cilium.io: NetworkPolicy Editor: Create, Visualize, and Share Kubernetes NetworkPolicies 🌟](https://cilium.io/blog/2021/02/10/network-policy-editor)
* [editor.cilium.io 🌟](https://editor.cilium.io/) Learn how to create Network Policies for Kubernetes using an interactive playground
* [buoyant.io: Kubernetes network policies with Cilium and Linkerd](https://buoyant.io/2020/12/23/kubernetes-network-policies-with-cilium-and-linkerd)

<center>
<script async class="speakerdeck-embed" data-id="9251193501114da199d70b2a679c552f" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
</center>

### Kubernetes Ingress Specification
- [Supporting the Evolving Ingress Specification in Kubernetes 1.18](https://kubernetes.io/blog/2020/06/05/supporting-the-evolving-ingress-specification-in-kubernetes-1.18/)
- [medium: Ingress service types in Kubernetes 🌟](https://medium.com/faun/ingress-service-types-in-kubernetes-3e9b68b78307)

### Xposer Kubernetes Controller To Manage Ingresses
* [Xposer 🌟](https://github.com/stakater/Xposer) A Kubernetes controller to manage (create/update/delete) Kubernetes Ingresses based on the Service
    * Problem: We would like to watch for services running in our cluster; and create Ingresses and generate TLS certificates automatically (optional)
    * Solution: Xposer can watch for all the services running in our cluster; Creates, Updates, Deletes Ingresses and uses certmanager to generate TLS certificates automatically based on some annotations.

### Software-Defined IP Address Management (IPAM)
- [IP Address Management (IPAM)](https://en.wikipedia.org/wiki/IP_address_management)
- [fusionlayer.com: Software-Defined IP Address Management (IPAM)](https://www.fusionlayer.com/products/ip-address-management-software-defined-ipam-infinity)
    - Cloud computing and service automation are changing the way in which applications and data are being delivered and consumed. The existing 30-year-old networking model is failing to keep up with the automated service architectures and the Internet of Things (IoT) based on end-to-end automation.
    - **To facilitate the migration to cloud-era computing, service providers and data centers must add networking into the automated service workflows.** This requires agility and elasticity that traditional networking products are not designed to provide. As IT environments of tomorrow involve a plethora of orchestrators and controllers spinning up services and applications inside shared networks, they all must be managed and provisioned by a unified solution authoritative for all network-related information.

### CNI Container Networking Interface 
* [Kubernetes.io: Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
* [rancher.com: Container Network Interface (CNI) Providers](https://rancher.com/docs/rancher/v2.x/en/faq/networking/cni-providers/)
* [github.com/containernetworking 🌟](https://github.com/containernetworking)
    * [CNI](https://github.com/containernetworking/cni)
* [dzone: How to Understand and Set Up Kubernetes Networking 🌟](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking) Take a look at this tutorial that goes through and explains the inner workings of Kubernetes networking, including working with multiple networks.
* [medium: Container Networking Interface aka CNI](https://medium.com/@vikram.fugro/container-networking-interface-aka-cni-bdfe23f865cf)
* [itnext.io: Benchmark results of Kubernetes network plugins (CNI) over 10Gbit/s network (Updated: August 2020)](https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-august-2020-6e1b757b9e49) 

#### List of existing CNI Plugins (IPAM)
- [Kubernetes Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- Overlay Network plugins:
    - [Flannel](https://github.com/coreos/flannel)
    - [Weave-net](https://www.weave.works/docs/net/latest/overview/)
- Routed Network Plugins:
    - [AWS-VPC](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)
    - [kube-router](https://www.kube-router.io/)
    - [Calico](https://www.projectcalico.org/)
    - [Canal](https://docs.projectcalico.org/getting-started/kubernetes/flannel/flannel)
    - [VMware-tanzu Antrea](https://github.com/vmware-tanzu/antrea)
- [IPAM](https://en.wikipedia.org/wiki/IP_address_management) modules:
    - dhcp
    - host-local
- Multi CNI plugins:
    - [Damn](https://github.com/nokia/danm)
    - [Multus](https://github.com/openshift/multus-cni)
    - [CNI-Genie](https://github.com/cni-genie/CNI-Genie)

<center>
[![kubernetes sdn solutions](images/kubernetes_sdn_solutions.png)](https://thenewstack.io/tigera-aims-ease-connectivity-pain-kubernetes/)
</center>

#### Project Calico
* [tigera.io](https://www.tigera.io/)
* [Project Calico 🌟](https://www.projectcalico.org/) Secure networking for the cloud native era
* [medium: Calico for Kubernetes networking: the basics & examples](https://medium.com/flant-com/calico-for-kubernetes-networking-792b41e19d69)
* [thenewstack.io: Tigera's Calico Aims to Ease Connectivity Pain with Kubernetes](https://thenewstack.io/tigera-aims-ease-connectivity-pain-kubernetes/)
* [projectcalico.org: Advertising Kubernetes Service IPs with Calico and BGP](https://www.projectcalico.org/advertising-kubernetes-service-ips-with-calico-and-bgp/)
* [mhmxs.blogspot.com: Autoscaling Calico Route Reflector topology in Kubernetes](https://mhmxs.blogspot.com/2020/12/autoscaling-calico-route-reflector.html)

### DNS Service with CoreDNS 
- [medium: How to Autoscale the DNS Service in a Kubernetes Cluster](https://medium.com/faun/how-to-autoscale-the-dns-service-in-a-kubernetes-cluster-cbb46ae89678)
- [thenewstack.io: Supercharge CoreDNS with Cluster Addons 🌟](https://thenewstack.io/supercharge-coredns-with-cluster-addons/)
- [sysdig.com: How to monitor coreDNS 🌟](https://sysdig.com/blog/how-to-monitor-coredns/) The most common problems and outages in a Kubernetes cluster come from coreDNS, so learning how to monitor coreDNS is crucial.

### Kubernetes Node Local DNS Cache
- [NodeLocal DNSCache](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/20190424-NodeLocalDNS-beta-proposal.md)
- [Kubernetes Node Local DNS Cache](https://povilasv.me/kubernetes-node-local-dns-cache/)

## Kubernetes Sidecars
* [banzaicloud.com: Sidecar container lifecycle changes in Kubernetes 1.18 🌟](https://banzaicloud.com/blog/k8s-sidecars/)
* [medium: Delaying application start until sidecar is ready](https://medium.com/@marko.luksa/delaying-application-start-until-sidecar-is-ready-2ec2d21a7b74) Taking advantage of a peculiar Kubernetes implementation detail to block containers from starting before another container starts.

## Kubernetes Security
* [cilium.io](https://cilium.io/)
* [Dzone - devops security at scale](https://dzone.com/articles/devops-security-at-scale)
* [Dzone - Kubernetes Policy Management with Kyverno](https://dzone.com/articles/kubernetes-policy-management-with-kyverno)
    * [github Kyverno - Kubernetes Native Policy Management](https://github.com/nirmata/kyverno/)
    * [nirmata.com: Auto-labeling Kubernetes resources with Kyverno](https://nirmata.com/2020/10/30/auto-labeling-kubernetes-resources-with-kyverno)
* [Dzone - OAuth 2.0](https://dzone.com/articles/oauth-20-beginners-guide)
* [Kubernetes Security Best Practices 🌟](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire)
* [jeffgeerling.com: Everyone might be a cluster-admin in your Kubernetes cluster](https://www.jeffgeerling.com/blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster)
* [Microsoft.com: Attack matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
* [codeburst.io: 7 Kubernetes Security Best Practices You Must Follow](https://codeburst.io/7-kubernetes-security-best-practices-you-must-follow-ae32f1ed6444)
* [thenewstack.io: Laying the Groundwork for Kubernetes Security, Across Workloads, Pods and Users](https://thenewstack.io/laying-the-groundwork-for-kubernetes-security-across-workloads-pods-and-users/)
* [horovits.wordpress.com: Kubernetes Security Best Practices](https://horovits.wordpress.com/2020/07/15/kubernetes-security-best-practices/)
* [containerjournal.com: How to Secure Your Kubernetes Cluster 🌟](https://containerjournal.com/topics/container-security/how-to-secure-your-kubernetes-cluster/)
* [medium: How to Harden Your Kubernetes Cluster for Production 🌟](https://medium.com/better-programming/how-to-harden-your-kubernetes-cluster-for-production-7e47990efc2a)
* [kubernetes.io: Cloud native security for your clusters](https://kubernetes.io/blog/2020/11/18/cloud-native-security-for-your-clusters/)
* [tldrsec.com: Risk8s Business: Risk Analysis of Kubernetes Clusters 🌟](https://tldrsec.com/guides/kubernetes/) A zero-to-hero guide for assessing the security risk of your Kubernetes cluster and hardening it.
* [microsoft.com: Threat matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
* [labs.bishopfox.com: Bad Pods: Kubernetes Pod Privilege Escalation 🌟](https://labs.bishopfox.com/tech-blog/bad-pods-kubernetes-pod-privilege-escalation) What are the risks associated with overly permissive pod creation in Kubernetes? The answer varies based on which of the host’s namespaces and security contexts are allowed. In this post, I will describe eight insecure pod configurations and the corresponding methods to perform privilege escalation. This article and the accompanying repository were created to help penetration testers and administrators better understand common misconfiguration scenarios.
* [sysdig.com: Kubernetes Security Guide 🌟](https://sysdig.com/resources/ebooks/kubernetes-security-guide/) Best practices, guidance and steps for implementing Kubernetes security.
* [resources.whitesourcesoftware.com: Kubernetes Security Best Practices 🌟](https://resources.whitesourcesoftware.com/blog-whitesource/kubernetes-security)
* [sysdig.com: Getting started with Kubernetes audit logs and Falco 🌟](https://sysdig.com/blog/kubernetes-audit-log-falco/)
* [thenewstack.io: Jetstack Secure Promises to Ease Kubernetes TLS Security](https://thenewstack.io/jetstack-secure-promises-to-ease-kubernetes-tls-security/)
* [thenewstack.io: Best Practices for Securely Setting up a Kubernetes Cluster](https://thenewstack.io/best-practices-for-securely-setting-up-a-kubernetes-cluster/)
* [stackrox/Kubernetes_Security_Specialist_Study_Guide 🌟](https://github.com/stackrox/Kubernetes_Security_Specialist_Study_Guide)
* [thenewstack.io: A Security Comparison of Docker, CRI-O and Containerd 🌟](https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd/)
* [github.com/stackrox: Certified Kubernetes Security Specialist Study Guide 🌟](https://github.com/stackrox/Kubernetes_Security_Specialist_Study_Guide)
* [youtube: Kubernetes Security: Attacking and Defending K8s Clusters - by Magno Logan](https://www.youtube.com/watch?v=OOHmg1J_8ck&ab_channel=RedTeamVillage)
* [cncf.io: Kubernetes Security 🌟](https://www.cncf.io/blog/2021/03/22/kubernetes-security/)
* [microsoft.com: Secure containerized environments with updated threat matrix for Kubernetes](https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes/)
* [kyverno.io 🌟](https://kyverno.io/) Kubernetes Native Policy Management. Open Policy Agent? That’s old school. Securely manage workloads on your kubernetesio clusters with this handy new tool, Kyverno.Kyverno is a policy engine designed for Kubernetes. With Kyverno, policies are managed as Kubernetes resources and no new language is required to write policies. This allows using familiar tools such as kubectl, git, and kustomize to manage policies. Kyverno policies can validate, mutate, and generate Kubernetes resources. The Kyverno CLI can be used to test policies and validate resources as part of a CI/CD pipeline. [youtube: The Way of the Future | Kubernetes Policy Management with Kyverno](https://www.youtube.com/watch?v=8fgrjBnxqi0&t=270s&ab_channel=AppSecEngineer) - [youtube: Securing and Automating Kubernetes with Kyverno](https://www.youtube.com/watch?v=0cJAfmQ7Emg&ab_channel=CloudNativeIslamabad)
* [cyberark.com: Attacking Kubernetes Clusters Through Your Network Plumbing: Part 1](https://www.cyberark.com/resources/threat-research-blog/attacking-kubernetes-clusters-through-your-network-plumbing-part-1?utm_sq=goa40uvlx1)
* [redkubes.com: 10 Kubernetes Security Risks & Best Practices](https://redkubes.com/10-kubernetes-security-risks-best-practices/)
* [thenewstack.io: Defend the Core: Kubernetes Security at Every Layer](https://thenewstack.io/defend-the-core-kubernetes-security-at-every-layer/)
* [techmanyu.com: Kubernetes Security with Kube-bench and Kube-hunter 🌟](https://www.techmanyu.com/kubernetes-security-with-kube-bench-and-kube-hunter-6765bf44ebc6)
    * [kube-bench 🌟](https://github.com/aquasecurity/kube-bench) Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
    * [kube-hunter 🌟](https://github.com/aquasecurity/kube-hunter) Hunt for security weaknesses in Kubernetes clusters
* [Analyze Kubernetes Audit logs using Falco 🌟](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster) Detect intrusions that happened in your Kubernetes cluster through audit logs using Falco
* [blog.kasten.io: Kubernetes Ransomware Protection with Kasten K10 v4.0](https://blog.kasten.io/ransomware-protection-kasten-k10-v4)
* [helpnetsecurity.com: Kubestriker: A security auditing tool for Kubernetes clusters 🌟](https://www.helpnetsecurity.com/2021/05/04/security-kubernetes/) Kubestriker is an open-source, platform-agnostic tool for identifying security misconfigurations in Kubernetes clusters.
* [Kubernetes Goat 🌟](https://madhuakula.com/kubernetes-goat) is designed to be an intentionally vulnerable cluster environment to learn and practice Kubernetes security.
* [itnext.io: How-To: Kubernetes Cluster Network Security 🌟](https://itnext.io/how-to-kubernetes-cluster-network-security-f19bc99161f5)
* [gist.github.com: How to protect your ~/.kube/ configuration](https://gist.github.com/PatrLind/e651d3cbc3bf68e4bd9fcc9568cbd3fb)
* [levelup.gitconnected.com: Enforce Audit Policy in Kubernetes (k8s)](https://levelup.gitconnected.com/enforce-audit-policy-in-kubernetes-k8s-34e504733300)
* [snyk.io: 10 Kubernetes Security Context settings you should understand](https://snyk.io/blog/10-kubernetes-security-context-settings-you-should-understand/)
* [magalix.com: Top 8 Kubernetes Security Best Practices 🌟](https://www.magalix.com/blog/top-8-kubernetes-security-best-practices)
* [redhat.com: The State of Kubernetes Security](https://www.redhat.com/en/blog/state-kubernetes-security)

### Service Accounts
* Service account is an important concept in terms of Kubernetes security. You can relate it to AWS instance roles and google cloud instance service account if you have a cloud background. By default, every pod gets assigned a default service account if you don't specify a custom service account. Service account allows pods to make calls to the API server to manage the cluster resources using ClusterRoles or resources scoped to a namespace using Roles. Also, you can use the Service account token from external applications to make API calls to the kubernetes API server. 
    * [devopscube.com: How To Create Kubernetes Service Account For API Access](https://devopscube.com/kubernetes-api-access-service-account/)
    * [devopscube.com: How to Create kubernetes Role for Service Account](https://devopscube.com/create-kubernetes-role/)
    * [github.com/scriptcamp/kubernetes-serviceaccount-example](https://github.com/scriptcamp/kubernetes-serviceaccount-example) Example Kubernetes manifests to create service account mapped to Rolebinding.
* [medium: Working with Service Account In Kubernetes 🌟](https://medium.com/the-programmer/working-with-service-account-in-kubernetes-df129cb4d1cc) How to configure a service account in Kubernetes and manage it?
* [github.com/dvob/k8s-s2s-auth: Kubernetes Service Accounts 🌟](https://github.com/dvob/k8s-s2s-auth) Service accounts are well known in Kubernetes to access the Kubernets API from within the cluster. This is often used for infrastructure components like operators and controllers. But we can also use service accounts to implement authentication in our own applications. This README tries to give an overview on how service accounts work and and shows a couple of variants how you can use them for authentication. Further this repository contains an example Go service which shows how to implement the authentication in an application.
* [sandeepbaldawa.medium.com: Service Accounts in K8s (Kubernetes)](https://sandeepbaldawa.medium.com/service-accounts-in-k8s-kubernetes-2779ee4fb331)

### Kubernetes Secrets
- [cncf.io: Revealing the secrets of Kubernetes secrets 🌟](https://www.cncf.io/blog/2021/04/22/revealing-the-secrets-of-kubernetes-secrets) In this article you will learn how to protect Secrets in your Kubernetes cluster
- [Hands on your first Kubernetes secrets 🌟](https://www.padok.fr/en/blog/kubernetes-secrets)
- [dev.to: Store your Kubernetes Secrets in Git thanks to Kubeseal. Hello SealedSecret! 🌟](https://dev.to/stack-labs/store-your-kubernetes-secrets-in-git-thanks-to-kubeseal-hello-sealedsecret-2i6h)
- [blog.doit-intl.com: Kubernetes and Secrets Management in the Cloud](https://blog.doit-intl.com/kubernetes-and-secrets-management-in-cloud-858533c20dca)
- [itnext.io: Effective Secrets with Vault and Kubernetes](https://itnext.io/effective-secrets-with-vault-and-kubernetes-9af5f5c04d06)  

### Encrypting the certificate for Kubernetes. SSL certificates with Let's Encrypt in Kubernetes Ingress via cert-manager
* [Kubernetes Certs](https://github.com/jetstack/cert-manager/)
* [Using SSL certificates from Let’s Encrypt in your Kubernetes Ingress via cert-manager 🌟](https://medium.com/flant-com/cert-manager-lets-encrypt-ssl-certs-for-kubernetes-7642e463bbce)
* [medium: Encrypting the certificate for Kubernetes (Let’s Encrypt) 🌟](https://medium.com/avmconsulting-blog/encrypting-the-certificate-for-kubernetes-lets-encrypt-805d2bf88b2a)
* [rejupillai.com: Let’s Encrypt the Web (for free)](https://www.rejupillai.com/index.php/2021/03/06/configure-tls-on-gke-ingress-for-free-with-lets-encrypt/)
* [betterprogramming.pub: Kubernetes and SSL Certificate Management 🌟](https://betterprogramming.pub/kubernetes-and-ssl-certificate-management-5f6a4b6f5ae9) Manage SSL certificate orders in K8s with Helm and Let’s Encrypt. 
 
<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/OAuth?src=hash&amp;ref_src=twsrc%5Etfw">#OAuth</a> has 4 Flows for retrieving an Access Token.<br><br>If you have worked with it, you know how difficult is it to remember what is what.<br><br>A Zine says a lot, seriously a lot. Check this out.<br>Idea credits <a href="https://twitter.com/b0rk?ref_src=twsrc%5Etfw">@b0rk</a> <a href="https://twitter.com/hashtag/IAM?src=hash&amp;ref_src=twsrc%5Etfw">#IAM</a> <a href="https://twitter.com/hashtag/security?src=hash&amp;ref_src=twsrc%5Etfw">#security</a> <a href="https://twitter.com/hashtag/infosec?src=hash&amp;ref_src=twsrc%5Etfw">#infosec</a> <a href="https://twitter.com/hashtag/webdev?src=hash&amp;ref_src=twsrc%5Etfw">#webdev</a> <a href="https://twitter.com/hashtag/web?src=hash&amp;ref_src=twsrc%5Etfw">#web</a> <a href="https://twitter.com/hashtag/webcomic?src=hash&amp;ref_src=twsrc%5Etfw">#webcomic</a> <a href="https://twitter.com/hashtag/webcomics?src=hash&amp;ref_src=twsrc%5Etfw">#webcomics</a> <br>RT if useful <a href="https://t.co/fbrls0V08K">pic.twitter.com/fbrls0V08K</a></p>&mdash; Rohit (@sec_r0) <a href="https://twitter.com/sec_r0/status/1347603985096724493?ref_src=twsrc%5Etfw">January 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

### RBAC
* [Configure RBAC in Kubernetes Like a Boss 🌟](https://medium.com/trendyol-tech/configure-rbac-in-kubernetes-like-a-boss-665e2a8665dd) Learn how to configure RBAC in kubernetes. In this post, you will configure RBAC both with kubectl and yaml definitions.
* [infracloud.io: How to setup Role based access (RBAC) to Kubernetes Cluster 🌟](https://www.infracloud.io/blogs/role-based-access-kubernetes)
* [Kubernetes RBAC Permission Manager 🌟](https://toolbox.kali-linuxtr.net/kubernetes-rbac-permission-manager.tool)
* [Krane 🌟](https://github.com/appvia/krane) is a Kubernetes RBAC static analysis tool. It identifies potential security risks in K8s RBAC design and makes suggestions on how to mitigate them. Krane dashboard presents current RBAC security posture and lets you navigate through its definition.

### Admission Control 
- [blog.styra.com: Why RBAC is not enough for kubernetes security 🌟🌟](https://blog.styra.com/blog/why-rbac-is-not-enough-for-kubernetes-api-security)

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

<center>
[![kubernetes security controls landscape](images/kubernetes-security-controls-landscape.jpg)](https://www.stackrox.com/post/2020/05/kubernetes-security-101/)
</center>

### Kubernetes Authentication and Authorization
* [kubernetes.io: Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)
* [kubernetes.io: Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
* [kubernetes.io: Accesing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/)
* [magalix.com: kubernetes authentication 🌟](https://www.magalix.com/blog/kubernetes-authentication)
* [magalix.com: kubernetes authorization 🌟](https://www.magalix.com/blog/kubernetes-authorization)
* [kubernetes login](https://blog.christianposta.com/kubernetes/logging-into-a-kubernetes-cluster-with-kubectl/)
* [learnk8s.io: Authentication between microservices using Kubernetes identities 🌟](https://learnk8s.io/microservices-authentication-kubernetes)

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
* [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 1](https://rancher.com/blog/2020/pod-security-policies-part-1)
    * [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 2](https://rancher.com/blog/2020/pod-security-policies-part-2)
* [developer.squareup.com: Kubernetes Pod Security Policies (PSP)](https://developer.squareup.com/blog/kubernetes-pod-security-policies/) an example with exception management
* [itnext.io: Implementing a Secure-First Pod Security Policy Architecture](https://itnext.io/implementing-a-restricted-first-pod-security-policyarchitecture-af4e906593b0)
* [Neon Mirrors: Kubernetes Policy Comparison: OPA/Gatekeeper vs Kyverno](https://kind-brown-cfb734.netlify.app/post/2021-02/kubernetes-policy-comparison-opa-gatekeeper-vs-kyverno/)

### EKS Security
* [Security Group Rules EKS](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
* [EC2 ENI and IP Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)
* [Calico in EKS](https://docs.aws.amazon.com/eks/latest/userguide/calico.html )
* [Amazon EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/)
    * [EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/iam/)
* [medium.com: Securing Kubernetes Dashboard on EKS with Pomerium](https://medium.com/dev-genius/securing-kubernetes-dashboard-on-eks-with-pomerium-e98c47610e2f)

## Kubernetes Scheduling and Scheduling Profiles
* [Kubernetes Scheduling](https://kubernetes.io/docs/reference/scheduling/)
* [Scheduling Profiles](https://kubernetes.io/docs/reference/scheduling/profiles/)

### Assigning Pods to Nodes. Pod Affinity and Anti-Affinity 
* [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)

### Pod Topology Spread Constraints and PodTopologySpread Scheduling Plugin
* [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/)
* [Introducing PodTopologySpread plugin](https://kubernetes.io/blog/2020/05/introducing-podtopologyspread/)

## Kubernetes etcd
- [medium: How to modify etcd data of your Kubernetes directly (without K8s API)](https://medium.com/flant-com/modifying-kubernetes-etcd-data-ed3d4bb42379)
- [medium: Getting Started with Kubernetes etcd](https://medium.com/@Alibaba_Cloud/getting-started-with-kubernetes-etcd-a26cba0b4258)
- [sysdig.com: How to monitor etcd 🌟](https://sysdig.com/blog/monitor-etcd/) Learning how to monitor etcd is of vital importance when running Kubernetes in production. Monitoring etcd will let you validate that things work as expected, while detecting and troubleshooting issues that could take your entire infrastructure down.

## Kubernetes Storage
- [Cloud Native Storage](storage.md)
* [itnext.io: Kubernetes: PersistentVolume and PersistentVolumeClaim — an overview with examples](https://itnext.io/kubernetes-persistentvolume-and-persistentvolumeclaim-an-overview-with-examples-3c5688222f99) 
* [thenewstack.io: How Kubernetes provides networking and storage to applications](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications/)

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

## Non-production Kubernetes Local Installers. Kubernetes distributions for local environments
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
    * [itnext.io: How to experiment locally on Kubernetes with minikube and your local Dockerfiles](https://itnext.io/how-to-experiment-locally-on-kubernetes-with-minikube-and-your-local-dockerfiles-48833fcd90c9)
* [**kind**](https://github.com/kubernetes-sigs/kind) Kubernetes IN Docker - local clusters for testing Kubernetes
    * [kubernetes-development-environment-in-a-box](https://github.com/ManagedKube/kubernetes-development-environment-in-a-box) This project is geared toward running multiple isolated KinD cluster on a single instance. This project produces an AMI image that can run an instance that has Docker and multiple isolated Kubernetes clusters running in it using KinD. The main use case is to setup one node that can run multiple fully isolated Kubernetes cluster on it for development purposes.
* [store.docker.com: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [medium.com: Local Kubernetes for Linux — MiniKube vs MicroK8s](https://medium.com/containers-101/local-kubernetes-for-linux-minikube-vs-microk8s-1b2acad068d3)
* [itnext.io: Run Kubernetes On Your Machine](https://itnext.io/run-kubernetes-on-your-machine-7ee463af21a2) Several options to start playing with K8s in no time
* [padok.fr: MiniKube, Kubeadm, Kind, K3S, how to get started on Kubernetes?](https://www.padok.fr/en/blog/minikube-kubeadm-kind-k3s)
* [loft.sh: Kubernetes Development Environments – A Comparison](https://loft.sh/blog/kubernetes-development-environments-comparison/)
* [opensource.com: 4 ways to run Kubernetes locally](https://opensource.com/article/20/11/run-kubernetes-locally) Set up a local development environment or just try out the container orchestration platform with these tools.
* [dex.dev: Local Development Clusters](https://www.dex.dev/dex-videos/development-clusters)
* [itnext.io: Kubernetes local playground alternatives](https://itnext.io/kubernetes-local-playground-alternatives-e1a590632b9f)
* [dex.dev: Local Development Clusters](https://www.dex.dev/dex-videos/development-clusters)
* [blog.radwell.codes: What’s the best Kubernetes distribution for local environments? 🌟](https://blog.radwell.codes/2021/05/best-kubernetes-distribution-for-local-environments/)

### Telepresence local development for k8s and openshift microservices
* [telepresence.io 🌟](https://www.telepresence.io) Fast, local development for kubernetes and openshift microservices.
* [telepresence.io: Debug a Kubernetes service locally 🌟](https://www.telepresence.io/tutorials/kubernetes) Imagine you have a service running in a cluster, and someone reports a bug. You want to run the service locally but how? Enter Telepresence

## Managed Kubernetes in Public Cloud
* [infoworld.com: 6 reasons to switch to managed Kubernetes](https://www.infoworld.com/article/3614605/6-reasons-to-switch-to-managed-kubernetes.html) Managed Kubernetes services have matured to the point where many enterprises are handing over the keys to their clusters. Here we identify some of the main drivers behind that trend.

### GKE vs EKS vs AKS
* [medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS](https://medium.com/@Platform9Sys/kubernetes-cloud-services-comparing-gke-eks-and-aks-1fe42770cad3)
* [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.com/post/2020/02/eks-vs-gke-vs-aks/)
* [youtube: Kubernetes Comparison](https://www.youtube.com/watch?v=xM9jpcVGTzY) A beautiful comparison of Kubernetes Services from GCP, AWS and Azure by learnk8s.
    * [learnk8s.io/research:  Comparison of Kubernetes managed services 🌟](https://learnk8s.io/research)
* [medium: State of Managed Kubernetes 2020](https://medium.com/swlh/state-of-managed-kubernetes-2020-4be006643360) EKS vs. AKS vs. GKE from a Developer’s Perspective
* [medium: Managed Kubernetes Services Compared: GKE vs. EKS vs. AKS](https://medium.com/better-programming/managed-kubernetes-services-compared-gke-vs-eks-vs-aks-df1ecb22bba0) Comparing the three most popular managed Kubernetes platforms in features and overall experience.
* [acloudguru.com: AKS vs EKS vs GKE: Managed Kubernetes services compared](https://acloudguru.com/blog/engineering/aks-vs-eks-vs-gke-managed-kubernetes-services-compared)

### Other Managed Kubernetes
- [thenewstack.io: Otomi Container Platform Offers an Integrated Kubernetes Bundle](https://thenewstack.io/otomi-container-platform-offers-an-integrated-kubernetes-bundle/) If you want to enjoy the benefits of Kubernetes, configuring and installing the software itself can be just the first of many deeply technical and oftentimes confusing steps. To simplify this, many major cloud providers offer managed Kubernetes services, but even then you may need to install secondary services to handle tasks such as tracing, logging, monitoring, identity access management, and so on. The Otomi Container Platform looks to address this complexity by bundling together more than 30 different Kubernetes add-ons, as well as providing what it calls an “OSX like interface,” and today the project has open sourced a community edition under the Apache 2.0 license.
    - [otomi.io 🌟](https://otomi.io/)

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
* [Deploying Infrastructure (FrontEnd + BackEnd) on AWS using Amazon EKS](https://medium.com/@ghumare64/deploying-infrastructure-frontend-backend-on-aws-using-amazon-eks-5f1f426d618e)
* [EKS Service Accounts Explained](https://fika.works/blog/eks-service-accounts/) In AWS you can assign IAM permissions to pods in your cluster. This article explains how it works.
* [medium: Building the CI/CD of the Future, Creating the EKS Cluster 🌟](https://medium.com/swlh/building-the-ci-cd-of-the-future-creating-the-eks-cluster-e4cce4eb3500)
* [Announcing the AWS Controllers for Kubernetes Preview](https://aws.amazon.com/about-aws/whats-new/2020/08/announcing-the-aws-controllers-for-kubernetes-preview/)
* [daveops.xyz: Administrar usuarios en EKS](https://daveops.xyz/2020/08/25/administrar-usuarios-en-eks/)
* [aws.github.io: AWS Controllers for Kubernetes](https://aws.github.io/aws-controllers-k8s/)
* [stacksimplify.com: AWS ALB Ingress Service - Basics 🌟](https://www.stacksimplify.com/aws-eks/aws-alb-ingress/lean-kubernetes-aws-alb-ingress-basics/)
* [Kubernetes PVCs with EFS provisioner](https://www.padok.fr/en/blog/efs-provisioner-kubernetes)
* [Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
* [Running spot instances effectively with Amazon EKS](https://m.signalvnoise.com/running-spot-instances-effectively-with-amazon-eks)
* [medium: Designing a Kubernetes Cluster with Amazon EKS From Scratch 🌟](https://medium.com/adobetech/designing-a-kubernetes-cluster-with-amazon-eks-from-scratch-4b4ee9d1b8f)
* [en.sokube.ch: AWS + Kubernetes = AWS Elastic Kubernetes Service (EKS) 🌟](https://en.sokube.ch/post/aws-kubernetes-aws-elastic-kubernetes-service-eks)
* [aws.amazon.com: Operating a multi-regional stateless application using Amazon EKS](https://aws.amazon.com/blogs/containers/operating-a-multi-regional-stateless-application-using-amazon-eks/)
* [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform 🌟](https://www.clickittech.com/aws/amazon-ecs-vs-eks/)
* [POKE - Provision Opinionated Kubernetes on EKS](https://github.com/bit-cloner/poke) Poke is infrastructure as software to provision EKS cluster in an opinianated way. Code is written in nodejs utilising pulumi framework. It is opinionated in such a way to improve security and simplicity.Consider this similar to terraform module. This package can be used to provision eks clusters declaratively with immutability and repeatability.
* [clickittech.com: Kubernetes Multi tenancy with Amazon EKS: Best practices and considerations](https://www.clickittech.com/saas/kubernetes-multi-tenancy/)
* [automateinfra.com: Getting Started with Amazon Elastic kubernetes Service (AWS EKS)](https://automateinfra.com/2021/04/01/the-only-ultimate-for-beginners-getting-started-with-amazon-eks/)
* [medium: Run Kubernetes Production Environment on EC2 Spot Instances With Zero Downtime: A Complete Guide](https://medium.com/riskified-technology/run-kubernetes-on-aws-ec2-spot-instances-with-zero-downtime-f7327a95dea)
* [releaseops.io: Scaling Kubernetes Deployments in AWS with Container Insights Metrics](https://releaseops.io/blog/scaling-kubernetes-deployments-in-aws-with-container-insights-metrics)

### Kubesphere
- [kubesphere.io](https://kubesphere.io/) The Kubernetes platform tailored for hybrid multicloud. KubeSphere is a distributed operating system managing cloud native applications with Kubernetes as its kernel, and provides plug-and-play architecture for the seamless integration of third-party applications to boost its ecosystem.
- [kubekey](https://github.com/kubesphere/kubekey) The Next-gen Installer: Installing Kubernetes and KubeSphere v3.0.0 fastly, flexibly and easily
- [kubesphere.io: Scaling a Kubernetes Cluster: One of the Best Practices for Using KubeKey](https://kubesphere.io/blogs/scale-kubernetes-cluster-using-kubekey/)
- [itnext.io: Adding Master Nodes to Achieve HA: One of the Best Practices for Using KubeKey](https://itnext.io/adding-master-nodes-to-achieve-ha-one-of-the-best-practices-for-using-kubekey-6207e94b0bdd)
- [youtube: Create a Jenkins Pipeline on Kubernetes with CI/CD Pipeline Template in KubeSphere](https://www.youtube.com/watch?v=MU5LdM83x9s&t=40s&ab_channel=KubeSphere) Two built-in Jenkins pipeline templates are available in KubeSphere 3.1. DevOps team can generate CICD or customize the workflow as you need by simple drag-and-drop.

### Tools for multi-cloud Kubernetes management
- [Banzai Cloud 🌟](https://banzaicloud.com/)
    - [Kubernetes node pool upgrades with Banzai Pipeline](https://banzaicloud.com/blog/kubernetes-nodepool-upgrades/)
- [Compare tools for multi-cloud Kubernetes management 🌟](https://searchcloudcomputing.techtarget.com/tip/Compare-tools-for-multi-cloud-Kubernetes-management)
    - NetApp Kubernetes Service -- formerly StackPointCloud
    - Cloudify
    - Terraform
    - Rancher
    - Platform9 Managed Kubernetes 
    - Red Hat OpenShift
    - Juke, from HTBase, now owned by Juniper Networks. 

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

### Deploying Kubernetes Cluster with Kubeadm
* [Kubernetes Cluster with **Kubeadm**](https://github.com/kubernetes/kubeadm) It works on any deb / rpm compatible Linux OS, for example Ubuntu, Debian, RedHat or CentOS. This is the main advantage of kubeadm. The tool itself is still in beta (Q1 2018), but is expected to become stable somewhere this year. It's very easy to use and lets you spin kubernetes cluster in just a couple of minutes.
* [medium.com: **Demystifying High Availability in Kubernetes Using Kubeadm**](https://medium.com/velotio-perspectives/demystifying-high-availability-in-kubernetes-using-kubeadm-3d83ed8c458b)
* [Setting Up a Kubernetes Cluster on Ubuntu 18.04](https://loves.cloud/setting-up-a-kubernetes-cluster-on-ubuntu-18-04/)
* [itnext.io: Up and running out of the cloud — How to setup the Masters using kubeadm bootstrap](https://itnext.io/kubernetes-journey-up-and-running-out-of-the-cloud-how-to-setup-the-masters-using-kubeadm-9a496a14fbc1) In this article, you’ll see how to make use of kubeadm bootstrap to set up and join 3 master instances as members of our cluster.
* [Set up a Bare Metal Kubernetes cluster with ](https://www.padok.fr/en/blog/kubeadm-kubernetes-cluster)
* [blog.tobias-huebner.org: Low-budget self-hosted Kubernetes 🌟](https://blog.tobias-huebner.org/low-budget-kubernetes-self-hosted-series/)
* [mirantis.com: How to install Kubernetes with Kubeadm: A quick and dirty guide](https://www.mirantis.com/blog/how-install-kubernetes-kubeadm)
* [kosyfrances.com: Using kubeadm to create a Kubernetes 1.20 cluster on VirtualBox with Ubuntu](https://kosyfrances.com/kubernetes-cluster/)

### Deploying Kubernetes Cluster with Ansible 
- [Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes)
- [krd](https://github.com/electrocucaracha/krd) offers a reference for deploying a Kubernetes cluster. Its ansible playbooks allow to provision a deployment on Bare-metal or Virtual Machines
- [Kubeinit 🌟](https://github.com/kubeinit/kubeinit) KubeInit provides Ansible playbooks and roles for the deployment and configuration of multiple Kubernetes distributions. KubeInit's mission is to have a fully automated way to deploy in a single command a curated list of prescribed architectures.
    - [youtube: OpenShift Commons En Vivo - KubeInit con Maria Bracho, Scott McCarty, and Carlos Camacho (Red Hat, Spanish) 🌟](https://www.youtube.com/watch?v=9_6H7Ahsdm4&ab_channel=OpenShift)

### kube-aws Kubernetes on AWS
- [Kubernetes on AWS (kube-aws)](https://kubernetes-incubator.github.io/kube-aws/) A command-line tool to declaratively manage Kubernetes clusters on AWS

### Kubespray
- [**Kubespray**](https://github.com/kubernetes-sigs/kubespray)
- [redhat.com: An introduction to Kubespray](https://www.redhat.com/sysadmin/kubespray-deploy-kubernetes) By combining Ansible and Kubernetes, Kubespray can deploy Kubernetes clusters on multiple machines.

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
* [medium: Upgrading Kubernetes The Hard Way](https://medium.com/nordcloud-engineering/upgrading-kubernetes-the-hard-way-ac533cfb4ff2)
* [Monzo: we learned a lot from self-hosting Kubernetes, but we wouldn't do it again](https://www.computing.co.uk/news/4019233/monzo-learned-lot-self-hosting-kubernetes-wouldn%E2%80%99) Don't need to do it the hard way anymore
* [medium: Kubernetes the hard way on Docker](https://medium.com/@brightzheng100/kubernetes-the-hard-way-on-docker-f512bae734af)
* [Autoscalable Kubernetes cluster at Exoscale, using Packer and Terraform](https://github.com/PhilippeChepy/exoscale-kubernetes-crio)
* [Kubernetes the Hard Way: Azure Edition](https://github.com/carlosonunez/kubernetes-the-hard-way-on-azure) teaches you how to deploy Kubernetes from scratch on Azure based on the legendary Kubernetes the Hard Way.
* [Kubernetes The Hard Way: AWS Edition](https://github.com/prabhatsharma/kubernetes-the-hard-way-aws) AWS version of Kelsey's kubernetes-the-hard-way

### Caravan
- [linecorp.com: Building Large Kubernetes Clusters with **Caravan**](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters/)

### ClusterAPI
- [**ClusterAPI**](https://cluster-api.sigs.k8s.io/)
- [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89)
- [medium: ClusterOps: 1-Line Commit to Upgrade Your Kubernetes Clusters 🌟](https://medium.com/swlh/clusterops-1-line-commit-to-upgrade-your-kubernetes-clusters-de3548124d04)
- [cncf.io webinar: Deploying Kubernetes to bare metal using cluster API](https://www.cncf.io/webinars/deploying-kubernetes-to-bare-metal-using-cluster-api/)
- [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89)
- [github.com: Cluster API Helm Chart](https://github.com/kgamanji/cluster-api-helm-chart) - [youtube: Cluster API & FluxCD - the power of GitOps](https://www.youtube.com/watch?v=QbSw8dPhHGM&ab_channel=KatieGamanji) A Helm chart to install Cluster API manifests

### Microk8s
- [**Microk8s**](https://microk8s.io/)
- [Kata Containers on MicroK8s](https://github.com/didier-durand/microk8s-kata-containers) This repository encompasses a fully scripted Github workflow to test the transparent use of the runtime for Kata Containers (Katas) on MicroK8s
- [MicroK8s & Kubernetes security benchmark from CIS](https://github.com/didier-durand/microk8s-kube-bench)

### k8s-tew
- [**k8s-tew**](https://github.com/darxkies/k8s-tew) Kubernetes is a fairly complex project. For a newbie it is hard to understand and also to use. While [Kelsey Hightower’s Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way), on which this project is based, helps a lot to understand Kubernetes, it is optimized for the use with Google Cloud Platform.

### Kubernetes Distributions
- [acloudguru.com: Which Kubernetes distribution is right for you?](https://acloudguru.com/blog/engineering/which-kubernetes-distribution-is-right-for-you)
#### Red Hat OpenShift 
* [Openshift Container Platform](openshift.md)
* [OKD](https://www.okd.io/) The Community Distribution of Kubernetes that powers Red Hat OpenShift

#### Rancher
* [Rancher: Enterprise management for Kubernetes](rancher.md)

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
* [tanzu.vmware.com: VMware Tanzu SQL: MySQL at Scale Made Easy for Kubernetes](https://tanzu.vmware.com/content/blog/vmware-tanzu-sql-mysql-at-scale-kubernetes)

##### KubeAcademy Pro (free training)
* [tanzu.vmware.com: Introducing KubeAcademy Pro: In-Depth Kubernetes Training, Totally Free](https://tanzu.vmware.com/content/blog/introducing-kubeacademy-pro-in-depth-kubernetes-training-totally-free)
* [kube.academy/pro 🌟](https://kube.academy/pro)

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

#### Mirantis k0s
- [k0s](https://k0sproject.io/)
- [infoq.com: Mirantis Announces k0s, a New Kubernetes Distribution](https://www.infoq.com/news/2020/12/k0s-kubernetes-distribution/)

#### K0s
- [K0s - Zero Friction Kubernetes](https://github.com/k0sproject/k0s) k0s is an all-inclusive Kubernetes distribution with all the required bells and whistles preconfigured to make building a Kubernetes clusters a matter of just copying an executable to every host and running it.
- [medium: k0s Ready for Production](https://medium.com/k0sproject/k0s-ready-for-production-20255c4b0791)
- [medium: k0s Optimizes Start Time, Adds Cluster Level Backup/Restore and More](https://medium.com/k0sproject/k0s-optimizes-start-time-adds-cluster-level-backup-restore-and-more-8ffef894a1ae)

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

## Multi-Cluster Federation. Hybrid Cloud Setup Tools
### KubeFed
- [KubeFed: Kubernetes Cluster Federation](https://github.com/kubernetes-sigs/kubefed)

### KubeCarrier
- [KubeCarrier](https://github.com/kubermatic/kubecarrier)

### Red Hat Operator Lifecycle Manager (OLM) 
- [Red Hat OLM](https://github.com/operator-framework/operator-lifecycle-manager) operator-lifecycle-manager is a management framework for extending Kubernetes with Operators. OLM extends Kubernetes to provide a declarative way to install, manage, and upgrade Operators and their dependencies in a cluster.

### Crossplane
- [Crossplane](https://crossplane.io/)

### Istio Service Mesh
- [Istio](https://istio.io/)

## Kubernetes interview questions
- [Kubernetes Interview Questions and Answers 2019 2020](https://linux.amitmaheshwari.in/2019/11/kubernetes-interview-questions-and.html)
- [intellipaat.com: Top Kubernetes Interview Questions and Answers](https://intellipaat.com/blog/interview-question/kubernetes-interview-questions-answers/)
- [automationreinvented.blogspot.com: Top 11 Kubernetes interview question and answers for SDET Devops QA SET-01?](https://automationreinvented.blogspot.com/2020/09/top-11-kubernetes-interview-question.html)
- [devsecops.co.in: Kubernetes Interview Questions and Answers](https://devsecops.co.in/2021/05/22/kubernetes-interview/)
- [ymmt2005.hatenablog.com: 47 things that you should know to be a Kubernetes experts (questions + answers)](https://ymmt2005.hatenablog.com/entry/k8s-things)

## Spanish Kubernetes Blogs 
- [returngis.net by @0GiS0](https://www.returngis.net/)
- [returngis.net: Organizar los pods en Kubernetes usando taints y tolerations](https://www.returngis.net/2020/06/organizar-los-pods-en-kubernetes-usando-taints-y-tolerations/)

## Container Ecosystem
* [Author: github.com/rootsongjc](https://github.com/rootsongjc)
  
[![Kubernetes components](images/kubernetes_components_rootsongjc.jpg)](https://github.com/rootsongjc)

## Container Flowchart
* [Assess managed Kubernetes services for your workloads.](https://searchcloudcomputing.techtarget.com/tip/Weigh-the-pros-and-cons-of-managed-Kubernetes-services) Managed services from cloud providers can simplify Kubernetes deployment but create some snags in a multi-cloud model. Follow three steps to see if these services can benefit you.

<center>
[![Container flowchart](images/container_flowchart.jpg)](https://searchcloudcomputing.techtarget.com/tip/Weigh-the-pros-and-cons-of-managed-Kubernetes-services)
</center>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">MEGATHREAD<br><br>Learn Kubernetes one Twitter thread at the time!<br><br>Below you can find a collection of threads about Kubernetes and Kubernetes-related tech!<br><br>I regularly add more, so you can follow me or <a href="https://twitter.com/learnk8s?ref_src=twsrc%5Etfw">@learnk8s</a> for more updates! <a href="https://t.co/0ingxHn9vx">pic.twitter.com/0ingxHn9vx</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1298543151901155330?ref_src=twsrc%5Etfw">August 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD<br><br>Running new apps in Kubernetes is straightforward.<br><br>But what happens when you have legacy apps that:<br><br>- Log to file instead of stdout?<br>- Has no support Prometheus?<br>- Has no support for HTTPS<br><br>Read on → <a href="https://t.co/m79f69Huqw">pic.twitter.com/m79f69Huqw</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1363783405389770752?ref_src=twsrc%5Etfw">February 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m often asked why I prefer zonal Kubernetes clusters over regional clusters. <a href="https://twitter.com/gctaylor?ref_src=twsrc%5Etfw">@gctaylor</a> does a great job explaining how <a href="https://twitter.com/reddit?ref_src=twsrc%5Etfw">@reddit</a> leverages zonal clusters to limit the blast radius of config changes and reduce cross AZ network traffic. <a href="https://t.co/3pW5awTtdQ">https://t.co/3pW5awTtdQ</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1372638634482884608?ref_src=twsrc%5Etfw">March 18, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD<br><br>How do you scale background jobs in Kubernetes?<br><br>With Python, Celery, RabbitMQ and KEDA! <a href="https://t.co/BOtwiSjIKW">pic.twitter.com/BOtwiSjIKW</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1376485484319272966?ref_src=twsrc%5Etfw">March 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

## Kubernetes Scripts
- [Kubernetes Scripts 🌟](https://github.com/eldada/kubernetes-scripts)

## Spot instances in Kubernetes
- [itnext.io: Embracing failures and cutting infrastructure costs: Spot instances in Kubernetes](https://itnext.io/embracing-failures-and-cutting-infrastructure-costs-spot-instances-in-kubernetes-6976781beacc)

## Pixie. Instantly troubleshoot applications on Kubernetes
- [Pixie 🌟](https://docs.pixielabs.ai/) Instantly debug your applications on Kubernetes
- [open source PxL scripts](https://github.com/pixie-labs/pixie/tree/main/pxl_scripts)

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