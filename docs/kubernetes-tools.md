# Kubernetes Plugins, Tools, Extensions and Projects
- [Introduction](#introduction)
- [K8s Tools](#k8s-tools)
- [Penetration Testing Tools](#penetration-testing-tools)
- [Deckhouse Kubernetes Platform](#deckhouse-kubernetes-platform)
- [Porter](#porter)
- [Datree. Quality Checks for Kubernetes YAMLs](#datree-quality-checks-for-kubernetes-yamls)
- [Kaniko Build Images in Kubernetes without docker](#kaniko-build-images-in-kubernetes-without-docker)
- [Shipwright Framework for Building Container Images on Kubernetes](#shipwright-framework-for-building-container-images-on-kubernetes)
- [BuildKit CLI for kubectl](#buildkit-cli-for-kubectl)
- [Buildpacks vs Dockerfiles](#buildpacks-vs-dockerfiles)
- [Kubevela](#kubevela)
- [Pixie. Instantly troubleshoot applications on Kubernetes](#pixie-instantly-troubleshoot-applications-on-kubernetes)
- [Dekorate. Generate k8s manifests for java apps](#dekorate-generate-k8s-manifests-for-java-apps)
- [Kubesploit](#kubesploit)
- [Kubeshop](#kubeshop)
- [Monokle](#monokle)
- [KubeLibrary](#kubelibrary)
- [kube-vip](#kube-vip)
- [Kubermetrics](#kubermetrics)
- [Kustomizer](#kustomizer)
- [MetalLB](#metallb)
- [Kubermatic Kubernetes Platform](#kubermatic-kubernetes-platform)
    - [Kubermatic Kubeone](#kubermatic-kubeone)
- [Usernetes](#usernetes)
- [k8syaml.com](#k8syamlcom)
- [Komodor Workflows](#komodor-workflows)
- [Popeye](#popeye)
- [kbrew](#kbrew)
- [KubExplorer](#kubexplorer)
- [Kubescape](#kubescape)
- [Kubectl Connections](#kubectl-connections)
- [Benchmark Operator](#benchmark-operator)
- [Source-To-Image (S2I)](#source-to-image-s2i)
- [VMware Tanzu Octant](#vmware-tanzu-octant)
- [Qovery Engine](#qovery-engine)
- [mck8s Container orchestrator for multi-cluster Kubernetes](#mck8s-container-orchestrator-for-multi-cluster-kubernetes)
- [Shipwright framework](#shipwright-framework)
- [Schiff (Deutsche Telekom)](#schiff-deutsche-telekom)
- [NetMaker](#netmaker)
- [AWS Karpenter kubernetes Autoscaler](#aws-karpenter-kubernetes-autoscaler)
- [Kuby (easy deployments of Ruby Rails App)](#kuby-easy-deployments-of-ruby-rails-app)
- [Direktiv](#direktiv)
- [Jabos](#jabos)
- [Pleco](#pleco)
- [Mesh-kridik](#mesh-kridik)
- [kubewatch](#kubewatch)
- [Botkube](#botkube)
- [Robusta](#robusta)
- [Soup GitOps Operator](#soup-gitops-operator)
- [Epinio](#epinio)
- [Testkube](#testkube)
- [KuberLogic](#kuberlogic)
- [Kusk](#kusk)
- [Azure AD Workload Identity](#azure-ad-workload-identity)
- [Kubernate](#kubernate)
- [Tackle](#tackle)
- [Azure Placement Policy Scheduler Plugins](#azure-placement-policy-scheduler-plugins)
- [Azure AAD Pod Identity](#azure-aad-pod-identity)
- [MicroShift](#microshift)
- [kubefwd (Kube Forward)](#kubefwd-kube-forward)
- [Kpng. Kubernetes Proxy NG](#kpng-kubernetes-proxy-ng)
- [Auto-portforward (apf)](#auto-portforward-apf)
- [gardener/Terraformer](#gardenerterraformer)
- [Tweets](#tweets)

## Introduction
- [collabnix.com: Top 10 Kubernetes Tools You Need for 2021 – Part 1](https://collabnix.com/top-10-kubernetes-tools-you-need-for-2021/)
- [collabnix.com: Top 10 Kubernetes Tools You Need for 2021 – Part 2](https://collabnix.com/top-10-kubernetes-tool-you-need-for-2021-part-2/)
- [collabnix.github.io: Kubetools - A Curated List of Kubernetes Tools: Kubetools - A Curated List of Kubernetes Tools](https://collabnix.github.io/kubetools/)
- [cyberithub.com: 70+ Important Kubernetes Related Tools You Should Know About](https://www.cyberithub.com/70-important-kubernetes-related-tools-you-should-know-about)
- [itnext.io: Kubernetes GitOps Tools](https://itnext.io/kubernetes-gitops-tools-cf0247eb5368)
- [itnext.io: Kubernetes Essential Tools: 2021](https://itnext.io/kubernetes-essential-tools-2021-def12e84c572)
- [containerjournal.com: 9 Open Source Developer Tools for Kubernetes](https://containerjournal.com/features/9-open-source-developer-tools-for-kubernetes/)
- [blog.devgenius.io: 7 Open Source Kubernetes Developer Tools to Follow in 2022](https://blog.devgenius.io/7-open-source-kubernetes-developer-tools-to-follow-in-2022-78a5e5dbd4e3)

## K8s Tools
* [downloadkubernetes.com: Download Kubernetes 🌟](https://www.downloadkubernetes.com/) An easier way to get the binaries you need 
* [ramitsurana/awesome-kubernetes: Tools 🌟](https://github.com/ramitsurana/awesome-kubernetes#configuration)
* [VMware octant](https://github.com/vmware/octant) A web-based, highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
    * [octant.dev](https://octant.dev/) Visualize your Kubernetes workloads. Octant is an open source developer-centric web interface for Kubernetes that lets you inspect a Kubernetes cluster and its applications.
* [KSS - Kubernetes pod status on steroid](https://github.com/chmouel/kss)
* [kubectl-tree](https://github.com/ahmetb/kubectl-tree) kubectl plugin to browse Kubernetes object hierarchies as a tree
* [The Golden Kubernetes Tooling and Helpers list](https://docs.google.com/spreadsheets/d/1WPHt0gsb7adVzY3eviMK2W8LejV0I5m_Zpc8tMzl_2w)
* [kubech (kubectl change)](https://github.com/aabouzaid/kubech) Set kubectl contexts/namespaces per shell/terminal to manage multi Kubernetes cluster at the same time.
* [Kubecle](https://github.com/rydogs/kubecle) is a web ui running locally that provides useful information about your kubernetes clusters. It is an alternative to Kubernetes Dashboard. Because it runs locally, you can access any kubernetes clusters you have access to
* [Permission Manager](https://github.com/sighupio/permission-manager) is a project that brings sanity to Kubernetes RBAC and Users management, Web UI FTW
* [cloudnatively.com: Kubernetes client tools overview](https://www.cloudnatively.com/kubernetes-client-tools-overview/)
* [==kubectx + kubens: : Power tools for kubectl==🌟🌟](https://github.com/ahmetb/kubectx) Faster way to switch between clusters and namespaces in kubectl 
* [go-kubectx](https://github.com/aca/go-kubectx) 5x-10x faster alternative to kubectx. Uses client-go.
* [kubevious: application centric Kubernetes UI 🌟](https://kubevious.io/) is open-source software that provides a usable and highly graphical interface for Kubernetes. Kubevious renders all configurations relevant to the application in one place.
    * [Kubevious SaaS: portal.kubevious.io](https://portal.kubevious.io/)
    * [Kubevious SaaS Beta is Live!](https://kubevious.io/blog/post/kubevious-saas-beta-launch)
* [Guard](https://github.com/appscode/guard) is a Kubernetes Webhook Authentication server. Using guard, you can log into your Kubernetes cluster using various auth providers. Guard also configures groups of authenticated user appropriately.
* [itnext.io: **arkade** by example — Kubernetes apps, the easy way 🌟](https://itnext.io/kubernetes-apps-the-easy-way-f06d9e5cad3c)
* [**Kubei**](https://github.com/Portshift/kubei) is a flexible Kubernetes runtime scanner, scanning images of worker and Kubernetes nodes providing accurate vulnerabilities assessment.
* [**Tubectl**: a kubectl alternative which adds a bit of magic to your everyday kubectl routines by reducing the complexity of working with contexts, namespaces and intelligent matching resources.](https://github.com/reconquest/tubekit)
* [**Kpt**: Packaging up your Kubernetes configuration with git and YAML since 2014 **(Google)**](https://opensource.googleblog.com/2020/03/kpt-packaging-up-your-kubernetes.html)
    * [kpt](https://googlecontainertools.github.io/kpt/)
    * [labs.meanpug.com: Kubernetes Kpt in The Wild: What it is and how to use it](https://labs.meanpug.com/kubernetes-kpt-in-the-wild/) Kubernetes Kpt is tooling by Google that facilitates a structured approach to defining, managing, and distributing kubernetes templates between teams and orgs.
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
* [Polaris 🌟](https://github.com/FairwindsOps/polaris) helps Kubernetes users avoid common mistakes when configuring their workloads. It runs a variety of checks to ensure that Kubernetes pods and controllers are configured using best practices, helping you avoid problems in the future.
    * [cncf.io: What is Polaris? Kubernetes open source configuration validation 🌟](https://www.cncf.io/blog/2021/07/01/what-is-fairwinds-polaris-kubernetes-open-source-configuration-validation/)
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
* [Kubernetes Node Label Monitor](https://github.com/adaptant-labs/k8s-node-label-monitor) is a Kubernetes controller for monitoring and notifying about changes to Node label states
* [kubeinit 🌟](https://github.com/Kubeinit/kubeinit) KubeInit provides Ansible playbooks and roles for the deployment and configuration of multiple Kubernetes distributions.
* [kubergui: Kubernetes Deployment Builder🌟](https://github.com/BrandonPotter/kubergui) quickly builds out a basic Kubernetes Deployment and Kubernetes Service YAML. Kubernetes GUI YAML generators for simple but typo-prone tasks.
* [fubectl](https://github.com/kubermatic/fubectl) is a tool that reduces repetitive interactions with kubectl
* [Authelia 🌟](https://github.com/authelia/authelia) is a Single Sign-On and Multi-Factor portal for web apps that can be installed in Kubernetes and can integrate with your ingress controller
* [k8sdeploy](https://github.com/pyang55/k8sdeploy) is a go based tool, written with the goal of creating a cli that utilizes helm and kubernetes client libraries to deploy to multiple namespaces at once.
* [kubewatch 🌟🌟](https://hub.docker.com/r/bitnami/kubewatch) 
    * [Espiando a tu kubernetes con kubewatch](https://bluetab.net/wp-content/uploads/2020/09/Blog.html)
* [node-policy-webhook](https://github.com/softonic/node-policy-webhook) is a Kubernetes webhook designed to help you handle tolerations, nodeSelector and nodeAffinity.
* [kubeonoff](https://github.com/GambitResearch/kubeonoff) is a simple web UI for managing Kubernetes deployments.
* [ipvs-node-controller](https://github.com/kakao/ipvs-node-controller) is the kubernetes controller that solves External-IP (Load Balancer IP) issue with IPVS proxy mode.
* [kubeonoff](https://github.com/GambitResearch/kubeonoff) A simple web UI for managing Kubernetes deployments. Kubeonoff is a small web UI that allows to quickly stop/start/restart pods. Basically it's for non-developers to manage k8s objects per namespace.
* [Maistra 🌟](https://maistra.io/) is an opinionated distribution of Istio designed to work with Openshift. It combines Kiali, Jaeger, and Prometheus into a platform managed according to the OperatorHub lifecycle.
* [custom-pod-autoscaler](https://github.com/jthomperoo/custom-pod-autoscaler) A Custom Pod Autoscaler is a Kubernetes autoscaler that is customised and user created. The Custom Pod Autoscaler framework allows easier and faster development of Kubernetes autoscalers.
* [Kubevol 🌟](https://github.com/bmaynard/kubevol) allows you to audit all your Kubernetes pods for an attached volume or see all the volumes attached to each pod by a specific type (eg: ConfigMap, Secret).
* [kubectl-fuzzy 🌟](https://github.com/d-kuro/kubectl-fuzzy) uses fzf(1)-like fuzzy-finder to do partial or fuzzy search of Kubernetes resources. Instead of specifying full resource names to kubectl commands, you can choose them from an interactive list that you can filter by typing a few characters.
* [Setec 🌟](https://github.com/anthonysterling/setec) Setec (pronounced see-tek) is a utility tool that encrypts and decrypts secrets that are managed by Bitnami's Sealed Secrets.
* [Kompose (Kubernetes + Compose) 🌟](https://github.com/kubernetes/kompose) kompose is a tool to help users who are familiar with docker-compose move to Kubernetes. kompose takes a Docker Compose file and translates it into Kubernetes resources. kompose is a convenience tool to go from local Docker development to managing your application with Kubernetes. Transformation of the Docker Compose format to Kubernetes resources manifest may not be exact, but it helps tremendously when first deploying an application on Kubernetes.
* [kalm.dev 🌟](https://kalm.dev/) Easily deploy and manage applications on Kubernetes. Get what you want out of Kubernetes without having to write and maintain a ton of custom tooling. Deploy apps, handle requests, and hook up CI/CD, all through an intuitive web interface.
* [Kev](https://github.com/appvia/kev) Develop Kubernetes apps iteratively with Docker-Compose. Kev helps developers port and iterate Docker Compose apps onto Kubernetes. It understands the Docker Compose application topology and prepares it for deployment in (multiple) target environments, with minimal user input. We leverage the Docker Compose specification and allow for target-specific configurations to be applied to each component of the application stack, simply.
* [Synator Kubernetes Secret and ConfigMap synchronizer 🌟](https://github.com/TheYkk/synator) Synator synchronize your Secrets and ConfigMaps with your desired namespaces
* [kubes 🌟](https://github.com/boltops-tools/kubes) is a Kubernetes Deployment Tool. It builds the docker image, creates the Kubernetes YAML, and runs kubectl apply.
* [Kubernetes DaemonSet that enables a direct shell on each Node using SSH to localhost](https://gist.github.com/xandout/8d24558c75c53f3cb8bf0a97ec25fcfc) Learn how you can use a DaemonSet to expose an SSH shell on each node of your cluster (even if you don't have SSH installed). I run several K8S cluster on EKS and by default do not setup inbound SSH to the nodes. Sometimes I need to get into each node to check things or run a one-off tool. Rather than update my terraform, rebuild the launch templates and redeploy brand new nodes, I decided to use kubernetes to access each node directly.
* [NS Killer](https://github.com/germainlefebvre4/ns-killer) A Kubernetes project to kill all namespace living over X times. Quite useful when auto-generated development environments on the fly and give them a lifecycle out-of-the-box from Kubernetes or even Helm. You might find it useful if auto-generate development environments on the fly and want to remove old ones on a schedule.
* [kubeswitch: Kubernetes Version Switcher 🌟](https://github.com/steamhaus/kubeswitch) Easily switch kubectl binary versions.
* [Kubeswitch (for operators) 🌟](https://github.com/danielfoehrKn/kubeswitch) The kubectx for operators. kubeswitch (lazy: switch) takes Kubeconfig context switching to the next level, catering to operators of large scale Kubernetes installations. Designed as a drop-in replacement for kubectx.
* [kubectl build (formerly known as kubectl-kaniko)](https://github.com/kvaps/kubectl-build) Kubectl build mimics the kaniko executor, but performs building on your Kubernetes cluster side. This allows you to simply build your local dockerfiles remotely without leaving your cozy environment.
* [Kubei 🌟](https://github.com/Portshift/Kubei) is a vulnerabilities scanning tool that allows users to get an accurate and immediate risk assessment of their kubernetes clusters. Kubei scans all images used in a Kubernetes cluster including images of application pods and system pods
* [Shell-operator](https://github.com/flant/shell-operator) is a tool for running event-driven scripts in a Kubernetes cluster. Shell-operator provides an integration layer between Kubernetes cluster events and shell scripts.
* [sinker is a tool to sync images from one container registry to another](https://github.com/plexsystems/sinker)  This is useful in cases when you rely on images that exist in a public container registry, but need to pull from a private registry.
* [ecrcp](https://github.com/bit-cloner/ecrcp) aims to mimic cp command in Linux systems as closely as possible in its implementation. Consider ecrcp to be the cp equivalent to copy container images from docker hub to ECR.
* [Checkov 🌟](https://github.com/bridgecrewio/checkov/) is a static code analysis tool for infrastructure-as-code. It scans cloud infrastructure provisioned using Terraform, Cloudformation, Kubernetes, Serverless or ARM Templates and detects security and compliance misconfigurations.
* [Cluster Cloner 🌟](https://github.com/doitintl/clustercloner/) Reads the Kubernetes clusters in one location (optionally filtering by labels) and clones them into another (or just outputs JSON as a dry run), to/from AWS, GCP, and Azure.
* [kubectl-eksporter 🌟](https://github.com/Kyrremann/kubectl-eksporter) A simple Ruby-script to export k8s resources, and removes a pre-defined set of fields for later import.
* [kubectl-neat 🌟](https://github.com/itaysk/kubectl-neat) Remove clutter from Kubernetes manifests to make them more readable.
* [medium: 4 Simple Kubernetes Terminal Customizations to Boost Your Productivity](https://medium.com/better-programming/4-simple-kubernetes-terminal-customizations-to-boost-your-productivity-deda60a19924)
* [Move2Kube 🌟](https://github.com/konveyor/move2kube) Move2Kube is a command-line tool that accelerates the process of re-platforming to Kubernetes/Openshift. It does so by analysing the environment and source artifacts, and asking guidance from the user when required. This tool that can help users migrate from Cloud Foundry and Docker Swarm to Kubernetes. https://move2kube.konveyor.io
* [skopeo 🌟](https://github.com/containers/skopeo) Use skopeo to copy images between registries
* [junit5-kubernetes](https://github.com/JeanBaptisteWATENBERG/junit5-kubernetes) aims at using a kubernetes pod directly form your junit5 test classes.
* [mbuffett.com: Replacing ngrok with ktunnel](https://mbuffett.com/posts/ktunnel-ngrok-replace/)
* [seaworthy: A CLI to verify #Kubernetes resource health !! 🌟](https://github.com/cakehappens/seaworthy) Post-apply check to verify your K8s resources are Seaworthy
* [kVDI](https://github.com/tinyzimmer/kvdi) A Kubernetes-native Virtual Desktop Infrastructure.
* [kcg 🌟](https://github.com/bit-cloner/kcg) is a command line tool that lets you create kubeconfig files. The user can interactively choose a namespace and service account and generate a config file with token authentication that has same RBAC permissions assigned to chosen service account.
* [Compass 🌟](https://github.com/winfordlin/Compass) Quickly Pinpoint Errors in your Kubernetes Deployment.
* [kubernetes-dashboard-iam-proxy](https://github.com/Nitro/kubernetes-dashboard-iam-proxy) An in-browser version of aws eks get-token to enable cluster authentication using IAM for the Kubernetes dashboard.
* [Gitkube 🌟](https://github.com/hasura/gitkube) is a tool for building and deploying Docker images on Kubernetes using git push. After a simple initial setup, users can simply keep git push-ing their repos to build and deploy to Kubernetes automatically.
* [vesion-checker](https://github.com/jetstack/version-checker) is a Kubernetes utility for observing the current versions of images running in the cluster, as well as the latest available upstream. These checks get exposed as Prometheus metrics to be viewed on a dashboard, or soft alert cluster operators.
* [Descheduler for Kubernetes 🌟](https://github.com/kubernetes-sigs/descheduler) -> [wecloudpro.com: Balance your Kubernetes cluster](https://www.wecloudpro.com/2020/11/01/Balance-your-kubernetes-cluster.html)
* [kubediff 🌟](https://github.com/weaveworks/kubediff) is a tool for Kubernetes to show you the differences between your running configuration and your version controlled configuration.
* [awslabs/karpenter](https://github.com/awslabs/karpenter) Karpenter is a metrics-driven autoscaler built for Kubernetes and can run in any Kubernetes cluster anywhere. It's performant, extensible, and can autoscale anything that implements the Kubernetes scale subresource.
* [ekglue - Envoy/Kubernetes glue](https://github.com/jrockway/ekglue) ekglue is a projects that facilitates connecting Kubernetes and Envoy, allowing Envoy to read Kubernetes services and endpoints as clusters (via CDS) and endpoints (via EDS).
* [salesforce/Craft](https://github.com/salesforce/craft) CRAFT helps you to create Kubernetes Operators in a robust and generic way for any resource, letting developers focus on CRUD operations of resource management in a Dockerfile.
* [hyscale 🌟](https://github.com/hyscale/hyscale) HyScale takes a declarative definition of your service config and it generates Dockerfile, Container Image, Kubernetes Manifests (YAMLs) and deploys to any Kubernetes Cluster.
* [kubectl-reap is a kubectl plugin that deletes unused Kubernetes resources 🌟](https://github.com/micnncim/kubectl-reap)
* [KubeLinter 🌟](https://github.com/stackrox/kube-linter) is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
* [KRD: Kubernetes Reference Deployment](https://github.com/electrocucaracha/krd) krd offers a reference for deploying a Kubernetes cluster. Its ansible playbooks allow to provision a deployment on Bare-metal or Virtual Machines
* [kubeshell](https://github.com/roubles/kubeshell) is a command line tool to interactively shell in to (and out of) kubernetes pods.
* [k8s-harness 🌟](https://github.com/carlosonunez/k8s-harness) lets you create a disposable Kubernetes cluster with **vagrant and Ansible to test your app in a prod-like environment**.
* [Secret backup operator](https://github.com/geritol/secret-backup-operator) is an operator designed to backup secrets on a Kubernetes cluster. Backup happens when secrets are modified.
* [Devtron 🌟](https://github.com/devtron-labs/devtron) is an open source software delivery workflow for kubernetes written in go. Web based CI/CD Platform for Kubernetes.
* [DevNation: 10 awesome kubernetes tools every user should know](https://bit.ly/kube-tools-1)
    * [developers.redhat.com: 10 awesome Kubernetes tools every user should know | DevNation Tech Talk (video)](https://developers.redhat.com/devnation/tech-talks/10-kubernetes-tools)
* [HyScale 🌟](https://github.com/hyscale/hyscale) takes a declarative definition of your service config and it generates Dockerfile, Container Image, Kubernetes Manifests (YAMLs) and deploys to any Kubernetes Cluster
* [kube-fledged](https://github.com/senthilrch/kube-fledged) is a kubernetes add-on for creating and managing a cache of container images directly on the worker nodes of a kubernetes cluster. It allows a user to define a list of images and onto which worker nodes those images should be cached (i.e. pre-pulled). As a result, application pods start almost instantly, since the images need not be pulled from the registry.
* [Tagger](https://github.com/ricardomaraschini/tagger) keeps references to externally hosted Docker images internally in a Kubernetes cluster by mapping their tags (such as latest) into their references by hash
* [helm-ecr 🌟](https://github.com/vetyy/helm-ecr) is a Helm plugin that supports installing Charts from AWS ECR.
* [PipeCD](https://github.com/pipe-cd/pipe) is a continuous delivery system for declarative Kubernetes, Serverless, and Infrastructure applications.
* [kubecolor 🌟](https://github.com/dty1er/kubecolor) colorises your kubectl output
* [kubectl-sudo](https://github.com/postfinance/kubectl-sudo) This plugin allows users to run kubernetes commands with the security privileges of another user.
* [kfilt](https://github.com/ryane/kfilt) is a tool that lets you filter specific resources from a stream of Kubernetes YAML manifests. It can read manifests from a file, URL, or from stdin.
* [k8s-mirror: Creates a local mirror of a kubernetes cluster in a docker container to support offline reviewing 🌟](https://github.com/darkbitio/k8s-mirror)
* [kube-secret-syncer 🌟](https://github.com/contentful-labs/kube-secret-syncer) is a Kubernetes operator developed using the Kubebuilder framework that keeps the values of Kubernetes Secrets synchronised to secrets in AWS Secrets Manager.
    * [contentful.com: Open-sourcing kube-secret-syncer: A Kubernetes operator to sync secrets from AWS Secrets Manager](https://www.contentful.com/blog/2020/10/20/open-source-kube-secret-syncer/) Kube-secret-syncer is a Kubernetes operator developed using the Kubebuilder framework that keeps the values of Kubernetes Secrets synchronised to secrets in AWS Secrets Manager.
* [kapp 🌟](https://carvel.dev/kapp) is a CLI that calculates changes between your configuration and live cluster state and applies changes you approve.
* [garden.io](https://garden.io/) Break down the barriers between development, testing, and CI. Use the same workflows and production-like Kubernetes environments at every step of the process
    * [thenewstack.io: Garden: The Configure-Once Kubernetes Platform for Seamless Dev/Prod Integration](https://thenewstack.io/garden-the-configure-once-kubernetes-platform-for-seamless-dev-prod-integration/)
* [pvc-autoresizer](https://github.com/topolvm/pvc-autoresizer) resizes PersistentVolumeClaims (PVCs) when the free amount of storage is below the threshold. It queries the volume usage metrics from Prometheus that collects metrics from kubelet.
    * [blog.kintone.io: Introducing pvc-autoresizer](https://blog.kintone.io/entry/pvc-autoresizer) 
* [sKan](https://github.com/alcideio/skan) is a tailor made Kubernetes configuration files and resources scanner that enables developers and devops team members to check whether their work is compliant with security & ops best practices
* [Kubernetes Node Auto Labeller](https://github.com/adaptant-labs/k8s-auto-labeller)
* [Kube_query](https://github.com/Isan-Rivkin/kube_query) Use kubectl but on all of the available k8s clusters available in the kubeconfig file. Currently will query only AWS EKS clusters.
* [kubernetes-event-exporter 🌟](https://github.com/opsgenie/kubernetes-event-exporter) This tool allows exporting the often missed Kubernetes events to various outputs so that they can be used for observability or alerting purposes. You won't believe what you are missing.
* [Kubeconform 🌟](https://github.com/yannh/kubeconform) is a Kubernetes manifests validation tool. Build it into your CI to validate your Kubernetes configuration using the schemas from kubernetes-json-schema
* [Kubernetes Janitor](https://codeberg.org/hjacobs/kube-janitor) cleans up (deletes) Kubernetes resources on a configured TTL (time to live) or a configured expiry date (absolute timestamp).
* [kube-batch](https://github.com/kubernetes-sigs/kube-batch) is a batch scheduler for Kubernetes, providing mechanisms for applications which would like to run batch jobs leveraging Kubernetes. A batch scheduler of kubernetes for high performance workload, e.g. AI/ML, BigData, HPC
* [slipway: A Kubernetes controller to automate gitops provisioning](https://github.com/slipway-gitops/slipway)
* [github.com: dnsconfig-injector - Mutating Admission Webhook for dnsconfig pod injection](https://github.com/karampok/dnsconfig-injector)
* [kubectl-view-webhook 🌟](https://github.com/Trendyol/kubectl-view-webhook) Visualize your webhook configurations in Kubernetes.
* [ContainerSSH: Launch containers on demand 🌟🌟](https://containerssh.io) ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects. Authentication and container configuration are dynamic using webhooks, no system users required.
* [reconshell.com: Kubei – Kubernetes Runtime Vulnerabilities Scanner 🌟](https://reconshell.com/kubei-kubernetes-runtime-vulnerabilities-scanner/)
* [Alcide Advisor: an agentless service for Kubernetes audit and compliance that's built to ensure a frictionless and secured DevSecOps workflow](https://github.com/alcideio/advisor)
* [Lockbox: Offline encryption of Kubernetes Secrets](https://github.com/cloudflare/lockbox) Lockbox is a secure way to store Kubernetes Secrets offline. Secrets are asymmetrically encrypted, and can only be decrypted by the Lockbox Kubernetes controller. A companion CLI tool, locket, makes encrypting secrets a one-step process.
* [openshift: Introducing kube-burner, A tool to Burn Down Kubernetes and OpenShift 🌟](https://www.openshift.com/blog/introducing-kube-burner-a-tool-to-burn-down-kubernetes-and-openshift) Kube-burner is a tool designed to stress different OpenShift components basically by coordinating the creation and deletion of k8s resources. Along this blog series we’ll talk about how to use it in OpenShift 4.
    * [github.com/cloud-bulldozer/kube-burner](https://github.com/cloud-bulldozer/kube-burner) Kube-burner is a tool aimed at stressing Kubernetes clusters by creating or deleting a high quantity of objects
* [kube-ebpf-exporter 🌟](https://github.com/ahas-sigs/kube-ebpf-exporter) Prometheus exporter for custom eBPF metrics.
* [qontract](https://github.com/app-sre/qontract-server) qontract (Queryable cONTRACT) is a collection of tools used to SREs to expose available managed services to application developer teams.
* [sheaf](https://github.com/bryanl/sheaf) Manages bundles of Kubernetes components. sheaf is a tool that can create a bundle of Kubernetes components. It can generate an archive from the bundle that can be distributed for use in Kubernetes clusters. The initial idea was inspired by CNAB. It answers the question: how can I distribute Kubernetes manifests with their associated images?
* [cnab.io: CNABs facilitate the bundling, installing and managing of container-native apps — and their coupled services](https://cnab.io/)
* [tremolosecurity.com: Secure Access to Kubernetes From Your Pipeline](https://www.tremolosecurity.com/post/secure-access-to-kubernetes-from-your-pipeline)
* [openpitrix 🌟](https://github.com/openpitrix/openpitrix) Application Management Platform on Multi-Cloud Environment. OpenPitrix is a web-based open-source system to package, deploy and manage different types of applications including Kubernetes application, microservice application and serverless applications into multiple cloud environment such as AWS, Azure, Kubernetes, QingCloud, OpenStack, VMWare etc.
* [kube-burner 🌟](https://github.com/cloud-bulldozer/kube-burner) Kube-burner is a tool aimed at stressing kubernetes clusters. 
* [gimletd - the GitOps release manager](https://github.com/gimlet-io/gimletd) GimletD acts as a release manager and detaches the release workflow from CI. By doing so, it unlocks the possibility of advanced release logics and flexibility to refactor workflows.
* [kubectl skew 🌟](https://github.com/dty1er/kubectl-skew) A simple kubectl plugin to show if your kubernetes/kubectl version is "skewed". In kubernetes, version skew policy is a bit confusing, especially for beginners. However, it is important to make sure you are always following the policy because using unsupported cluster/kubectl is problematic and even dangerous.
* [github.com/cloudflare/lockbox](https://github.com/cloudflare/lockbox) Offline encryption of Kubernetes Secrets. Lockbox is a secure way to store Kubernetes Secrets offline. Secrets are asymmetrically encrypted, and can only be decrypted by the Lockbox Kubernetes controller. A companion CLI tool, locket, makes encrypting secrets a one-step process.
* [Suspicious pods 🌟](https://github.com/edrevo/suspicious-pods) Prints a list of k8s pods that might not be working correctly
* [Armada](https://github.com/G-Research/armada) A multi-cluster batch queuing system for high-throughput workloads on Kubernetes. Armada is an application to achieve high throughput of run-to-completion jobs on multiple Kubernetes clusters. It stores queues for users/projects with pod specifications and creates these pods once there is available resource in one of the connected Kubernetes clusters.
* [Ko: Easy Go Containers 🌟](https://github.com/google/ko) Build and deploy Go applications on Kubernetes
* [Kubetail 🌟](https://github.com/johanhaleby/kubetail) Bash script to tail Kubernetes logs from multiple pods at the same time
    * [Stern 🌟](https://github.com/wercker/stern) Multi pod and container log tailing for Kubernetes
* [kubestr 🌟](https://kubestr.io/) Explore your Kubernetes storage options. Kubestr is a collection of tools to discover, validate and evaluate your kubernetes storage options.
* [KubeEye: An Automatic Diagnostic Tool that Provides a Holistic View of Your Kubernetes Cluster 🌟](https://kubesphere.io/blogs/kubeeye-automatic-cluster-diagnostic-tool/)
* [k8gb 🌟](https://github.com/k8gb-io/k8gb) A cloud native Kubernetes Global Balancer [k8gb.io](https://www.k8gb.io/)
* [k8s-image-swapper 🌟](https://github.com/estahn/k8s-image-swapper) Mirror images into your own registry and swap image references automatically. [estahn.github.io/k8s-image-swapper](https://estahn.github.io/k8s-image-swapper/)
* [RBACSync 🌟](https://github.com/cruise-automation/rbacsync) Automatically sync groups into Kubernetes RBAC. RBACSync provides a Kubernetes controller to synchronize RoleBindings and ClusterRoleBindings, used in Kubernetes RBAC, from group membership sources using consolidated configuration objects.
* [Saffire](https://github.com/FairwindsOps/saffire) a controller to override image sources in the event that an image cannot be pulled. The intent of saffire is to provide operators with a method of automatically switching image repositories when imagePullErrors occur.
* [vcluster 🌟](https://github.com/loft-sh/vcluster)  Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it offers better multi-tenancy and isolation than regular namespaces.
* [Cluster API Provider for Managed Bare Metal Hardware](https://github.com/metal3-io/cluster-api-provider-metal3) This repository contains a Machine actuator implementation for the Kubernetes Cluster API for managing bare metal hardware - [metal3.io: Bare metal host provisioning for kubernetes](http://metal3.io/)
* [enterprisersproject.com: Kubernetes: 6 open source tools to put your cluster to the test](https://enterprisersproject.com/article/2021/5/kubernetes-6-open-source-tools-to-test-clusters) The Kubernetes ecosystem includes an ever-growing number of tools and services you can plug in: Let’s look at six useful tools for putting your Kubernetes cluster and applications to the test.
* [kubectl-node-restart 🌟](https://github.com/MnrGreg/kubectl-node-restart) Krew plugin to restart Kubernetes Nodes sequentially and gracefully
* [k8s-platform-lcm: Kubernetes platform lifecycle management 🌟](https://github.com/arminc/k8s-platform-lcm) A faster and easier way to manage the lifecycle of applications and tools, running and living around your Kubernetes platform. Kubernetes platform lifecycle management helps you keep track of all your software and tools that are used or running in and around your Kubernetes platform.
* [Nebula](https://github.com/slackhq/nebula) A scalable overlay networking tool with a focus on performance, simplicity and security. It lets you seamlessly connect computers anywhere in the world.
* [kube-bench](https://github.com/aquasecurity/kube-bench) Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
* [kube-bench-exporter](https://github.com/yashvardhan-kukreja/kube-bench-exporter) Helps you to export your kube-bench reports to multiple targets like Amazon S3 buckets with ease.
* [Karmada](https://github.com/karmada-io/karmada) Karmada (Kubernetes Armada) is a Kubernetes management system that enables you to run your cloud-native applications across multiple Kubernetes clusters and clouds, with no changes to your applications. By speaking Kubernetes-native APIs and providing advanced scheduling capabilities, Karmada enables truly open, multi-cloud Kubernetes.
* [kube-secrets-init](https://github.com/doitintl/kube-secrets-init) Kubernetes mutating webhook for `secrets-init` injection
* [liqo: Enable dynamic and seamless Kubernetes multi-cluster topologies](https://github.com/liqotech/liqo) Building your endless Kubernetes ocean. Enable dynamic and seamless Kubernetes multi-cluster topologies. Liqo is a platform to enable dynamic and decentralized resource sharing across Kubernetes clusters, either on-prem or managed. Liqo allows to run pods on a remote cluster seamlessly and without any modification of Kubernetes and the applications. With Liqo it is possible to extend the control plane of a Kubernetes cluster across the cluster's boundaries, making multi-cluster native and transparent: collapse an entire remote cluster to a virtual local node, by allowing workloads offloading and resource management compliant with the standard Kubernetes approach.
* [redhat-certification: chart-verifier: Rules based tool to certify Helm charts 🌟](https://github.com/redhat-certification/chart-verifier)
* [helm-changelog: Create changelogs for Helm Charts, based on git history](https://github.com/mogensen/helm-changelog)
* [ingressbuilder.jetstack.io 🌟🌟](https://ingressbuilder.jetstack.io) Ingress Builder allows users to select any annotation from the list of available controllers, to add to the ingress manifest.
* [Jetstack Secure Agent 🌟🌟](https://github.com/jetstack/preflight) **Automatically perform Kubernetes cluster configuration checks using Open Policy Agent (OPA)**
* [Replicated Troubleshoot](https://github.com/replicatedhq/troubleshoot) Preflight Checks and Support Bundles Framework for Kubernetes Applications. Replicated Troubleshoot is a framework for collecting, redacting, and analyzing highly customizable diagnostic information about a Kubernetes cluster. Troubleshoot specs are created by 3rd-party application developers/maintainers and run by cluster operators in the initial and ongoing operation of those applications.
* [outdated.sh 🌟](https://outdated.sh/) A kubectl plugin to show out-of-date images running in a cluster.
* [kubestriker 🌟](https://github.com/vchinnipilli/kubestriker) A Blazing fast Security Auditing tool for Kubernetes. Kubestriker is a platform-agnostic tool designed to tackle Kuberenetes cluster security issues due to misconfigurations and will help strengthen the overall IT infrastructure of any organisation.
* [KubeEye 🌟](https://github.com/kubesphere/kubeeye) KubeEye aims to find various problems on Kubernetes, such as application misconfiguration, unhealthy cluster components and node problems.
* [Analyze Kubernetes Audit logs using Falco 🌟](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster) Detect intrusions that happened in your Kubernetes cluster through audit logs using Falco
* [KubeHelper](https://github.com/kubehelper/kubehelper) KubeHelper - simplifies many daily Kubernetes cluster tasks through a web interface. Search, analysis, run commands, cron jobs, reports, filters, git synchronization and many more.
* [kubewebhook](https://github.com/slok/kubewebhook) Go framework to create Kubernetes mutating and validating webhooks
* [kaDalu](https://github.com/kadalu/kadalu) A lightweight Persistent storage solution for Kubernetes / OpenShift using GlusterFS in background. Kadalu is a project which started as an idea to make glusterfs's deployment and management simpler in kubernetes
* [forklift.konveyor.io 🌟](https://forklift.konveyor.io/) A tool that accelerates the process of re-hosting / re-platforming virtual machines to Kubernetes and KubeVirt. It does so by mapping resources (network and storage), creating equivalent resources int he target, and converting disk images.
    * [opensource.com: Migrate virtual machines to Kubernetes with this new tool - forklift 🌟](https://opensource.com/article/21/6/migrate-vms-kubernetes-forklift) Transition your virtualized workloads to Kubernetes with Forklift.
    * [konveyor 🌟](https://www.konveyor.io/) is an open source project that helps transition existing workloads (development, test, and production) to Kubernetes. Its tools include Crane, to move containers from one Kubernetes platform to another; Move2Kube, to bring workloads from Cloud Foundry to Kubernetes; and Tackle, to analyze Java applications to modernize them by making them more standard and portable for the runtimes available in containerized platforms like Kubernetes.
* [go-containerregistry 🌟](https://github.com/google/go-containerregistry) Go library and CLIs for working with container registries
* [kubebox](https://github.com/astefanutti/kubebox) Terminal and Web console for Kubernetes
* [skooner - Kubernetes Dashboard](https://github.com/skooner-k8s/skooner) Simple Kubernetes realtime dashboard and management
* [Polaris: Best Practices for Kubernetes Workload Configuration 🌟](https://github.com/FairwindsOps/polaris) Validation of best practices in your Kubernetes clusters - [fairwinds.com: What is Fairwinds’ Polaris? Kubernetes Open Source Configuration Validation](https://www.fairwinds.com/blog/fairwinds-polaris-kubernetes-open-source-configuration-validation) 
* [Krane 🌟](https://github.com/appvia/krane) is a Kubernetes RBAC static analysis tool. It identifies potential security risks in K8s RBAC design and makes suggestions on how to mitigate them. Krane dashboard presents current RBAC security posture and lets you navigate through its definition.
* [KTail: Kubernetes log viewer 🌟](https://www.ktail.de/) KTail allows you to tail multiple pods in one view. It automatically detects updates and attaches to new pods. Configurable highlighters show how often regular expressions matched and let you quickly navigate in the results.
* [Manifesto 🌟](https://gitlab.com/jackatbancast/manifesto) allows you to create an application structure to facilitate easy deployment to kubernetes. Jsonnet is used to create the underlying application structure, manifesto manipulates this structure to produce manifests.
* [==SigNoz: Open source Application Performance Monitoring (APM) & Observability tool== 🌟](https://github.com/SigNoz/signoz) SigNoz helps developers monitor their applications & troubleshoot problems, an open-source alternative to DataDog, NewRelic, etc. 
* [port-map-operator](https://github.com/MOZGIII/port-map-operator) LoadBalancer Service type implementation for home clusters via Port Control Protocol.
* [Raspbernetes - Kubernetes Cluster: k8s-gitops](https://github.com/xUnholy/k8s-gitops) Kubernetes cluster managed by GitOps - Git as a single source of truth, automated pipelines, declarative everything, next-generation DevOps. This repo is a declarative implementation of a Kubernetes cluster. It's using the GitOps Toolkit known as Fluxv2. The goal is to demonstrates how to implement enterprise-grade security, observability, and overall cluster config management using GitOps in a Kubernetes cluster.
* [KubeHelper](https://github.com/kubehelper/kubehelper) KubeHelper - simplifies many daily Kubernetes cluster tasks through a web interface. Search, analysis, run commands, cron jobs, reports, filters, git synchronization and many more.
* [Kpexec](https://github.com/ssup2/kpexec) kpexec is a kubernetes cli that runs commands in a container with high privileges. 
* [OpenShiftKubeAudit](https://github.com/AICoE/OpenShiftKubeAudit) An auditing program to detect incompatibilities in Kubernetes manifests brought over to OpenShift. This auditing tool currently only supports Kubernetes manifests, but we plan to expand it to include Helm charts and Go code, as well. The tool is in very early stages, but is looking for community input to help add use cases.
* [Kubernetes Kpt in The Wild: What it is and how to use it 🌟](https://labs.meanpug.com/kubernetes-kpt-in-the-wild) Kubernetes Kpt is tooling by Google that facilitates a structured approach to defining, managing, and distributing kubernetes templates between teams and orgs.
* [RollingUpgrade](https://github.com/keikoproj/upgrade-manager) Reliable, extensible rolling-upgrades of Autoscaling groups in Kubernetes
* [Kerbi 🌟](https://github.com/nmachine-io/kerbi) Kerbi (Kubernetes Emdedded Ruby Interpolator) is yet another templating engine for generating Kubernetes resource manifests. It enables multi-strategy, multi-source templating, giving you the freedom to design highly specialized templating pipelines.
* [Kourier](https://github.com/knative-sandbox/net-kourier) Purpose-built Knative Ingress implementation using just Envoy with no additional CRDs. Kourier is an Ingress for Knative Serving. Kourier is a lightweight alternative for the Istio ingress as its deployment consists only of an Envoy proxy and a control plane for it.
* [space-cloud: Develop, Deploy and Secure Serverless Apps on Kubernetes.](https://github.com/spacecloud-io/space-cloud) Open source Firebase + Heroku to develop, scale and secure serverless apps on Kubernetes - [space-cloud.io](https://space-cloud.io/) Space Cloud is a Kubernetes based serverless platform that provides instant, realtime APIs on any database, with event triggers and unified APIs for your custom business logic.
* [community.suse.com: Comparing Modern-Day Container Image Builders: Jib, Buildpacks and Docker 🌟](https://community.suse.com/posts/comparing-modern-day-container-image-builders-jib-buildpacks-and-docker) 
* [Teleport 🌟](https://github.com/gravitational/teleport) Certificate authority and access plane for SSH, Kubernetes, web applications, and databases 
* [weaveworks: kured - Kubernetes Reboot Daemon 🌟](https://github.com/weaveworks/kured) - [weave.works: One year kured - your Kubernetes Reboot Daemon](https://www.weave.works/blog/one-year-kured-kubernetes-reboot-daemon) Kured (KUbernetes REboot Daemon) is a Kubernetes daemonset that performs safe automatic node reboots when the need to do so is indicated by the package management system of the underlying OS. Many rely on Kured, which helps perform safe automatic node reboots when indicated by the package management of the underlying OS, to help make OS security better.
* [k8s-cluster-simulator](https://github.com/pfnet-research/k8s-cluster-simulator) Kubernetes cluster simulator for evaluating schedulers.
* [kubelogin 🌟](https://github.com/int128/kubelogin) kubectl plugin for Kubernetes OpenID Connect authentication (kubectl oidc-login)
* [==kube-oidc-proxy==](https://github.com/jetstack/kube-oidc-proxy) Reverse proxy to authenticate to managed Kubernetes API servers via OIDC.
    * [==tremolosecurity.com: Updating kube-oidc-proxy==](https://www.tremolosecurity.com/post/updating-kube-oidc-proxy) **Kubernetes offers multiple ways to authenticate users to the API server. The best way to go, when available, is to use OpenID Connect (OIDC). We've talked about why you shouldn't use certificates for kubernetes authentication, but most cloud providers won't let you configure the API server flags needed to integrate managed clusters into an OIDC identity provider.**
* [KubeSurvival 🌟](https://github.com/aporia-ai/kubesurvival) Significantly reduce Kubernetes costs by finding the cheapest machine types that can run your workloads
* [K8s Vault Webhook 🌟](https://ot-container-kit.github.io/k8s-vault-webhook/) - [github: k8s-vault-webhook](https://github.com/OT-CONTAINER-KIT/k8s-vault-webhook) A k8s vault webhook is a Kubernetes webhook that can inject secrets into Kubernetes resources by connecting to multiple secret managers
* [cf-for-k8s](https://github.com/cloudfoundry/cf-for-k8s) The open source deployment manifest for Cloud Foundry on Kubernetes. cf-for-k8s blends the popular CF developer API with Kubernetes, Istio, and other open source technologies. The project aims to improve developer productivity for organizations using Kubernetes
* [tekline 🌟](https://github.com/joyrex2001/tekline) tekline is a tekton delegated-pipeline to enable a bring-your-own pipeline configuration.
* [nerdctl 🌟](https://github.com/containerd/nerdctl) Docker-compatible CLI for containerd
* [El Carro: The Oracle Operator for Kubernetes 🌟](https://github.com/GoogleCloudPlatform/elcarro-oracle-operator) El Carro is a new project that offers a way to run Oracle databases in Kubernetes as a portable, open source, community driven, no vendor lock-in container orchestration system. El Carro provides a powerful declarative API for comprehensive and consistent configuration and deployment as well as for real-time operations and monitoring.
* [jspolicy](https://github.com/loft-sh/jspolicy) jsPolicy is an operator that helps you define Kubernetes Policies using JavaScript or TypeScript. Easier & Faster Kubernetes Policies using JavaScript or TypeScript.
* [k8scr 🌟](https://github.com/hasheddan/k8scr) A kubectl plugin for pushing OCI images through the Kubernetes API server.
* [jsonnet-controller](https://github.com/pelotech/jsonnet-controller) A fluxcd controller for managing manifests declared in jsonnet.
* [rback: RBAC in Kubernetes visualizer 🌟🌟](https://github.com/team-soteria/rback) A simple "RBAC in Kubernetes" visualizer. No matter how complex the setup, rback queries all RBAC related information of an Kubernetes cluster in constant time and generates a graph representation of service accounts, (cluster) roles, and the respective access rules in dot format.
* [github: Kubernetes JSON Schemas 🌟](https://github.com/instrumenta/kubernetes-json-schema) Schemas for every version of every object in every version of Kubernetes
* [kcp: a prototype of a Kubernetes API server that is not a Kubernetes cluster - a place to create, update, and maintain Kube-like APIs with controllers above or without clusters](https://github.com/kcp-dev/kcp) Kubernetes is mainly known as a container orchestration platform today, but we believe it can be even more. With the power of CustomResourceDefinitions, Kubernetes provides a flexible platform for declarative APIs of all types, and the reconciliation pattern common to Kubernetes controllers is a powerful tool in building robust, expressive systems. At the same time, a diverse and creative community of tools and services has sprung up around Kubernetes APIs. Imagine a declarative Kubernetes-style API for anything, supported by an ecosystem of Kubernetes-aware tooling, separate from Kubernetes-the-container-orchestrator. That's kcp.
* [Metacontroller](https://github.com/metacontroller/metacontroller) Metacontroller is an add-on for Kubernetes that makes it easy to write and deploy custom controllers in the form of simple scripts.
* [KubeCarrier - Service Management at Scale](https://github.com/kubermatic/kubecarrier) KubeCarrier is an open source system for managing applications and services across multiple Kubernetes Clusters; providing a framework to centralize the management of services and provide these services with external users in a self service hub.
* [github.com: NFS Ganesha server and external provisioner](https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner) NFS Ganesha Server and Volume Provisioner. nfs-ganesha-server-and-external-provisioner is an out-of-tree dynamic provisioner for Kubernetes 1.14+. You can use it to quickly & easily deploy shared storage that works almost anywhere. 
* [Armada kubectl plugin 🌟](https://github.com/night-gold/armada) Command line tools to manage kustomize packaged apps deployment. Armada is a Kubectl plugin that adds templating capacity and manage deployment to Kustomize apps. Templating uses go template to allow you to generate kustomize apps with templates inside. Armada allows you to git clone a packaged kustomize base and call it with the help of a config file.
* [Minnaker](https://github.com/armory/minnaker) Minnaker is a simple way to install Spinnaker inside a VM. Spinnaker on Lightweight Kubernetes (K3s)
* [kVDI](https://github.com/kvdi/kvdi) A Kubernetes-native Virtual Desktop Infrastructure
* [Kubesurveyor 🌟](https://github.com/viralpoetry/kubesurveyor) Good enough Kubernetes namespace visualization tool. No provisioning to a cluster required, only Kubernetes API is scrapped.
* [NVIDIA k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin) NVIDIA device plugin for Kubernetes. The NVIDIA device plugin for Kubernetes is a Daemonset that allows you to automatically: Expose GPUs on each nodes of your cluster, Keep track of the health of your GPUs, Run GPU enabled containers.
* [kubectl-tmux-exec](https://github.com/predatorray/kubectl-tmux-exec) A kubectl plugin to control multiple pods simultaneously using Tmux
* [grype: a vulnerability scanner for container images and filesystems](https://github.com/anchore/grype)
* [KubeView 🌟](https://github.com/benc-uk/kubeview) Kubernetes cluster visualiser and graphical explorer. KubeView displays what is happening inside a Kubernetes cluster (or single namespace), it maps out the API objects and how they are interconnected. Data is fetched real-time from the Kubernetes API. The status of some objects (Pods, ReplicaSets, Deployments) is colour coded red/green to represent their status and health
* [karma 🌟](https://github.com/prymitive/karma) Alert dashboard for Prometheus Alertmanager
* [Rancher Desktop 🌟](https://github.com/rancher-sandbox/rancher-desktop) Kubernetes and container management to the desktop. Rancher Desktop is an open-source project to bring Kubernetes and container management to the desktop. Windows and macOS versions of Rancher Desktop are available for download.
* [realvz/awesome-eks: A curated list of awesome tools for Amazon EKS 🌟](https://github.com/realvz/awesome-eks)
* [salesforce/Sloop - Kubernetes History Visualization 🌟](https://github.com/salesforce/sloop) Sloop monitors Kubernetes, recording histories of events and resource state changes and providing visualizations to aid in debugging past events.
* [scalabledelivery/init-sync](https://github.com/scalabledelivery/init-sync) Sidecar for securely copying directory for statefulsets. A sidecar containner and initContainer for securely copying a directory between pods in StatefulSets.
* [Keel 🌟](https://github.com/keel-hq/keel) Kubernetes Operator to automate Helm, DaemonSet, StatefulSet & Deployment updates
* [Kspan - Turning Kubernetes Events into spans 🌟](https://github.com/weaveworks-experiments/kspan) Most Kubernetes components produce Events when something interesting happens. This program turns those Events into OpenTelemetry Spans, joining them up by causality and grouping them together into Traces.
* [csi-rclone: CSI rclone mount plugin](https://github.com/wunderio/csi-rclone) CSI driver for rclone. This project implements Container Storage Interface (CSI) plugin that allows using rclone mount as storage backend. Rclone mount points and parameters can be configured using Secret or PersistentVolume volumeAttibutes.
* [stackrox.io: Top 9 Open Source DevSecOps Tools for Kubernetes in 2021 🌟](https://www.stackrox.io/blog/top-9-open-source-devsecops-tools-for-kubernetes/) **Anchore, Checkov, Clair, Falco, Kube-bench, Kube-hunter, KubeLinter, Open Policy Agent (OPA), Terrascan**
* [Kdo: deployless development on Kubernetes 🌟](https://kdo.dev/) Kdo is a command line tool that enables developers to run, develop and test code changes in a realistic deployed setting without having to deal with the complexity of Kubernetes deployment and configuration.
* [chekr](https://github.com/ckotzbauer/chekr) A inspection utility for the maintenance of Kubernetes clusters.
    * [github.com issues: Generate Kyverno deprecation policies with chekr](https://github.com/ckotzbauer/chekr/issues/61)
* [KUR8 🌟](https://github.com/oslabs-beta/KUR8) A visual overview of Kubernetes architecture and Prometheus metrics. KUR8 is an open-source Kubernetes analytics, monitoring, and visualizer web application that allows for querying, alerts, and creating custom charts and graphs that leverage Prothemeus and its time logged series database metrics.
* [mperezco/forklift-configmap-service](https://github.com/mperezco/forklift-configmap-service) Systemd service to run in VMs on KubeVirt to mount ConfigMaps
* [cdk8s](https://github.com/cdk8s-team/cdk8s) Define Kubernetes native apps and abstractions using object-oriented programming
* [Havener](https://github.com/homeport/havener) Think of it as a swiss army knife for Kubernetes tasks. 
* [KFServing 🌟](https://github.com/kubeflow/kfserving) Serverless Inferencing on Kubernetes. KFServing provides a Kubernetes Custom Resource Definition for serving machine learning (ML) models on arbitrary frameworks. It aims to solve production model serving use cases by providing performant, high abstraction interfaces for common ML frameworks like Tensorflow, XGBoost, ScikitLearn, PyTorch, and ONNX.
* [rkubelog 🌟](https://github.com/solarwinds/rkubelog) Send k8s Logs to Papertrail and Loggly Without DaemonSets (for Nodeless Clusters) - [dzone: ContainerD Kubernetes Syslog Forwarding](https://dzone.com/articles/containerd-kubernetes-syslog-forwarding) Move from Logspout to Filebeat to support containerd logging architecture.
* [kubernetes-sigs: Trimaran: Load-aware scheduling plugins 🌟](https://github.com/kubernetes-sigs/scheduler-plugins/tree/master/pkg/trimaran) Trimaran is a collection of load-aware scheduler plugins - [thenewstack.io: IBM, Red Hat Bring Load-Aware Resource Management to Kubernetes](https://thenewstack.io/ibm-red-hat-bring-load-aware-resource-management-to-kubernetes/)
* [AWS Controllers for Kubernetes (ACK) 🌟](https://github.com/aws-controllers-k8s/community) AWS Controllers for Kubernetes (ACK) is a project enabling you to manage AWS services from Kubernetes
* [connaisseur](https://github.com/sse-secure-systems/connaisseur) An admission controller that integrates Container Image Signature Verification into a Kubernetes cluster
* [VolSync 🌟](https://github.com/backube/volsync) Asynchronous data replication for Kubernetes volumes. VolSync asynchronously replicates Kubernetes persistent volumes between clusters using either rsync or rclone. It also supports creating backups of persistent volumes via restic. VolSync, a new storage-agnostic utility for exporting and importing objects from one Kubernetes namespace to another, even across clusters! 
* [ketall](https://github.com/corneliusweig/ketall) Kubectl plugin to show really all kubernetes resources. Like `kubectl get all`, but get really all resources
* [kube-scheduler-simulator](https://github.com/kubernetes-sigs/kube-scheduler-simulator) Web-based Kubernetes scheduler simulator
* [multus-cni 🌟](https://github.com/k8snetworkplumbingwg/multus-cni) A CNI meta-plugin for multi-homed pods in Kubernetes. Multus CNI is a container network interface (CNI) plugin for Kubernetes that enables attaching multiple network interfaces to pods. Typically, in Kubernetes each pod only has one network interface (apart from a loopback) -- with Multus you can create a multi-homed pod that has multiple interfaces. This is accomplished by Multus acting as a "meta-plugin", a CNI plugin that can call multiple other CNI plugins.
* [kim - The Kubernetes Image Manager](https://github.com/rancher/kim)
* [KUDO: The Kubernetes Universal Declarative Operator 🌟](https://kudo.dev/) KUDO is a toolkit that makes it easy to build Kubernetes Operators, in most cases just using YAML.
* [K8sPurger 🌟](https://github.com/yogeshkk/K8sPurger) K8SPurger is a controller that finds all unused resources and show them in a nice format
* [jenkins-x/gsm-controller](https://github.com/jenkins-x/gsm-controller) gsm-controller is a Kubernetes controller that copies secrets from Google Secrets Manager into Kubernetes secrets. The controller watches Kubernetes secrets looking for an annotation, if the annotation is not found on the secret nothing more is done.
* [kontacts](https://github.com/scalabledelivery/kontacts) A Kubernetes directory tool for finding pods and services.
* [sciuro](https://github.com/cloudflare/sciuro) Alertmanager to Kubernetes Node conditions bridge. Sciuro is a bridge between Alertmanager and Kubernetes to sync alerts as Node Conditions. It is designed to work in tandem with other controllers that observe Node Conditions such as draino or the cluster-api. 
* [rottencandy/vimkubectl](https://github.com/rottencandy/vimkubectl) Manage Kubernetes resources from Vim
* [carlosedp/cluster-monitoring: Cluster Monitoring stack for ARM / X86-64 platforms](https://github.com/carlosedp/cluster-monitoring) Cluster monitoring stack for clusters based on Prometheus Operator
* [abhirockzz/kubexpose-operator](https://github.com/abhirockzz/kubexpose-operator) Access your Kubernetes Deployment over the Internet - [itnext.io: Kubexpose: A Kubernetes Operator, for fun and profit!](https://itnext.io/kubexpose-a-kubernetes-operator-for-fun-and-profit-f528586eee07) Access your Kubernetes Deployment over the Internet
* [kubernetes-reflector](https://github.com/emberstack/kubernetes-reflector) **Custom Kubernetes controller that can be used to replicate secrets, configmaps and certificates.**
* [Another Autoscaler](https://github.com/dignajar/another-autoscaler) Another Autoscaler is a Kubernetes controller that automatically starts, stops, or restarts pods from a deployment at a specified time using a cron syntax.
* [cloud-ark/kubeplus 🌟](https://github.com/cloud-ark/kubeplus) Kubernetes Operator to deliver Helm charts as-a-service
* [cloud-ark/caastle](https://github.com/cloud-ark/caastle) Full-stack microservices deployment for Google Kubernetes Engine and Amazon Elastic Container Service
* [eezhee/eezhee](https://github.com/eezhee/eezhee) The easiest way to build a k3s cluster on various public clouds. A super fast and easy way to create a k3s based kubernetes cluster on a variety of public clouds. Currently DigitalOcean, Linode and Vultr are supported. All it takes is a single command and about 2 minutes and your cluster is ready to use. Most of the time is taken by the cloud provider bring up the base VM. Eezhee is ideal for development, testing or learning about Kubernetes.
* [ContainerSolutions/ImageWolf: ImageWolf - Fast Distribution of Docker Images on Clusters](https://github.com/ContainerSolutions/ImageWolf) Fast Distribution of Docker Images on Clusters. ImageWolf is a PoC that provides a blazingly fast way to get Docker images loaded onto your cluster, allowing updates to be pushed out quicker.
* [dcherman/image-cache-daemon)](https://github.com/dcherman/image-cache-daemon) Image Cache Daemon is a service to pre-pull / cache images on Kubernetes before they're needed
* [KnicKnic/temp-kubernetes-ci: Temp Kubernetes CI](https://github.com/KnicKnic/temp-kubernetes-ci) A github action to create a k3s kubernetes cluster in your CI VM for both linux & windows. Also has cmdline to copy and paste for other CI platforms.
* [mattmoor/warm-image: Kubernetes WarmImage CRD](https://github.com/mattmoor/warm-image) A Kubernetes CRD for prefetching container images onto nodes.
* [maorfr/kube-tasks: Kube tasks](https://github.com/maorfr/kube-tasks) A tool to perform simple Kubernetes related actions. Simple Backups, Wait for Pods, Execute a command in a container. 
* [tmobile/MagTape](https://github.com/tmobile/magtape) MagTape Policy-as-Code for Kubernetes. MagTape is a Policy-as-Code tool for Kubernetes that allows for evaluating Kubernetes resources against a set of defined policies. MagTape includes variable policy enforcement, notifications, and targeted metrics
* [vidispine/HULL - Helm Uniform Layer Library](https://github.com/vidispine/hull) HULL (Helm Uniform Layer Library) is designed to ease building, maintaining and configuring Kubernetes objects in Helm charts.
* [hiddeco/Cronjobber](https://github.com/hiddeco/cronjobber) Cronjobber is a cronjob controller for Kubernetes with support for time zones
* [karmab/autolabeller](https://github.com/karmab/autolabeller) This repo contains a controller automatically labelling nodes based on either:
    * predefined regex rules matching node name.
    * a set of matching labels (with their associated value) present on the node.
* [kubernetes-sigs/nfs-subdir-external-provisioner: Kubernetes NFS Subdir External Provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner) Dynamic sub-dir volume provisioner on a remote NFS server. NFS subdir external provisioner is an automatic provisioner that use your existing NFS server to support dynamic provisioning of Kubernetes Persistent Volumes via Persistent Volume Claims
* [ori-edge/k8s_gateway](https://github.com/ori-edge/k8s_gateway) A CoreDNS plugin to resolve all types of external Kubernetes resources. k8s_gateway is a CoreDNS plugin that resolves load balancer and external IPs from outside Kubernetes clusters and supports all types of Kubernetes external resources - Ingress, Service of type LoadBalancer.
* [viaduct-ai/kustomize-sops](https://github.com/viaduct-ai/kustomize-sops) KSOPS - A Flexible Kustomize Plugin for SOPS Encrypted Resources
* [vadosware.io: Using Makefiles And Envsubst As An Alternative To Helm And Ksonnet (deprecated)](https://vadosware.io/post/using-makefiles-and-envsubst-as-an-alternative-to-helm-and-ksonnet/)
* [uw-labs.github.io: Kubernetes Semaphore: A modular and nonintrusive framework for cross cluster communication](https://uw-labs.github.io/blog/kubernetes,/multicluster/2021/07/21/kube-semaphore-intro.html)
* [zakkg3/ClusterSecret: Kubernetes ClusterSecret operator](https://github.com/zakkg3/ClusterSecret) ClusterSecret operator makes sure all the matching namespaces have the secret available. New namespaces, if they match the pattern, will also have the secret. Any change on the ClusterSecret will update all related secrets. Deleting the ClusterSecret deletes "child" secrets (all cloned secrets) too. 
* [tektoncd/chains](https://github.com/tektoncd/chains) Tekton Chains is a Kubernetes Custom Resource Definition (CRD) controller that allows you to manage your supply chain security in Tekton.
* [gopaddle-io/configurator](https://github.com/gopaddle-io/configurator) Synchronize and Version Control ConfigMaps & Secrets across Deployment Rollouts.
* [biosimulations/deployment](https://github.com/biosimulations/deployment) Kubernetes Configuration for [BioSimulations](https://github.com/biosimulations/biosimulations) platform. 
* [chrislusf/seaweedfs](https://github.com/chrislusf/seaweedfs) SeaweedFS is a fast distributed storage system for blobs, objects, files, and data lake, for billions of files! Blob store has O(1) disk seek, local tiering, cloud tiering. Filer supports Cloud Drive, cross-DC active-active replication, Kubernetes, POSIX FUSE mount, S3 API, Hadoop, WebDAV, encryption, Erasure Coding.
* [kubernetes-sigs/kui](https://github.com/kubernetes-sigs/kui) A hybrid command-line/UI development experience for cloud-native development
* [DaspawnW/vault-crd](https://github.com/DaspawnW/vault-crd) Vault CRD for sharing Vault Secrets with Kubernetes. Vault-CRD is a custom resource definition for holding secrets that are stored in HashiCorp Vault and kept up to date with Kubernetes secrets
* [stakater/Reloader 🌟](https://github.com/stakater/Reloader) A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig 
* [dignajar/another-ldap](https://github.com/dignajar/another-ldap) Another LDAP is a form-based authentication for Active Directory / LDAP server. Provides Authentication and Authorization for your applications running in Kubernetes.
* [ddosify/ddosify](https://github.com/ddosify/ddosify) High-performance load testing tool, written in Golang.
* [==anchore/syft==](https://github.com/anchore/syft) CLI tool and library for generating a Software Bill of Materials from container images and filesystems. Exceptional for vulnerability detection when used with a scanner tool like Grype.
* [==aws/aws-node-termination-handler== 🌟](https://github.com/aws/aws-node-termination-handler) Gracefully handle EC2 instance shutdown within Kubernetes
* [aelsabbahy/goss](https://github.com/aelsabbahy/goss) Quick and Easy server testing/validation
* [chr-fritz/csi-sshfs](https://github.com/chr-fritz/csi-sshfs) Kubernetes CSI Plugin for SSHFS. It allows to mount directories using a ssh connection.
* [ctrox/csi-s3](https://github.com/ctrox/csi-s3) A Container Storage Interface for S3. This is a Container Storage Interface (CSI) for S3 (or S3 compatible) storage. This can dynamically allocate buckets and mount them via a fuse mount into any container.
* [codesenberg/bombardier 🌟](https://github.com/codesenberg/bombardier) Fast cross-platform HTTP benchmarking tool written in Go
* [fstab/cifs](https://github.com/fstab/cifs) CIFS Flexvolume Plugin for Kubernetes. Driver for CIFS (SMB, Samba, Windows Share) network filesystems as Kubernetes volumes.
* [kui.tools](https://kui.tools) Kui: CLI-driven Graphics for Kubernetes. Tired of working with Kubernetes in cli mode only? Try kui - a hybrid tool that allows you to interact with any Kubernetes cluster easily with more advanced features available only in GUI.
* [bloomberg/goldpinger 🌟](https://github.com/bloomberg/goldpinger) Debugging tool for Kubernetes which tests and displays connectivity between nodes in the cluster. **Goldpinger makes calls between its instances to monitor your networking. It runs as a DaemonSet on Kubernetes and produces Prometheus metrics that can be scraped, visualised and alerted on.**
* [haxsaw/hikaru 🌟](https://github.com/haxsaw/hikaru) Move smoothly between Kubernetes YAML and Python for creating/updating/componentizing configurations. **Hikaru is a tool that provides you the ability to easily shift between YAML, Python objects/source, and JSON representations of your Kubernetes config files.** It provides assistance in authoring these files in Python, opens up options in how you can assemble and customise the files, and provides some programmatic tools for inspecting large, complex files to enable automation of policy and security compliance. Additionally, Hikaru allows you to use its K8s model objects to interact with Kubernetes, directing it to create, modify, and delete resources.
* [kei6u/kubectl-secret-data](https://github.com/kei6u/kubectl-secret-data) A kubectl plugin for finding decoded secret data with productive search flags.
* [ofek/csi-gcs](https://github.com/ofek/csi-gcs) Kubernetes CSI driver for Google Cloud Storage. An easy-to-use, cross-platform, and highly optimized Kubernetes CSI driver for mounting Google Cloud Storage buckets.
* [target/pod-reaper](https://github.com/target/pod-reaper) ==Rule based pod killing kubernetes controller==. Pod-Reaper was designed to kill pods that meet specific conditions. See the "Implemented Rules" section below for details on specific rules.
* [utilitywarehouse/kube-applier](https://github.com/utilitywarehouse/kube-applier) **kube-applier enables automated deployment and declarative configuration for your Kubernetes cluster.** kube-applier is Kubernetes deployment tool strongly following gitOps principals. It enables continuous deployment of Kubernetes objects by applying declarative configuration files from a Git repository to a Kubernetes cluster.
    * https://github.com/box/kube-applier
* [Trendyol/kink](https://github.com/Trendyol/kink) KinK is a helper CLI that facilitates to manage KinD clusters as Kubernetes pods. Designed to ease clusters up for fast testing with batteries included in mind.
* [vbouchaud/k8s-ldap-auth](https://github.com/vbouchaud/k8s-ldap-auth) Kubernetes webhook token authentication plugin implementation using ldap.
* [wangjia184/pod-inspector](https://github.com/wangjia184/pod-inspector) A tool to inspect pods in kubernetes. Unlike other dashboardes for Kubernetes(Lens / Rancher / etc), ==Kubernetes Pod Inspector allows to check the file system and processes within running Linux pods without using kubectl. This is useful when we want to check the files within volumes mounted by pods==
* [witchery-project/witchery](https://github.com/witchery-project/witchery) build distroless images with alpine tools
* [==knight42/kubectl-blame: kubectl-blame: git-like blame for kubectl==](https://github.com/knight42/kubectl-blame) Show who edited resource fields. A useful opensource tool that comes as a plugin to show who modified attributes in kubernetes resource fields.
* [curiefense/curiefense](https://github.com/curiefense/curiefense) Curiefense extends Envoy proxy to defend against a variety of threats, including SQL and command injection, cross site scripting (XSS), account takeovers (ATOs) and more
* [==kubernetes-sigs/node-feature-discovery: Node feature discovery for Kubernetes==](https://github.com/kubernetes-sigs/node-feature-discovery) Welcome to Node Feature Discovery – a Kubernetes add-on for detecting hardware features and system configuration!
* [grpc-ecosystem/grpc-gateway: gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway) gRPC to JSON proxy generator following the gRPC HTTP spec
* [==arttor/helmify==](https://github.com/arttor/helmify) Creates Helm chart from Kubernetes yaml. Helmify reads a list of supported k8s objects from stdin and converts it to a helm chart. Designed to generate charts for k8s operators but not limited to. See examples of charts generated by helmify.
* [4ARMED/kubeletmein](https://github.com/4ARMED/kubeletmein) Security testing tool for Kubernetes, abusing kubelet credentials on public cloud providers. This is a simple penetration testing tool which takes advantage of public cloud provider approaches to providing kubelet credentials to nodes in a Kubernetes cluster in order to gain privileged access to the k8s API. This access can then potentially be used to further compromise the applications running in the cluster or, in many cases, access secrets that facilitate complete control of Kubernetes.
* [patrickdappollonio/kubectl-slice](https://github.com/patrickdappollonio/kubectl-slice) Split multiple Kubernetes files into smaller files with ease. Split multi-YAML files into individual files.
* [appvia/cosign-keyless-admission-webhook](https://github.com/appvia/cosign-keyless-admission-webhook) Kubernetes admission webhook that uses cosign verify to check the subject and issuer of the image matches what you expect
* [theketchio/ketch 🌟](https://github.com/theketchio/ketch) Ketch is an application delivery framework that facilitates the deployment and management of applications on Kubernetes using a simple command line interface.
* [joyrex2001/kubedock](https://github.com/joyrex2001/kubedock) Kubedock is a minimal implementation of the docker api that will orchestrate containers on a Kubernetes cluster, rather than running containers locally.
* [corneliusweig/konfig](https://github.com/corneliusweig/konfig) konfig helps to merge, split or import kubeconfig files
* [armosec/regolibrary](https://github.com/armosec/regolibrary) ARMO rego library for detecting miss-configurations in Kubernetes manifests
* [groundnuty/k8s-wait-for 🌟](https://github.com/groundnuty/k8s-wait-for) A simple script that allows to wait for a k8s service, job or pods to enter a desired state
* [nabsul/k8s-ecr-login-renew: Renew Kubernetes Docker secrets for AWS ECR](https://github.com/nabsul/k8s-ecr-login-renew) Renews Docker login credentials for an AWS ECR container registry.
* [particledecay/kconf](https://github.com/particledecay/kconf) Manage multiple kubeconfigs easily
* [maruina/aws-auth-manager: K8s controller to manage the aws-auth configmap](https://github.com/maruina/aws-auth-manager) A kuberneres controller to manage the aws-auth configmap in EKS using a new AWSAuthItem CRD.
* [segmentio/kubectl-curl: Kubectl plugin to run curl commands against kubernetes pods](https://github.com/segmentio/kubectl-curl)
* [wallarm/sysbindings](https://github.com/wallarm/sysbindings) sysctl/sysfs settings on a fly for Kubernetes Cluster. No restarts are required for clusters and nodes.

## Penetration Testing Tools
* [intellipaat.com: What is Penetration Testing?](https://intellipaat.com/blog/what-is-penetration-testing) Penetration testing is otherwise referred to as pen testing. This blog on ‘What is Penetration Testing? - Types, Phases, Tools Explained’ discusses in detail what pen testing is and how it works, the numerous tools involved in this field, and so on. This blog aims to give you an insight into pen testing and how Ethical Hackers use it for the purpose of Cyber Security. Let’s dive right in.
* [quarkslab/kdigger](https://github.com/quarkslab/kdigger) kdigger is a context discovery tool for Kubernetes penetration testing.
* [inguardians/peirates](https://github.com/inguardians/peirates) Peirates - Kubernetes Penetration Testing tool

## Deckhouse Kubernetes Platform
* [Deckhouse: NoOps Kubernetes platform 🌟](https://github.com/deckhouse/deckhouse) Deckhouse is an Open Source platform for managing Kubernetes clusters in a fully automatic and uniform fashion. It allows you to create homogeneous Kubernetes clusters anywhere and fully manages them. It supplies all the add-ons you need for auto-scaling, observability, security, and service mesh. It comes in Enterprise Edition (EE) and Community Edition (CE). 

## Porter
- [Porter](https://porter.sh/) Package your application artifact, client tools, configuration and deployment logic together as a versioned bundle that you can distribute, and then install with a single command - [github.com/getporter/porter](https://github.com/getporter/porter) 

## Datree. Quality Checks for Kubernetes YAMLs
- [Datree.io](https://www.datree.io/) Datree prevents kubernetes misconfigurations from reaching production. Datree is a CLI solution that supports kubernetes owners in their roles, by preventing developers from making errors in k8s configurations. 
- [dev.to: CI With Datree](https://dev.to/thenjdevopsguy/ci-with-datree-4h8d) Learn all about Datree, the leader in Kubernetes static code analysis; Helm chart analysis; and how to ensure that all manifest configurations are working properly in a Continuous Integration (CI) build process. [youtube: CI and Building Code With Datree](https://www.youtube.com/watch?v=2Z5HhEk1zK8&ab_channel=MichaelLevan)
* [dev.to: Automating quality checks for Kubernetes YAMLs](https://dev.to/wkrzywiec/automating-quality-checks-for-kubernetes-yamls-398)

## Kaniko Build Images in Kubernetes without docker
- [Kaniko 🌟](https://github.com/GoogleContainerTools/kaniko) Kaniko is a tool to build container images from a Dockerfile. Unlike Docker, Kaniko doesn’t require the Docker daemon. With the help of Kaniko, you won’t be needing to run docker containers with privileged mode.
- [medium: Multibranch and HA Pipeline in Jenkins with Kaniko on GKE](https://medium.com/searce/multibranch-and-ha-pipeline-in-jenkins-with-kaniko-on-gke-8a1e7fa93403)
- [developers.redhat.com: Perform a kaniko build on a Red Hat OpenShift cluster and push the image to a registry](https://developers.redhat.com/articles/2021/06/18/perform-kaniko-build-red-hat-openshift-cluster-and-push-image-registry)
- [devopscube.com: How To Build Docker Image In Kubernetes Pod 🌟](https://devopscube.com/build-docker-image-kubernetes-pod/)
- [learnsteps.com: Kaniko and how you can build images on Kubernetes using kaniko?](https://www.learnsteps.com/kaniko-and-how-you-can-build-images-on-kubernetes-using-kaniko/)
- [kubesandclouds.com: Kaniko: Building images without Docker](https://kubesandclouds.com/index.php/2021/11/04/kaniko/)
- [blog.rewanthtammana.com: Hardening Kaniko build process with Linux capabilities](https://blog.rewanthtammana.com/hardening-kaniko-build-process-with-linux-capabilities) Build images inside Kubernetes/containers? Wide privileges in default configuration? How to secure Kaniko? Can we take things a notch higher?

## Shipwright Framework for Building Container Images on Kubernetes
- [shipwright.io](https://shipwright.io/)
- [cd.foundation: CD Foundation Welcomes Shipwright, Framework for Building Container Images on Kubernetes, As New Incubating Project](https://cd.foundation/blog/2021/08/03/cd-foundation-shipwright-announcement/)

## BuildKit CLI for kubectl
- [BuildKit CLI for kubectl (by vmware-tanzu) 🌟](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl) BuildKit CLI for kubectl is a tool for building container images with your Kubernetes cluster.
- [container-registry.com: Lifting Developers’ Productivity 🌟](https://container-registry.com/posts/productivity-lift-buildkit-cli-for-kubectl/) With BuildKit CLI for kubectl a drop in replacement for docker build

## Buildpacks vs Dockerfiles
- [technology.doximity.com: Buildpacks vs Dockerfiles 🌟](https://technology.doximity.com/articles/buildpacks-vs-dockerfiles) Exploring the tradeoffs of building container images at scale

## Kubevela
- [kubevela.io 🌟](https://kubevela.io/) KubeVela is a modern application platform that makes deploying and managing applications across today's hybrid, multi-cloud environments easier and faster. KubeVela is runtime agnostic, natively extensible, yet most importantly, application-centric .
- [blog.logrocket.com: Intro to KubeVela: A better way to ship applications](https://blog.logrocket.com/kubevela-intro-better-way-ship-applications/) KubeVela makes deploying applications to Kubernetes much easier. Rather than knowing about service, deployment, pods, and horizontal pod scaling, you can specify a much lighter configuration. 

## Pixie. Instantly troubleshoot applications on Kubernetes
- [px.dev: Pixie](https://px.dev) Open source Kubernetes observability for developers. Auto-instrumented. Scriptable. Kubernetes native.
- [docs.pixielabs.ai: Pixie](https://docs.pixielabs.ai/) Instantly debug your applications on Kubernetes
- [github.com: Pixie - Instant Kubernetes-Native Application Observability](https://github.com/pixie-io/pixie/)
- [open source PxL scripts](https://github.com/pixie-labs/pixie/tree/main/pxl_scripts)

## Dekorate. Generate k8s manifests for java apps
* [dekorate.io](http://dekorate.io/)
* [developers.redhat.com: Using Dekorate to generate Kubernetes manifests for Java applications](https://developers.redhat.com/blog/2021/03/17/using-dekorate-to-generate-kubernetes-manifests-for-java-applications/)

## Kubesploit
- [github.com/cyberark/kubesploit 🌟](https://github.com/cyberark/kubesploit) Kubesploit is a cross-platform post-exploitation HTTP/2 Command & Control server and agent dedicated for containerized environments written in Golang and built on top of Merlin project
- [cyberark.com: Kubesploit: A New Offensive Tool for Testing Containerized Environments](https://www.cyberark.com/resources/threat-research-blog/kubesploit-a-new-offensive-tool-for-testing-containerized-environments) 

## Kubeshop
- [Kubeshop 🌟](https://kubeshop.io/) First in the World Open-Source Accelerator/Incubator focusing on building project for Developers in the Kubernetes space
- [venturebeat.com: Kubeshop wants to be a Kubernetes product pipeline](https://venturebeat.com/2021/09/17/kubeshop-wants-to-be-a-kubernetes-product-pipeline/)

## Monokle
- [==kubeshop/monokle==](https://github.com/kubeshop/monokle) Monokle - your friendly desktop UI for managing k8s manifests!
- [medium.com/kubeshop-i: Monokle 1.5.0 Release](https://medium.com/kubeshop-i/monokle-1-5-0-release-kubeshop-95f574563c79) Monokle by @thekubeshop  is your K8s best friend for creating, validating, debugging and managing manifests! Monokle now provides templates to help you get started with creating resources.

## KubeLibrary
- [KubeLibrary](https://github.com/devopsspiral/KubeLibrary) KubeLibrary is a RobotFramework library for testing Kubernetes cluster

## kube-vip
* [kube-vip](https://github.com/kube-vip/kube-vip) is a Load-Balancer for both inside and outside a Kubernetes cluster. 
* **What's one of the biggest pain in implementing Kubernetes for on-prem? Lack of support for LoadBalancer Service.** Now there's a second project (the first is [MetalLB](https://github.com/metallb/metallb)) that provides this functionality for on-prem: kube-vip.

## Kubermetrics
* [oslabs-beta/kubermetrics](https://github.com/oslabs-beta/kubermetrics) Kubermetrics is an open-source dev tool that provides Kubernetes cluster monitoring as well as data visualization in a simple and easy to understand user interface. Kubermetrics intergrates both the Prometheus and Grafana Dashboards on one page! Allowing for custominzable dashboards and alerts.
* [medium: Kubermetrics — Cluster Visualization Made Simple](https://medium.com/@sachem2015/kubermetrics-cluster-visualization-made-simple-d24928f63451)

## Kustomizer
- [kustomizer](https://kustomizer.dev/) Kustomize build, apply, prune command-line utility. Kustomizer is a command-line utility for applying kustomizations on Kubernetes clusters. Kustomizer garbage collector keeps track of the applied resources and prunes the Kubernetes objects that were previously applied on the cluster but are missing from the current revision.

## MetalLB
- [MetalLB](https://github.com/metallb/metallb) A network load-balancer implementation for Kubernetes using standard routing protocols

## Kubermatic Kubernetes Platform
- [Kubermatic Kubernetes Platform 🌟](https://github.com/Kubermatic/Kubermatic) is an open source project to centrally manage the global automation of thousands of Kubernetes clusters across multicloud, on-prem and edge with unparalleled density and resilience.
- [thenewstack.io: Kubermatic Kubernetes Platform Beats Complexity Through Automation](https://thenewstack.io/kubermatic-kubernetes-platform-beats-complexity-through-automation/)

### Kubermatic Kubeone
- [==kubermatic/kubeone== 🌟](https://github.com/kubermatic/kubeone) Kubermatic KubeOne automate cluster operations on all your cloud, on-prem, edge, and IoT environments.
- [youtube.com: How to Write Software That Sets Up Kubernetes Anywhere with Kubermatic Kubeone](https://www.youtube.com/watch?v=BJufhuPK2DY&t=250s&ab_channel=Kubermatic) Kubernetes is a complex system. But installing Kubernetes doesn’t need to be hard. In this short clip, our Software Engineer Marko Mudrinić explains how to use existing tools to make tasks easier for you. He provides you with some insights on the learnings we made while creating KubeOne, an open source and infrastructure-agnostic cluster lifecycle management tool for single and HA Kubernetes clusters.

## Usernetes
- [rootless-containers/usernetes](https://github.com/rootless-containers/usernetes) Kubernetes installable under $HOME, without the root privileges

## k8syaml.com
- [k8syaml.com 🌟](https://k8syaml.com) Kubernetes YAML Generator - Powered by Octopus

## Komodor Workflows
- [komodor.com: Komodor Workflows: Automated Troubleshooting at the Speed of WHOOSH!](https://komodor.com/blog/using-workflows-to-troubleshoot-like-a-pro/)

<center>
[![komodor workflow](images/komodor_workflow.png)](https://komodor.com/blog/using-workflows-to-troubleshoot-like-a-pro/)
</center>

## Popeye
- [Popeye - A Kubernetes Cluster Sanitizer 🌟🌟](https://github.com/derailed/popeye) Popeye is a utility that scans live Kubernetes cluster and reports potential issues with deployed resources and configurations. It sanitizes your cluster based on what's deployed and not what's sitting on disk. By scanning your cluster, it detects misconfigurations and helps you to ensure that best practices are in place, thus preventing future headaches. It aims at reducing the cognitive overload one faces when operating a Kubernetes cluster in the wild. Furthermore, if your cluster employs a metric-server, it reports potential resources over/under allocations and attempts to warn you should your cluster run out of capacity.
- [collabnix.com: Top 10 Kubernetes Tools You Need for 2021 – Popeye](https://collabnix.com/top-10-kubernetes-tools-you-need-for-2021/)

## kbrew
- [kbrew](https://github.com/kbrew-dev/kbrew) kbrew is homebrew for Kubernetes. kbrew is a CLI tool for Kubernetes which makes installing any complex stack easy in one step (And yes we are definitely inspired by Homebrew from MacOS)

## KubExplorer
- [Pscheidl/kubexplorer](https://github.com/Pscheidl/kubexplorer) Detects orphan configmaps and secrets in a Kubernetes cluster

## Kubescape
- [Kubescape 🌟](https://github.com/armosec/kubescape) **kubescape is the first tool for testing if Kubernetes is deployed securely as defined in Kubernetes Hardening Guidance by to NSA and CISA.** Tests are configured with YAML files, making this tool easy to update as test specifications evolve.
- [armosec.io: Use Kubescape to check if your Kubernetes clusters are exposed to the latest K8s Symlink vulnerability (CVE-2021-25741)](https://www.armosec.io/blog/kubescape-checks-if-kubernetes-exposed-to-k8s-symlink-vulnerability-cve202125741)

## Kubectl Connections
- [KubePlus kubectl plugins -> kubectl connections](https://github.com/cloud-ark/kubeplus/blob/master/kubeplus-kubectl-commands.md)
- [cloudark.medium.com: kubectl connections](https://cloudark.medium.com/whats-cooking-in-your-kubernetes-namespace-9200be114f8) that can help you discover and visualize relationship between resources (Deployments, Services, etc.) in your namespace

## Benchmark Operator
- [cloud-bulldozer/benchmark-operator: The Chuck Norris of cloud benchmarks](https://github.com/cloud-bulldozer/benchmark-operator) The intent of this Operator is to deploy common workloads to establish a performance baseline of Kubernetes cluster on your provider.

## Source-To-Image (S2I)
- [openshift/source-to-image](https://github.com/openshift/source-to-image) A tool for building artifacts from source and injecting into container images. Source-to-Image (S2I) is a toolkit and workflow for building reproducible container images from source code. **No writing a bunch of YAML to build your container.**

## VMware Tanzu Octant
* [vmware-tanzu/octant](https://github.com/vmware-tanzu/octant) Highly extensible platform for developers to better understand the complexity of Kubernetes clusters. Octant is a tool for developers to understand how applications run on a Kubernetes cluster. It aims to be part of the developer's toolkit for gaining insight and approaching complexity found in Kubernetes. Octant offers a combination of introspective tooling, cluster navigation, and object management along with a plugin system to further extend its capabilities.

## Qovery Engine
- [Qovery/engine: Qovery Engine 🌟](https://github.com/Qovery/engine) Qovery Engine is an open-source abstraction layer library that turns easy apps deployment on AWS, GCP, Azure, and other Cloud providers in just a few minutes. The Qovery Engine is written in Rust and takes advantage of Terraform, Helm, Kubectl, and Docker to manage resources.

## mck8s Container orchestrator for multi-cluster Kubernetes
- [moule3053/mck8s](https://github.com/moule3053/mck8s) mck8s, short for multi-cluster Kubernetes, allows you to automate the deployment of multi-cluster applications on multiple Kubernetes clusters by offering enhanced configuration possibilities. The main aim of mck8s is maximizing resource utilization and supporting elasitcity across multiple Kubenetes clusters by providing multiple placement policies, as well as bursting, cloud resource provisioning, autoscaling and de-provisioning capabilities. mck8s builds upon other open-source software such as Kubernetes, Kubernetes Federation, kopf, serf, Cilium, Cluster API, and Prometheus.

## Shipwright framework
- [shipwright-io/build: shipwright](https://github.com/shipwright-io/build) A framework for building container images on Kubernetes.
- With Shipwright, developers get a simplified approach for building container images, by defining a minimal YAML that does not require any previous knowledge of containers or container tooling. All you need is your source code in git and access to a container registry.
- Shipwright supports any tool that can build container images in Kubernetes clusters, such as:
    - Kaniko
    - Cloud Native Buildpacks
    - BuildKit
    - Buildah

## Schiff (Deutsche Telekom)
- [telekom/das-schiff](https://github.com/telekom/das-schiff) This is home of Das Schiff - Deutsche Telekom Technik's engine for Kubernetes Cluster as a Service (CaaS) in on-premise environment on top of bare-metal servers and VMs.

## NetMaker 
- [NetMaker](https://github.com/gravitl/netmaker) Netmaker makes networks with WireGuard. Netmaker automates fast, secure, and distributed virtual networks.

## AWS Karpenter kubernetes Autoscaler
- [==Karpenter==](https://karpenter.sh/) Just-in-time Nodes for Any Kubernetes Cluster. __Karpenter simplifies Kubernetes infrastructure with the right nodes at the right time.__ Karpenter automatically launches just the right compute resources to handle your cluster's applications. It is designed to let you take full advantage of the cloud with fast and simple compute provisioning for Kubernetes clusters.
- [techcrunch.com: AWS launches Karpenter, an open source autoscaler for Kubernetes clusters](https://techcrunch.com/2021/11/30/aws-launches-karpenter-an-open-source-autoscaler-for-kubernetes-clusters/)
- [itnext.io: Karpenter: Open-Source, High-Performance Kubernetes Cluster Autoscaler](https://itnext.io/karpenter-open-source-high-performance-kubernetes-cluster-autoscaler-d56e3ab06aae)
- [blog.kloia.com: Karpenter Cluster Autoscaler](https://blog.kloia.com/karpenter-cluster-autoscaler-76d7f7ec0d0e)
- [infoq.com: AWS Releases Multi-Cloud Kubernetes Autoscaler Karpenter](https://www.infoq.com/news/2022/01/karpenter-kubernetes-autoscaler/)

## Kuby (easy deployments of Ruby Rails App)
- [Kuby](https://getkuby.io/) Deploy Your Rails App the Easy Way. Kuby is a convention-over-configuration approach to deploying Rails apps. It makes the power of Docker and Kubernetes accessible to the average Rails developer without requiring a devops black belt.
- [evilmartians.com: Kubing Rails: stressless Kubernetes deployments with Kuby](https://evilmartians.com/chronicles/kubing-rails-stressless-kubernetes-deployments-with-kuby)

## Direktiv
- [Direktiv](https://github.com/direktiv/direktiv) Serverless Container Orchestration. Diretiv is a serverless workflow and automation engine running on Kubernetes and Knative. Direktiv is the equivalent of AWS Step Functions, or Google Cloud Workflows or Alibaba Serverless Workflows. The difference between Direktiv and the cloud provider workflow engines is that Direktiv is cloud & platform agnostic, runs on kubernetes and executes containers as "plugins".
- [blog.direktiv.io: Building a simple cloud-native, orchestrated microservice from containers](https://blog.direktiv.io/building-a-simple-cloud-native-orchestrated-microservice-from-containers-39dbcb80b0d8) 

## Jabos
- [Jabos](https://github.com/srfrnk/jabos)
- [itnext.io: Keep it simple K8s. Kubernetes GitOps using Jabos](https://itnext.io/keep-it-simple-k8s-c0c68c46eabb)

## Pleco
- [Qovery/pleco](https://github.com/Qovery/pleco) Automatically removes Cloud managed services and Kubernetes resources based on tags with TTL
- [qovery.com: Announcement: Pleco - the open-source Kubernetes and Cloud Services garbage collector](https://www.qovery.com/blog/announcement-of-pleco-the-open-source-kubernetes-and-cloud-services-garbage-collector)

## Mesh-kridik
- (chen-keinan/mesh-kridik)[https://github.com/chen-keinan/mesh-kridik] mesh-kridik is an open-source security checker that performs various security checks on a Kubernetes cluster with istio service mesh and is leveraged by OPA (Open Policy Agent) to enforce security rules.
- [kitploit.com: Mesh-Kridik](https://www.kitploit.com/2021/12/mesh-kridik-open-source-security.html)

## kubewatch
- [==bitnami-labs/kubewatch==](https://github.com/bitnami-labs/kubewatch) Watch k8s events and trigger Handlers. kubewatch is a Kubernetes watcher that currently publishes notification to available collaboration hubs/notification channels. Run it in your k8s cluster, and you will get event notifications through webhooks.

## Botkube
- [botkube.io](https://www.botkube.io) BotKube is a messaging bot for monitoring and debugging Kubernetes clusters.

## Robusta
- [Robusta](https://docs.robusta.dev/) Robusta is an open source platform for webhooks and automations. It contains a library of 50+ builtin actions.

## Soup GitOps Operator
- [caldito/soup](https://github.com/caldito/soup) Soup is a GitOps operator for Kubernetes. GitOps continuous deployment and management tool for Kubernetes focused on simplicity.

## Epinio
- https://epinio.io The Application Development Engine for Kubernetes. Epinio is how you tame the developer workflow in Kubernetes to go from Code to URL in a single step.
- [epinio/epinio](https://github.com/epinio/epinio) Opinionated platform that runs on Kubernetes, that takes you from App to URL in one step.

## Testkube
- [kubeshop/testkube](https://github.com/kubeshop/testkube) Kubernetes-native framework for test definition and execution
- [thenewstack.io: TestKube: A New Approach to Cloud Native Testing](https://thenewstack.io/testkube-a-new-approach-to-cloud-native-testing/)

## KuberLogic
- [kuberlogic](https://github.com/kuberlogic/kuberlogic) Kuberlogic is an open-source product that deploys and manages software on top of the Kubernetes cluster and turns infrastructure into a managed PaaS. KuberLogic is that allows running managed databases and popular applications deploying on-premises or at any cloud. The solution provides API, monitoring, backups, and integration with SSO right out of the box

## Kusk
- [kubeshop/kusk: use OpenAPI to configure Kubernetes](https://github.com/kubeshop/kusk) Kusk makes your OpenAPI definition the source of truth for API resources in your cluster. Kusk treats your OpenAPI/Swagger definition as a source of truth for generating supplementary Kubernetes resources for your REST APIs in regard to mappings, security, traffic-control, monitoring, etc.

## Azure AD Workload Identity
- [==Azure/azure-workload-identity==](https://github.com/Azure/azure-workload-identity) Azure AD Workload Identity uses Kubernetes primitives to associate managed identities for Azure resources and identities in Azure Active Directory (AAD) with pods. It simplifies accessing Azure AD protected resources securely from Kubernetes workloads.

## Kubernate
- https://kubernate.dev 
- [laurci/kubernate](https://github.com/laurci/kubernate) Kubernetes+Generate = Kubernate. Kubernate is a Kubernetes YAML generator that can be used as an alternative to other popular tools like Helm. Kubernate is distributed as a library and as a CLI, both working together to achieve one goal: Kubernetes as Code.

## Tackle
- https://www.konveyor.io/tackle
- [redhat.com: How to streamline application portfolio modernization with Tackle](https://www.redhat.com/architect/tackle-application-modernization) Tackle is an open source tool that helps organizations migrate and modernize their application portfolio to leverage Kubernetes without risk of vendor lock-in.

## Azure Placement Policy Scheduler Plugins
- [Azure/placement-policy-scheduler-plugins](https://github.com/Azure/placement-policy-scheduler-plugins) Most of cloud environments today provides cluster admins with ephemeral nodes (VMs). These nodes typically cost significantly less but they offer less reliability than their regular counterpart. Cluster admins are often torn between the choice of cost and reliability because of the innate inability of the default Kubernetes scheduler to place some of a specific workload pods on these nodes. Having the entire workload on ephemeral nodes risks the reliability of the workload when the cloud environment stops these nodes. This scheduler enables cluster admins to offload some configurable percentage of their workloads on these nodes enabling them to decrease the cost of running these pods without affecting its reliability.

## Azure AAD Pod Identity
- [Azure/aad-pod-identity)](https://github.com/Azure/aad-pod-identity) Assign Azure Active Directory Identities to Kubernetes applications.

## MicroShift
- [==microshift.io==](https://microshift.io) **MicroShift is a research project that is exploring how OpenShift1 and Kubernetes can be optimized for small form factor and edge computing.**
- It requires only 2GB to run
- You can run it as a container with Docker or Podman
- It is a very trimmed version of OpenShift without many features

## kubefwd (Kube Forward)
- [==txn2/kubefwd==](https://github.com/txn2/kubefwd) Kubernetes port forwarding for local development.

## Kpng. Kubernetes Proxy NG
- [kubernetes-sigs/kpng](https://github.com/kubernetes-sigs/kpng) Reworking kube-proxy's architecture
- [kubernetes.io: Use KPNG to Write Specialized kube-proxiers](https://kubernetes.io/blog/2021/10/18/use-kpng-to-write-specialized-kube-proxiers/) The post will show you how to create a specialized service kube-proxy style network proxier using Kubernetes Proxy NG kpng without interfering with the existing kube-proxy

## Auto-portforward (apf)
- [ruoshan/autoportforward](https://github.com/ruoshan/autoportforward) Bidirectional port-forwarding for docker, podman and kubernetes. A handy tool to automatically set up proxies that expose the remote container's listening ports back to the local machine. Just like kubectl portforward or docker run -p LOCAL:REMOTE, but automatically discover and update the ports to be forwarded on the fly. apf can create listening ports in the container and forward them back as well.

## gardener/Terraformer
- [gardener/terraformer: Terraformer](https://github.com/gardener/terraformer) Executes Terraform configuration as job/pod inside a Kubernetes cluster. Terraformer is a tool that can execute Terraform commands (apply, destroy and validate) and can be run as a Pod inside a Kubernetes cluster. The Terraform configuration and state files (main.tf, variables.tf, terraform.tfvars and terraform.tfstate) are stored as ConfigMaps and Secrets in the Kubernetes cluster and will be retrieved and updated by Terraformer.

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">One of the biggest problems in IT is that we keep reinventing the wheel.<br><br>We are running the same circles, producing similar technologies to solve the same problems.<br><br>Reinventing the wheel is a great way to learn how the wheel works, but not an efficient way to build software.</p>&mdash; Daniel Moka⚡ (@dmokafa) <a href="https://twitter.com/dmokafa/status/1388448114047164416?ref_src=twsrc%5Etfw">May 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">`kubectl logs --previous` saved my life <a href="https://t.co/mIsCJehVwI">pic.twitter.com/mIsCJehVwI</a></p>&mdash; memenetes (@memenetes) <a href="https://twitter.com/memenetes/status/1425925390644690954?ref_src=twsrc%5Etfw">August 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Tech industry thinks throwing more tools to the problem is the solution. More tools = more failure modes.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1451990747318611968?ref_src=twsrc%5Etfw">October 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Interesting developer tools &amp; frameworks for <a href="https://twitter.com/hashtag/Kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#Kubernetes</a> to learn in 2022:<br>🔹<a href="https://twitter.com/telepresenceio?ref_src=twsrc%5Etfw">@telepresenceio</a> - dev CLI<br>🔹<a href="https://twitter.com/DevSpace?ref_src=twsrc%5Etfw">@DevSpace</a> - dev CLI <br>🔹<a href="https://twitter.com/KnativeProject?ref_src=twsrc%5Etfw">@KnativeProject</a> - <a href="https://twitter.com/hashtag/serverless?src=hash&amp;ref_src=twsrc%5Etfw">#serverless</a> platform<br>🔹<a href="https://twitter.com/skaffolddev?ref_src=twsrc%5Etfw">@skaffolddev</a> - dev CLI<br>🔹<a href="https://twitter.com/hashtag/KubeVela?src=hash&amp;ref_src=twsrc%5Etfw">#KubeVela</a> - <a href="https://twitter.com/oam_dev?ref_src=twsrc%5Etfw">@oam_dev</a> platform<br>🔹<a href="https://twitter.com/okteto?ref_src=twsrc%5Etfw">@okteto</a> - dev platform <br>🔹<a href="https://twitter.com/QuarkusIO?ref_src=twsrc%5Etfw">@QuarkusIO</a> - <a href="https://twitter.com/hashtag/java?src=hash&amp;ref_src=twsrc%5Etfw">#java</a> framework</p>&mdash; Piotr Mińkowski (@piotr_minkowski) <a href="https://twitter.com/piotr_minkowski/status/1475065476388728832?ref_src=twsrc%5Etfw">December 26, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-168051035-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-168051035-1');
</script>


