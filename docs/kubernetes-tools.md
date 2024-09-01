# Kubernetes Plugins, Tools, Extensions and Projects

1. [Introduction](#introduction)
2. [K8s Tools](#k8s-tools)
3. [kubetail](#kubetail)
4. [Portainer](#portainer)
5. [kubecfg](#kubecfg)
6. [Curl](#curl)
7. [kcp](#kcp)
8. [Clusternet](#clusternet)
9. [Open Cluster Management](#open-cluster-management)
10. [Penetration Testing Tools](#penetration-testing-tools)
11. [Deckhouse Kubernetes Platform](#deckhouse-kubernetes-platform)
12. [KubeIP (GKE)](#kubeip-gke)
13. [Porter](#porter)
14. [Datree. Quality Checks for Kubernetes YAMLs](#datree-quality-checks-for-kubernetes-yamls)
15. [Kaniko Build Images in Kubernetes without docker](#kaniko-build-images-in-kubernetes-without-docker)
16. [Shipwright Framework for Building Container Images on Kubernetes](#shipwright-framework-for-building-container-images-on-kubernetes)
17. [BuildKit CLI for kubectl](#buildkit-cli-for-kubectl)
18. [Buildpacks vs Dockerfiles](#buildpacks-vs-dockerfiles)
19. [Kubevela](#kubevela)
20. [Pixie. Instantly troubleshoot applications on Kubernetes](#pixie-instantly-troubleshoot-applications-on-kubernetes)
21. [Dekorate. Generate k8s manifests for java apps](#dekorate-generate-k8s-manifests-for-java-apps)
22. [Kubesploit](#kubesploit)
23. [Kubeshop](#kubeshop)
24. [Monokle](#monokle)
25. [KubeLibrary](#kubelibrary)
26. [kube-vip](#kube-vip)
27. [Kubermetrics](#kubermetrics)
28. [Kustomizer](#kustomizer)
29. [MetalLB](#metallb)
30. [Kubermatic Kubernetes Platform](#kubermatic-kubernetes-platform)
     1. [Kubermatic Kubeone](#kubermatic-kubeone)
31. [Usernetes](#usernetes)
32. [k8syaml.com](#k8syamlcom)
33. [Popeye](#popeye)
34. [kbrew](#kbrew)
35. [KubExplorer](#kubexplorer)
36. [Kubescape](#kubescape)
37. [Kubectl Connections](#kubectl-connections)
38. [Benchmark Operator](#benchmark-operator)
39. [Source-To-Image (S2I)](#source-to-image-s2i)
40. [VMware Tanzu Octant](#vmware-tanzu-octant)
41. [Qovery Engine](#qovery-engine)
42. [mck8s Container orchestrator for multi-cluster Kubernetes](#mck8s-container-orchestrator-for-multi-cluster-kubernetes)
43. [Shipwright framework](#shipwright-framework)
44. [Schiff (Deutsche Telekom)](#schiff-deutsche-telekom)
45. [NetMaker](#netmaker)
46. [AWS Karpenter kubernetes Autoscaler](#aws-karpenter-kubernetes-autoscaler)
47. [Kuby (easy deployments of Ruby Rails App)](#kuby-easy-deployments-of-ruby-rails-app)
48. [Direktiv](#direktiv)
49. [Jabos](#jabos)
50. [Pleco](#pleco)
51. [Mesh-kridik](#mesh-kridik)
52. [kubewatch](#kubewatch)
53. [Botkube](#botkube)
54. [Robusta](#robusta)
55. [Soup GitOps Operator](#soup-gitops-operator)
56. [Epinio](#epinio)
57. [Testkube](#testkube)
58. [KuberLogic](#kuberlogic)
59. [Kusk](#kusk)
60. [Azure AD Workload Identity](#azure-ad-workload-identity)
61. [Kubernate](#kubernate)
62. [Tackle](#tackle)
63. [Azure Placement Policy Scheduler Plugins](#azure-placement-policy-scheduler-plugins)
64. [Azure AAD Pod Identity](#azure-aad-pod-identity)
65. [MicroShift](#microshift)
66. [kubefwd (Kube Forward)](#kubefwd-kube-forward)
67. [Kpng. Kubernetes Proxy NG](#kpng-kubernetes-proxy-ng)
68. [Auto-portforward (apf)](#auto-portforward-apf)
69. [Gardener](#gardener)
70. [Werf](#werf)
71. [Starboard kubernetes-native security toolkit](#starboard-kubernetes-native-security-toolkit)
72. [Netshoot](#netshoot)
73. [The Hierarchical Namespace Controller (HNC)](#the-hierarchical-namespace-controller-hnc)
74. [Kratix](#kratix)
75. [gRPC-Gateway](#grpc-gateway)
76. [KubeOrbit. Test your app on kubernetes](#kubeorbit-test-your-app-on-kubernetes)
77. [Mizu API Traffic Viewer for Kubernetes](#mizu-api-traffic-viewer-for-kubernetes)
78. [vcluster](#vcluster)
79. [Kateyes](#kateyes)
80. [Keepass Secret](#keepass-secret)
81. [Workflow Schedulers](#workflow-schedulers)
     1. [Komodor Workflows](#komodor-workflows)
82. [Azure Eraser](#azure-eraser)
83. [Data Pipeline Workflow Schedulers](#data-pipeline-workflow-schedulers)
84. [ConfigMap Reloader](#configmap-reloader)
85. [Kluctl](#kluctl)
86. [k2tf Kubernetes YAML to Terraform HCL converter](#k2tf-kubernetes-yaml-to-terraform-hcl-converter)
87. [Kubernetes Security Tools](#kubernetes-security-tools)
88. [PureLB](#purelb)
89. [Murre](#murre)
90. [k9s](#k9s)
91. [Pluto](#pluto)
92. [Konf Lightweight Kubeconfig Manager](#konf-lightweight-kubeconfig-manager)
93. [K8spacket](#k8spacket)
94. [Infrastructure as Code using Kubernetes. Config Connector](#infrastructure-as-code-using-kubernetes-config-connector)
95. [Claudie Cloud-agnostic managed Kubernetes](#claudie-cloud-agnostic-managed-kubernetes)
96. [Observability Monitoring Tools](#observability-monitoring-tools)
     1. [Debugging and Troubleshooting Tools](#debugging-and-troubleshooting-tools)
97. [Security](#security)
98. [Develop microservices locally while being connected to your Kubernetes environment](#develop-microservices-locally-while-being-connected-to-your-kubernetes-environment)
99. [AI Tools](#ai-tools)
100. [Tweets](#tweets)
101. [Videos](#videos)

## Introduction

- [collabnix.com: Top 10 Kubernetes Tools You Need for 2021 – Part 1](https://collabnix.com/top-10-kubernetes-tools-you-need-for-2021/)
- [collabnix.com: Top 10 Kubernetes Tools You Need for 2021 – Part 2](https://collabnix.com/top-10-kubernetes-tool-you-need-for-2021-part-2/)
- [collabnix.github.io: Kubetools - A Curated List of Kubernetes Tools: Kubetools - A Curated List of Kubernetes Tools](https://collabnix.github.io/kubetools/)
- [cyberithub.com: 70+ Important Kubernetes Related Tools You Should Know About](https://www.cyberithub.com/70-important-kubernetes-related-tools-you-should-know-about)
- [itnext.io: Kubernetes GitOps Tools](https://itnext.io/kubernetes-gitops-tools-cf0247eb5368)
- [itnext.io: Kubernetes Essential Tools: 2021](https://itnext.io/kubernetes-essential-tools-2021-def12e84c572)
- [containerjournal.com: 9 Open Source Developer Tools for Kubernetes](https://containerjournal.com/features/9-open-source-developer-tools-for-kubernetes/)
- [blog.devgenius.io: 7 Open Source Kubernetes Developer Tools to Follow in 2022](https://blog.devgenius.io/7-open-source-kubernetes-developer-tools-to-follow-in-2022-78a5e5dbd4e3)
- [dev.to: Top 200 Kubernetes Tools for DevOps Engineer Like You](https://dev.to/ajeetraina/top-200-kubernetes-tools-for-devops-engineer-like-you-3h7e)
- [devops.cisel.ch: Kubernetes operational tools you must TRY](https://devops.cisel.ch/kubernetes-operational-tools-you-must-try)
- [loft.sh: Kubernetes on Windows: 6 Life-Saving Tools & Tips](https://loft.sh/blog/kubernetes-on-windows-6-life-saving-tools-and-tips) Kubernetes is primarily a Linux technology, so it's fairly straightforward to run it on different Linux distros. But what about the developers working on Windows who need to run Kubernetes locally?
- [infoworld.com: 15 tools that make Kubernetes easier](https://www.infoworld.com/article/3488817/15-tools-that-make-kubernetes-easier.html) Take advantage of these Kubernetes companions to improve monitoring, command-line ops, multi-cluster management, and more.
- [youtube: 10 Must-Have Kubernetes Tools | DevOps Toolkit](https://www.youtube.com/watch?v=CB79eTFbR0w&feature=youtu.be&ab_channel=DevOpsToolkit)
- [medium.com/container-talks: 7 Tools To Make Kubernetes Management Easy](https://medium.com/container-talks/7-tools-to-make-kubernetes-management-easy-ba8238e6ce8d)
- [opensource.com: 5 open source tools for developing on the cloud](https://opensource.com/article/22/4/open-source-tools-developing-cloud) Here are a few IDEs that can improve your programming experience while using multiple cloud service providers.
- [devtron.ai: 7 Tools To Make Kubernetes Management Easy](https://devtron.ai/blog/7-tools-to-make-kubernetes-management-easy/)
- [developers.redhat.com: 8 open source Kubernetes security tools](https://developers.redhat.com/articles/2022/06/20/8-open-source-kubernetes-security-tools#)
- [blog.devops.dev: Tools to manage Kubernetes](https://blog.devops.dev/tools-to-manage-kubernetes-15b675f407d4) Kubernetes Command Line Tools
- [medium.com/@onai.rotich: 4 Tools that Make it Easy to manage your Kubernetes Cluster](https://medium.com/@onai.rotich/4-tools-that-make-it-easy-to-manage-your-kubernetes-cluster-be252847cd85)
- [virtualizationhowto.com: Kubernetes Best Kubernetes Management Tools in 2023](https://www.virtualizationhowto.com/2023/08/best-kubernetes-management-tools-in-2023)
- Favourite CLI tools for containers and Kubernetes:
    - dive - to explore Docker image layers
    - kubectx - to easily switch between k8s contexts
    - skaffold - to easily build, deploy, and dev apps on k8s
    - mirrord - to intercept traffic from k8s to the local app instance
- [coruzant.com/appdev: Kubernetes Management: Tools and Best Practices](https://coruzant.com/appdev/kubernetes-management-tools-and-best-practices/)
- [dev.to/cyclops-ui: Five tools to make your K8s experience more enjoyable](https://dev.to/cyclops-ui/five-tools-to-make-your-k8s-experience-more-enjoyable-5d85)

## K8s Tools

- [downloadkubernetes.com: Download Kubernetes 🌟](https://www.downloadkubernetes.com/) An easier way to get the binaries you need
- [ramitsurana/awesome-kubernetes: Tools 🌟](https://github.com/ramitsurana/awesome-kubernetes#configuration)
- [VMware octant](https://github.com/vmware/octant) A web-based, highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
    - [octant.dev](https://octant.dev/) Visualize your Kubernetes workloads. Octant is an open source developer-centric web interface for Kubernetes that lets you inspect a Kubernetes cluster and its applications.
- [KSS - Kubernetes pod status on steroid](https://github.com/chmouel/kss)
- [kubectl-tree](https://github.com/ahmetb/kubectl-tree) kubectl plugin to browse Kubernetes object hierarchies as a tree
- [The Golden Kubernetes Tooling and Helpers list](https://docs.google.com/spreadsheets/d/1WPHt0gsb7adVzY3eviMK2W8LejV0I5m_Zpc8tMzl_2w)
- [kubech (kubectl change)](https://github.com/aabouzaid/kubech) Set kubectl contexts/namespaces per shell/terminal to manage multi Kubernetes cluster at the same time.
- [Kubecle](https://github.com/rydogs/kubecle) is a web ui running locally that provides useful information about your kubernetes clusters. It is an alternative to Kubernetes Dashboard. Because it runs locally, you can access any kubernetes clusters you have access to
- [==Permission Manager== 🌟](https://github.com/sighupio/permission-manager) **is a project that brings sanity to Kubernetes RBAC and Users management, Web UI FTW. Permission Manager is an application that enables a super-easy and user-friendly RBAC management for Kubernetes. With Permission Manager, you can create users, assign namespaces/permissions, and distribute Kubeconfig YAML files via a nice & easy web UI.**
- [cloudnatively.com: Kubernetes client tools overview](https://www.cloudnatively.com/kubernetes-client-tools-overview/)
- [==kubectx + kubens: : Power tools for kubectl==🌟🌟](https://github.com/ahmetb/kubectx) Faster way to switch between clusters and namespaces in kubectl
- [go-kubectx](https://github.com/aca/go-kubectx) 5x-10x faster alternative to kubectx. Uses client-go.
- [kubevious: application centric Kubernetes UI 🌟](https://kubevious.io/) is open-source software that provides a usable and highly graphical interface for Kubernetes. Kubevious renders all configurations relevant to the application in one place.
    - [Kubevious SaaS: portal.kubevious.io](https://portal.kubevious.io/)
    - [Kubevious SaaS Beta is Live!](https://kubevious.io/blog/post/kubevious-saas-beta-launch)
    - [==kubevious.io: Built-in Validators==](https://kubevious.io/docs/built-in-validators/) Kubevious comes with 32 build-in validators to detect misconfigurations and violations to Kubernetes and Cloud-Native best practices.
    - [learnitguide.net: Kubevious - A Powerful Kubernetes Dashboard](https://www.learnitguide.net/2023/05/kubevious-powerful-kubernetes-dashboard.html)
- [Guard](https://github.com/appscode/guard) is a Kubernetes Webhook Authentication server. Using guard, you can log into your Kubernetes cluster using various auth providers. Guard also configures groups of authenticated user appropriately.
- [itnext.io: **arkade** by example — Kubernetes apps, the easy way 🌟](https://itnext.io/kubernetes-apps-the-easy-way-f06d9e5cad3c)
- [**Kubei**](https://github.com/Portshift/kubei) is a flexible Kubernetes runtime scanner, scanning images of worker and Kubernetes nodes providing accurate vulnerabilities assessment.
- [**Tubectl**: a kubectl alternative which adds a bit of magic to your everyday kubectl routines by reducing the complexity of working with contexts, namespaces and intelligent matching resources.](https://github.com/reconquest/tubekit)
- [**Kpt**: Packaging up your Kubernetes configuration with git and YAML since 2014 **(Google)**](https://opensource.googleblog.com/2020/03/kpt-packaging-up-your-kubernetes.html)
    - [kpt](https://googlecontainertools.github.io/kpt/)
    - [labs.meanpug.com: Kubernetes Kpt in The Wild: What it is and how to use it](https://labs.meanpug.com/kubernetes-kpt-in-the-wild/) Kubernetes Kpt is tooling by Google that facilitates a structured approach to defining, managing, and distributing kubernetes templates between teams and orgs.
- [kubernetes-common-services](https://github.com/ManagedKube/kubernetes-common-services) These services help make it easier to manage your applications environment in Kubernetes
- [**k8s-job-notify**](https://github.com/sukeesh/k8s-job-notify) Kubernetes Job/CronJob Notifier. This tool sends an alert to slack whenever there is a Kubernetes cronJob/Job failure/success.
- [**kube-opex-analytics** 🌟](https://github.com/rchakode/kube-opex-analytics) Kubernetes **Cost Allocation and Capacity Planning** Analytics Tool. Built-in hourly, daily, monthly reports - Prometheus exporter - Grafana dashboard.
- [**kubeletctl**](https://github.com/cyberark/kubeletctl) is a command line tool that implement kubelet's API. Part of kubelet's API is documented but most of it is not. This tool covers all the documented and undocumented APIs. The full list of all kubelet's API can be view through the tool or this [API table](https://github.com/cyberark/kubeletctl/blob/master/API_TABLE.md). What can it do ?:
    - Run any kubelet API call
    - Scan for nodes with opened kubelet API
    - Scan for containers with RCE
    - Run a command on all the available containers by kubelet at the same time
    - Get service account tokens from all available containers by kubelet
    - Nice printing :)
- [**K8bit** — the tiny Kubernetes dashboard 🌟](https://github.com/learnk8s/k8bit) K8bit is a tiny dashboard that is meant to demonstrate how to use the Kubernetes API to watch for changes.
    - [learnk8s.io/real-time-dashboard](https://learnk8s.io/real-time-dashboard)
- [**KUbernetes Test TooL (kuttl)** 🌟](https://kuttl.dev/)
    - [Youtube Webinar: The KUbernetes Test TooL (kuttl)](https://www.youtube.com/watch?v=Jh-viBv-D04)
- [Portfall: A desktop k8s port-forwarding portal for easy access to all your cluster UIs 🌟](https://github.com/rekon-oss/portfall)
- [k8s-dt-node-labeller](https://github.com/adaptant-labs/k8s-dt-node-labeller) is a Kubernetes controller for labelling a node with devicetree properties (devicetree is a data structure for describing hardware).
- [kubedev 🌟](https://relferreira.github.io/kubedev/) is a Kubernetes Dashboard that helps developers in their everyday usage
- [Kubectl SSH Proxy 🌟](https://github.com/little-angry-clouds/kubectl-ssh-proxy) Kubectl plugin to launch a ssh socks proxy and use it. This plugin aims to make your life easier when using kubectl a cluster that's behind a SSH bastion.
- [kubectl-images](https://github.com/chenjiandongx/kubectl-images) Show container images used in the cluster. Kubectl-images is a kubectl plugin that shows the container images used in the cluster. It first calls kubectl get pods to retrieve pods details and filters out the container image information of each pod then prints out the final result in a table view.
- [Access Pod Online using Podtnl](https://github.com/narendranathreddythota/podtnl) A Powerful CLI that makes your pod available to online without exposing a k8 service.
- [kiosk: Multi-Tenancy Extension For Kubernetes - Secure Cluster Sharing & Self-Service Namespace Provisioning 🌟](https://github.com/kiosk-sh/kiosk?utm_sq=gf3f25b1tk#why-kiosk) Kubernetes is designed as a single-tenant platform, which makes it hard for cluster admins to host multiple tenants in a single cluster. **Kiosk extends Kubernetes for multi-tenancy. The core idea is to use Kubernetes namespaces as isolated workspaces.**
- [asdf-kubectl](https://github.com/Banno/asdf-kubectl) kubectl plugin for [asdf version manager](https://asdf-vm.com/). asdf-vm is a CLI tool that can manage multiple language runtime versions on a per-project basis. It is like gvm, nvm, rbenv & pyenv (and more) all in one! Simply install your language’s plugin!
- [k8s Spot Rescheduler](https://github.com/pusher/k8s-spot-rescheduler) is a tool that tries to reduce load on a set of Kubernetes nodes. It was designed with the purpose of moving Pods scheduled on AWS on-demand instances to AWS spot instances to allow the on-demand instances to be safely scaled down (By the Cluster Autoscaler).
- [kube-spot-termination-notice-handler](https://github.com/kube-aws/kube-spot-termination-notice-handler) is a Kubernetes DaemonSet designed to gracefully delete pods 2 minutes before an EC2 Spot Instance is terminated.
- [Polaris 🌟](https://github.com/FairwindsOps/polaris) helps Kubernetes users avoid common mistakes when configuring their workloads. It runs a variety of checks to ensure that Kubernetes pods and controllers are configured using best practices, helping you avoid problems in the future.
    - [cncf.io: What is Polaris? Kubernetes open source configuration validation 🌟](https://www.cncf.io/blog/2021/07/01/what-is-fairwinds-polaris-kubernetes-open-source-configuration-validation/)
- [kmoncon](https://github.com/Stono/kconmon) Monitoring connectivity between your kubernetes nodes.
- [Tesoro](https://github.com/kapicorp/tesoro) [Kapitan](https://kapitan.dev/) Secrets Controller for Kubernetes. Tesoro is Kapitan Admission Controller Webhook. Tesoro allows you to seamleslsly apply Kapitan secret refs in compiled Kubernetes manifests. As it runs in the cluster, it will be able to reveal embedded kapitan secret refs in manifests when applied.
- [DAST operator](https://github.com/banzaicloud/dast-operator) Dynamic application security testing (DAST) is a Kubernetes operator that leverages OWASP ZAP to make automated basic web service security testing.
- [Teleskope](https://github.com/teleskopeView/teleskope_k8s) is a Kubernetes dashboard designed to give your devs and product managers an inside view of the cluster.
- [Introducing cdk8s+: Intent-driven APIs for Kubernetes objects](https://aws.amazon.com/es/blogs/containers/introducing-cdk8s-intent-driven-apis-for-kubernetes-objects/) Everyone hates yaml. Take that 75 lines of yaml and turn it into 45 lines of testable javascript with cdk8s+
    * https://github.com/awslabs/cdk8s/tree/master/packages/cdk8s-plus
- [KuUI (Kubernetes UI)](https://github.com/viveksinghggits/kuui) is a simple UI that can be used to manage the configmaps/secrets of your Kubernetes cluster.
- [Deprek8ion](https://github.com/swade1987/deprek8ion) is a set of rego policies to monitor Kubernetes APIs deprecations. It is designed to work with conftest.
- [Beetle](https://github.com/Clivern/Beetle) Kubernetes multi-cluster deployment automation service.
- [vault-controller](https://github.com/gobins/vault-controller) A K8s controller to manage Hashicorp Vault configuration using CRDs.
- [k8s-crash-informer](https://github.com/lnsp/k8s-crash-informer) is a Kubernetes controller that informs a Mattermost or Slack channel if an annotated deployment goes into crash loop.
- [Azure Arc enabled Kubernetes allows you to connect and manage external Kubernetes clusters in Azure](https://thorsten-hans.com/azure-arc-enabled-kubernetes-digital-ocean)
- [Kip, the Kubernetes Cloud Instance Provider](https://github.com/elotl/kip) Kip is a Virtual Kubelet provider that allows a Kubernetes cluster to transparently launch pods onto their own cloud instances. The kip pod is run on a cluster and will create a virtual Kubernetes node in the cluster.
- [Kubeletctl is a command line tool that implement kubelet's API 🌟](https://github.com/cyberark/kubeletctl)
- [k8s-node-label-monitor: Kubernetes Node Label Monitor provides a custom Kubernetes controller for monitoring and notifying changes in the label states of Kubernetes nodes (labels added, deleted, or updated), and can be run either node-local or cluster-wide](https://github.com/adaptant-labs/k8s-node-label-monitor)
- [medium: How to Validate Your Kubernetes Cluster With Sonobuoy 🌟](https://medium.com/better-programming/how-to-validate-your-kubernetes-cluster-with-sonobuoy-c91b282908fe) Run comprehensive conformance testing for your Kubernetes cluster
- [k42s is a full multinode Kubernetes Vagrant cluster with a real load balancer](https://github.com/p0bailey/k42s)
- [Pluto is a cli tool to help discover deprecated apiVersions in Kubernetes 🌟](https://github.com/FairwindsOps/pluto) Find Kubernetes resources that have been deprecated
- [Switchboard](https://github.com/borchero/switchboard) is a tool that manages DNS zones and their A/CNAME records for arbitrary backends. It runs as Kubernetes controller and watches for custom resources DNSZone and DNSRecord.
- [Kubernetes Deployment Builder 🌟🌟](https://static.brandonpotter.com/kubernetes/DeploymentBuilder.html)
- [ktx 🌟](https://github.com/heptiolabs/ktx) Managing kubeconfig files can become tedious when you have multiple clusters and contexts to switch between. ktx aims to reduce friction caused by switching between various configurations.
- [k8s-alert](https://github.com/kareem-elsayed/k8s-alerts) is a simple and lightweight alerting tool for Kubernetes.
- [Arktos](https://github.com/futurewei-cloud/arktos) is an open source cluster management system designed for large scale clouds. It is evolved from the open source Kubernetes v1.15 codebase with some fundamental improvements.
- [kube-exec 🌟](https://engineerd.github.io/kube-exec/introduction/) is a library similar to os/exec that allows you to run commands in a Kubernetes pod, as if that command was executed locally. It is inspired from go-dexec, which does the same thing, but for a Docker engine.
- [identity-server](https://github.com/kubeshield/identity-server) Identity Server implements a Kubernetes "whoami" service.
- [Kubermatic Kubernetes Platform 🌟](https://github.com/Kubermatic/Kubermatic) is in an open source project to centrally manage the global automation Kubernetes clusters across multicloud, on-prem and edge with unparalleled density and resilience.
- [The Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) is a project designed to be intentionally vulnerable cluster environment to learn and practice Kubernetes security.
- [kubefs](https://github.com/configurator/kubefs) lets you mount kubernetes's metadata object store as a file system
- [DAST Operator (Dynamic application security testing)](https://github.com/banzaicloud/dast-operator) is a Kubernetes operator that leverages OWASP ZAP to make automated basic web service security testing
- [KuUI (Kubernetes UI)](https://github.com/viveksinghggits/kuui) is a simple UI that can be used to manage the configmaps/secrets of your Kubernetes cluster.
- [pangolin 🌟](https://github.com/dpeckett/pangolin) is an enhanced Horizontal Pod Autoscaler for Kubernetes.
- [kubectl-isolate](https://github.com/yteraoka/kubectl-isolate) is a kubectl plugin to isolate a Pod from the Kubernetes Service
- [k8s-diagrams 🌟](https://github.com/cloudogu/k8s-diagrams) is a collection of diagrams explaining kubernetes, extracted from our trainings, articles and talks (k8s sec, k8s intro).
- [kconmon](https://github.com/Stono/kconmon) is a Kubernetes node connectivity monitoring tool
- [helm-docs](https://github.com/norwoodj/helm-docs) is a tool for automatically generating markdown documentation for helm charts.
- [Kubernetes Active Passive Applications](https://github.com/amelbakry/kubernetes-active-passive) is an ingenious script that combines StatefulSets and readiness probes to achieve an active-passive configuration for your Pods/apps.
- [Agorakube](https://github.com/ilkilab/agorakube) is a Certified Kubernetes Distribution that provides an enterprise grade solution following best practices to manage a conformant Kubernetes cluster for on-premise and public cloud providers.
- [dynamic-pv-scaler](https://github.com/opstree/dynamic-pv-scaler) is a golang based Kubernetes application which has been created to overcome the scaling issue of Persistent Volume in Kubernetes. This can scale the Persistent Volume on the basis of threshold which you have set.
- [Sinker](https://github.com/plexsystems/sinker) Imagesync enables the syncing of container images from one container registry to another. This is useful in cases where you need to mirror images that exist in a public container registry, to a private one.
- [Cluster Turndown](https://github.com/kubecost/cluster-turndown) is an automated scaledown and scaleup of a Kubernetes cluster's backing nodes based on a custom schedule and turndown criteria.
- [Kubernetes Node Label Monitor](https://github.com/adaptant-labs/k8s-node-label-monitor) is a Kubernetes controller for monitoring and notifying about changes to Node label states
- [kubeinit 🌟](https://github.com/Kubeinit/kubeinit) KubeInit provides Ansible playbooks and roles for the deployment and configuration of multiple Kubernetes distributions.
- [kubergui: Kubernetes Deployment Builder🌟](https://github.com/BrandonPotter/kubergui) quickly builds out a basic Kubernetes Deployment and Kubernetes Service YAML. Kubernetes GUI YAML generators for simple but typo-prone tasks.
- [fubectl](https://github.com/kubermatic/fubectl) is a tool that reduces repetitive interactions with kubectl
- [Authelia 🌟](https://github.com/authelia/authelia) is a Single Sign-On and Multi-Factor portal for web apps that can be installed in Kubernetes and can integrate with your ingress controller
- [k8sdeploy](https://github.com/pyang55/k8sdeploy) is a go based tool, written with the goal of creating a cli that utilizes helm and kubernetes client libraries to deploy to multiple namespaces at once.
- [kubewatch 🌟🌟](https://hub.docker.com/r/bitnami/kubewatch)
    - [Espiando a tu kubernetes con kubewatch](https://bluetab.net/wp-content/uploads/2020/09/Blog.html)
- [node-policy-webhook](https://github.com/softonic/node-policy-webhook) is a Kubernetes webhook designed to help you handle tolerations, nodeSelector and nodeAffinity.
- [kubeonoff](https://github.com/GambitResearch/kubeonoff) is a simple web UI for managing Kubernetes deployments.
- [ipvs-node-controller](https://github.com/kakao/ipvs-node-controller) is the kubernetes controller that solves External-IP (Load Balancer IP) issue with IPVS proxy mode.
- [kubeonoff](https://github.com/GambitResearch/kubeonoff) A simple web UI for managing Kubernetes deployments. Kubeonoff is a small web UI that allows to quickly stop/start/restart pods. Basically it's for non-developers to manage k8s objects per namespace.
- [Maistra 🌟](https://maistra.io/) is an opinionated distribution of Istio designed to work with Openshift. It combines Kiali, Jaeger, and Prometheus into a platform managed according to the OperatorHub lifecycle.
- [custom-pod-autoscaler](https://github.com/jthomperoo/custom-pod-autoscaler) A Custom Pod Autoscaler is a Kubernetes autoscaler that is customised and user created. The Custom Pod Autoscaler framework allows easier and faster development of Kubernetes autoscalers.
- [Kubevol 🌟](https://github.com/bmaynard/kubevol) allows you to audit all your Kubernetes pods for an attached volume or see all the volumes attached to each pod by a specific type (eg: ConfigMap, Secret).
- [kubectl-fuzzy 🌟](https://github.com/d-kuro/kubectl-fuzzy) uses fzf(1)-like fuzzy-finder to do partial or fuzzy search of Kubernetes resources. Instead of specifying full resource names to kubectl commands, you can choose them from an interactive list that you can filter by typing a few characters.
- [Setec 🌟](https://github.com/anthonysterling/setec) Setec (pronounced see-tek) is a utility tool that encrypts and decrypts secrets that are managed by Bitnami's Sealed Secrets.
- [==Kompose (Kubernetes + Compose)== 🌟](https://github.com/kubernetes/kompose) kompose is a tool to help users who are familiar with docker-compose move to Kubernetes. kompose takes a Docker Compose file and translates it into Kubernetes resources. kompose is a convenience tool to go from local Docker development to managing your application with Kubernetes. Transformation of the Docker Compose format to Kubernetes resources manifest may not be exact, but it helps tremendously when first deploying an application on Kubernetes.
    - [hackernoon.com: How to Generate Kubernetes Manifests With a Single Command (kompose)](https://hackernoon.com/how-to-generate-kubernetes-manifests-with-a-single-command)
- [kalm.dev 🌟](https://kalm.dev/) Easily deploy and manage applications on Kubernetes. Get what you want out of Kubernetes without having to write and maintain a ton of custom tooling. Deploy apps, handle requests, and hook up CI/CD, all through an intuitive web interface.
- [Kev](https://github.com/appvia/kev) Develop Kubernetes apps iteratively with Docker-Compose. Kev helps developers port and iterate Docker Compose apps onto Kubernetes. It understands the Docker Compose application topology and prepares it for deployment in (multiple) target environments, with minimal user input. We leverage the Docker Compose specification and allow for target-specific configurations to be applied to each component of the application stack, simply.
- [Synator Kubernetes Secret and ConfigMap synchronizer 🌟](https://github.com/TheYkk/synator) Synator synchronize your Secrets and ConfigMaps with your desired namespaces
- [kubes 🌟](https://github.com/boltops-tools/kubes) is a Kubernetes Deployment Tool. It builds the docker image, creates the Kubernetes YAML, and runs kubectl apply.
- [Kubernetes DaemonSet that enables a direct shell on each Node using SSH to localhost](https://gist.github.com/xandout/8d24558c75c53f3cb8bf0a97ec25fcfc) Learn how you can use a DaemonSet to expose an SSH shell on each node of your cluster (even if you don't have SSH installed). I run several K8S cluster on EKS and by default do not setup inbound SSH to the nodes. Sometimes I need to get into each node to check things or run a one-off tool. Rather than update my terraform, rebuild the launch templates and redeploy brand new nodes, I decided to use kubernetes to access each node directly.
- [NS Killer](https://github.com/germainlefebvre4/ns-killer) A Kubernetes project to kill all namespace living over X times. Quite useful when auto-generated development environments on the fly and give them a lifecycle out-of-the-box from Kubernetes or even Helm. You might find it useful if auto-generate development environments on the fly and want to remove old ones on a schedule.
- [kubeswitch: Kubernetes Version Switcher 🌟](https://github.com/steamhaus/kubeswitch) Easily switch kubectl binary versions.
- [Kubeswitch (for operators) 🌟](https://github.com/danielfoehrKn/kubeswitch) The kubectx for operators. kubeswitch (lazy: switch) takes Kubeconfig context switching to the next level, catering to operators of large scale Kubernetes installations. Designed as a drop-in replacement for kubectx.
- [kubectl build (formerly known as kubectl-kaniko)](https://github.com/kvaps/kubectl-build) Kubectl build mimics the kaniko executor, but performs building on your Kubernetes cluster side. This allows you to simply build your local dockerfiles remotely without leaving your cozy environment.
- [Kubei 🌟](https://github.com/Portshift/Kubei) is a vulnerabilities scanning tool that allows users to get an accurate and immediate risk assessment of their kubernetes clusters. Kubei scans all images used in a Kubernetes cluster including images of application pods and system pods
- [Shell-operator](https://github.com/flant/shell-operator) is a tool for running event-driven scripts in a Kubernetes cluster. Shell-operator provides an integration layer between Kubernetes cluster events and shell scripts.
- [sinker is a tool to sync images from one container registry to another](https://github.com/plexsystems/sinker)  This is useful in cases when you rely on images that exist in a public container registry, but need to pull from a private registry.
- [ecrcp](https://github.com/bit-cloner/ecrcp) aims to mimic cp command in Linux systems as closely as possible in its implementation. Consider ecrcp to be the cp equivalent to copy container images from docker hub to ECR.
- [Checkov 🌟](https://github.com/bridgecrewio/checkov/) is a static code analysis tool for infrastructure-as-code. It scans cloud infrastructure provisioned using Terraform, Cloudformation, Kubernetes, Serverless or ARM Templates and detects security and compliance misconfigurations.
- [Cluster Cloner 🌟](https://github.com/doitintl/clustercloner/) Reads the Kubernetes clusters in one location (optionally filtering by labels) and clones them into another (or just outputs JSON as a dry run), to/from AWS, GCP, and Azure.
- [kubectl-eksporter 🌟](https://github.com/Kyrremann/kubectl-eksporter) A simple Ruby-script to export k8s resources, and removes a pre-defined set of fields for later import.
- [kubectl-neat 🌟](https://github.com/itaysk/kubectl-neat) Remove clutter from Kubernetes manifests to make them more readable.
- [medium: 4 Simple Kubernetes Terminal Customizations to Boost Your Productivity](https://medium.com/better-programming/4-simple-kubernetes-terminal-customizations-to-boost-your-productivity-deda60a19924)
- [Move2Kube 🌟](https://github.com/konveyor/move2kube) Move2Kube is a command-line tool that accelerates the process of re-platforming to Kubernetes/Openshift. It does so by analysing the environment and source artifacts, and asking guidance from the user when required. This tool that can help users migrate from Cloud Foundry and Docker Swarm to Kubernetes. https://move2kube.konveyor.io
- [skopeo 🌟](https://github.com/containers/skopeo) Use skopeo to copy images between registries
- [junit5-kubernetes](https://github.com/JeanBaptisteWATENBERG/junit5-kubernetes) aims at using a kubernetes pod directly form your junit5 test classes.
- [mbuffett.com: Replacing ngrok with ktunnel](https://mbuffett.com/posts/ktunnel-ngrok-replace/)
- [seaworthy: A CLI to verify #Kubernetes resource health !! 🌟](https://github.com/cakehappens/seaworthy) Post-apply check to verify your K8s resources are Seaworthy
- [kVDI](https://github.com/tinyzimmer/kvdi) A Kubernetes-native Virtual Desktop Infrastructure.
- [kcg 🌟](https://github.com/bit-cloner/kcg) is a command line tool that lets you create kubeconfig files. The user can interactively choose a namespace and service account and generate a config file with token authentication that has same RBAC permissions assigned to chosen service account.
- [Compass 🌟](https://github.com/winfordlin/Compass) Quickly Pinpoint Errors in your Kubernetes Deployment.
- [kubernetes-dashboard-iam-proxy](https://github.com/Nitro/kubernetes-dashboard-iam-proxy) An in-browser version of aws eks get-token to enable cluster authentication using IAM for the Kubernetes dashboard.
- [Gitkube 🌟](https://github.com/hasura/gitkube) is a tool for building and deploying Docker images on Kubernetes using git push. After a simple initial setup, users can simply keep git push-ing their repos to build and deploy to Kubernetes automatically.
- [vesion-checker](https://github.com/jetstack/version-checker) is a Kubernetes utility for observing the current versions of images running in the cluster, as well as the latest available upstream. These checks get exposed as Prometheus metrics to be viewed on a dashboard, or soft alert cluster operators.
- [Descheduler for Kubernetes 🌟](https://github.com/kubernetes-sigs/descheduler) -> [wecloudpro.com: Balance your Kubernetes cluster](https://www.wecloudpro.com/2020/11/01/Balance-your-kubernetes-cluster.html)
- [kubediff 🌟](https://github.com/weaveworks/kubediff) is a tool for Kubernetes to show you the differences between your running configuration and your version controlled configuration.
- [awslabs/karpenter](https://github.com/awslabs/karpenter) Karpenter is a metrics-driven autoscaler built for Kubernetes and can run in any Kubernetes cluster anywhere. It's performant, extensible, and can autoscale anything that implements the Kubernetes scale subresource.
- [ekglue - Envoy/Kubernetes glue](https://github.com/jrockway/ekglue) ekglue is a projects that facilitates connecting Kubernetes and Envoy, allowing Envoy to read Kubernetes services and endpoints as clusters (via CDS) and endpoints (via EDS).
- [salesforce/Craft](https://github.com/salesforce/craft) CRAFT helps you to create Kubernetes Operators in a robust and generic way for any resource, letting developers focus on CRUD operations of resource management in a Dockerfile.
- [hyscale 🌟](https://github.com/hyscale/hyscale) HyScale takes a declarative definition of your service config and it generates Dockerfile, Container Image, Kubernetes Manifests (YAMLs) and deploys to any Kubernetes Cluster.
- [kubectl-reap is a kubectl plugin that deletes unused Kubernetes resources 🌟](https://github.com/micnncim/kubectl-reap)
- [KubeLinter 🌟](https://github.com/stackrox/kube-linter) is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
- [KRD: Kubernetes Reference Deployment](https://github.com/electrocucaracha/krd) krd offers a reference for deploying a Kubernetes cluster. Its ansible playbooks allow to provision a deployment on Bare-metal or Virtual Machines
- [kubeshell](https://github.com/roubles/kubeshell) is a command line tool to interactively shell in to (and out of) kubernetes pods.
- [k8s-harness 🌟](https://github.com/carlosonunez/k8s-harness) lets you create a disposable Kubernetes cluster with **vagrant and Ansible to test your app in a prod-like environment**.
- [Secret backup operator](https://github.com/geritol/secret-backup-operator) is an operator designed to backup secrets on a Kubernetes cluster. Backup happens when secrets are modified.
- [DevNation: 10 awesome kubernetes tools every user should know](https://bit.ly/kube-tools-1)
    - [developers.redhat.com: 10 awesome Kubernetes tools every user should know | DevNation Tech Talk (video)](https://developers.redhat.com/devnation/tech-talks/10-kubernetes-tools)
- [HyScale 🌟](https://github.com/hyscale/hyscale) takes a declarative definition of your service config and it generates Dockerfile, Container Image, Kubernetes Manifests (YAMLs) and deploys to any Kubernetes Cluster
- [kube-fledged](https://github.com/senthilrch/kube-fledged) is a kubernetes add-on for creating and managing a cache of container images directly on the worker nodes of a kubernetes cluster. It allows a user to define a list of images and onto which worker nodes those images should be cached (i.e. pre-pulled). As a result, application pods start almost instantly, since the images need not be pulled from the registry.
- [Tagger](https://github.com/ricardomaraschini/tagger) keeps references to externally hosted Docker images internally in a Kubernetes cluster by mapping their tags (such as latest) into their references by hash
- [helm-ecr 🌟](https://github.com/vetyy/helm-ecr) is a Helm plugin that supports installing Charts from AWS ECR.
- [PipeCD](https://github.com/pipe-cd/pipe) is a continuous delivery system for declarative Kubernetes, Serverless, and Infrastructure applications.
- [kubecolor 🌟](https://github.com/dty1er/kubecolor) colorises your kubectl output
    - [blog.devgenius.io: K8s — Kubecolor Introduction](https://blog.devgenius.io/k8s-kubecolor-introduction-3d650effc36f)
- [kubectl-sudo](https://github.com/postfinance/kubectl-sudo) This plugin allows users to run kubernetes commands with the security privileges of another user.
- [kfilt](https://github.com/ryane/kfilt) is a tool that lets you filter specific resources from a stream of Kubernetes YAML manifests. It can read manifests from a file, URL, or from stdin.
- [k8s-mirror: Creates a local mirror of a kubernetes cluster in a docker container to support offline reviewing 🌟](https://github.com/darkbitio/k8s-mirror)
- [kube-secret-syncer 🌟](https://github.com/contentful-labs/kube-secret-syncer) is a Kubernetes operator developed using the Kubebuilder framework that keeps the values of Kubernetes Secrets synchronised to secrets in AWS Secrets Manager.
    - [contentful.com: Open-sourcing kube-secret-syncer: A Kubernetes operator to sync secrets from AWS Secrets Manager](https://www.contentful.com/blog/2020/10/20/open-source-kube-secret-syncer/) Kube-secret-syncer is a Kubernetes operator developed using the Kubebuilder framework that keeps the values of Kubernetes Secrets synchronised to secrets in AWS Secrets Manager.
- [kapp 🌟](https://carvel.dev/kapp) is a CLI that calculates changes between your configuration and live cluster state and applies changes you approve.
    - [thecloudblog.net: Managing Applications in Kubernetes with the Carvel Kapp Controller](https://thecloudblog.net/post/managing-applications-in-kubernetes-with-the-carvel-kapp-controller/) kapp enables users to group a set of resources (resources with the same label) as an application. In this tutorial, you will learn how to deploy a front-end and backend app with Redis as a single unit with kapp.
- [garden.io](https://garden.io/) Break down the barriers between development, testing, and CI. Use the same workflows and production-like Kubernetes environments at every step of the process
    - [thenewstack.io: Garden: The Configure-Once Kubernetes Platform for Seamless Dev/Prod Integration](https://thenewstack.io/garden-the-configure-once-kubernetes-platform-for-seamless-dev-prod-integration/)
- [pvc-autoresizer](https://github.com/topolvm/pvc-autoresizer) resizes PersistentVolumeClaims (PVCs) when the free amount of storage is below the threshold. It queries the volume usage metrics from Prometheus that collects metrics from kubelet.
    - [blog.kintone.io: Introducing pvc-autoresizer](https://blog.kintone.io/entry/pvc-autoresizer)
- [sKan](https://github.com/alcideio/skan) is a tailor made Kubernetes configuration files and resources scanner that enables developers and devops team members to check whether their work is compliant with security & ops best practices
- [Kubernetes Node Auto Labeller](https://github.com/adaptant-labs/k8s-auto-labeller)
- [Kube_query](https://github.com/Isan-Rivkin/kube_query) Use kubectl but on all of the available k8s clusters available in the kubeconfig file. Currently will query only AWS EKS clusters.
- [kubernetes-event-exporter 🌟](https://github.com/opsgenie/kubernetes-event-exporter) This tool allows exporting the often missed Kubernetes events to various outputs so that they can be used for observability or alerting purposes. You won't believe what you are missing.
- [==Kubeconform== 🌟](https://github.com/yannh/kubeconform) **is a Kubernetes manifests validation tool. Build it into your CI to validate your Kubernetes configuration using the schemas from kubernetes-json-schema.** Similar to Kubeval, but with the following improvements:
    - High performance
    - Remote or local schemas locations
    - Up-to-date schemas for all recent versions of Kubernetes
- [Kubernetes Janitor](https://codeberg.org/hjacobs/kube-janitor) cleans up (deletes) Kubernetes resources on a configured TTL (time to live) or a configured expiry date (absolute timestamp).
- [kube-batch](https://github.com/kubernetes-sigs/kube-batch) is a batch scheduler for Kubernetes, providing mechanisms for applications which would like to run batch jobs leveraging Kubernetes. A batch scheduler of kubernetes for high performance workload, e.g. AI/ML, BigData, HPC
- [slipway: A Kubernetes controller to automate gitops provisioning](https://github.com/slipway-gitops/slipway)
- [github.com: dnsconfig-injector - Mutating Admission Webhook for dnsconfig pod injection](https://github.com/karampok/dnsconfig-injector)
- [kubectl-view-webhook 🌟](https://github.com/Trendyol/kubectl-view-webhook) Visualize your webhook configurations in Kubernetes.
- [ContainerSSH: Launch containers on demand 🌟🌟](https://containerssh.io) ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects. Authentication and container configuration are dynamic using webhooks, no system users required.
- [reconshell.com: Kubei – Kubernetes Runtime Vulnerabilities Scanner 🌟](https://reconshell.com/kubei-kubernetes-runtime-vulnerabilities-scanner/)
- [Lockbox: Offline encryption of Kubernetes Secrets](https://github.com/cloudflare/lockbox) Lockbox is a secure way to store Kubernetes Secrets offline. Secrets are asymmetrically encrypted, and can only be decrypted by the Lockbox Kubernetes controller. A companion CLI tool, locket, makes encrypting secrets a one-step process.
- [openshift: Introducing kube-burner, A tool to Burn Down Kubernetes and OpenShift 🌟](https://www.openshift.com/blog/introducing-kube-burner-a-tool-to-burn-down-kubernetes-and-openshift) Kube-burner is a tool designed to stress different OpenShift components basically by coordinating the creation and deletion of k8s resources. Along this blog series we’ll talk about how to use it in OpenShift 4.
    - [github.com/cloud-bulldozer/kube-burner](https://github.com/cloud-bulldozer/kube-burner) Kube-burner is a tool aimed at stressing Kubernetes clusters by creating or deleting a high quantity of objects
- [kube-ebpf-exporter 🌟](https://github.com/ahas-sigs/kube-ebpf-exporter) Prometheus exporter for custom eBPF metrics.
- [qontract](https://github.com/app-sre/qontract-server) qontract (Queryable cONTRACT) is a collection of tools used to SREs to expose available managed services to application developer teams.
- [sheaf](https://github.com/bryanl/sheaf) Manages bundles of Kubernetes components. sheaf is a tool that can create a bundle of Kubernetes components. It can generate an archive from the bundle that can be distributed for use in Kubernetes clusters. The initial idea was inspired by CNAB. It answers the question: how can I distribute Kubernetes manifests with their associated images?
- [cnab.io: CNABs facilitate the bundling, installing and managing of container-native apps — and their coupled services](https://cnab.io/)
- [tremolosecurity.com: Secure Access to Kubernetes From Your Pipeline](https://www.tremolosecurity.com/post/secure-access-to-kubernetes-from-your-pipeline)
- [openpitrix 🌟](https://github.com/openpitrix/openpitrix) Application Management Platform on Multi-Cloud Environment. OpenPitrix is a web-based open-source system to package, deploy and manage different types of applications including Kubernetes application, microservice application and serverless applications into multiple cloud environment such as AWS, Azure, Kubernetes, QingCloud, OpenStack, VMWare etc.
- [kube-burner 🌟](https://github.com/cloud-bulldozer/kube-burner) Kube-burner is a tool aimed at stressing kubernetes clusters.
- [gimletd - the GitOps release manager](https://github.com/gimlet-io/gimletd) GimletD acts as a release manager and detaches the release workflow from CI. By doing so, it unlocks the possibility of advanced release logics and flexibility to refactor workflows.
- [kubectl skew 🌟](https://github.com/dty1er/kubectl-skew) A simple kubectl plugin to show if your kubernetes/kubectl version is "skewed". In kubernetes, version skew policy is a bit confusing, especially for beginners. However, it is important to make sure you are always following the policy because using unsupported cluster/kubectl is problematic and even dangerous.
- [github.com/cloudflare/lockbox](https://github.com/cloudflare/lockbox) Offline encryption of Kubernetes Secrets. Lockbox is a secure way to store Kubernetes Secrets offline. Secrets are asymmetrically encrypted, and can only be decrypted by the Lockbox Kubernetes controller. A companion CLI tool, locket, makes encrypting secrets a one-step process.
- [Suspicious pods 🌟](https://github.com/edrevo/suspicious-pods) Prints a list of k8s pods that might not be working correctly
- [Armada](https://github.com/G-Research/armada) A multi-cluster batch queuing system for high-throughput workloads on Kubernetes. Armada is an application to achieve high throughput of run-to-completion jobs on multiple Kubernetes clusters. It stores queues for users/projects with pod specifications and creates these pods once there is available resource in one of the connected Kubernetes clusters.
- [Ko: Easy Go Containers 🌟](https://github.com/google/ko) Build and deploy Go applications on Kubernetes
- [kubestr 🌟](https://kubestr.io/) Explore your Kubernetes storage options. Kubestr is a collection of tools to discover, validate and evaluate your kubernetes storage options.
- [KubeEye: An Automatic Diagnostic Tool that Provides a Holistic View of Your Kubernetes Cluster 🌟](https://kubesphere.io/blogs/kubeeye-automatic-cluster-diagnostic-tool/)
- [k8gb 🌟](https://github.com/k8gb-io/k8gb) A cloud native Kubernetes Global Balancer [k8gb.io](https://www.k8gb.io/)
- [k8s-image-swapper 🌟](https://github.com/estahn/k8s-image-swapper) Mirror images into your own registry and swap image references automatically. [estahn.github.io/k8s-image-swapper](https://estahn.github.io/k8s-image-swapper/)
- [RBACSync 🌟](https://github.com/cruise-automation/rbacsync) Automatically sync groups into Kubernetes RBAC. RBACSync provides a Kubernetes controller to synchronize RoleBindings and ClusterRoleBindings, used in Kubernetes RBAC, from group membership sources using consolidated configuration objects.
- [Saffire](https://github.com/FairwindsOps/saffire) a controller to override image sources in the event that an image cannot be pulled. The intent of saffire is to provide operators with a method of automatically switching image repositories when imagePullErrors occur.
- [Cluster API Provider for Managed Bare Metal Hardware](https://github.com/metal3-io/cluster-api-provider-metal3) This repository contains a Machine actuator implementation for the Kubernetes Cluster API for managing bare metal hardware - [metal3.io: Bare metal host provisioning for kubernetes](http://metal3.io/)
- [enterprisersproject.com: Kubernetes: 6 open source tools to put your cluster to the test](https://enterprisersproject.com/article/2021/5/kubernetes-6-open-source-tools-to-test-clusters) The Kubernetes ecosystem includes an ever-growing number of tools and services you can plug in: Let’s look at six useful tools for putting your Kubernetes cluster and applications to the test.
- [kubectl-node-restart 🌟](https://github.com/MnrGreg/kubectl-node-restart) Krew plugin to restart Kubernetes Nodes sequentially and gracefully
- [k8s-platform-lcm: Kubernetes platform lifecycle management 🌟](https://github.com/arminc/k8s-platform-lcm) A faster and easier way to manage the lifecycle of applications and tools, running and living around your Kubernetes platform. Kubernetes platform lifecycle management helps you keep track of all your software and tools that are used or running in and around your Kubernetes platform.
- [Nebula](https://github.com/slackhq/nebula) A scalable overlay networking tool with a focus on performance, simplicity and security. It lets you seamlessly connect computers anywhere in the world.
- [kube-bench](https://github.com/aquasecurity/kube-bench) Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
- [kube-bench-exporter](https://github.com/yashvardhan-kukreja/kube-bench-exporter) Helps you to export your kube-bench reports to multiple targets like Amazon S3 buckets with ease.
- [Karmada](https://github.com/karmada-io/karmada) Karmada (Kubernetes Armada) is a Kubernetes management system that enables you to run your cloud-native applications across multiple Kubernetes clusters and clouds, with no changes to your applications. By speaking Kubernetes-native APIs and providing advanced scheduling capabilities, Karmada enables truly open, multi-cloud Kubernetes. - https://karmada.io/
- [kube-secrets-init](https://github.com/doitintl/kube-secrets-init) Kubernetes mutating webhook for `secrets-init` injection
- [liqo: Enable dynamic and seamless Kubernetes multi-cluster topologies](https://github.com/liqotech/liqo) Building your endless Kubernetes ocean. Enable dynamic and seamless Kubernetes multi-cluster topologies. Liqo is a platform to enable dynamic and decentralized resource sharing across Kubernetes clusters, either on-prem or managed. Liqo allows to run pods on a remote cluster seamlessly and without any modification of Kubernetes and the applications. With Liqo it is possible to extend the control plane of a Kubernetes cluster across the cluster's boundaries, making multi-cluster native and transparent: collapse an entire remote cluster to a virtual local node, by allowing workloads offloading and resource management compliant with the standard Kubernetes approach.
- [redhat-certification: chart-verifier: Rules based tool to certify Helm charts 🌟](https://github.com/redhat-certification/chart-verifier)
- [helm-changelog: Create changelogs for Helm Charts, based on git history](https://github.com/mogensen/helm-changelog)
- [ingressbuilder.jetstack.io 🌟🌟](https://ingressbuilder.jetstack.io) Ingress Builder allows users to select any annotation from the list of available controllers, to add to the ingress manifest.
- [Jetstack Secure Agent 🌟🌟](https://github.com/jetstack/preflight) **Automatically perform Kubernetes cluster configuration checks using Open Policy Agent (OPA)**
- [Replicated Troubleshoot 🌟](https://github.com/replicatedhq/troubleshoot) Troubleshoot is a framework for collecting, redacting, and analyzing highly customizable diagnostic information about a Kubernetes cluster.
- [outdated.sh 🌟](https://outdated.sh/) A kubectl plugin to show out-of-date images running in a cluster.
- [kubestriker 🌟](https://github.com/vchinnipilli/kubestriker) A Blazing fast Security Auditing tool for Kubernetes. Kubestriker is a platform-agnostic tool designed to tackle Kuberenetes cluster security issues due to misconfigurations and will help strengthen the overall IT infrastructure of any organisation.
- [KubeEye 🌟](https://github.com/kubesphere/kubeeye) KubeEye aims to find various problems on Kubernetes, such as application misconfiguration, unhealthy cluster components and node problems.
- [Analyze Kubernetes Audit logs using Falco 🌟](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster) Detect intrusions that happened in your Kubernetes cluster through audit logs using Falco
- [KubeHelper](https://github.com/kubehelper/kubehelper) KubeHelper - simplifies many daily Kubernetes cluster tasks through a web interface. Search, analysis, run commands, cron jobs, reports, filters, git synchronization and many more.
- [kubewebhook](https://github.com/slok/kubewebhook) Go framework to create Kubernetes mutating and validating webhooks
- [kaDalu](https://github.com/kadalu/kadalu) A lightweight Persistent storage solution for Kubernetes / OpenShift using GlusterFS in background. Kadalu is a project which started as an idea to make glusterfs's deployment and management simpler in kubernetes
- [forklift.konveyor.io 🌟](https://forklift.konveyor.io/) A tool that accelerates the process of re-hosting / re-platforming virtual machines to Kubernetes and KubeVirt. It does so by mapping resources (network and storage), creating equivalent resources int he target, and converting disk images.
    - [opensource.com: Migrate virtual machines to Kubernetes with this new tool - forklift 🌟](https://opensource.com/article/21/6/migrate-vms-kubernetes-forklift) Transition your virtualized workloads to Kubernetes with Forklift.
    - [konveyor 🌟](https://www.konveyor.io/) is an open source project that helps transition existing workloads (development, test, and production) to Kubernetes. Its tools include Crane, to move containers from one Kubernetes platform to another; Move2Kube, to bring workloads from Cloud Foundry to Kubernetes; and Tackle, to analyze Java applications to modernize them by making them more standard and portable for the runtimes available in containerized platforms like Kubernetes.
- [go-containerregistry 🌟](https://github.com/google/go-containerregistry) Go library and CLIs for working with container registries
- [kubebox](https://github.com/astefanutti/kubebox) Terminal and Web console for Kubernetes
- [skooner - Kubernetes Dashboard](https://github.com/skooner-k8s/skooner) Simple Kubernetes realtime dashboard and management
- [Polaris: Best Practices for Kubernetes Workload Configuration 🌟](https://github.com/FairwindsOps/polaris) Validation of best practices in your Kubernetes clusters - [fairwinds.com: What is Fairwinds’ Polaris? Kubernetes Open Source Configuration Validation](https://www.fairwinds.com/blog/fairwinds-polaris-kubernetes-open-source-configuration-validation)
- [Krane 🌟](https://github.com/appvia/krane) is a Kubernetes RBAC static analysis tool. It identifies potential security risks in K8s RBAC design and makes suggestions on how to mitigate them. Krane dashboard presents current RBAC security posture and lets you navigate through its definition.
- [KTail: Kubernetes log viewer 🌟](https://www.ktail.de/) KTail allows you to tail multiple pods in one view. It automatically detects updates and attaches to new pods. Configurable highlighters show how often regular expressions matched and let you quickly navigate in the results.
- [Manifesto 🌟](https://gitlab.com/jackatbancast/manifesto) allows you to create an application structure to facilitate easy deployment to kubernetes. Jsonnet is used to create the underlying application structure, manifesto manipulates this structure to produce manifests.
- [==SigNoz: Open source Application Performance Monitoring (APM) & Observability tool== 🌟](https://github.com/SigNoz/signoz) SigNoz helps developers monitor their applications & troubleshoot problems, an open-source alternative to DataDog, NewRelic, etc.
    - [golang.ch: A Golang-based open-source alternative to DataDog, New Relic, etc](https://golang.ch/a-golang-based-open-source-alternative-to-datadog-new-relic-etc/)
- [port-map-operator](https://github.com/MOZGIII/port-map-operator) LoadBalancer Service type implementation for home clusters via Port Control Protocol.
- [Raspbernetes - Kubernetes Cluster: k8s-gitops](https://github.com/xUnholy/k8s-gitops) Kubernetes cluster managed by GitOps - Git as a single source of truth, automated pipelines, declarative everything, next-generation DevOps. This repo is a declarative implementation of a Kubernetes cluster. It's using the GitOps Toolkit known as Fluxv2. The goal is to demonstrates how to implement enterprise-grade security, observability, and overall cluster config management using GitOps in a Kubernetes cluster.
- [Kpexec](https://github.com/ssup2/kpexec) kpexec is a kubernetes cli that runs commands in a container with high privileges.
- [OpenShiftKubeAudit](https://github.com/AICoE/OpenShiftKubeAudit) An auditing program to detect incompatibilities in Kubernetes manifests brought over to OpenShift. This auditing tool currently only supports Kubernetes manifests, but we plan to expand it to include Helm charts and Go code, as well. The tool is in very early stages, but is looking for community input to help add use cases.
- [Kubernetes Kpt in The Wild: What it is and how to use it 🌟](https://labs.meanpug.com/kubernetes-kpt-in-the-wild) Kubernetes Kpt is tooling by Google that facilitates a structured approach to defining, managing, and distributing kubernetes templates between teams and orgs.
- [RollingUpgrade](https://github.com/keikoproj/upgrade-manager) Reliable, extensible rolling-upgrades of Autoscaling groups in Kubernetes
- [Kerbi 🌟](https://github.com/nmachine-io/kerbi) Kerbi (Kubernetes Emdedded Ruby Interpolator) is yet another templating engine for generating Kubernetes resource manifests. It enables multi-strategy, multi-source templating, giving you the freedom to design highly specialized templating pipelines.
- [Kourier](https://github.com/knative-sandbox/net-kourier) Purpose-built Knative Ingress implementation using just Envoy with no additional CRDs. Kourier is an Ingress for Knative Serving. Kourier is a lightweight alternative for the Istio ingress as its deployment consists only of an Envoy proxy and a control plane for it.
- [space-cloud: Develop, Deploy and Secure Serverless Apps on Kubernetes.](https://github.com/spacecloud-io/space-cloud) Open source **Firebase + Heroku** to develop, scale and secure serverless apps on Kubernetes - [space-cloud.io](https://space-cloud.io/) Space Cloud is a Kubernetes based serverless platform that provides instant, realtime APIs on any database, with event triggers and unified APIs for your custom business logic.
- [community.suse.com: Comparing Modern-Day Container Image Builders: Jib, Buildpacks and Docker 🌟](https://community.suse.com/posts/comparing-modern-day-container-image-builders-jib-buildpacks-and-docker)
- [Teleport 🌟](https://github.com/gravitational/teleport) Certificate authority and access plane for SSH, Kubernetes, web applications, and databases
- [weaveworks: kured - Kubernetes Reboot Daemon 🌟](https://github.com/weaveworks/kured) - [weave.works: One year kured - your Kubernetes Reboot Daemon](https://www.weave.works/blog/one-year-kured-kubernetes-reboot-daemon) Kured (KUbernetes REboot Daemon) is a Kubernetes daemonset that performs safe automatic node reboots when the need to do so is indicated by the package management system of the underlying OS. Many rely on Kured, which helps perform safe automatic node reboots when indicated by the package management of the underlying OS, to help make OS security better.
- [k8s-cluster-simulator](https://github.com/pfnet-research/k8s-cluster-simulator) Kubernetes cluster simulator for evaluating schedulers.
- [kubelogin 🌟](https://github.com/int128/kubelogin) kubectl plugin for Kubernetes OpenID Connect authentication (kubectl oidc-login)
- [==kube-oidc-proxy==](https://github.com/jetstack/kube-oidc-proxy) Reverse proxy to authenticate to managed Kubernetes API servers via OIDC.
    - [==tremolosecurity.com: Updating kube-oidc-proxy==](https://www.tremolosecurity.com/post/updating-kube-oidc-proxy) **Kubernetes offers multiple ways to authenticate users to the API server. The best way to go, when available, is to use OpenID Connect (OIDC). We've talked about why you shouldn't use certificates for kubernetes authentication, but most cloud providers won't let you configure the API server flags needed to integrate managed clusters into an OIDC identity provider.**
- [KubeSurvival 🌟](https://github.com/aporia-ai/kubesurvival) Significantly reduce Kubernetes costs by finding the cheapest machine types that can run your workloads
- [K8s Vault Webhook 🌟](https://ot-container-kit.github.io/k8s-vault-webhook/) - [github: k8s-vault-webhook](https://github.com/OT-CONTAINER-KIT/k8s-vault-webhook) A k8s vault webhook is a Kubernetes webhook that can inject secrets into Kubernetes resources by connecting to multiple secret managers
- [cf-for-k8s](https://github.com/cloudfoundry/cf-for-k8s) The open source deployment manifest for Cloud Foundry on Kubernetes. cf-for-k8s blends the popular CF developer API with Kubernetes, Istio, and other open source technologies. The project aims to improve developer productivity for organizations using Kubernetes
- [tekline 🌟](https://github.com/joyrex2001/tekline) tekline is a tekton delegated-pipeline to enable a bring-your-own pipeline configuration.
- [nerdctl 🌟](https://github.com/containerd/nerdctl) Docker-compatible CLI for containerd
- [El Carro: The Oracle Operator for Kubernetes 🌟](https://github.com/GoogleCloudPlatform/elcarro-oracle-operator) El Carro is a new project that offers a way to run Oracle databases in Kubernetes as a portable, open source, community driven, no vendor lock-in container orchestration system. El Carro provides a powerful declarative API for comprehensive and consistent configuration and deployment as well as for real-time operations and monitoring.
- [jspolicy](https://github.com/loft-sh/jspolicy) jsPolicy is an operator that helps you define Kubernetes Policies using JavaScript or TypeScript. Easier & Faster Kubernetes Policies using JavaScript or TypeScript.
    - [blog.ediri.io: Writing Kubernetes policies with jsPolicy and deploy them via FluxCD](https://blog.ediri.io/writing-kubernetes-policies-with-jspolicy) In this tutorial, you will learn how to write Kubernetes policies using JavaScript/Typescript with the help of jsPolicy and deploy them via GitOps using Flux
- [k8scr 🌟](https://github.com/hasheddan/k8scr) A kubectl plugin for pushing OCI images through the Kubernetes API server.
- [jsonnet-controller](https://github.com/pelotech/jsonnet-controller) A fluxcd controller for managing manifests declared in jsonnet.
- [rback: RBAC in Kubernetes visualizer 🌟🌟](https://github.com/team-soteria/rback) A simple "RBAC in Kubernetes" visualizer. No matter how complex the setup, rback queries all RBAC related information of an Kubernetes cluster in constant time and generates a graph representation of service accounts, (cluster) roles, and the respective access rules in dot format.
- [github: Kubernetes JSON Schemas 🌟](https://github.com/instrumenta/kubernetes-json-schema) Schemas for every version of every object in every version of Kubernetes
- [Metacontroller](https://github.com/metacontroller/metacontroller) Metacontroller is an add-on for Kubernetes that makes it easy to write and deploy custom controllers in the form of simple scripts.
- [KubeCarrier - Service Management at Scale](https://github.com/kubermatic/kubecarrier) KubeCarrier is an open source system for managing applications and services across multiple Kubernetes Clusters; providing a framework to centralize the management of services and provide these services with external users in a self service hub.
- [github.com: NFS Ganesha server and external provisioner](https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner) NFS Ganesha Server and Volume Provisioner. nfs-ganesha-server-and-external-provisioner is an out-of-tree dynamic provisioner for Kubernetes 1.14+. You can use it to quickly & easily deploy shared storage that works almost anywhere.
- [Armada kubectl plugin 🌟](https://github.com/night-gold/armada) Command line tools to manage kustomize packaged apps deployment. Armada is a Kubectl plugin that adds templating capacity and manage deployment to Kustomize apps. Templating uses go template to allow you to generate kustomize apps with templates inside. Armada allows you to git clone a packaged kustomize base and call it with the help of a config file.
- [Minnaker](https://github.com/armory/minnaker) Minnaker is a simple way to install Spinnaker inside a VM. Spinnaker on Lightweight Kubernetes (K3s)
- [kVDI](https://github.com/kvdi/kvdi) A Kubernetes-native Virtual Desktop Infrastructure
- [Kubesurveyor 🌟](https://github.com/viralpoetry/kubesurveyor) Good enough Kubernetes namespace visualization tool. No provisioning to a cluster required, only Kubernetes API is scrapped.
- [NVIDIA k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin) NVIDIA device plugin for Kubernetes. The NVIDIA device plugin for Kubernetes is a Daemonset that allows you to automatically: Expose GPUs on each nodes of your cluster, Keep track of the health of your GPUs, Run GPU enabled containers.
- [kubectl-tmux-exec](https://github.com/predatorray/kubectl-tmux-exec) A kubectl plugin to control multiple pods simultaneously using Tmux
- [grype: a vulnerability scanner for container images and filesystems](https://github.com/anchore/grype)
- [KubeView 🌟](https://github.com/benc-uk/kubeview) Kubernetes cluster visualiser and graphical explorer. KubeView displays what is happening inside a Kubernetes cluster (or single namespace), it maps out the API objects and how they are interconnected. Data is fetched real-time from the Kubernetes API. The status of some objects (Pods, ReplicaSets, Deployments) is colour coded red/green to represent their status and health
- [karma 🌟](https://github.com/prymitive/karma) Alert dashboard for Prometheus Alertmanager
- [Rancher Desktop 🌟](https://github.com/rancher-sandbox/rancher-desktop) Kubernetes and container management to the desktop. Rancher Desktop is an open-source project to bring Kubernetes and container management to the desktop. Windows and macOS versions of Rancher Desktop are available for download.
- [realvz/awesome-eks: A curated list of awesome tools for Amazon EKS 🌟](https://github.com/realvz/awesome-eks)
- [salesforce/Sloop - Kubernetes History Visualization 🌟](https://github.com/salesforce/sloop) Sloop monitors Kubernetes, recording histories of events and resource state changes and providing visualizations to aid in debugging past events.
- [scalabledelivery/init-sync](https://github.com/scalabledelivery/init-sync) Sidecar for securely copying directory for statefulsets. A sidecar containner and initContainer for securely copying a directory between pods in StatefulSets.
- [Kspan - Turning Kubernetes Events into spans 🌟](https://github.com/weaveworks-experiments/kspan) Most Kubernetes components produce Events when something interesting happens. This program turns those Events into OpenTelemetry Spans, joining them up by causality and grouping them together into Traces.
- [csi-rclone: CSI rclone mount plugin](https://github.com/wunderio/csi-rclone) CSI driver for rclone. This project implements Container Storage Interface (CSI) plugin that allows using rclone mount as storage backend. Rclone mount points and parameters can be configured using Secret or PersistentVolume volumeAttibutes.
- [stackrox.io: Top 9 Open Source DevSecOps Tools for Kubernetes in 2021 🌟](https://www.stackrox.io/blog/top-9-open-source-devsecops-tools-for-kubernetes/) **Anchore, Checkov, Clair, Falco, Kube-bench, Kube-hunter, KubeLinter, Open Policy Agent (OPA), Terrascan**
- [Kdo: deployless development on Kubernetes 🌟](https://kdo.dev/) Kdo is a command line tool that enables developers to run, develop and test code changes in a realistic deployed setting without having to deal with the complexity of Kubernetes deployment and configuration.
- [chekr](https://github.com/ckotzbauer/chekr) A inspection utility for the maintenance of Kubernetes clusters.
    - [github.com issues: Generate Kyverno deprecation policies with chekr](https://github.com/ckotzbauer/chekr/issues/61)
- [KUR8 🌟](https://github.com/oslabs-beta/KUR8) A visual overview of Kubernetes architecture and Prometheus metrics. KUR8 is an open-source Kubernetes analytics, monitoring, and visualizer web application that allows for querying, alerts, and creating custom charts and graphs that leverage Prothemeus and its time logged series database metrics.
- [mperezco/forklift-configmap-service](https://github.com/mperezco/forklift-configmap-service) Systemd service to run in VMs on KubeVirt to mount ConfigMaps
- [cdk8s](https://github.com/cdk8s-team/cdk8s) Define Kubernetes native apps and abstractions using object-oriented programming
- [Havener](https://github.com/homeport/havener) Think of it as a swiss army knife for Kubernetes tasks.
- [KFServing 🌟](https://github.com/kubeflow/kfserving) Serverless Inferencing on Kubernetes. KFServing provides a Kubernetes Custom Resource Definition for serving machine learning (ML) models on arbitrary frameworks. It aims to solve production model serving use cases by providing performant, high abstraction interfaces for common ML frameworks like Tensorflow, XGBoost, ScikitLearn, PyTorch, and ONNX.
- [rkubelog 🌟](https://github.com/solarwinds/rkubelog) Send k8s Logs to Papertrail and Loggly Without DaemonSets (for Nodeless Clusters) - [dzone: ContainerD Kubernetes Syslog Forwarding](https://dzone.com/articles/containerd-kubernetes-syslog-forwarding) Move from Logspout to Filebeat to support containerd logging architecture.
- [kubernetes-sigs: Trimaran: Load-aware scheduling plugins 🌟](https://github.com/kubernetes-sigs/scheduler-plugins/tree/master/pkg/trimaran) Trimaran is a collection of load-aware scheduler plugins - [thenewstack.io: IBM, Red Hat Bring Load-Aware Resource Management to Kubernetes](https://thenewstack.io/ibm-red-hat-bring-load-aware-resource-management-to-kubernetes/)
- [AWS Controllers for Kubernetes (ACK) 🌟](https://github.com/aws-controllers-k8s/community) AWS Controllers for Kubernetes (ACK) is a project enabling you to manage AWS services from Kubernetes
- [connaisseur](https://github.com/sse-secure-systems/connaisseur) An admission controller that integrates Container Image Signature Verification into a Kubernetes cluster
- [VolSync 🌟](https://github.com/backube/volsync) Asynchronous data replication for Kubernetes volumes. VolSync asynchronously replicates Kubernetes persistent volumes between clusters using either rsync or rclone. It also supports creating backups of persistent volumes via restic. VolSync, a new storage-agnostic utility for exporting and importing objects from one Kubernetes namespace to another, even across clusters!
- [ketall](https://github.com/corneliusweig/ketall) Kubectl plugin to show really all kubernetes resources. Like `kubectl get all`, but get really all resources
- [kube-scheduler-simulator](https://github.com/kubernetes-sigs/kube-scheduler-simulator) Web-based Kubernetes scheduler simulator
- [multus-cni 🌟](https://github.com/k8snetworkplumbingwg/multus-cni) A CNI meta-plugin for multi-homed pods in Kubernetes. Multus CNI is a container network interface (CNI) plugin for Kubernetes that enables attaching multiple network interfaces to pods. Typically, in Kubernetes each pod only has one network interface (apart from a loopback) -- with Multus you can create a multi-homed pod that has multiple interfaces. This is accomplished by Multus acting as a "meta-plugin", a CNI plugin that can call multiple other CNI plugins.
- [kim - The Kubernetes Image Manager](https://github.com/rancher/kim)
- [KUDO: The Kubernetes Universal Declarative Operator 🌟](https://kudo.dev/) KUDO is a toolkit that makes it easy to build Kubernetes Operators, in most cases just using YAML.
- [K8sPurger 🌟](https://github.com/yogeshkk/K8sPurger) K8SPurger is a controller that finds all unused resources and show them in a nice format
- [jenkins-x/gsm-controller](https://github.com/jenkins-x/gsm-controller) gsm-controller is a Kubernetes controller that copies secrets from Google Secrets Manager into Kubernetes secrets. The controller watches Kubernetes secrets looking for an annotation, if the annotation is not found on the secret nothing more is done.
- [kontacts](https://github.com/scalabledelivery/kontacts) A Kubernetes directory tool for finding pods and services.
- [sciuro](https://github.com/cloudflare/sciuro) Alertmanager to Kubernetes Node conditions bridge. Sciuro is a bridge between Alertmanager and Kubernetes to sync alerts as Node Conditions. It is designed to work in tandem with other controllers that observe Node Conditions such as draino or the cluster-api.
- [rottencandy/vimkubectl](https://github.com/rottencandy/vimkubectl) Manage Kubernetes resources from Vim
- [carlosedp/cluster-monitoring: Cluster Monitoring stack for ARM / X86-64 platforms](https://github.com/carlosedp/cluster-monitoring) Cluster monitoring stack for clusters based on Prometheus Operator
- [abhirockzz/kubexpose-operator](https://github.com/abhirockzz/kubexpose-operator) Access your Kubernetes Deployment over the Internet - [itnext.io: Kubexpose: A Kubernetes Operator, for fun and profit!](https://itnext.io/kubexpose-a-kubernetes-operator-for-fun-and-profit-f528586eee07) Access your Kubernetes Deployment over the Internet
- [kubernetes-reflector](https://github.com/emberstack/kubernetes-reflector) **Custom Kubernetes controller that can be used to replicate secrets, configmaps and certificates.**
- [Another Autoscaler](https://github.com/dignajar/another-autoscaler) Another Autoscaler is a Kubernetes controller that automatically starts, stops, or restarts pods from a deployment at a specified time using a cron syntax.
- [cloud-ark/kubeplus 🌟](https://github.com/cloud-ark/kubeplus) Kubernetes Operator to deliver Helm charts as-a-service
- [cloud-ark/caastle](https://github.com/cloud-ark/caastle) Full-stack microservices deployment for Google Kubernetes Engine and Amazon Elastic Container Service
- [eezhee/eezhee](https://github.com/eezhee/eezhee) The easiest way to build a k3s cluster on various public clouds. A super fast and easy way to create a k3s based kubernetes cluster on a variety of public clouds. Currently DigitalOcean, Linode and Vultr are supported. All it takes is a single command and about 2 minutes and your cluster is ready to use. Most of the time is taken by the cloud provider bring up the base VM. Eezhee is ideal for development, testing or learning about Kubernetes.
- [ContainerSolutions/ImageWolf: ImageWolf - Fast Distribution of Docker Images on Clusters](https://github.com/ContainerSolutions/ImageWolf) Fast Distribution of Docker Images on Clusters. ImageWolf is a PoC that provides a blazingly fast way to get Docker images loaded onto your cluster, allowing updates to be pushed out quicker.
- [dcherman/image-cache-daemon](https://github.com/dcherman/image-cache-daemon) Image Cache Daemon is a service to pre-pull / cache images on Kubernetes before they're needed
- [KnicKnic/temp-kubernetes-ci: Temp Kubernetes CI](https://github.com/KnicKnic/temp-kubernetes-ci) A github action to create a k3s kubernetes cluster in your CI VM for both linux & windows. Also has cmdline to copy and paste for other CI platforms.
- [mattmoor/warm-image: Kubernetes WarmImage CRD](https://github.com/mattmoor/warm-image) A Kubernetes CRD for prefetching container images onto nodes.
- [maorfr/kube-tasks: Kube tasks](https://github.com/maorfr/kube-tasks) A tool to perform simple Kubernetes related actions. Simple Backups, Wait for Pods, Execute a command in a container.
- [tmobile/MagTape](https://github.com/tmobile/magtape) MagTape Policy-as-Code for Kubernetes. MagTape is a Policy-as-Code tool for Kubernetes that allows for evaluating Kubernetes resources against a set of defined policies. MagTape includes variable policy enforcement, notifications, and targeted metrics
- [vidispine/HULL - Helm Uniform Layer Library](https://github.com/vidispine/hull) HULL (Helm Uniform Layer Library) is designed to ease building, maintaining and configuring Kubernetes objects in Helm charts.
- [hiddeco/Cronjobber](https://github.com/hiddeco/cronjobber) Cronjobber is a cronjob controller for Kubernetes with support for time zones
- [karmab/autolabeller](https://github.com/karmab/autolabeller) This repo contains a controller automatically labelling nodes based on either:
    - predefined regex rules matching node name.
    - a set of matching labels (with their associated value) present on the node.
- [kubernetes-sigs/nfs-subdir-external-provisioner: Kubernetes NFS Subdir External Provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner) Dynamic sub-dir volume provisioner on a remote NFS server. NFS subdir external provisioner is an automatic provisioner that use your existing NFS server to support dynamic provisioning of Kubernetes Persistent Volumes via Persistent Volume Claims
- [ori-edge/k8s_gateway](https://github.com/ori-edge/k8s_gateway) A CoreDNS plugin to resolve all types of external Kubernetes resources. k8s_gateway is a CoreDNS plugin that resolves load balancer and external IPs from outside Kubernetes clusters and supports all types of Kubernetes external resources - Ingress, Service of type LoadBalancer.
- [viaduct-ai/kustomize-sops](https://github.com/viaduct-ai/kustomize-sops) KSOPS - A Flexible Kustomize Plugin for SOPS Encrypted Resources
- [vadosware.io: Using Makefiles And Envsubst As An Alternative To Helm And Ksonnet (deprecated)](https://vadosware.io/post/using-makefiles-and-envsubst-as-an-alternative-to-helm-and-ksonnet/)
- [uw-labs.github.io: Kubernetes Semaphore: A modular and nonintrusive framework for cross cluster communication](https://uw-labs.github.io/blog/kubernetes,/multicluster/2021/07/21/kube-semaphore-intro.html)
- [zakkg3/ClusterSecret: Kubernetes ClusterSecret operator](https://github.com/zakkg3/ClusterSecret) ClusterSecret operator makes sure all the matching namespaces have the secret available. New namespaces, if they match the pattern, will also have the secret. Any change on the ClusterSecret will update all related secrets. Deleting the ClusterSecret deletes "child" secrets (all cloned secrets) too.
- [tektoncd/chains](https://github.com/tektoncd/chains) Tekton Chains is a Kubernetes Custom Resource Definition (CRD) controller that allows you to manage your supply chain security in Tekton.
- [gopaddle-io/configurator](https://github.com/gopaddle-io/configurator) Synchronize and Version Control ConfigMaps & Secrets across Deployment Rollouts.
- [biosimulations/deployment](https://github.com/biosimulations/deployment) Kubernetes Configuration for [BioSimulations](https://github.com/biosimulations/biosimulations) platform.
- [chrislusf/seaweedfs](https://github.com/chrislusf/seaweedfs) SeaweedFS is a fast distributed storage system for blobs, objects, files, and data lake, for billions of files! Blob store has O(1) disk seek, local tiering, cloud tiering. Filer supports Cloud Drive, cross-DC active-active replication, Kubernetes, POSIX FUSE mount, S3 API, Hadoop, WebDAV, encryption, Erasure Coding.
- [kubernetes-sigs/kui](https://github.com/kubernetes-sigs/kui) A hybrid command-line/UI development experience for cloud-native development
- [DaspawnW/vault-crd](https://github.com/DaspawnW/vault-crd) Vault CRD for sharing Vault Secrets with Kubernetes. Vault-CRD is a custom resource definition for holding secrets that are stored in HashiCorp Vault and kept up to date with Kubernetes secrets
- [stakater/Reloader 🌟](https://github.com/stakater/Reloader) A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig
- [dignajar/another-ldap](https://github.com/dignajar/another-ldap) Another LDAP is a form-based authentication for Active Directory / LDAP server. Provides Authentication and Authorization for your applications running in Kubernetes.
- [ddosify/ddosify](https://github.com/ddosify/ddosify) High-performance load testing tool, written in Golang.
- [==anchore/syft==](https://github.com/anchore/syft) CLI tool and library for generating a Software Bill of Materials from container images and filesystems. Exceptional for vulnerability detection when used with a scanner tool like Grype.
- [==aws/aws-node-termination-handler== 🌟](https://github.com/aws/aws-node-termination-handler) Gracefully handle EC2 instance shutdown within Kubernetes
- [aelsabbahy/goss](https://github.com/aelsabbahy/goss) Quick and Easy server testing/validation
- [chr-fritz/csi-sshfs](https://github.com/chr-fritz/csi-sshfs) Kubernetes CSI Plugin for SSHFS. It allows to mount directories using a ssh connection.
- [ctrox/csi-s3](https://github.com/ctrox/csi-s3) A Container Storage Interface for S3. This is a Container Storage Interface (CSI) for S3 (or S3 compatible) storage. This can dynamically allocate buckets and mount them via a fuse mount into any container.
- [codesenberg/bombardier 🌟](https://github.com/codesenberg/bombardier) Fast cross-platform HTTP benchmarking tool written in Go
- [fstab/cifs](https://github.com/fstab/cifs) CIFS Flexvolume Plugin for Kubernetes. Driver for CIFS (SMB, Samba, Windows Share) network filesystems as Kubernetes volumes.
- [kui.tools](https://kui.tools) Kui: CLI-driven Graphics for Kubernetes. Tired of working with Kubernetes in cli mode only? Try kui - a hybrid tool that allows you to interact with any Kubernetes cluster easily with more advanced features available only in GUI.
- [bloomberg/goldpinger 🌟](https://github.com/bloomberg/goldpinger) Debugging tool for Kubernetes which tests and displays connectivity between nodes in the cluster. **Goldpinger makes calls between its instances to monitor your networking. It runs as a DaemonSet on Kubernetes and produces Prometheus metrics that can be scraped, visualised and alerted on.**
- [haxsaw/hikaru 🌟](https://github.com/haxsaw/hikaru) Move smoothly between Kubernetes YAML and Python for creating/updating/componentizing configurations. **Hikaru is a tool that provides you the ability to easily shift between YAML, Python objects/source, and JSON representations of your Kubernetes config files.** It provides assistance in authoring these files in Python, opens up options in how you can assemble and customise the files, and provides some programmatic tools for inspecting large, complex files to enable automation of policy and security compliance. Additionally, Hikaru allows you to use its K8s model objects to interact with Kubernetes, directing it to create, modify, and delete resources.
- [kei6u/kubectl-secret-data](https://github.com/kei6u/kubectl-secret-data) A kubectl plugin for finding decoded secret data with productive search flags.
- [ofek/csi-gcs](https://github.com/ofek/csi-gcs) Kubernetes CSI driver for Google Cloud Storage. An easy-to-use, cross-platform, and highly optimized Kubernetes CSI driver for mounting Google Cloud Storage buckets.
- [target/pod-reaper](https://github.com/target/pod-reaper) ==Rule based pod killing kubernetes controller==. Pod-Reaper was designed to kill pods that meet specific conditions. See the "Implemented Rules" section below for details on specific rules.
- [utilitywarehouse/kube-applier](https://github.com/utilitywarehouse/kube-applier) **kube-applier enables automated deployment and declarative configuration for your Kubernetes cluster.** kube-applier is Kubernetes deployment tool strongly following gitOps principals. It enables continuous deployment of Kubernetes objects by applying declarative configuration files from a Git repository to a Kubernetes cluster.
    - https://github.com/box/kube-applier
- [Trendyol/kink](https://github.com/Trendyol/kink) KinK is a helper CLI that facilitates to manage KinD clusters as Kubernetes pods. Designed to ease clusters up for fast testing with batteries included in mind.
- [vbouchaud/k8s-ldap-auth](https://github.com/vbouchaud/k8s-ldap-auth) Kubernetes webhook token authentication plugin implementation using ldap.
- [wangjia184/pod-inspector](https://github.com/wangjia184/pod-inspector) A tool to inspect pods in kubernetes. Unlike other dashboardes for Kubernetes(Lens / Rancher / etc), ==Kubernetes Pod Inspector allows to check the file system and processes within running Linux pods without using kubectl. This is useful when we want to check the files within volumes mounted by pods==
- [witchery-project/witchery](https://github.com/witchery-project/witchery) build distroless images with alpine tools
- [==knight42/kubectl-blame: kubectl-blame: git-like blame for kubectl==](https://github.com/knight42/kubectl-blame) Show who edited resource fields. A useful opensource tool that comes as a plugin to show who modified attributes in kubernetes resource fields.
- [curiefense/curiefense](https://github.com/curiefense/curiefense) Curiefense extends Envoy proxy to defend against a variety of threats, including SQL and command injection, cross site scripting (XSS), account takeovers (ATOs) and more
- [==kubernetes-sigs/node-feature-discovery: Node feature discovery for Kubernetes==](https://github.com/kubernetes-sigs/node-feature-discovery) Welcome to Node Feature Discovery – a Kubernetes add-on for detecting hardware features and system configuration!
- [==arttor/helmify==](https://github.com/arttor/helmify) Creates Helm chart from Kubernetes yaml. Helmify reads a list of supported k8s objects from stdin and converts it to a helm chart. Designed to generate charts for k8s operators but not limited to. See examples of charts generated by helmify.
    - [medium.com/geekculture: Convert Kubernetes YAML Files Into Helm Charts](https://medium.com/geekculture/convert-kubernetes-yaml-files-into-helm-charts-4107de079455)
- [4ARMED/kubeletmein](https://github.com/4ARMED/kubeletmein) Security testing tool for Kubernetes, abusing kubelet credentials on public cloud providers. This is a simple penetration testing tool which takes advantage of public cloud provider approaches to providing kubelet credentials to nodes in a Kubernetes cluster in order to gain privileged access to the k8s API. This access can then potentially be used to further compromise the applications running in the cluster or, in many cases, access secrets that facilitate complete control of Kubernetes.
- [patrickdappollonio/kubectl-slice](https://github.com/patrickdappollonio/kubectl-slice) Split multiple Kubernetes files into smaller files with ease. Split multi-YAML files into individual files.
- [appvia/cosign-keyless-admission-webhook](https://github.com/appvia/cosign-keyless-admission-webhook) Kubernetes admission webhook that uses cosign verify to check the subject and issuer of the image matches what you expect
- [theketchio/ketch 🌟](https://github.com/theketchio/ketch) Ketch is an application delivery framework that facilitates the deployment and management of applications on Kubernetes using a simple command line interface.
- [joyrex2001/kubedock](https://github.com/joyrex2001/kubedock) Kubedock is a minimal implementation of the docker api that will orchestrate containers on a Kubernetes cluster, rather than running containers locally.
- [corneliusweig/konfig](https://github.com/corneliusweig/konfig) konfig helps to merge, split or import kubeconfig files
- [armosec/regolibrary](https://github.com/armosec/regolibrary) ARMO rego library for detecting miss-configurations in Kubernetes manifests
- [groundnuty/k8s-wait-for 🌟](https://github.com/groundnuty/k8s-wait-for) A simple script that allows to wait for a k8s service, job or pods to enter a desired state
- [nabsul/k8s-ecr-login-renew: Renew Kubernetes Docker secrets for AWS ECR](https://github.com/nabsul/k8s-ecr-login-renew) Renews Docker login credentials for an AWS ECR container registry.
- [particledecay/kconf](https://github.com/particledecay/kconf) Manage multiple kubeconfigs easily
- [maruina/aws-auth-manager: K8s controller to manage the aws-auth configmap](https://github.com/maruina/aws-auth-manager) aws-auth-manager is a Kubernetes controller designed to manage the aws-auth ConfigMap in EKS using a new AWSAuthItem CRD
- [segmentio/kubectl-curl: Kubectl plugin to run curl commands against kubernetes pods](https://github.com/segmentio/kubectl-curl)
- [wallarm/sysbindings](https://github.com/wallarm/sysbindings) sysctl/sysfs settings on a fly for Kubernetes Cluster. No restarts are required for clusters and nodes.
- [==atombender/ktail== 🌟](https://github.com/atombender/ktail) ktail is a tool to easily tail Kubernetes logs. It's like kubectl logs, but with a bunch of features to make it more convenient:
    - Detects pods and containers as they come and go
    - Tails multiple pods and containers
    - All containers are tailed by default
    - Recovers from failure
- https://pinniped.dev 🌟 - [vmware-tanzu/pinniped](https://github.com/vmware-tanzu/pinniped) **Pinniped is the easy, secure way to log in to your Kubernetes clusters.**
- [keisku/kubectl-explore](https://github.com/keisku/kubectl-explore) A better kubectl explain with the fuzzy finder. This plugin fuzzy-find the field explanation from supported API resources. It implements different explanations for particular API version. kubectl-explore is a kubectl plugin to fuzzy-find and explain the field supported API resources like "pod.spec", "cronJob.spec.jobTemplate", etc.
- [box/kube-exec-controller](https://github.com/box/kube-exec-controller) An admission controller service and kubectl plugin to handle container drift in K8s clusters. kube-exec-controller is an admission controller for handling container drift (caused by kubectl exec, attach, cp, or other interactive requests) inside a Kubernetes cluster. This project also includes a kubectl plugin for checking such Pods.
- [==abahmed/kwatch==](https://github.com/abahmed/kwatch) 👀 monitor & detect crashes in your Kubernetes(K8s) cluster instantly. kwatch helps you monitor all changes in your Kubernetes cluster, detects crashes in your running apps in real-time, and publishes notifications to your channels (Slack, Discord, etc.) instantly.
- [cuber-cloud/cuber-gem: CUBER](https://github.com/cuber-cloud/cuber-gem) An automation tool that simplify the deployment of your apps on Kubernetes.
    - https://cuber.cloud/ 🌟
- [==kubeops/config-syncer: Config Syncer (previously Kubed)==](https://github.com/kubeops/config-syncer) Kubernetes Config Syncer (previously kubed). **Config Syncer keeps ConfigMaps and Secrets synchronized across namespaces and/or clusters**
- [eldadru/ksniff 🌟](https://github.com/eldadru/ksniff) Kubectl plugin to ease sniffing on kubernetes pods using tcpdump and wireshark
- [openclarity/kubeclarity](https://github.com/openclarity/kubeclarity) KubeClarity is a tool for detection and management of Software Bill Of Materials (SBOM) and vulnerabilities of container images and filesystems
    - [medium.com/@ryan.dardis: KubeClarity — Cloud-Native Security Scanning for your Kubernetes Cluster and more](https://medium.com/@ryan.dardis/kubeclarity-cloud-native-security-scanning-for-your-kubernetes-cluster-and-more-7c3ee6a16556)
- [==NimbleArchitect/kubectl-ice== 🌟](https://github.com/NimbleArchitect/kubectl-ice) Cleanly list all containers in kubernetes pods including init containers and view running kubernetes information about those multi-container pods to assist in troubleshooting and information gathering. kubectl-ice is a kubectl plugin that lets you see the configuration of all pod's containers. You can inspect volumes, images, ports and executable configurations, along with current CPU and memory metrics at the container level.
- [==vmware-tanzu/k-bench== 🌟](https://github.com/vmware-tanzu/k-bench) Workload Benchmark for Kubernetes. K-Bench is a framework to benchmark the control and data plane aspects of a Kubernetes infrastructure. It provides a configurable way to prescriptively create and manipulate Kubernetes resources at scale and collect the metrics.
- [k8tz/k8tz: Kubernetes Timezone Controller](https://github.com/k8tz/k8tz) Kubernetes admission controller and a CLI tool to inject timezones into Pods and CronJobs
- [patrickdappollonio/tabloid: tabloid -- your tabulated data's best friend](https://github.com/patrickdappollonio/tabloid) tabloid is a simple command line tool to parse and filter column-based CLI outputs from commands like kubectl or docker
- [ReallyLiri/kubescout: Kube-Scout](https://github.com/ReallyLiri/kubescout) Scout for alarming issues across your Kubernetes clusters. kubescout is a command-line tool designed to issue alerts in real-time for:
    - Pod evictions
    - Pod stuck in terminating/initializing
    - Excessive disk usage, process & inode allocation
    - Warning/errors in native logs
    - Helm failures
    - etc
- [govirtuo/kube-ns-suspender 🌟](https://github.com/govirtuo/kube-ns-suspender) A k8s controller that scales up and down namespaces on-demand with an embedded friendly UI and a Prometheus exporter. Inspired by [kube-downscaler](https://codeberg.org/hjacobs/kube-downscaler).**Kube-ns-suspender watches namespaces and "suspends" them by scaling to 0 some of the resources. Once a namespace is suspended, it will not be restarted automatically. This allows to "reactivate" namespaces only when required and reduces costs**
- [codeberg.org/hjacobs/kube-downscaler: Kubernetes Downscaler 🌟](https://codeberg.org/hjacobs/kube-downscaler) **Scale down / "pause" Kubernetes workload (Deployments, StatefulSets, and/or HorizontalPodAutoscalers and CronJobs too !) during non-work hours.**
- [deepfence/PacketStreamer](https://github.com/deepfence/PacketStreamer) ⭐⭐ Distributed tcpdump for cloud native environments ⭐⭐ PacketStreamer is a high-performance remote packet capture and collection tool. It is used by Deepfence's ThreatStryker security observability platform to gather network traffic on demand from cloud workloads for forensic analysis.
- [kris-nova/kaar](https://github.com/kris-nova/kaar) kaar is the Kubernetes Application Archive. kaar will:
    - Recursively iterate through every file in the path and search for valid Kubernetes YAML
    - Identify all container images referenced from the YAML
    - Archive the container images
- [mohatb/kubectl-exec](https://github.com/mohatb/kubectl-exec) kubectl-exec is a kubectl plugin that allows you to access a node. It works by creating a pod (with a privileged container) in the node you specified and using nsenter for getting a shell into your Kubernetes nodes. Works on both Linux and Windows.
- [kudobuilder/kuttl](https://github.com/kudobuilder/kuttl) KUbernetes Test TooL (KUTTL) provides a declarative approach to test Kubernetes Operators. It is designed for testing operators, however it can declaratively test any kubernetes objects.
- [==steveteuber/kubectl-graph== ⭐](https://github.com/steveteuber/kubectl-graph) **A kubectl plugin to visualize Kubernetes resources and relationships.**
- [crazy-max/diun](https://github.com/crazy-max/diun) Diun is a CLI application written in Go and delivered as a single executable (and a Docker image) to receive notifications when a Docker image is updated on a Docker registry.
- [==omrikiei/ktunnel== ⭐](https://github.com/omrikiei/ktunnel) **A cli that exposes your local resources to kubernetes. A CLI tool that establishes a reverse tunnel between a kubernetes cluster and your local machine.**
- [dev.to: Pixie: an X-ray Machine for Kubernetes Traffic](https://dev.to/otomato_io/pixie-an-x-ray-machine-for-kubernetes-traffic-23pd) Pixie is one of a handful of observability tools that offer eBPF or kernel-level observability. In this tutorial, you will learn how to see all of your applications' metrics, events, logs, and traces using Pixie with Kubernetes.
- [plural.sh: Deploy open-source software on Kubernetes in record time ⭐](https://www.plural.sh/) An open-source platform to build, maintain, and scale infrastructure on Kubernetes. Batteries included.
    - [medium.com/@michaeljguarino: How we Created an in-Browser Kubernetes Experience](https://medium.com/@michaeljguarino/how-we-created-an-in-browser-kubernetes-experience-58c065cda803)
- [pan-net-security/kcount](https://github.com/pan-net-security/kcount) kcount counts Kubernetes objects across namespaces and clusters. It can be used as a CLI tool or as a daemon (service) exposing Prometheus metrics.
- [cloudtty/cloudtty: A Kubernetes Cloud Shell (Web Terminal) Operator](https://github.com/cloudtty/cloudtty) A Friendly Kubernetes CloudShell (Web Terminal) !
- [jthomperoo/k8shorizmetrics](https://github.com/jthomperoo/k8shorizmetrics) k8shorizmetrics is a library that provides the internal workings of the Kubernetes Horizontal Pod Autoscaler (HPA) wrapped up in a simple API. The project allows querying metrics just as the HPA does, and also running the calculations.
- [==Kube-capacity==](https://github.com/robscott/kube-capacity/releases) is a simple and powerful CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster. It combines the best parts of kubectl top and describe into an easy to use CLI focused on cluster resources.
- [==github.com/FairwindsOps: Goldilocks is a utility that can help you identify a starting point for resource requests and limits==](https://github.com/FairwindsOps/goldilocks)
- [==learnk8s/xlskubectl==](https://github.com/learnk8s/xlskubectl) a spreadsheet to control your Kubernetes cluster. xlskubectl integrates Google Spreadsheet with Kubernetes. You can finally administer your cluster from the same spreadsheet that you use to track your expenses.
- [kingdonb/kubectl-exec-user](https://github.com/kingdonb/kubectl-exec-user) lets you exec as a specified user into a Kubernetes container
- [upmc-enterprises/registry-creds: Registry Credentials ⭐](https://github.com/upmc-enterprises/registry-creds) Allow for AWS ECR, Google Registry, & Azure Container Registry credentials to be refreshed inside your Kubernetes cluster via ImagePullSecrets
- [pymag09/kubecui](https://github.com/pymag09/kubecui) kubeui makes kubectl more user friendly. This is still kubectl but enhanced with [fzf](https://github.com/junegunn/fzf). However, kubectl slows you down - requires heavy keyboard typing. In order to alleviate interaction with kubernetes API and describe the fields associated with each supported API resource directly in the Terminal, kubectl was complemented by fzf.
- [awesome-it/adeploy](https://github.com/awesome-it/adeploy) adeploy is a deployment tool for Kubernetes that supports the rendering and deploying of lightweight Jinja templated Kubernetes manifests and complex Helm charts
- [stakater/Forecastle](https://github.com/stakater/Forecastle) Forecastle is a control panel which dynamically discovers and provides a launchpad to access applications deployed on Kubernetes
- [acorn-io/acorn](https://github.com/acorn-io/acorn) Acorn is a simple application deployment framework for Kubernetes:
    - One artifact across dev, test, and production
    - Simple CLI and powerful API
    - Runs on any Kubernetes cluster
- [smartxworks/knest](https://github.com/smartxworks/knest) knest: Kubernetes-in-Kubernetes Made Simple
- [smartxworks/virtink](https://github.com/smartxworks/virtink) Virtink is a Kubernetes add-on for running Cloud Hypervisor virtual machines. By using Cloud Hypervisor as the underlying hypervisor, Virtink enables a lightweight and secure way to run fully virtualized workloads in a canonical Kubernetes cluster
- [inspektor-gadget/inspektor-gadget](https://github.com/inspektor-gadget/inspektor-gadget) Introspecting and debugging Kubernetes applications using eBPF "gadgets". Inspektor Gadget is a collection of tools (or gadgets) to debug and inspect Kubernetes resources and applications. It manages the packaging, deployment and execution of eBPF programs in a Kubernetes cluster, including many based on BCC tools, as well as some developed specifically for use in Inspektor Gadget. It automatically maps low-level kernel primitives to high-level Kubernetes resources, making it easier and quicker to find the relevant information.
- [toboshii/hajimari](https://github.com/toboshii/hajimari) Hajimari is a beautiful & customizable browser startpage/dashboard with Kubernetes application discovery.
- [Ramilito/kubediff ⭐](https://github.com/Ramilito/kubediff) Source VS Deployed. kubediff compares the local YAML resource definitions with the ones currently deployed in the cluster.
- [FairwindsOps/gonogo](https://github.com/FairwindsOps/gonogo) GoNoGo is a utility to help users determine upgrade confidence around Kubernetes cluster addons
- [==pulumi/kube2pulumi==](https://github.com/pulumi/kube2pulumi) Upgrade your Kubernetes YAML to a modern language
- [==doitintl/kube-no-trouble: kubent== ⭐⭐⭐](https://github.com/doitintl/kube-no-trouble) **Easily check your clusters for use of deprecated APIs.** Kube No Trouble (kubent) is a tool to check whether you're using any deprecated APIs in your cluster and, therefore, should upgrade your workloads first before upgrading your Kubernetes cluster
- [resmoio/kubernetes-event-exporter](https://github.com/resmoio/kubernetes-event-exporter) Export Kubernetes events to multiple destinations with routing and filtering. kubernetes-event-exporter allows exporting the often missed Kubernetes events to various outputs to be used for observability or alerting purposes
- [jthomperoo/predictive-horizontal-pod-autoscaler](https://github.com/jthomperoo/predictive-horizontal-pod-autoscaler) Horizontal Pod Autoscaler built with predictive abilities using statistical models
- [github.com/chenjiandongx/kubectl-count](https://github.com/chenjiandongx/kubectl-count) Count resources by kind. kubectl-count uses the dynamic library to find server preferred resources and then leverages the informer mechanism to list and count resources by kind. You can show any kinds counts in kubernetes and group by namespaces.
- [github.com/rothgar/bashScheduler](https://github.com/rothgar/bashScheduler) Kubernetes scheduler written in less than 100 lines of bash
- [github.com/kubereboot/kured ⭐](https://github.com/kubereboot/kured) Kured (KUbernetes REboot Daemon) is a Kubernetes daemonset that performs safe automatic node reboots when the need to do so is indicated by the package management system of the underlying OS.
- [kubernetes-sigs/kwok](https://github.com/kubernetes-sigs/kwok) Kubernetes WithOut Kubelet - Simulates thousands of Nodes and Clusters. KWOK (Kubernetes-WithOut-Kubelet) is a toolkit that enables setting up a cluster of thousands of nodes in seconds. Under the scene, all Nodes are simulated to behave like real ones, so the overall approach employs a pretty low resource footprint.
- [github.com/squat/kilo](https://github.com/squat/kilo) Kilo is a multi-cloud network overlay built on WireGuard and designed for Kubernetes (k8s + wg = kg)
- [github.com/krateoplatformops/krateo](https://github.com/krateoplatformops/krateo) Krateo Platformops is an open-source tool that allows users to create any desired resource on various infrastructures. It acts as a centralized control plane, allowing users to monitor and control resources.
- [github.com/jwcesign/kubespider](https://github.com/jwcesign/kubespider) A global resource download orchestration system, build your home download center.
- [faun.pub: A browser based remote desktop solution on kubernetes](https://faun.pub/a-browser-based-remote-desktop-solution-on-kubernetes-d6b3d33e73b6) Building a cost effective and simple remote desktop solution on kubernetes using open source apache guacamole
- [kvaps/kubectl-node-shell](https://github.com/kvaps/kubectl-node-shell) kubectl node-shell is a krew plugin that lets start a root shell in the node's host
- [github.com/distribution/distribution](https://github.com/distribution/distribution) In this repository, you'll find the code for storing and distributing container images using the OCI Distribution Specification. The goal of this project is to provide a simple, secure, and scalable base for building a large-scale registry solution.
- [github.com/flomesh-io/pipy](https://github.com/flomesh-io/pipy) Pipy is a programmable proxy for the cloud, edge and IoT.
    - [blog.flomesh.io: sing Pipy as a Kubernetes policy engine](https://blog.flomesh.io/using-pipy-as-a-kubernetes-policy-engine-e70a23c8d54c)
- [github.com/KWasm/podman-wasm](https://github.com/KWasm/podman-wasm) This repository contains a Podman machine image that can run native WebAssembly container images, which only contain wasm files and no runtime
- [github.com/ibuildthecloud/wtfk8s](https://github.com/ibuildthecloud/wtfk8s) Watch and print changes in k8s. This tool watches kubernetes resources and prints the delta in changes.
- [==github.com/ContainerSSH/ContainerSSH==](https://github.com/ContainerSSH/ContainerSSH) ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects.
- [github.com/Netcracker/KubeMarine](https://github.com/Netcracker/KubeMarine) Management tool for Kubernetes cluster deployment and maintenance. Kubemarine is an open-source, lightweight and powerful management tool built for end-to-end Kubernetes cluster deployment and maintenance
- [github.com/Skarlso/crd-to-sample-yaml](https://github.com/Skarlso/crd-to-sample-yaml) card-to-sample-YAML lets you generate a sample YAML file from a Custom Resource Definition
- [==github.com/alexellis/run-job==](https://github.com/alexellis/run-job) Run a Kubernetes Job and get the logs when it's done 🏃‍♂️
- [github.com/JovianX/Service-Hub](https://github.com/JovianX/Service-Hub) Service Hub is a tool to create and manage a Self-Service portal for your applications using Kubernetes and Helm
- [medium.com/@markcallen_devops: Setup Kubernetes Admin on Linux with Brew](https://medium.com/@markcallen_devops/setup-kubernetes-admin-on-linux-with-brew-da143cef1c90)
- [github.com/ahmetb/kubectl-foreach: kubectl foreach ⭐](https://github.com/ahmetb/kubectl-foreach) kubectl-foreach is a kubectl plugin that runs a kubectl command in one or more contexts (clusters) in parallel (similar to GNU parallel/xargs)
- [github.com/kubernetes-sigs/etcdadm ⭐](https://github.com/kubernetes-sigs/etcdadm) etcdadm is a command-line tool for operating an etcd cluster. It makes it easy to create a new cluster, add a member to, or remove a member from an existing cluster. Its user experience is inspired by kubeadm.
- [infoq.com: Kwok, a Tool to Spin up Kubernetes Nodes in a Second](https://www.infoq.com/news/2023/03/kwok-kubernetes/)
- [==github.com/jetpack-io/launchpad== ⭐](https://github.com/jetpack-io/launchpad) Launchpad is a command-line tool that lets you easily create applications on Kubernetes. In practice, Launchpad works similar to Heroku or Vercel, except everything is on Kubernetes.
- [github.com/OvidiuBorlean/kubectl-sockperf](https://github.com/OvidiuBorlean/kubectl-sockperf) Kubectl Sockperf plugin - Latency Measurement in Kubernetes
- [github.com/oslabs-beta/Ekkremis](https://github.com/oslabs-beta/Ekkremis) This repository contains the code for Ekkremis: a Prometheus-based alert manager to resolve kubernetes pods pending issues
- [==github.com/jonmosco/kube-ps1== ⭐](https://github.com/jonmosco/kube-ps1) Kubernetes prompt for bash and zsh. **kube-ps1 is a script that lets you add the current Kubernetes context and namespace configured on kubectl to your Bash/Zsh prompt strings (i.e. the `$PS1`)**
- [==github.com/cloudnativelabs/kube-shell== ⭐](https://github.com/cloudnativelabs/kube-shell) **Kube-shell is an integrated shell for working with the Kubernetes CLI. Under the hood, Kube-shell still calls kubectl. Kube-shell aims to provide ease-of-use of kubectl and increase productivity.**
- [github.com/DataCater/datacater (real-time, cloud-native data pipeline platform)](https://github.com/DataCater/datacater) The developer-friendly ETL platform for transforming data in real-time. Based on Apache Kafka® and Kubernetes®. DataCater helps you to build modern, real-time data pipelines with Apache Kafka and Kubernetes. You can choose from an extensive repository of filter functions, apply transformations, or code your own transforms in Python.
- [==github.com/alcideio/rbac-tool==](https://github.com/alcideio/rbac-tool) **RBAC Tool for Kubernetes.** Rapid7 | insightCloudSec | Kubernetes RBAC Power Toys - Visualize, Analyze, Generate & Query
- [oslabs-beta/Palaemon](https://github.com/oslabs-beta/Palaemon) Palaemon is an open-source developer tool for monitoring health and resource metrics of Kubernetes clusters and analyzing Out of Memory (OOMKill) errors
- [openobserve/debug-container](https://github.com/openobserve/debug-container) A container with common utilities for debugging your cluster
- [==platformengineering.org/tools/capsule== ⭐](https://platformengineering.org/tools/capsule) Capsule is an open source framework that enables Platform Engineers to build a secure multi-tenant Internal Developer Platform on top of any Kubernetes infrastructure.
- [Ksctl: Cloud Agnostic Kubernetes Management tool](https://github.com/kubesimplify/ksctl) ksctl is a simple multi-environment Kubernetes management CLI tool
- [github.com/ajayk/drifter](https://github.com/ajayk/drifter) Drifter scans your cluster to find configuration drifts on Kubernetes resources or Helm charts
- [github.com/nebuly-ai/nos](https://github.com/nebuly-ai/nos) Module to Automatically maximize the utilization of GPU resources in a Kubernetes cluster through real-time dynamic partitioning and
elastic quotas - Effortless optimization at its finest!
- [github.com/lsdopen/ahoy](https://github.com/lsdopen/ahoy) Ahoy helps teams release and manage applications and services across multiple k8s clusters without needing to write any yaml.
- [github.com/opencontrolplane](https://github.com/opencontrolplane) OpenCP (Open Control Plane) is an open source project designed to provide a single interface to manage infrastructure across providers using a single tool: kubectl
- [github.com/yonahd/orphaned-configmaps: Orphaned ConfigMaps](https://github.com/yonahd/orphaned-configmaps) A script for finding orphaned configmaps
- [github.com/updatecli/updatecli](https://github.com/updatecli/updatecli) A Declarative Dependency Management tool
    - Automatically open a PR on your GitOps repository when a third party service publishes an update
    - Updatecli is a tool used to apply file update strategies. Designed to be used from everywhere, each application "run" detects if a value needs to be updated using a custom strategy then apply changes according to the strategy.
- [==github.com/yonahd/kor==](https://github.com/yonahd/kor) A Golang Tool to discover unused Kubernetes Resources. Currently, Kor can identify and list unused:
    - ConfigMaps
    - Secrets
    - Services
    - ServiceAccounts
    - Deployments
    - Statefulsets
    - Roles
- [granted.dev](https://www.granted.dev) A CLI application which provides the world’s best developer UX for finding and accessing cloud roles to multiple cloud accounts, fast!
- [devtron.ai](https://devtron.ai/) Adopt Kubernetes in Weeks With Our K8s Acceleration Platform. Old software delivery platforms are holding you back and slowing you down. Rapidly adopt K8s without creating cognitive overload for your developers.
- [==github.com/kubefirst/kubefirst==](https://github.com/kubefirst/kubefirst) The Kubefirst CLI creates instant GitOps platforms that integrate some of the best tools in cloud native from scratch in minutes. The Kubefirst CLI is a cloud provisioning tool that creates a kubernetes cluster with automated Infrastructure as Code, GitOps asset management and application delivery, secrets management, and more.
- [github.com/Trolley-MGMT/trolleymgmt](https://github.com/Trolley-MGMT/trolleymgmt) Trolley is a multi cloud Kubernetes management system. A simplified UI which allows the user to Deploy, Edit and Delete clusters and deployments within them on AWS, Azure and GCP.
- [==github.com/akuity/kargo==](https://github.com/akuity/kargo) - [kargo.akuity.io](https://kargo.akuity.io) Application lifecycle orchestration. Kargo is a next-generation continuous delivery and application lifecycle orchestration platform for Kubernetes. It builds upon GitOps principles and integrates with existing technologies, like Argo CD, to streamline and automate the progressive rollout of changes across the many stages of an application's lifecycle.
- [==github.com/Wilfred/difftastic==](https://github.com/Wilfred/difftastic) a structural diff that understands syntax
- [==github.com/kubernetes/git-sync== ⭐](https://github.com/kubernetes/git-sync) **A sidecar app which clones a git repo and keeps it in sync with the upstream.** git-sync is a simple command that pulls a git repository into a local directory. It is a perfect "sidecar" container in Kubernetes - it can periodically pull files down from a repository so that an application can consume them.
- [==github.com/kubepug/kubepug: Deprecations AKA KubePug - Pre UpGrade (Checker)== ⭐](https://github.com/kubepug/kubepug) KubePug/Deprecations is intended to be a kubectl plugin, which:
    - Downloads a generated data.json file containing API deprecation information for a specified release of Kubernetes
    - Scans a running Kubernetes cluster to determine if any objects will be affected by deprication
    - Displays affected objects to the user
- [==github.com/hcavarsan/kftray== ⭐](https://github.com/hcavarsan/kftray) Manage multiple kubectl port-forward commands with a menu bar or a TUI app, with support for UDP and proxy connections through Kubernetes clusters, and gitops-like state sync with github.
- [kondense 🌟](https://github.com/unagex/kondense) Kondense is an automated resource sizing tool. It runs as a sidecar in kubernetes pods.

## kubetail

- [github.com/kubetail-org/kubetail 🌟](https://github.com/kubetail-org/kubetail) **Private, real-time log viewer for Kubernetes**
    - Kubetail is a bash script aggregating (tail/follow) logs from multiple pods into one stream
    - This is the same as running `kubectl logs -f` but for multiple pods
- [Kubetail 🌟](https://github.com/johanhaleby/kubetail) Bash script to tail Kubernetes logs from multiple pods at the same time
- [Stern 🌟](https://github.com/stern/stern) Multi pod and container log tailing for Kubernetes. Stern allows you to tail multiple pods on Kubernetes and multiple containers within the pod. Each result is color coded for quicker debugging -- Friendly fork of https://github.com/wercker/stern

## Portainer

- [github.com/portainer/portainer](https://github.com/portainer/portainer) Making Docker and Kubernetes management easy.

## kubecfg

- [github.com/kubecfg/kubecfg](https://github.com/kubecfg/kubecfg) kubecfg is a tool for managing Kubernetes resources as code that allows you to express the patterns across your infrastructure, reuse "templates" across many services, and then manage those templates as files in version control

## Curl

- [zhimin-wen.medium.com: Curl as a Network Protocol Testing Tool](https://zhimin-wen.medium.com/curl-as-a-network-protocol-testing-tool-7f49151ea365)

## kcp

- https://github.com/kcp-dev/
- [kcp: a prototype of a Kubernetes API server that is not a Kubernetes cluster - a place to create, update, and maintain Kube-like APIs with controllers above or without clusters](https://github.com/kcp-dev/kcp) Kubernetes is mainly known as a container orchestration platform today, but we believe it can be even more. With the power of CustomResourceDefinitions, Kubernetes provides a flexible platform for declarative APIs of all types, and the reconciliation pattern common to Kubernetes controllers is a powerful tool in building robust, expressive systems. At the same time, a diverse and creative community of tools and services has sprung up around Kubernetes APIs. Imagine a declarative Kubernetes-style API for anything, supported by an ecosystem of Kubernetes-aware tooling, separate from Kubernetes-the-container-orchestrator. That's kcp.
- [cloudnativesimplified.substack.com: kcp: Kubernetes-like control plane](https://cloudnativesimplified.substack.com/p/tool-series-1-kcp) kcp is a control plane for workloads on many clusters. In this article, you will explore how to use it to manage multiple tenants:
    - In a single cluster with workspaces (isolated namespaces)
    - In multiple clusters with SyncTarget and Placements

## Clusternet

- [==github.com/clusternet==](https://github.com/clusternet/clusternet) Managing your Kubernetes clusters (including public, private, edge, etc) as easily as visiting the Internet
    - https://clusternet.io/
    - Clusternet (Cluster Internet) is a tool that helps you manage thousands of Kubernetes clusters
    - It can also help deploy and manage applications across several clusters from a single set of APIs in a single hosting cluster

## Open Cluster Management

- [==open-cluster-management.io==](https://open-cluster-management.io/) Make working with many Kubernetes clusters super easy regardless of where they are deployed. Open Cluster Management is a community-driven project focused on multicluster and multicloud scenarios for Kubernetes apps. Open APIs are evolving within this project for cluster registration, work distribution, dynamic placement of policies and workloads, and much more.

## Penetration Testing Tools

- [intellipaat.com: What is Penetration Testing?](https://intellipaat.com/blog/what-is-penetration-testing) Penetration testing is otherwise referred to as pen testing. This blog on ‘What is Penetration Testing? - Types, Phases, Tools Explained’ discusses in detail what pen testing is and how it works, the numerous tools involved in this field, and so on. This blog aims to give you an insight into pen testing and how Ethical Hackers use it for the purpose of Cyber Security. Let’s dive right in.
- [quarkslab/kdigger](https://github.com/quarkslab/kdigger) kdigger is a context discovery tool for Kubernetes penetration testing.
- [inguardians/peirates](https://github.com/inguardians/peirates) Peirates - Kubernetes Penetration Testing tool

## Deckhouse Kubernetes Platform

- [Deckhouse: NoOps Kubernetes platform 🌟](https://github.com/deckhouse/deckhouse) Deckhouse is an Open Source platform for managing Kubernetes clusters in a fully automatic and uniform fashion. It allows you to create homogeneous Kubernetes clusters anywhere and fully manages them. It supplies all the add-ons you need for auto-scaling, observability, security, and service mesh. It comes in Enterprise Edition (EE) and Community Edition (CE).

## KubeIP (GKE)

- [kubeip.com](https://kubeip.com) Many applications need to be whitelisted by users based on a Source IP Address. As of today, Google Kubernetes Engine doesn’t support assigning a static pool of IP addresses to the GKE cluster. Using kubeIP, this problem is solved by assigning GKE nodes external IP addresses from a predefined list. kubeIP monitors the Kubernetes API for new/removed nodes and applies the changes accordingly.
- Many applications need to be whitelisted based on a Source IP Address.
- Using kubeIP, you can assign external IP addresses from a predefined list to GKE nodes. kubeIP monitors the Kubernetes API for new/removed nodes and applies the changes
- [doitintl/kubeIP](https://github.com/doitintl/kubeIP) Assign static external IPs from predefined pool of external IP addresses to Google GKE nodes so your customers could whitelist them

## Porter

- [Porter](https://porter.sh/) Package your application artifact, client tools, configuration and deployment logic together as a versioned bundle that you can distribute, and then install with a single command - [github.com/getporter/porter](https://github.com/getporter/porter)

## Datree. Quality Checks for Kubernetes YAMLs

- [Datree.io](https://www.datree.io/) Datree prevents kubernetes misconfigurations from reaching production. Datree is a CLI solution that supports kubernetes owners in their roles, by preventing developers from making errors in k8s configurations.
- [dev.to: CI With Datree](https://dev.to/thenjdevopsguy/ci-with-datree-4h8d) Learn all about Datree, the leader in Kubernetes static code analysis; Helm chart analysis; and how to ensure that all manifest configurations are working properly in a Continuous Integration (CI) build process. [youtube: CI and Building Code With Datree](https://www.youtube.com/watch?v=2Z5HhEk1zK8&ab_channel=MichaelLevan)
- [dev.to: Automating quality checks for Kubernetes YAMLs](https://dev.to/wkrzywiec/automating-quality-checks-for-kubernetes-yamls-398)

## Kaniko Build Images in Kubernetes without docker

- [Kaniko 🌟](https://github.com/GoogleContainerTools/kaniko) Kaniko is a tool to build container images from a Dockerfile. Unlike Docker, Kaniko doesn’t require the Docker daemon. With the help of Kaniko, you won’t be needing to run docker containers with privileged mode.
- [medium: Multibranch and HA Pipeline in Jenkins with Kaniko on GKE](https://medium.com/searce/multibranch-and-ha-pipeline-in-jenkins-with-kaniko-on-gke-8a1e7fa93403)
- [developers.redhat.com: Perform a kaniko build on a Red Hat OpenShift cluster and push the image to a registry](https://developers.redhat.com/articles/2021/06/18/perform-kaniko-build-red-hat-openshift-cluster-and-push-image-registry)
- [devopscube.com: How To Build Docker Image In Kubernetes Pod 🌟](https://devopscube.com/build-docker-image-kubernetes-pod/)
- [learnsteps.com: Kaniko and how you can build images on Kubernetes using kaniko?](https://www.learnsteps.com/kaniko-and-how-you-can-build-images-on-kubernetes-using-kaniko/)
- [kubesandclouds.com: Kaniko: Building images without Docker](https://kubesandclouds.com/index.php/2021/11/04/kaniko/)
- [blog.rewanthtammana.com: Hardening Kaniko build process with Linux capabilities](https://blog.rewanthtammana.com/hardening-kaniko-build-process-with-linux-capabilities) Build images inside Kubernetes/containers? Wide privileges in default configuration? How to secure Kaniko? Can we take things a notch higher?
- [medium.com/@Mohamed-ElEmam: Build Docker Images in Kubernetes POD Without Docker -Kaniko](https://medium.com/@Mohamed-ElEmam/build-docker-images-in-kubernetes-pod-without-docker-kaniko-46e1a5b76c9)
- [medium.com/@aqsarahman71: Introduction to Kaniko](https://medium.com/@aqsarahman71/introduction-to-kaniko-912e0f494570)

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

- [==dekorate.io== 🌟🌟🌟](http://dekorate.io/) - https://github.com/dekorateio/dekorate
- Dekorate is a collection of Java compile-time generators and decorators for Kubernetes manifests. You can generate a manifest by adding a dependency to the classpath of your project. You can also customize it with an annotation or application property
- One-stop jar to Kubernetes manifest generation that works for all jvm languages regardless of the build tool. It makes generating Kubernetes manifests as easy as adding a dependency to the classpath!
- [developers.redhat.com: Using Dekorate to generate Kubernetes manifests for Java applications](https://developers.redhat.com/blog/2021/03/17/using-dekorate-to-generate-kubernetes-manifests-for-java-applications/)

## Kubesploit

- [github.com/cyberark/kubesploit 🌟](https://github.com/cyberark/kubesploit) Kubesploit is a cross-platform post-exploitation HTTP/2 Command & Control server and agent dedicated for containerized environments written in Golang and built on top of Merlin project
- [cyberark.com: Kubesploit: A New Offensive Tool for Testing Containerized Environments](https://www.cyberark.com/resources/threat-research-blog/kubesploit-a-new-offensive-tool-for-testing-containerized-environments)

## Kubeshop

- [Kubeshop 🌟](https://kubeshop.io/) First in the World Open-Source Accelerator/Incubator focusing on building project for Developers in the Kubernetes space
- [venturebeat.com: Kubeshop wants to be a Kubernetes product pipeline](https://venturebeat.com/2021/09/17/kubeshop-wants-to-be-a-kubernetes-product-pipeline/)

## Monokle

- [==kubeshop/monokle==](https://github.com/kubeshop/monokle) Monokle - your friendly desktop UI for managing k8s manifests!
- [medium.com/kubeshop-i: Monokle 1.5.0 Release](https://medium.com/kubeshop-i/monokle-1-5-0-release-kubeshop-95f574563c79) Monokle by @thekubeshop  is your K8s best friend for creating, validating, debugging and managing manifests! Monokle now provides templates to help you get started with creating resources.
- [kunalkushwaha.com: Manage and debug Kubernetes manifests with Monokle by Kubeshop](https://kunalkushwaha.com/manage-and-debug-kubernetes-manifests-with-monokle-by-kubeshop) **Improve your workflows**
- [youtube: From Code to Cloud: Quality Kubernetes Deployments with Monokle | Cloud Native Islamabad](https://www.youtube.com/watch?v=7IFAg782pf8)
    - Create, debug, and implement OPA validation of the necessary YAML resource manifests for proper
    - See how the application behaves in Prod

## KubeLibrary

- [KubeLibrary](https://github.com/devopsspiral/KubeLibrary) KubeLibrary is a RobotFramework library for testing Kubernetes cluster

## kube-vip

- [kube-vip](https://github.com/kube-vip/kube-vip) is a Load-Balancer for both inside and outside a Kubernetes cluster. kube-vip provides Kubernetes clusters with a virtual IP and load balancer for both the control plane (for building a highly-available cluster) and Kubernetes Services of type LoadBalancer without relying on any external hardware or software.
- **What's one of the biggest pain in implementing Kubernetes for on-prem? Lack of support for LoadBalancer Service.** Now there's a second project (the first is [MetalLB](https://github.com/metallb/metallb)) that provides this functionality for on-prem: kube-vip.

## Kubermetrics

- [oslabs-beta/kubermetrics](https://github.com/oslabs-beta/kubermetrics) Kubermetrics is an open-source dev tool that provides Kubernetes cluster monitoring as well as data visualization in a simple and easy to understand user interface. Kubermetrics intergrates both the Prometheus and Grafana Dashboards on one page! Allowing for custominzable dashboards and alerts.
- [medium: Kubermetrics — Cluster Visualization Made Simple](https://medium.com/@sachem2015/kubermetrics-cluster-visualization-made-simple-d24928f63451)

## Kustomizer

- [kustomizer](https://kustomizer.dev/) Kustomize build, apply, prune command-line utility. Kustomizer is a command-line utility for applying kustomizations on Kubernetes clusters. Kustomizer garbage collector keeps track of the applied resources and prunes the Kubernetes objects that were previously applied on the cluster but are missing from the current revision.

## MetalLB

- [MetalLB](https://github.com/metallb/metallb) A network load-balancer implementation for Kubernetes using standard routing protocols
- [medium.com/@charled.breteche: Kind, Cilium, MetalLB, and still no kube-proxy](https://medium.com/@charled.breteche/kind-cilium-metallb-and-no-kube-proxy-a9fe66ddfad6) In this article I will show you how to add MetalLB into the mix to enable services of type LoadBalancer to work in your local cluster.
- [patrick.easte.rs: Forging an optimal MetalLB configuration](https://patrick.easte.rs/post/2022/forging-optimal-metallb-config/) MetalLB discovers services needing load balancers, allocates IP addresses, and advertises them. There are 2 primary modes for announcing load balancers: Layer 2 and 3 (BGP). Each mode has its pros and cons and this article compares them.
- [adaltas.com: Ingresses and Load Balancers in Kubernetes with MetalLB and nginx-ingress](https://www.adaltas.com/en/2022/09/08/kubernetes-metallb-nginx/) This tutorial will teach you how to use MetalLB and nginx-ingress to  load-balance requests in a bare-metal Kubernetes cluster
- [itnext.io: Configuring routing for MetalLB in L2 mode](https://itnext.io/configuring-routing-for-metallb-in-l2-mode-7ea26e19219e) In this article, you will discover how to configure source-based and policy-based routing for the external network on your cluster using MetalLB

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

## Popeye

- [Popeye - A Kubernetes Cluster Sanitizer 🌟🌟](https://github.com/derailed/popeye) Popeye is a utility that scans live Kubernetes cluster and reports potential issues with deployed resources and configurations. It sanitizes your cluster based on what's deployed and not what's sitting on disk. By scanning your cluster, it detects misconfigurations and helps you to ensure that best practices are in place, thus preventing future headaches. It aims at reducing the cognitive overload one faces when operating a Kubernetes cluster in the wild. Furthermore, if your cluster employs a metric-server, it reports potential resources over/under allocations and attempts to warn you should your cluster run out of capacity.
- [collabnix.com: Top 10 Kubernetes Tools You Need for 2021 – Popeye](https://collabnix.com/top-10-kubernetes-tools-you-need-for-2021/)

## kbrew

- [kbrew](https://github.com/kbrew-dev/kbrew) kbrew is homebrew for Kubernetes. kbrew is a CLI tool for Kubernetes which makes installing any complex stack easy in one step (And yes we are definitely inspired by Homebrew from MacOS)

## KubExplorer

- [Pscheidl/kubexplorer](https://github.com/Pscheidl/kubexplorer) Detects orphan configmaps and secrets in a Kubernetes cluster

## Kubescape

- [==Kubescape== 🌟](https://github.com/kubescape/kubescape) **kubescape is the first tool for testing if Kubernetes is deployed securely as defined in Kubernetes Hardening Guidance by to NSA and CISA.** Tests are configured with YAML files, making this tool easy to update as test specifications evolve.
    - Kubescape is a tool that provides risk analysis, security compliance, RBAC visualizer and image vulnerabilities scanning.
- [armosec.io: Use Kubescape to check if your Kubernetes clusters are exposed to the latest K8s Symlink vulnerability (CVE-2021-25741)](https://www.armosec.io/blog/kubescape-checks-if-kubernetes-exposed-to-k8s-symlink-vulnerability-cve202125741)
- [armosec.io: Kubescape makes {RBAC easy} 🌟](https://www.armosec.io/lp-2-rbac/) Graph all roles, resources, and role-bindings. Run pre-defined queries and reveal RBAC insights. Find who has access to K8s components using NLP-like queries. Perform deep RBAC analysis up to a single role and resource.
- [medium.com/@sheraznadeem1: Kubescape & Kubernetes Hardening- Demystified](https://medium.com/@sheraznadeem1/kubescape-kubernetes-hardening-demystified-87fba47f3b6a)
- [blog.devgenius.io: Scanning Kubernetes YAML Files for Security 🌟](https://blog.devgenius.io/scanning-kubernetes-yaml-files-for-security-e302542b5407)
- [infracloud.io: Securing Kubernetes Cluster using Kubescape and kube-bench](https://www.infracloud.io/blogs/securing-kubernetes-cluster-kubescape-kubebench/) In this article, you will discuss how you can secure a Kubernetes cluster using Kubescape and kube-bench

## Kubectl Connections

- [KubePlus kubectl plugins -> kubectl connections](https://github.com/cloud-ark/kubeplus/blob/master/kubeplus-kubectl-commands.md)
- [cloudark.medium.com: kubectl connections](https://cloudark.medium.com/whats-cooking-in-your-kubernetes-namespace-9200be114f8) that can help you discover and visualize relationship between resources (Deployments, Services, etc.) in your namespace

## Benchmark Operator

- [cloud-bulldozer/benchmark-operator: The Chuck Norris of cloud benchmarks](https://github.com/cloud-bulldozer/benchmark-operator) The intent of this Operator is to deploy common workloads to establish a performance baseline of Kubernetes cluster on your provider.

## Source-To-Image (S2I)

- [openshift/source-to-image](https://github.com/openshift/source-to-image) A tool for building artifacts from source and injecting into container images. Source-to-Image (S2I) is a toolkit and workflow for building reproducible container images from source code. **No writing a bunch of YAML to build your container.**

## VMware Tanzu Octant

- [vmware-tanzu/octant](https://github.com/vmware-tanzu/octant) Highly extensible platform for developers to better understand the complexity of Kubernetes clusters. Octant is a tool for developers to understand how applications run on a Kubernetes cluster. It aims to be part of the developer's toolkit for gaining insight and approaching complexity found in Kubernetes. Octant offers a combination of introspective tooling, cluster navigation, and object management along with a plugin system to further extend its capabilities.

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
- [aws.amazon.com: Using Amazon EC2 Spot Instances with Karpenter](https://aws.amazon.com/blogs/containers/using-amazon-ec2-spot-instances-with-karpenter/) Karpenter is a dynamic, high-performance cluster auto-scaling solution for the Kubernetes platform. In this blog post, we will look at how to use Karpenter with EC2 Spot Instances and handle Spot Instance interruptions.
- [makendran.hashnode.dev: Just-in-time Worker Nodes with Karpenter](https://makendran.hashnode.dev/just-in-time-worker-nodes-with-karpenter) Karpenter is an open source project licensed under the Apache 2.0 license and it is a node-based scaling solution created for K8S. In an AWS EKS cluster, you cannot manage nodes directly. Instead, you have to use additional orchestration mechanisms such as node groups. Unless you use Karpenter — an open-source, flexible, high-performance Kubernetes cluster autoscaler.
- [awstip.com: This Code Works! — Autoscaling An Amazon EKS Cluster with Karpenter — Part 1/3](https://awstip.com/this-code-works-autoscaling-an-amazon-eks-cluster-with-karpenter-part-1-3-40c7bed26cfd) In this three-part series, you will learn how to use Karpenter:
    - Introduction and Karpenter vs Kubernetes Cluster Autoscaler
    - Karpenter deployment guide
    - End-to-end working code to implement a fully functional EKS Cluster
- [dev.to: Karpenter: The Better Autoscaling Solution for Kubernetes- Part 1](https://dev.to/aws-builders/karpenter-the-better-autoscaling-solution-for-kubernetes-part-1-4pd5)
- [medium.com/summit-technology-group: Karpenter — AutoScaling and Right-Sizing EKS Nodes](https://medium.com/summit-technology-group/karpenter-autoscaling-and-right-sizing-eks-nodes-bc6d2b83d48e) Karpenter simplifies node autoscaling and right-sizing for Kubernetes workloads on AWS, resulting in cost savings and easier use of spot instances
- [medium.com/israeli-tech-radar: Karpenter, and the future of Kubernetes](https://medium.com/israeli-tech-radar/karpenter-and-the-future-of-kubernetes-4ab7428b7f87)
- [medium.com/@micheldirk: On Amazon EKS and Karpenter](https://medium.com/@micheldirk/on-amazon-eks-and-karpenter-2b84e75e254e)
- [medium.com/@gajaoncloud: Unleash the Power of Karpenter: Automating AWS EKS Scaling and Cost Optimization](https://medium.com/@gajaoncloud/unleash-the-power-of-karpenter-automating-aws-eks-scaling-and-cost-optimization-7e236319eda4)
- [medium.com/@gajaoncloud: Karpenter Mastery: NodePools & NodeClasses for Workload Nirvana](https://medium.com/@gajaoncloud/karpenter-mastery-nodepools-nodeclasses-for-workload-nirvana-bc89850fa934)
- [medium.com/@gajaoncloud: Demystifying Karpenter’s Advanced Features: Consolidation, Drift, and Spot Handling](https://medium.com/@gajaoncloud/demystifying-karpenters-advanced-features-consolidation-drift-and-spot-handling-007fbad29549) In this article, you will learn about Karpenter's advanced features, such as consolidation for optimal resource utilization, drift detection for automatic updates, and spot instance handling for graceful interruptions

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
- [home.robusta.dev: Why everyone should track Kubernetes changes and top four ways to do so](https://home.robusta.dev/blog/why-everyone-should-track-and-audit-kubernetes-changes-and-top-ways/) Robusta is an event-triggered automations engine. Using Robusta you can subscribe to changes in a cluster (or multiple clusters) and publish that information to useful locations.
- [==robusta-dev/krr==](https://github.com/robusta-dev/krr) Prometheus-based Kubernetes Resource Recommendations. Robusta KRR (Kubernetes Resource Recommender) is a CLI tool for optimizing resource allocation in Kubernetes clusters. It gathers pod usage data from Prometheus and recommends requests and limits for CPU and memory. This reduces costs and improves performance.
- [==blog.devops.dev: How to use the Kubernetes Resource Recommender tool in a GKE Cluster== 🌟](https://blog.devops.dev/how-to-use-the-kubernetes-resource-recommender-tool-in-a-gke-cluster-ef48a6dea85c)

## Soup GitOps Operator

- [caldito/soup](https://github.com/caldito/soup) Soup is a GitOps operator for Kubernetes. GitOps continuous deployment and management tool for Kubernetes focused on simplicity.

## Epinio

- https://epinio.io The Application Development Engine for Kubernetes. Epinio is how you tame the developer workflow in Kubernetes to go from Code to URL in a single step.
- [epinio/epinio](https://github.com/epinio/epinio) Opinionated platform that runs on Kubernetes, that takes you from App to URL in one step.

## Testkube

- [==https://testkube.io== 🌟](https://testkube.io)
- [kubeshop/testkube](https://github.com/kubeshop/testkube) Kubernetes-native framework for test definition and execution
- [thenewstack.io: TestKube: A New Approach to Cloud Native Testing](https://thenewstack.io/testkube-a-new-approach-to-cloud-native-testing/)
- [thenewstack.io: Testkube: A Cloud Native Testing Framework for Kubernetes](https://thenewstack.io/testkube-cloud-native-testing-framework-for-kubernetes/)
- [piotrminkowski.com: Testing Java Apps on Kubernetes with Testkube](https://piotrminkowski.com/2023/11/27/testing-java-apps-on-kubernetes-with-testkube/)

## KuberLogic

- [kuberlogic](https://github.com/kuberlogic/kuberlogic) Kuberlogic is an open-source product that deploys and manages software on top of the Kubernetes cluster and turns infrastructure into a managed PaaS. KuberLogic is that allows running managed databases and popular applications deploying on-premises or at any cloud. The solution provides API, monitoring, backups, and integration with SSO right out of the box

## Kusk

- [kubeshop/kusk: use OpenAPI to configure Kubernetes](https://github.com/kubeshop/kusk) Kusk makes your OpenAPI definition the source of truth for API resources in your cluster. Kusk treats your OpenAPI/Swagger definition as a source of truth for generating supplementary Kubernetes resources for your REST APIs in regard to mappings, security, traffic-control, monitoring, etc.
- [medium.com/kubeshop-i: Rapidly prototype your APIs on Kubernetes with Kusk Gateway — Kubeshop 🌟](https://medium.com/kubeshop-i/rapidly-prototype-your-apis-on-kubernetes-with-kusk-gateway-kubeshop-4006f030e8e4)

## Azure AD Workload Identity

- [==Azure/azure-workload-identity==](https://github.com/Azure/azure-workload-identity) Azure AD Workload Identity uses Kubernetes primitives to associate managed identities for Azure resources and identities in Azure Active Directory (AAD) with pods. It simplifies accessing Azure AD protected resources securely from Kubernetes workloads.

## Kubernate

- https://kubernate.dev
- [laurci/kubernate](https://github.com/laurci/kubernate) Kubernetes+Generate = Kubernate. Kubernate is a Kubernetes YAML generator that can be used as an alternative to other popular tools like Helm. Kubernate is distributed as a library and as a CLI, both working together to achieve one goal: Kubernetes as Code.

## Tackle

- https://www.konveyor.io/tackle
- [redhat.com: How to streamline application portfolio modernization with Tackle](https://www.redhat.com/architect/tackle-application-modernization) Tackle is an open source tool that helps organizations migrate and modernize their application portfolio to leverage Kubernetes without risk of vendor lock-in.

## Azure Placement Policy Scheduler Plugins

- [Azure/placement-policy-scheduler-plugins](https://github.com/Azure/placement-policy-scheduler-plugins) This scheduler enables cluster admins to **offload some configurable percentage of their workloads to spot nodes** enabling them to decrease the cost of running these pods without affecting their reliability.
- Most of cloud environments today provides cluster admins with ephemeral nodes (VMs). These nodes typically cost significantly less but they offer less reliability than their regular counterpart. Cluster admins are often torn between the choice of cost and reliability because of the innate inability of the default Kubernetes scheduler to place some of a specific workload pods on these nodes. Having the entire workload on ephemeral nodes risks the reliability of the workload when the cloud environment stops these nodes. This scheduler enables cluster admins to offload some configurable percentage of their workloads on these nodes enabling them to decrease the cost of running these pods without affecting its reliability.

## Azure AAD Pod Identity

- [Azure/aad-pod-identity)](https://github.com/Azure/aad-pod-identity) Assign Azure Active Directory Identities to Kubernetes applications.

## MicroShift

- [==microshift.io==](https://microshift.io) **MicroShift is a research project that is exploring how OpenShift1 and Kubernetes can be optimized for small form factor and edge computing.**
- It requires only 2GB to run
- You can run it as a container with Docker or Podman
- It is a very trimmed version of OpenShift without many features

## kubefwd (Kube Forward)

- [==txn2/kubefwd==](https://github.com/txn2/kubefwd) Kubernetes port forwarding for local development.
- kubefwd is a tool built to port forward multiple services within one or more namespaces on one or more Kubernetes clusters
- kubefwd uses the same port exposed by the service and forwards it from a loopback IP address on your local workstation

## Kpng. Kubernetes Proxy NG

- [kubernetes-sigs/kpng](https://github.com/kubernetes-sigs/kpng) Reworking kube-proxy's architecture
- [kubernetes.io: Use KPNG to Write Specialized kube-proxiers](https://kubernetes.io/blog/2021/10/18/use-kpng-to-write-specialized-kube-proxiers/) The post will show you how to create a specialized service kube-proxy style network proxier using Kubernetes Proxy NG kpng without interfering with the existing kube-proxy

## Auto-portforward (apf)

- [ruoshan/autoportforward](https://github.com/ruoshan/autoportforward) Bidirectional port-forwarding for docker, podman and kubernetes. A handy tool to automatically set up proxies that expose the remote container's listening ports back to the local machine. Just like kubectl portforward or docker run -p LOCAL:REMOTE, but automatically discover and update the ports to be forwarded on the fly. apf can create listening ports in the container and forward them back as well.

## Gardener

- [==github.com/gardener/gardener: Deliver fully-managed clusters at scale everywhere with your own Kubernetes-as-a-Service==](https://github.com/gardener/gardener) **Homogeneous Kubernetes clusters at scale on any infrastructure using hosted control planes.**
- [gardener/terraformer: Terraformer](https://github.com/gardener/terraformer) Executes Terraform configuration as job/pod inside a Kubernetes cluster. Terraformer is a tool that can execute Terraform commands (apply, destroy and validate) and can be run as a Pod inside a Kubernetes cluster. The Terraform configuration and state files (main.tf, variables.tf, terraform.tfvars and terraform.tfstate) are stored as ConfigMaps and Secrets in the Kubernetes cluster and will be retrieved and updated by Terraformer.

## Werf

- [==werf/werf==](https://github.com/werf/werf)
- The CLI tool gluing Git, Docker, Helm, and Kubernetes with any CI system to implement CI/CD and Giterminism. Werf is an Open Source CLI tool written in Go, designed to simplify and speed up the delivery of applications. To use it, you need to describe the configuration of your application (in other words, how to build and deploy it to Kubernetes) and store it in a Git repo — the latter acts as a single source of truth. In short, that's what we call **GitOps** today.
- A solution for implementing efficient/consistent software delivery to Kubernetes. It covers the entire life cycle of CI/CD and related artifacts, gluing commonly used tools (Git, Docker, Helm, K8s, gitops).
- [werf/kubedog](https://github.com/werf/kubedog) Kubedog is a library to watch and follow Kubernetes resources in CI/CD deploy pipelines. This library is used in the werf CI/CD tool to track resources during deploy process.
- [blog.werf.io: Running one-time tasks and debugging images in the Kubernetes cluster using werf](https://blog.werf.io/running-one-time-tasks-and-debugging-images-in-the-kubernetes-cluster-using-werf-936d6dc483e2)
- [blog.werf.io: werf v1.2 is now stable! Here’s what it is all about](https://blog.werf.io/werf-v1-2-is-now-stable-heres-what-it-is-all-about-832ed647810f) werf is an Open Source CLI tool for building applications and deploying them to Kubernetes clusters. Version 1.2 features many new changes and improvements.
- [blog.werf.io: Deploying Helm charts with dependencies in Kubernetes via werf](https://blog.werf.io/deploying-helm-charts-with-dependencies-in-kubernetes-via-werf-17e5457cdd3f)

## Starboard kubernetes-native security toolkit

- [==aquasecurity/starboard==](https://github.com/aquasecurity/starboard) Kubernetes-native security toolkit. Starboard is a completely open source tool that integrates with other security tools to scan your workloads and make security reports accessible through the Kubernetes API - K8s all the way 🚀

## Netshoot

- [nicolaka/netshoot](https://github.com/nicolaka/netshoot) a Docker + Kubernetes network trouble-shooting swiss-army container. Purpose: Docker and Kubernetes network troubleshooting can become complex. With proper understanding of how Docker and Kubernetes networking works and the right set of tools, you can troubleshoot and resolve these networking issues. The netshoot container has a set of powerful networking tshooting tools that can be used to troubleshoot Docker networking issues. Along with these tools come a set of use-cases that show how this container can be used in real-world scenarios.

## The Hierarchical Namespace Controller (HNC)

- [kubernetes-sigs/hierarchical-namespaces: The Hierarchical Namespace Controller (HNC)](https://github.com/kubernetes-sigs/hierarchical-namespaces) Home of the Hierarchical Namespace Controller (HNC). Adds hierarchical policies and delegated creation to Kubernetes namespaces for improved in-cluster multitenancy.

## Kratix

- [syntasso/kratix](https://github.com/syntasso/kratix) Kratix is a framework for building Platform-as-a-Product.
- Kratix is a framework that enables co-creation of capabilities by providing a clear contract between application and platform teams through the definition and creation of “Promises”. Using the GitOps workflow and Kubernetes-native constructs, Kratix provides a flexible solution to empower your platform team to curate an API-driven, curated, bespoke platform that can easily be kept secure and up-to-date, as well as evolving as business needs change.
- Kratix enables platform teams to deliver a  Kubernetes-native platform API, over fleets of Kubernetes clusters.
- Kratix is deployed to a platform cluster, and uses the GitOps Toolkit to orchestrate a topology of worker clusters.

## gRPC-Gateway

- [grpc-ecosystem/grpc-gateway: gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway) gRPC to JSON proxy generator following the gRPC HTTP spec
- [blog.logrocket.com: An all-in-one guide to gRPC-Gateway](https://blog.logrocket.com/guide-to-grpc-gateway/) gRPC-Gateway is a plugin that generates a reverse proxy server for gRPC services that convert Restful/JSON into gRPC and vice versa.

## KubeOrbit. Test your app on kubernetes

- [teamcode-inc/kubeorbit](https://github.com/teamcode-inc/kubeorbit) Test your application on Kubernetes in a brand new simple way

## Mizu API Traffic Viewer for Kubernetes

- [==up9inc/mizu==](https://github.com/up9inc/mizu) API traffic viewer for Kubernetes enabling you to view all API communication between microservices to help your debug and troubleshoot regressions. Think TCPDump and Wireshark re-invented for Kubernetes.

## vcluster

- [vcluster.com](https://www.vcluster.com) Virtual Kubernetes Clusters that run inside regular namespaces. Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it offers better multi-tenancy and isolation than regular namespaces.
- [thenewstack.io: Locking Down Kubernetes Containers with vcluster](https://thenewstack.io/locking-down-kubernetes-containers-with-vcluster/)
- [salaboy.com: Building platforms on top of Kubernetes: VCluster and Crossplane](https://salaboy.com/2022/08/03/building-platforms-on-top-of-kubernetes-vcluster-and-crossplane/) In this tutorial, you'll learn how to:
    - Create an isolated cluster with vcluster
    - Package apps with Helm
    - Submit a request for a "new environment" that will automatically create a new cluster and install the Helm chart using Crossplane

## Kateyes

- [kateyes.co.uk](https://www.kateyes.co.uk/) Explore Kubernetes, visually! Kateyes is an application that provides a visual representation of the relationships between Kubernetes objects, from an application perspective.
- [blog.devops.dev: Kateyes — Visual Kubernetes Explorer](https://blog.devops.dev/kateyes-visual-kubernetes-explorer-c40510874969) Kubernetes is hard and so is exploring a Kubernetes cluster!

## Keepass Secret

- [rene6502/keepass-secret ](https://github.com/rene6502/keepass-secret) keepass-secret is a command-line tool that converts entries from a KeePass 2.3 file into Kubernetes secrets. This tool was created to automatically create Kubernetes Secret in CI/CD pipelines to deploy workloads to Kubernetes clusters.

## Workflow Schedulers

- [Devtron 🌟](https://github.com/devtron-labs/devtron) is an open source software delivery workflow for kubernetes written in go. Web based CI/CD Platform for Kubernetes.
- [Alcide Advisor: an agentless service for Kubernetes audit and compliance that's built to ensure a frictionless and secured DevSecOps workflow](https://github.com/alcideio/advisor)

### Komodor Workflows

- [komodor.com: Komodor Workflows: Automated Troubleshooting at the Speed of WHOOSH!](https://komodor.com/blog/using-workflows-to-troubleshoot-like-a-pro/)

## Azure Eraser

- [github.com/Azure/eraser 🌟](https://github.com/Azure/eraser) 🧹 Cleaning up images from Kubernetes nodes. **Eraser is a tool that helps Kubernetes admins remove a list of non-running images from all Kubernetes nodes in a cluster**

<center>
[![komodor workflow](images/komodor_workflow.png)](https://komodor.com/blog/using-workflows-to-troubleshoot-like-a-pro/)
</center>

## Data Pipeline Workflow Schedulers

- [apache/dolphinscheduler: Apache DolphinScheduler 🌟](https://github.com/apache/dolphinscheduler) - [dolphinscheduler.apache.org](https://dolphinscheduler.apache.org) is a distributed and extensible workflow scheduler platform with powerful DAG visual interfaces, dedicated to solving complex job dependencies in the data pipeline and providing various types of jobs available out of box.

## ConfigMap Reloader

- https://github.com/stakater/Reloader 🌟
- [medium.com/linux-shots: ConfigMap Reloader — Automatically reload new data from ConfigMap/Secret to deployments](https://medium.com/linux-shots/configmap-secret-reloader-automatically-add-reload-data-from-configmap-secret-to-deployments-dc245e06b92c)
    - ConfigMaps and Secrets are way to inject environment variables and application configurations to a Pod in Kubernetes. Sometimes and sometime many times, we need to change the value of environment variables or configurations. For that we need to update ConfigMap/Secret.
    - In Kubernetes, When we make some changes to a ConfigMap or Secret, new data is not automatically propagated to the pods from that configmap/secret. We often need to restart the pods to load new data.
    - This can be achieved using a tool ‘Reloader’. It is a Kubernetes controller which watch the changes made to secrets and ConfigMaps and perform rolling upgrades on pods with their associated Deployments, StatefulSets or DaemonSets. It is an Opensource tool provided by Stakater who also provide various other enterprise K8s solutions.

## Kluctl

- [kluctl.io 🌟](https://kluctl.io) Kluctl is the missing glue to put together large Kubernetes deployments. It allows you to declare and manage multi-environment and multi-cluster deployments. Kluctl does not have cluster-side dependencies and works out of the box.

## k2tf Kubernetes YAML to Terraform HCL converter

- [==github.com/sl1pm4t/k2tf: Kubernetes YAML to Terraform HCL converter==](https://github.com/sl1pm4t/k2tf)

## Kubernetes Security Tools

- [PaloAltoNetworks/rbac-police](https://github.com/PaloAltoNetworks/rbac-police) RBAC-police is a CLI tool that lets you evaluate the RBAC permissions of service accounts, pods and nodes in Kubernetes clusters through policies written in Rego
- [m9sweeper/m9sweeper](https://github.com/m9sweeper/m9sweeper) m9sweeper is a complete kubernetes security platform that wraps trivy, project falco, kube-bench, kube-hunter, kubesec, and OPA Gatekeeper into one easy to manage user interface.
- [github.com/reddec/keycloak-ext-operator](https://github.com/reddec/keycloak-ext-operator) Creates OAuth clients in Keycloak and creates corresponding secrets in kubernetes

## PureLB

- [purelb/purelb](https://gitlab.com/purelb/purelb) PureLB - is a Service Load Balancer for Kubernetes. PureLB is a load-balancer orchestrator for  Kubernetes clusters. It uses standard Linux networking and routing protocols, and works with the operating system to announce service addresses.

## Murre

- [groundcover-com/murre](https://github.com/groundcover-com/murre) Murre is an on-demand, scaleable source of container resource metrics for K8s.
- [betterprogramming.pub: Dependency-Free Kubernetes Cluster Monitoring](https://betterprogramming.pub/dependency-free-kubernetes-cluster-monitoring-5f7aa2f038d9) Introduce Murre for continued monitoring of Kubernetes containers

## k9s

- [==k9scli.io==](https://k9scli.io) The most essential tool after kubectl. It provides a top like interface to a k8s namespace making it easy to inspect, kill, view logs, or exec and get a shell into your containers.
- [K9s - Kubernetes CLI To Manage Your Clusters In Style!](https://github.com/derailed/k9s) K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.
- [medium.com/@fwiles: k9s EKS Context Error](https://medium.com/@fwiles/k9s-eks-context-error-7ff18df7547f)
- [tonylixu.medium.com: K8s Tools — K9s, Terminal Based UI to Manage Your Cluster](https://tonylixu.medium.com/devops-in-k8s-k9s-terminal-based-ui-to-manage-your-cluster-85b4f147e209) Introduction to K9s CLI, a K8s management tool
- [kubetools.io: Why K9s Should Be Your Go-To Tool for Kubernetes Management](https://www.kubetools.io/kubernetes/why-k9s-should-be-your-go-to-tool-for-kubernetes-management/)
- [medium.com/@gavinklfong: 8 tips to incredibly boost the efficiency of command execution on Kubernetes using k9s](https://medium.com/@gavinklfong/8-tips-to-incredibly-boost-the-efficiency-of-command-execution-on-kubernetes-using-k9s-a515a90a3a27) k9s —awesome text based graphical tool with powerful hotkey design

## Pluto

- [Pluto](https://github.com/FairwindsOps/pluto) A cli tool to help discover deprecated apiVersions in Kubernetes
- [==dev.to: Detecting Kubernetes API Deprecations with pluto==](https://dev.to/fkurz/detecting-kubernetes-api-deprecations-with-pluto-3g2m) Utility to help users find deprecated Kubernetes API versions in their code repositories and their helm releases.

## Konf Lightweight Kubeconfig Manager

- [github.com/SimonTheLeg/konf-go](https://github.com/SimonTheLeg/konf-go) konf is a lightweight kubeconfig manager. With konf you can use different kubeconfigs at the same time. And because it does not need subshells, konf is blazing fast!

## K8spacket

- [github.com/k8spacket/k8spacket](https://github.com/k8spacket/k8spacket) k8spacket - packets traffic visualization for kubernetes. k8spacket helps to understand TCP packets traffic in your kubernetes cluster:
    - Shows traffic between workloads in the cluster
    - Informs where the traffic is routed outside the cluster
    - Displays information about closing sockets by connections

## Infrastructure as Code using Kubernetes. Config Connector

- [==cloud.google.com/config-connector==](https://cloud.google.com/config-connector/docs/overview) Config Connector is an open source Kubernetes addon that allows you to manage Google Cloud resources through Kubernetes.
- [medium.com/globant: Infrastructure as Code using Kubernetes](https://medium.com/globant/infrastructure-as-code-using-kubernetes-d3d329446517)
    - Config Connector (KCC) is a solution to maintain Cloud Resources as Infrastructure as Code. It is built as an Open Source initiative and runs on Kubernetes clusters. As such, it leverages YAML files to maintain and operate such resources.
    - Config Connector has two versions: an Add-On for Google Kubernetes Engine (GKE) clusters and a manual installation for other Kubernetes distributions.

## Claudie Cloud-agnostic managed Kubernetes

- [==github.com/Berops/claudie==](https://github.com/Berops/claudie) Claudie is a platform for managing multi-cloud Kubernetes clusters with each node pools in a different cloud provider

## Observability Monitoring Tools

- [github.com/oslabs-beta/oslabs](https://github.com/oslabs-beta/oslabs) KubernOcular is a free, open-source tool which harnesses the power of Prometheus and the Kubernetes-Client Node API to give developers an insightful and holistic view of Kubernetes clusters.
- [github.com/M3DZIK/go-pingbot](https://github.com/M3DZIK/go-pingbot) This application "pings" websites every few minutes. It can be used to keep the application alive on e.g. glitch.me or repl.it.
- [vladimirvivien/ktop](https://github.com/vladimirvivien/ktop) A top-like tool for your Kubernetes clusters
- [github.com/oslabs-beta/ClusterWatch](https://github.com/oslabs-beta/ClusterWatch) ClusterWatch provides a visualization of the Kubernetes cluster architecture with detailed descriptions and stats. It also offers real-time metrics data, presented via Grafana charts, and built-in support for Prometheus and alerts.

### Debugging and Troubleshooting Tools

- [github.com/JamesTGrant/kubectl-debug](https://github.com/JamesTGrant/kubectl-debug) kubectl-debug is a tool that lets you debug a target container in a Kubernetes cluster by automatically creating a new, non-invasive, 'debug' container in the same PID, network, user, and IPC namespace as the target container without any disruption
- [github.com/AdamRussak/k8f](https://github.com/AdamRussak/k8f) A simple go tool to check that your cluster is in supported version written in GO. k8f is a command line tool to find, list, connect and check versions for kubernetes clusters. With k8f you can connect at once to all clusters tagged as "AWS" or find a specific cluster in your kubeconfig.
- [==github.com/komodorio/validkube==](https://github.com/komodorio/validkube) Validkube combines the best open-source tools to help ensure Kubernetes YAML best practices, hygiene & security
- [github.com/box/kube-iptables-tailer](https://github.com/box/kube-iptables-tailer) A service for better network visibility for your Kubernetes clusters. kube-iptables-tailer is a service that gives you better visibility on networking issues in your Kubernetes cluster by detecting the traffic denied by iptables and surfacing corresponding information to the affected Pods via Kubernetes events.
- [github.com/OvidiuBorlean/kubectl-windumps](https://github.com/OvidiuBorlean/kubectl-windumps) Network traffic capture in AKS Windows Nodes

## Security

- [github.com/controlplaneio/badrobot](https://github.com/controlplaneio/badrobot) Badrobot is a Kubernetes Operator audit tool. It statically analyses manifests for high-risk configurations such as lack of security restrictions on the deployed controller and the permissions of an associated clusterole.
- [==infrahq/infra== 🌟](https://github.com/infrahq/infra) Infra enables you to discover and access infrastructure (e.g. Kubernetes, databases). It helps you connect an identity provider such as Okta or Azure active directory, and map users/groups with the permissions you set to your infrastructure. **Infra provides authentication and access management to servers, clusters, and databases**

## Develop microservices locally while being connected to your Kubernetes environment

- [github.com/we-dcode/kubetunnel](https://github.com/we-dcode/kubetunnel)

## AI Tools

- [kubetools.io: KoPylot: An AI-Powered Kubernetes Assistant for DevOps & Developers](https://www.kubetools.io/kubernetes/kopylot-an-ai-powered-kubernetes-assistant-for-devops-developers/)
- [chat.openai.com: Kube Debugger: A Kubernetes error debugger offering diagnostic and resolution guidance.](https://chat.openai.com/g/g-TCE8R7bcL-kube-debugger) You can copy and paste your Kubernetes error into the prompt, and the Kube debugger will give you step-by-step instructions to troubleshoot. This GPT will reduce the amount of time you spend troubleshooting Kubernetes errors. It requires the ChatGPT plus subscription.

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">One of the biggest problems in IT is that we keep reinventing the wheel.<br><br>We are running the same circles, producing similar technologies to solve the same problems.<br><br>Reinventing the wheel is a great way to learn how the wheel works, but not an efficient way to build software.</p>&mdash; Daniel Moka⚡ (@dmokafa) <a href="https://twitter.com/dmokafa/status/1388448114047164416?ref_src=twsrc%5Etfw">May 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">`kubectl logs --previous` saved my life <a href="https://t.co/mIsCJehVwI">pic.twitter.com/mIsCJehVwI</a></p>&mdash; memenetes (@memenetes) <a href="https://twitter.com/memenetes/status/1425925390644690954?ref_src=twsrc%5Etfw">August 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Tech industry thinks throwing more tools to the problem is the solution. More tools = more failure modes.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1451990747318611968?ref_src=twsrc%5Etfw">October 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Interesting developer tools &amp; frameworks for <a href="https://twitter.com/hashtag/Kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#Kubernetes</a> to learn in 2022:<br>🔹<a href="https://twitter.com/telepresenceio?ref_src=twsrc%5Etfw">@telepresenceio</a> - dev CLI<br>🔹<a href="https://twitter.com/DevSpace?ref_src=twsrc%5Etfw">@DevSpace</a> - dev CLI <br>🔹<a href="https://twitter.com/KnativeProject?ref_src=twsrc%5Etfw">@KnativeProject</a> - <a href="https://twitter.com/hashtag/serverless?src=hash&amp;ref_src=twsrc%5Etfw">#serverless</a> platform<br>🔹<a href="https://twitter.com/skaffolddev?ref_src=twsrc%5Etfw">@skaffolddev</a> - dev CLI<br>🔹<a href="https://twitter.com/hashtag/KubeVela?src=hash&amp;ref_src=twsrc%5Etfw">#KubeVela</a> - <a href="https://twitter.com/oam_dev?ref_src=twsrc%5Etfw">@oam_dev</a> platform<br>🔹<a href="https://twitter.com/okteto?ref_src=twsrc%5Etfw">@okteto</a> - dev platform <br>🔹<a href="https://twitter.com/QuarkusIO?ref_src=twsrc%5Etfw">@QuarkusIO</a> - <a href="https://twitter.com/hashtag/java?src=hash&amp;ref_src=twsrc%5Etfw">#java</a> framework</p>&mdash; Piotr Mińkowski (@piotr_minkowski) <a href="https://twitter.com/piotr_minkowski/status/1475065476388728832?ref_src=twsrc%5Etfw">December 26, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Running tests in Kubernetes using existing CI/CD pipelines can lead to security, performance, and consistency challenges.<br><br>Hear from <a href="https://twitter.com/olensmar?ref_src=twsrc%5Etfw">@olensmar</a>, CTO at <a href="https://twitter.com/thekubeshop?ref_src=twsrc%5Etfw">@thekubeshop</a>, about how <a href="https://twitter.com/Testkube_io?ref_src=twsrc%5Etfw">@Testkube_io</a> can help teams overcome these challenges. <a href="https://t.co/7yMQyiTJjk">pic.twitter.com/7yMQyiTJjk</a></p>&mdash; Kunal Kushwaha (@kunalstwt) <a href="https://twitter.com/kunalstwt/status/1656625448980480001?ref_src=twsrc%5Etfw">May 11, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/CB79eTFbR0w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-168051035-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-168051035-1');
</script>