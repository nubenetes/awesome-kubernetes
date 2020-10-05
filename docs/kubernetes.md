# Kubernetes
- [Certified Kubernetes Offerings](#certified-kubernetes-offerings)
- [The State of Cloud-Native Development. Details data on the use of Kubernetes, serverless computing and more](#the-state-of-cloud-native-development-details-data-on-the-use-of-kubernetes-serverless-computing-and-more)
- [Kubernetes open-source container-orchestation](#kubernetes-open-source-container-orchestation)
    - [Kubernetes Best Practices & Tips](#kubernetes-best-practices--tips)
    - [Disruptions](#disruptions)
    - [Cost Estimation Strategies](#cost-estimation-strategies)
    - [Kubernetes Resource and Capacity Management](#kubernetes-resource-and-capacity-management)
    - [Kubernetes Monitoring](#kubernetes-monitoring)
        - [Logging in Kubernetes](#logging-in-kubernetes)
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
    - [Kubectl Alternatives](#kubectl-alternatives)
        - [Manage Kubernetes (K8s) objects with Ansible Kubernetes Module](#manage-kubernetes-k8s-objects-with-ansible-kubernetes-module)
        - [Jenkins Kubernetes Plugins](#jenkins-kubernetes-plugins)
- [Self Service Kubernetes Namespaces](#self-service-kubernetes-namespaces)
- [Client Libraries for Kubernetes](#client-libraries-for-kubernetes)
- [Helm Kubernetes Tool](#helm-kubernetes-tool)
- [Kubernetes Development Tools. Kubernetes clients and dashboards](#kubernetes-development-tools-kubernetes-clients-and-dashboards)
    - [Lens Kubernetes IDE](#lens-kubernetes-ide)
    - [Kubenav](#kubenav)
    - [Skaffold. Local Kubernetes Development](#skaffold-local-kubernetes-development)
    - [Kind](#kind)
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
            - [Kubectl Plugins and Tools. Kubernetes Extensions & Projects](#kubectl-plugins-and-tools-kubernetes-extensions--projects)
- [Enforcing Policies and governance for kubernetes workloads with Conftest](#enforcing-policies-and-governance-for-kubernetes-workloads-with-conftest)
- [Kubernetes Backup](#kubernetes-backup)
    - [Backup with Velero](#backup-with-velero)
- [Kubernetes Troubleshooting](#kubernetes-troubleshooting)
    - [Debugging Techniques and Strategies. Debugging with ephemeral containers](#debugging-techniques-and-strategies-debugging-with-ephemeral-containers)
- [Kubernetes Tutorials](#kubernetes-tutorials)
    - [Online Training](#online-training)
    - [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019)
    - [Famous Kubernetes resources of 2020](#famous-kubernetes-resources-of-2020)
    - [K8s Diagrams](#k8s-diagrams)
- [Kubernetes Patterns](#kubernetes-patterns)
- [e-Books](#e-books)
    - [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019-1)
    - [Kubernetes Patterns eBooks](#kubernetes-patterns-ebooks)
- [Kubernetes Operators](#kubernetes-operators)
    - [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
    - [K8s KPIs with Kuberhealthy Operator](#k8s-kpis-with-kuberhealthy-operator)
    - [Writing Kubernetes Operators](#writing-kubernetes-operators)
- [Kubernetes Networking](#kubernetes-networking)
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
    - [RBAC](#rbac)
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
- [Non-production Kubernetes Local Installers](#non-production-kubernetes-local-installers)
- [Kubernetes in Public Cloud](#kubernetes-in-public-cloud)
    - [GKE vs EKS vs AKS](#gke-vs-eks-vs-aks)
    - [AWS EKS (Hosted/Managed Kubernetes on AWS)](#aws-eks-hostedmanaged-kubernetes-on-aws)
    - [GCP & GKE](#gcp--gke)
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
        - [Kontena Pharos](#kontena-pharos)
        - [Mirantis Docker Enterprise with Kubernetes and Docker Swarm](#mirantis-docker-enterprise-with-kubernetes-and-docker-swarm)
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
* [learnk8s.io: Load balancing and scaling long-lived connections in Kubernetes 🌟](https://learnk8s.io/kubernetes-long-lived-connections)
* [itnext.io: Successful & Short Kubernetes Stories For DevOps Architects](https://itnext.io/successful-short-kubernetes-stories-for-devops-architects-677f8bfed803)
* [itnext.io: K8s Vertical Pod Autoscaling 🌟](https://itnext.io/k8s-vertical-pod-autoscaling-fd9e602cbf81)
* [medium.com: kubernetes Pod Priority and Preemption](https://medium.com/@mohaamer5/kubernetes-pod-priority-and-preemption-943c58aee07d)
* [returngis.net: Pruebas de vida de nuestros contenedores en Kubernetes](https://www.returngis.net/2020/02/pruebas-de-vida-de-nuestros-contenedores-en-kubernetes/)
* [itnext.io: K8s prevent queue worker Pod from being killed during deployment](https://itnext.io/k8s-prevent-queue-worker-pod-from-being-killed-during-deployment-4252ea7c13f6) How to prevent a Kubernetes (like RabbitMQ) queue worker Pod from being killed during deployment while handling a message?
* [youtube: deployment strategies in kubernetes | recreate | rolling update | blue/green | canary](https://youtu.be/efiMiaFjtn8)
* [kodekloud.com: Kubernetes Features Every Beginner Must Know](https://kodekloud.com/blog/200628/kubernetes-features-every-beginner-must-know)
* [platform9.com: Kubernetes CI/CD Pipelines at Scale](https://platform9.com/blog/kubernetes-ci-cd-pipelines-at-scale/)
* [magalix.com: Capacity Planning 🌟](https://www.magalix.com/blog/kubernetes-patterns-capacity-planning) When we have multiple Pods with different Priority Class values, the admission controller starts by sorting Pods according to their priority. What happens when there are no nodes with available resources to schedule a high-priority pods? 
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
* [Creating a Kubernetes cloud provider, doesn't required boiling the ocean](https://thebsdbox.co.uk/2020/03/18/Creating-a-Kubernetes-cloud-doesn-t-required-boiling-the-ocean/?utm_sq=gf0mhghh60)
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
* [Hands on your first Kubernetes secrets 🌟](https://www.padok.fr/en/blog/kubernetes-secrets)
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

<center>
[![Kubernetes architecture](images/kubernetes-pod-creation.png)](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)

[![10 most common mistakes](images/10_common_kubernetes_mistakes.jpg){: style="width:60%"}](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s)

[![5 Open-source projects that make #Kubernetes even better](images/five-oss-projects-kubernetes.jpg){: style="width:80%"}](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve)

[![kubernetes arch multicloud hybrid](images/kubernetes_architecture_multicloud_hybride.jpg){: style="width:70%"}](https://www.journaldunet.com/web-tech/cloud/1492047-comment-kubernetes-perce-les-frontieres-du-cloud/)
</center>
<br/>

### Kubernetes Best Practices & Tips
* [**Optimize** Kubernetes cluster management with these 5 tips 🌟](https://searchitoperations.techtarget.com/feature/Optimize-Kubernetes-cluster-management-with-these-5-tips) Effective Kubernetes cluster management requires operations teams to balance pod and node deployments with performance and availability needs.
* [techradar.com: Three tips to implement Kubernetes with open standards](https://www.techradar.com/news/three-tips-to-implement-kubernetes-with-open-standards)
* [geekflare.com: 10 Kubernetes Best Practices for Better Container Orchestration 🌟](https://geekflare.com/kubernetes-best-practices/)
* [wideops.com: Kubernetes best practices: Setting up health checks with readiness and liveness probes](https://wideops.com/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes/)
* [containerjournal.com: 10 Best Practices Worth Implementing to Adopt Kubernetes](https://containerjournal.com/topics/container-management/10-best-practices-worth-implementing-to-adopt-kubernetes/)

### Disruptions
- [thenewstack.io: Kubernetes: Use PodDisruptionBudgets for Application Maintenance and Upgrades](https://thenewstack.io/kubernetes-use-poddisruptionbudgets-for-application-maintenance-and-upgrades/)

### Cost Estimation Strategies
- [cncf.io: 5 Problems with Kubernetes Cost Estimation Strategies](https://www.cncf.io/blog/2020/09/18/5-problems-with-kubernetes-cost-estimation-strategies)
- [loft.sh: How To Reduce Your Kubernetes Cost](https://loft.sh/blog/reduce-kubernetes-cost/)
- [harness.io: Getting Started with Cloud Cost Optimization](https://harness.io/2020/09/getting-started-with-cloud-cost-optimization/)
- [rancher.com: Gain Better Visibility into Kubernetes Cost Allocation](https://rancher.com/blog/2020/gain-better-visibility-kubernetes-cost-allocation)

### Kubernetes Resource and Capacity Management
* [itnext.io: Kubernetes Resource Management in Production 🌟](https://itnext.io/kubernetes-resource-management-in-production-d5382c904ed1) Requests, Limits, Overcommitment, Slack/Waste, Throttling
* [medium: Ultimate Kubernetes Resource Planning Guide 🌟](https://medium.com/dev-genius/ultimate-kubernetes-resource-planning-guide-449a4fddd1d6)
* [learnk8s.io: Setting the right requests and limits in Kubernetes 🌟](https://learnk8s.io/setting-cpu-memory-limits-requests)

### Kubernetes Monitoring
* [medium: Kubernetes Monitoring: Kube-State-Metrics](https://medium.com/@chrisedrego/kubernetes-monitoring-kube-state-metrics-df6546aea324)
* [Kubernetes Monitoring 101 — Core pipeline & Services Pipeline 🌟](https://levelup.gitconnected.com/kubernetes-monitoring-101-core-pipeline-services-pipeline-a34cd4cc9627)
* [medium: Utilizing and monitoring kubernetes cluster resources more effectively](https://medium.com/@martin.schneppenheim/utilizing-and-monitoring-kubernetes-cluster-resources-more-effectively-using-this-tool-df4c68ec2053)
* [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://sysdig.com/blog/kubernetes-monitoring-best-practices/)

#### Logging in Kubernetes
- [cncf.io: Logging in Kubernetes: EFK vs PLG Stack 🌟](https://www.cncf.io/blog/2020/07/27/logging-in-kubernetes-efk-vs-plg-stack/)
- [medium: How to Deploy an EFK stack to Kubernetes](https://medium.com/avmconsulting-blog/how-to-deploy-an-efk-stack-to-kubernetes-ebc1b539d063)
- [digitalocean.com: How To Set Up an Elasticsearch, Fluentd and Kibana (EFK) Logging Stack on Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes)
- [portworx.com: How to backup and restore Elasticsearch on Kubernetes](https://portworx.com/how-to-backup-and-restore-elasticsearch-on-kubernetes/)

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

### Kube Scheduler
- [All you need to know to get started with the Kube Scheduler](https://gist.github.com/luisalfonsopreciado/40a0fc2319241d517832affdce2bc1ff)

### Kubernetes Knowledge Hubs
- [k8sref.io 🌟](https://www.k8sref.io/) Kubernetes Reference
- [Kubernetes Research. Research documents on node instance types, managed services, ingress controllers, CNIs, etc. 🌟](https://learnk8s.io/research) A research hub to collect all knowledge around Kubernetes. Those are in-depth reports and comparisons designed to drive your decisions. Should you use GKE, AKS, EKS? How many nodes? What instance type?

## Kubectl commands
* [itnext.io: Boosting your kubectl productivity](https://itnext.io/boosting-your-kubectl-productivity-b348f7c25712)
* [medium: 4 Simple Kubernetes Terminal Customizations to Boost Your Productivity](https://medium.com/better-programming/4-simple-kubernetes-terminal-customizations-to-boost-your-productivity-deda60a19924)

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

### Lens Kubernetes IDE
- [Lens Kubernetes IDE 🌟](https://k8slens.dev/) Lens is the only IDE you’ll ever need to take control of your Kubernetes clusters. It's open source and free. Download it today!

[![lens ide](images/header-lens.png)](https://k8slens.dev/)

### Kubenav
- [kubenav](https://github.com/kubenav/kubenav) is the navigator for your Kubernetes clusters right in your pocket. kubenav is a mobile, desktop and web app to manage Kubernetes clusters and to get an overview of the status of your resources.

### Skaffold. Local Kubernetes Development
- [Skaffold 🌟](https://skaffold.dev/)
- [infracloud.io: Build and deploy Kubernetes apps with Skaffold](https://www.infracloud.io/blogs/skaffold-usecases/)

### Kind
- [Kind](https://kind.sigs.k8s.io/) is a tool for running local Kubernetes clusters using Docker container “nodes”. kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

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
* [medium: Build Kubernetes Autoscaling for Cluster Nodes and Application Pods 🌟](https://medium.com/better-programming/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07)
* [Auto-Scaling Your Kubernetes Workloads (K8s) 🌟](https://medium.com/faun/autoscaling-in-kubernetes-cluster-bc55b8393a19)

### HPA and VPA
* [HPA: Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
* [VPA: Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)
* [returngis.net: Escalado vertical de tus pods en Kubernetes con VerticalPodAutoscaler](https://www.returngis.net/2020/07/escalado-vertical-de-tus-pods-en-kubernetes/)
* [partlycloudy.blog: Horizontal Autoscaling in Kubernetes #3 – KEDA](https://partlycloudy.blog/2020/05/29/horizontal-autoscaling-in-kubernetes-3-keda/?utm_sq=gg9zmjs4yi)
* [medium: Build Kubernetes Autoscaling for Cluster Nodes and Application Pods](https://medium.com/better-programming/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07) Via the Cluster Autoscaler, Horizontal Pod Autoscaler, and Vertical Pod Autoscaler
* [itnext.io: Horizontal Pod Autoscaling with Custom Metric from Different Namespace](https://itnext.io/horizontal-pod-autoscaling-with-custom-metric-from-different-namespace-f19f8446143b)

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

<center>
<iframe src="https://www.youtube.com/embed/_W2qZvQT6XY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br/>

##### Kubectl Plugins and Tools. Kubernetes Extensions & Projects
* [ramitsurana/awesome-kubernetes: Tools 🌟](https://github.com/ramitsurana/awesome-kubernetes#configuration)
* [VMware octant](https://github.com/vmware/octant) A web-based, highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
    * [octant.dev](https://octant.dev/) Visualize your Kubernetes workloads. Octant is an open source developer-centric web interface for Kubernetes that lets you inspect a Kubernetes cluster and its applications.
* [KSS - Kubernetes pod status on steroid](https://github.com/chmouel/kss)
* [kubectl-tree](https://github.com/ahmetb/kubectl-tree) kubectl plugin to browse Kubernetes object hierarchies as a tree
* [The Golden Kubernetes Tooling and Helpers list](https://docs.google.com/spreadsheets/d/1WPHt0gsb7adVzY3eviMK2W8LejV0I5m_Zpc8tMzl_2w)
* [kubech (kubectl change)](https://github.com/aabouzaid/kubech) Set kubectl contexts/namespaces per shell/terminal to manage multi Kubernetes cluster at the same time.
* [Kubecle](https://github.com/rydogs/kubecle) is a web ui running locally that provides useful information about your kubernetes clusters. It is an alternative to Kubernetes Dashboard. Because it runs locally, you can access any kubernetes clusters you have access to
* [Permission Manager](https://github.com/sighupio/permission-manager) is a project that brings sanity to Kubernetes RBAC and Users management, Web UI FTW
* [developer.sh: Kubernetes client tools overview](https://developer.sh/posts/kubernetes-client-tools-overview)
* [kubectx](https://github.com/ahmetb/kubectx) Faster way to switch between clusters and namespaces in kubectl 
* [go-kubectx](https://github.com/aca/go-kubectx) 5x-10x faster alternative to kubectx. Uses client-go.
* [kubevious: application centric Kubernetes UI 🌟](https://kubevious.io/) is open-source software that provides a usable and highly graphical interface for Kubernetes. Kubevious renders all configurations relevant to the application in one place.
* [Guard](https://github.com/appscode/guard) is a Kubernetes Webhook Authentication server. Using guard, you can log into your Kubernetes cluster using various auth providers. Guard also configures groups of authenticated user appropriately.
* [itnext.io: **arkade** by example — Kubernetes apps, the easy way 🌟](https://itnext.io/kubernetes-apps-the-easy-way-f06d9e5cad3c)
* [**Kubei**](https://github.com/Portshift/kubei) is a flexible Kubernetes runtime scanner, scanning images of worker and Kubernetes nodes providing accurate vulnerabilities assessment.
* [**Tubectl**: a kubectl alternative which adds a bit of magic to your everyday kubectl routines by reducing the complexity of working with contexts, namespaces and intelligent matching resources.](https://github.com/reconquest/tubekit)
* [**Kpt**: Packaging up your Kubernetes configuration with git and YAML since 2014 **(Google)**](https://opensource.googleblog.com/2020/03/kpt-packaging-up-your-kubernetes.html)
    * [kpt](https://googlecontainertools.github.io/kpt/)
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
* [**K8bit** — the tiny Kubernetes dashboard 🌟](https://github.com/learnk8s/k8bit) K8bit is a tiny dashboard that is meant to demonstrate how to use the Kubernetes API to watch for changes.
    * [learnk8s.io/real-time-dashboard](https://learnk8s.io/real-time-dashboard)
* [**KUbernetes Test TooL (kuttl)** 🌟](https://kuttl.dev/)
    * [Youtube Webinar: The KUbernetes Test TooL (kuttl)](https://www.youtube.com/watch?v=Jh-viBv-D04)
* [Portfall: A desktop k8s port-forwarding portal for easy access to all your cluster UIs 🌟](https://github.com/rekon-oss/portfall)
* [k8s-dt-node-labeller](https://github.com/adaptant-labs/k8s-dt-node-labeller) is a Kubernetes controller for labelling a node with devicetree properties (devicetree is a data structure for describing hardware).
* [kubedev 🌟](https://relferreira.github.io/kubedev/) is a Kubernetes Dashboard that helps developers in their everyday usage
* [Kubectl SSH Proxy 🌟](https://github.com/little-angry-clouds/kubectl-ssh-proxy) Kubectl plugin to launch a ssh socks proxy and use it. This plugin aims to make your life easier when using kubectl a cluster that's behind a SSH bastion.
* [K9s - Kubernetes CLI To Manage Your Clusters In Style!](https://github.com/derailed/k9s) K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources. 
* [kubectl-images](https://github.com/chenjiandongx/kubectl-images) Show container images used in the cluster. Kubectl-images is a kubectl plugin that shows the container images used in the cluster. It first calls kubectl get pods to retrieve pods details and filters out the container image information of each pod then prints out the final result in a table view.
* [Access Pod Online using Podtnl](https://github.com/narendranathreddythota/podtnl) A Powerful CLI that makes your pod available to online without exposing a k8 service.
* [kiosk: Multi-Tenancy Extension For Kubernetes - Secure Cluster Sharing & Self-Service Namespace Provisioning 🌟](https://github.com/kiosk-sh/kiosk?utm_sq=gf3f25b1tk#why-kiosk) Kubernetes is designed as a single-tenant platform, which makes it hard for cluster admins to host multiple tenants in a single cluster. **Kiosk extends Kubernetes for multi-tenancy. The core idea is to use Kubernetes namespaces as isolated workspaces.**
* [asdf-kubectl](https://github.com/Banno/asdf-kubectl) kubectl plugin for [asdf version manager](https://asdf-vm.com/). asdf-vm is a CLI tool that can manage multiple language runtime versions on a per-project basis. It is like gvm, nvm, rbenv & pyenv (and more) all in one! Simply install your language’s plugin! 
* [k8s Spot Rescheduler](https://github.com/pusher/k8s-spot-rescheduler) is a tool that tries to reduce load on a set of Kubernetes nodes. It was designed with the purpose of moving Pods scheduled on AWS on-demand instances to AWS spot instances to allow the on-demand instances to be safely scaled down (By the Cluster Autoscaler). 
* [kube-spot-termination-notice-handler](https://github.com/kube-aws/kube-spot-termination-notice-handler) is a Kubernetes DaemonSet designed to gracefully delete pods 2 minutes before an EC2 Spot Instance is terminated.
* [Kubermatic Kubernetes Platform](https://github.com/Kubermatic/Kubermatic) is an open source project to centrally manage the global automation of thousands of Kubernetes clusters across multicloud, on-prem and edge with unparalleled density and resilience.
* [Polaris](https://github.com/FairwindsOps/polaris) helps Kubernetes users avoid common mistakes when configuring their workloads. It runs a variety of checks to ensure that Kubernetes pods and controllers are configured using best practices, helping you avoid problems in the future.
* [kmoncon](https://github.com/Stono/kconmon) Monitoring connectivity between your kubernetes nodes.
* [Tesoro](https://github.com/kapicorp/tesoro) [Kapitan](https://kapitan.dev/) Secrets Controller for Kubernetes. Tesoro is Kapitan Admission Controller Webhook. Tesoro allows you to seamleslsly apply Kapitan secret refs in compiled Kubernetes manifests. As it runs in the cluster, it will be able to reveal embedded kapitan secret refs in manifests when applied.
* [DAST operator](https://github.com/banzaicloud/dast-operator) Dynamic application security testing (DAST) is a Kubernetes operator that leverages OWASP ZAP to make automated basic web service security testing.
* [Teleskope](https://github.com/teleskopeView/teleskope_k8s) is a Kubernetes dashboard designed to give your devs and product managers an inside view of the cluster.
* [Introducing cdk8s+: Intent-driven APIs for Kubernetes objects](https://aws.amazon.com/es/blogs/containers/introducing-cdk8s-intent-driven-apis-for-kubernetes-objects/) Everyone hates yaml. Take that 75 lines of yaml and turn it into 45 lines of testable javascript with cdk8s+
    * https://github.com/awslabs/cdk8s/tree/master/packages/cdk8s-plus
* [KuUI (Kubernetes UI)](https://github.com/viveksinghggits/kuui) is a simple UI that can be used to manage the configmaps/secrets of your Kubernetes cluster.
* [Deprek8ion](https://github.com/swade1987/deprek8ion) is a set of rego policies to monitor Kubernetes APIs deprecations. It is designed to work with conftest.
* [Beetle](https://github.com/Clivern/Beetle) Kubernetes multi-cluster deployment automation service.
* [vault-controller](https://github.com/gobins/vault-controller) A K8s controller to manage Hashicorp Vault configuration using CRDs.
* [k8s-crash-informer](https://github.com/lnsp/k8s-crash-informer) is a Kubernetes controller that informs a Mattermost or Slack channel if an annotated deployment goes into crash loop.
* [Azure Arc enabled Kubernetes allows you to connect and manage external Kubernetes clusters in Azure](https://thorsten-hans.com/azure-arc-enabled-kubernetes-digital-ocean)
* [Kip, the Kubernetes Cloud Instance Provider](https://github.com/elotl/kip) Kip is a Virtual Kubelet provider that allows a Kubernetes cluster to transparently launch pods onto their own cloud instances. The kip pod is run on a cluster and will create a virtual Kubernetes node in the cluster.
* [Kubeletctl is a command line tool that implement kubelet's API 🌟](https://github.com/cyberark/kubeletctl)
* [k8s-node-label-monitor: Kubernetes Node Label Monitor provides a custom Kubernetes controller for monitoring and notifying changes in the label states of Kubernetes nodes (labels added, deleted, or updated), and can be run either node-local or cluster-wide](https://github.com/adaptant-labs/k8s-node-label-monitor)
* [medium: How to Validate Your Kubernetes Cluster With Sonobuoy 🌟](https://medium.com/better-programming/how-to-validate-your-kubernetes-cluster-with-sonobuoy-c91b282908fe) Run comprehensive conformance testing for your Kubernetes cluster
* [k42s is a full multinode Kubernetes Vagrant cluster with a real load balancer](https://github.com/p0bailey/k42s)
* [Pluto is a cli tool to help discover deprecated apiVersions in Kubernetes 🌟](https://github.com/FairwindsOps/pluto) Find Kubernetes resources that have been deprecated
* [Switchboard](https://github.com/borchero/switchboard) is a tool that manages DNS zones and their A/CNAME records for arbitrary backends. It runs as Kubernetes controller and watches for custom resources DNSZone and DNSRecord.
* [Kubernetes Deployment Builder 🌟🌟](https://static.brandonpotter.com/kubernetes/DeploymentBuilder.html)
* [ktx 🌟](https://github.com/heptiolabs/ktx) Managing kubeconfig files can become tedious when you have multiple clusters and contexts to switch between. ktx aims to reduce friction caused by switching between various configurations.
* [telepresence.io 🌟🌟](https://www.telepresence.io) Fast, local development for kubernetes and openshift microservices.
* [k8s-alert](https://github.com/kareem-elsayed/k8s-alerts) is a simple and lightweight alerting tool for Kubernetes.
* [Arktos](https://github.com/futurewei-cloud/arktos) is an open source cluster management system designed for large scale clouds. It is evolved from the open source Kubernetes v1.15 codebase with some fundamental improvements.
* [kube-exec 🌟](https://engineerd.github.io/kube-exec/introduction/) is a library similar to os/exec that allows you to run commands in a Kubernetes pod, as if that command was executed locally. It is inspired from go-dexec, which does the same thing, but for a Docker engine.
* [identity-server](https://github.com/kubeshield/identity-server) Identity Server implements a Kubernetes "whoami" service.
* [Kubermatic Kubernetes Platform 🌟](https://github.com/Kubermatic/Kubermatic) is in an open source project to centrally manage the global automation Kubernetes clusters across multicloud, on-prem and edge with unparalleled density and resilience.
* [The Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) is a project designed to be intentionally vulnerable cluster environment to learn and practice Kubernetes security.
* [kubefs](https://github.com/configurator/kubefs) lets you mount kubernetes's metadata object store as a file system
* [DAST Operator (Dynamic application security testing)](https://github.com/banzaicloud/dast-operator) is a Kubernetes operator that leverages OWASP ZAP to make automated basic web service security testing
* [KuUI (Kubernetes UI)](https://github.com/viveksinghggits/kuui) is a simple UI that can be used to manage the configmaps/secrets of your Kubernetes cluster.
* [pangolin 🌟](https://github.com/dpeckett/pangolin) is an enhanced Horizontal Pod Autoscaler for Kubernetes.
* [kubectl-isolate](https://github.com/yteraoka/kubectl-isolate) is a kubectl plugin to isolate a Pod from the Kubernetes Service
* [k8s-diagrams 🌟](https://github.com/cloudogu/k8s-diagrams) is a collection of diagrams explaining kubernetes, extracted from our trainings, articles and talks (k8s sec, k8s intro).
* [kconmon](https://github.com/Stono/kconmon) is a Kubernetes node connectivity monitoring tool
* [helm-docs](https://github.com/norwoodj/helm-docs) is a tool for automatically generating markdown documentation for helm charts.
* [Kubernetes Active Passive Applications](https://github.com/amelbakry/kubernetes-active-passive) is an ingenious script that combines StatefulSets and readiness probes to achieve an active-passive configuration for your Pods/apps.
* [Agorakube](https://github.com/ilkilab/agorakube) is a Certified Kubernetes Distribution that provides an enterprise grade solution following best practices to manage a conformant Kubernetes cluster for on-premise and public cloud providers.
* [dynamic-pv-scaler](https://github.com/opstree/dynamic-pv-scaler) is a golang based Kubernetes application which has been created to overcome the scaling issue of Persistent Volume in Kubernetes. This can scale the Persistent Volume on the basis of threshold which you have set.
* [Sinker](https://github.com/plexsystems/sinker) Imagesync enables the syncing of container images from one container registry to another. This is useful in cases where you need to mirror images that exist in a public container registry, to a private one. 
* [Cluster Turndown](https://github.com/kubecost/cluster-turndown) is an automated scaledown and scaleup of a Kubernetes cluster's backing nodes based on a custom schedule and turndown criteria.
* [capsule](https://github.com/clastix/capsule) is a Kubernetes multi-tenant Operator. It aggregates multiple namespaces in a Tenant. Within each tenant, users are free to create their namespaces and share all the assigned resources between the namespaces of the tenant.
* [Kubernetes Node Label Monitor](https://github.com/adaptant-labs/k8s-node-label-monitor) is a Kubernetes controller for monitoring and notifying about changes to Node label states
* [kubeinit](https://github.com/Kubeinit/kubeinit) KubeInit provides Ansible playbooks and roles for the deployment and configuration of multiple Kubernetes distributions.
* [kubergui: Kubernetes Deployment Builder🌟](https://github.com/BrandonPotter/kubergui) quickly builds out a basic Kubernetes Deployment and Kubernetes Service YAML. Kubernetes GUI YAML generators for simple but typo-prone tasks.
* [fubectl](https://github.com/kubermatic/fubectl) is a tool that reduces repetitive interactions with kubectl
* [Authelia 🌟](https://github.com/authelia/authelia) is a Single Sign-On and Multi-Factor portal for web apps that can be installed in Kubernetes and can integrate with your ingress controller
* [k8sdeploy](https://github.com/pyang55/k8sdeploy) is a go based tool, written with the goal of creating a cli that utilizes helm and kubernetes client libraries to deploy to multiple namespaces at once.
* [kubewatch 🌟🌟](https://hub.docker.com/r/bitnami/kubewatch) 
    * [Espiando a tu kubernetes con kubewatch](https://bluetab.net/wp-content/uploads/2020/09/Blog.html)
* [node-policy-webhook](https://github.com/softonic/node-policy-webhook) is a Kubernetes webhook designed to help you handle tolerations, nodeSelector and nodeAffinity.
- [kubeonoff](https://github.com/GambitResearch/kubeonoff) is a simple web UI for managing Kubernetes deployments.
- [ipvs-node-controller](https://github.com/kakao/ipvs-node-controller) is the kubernetes controller that solves External-IP (Load Balancer IP) issue with IPVS proxy mode.
- [kubeonoff](https://github.com/GambitResearch/kubeonoff) A simple web UI for managing Kubernetes deployments. Kubeonoff is a small web UI that allows to quickly stop/start/restart pods. Basically it's for non-developers to manage k8s objects per namespace.
- [Maistra 🌟](https://maistra.io/) is an opinionated distribution of Istio designed to work with Openshift. It combines Kiali, Jaeger, and Prometheus into a platform managed according to the OperatorHub lifecycle.
- [custom-pod-autoscaler](https://github.com/jthomperoo/custom-pod-autoscaler) A Custom Pod Autoscaler is a Kubernetes autoscaler that is customised and user created. The Custom Pod Autoscaler framework allows easier and faster development of Kubernetes autoscalers.
- [Kubevol 🌟](https://github.com/bmaynard/kubevol) allows you to audit all your Kubernetes pods for an attached volume or see all the volumes attached to each pod by a specific type (eg: ConfigMap, Secret).
- [kubectl-fuzzy 🌟](https://github.com/d-kuro/kubectl-fuzzy) uses fzf(1)-like fuzzy-finder to do partial or fuzzy search of Kubernetes resources. Instead of specifying full resource names to kubectl commands, you can choose them from an interactive list that you can filter by typing a few characters.
- [Setec 🌟](https://github.com/anthonysterling/setec) Setec (pronounced see-tek) is a utility tool that encrypts and decrypts secrets that are managed by Bitnami's Sealed Secrets.
- [Kompose (Kubernetes + Compose) 🌟](https://github.com/kubernetes/kompose) kompose is a tool to help users who are familiar with docker-compose move to Kubernetes. kompose takes a Docker Compose file and translates it into Kubernetes resources. kompose is a convenience tool to go from local Docker development to managing your application with Kubernetes. Transformation of the Docker Compose format to Kubernetes resources manifest may not be exact, but it helps tremendously when first deploying an application on Kubernetes.
- [kalm.dev 🌟](https://kalm.dev/) Easily deploy and manage applications on Kubernetes. Get what you want out of Kubernetes without having to write and maintain a ton of custom tooling. Deploy apps, handle requests, and hook up CI/CD, all through an intuitive web interface.
- [Kev](https://github.com/appvia/kev) Develop Kubernetes apps iteratively with Docker-Compose. Kev helps developers port and iterate Docker Compose apps onto Kubernetes. It understands the Docker Compose application topology and prepares it for deployment in (multiple) target environments, with minimal user input. We leverage the Docker Compose specification and allow for target-specific configurations to be applied to each component of the application stack, simply.
- [Synator Kubernetes Secret and ConfigMap synchronizer 🌟](https://github.com/TheYkk/synator) Synator synchronize your Secrets and ConfigMaps with your desired namespaces
- [kubes 🌟](https://github.com/boltops-tools/kubes) is a Kubernetes Deployment Tool. It builds the docker image, creates the Kubernetes YAML, and runs kubectl apply.
- [Kubernetes DaemonSet that enables a direct shell on each Node using SSH to localhost](https://gist.github.com/xandout/8d24558c75c53f3cb8bf0a97ec25fcfc) Learn how you can use a DaemonSet to expose an SSH shell on each node of your cluster (even if you don't have SSH installed). I run several K8S cluster on EKS and by default do not setup inbound SSH to the nodes. Sometimes I need to get into each node to check things or run a one-off tool. Rather than update my terraform, rebuild the launch templates and redeploy brand new nodes, I decided to use kubernetes to access each node directly.
- [NS Killer](https://github.com/germainlefebvre4/ns-killer) A Kubernetes project to kill all namespace living over X times. Quite useful when auto-generated development environments on the fly and give them a lifecycle out-of-the-box from Kubernetes or even Helm. You might find it useful if auto-generate development environments on the fly and want to remove old ones on a schedule.
- [kubeswitch: Kubernetes Version Switcher 🌟](https://github.com/steamhaus/kubeswitch) Easily switch kubectl binary versions.
- [Move2Kube 🌟](https://github.com/konveyor/move2kube) a tool that can help users migrate from Cloud Foundry and Docker Swarm to Kubernetes. Move2Kube is a command-line tool that accelerates the process of re-platforming to Kubernetes/Openshift. It does so by analysing the environment and source artifacts, and asking guidance from the user when required.
- [kubectl build (formerly known as kubectl-kaniko)](https://github.com/kvaps/kubectl-build) Kubectl build mimics the kaniko executor, but performs building on your Kubernetes cluster side. This allows you to simply build your local dockerfiles remotely without leaving your cozy environment.
- [Kubei 🌟](https://github.com/Portshift/Kubei) is a vulnerabilities scanning tool that allows users to get an accurate and immediate risk assessment of their kubernetes clusters. Kubei scans all images used in a Kubernetes cluster including images of application pods and system pods
- [Shell-operator](https://github.com/flant/shell-operator) is a tool for running event-driven scripts in a Kubernetes cluster. Shell-operator provides an integration layer between Kubernetes cluster events and shell scripts.
- [sinker is a tool to sync images from one container registry to another](https://github.com/plexsystems/sinker)  This is useful in cases when you rely on images that exist in a public container registry, but need to pull from a private registry.
- [ecrcp](https://github.com/bit-cloner/ecrcp) aims to mimic cp command in Linux systems as closely as possible in its implementation. Consider ecrcp to be the cp equivalent to copy container images from docker hub to ECR.
- [Checkov 🌟](https://github.com/bridgecrewio/checkov/) is a static code analysis tool for infrastructure-as-code. It scans cloud infrastructure provisioned using Terraform, Cloudformation, Kubernetes, Serverless or ARM Templates and detects security and compliance misconfigurations.

## Enforcing Policies and governance for kubernetes workloads with Conftest
* [Accelerated Feedback Loops when Developing for Kubernetes with Conftest](https://engineering.plex.com/posts/kubernetes-policy-conftest) Learn how to validate Kubernetes resources with Conftest for faster feedback loops
    * [open-policy-agent/conftest](https://github.com/open-policy-agent/conftest)
    * [Enforcing policies and governance for Kubernetes workloads 🌟](https://learnk8s.io/kubernetes-policies)
* [Deprek8ion](https://github.com/swade1987/deprek8ion) is a set of rego policies to monitor Kubernetes APIs deprecations and designed to work with conftest.
* [k8s-worker-pod-autoscaler](https://github.com/practo/k8s-worker-pod-autoscaler) scales the replicas in a deployment based on observed queue length.
* [kubectl-prune / kubectl-reap 🌟](https://github.com/micnncim/kubectl-reap) is a kubectl plugin that prunes unused Kubernetes resources.
* [kconnect - The Kubernetes Connection Manager CLI 🌟](https://github.com/fidelity/kconnect) kconnect is a CLI utility that can be used to discover and securely access Kubernetes clusters across multiple operating environments. Based on the authentication mechanism chosen the CLI will discover Kubernetes clusters you are allowed to access in a target hosting environment (i.e. EKS, AKS, Rancher) and generate a kubeconfig for a chosen cluster.

## Kubernetes Backup
* [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup)  
* [Stash](https://github.com/stashed/stash) If you are running production workloads in Kubernetes, you might want to take backup of your disks, databases etc. Stash is a cloud native data backup and recovery solution for Kubernetes workloads
* [thenewstack.io: Cloud Native Backups, Disaster Recovery and Migrations on Kubernetes](https://thenewstack.io/cloud-native-backups-disaster-recovery-and-migrations-on-kubernetes/)
* [rancher.com: The No. 1 Rule of Disaster Recovery](https://rancher.com/blog/2020/number-one-rule-disaster-recovery)
* [rancher.com: Disaster Recovery Preparedness for Your Kubernetes Clusters 🌟](https://rancher.com/blog/2020/disaster-recovery-preparedness-kubernetes-clusters)
* [k8s-snapshots: Automatic Volume Snapshots on Kubernetes](https://github.com/miracle2k/k8s-snapshots) is an operator that creates and expires snapshots according to annotations to your PersistentVolume or PersistentVolumeClaim resources.
* [infracloud.io: Protecting Kubernetes applications data using Kanister](https://www.infracloud.io/blogs/protecting-kubernetes-applications-with-kanister)
    * [kanister.io](https://kanister.io/)

### Backup with Velero
* [akomljen.com: Kubernetes Backup and Restore with Velero 🌟](https://akomljen.com/kubernetes-backup-and-restore-with-velero/?utm_sq=ggwzo8xdd8)
* [wecloudpro.com: Kubernetes Disaster Recovery with Velero 🌟](https://www.wecloudpro.com/2020/08/22/kubernetes-disaster-recovery-with-velero.html)
* [medium: Backup,Restore & Migrate Kubernetes cluster with Velero](https://medium.com/@maheshd7878/restore-backup-migrate-kubernetes-cluster-with-velero-434fa151f1e8)
* [medium: Velero backup/restore for K8s Stateful Applications managed by Operators](https://medium.com/@Sandeepkallazhi/velero-backup-restore-for-k8s-stateful-applications-managed-by-operators-8fd9c732ffcc?utm_sq=gi0vbpxxa3)

## Kubernetes Troubleshooting
* [Kubernetes troubleshooting diagram 🌟](https://github.com/redhatspain/awesome-kubernetes/blob/master/docs/images/kubernetes-troubleshooting.jpg)
* [Understanding Kubernetes cluster events 🌟](https://banzaicloud.com/blog/k8s-cluster-logging/)
* [nigelpoulton.com: Troubleshooting kubernetes service discovery - Part 1](https://nigelpoulton.com/blog/f/troubleshooting-kubernetes-service-discovery---part-1)
* [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)

### Debugging Techniques and Strategies. Debugging with ephemeral containers
- [kubectl-debug](https://github.com/aylei/kubectl-debug)
- [kubesandclouds.com: Debugging with ephemeral containers in K8s (v1.18+)](https://kubesandclouds.com/index.php/2020/05/30/ephemeral-containers-in-k8s/)
- [How to quarantine pods 🌟](https://www.reddit.com/r/kubernetes/comments/gt3uvg/how_to_quarantine_pods/)
- [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg) KDBG (Kubernetes Debuger) is a small docker container based on lastest Alpine Linux image, used for debugging Kubernetes clusters from inside a pod.
- [inspektor-gadget](https://github.com/kinvolk/inspektor-gadget) Collection of gadgets for debugging and introspecting Kubernetes applications using BPF 
    - [kinvolk.io](https://kinvolk.io)
- [learnk8s.io: A visual guide on troubleshooting Kubernetes deployments 🌟](https://learnk8s.io/troubleshooting-deployments)
- [StatusBay 🌟](https://github.com/similarweb/statusbay) is a tool that provides the missing visibility into the K8S deployment process. The main goal is to ease the experience of troubleshooting and debugging services in K8S and provide confidence while making changes.

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

## Kubernetes Patterns
* [github.com/k8spatterns/examples 🌟](https://github.com/k8spatterns/examples) Examples for "Kubernetes Patterns - Reusable Elements for Designing Cloud-Native Applications"
* [kubernetes.io: container design patterns](https://kubernetes.io/blog/2016/06/container-design-patterns/)
* [magalix.com: Kubernetes Patterns - The Service Discovery Pattern 🌟](https://www.magalix.com/blog/kubernetes-patterns-the-service-discovery-pattern)
* [gardener.cloud: Kubernetes Antipatterns](https://gardener.cloud/050-tutorials/content/howto/antipattern/)
* [dzone.com: Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1)
* [developers.redhat.com: Top 10 must-know Kubernetes design patterns](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)
* [medium: 10 Anti-Patterns for Kubernetes Deployments 🌟](https://medium.com/better-programming/10-antipatterns-for-kubernetes-deployments-e97ce1199f2d) Common practices in Kubernetes deployments that have better solutions
* [learnsteps.com: How Kubernetes works on reconciler pattern](https://www.learnsteps.com/how-kubernetes-works-on-a-reconciler-pattern/)
* [learncloudnative.com: Sidecar Container Pattern](https://www.learncloudnative.com/blog/2020-09-30-sidecar-container/)

[![Top 10 Kubernetes patterns](images/top_10_kubernetes_patterns.png)](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)

## e-Books
### Famous Kubernetes resources of 2019
* [Kubernetes essentials E-book 🌟](https://images.linoxide.com/ebook-kubernetes-essentials.pdf)
* [Cloud-Native DevOps With Kubernetes O'Reilly book (Free) 🌟](https://www.nginx.com/resources/library/cloud-native-devops-with-kubernetes/)
* [Kubernetes: Up and Running, 2nd Edition🌟](http://shop.oreilly.com/product/0636920223788.do) Dive into the Future of Infrastructure. By Brendan Burns, Kelsey Hightower, Joe Beda
* [Container Security](https://www.amazon.com/gp/product/1492056707)
    * [Don't make this container security mistake](https://bitfieldconsulting.com/blog/container-security)

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
- [K8Spin Operator 🌟](https://github.com/k8spin/k8spin-operator) Kubernetes multi-tenant operator. Enables multi-tenant capabilities in your Kubernetes Cluster. [We defined some small features to implement](https://github.com/k8spin/k8spin-operator/projects/1). If you know python & Kubernetes and want to contribute to this project, ping us!
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


### Flux. The GitOps Operator for Kubernetes
* [Flux 🌟](https://fluxcd.io/) The GitOps operator for Kubernetes
* [docs.fluxcd.io](https://docs.fluxcd.io/)
* [github: Flux CD](https://github.com/fluxcd/flux)
* [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.

### K8s KPIs with Kuberhealthy Operator
- [K8s KPIs with Kuberhealthy 🌟](https://kubernetes.io/blog/2020/05/29/k8s-kpis-with-kuberhealthy/) transforming Kuberhealthy into a Kubernetes operator for synthetic monitoring. This new ability granted developers the means to create their own Kuberhealthy check containers to synthetically monitor their applications and clusters. Additionally, we created a guide on how to easily install and use Kuberhealthy in order to capture some helpful synthetic [KPIs](https://kpi.org/KPI-Basics).

### Writing Kubernetes Operators
* [Kubernetes.io: Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
* [opensource.com: Build a Kubernetes Operator in 10 minutes with Operator SDK](https://opensource.com/article/20/3/kubernetes-operator-sdk)
* [magalix.com: Creating Custom Kubernetes Operators](https://www.magalix.com/blog/creating-custom-kubernetes-operators)
* [medium.com: Writing Your First Kubernetes Operator](https://medium.com/faun/writing-your-first-kubernetes-operator-8f3df4453234)
* [bmc.com: What Is a Kubernetes Operator?](https://www.bmc.com/blogs/kubernetes-operator/)
* [Writing a Kubernetes Operator in Java Cheat Sheet](https://developers.redhat.com/cheat-sheets/writing-kubernetes-operator-java/)
* [linuxera.org: Writing Operators using the Operator Framework SDK](https://linuxera.org/writing-operators-using-operator-framework/)
* [openshift.com: 7 Best Practices for Writing Kubernetes Operators: An SRE Perspective](https://www.openshift.com/blog/7-best-practices-for-writing-kubernetes-operators-an-sre-perspective)
* [medium: From Zero to Kubernetes Operator](https://medium.com/@victorpaulo/from-zero-to-kubernetes-operator-dd06436b9d89) In this post you will learn how to build a simple Kubernetes Operator. The article starts with the main concepts and then continues with hands-on labs where you will create a Kubernetes Operator from the ground up.


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
* [howtoforge.com: Network Policy in Kubernetes 🌟](https://www.howtoforge.com/kubernetes_network_policy/) By default, pods accept traffic from any source. A network policy helps to specify how a group of pods can communicate with each other and other network endpoints.
* [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification/)

<center>
<script async class="speakerdeck-embed" data-id="9251193501114da199d70b2a679c552f" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
</center>

### Kubernetes Ingress Specification
- [Supporting the Evolving Ingress Specification in Kubernetes 1.18](https://kubernetes.io/blog/2020/06/05/supporting-the-evolving-ingress-specification-in-kubernetes-1.18/)

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

### DNS Service with CoreDNS
- [medium: How to Autoscale the DNS Service in a Kubernetes Cluster](https://medium.com/faun/how-to-autoscale-the-dns-service-in-a-kubernetes-cluster-cbb46ae89678)

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
* [Dzone - OAuth 2.0](https://dzone.com/articles/oauth-20-beginners-guide)
* [Kubernetes Security Best Practices 🌟](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire)
* [Kubernetes Certs](https://github.com/jetstack/cert-manager/)
* [Using SSL certificates from Let’s Encrypt in your Kubernetes Ingress via cert-manager 🌟](https://medium.com/flant-com/cert-manager-lets-encrypt-ssl-certs-for-kubernetes-7642e463bbce)
* [jeffgeerling.com: Everyone might be a cluster-admin in your Kubernetes cluster](https://www.jeffgeerling.com/blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster)
* [Microsoft.com: Attack matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
* [codeburst.io: 7 Kubernetes Security Best Practices You Must Follow](https://codeburst.io/7-kubernetes-security-best-practices-you-must-follow-ae32f1ed6444)
* [itnext.io: Effective Secrets with Vault and Kubernetes](https://itnext.io/effective-secrets-with-vault-and-kubernetes-9af5f5c04d06)  
* [thenewstack.io: Laying the Groundwork for Kubernetes Security, Across Workloads, Pods and Users](https://thenewstack.io/laying-the-groundwork-for-kubernetes-security-across-workloads-pods-and-users/)
* [horovits.wordpress.com: Kubernetes Security Best Practices](https://horovits.wordpress.com/2020/07/15/kubernetes-security-best-practices/)

### RBAC
* [Configure RBAC in Kubernetes Like a Boss 🌟](https://medium.com/trendyol-tech/configure-rbac-in-kubernetes-like-a-boss-665e2a8665dd) Learn how to configure RBAC in kubernetes. In this post, you will configure RBAC both with kubectl and yaml definitions.
* [infracloud.io: How to setup Role based access (RBAC) to Kubernetes Cluster 🌟](https://www.infracloud.io/blogs/role-based-access-kubernetes)
* [Kubernetes RBAC Permission Manager 🌟](https://toolbox.kali-linuxtr.net/kubernetes-rbac-permission-manager.tool)
* [Krane 🌟](https://github.com/appvia/krane) is a Kubernetes RBAC static analysis tool. It identifies potential security risks in K8s RBAC design and makes suggestions on how to mitigate them. Krane dashboard presents current RBAC security posture and lets you navigate through its definition.

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

### EKS Security
* [Security Group Rules EKS](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
* [EC2 ENI and IP Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)
* [Calico in EKS](https://docs.aws.amazon.com/eks/latest/userguide/calico.html )
* [Amazon EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/)
    * [EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/iam/)

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
- [medium.com: How to modify etcd data of your Kubernetes directly (without K8s API)](https://medium.com/flant-com/modifying-kubernetes-etcd-data-ed3d4bb42379)

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

## Non-production Kubernetes Local Installers
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
    * [itnext.io: How to experiment locally on Kubernetes with minikube and your local Dockerfiles](https://itnext.io/how-to-experiment-locally-on-kubernetes-with-minikube-and-your-local-dockerfiles-48833fcd90c9)
* [**kind**](https://github.com/kubernetes-sigs/kind) Kubernetes IN Docker - local clusters for testing Kubernetes
* [store.docker.com: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [medium.com: Local Kubernetes for Linux — MiniKube vs MicroK8s](https://medium.com/containers-101/local-kubernetes-for-linux-minikube-vs-microk8s-1b2acad068d3)
* [itnext.io: Run Kubernetes On Your Machine](https://itnext.io/run-kubernetes-on-your-machine-7ee463af21a2) Several options to start playing with K8s in no time
* [padok.fr: MiniKube, Kubeadm, Kind, K3S, how to get started on Kubernetes?](https://www.padok.fr/en/blog/minikube-kubeadm-kind-k3s)

## Kubernetes in Public Cloud
### GKE vs EKS vs AKS
* [medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS](https://medium.com/@Platform9Sys/kubernetes-cloud-services-comparing-gke-eks-and-aks-1fe42770cad3)
* [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.com/post/2020/02/eks-vs-gke-vs-aks/)
* [youtube: Kubernetes Comparison](https://www.youtube.com/watch?v=xM9jpcVGTzY) A beautiful comparison of Kubernetes Services from GCP, AWS and Azure by learnk8s.
    * [learnk8s.io/research:  Comparison of Kubernetes managed services 🌟](https://learnk8s.io/research)
* [medium: State of Managed Kubernetes 2020](https://medium.com/swlh/state-of-managed-kubernetes-2020-4be006643360) EKS vs. AKS vs. GKE from a Developer’s Perspective
* [medium: Managed Kubernetes Services Compared: GKE vs. EKS vs. AKS](https://medium.com/better-programming/managed-kubernetes-services-compared-gke-vs-eks-vs-aks-df1ecb22bba0) Comparing the three most popular managed Kubernetes platforms in features and overall experience.

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
* [How to track costs in multi-tenant Amazon EKS clusters using Kubecost](https://aws.amazon.com/blogs/containers/how-to-track-costs-in-multi-tenant-amazon-eks-clusters-using-kubecost/)
* [EKS Service Accounts Explained](https://fika.works/blog/eks-service-accounts/) In AWS you can assign IAM permissions to pods in your cluster. This article explains how it works.
* [medium: Building the CI/CD of the Future, Creating the EKS Cluster 🌟](https://medium.com/swlh/building-the-ci-cd-of-the-future-creating-the-eks-cluster-e4cce4eb3500)
* [Announcing the AWS Controllers for Kubernetes Preview](https://aws.amazon.com/about-aws/whats-new/2020/08/announcing-the-aws-controllers-for-kubernetes-preview/)
* [daveops.xyz: Administrar usuarios en EKS](https://daveops.xyz/2020/08/25/administrar-usuarios-en-eks/)
* [aws.github.io: AWS Controllers for Kubernetes](https://aws.github.io/aws-controllers-k8s/)
* [stacksimplify.com: AWS ALB Ingress Service - Basics 🌟](https://www.stacksimplify.com/aws-eks/aws-alb-ingress/lean-kubernetes-aws-alb-ingress-basics/)
* [Kubernetes PVCs with EFS provisioner](https://www.padok.fr/en/blog/efs-provisioner-kubernetes)
* [Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
* [itnext.io: Migrating Apache Spark workloads from AWS EMR to Kubernetes](https://itnext.io/migrating-apache-spark-workloads-from-aws-emr-to-kubernetes-463742b49fda)
* [Running spot instances effectively with Amazon EKS](https://m.signalvnoise.com/running-spot-instances-effectively-with-amazon-eks)

### GCP & GKE
- [Fetches all Primitive and Predefined GCP IAM Roles](https://github.com/darkbitio/gcp-iam-role-permissions)
- [Using new traffic control features in External HTTP(S) load balancer](https://cloudblog.withgoogle.com/products/networking/how-to-use-new-traffic-control-features-in-cloud-load-balancing/amp/)
- [Setting up NodeLocal DNSCache](https://cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
- [Looking ahead as GKE, the original managed Kubernetes, turns 5](https://cloudblog.withgoogle.com/products/containers-kubernetes/5-ways-google-cloud-is-making-gke-the-best-place-to-run-kubernetes/amp/)
- [whizlabs.com: Introduction To Google Cloud Platform](https://www.whizlabs.com/blog/google-cloud-platform/)
- [blog.doit-intl.com: How to Set Up Multi-Cluster Load Balancing with GKE](https://blog.doit-intl.com/how-to-setup-multi-cluster-load-balancing-with-gke-4b407e1f3dff)

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
* [Set up a Bare Metal Kubernetes cluster with kubeadm](https://www.padok.fr/en/blog/kubeadm-kubernetes-cluster)

### Deploying Kubernetes Cluster with Ansible 
- [Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes)

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

### Caravan
- [linecorp.com: Building Large Kubernetes Clusters with **Caravan**](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters/)

### ClusterAPI
- [**ClusterAPI**](https://cluster-api.sigs.k8s.io/)
- [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89)

### Microk8s
- [**Microk8s**](https://microk8s.io/)

### k8s-tew
- [**k8s-tew**](https://github.com/darxkies/k8s-tew) Kubernetes is a fairly complex project. For a newbie it is hard to understand and also to use. While [Kelsey Hightower’s Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way), on which this project is based, helps a lot to understand Kubernetes, it is optimized for the use with Google Cloud Platform.

### Kubernetes Distributions
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
</center>

## Kubernetes Scripts
- [Kubernetes Scripts 🌟](https://github.com/eldada/kubernetes-scripts)

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