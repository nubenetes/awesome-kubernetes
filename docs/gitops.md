# GitOps
- [Introduction](#introduction)
- [Git Repositories Structures](#git-repositories-structures)
- [GitOps Tools](#gitops-tools)
	- [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
	- [Kustomize. Kubernetes native configuration management](#kustomize-kubernetes-native-configuration-management)
	- [Flagger](#flagger)
	- [WKSctl. Weave Kubernetes System Control](#wksctl-weave-kubernetes-system-control)
	- [Helm](#helm)
	- [Jenkins](#jenkins)
	- [Terraform](#terraform)
	- [Config Sync and Anthos Config Management](#config-sync-and-anthos-config-management)
	- [Portworx AutoPilot](#portworx-autopilot)
	- [OpenShift Applier](#openshift-applier)
- [GitOps Frameworks](#gitops-frameworks)
- [Kubernetes Platforms and GitOps](#kubernetes-platforms-and-gitops)
	- [OpenShift GitOps](#openshift-gitops)
	- [AWS Kubernetes](#aws-kubernetes)
	- [Weave Kubernetes Platform](#weave-kubernetes-platform)
	- [Ubuntu Charmed Kubernetes](#ubuntu-charmed-kubernetes)

## Introduction
- [gitops.tech](https://www.gitops.tech/)
- [weave.works: Guide to GitOps](https://www.weave.works/technologies/gitops/)
- [weave.works: What Is GitOps?](https://www.weave.works/blog/what-is-gitops-really)
- [atlassian.com: Is GitOps the next big thing in DevOps?](https://www.atlassian.com/git/tutorials/gitops)
- [cloudbees.com: What is GitOps?](https://www.cloudbees.com/gitops/what-is-gitops)
- [dzone: What Is GitOps, Really?](https://dzone.com/articles/what-is-gitops-really) This article will help you understand what GitOps really is as a strategy for development, and its benefits over other CI/CD approaches
- [Continuous GitOps, the way to do DevOps in Kubernetes](https://medium.com/@imarunrk/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster.  
- [thenewstack.io: What Is GitOps and Why It Might Be The Next Big Thing for DevOps](https://thenewstack.io/what-is-gitops-and-why-it-might-be-the-next-big-thing-for-devops/)
- [opensource.substack.com: All You Need To Know About GitOps](https://opensource.substack.com/p/all-you-need-to-know-about-gitops) A complete guide about GitOps, what why and how
- [itnext.io: Continuous GitOps, the way to do DevOps in Kubernetes](https://itnext.io/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster 
- [container-solutions.com: GitOps: The Bad and the Ugly](https://blog.container-solutions.com/gitops-the-bad-and-the-ugly)
- [itnext.io: Principles, Patterns, and Practices for Effective Infrastructure as Code](https://itnext.io/principles-patterns-and-practices-for-effective-infrastructure-as-code-e5f7bbe13df1) Deliver Infrastructure and Software running on it Rapidly and Reliably at Scale.
- [medium: GitOps: Build infrastructure resilient applications 🌟](https://medium.com/@franoisdagostini/gitops-build-infrastructure-resilient-applications-95bbc939046d)
- [itnext.io: Continuous GitOps, the way to do DevOps in Kubernetes 🌟](https://itnext.io/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster.
- [itnext.io: Managing Kubernetes Secrets Securely with GitOps 🌟](https://itnext.io/managing-kubernetes-secrets-securely-with-gitops-b8174b4f4d30)
- [sufle.io: Adopting GitOps for Enhanced Operations](https://www.sufle.io/blog/adopting-gitops-for-enhanced-operations)
- [medium: GitOps : The Next Big Thing for DevOps and Automation!](https://medium.com/searce/gitops-the-next-big-thing-for-devops-and-automation-2a9597e51559) If you have similar questions like: “What’s GitOps?”, “Why we are moving towards this?”, “How and when one can implement this strategy in now running environment?”, “What are the tools it included?” then you have landed on the right page.
- [thenewstack.io: Understanding GitOps: The Latest Tools and Philosophies](https://thenewstack.io/understanding-gitops-the-latest-tools-and-philosophies/)
- [samiyaakhtar.medium.com: GitOps Observability — Visualizing the journey of a container](https://samiyaakhtar.medium.com/gitops-observability-visualizing-the-journey-of-a-container-5f6ef1f3c9d2)
- [clickittech.com: What is GitOps? 🌟](https://www.clickittech.com/devops/what-is-gitops)
- [blog.container-solutions.com: 11 Reasons for Adopting GitOps](https://blog.container-solutions.com/why-adopt-gitops)
- [opensource.com: GitOps vs. DevOps: What's the difference? 🌟](https://opensource.com/article/21/3/gitops) Get to know GitOps, an evolved form of DevOps.
- [geekflare.com: An Introduction to GitOps](https://geekflare.com/gitops-introduction/)
- [thenewstack.io: GitOps Use Cases You May Not Have Considered](https://thenewstack.io/gitops-use-cases-you-may-not-have-considered/)
- [kumomind.medium.com: Should I consider the GitOps methodology?](https://kumomind.medium.com/should-i-consider-the-gitops-methodology-f49e042b8c22)
- [dzone: GitOps: How to Ops Your Git the Right Way 🌟](https://dzone.com/articles/gitops-how-to-ops-your-git-the-right-way) In this article we’ll look into the specifics of creating Git repositories structures  —  the very core of the GitOps approach.
- [braindose.blog: 4 Key Characteristics for a Successful GitOps Implementation](https://braindose.blog/2020/03/18/4-key-characteristics-of-gitops/)
- [blog.container-solutions.com: GitOps: The Bad and the Ugly](https://blog.container-solutions.com/gitops-limitations)

## Git Repositories Structures
- [GitOps: How to Ops Your Git the Right Way 🌟](https://dzone.com/articles/gitops-how-to-ops-your-git-the-right-way) In this article we’ll look into the specifics of creating Git repositories structures  —  the very core of the GitOps approach.

## GitOps Tools
- [FluxCD, ArgoCD or Jenkins X: Which Is the Right GitOps Tool for You?](https://blog.container-solutions.com/fluxcd-argocd-or-jenkins-x-which-is-the-right-gitops-tool-for-you)
- [slideshare: GitOps, Jenkins X & Future of CI/CD](https://slideshare.net/rakutentech/gitops-jenkins-x-future-of-cicd)
- [kubesandclouds.com: Werf: Fully customizable GitOps](https://kubesandclouds.com/index.php/2020/09/01/werf-gitops/)
- [searchitoperations.techtarget.com: GitOps pros grapple with Kubernetes configuration management. GitOps users seek ideal Kubernetes config tool 🌟](https://searchitoperations.techtarget.com/news/252492459/GitOps-pros-grapple-with-Kubernetes-configuration-management) Configuration management challenges GitOps early adopters, especially at large enterprises with millions of lines of Kubernetes YAML to manage. Ultimately, the industry hasn't found an ideal approach to Kubernetes configuration management, especially for GitOps.
	- [Tanka](https://tanka.dev/tutorial/jsonnet) a utility that blends Helm charts with Jsonnet, which combines the deployment speed and ubiquity of Helm charts with the more granular customizability supported by Jsonnet.
- [openshift.com: Announcing OpenShift GitOps](https://www.openshift.com/blog/announcing-openshift-gitops)
- [ibm.com: Enable GitOps](https://www.ibm.com/garage/method/practices/run/gitops/) GitOps focuses on the Ops side of DevOps and shows how operations configurations, infrastructures, and actions are like software. Everything is code and code is managed with Git.

### Flux. The GitOps Operator for Kubernetes
- [Flux](https://fluxcd.io/) The GitOps operator for Kubernetes
- [github: Flux](https://github.com/fluxcd/flux)
- [github: Flux Version 2](https://github.com/fluxcd/flux2)
- [toolkit.fluxcd.io: GitOps Toolkit 🌟](https://toolkit.fluxcd.io/) Great docs for the GitOps toolkit 
    - https://github.com/fluxcd/toolkit
- [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.
- [A Complete Step by Step Guide to Implementing a GitOps Workflow with Flux 🌟](https://managedkube.com/gitops/flux/weaveworks/guide/tutorial/2020/05/01/a-complete-step-by-step-guide-to-implementing-a-gitops-workflow-with-flux.html) 
- [itnext.io: Managing Kubernetes Secrets Securely with GitOps (SOPS + AWS KMS + Flux)](https://itnext.io/managing-kubernetes-secrets-securely-with-gitops-b8174b4f4d30)
- [acloudguru.com: Adopting GitOps for Kubernetes on AWS 🌟](https://acloudguru.com/blog/engineering/adopting-gitops-for-kubernetes-on-aws?utm_source=linkedin&utm_medium=social&utm_campaign=kubernetesblog) Tips for adopting GitOps for your Kubernetes workload in AWS: 
	- Use Git as your source of truth
	- Use a Git branch per environment
	- Practice proper change management
	- Roll back with Git
	- Automate everything
- [blog.sldk.de: Introduction to GitOps on Kubernetes with Flux v2 🌟](https://blog.sldk.de/2021/02/introduction-to-gitops-on-kubernetes-with-flux-v2/)
- [docs.microsoft.com: Configurations and GitOps with Azure Arc enabled Kubernetes](https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-configurations)
- [cloud-viadee.medium.com: GitOps for IT-Architects: Transparent and Secure Kubernetes deployments](https://cloud-viadee.medium.com/gitops-for-it-architects-6312e7822819)
- [johnclarke73.medium.com: How GitOps works for us](https://johnclarke73.medium.com/our-continuous-delivery-journey-11d86dd68a49) From manually deployed monoliths to containers and GitOps with Weaveworks Flux

### Kustomize. Kubernetes native configuration management
- [kustomize.io 🌟](https://kustomize.io/) Kustomize introduces a template-free way to customize application configuration that simplifies the use of off-the-shelf applications. Now, built into kubectl as apply -k.

### Flagger
- [Flagger](https://flagger.app/) Progressive Delivery Operator for Kubernetes. Release new versions of your application/services to Kubernetes like a pro with 
Weaveworks's Flagger.
- [partlycloudy.blog: Release to Kubernetes like a Pro with Flagger](https://partlycloudy.blog/2020/07/08/release-to-k8s-like-a-pro-with-flagger/)

### WKSctl. Weave Kubernetes System Control
* [Weave Kubernetes System Control - wksctl](https://github.com/weaveworks/wksctl) Open Source Weaveworks Kubernetes System
* [WKSctl - A New OSS Kubernetes Manager using GitOps](https://www.weave.works/blog/wksctl-a-new-oss-kubernetes-manager-using-gitops)
* [WKSctl: a Tool for Kubernetes Cluster Management Using GitOps](https://www.infoq.com/news/2020/02/wksctl-kubernetes-gitops/)

### Helm
* [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)

### Jenkins
- There are many tools in the market that have been technically built for GitOps, like [ArgoCD](https://argoproj.github.io/argo-cd/), [Flux](https://github.com/fluxcd/flux), and [Jenkins X](https://jenkins-x.io/). All these tools have in-built proficiency to implement GitOps process for you. But we are going to use our old beloved Jenkins.
- [GitOps for Kubernetes with Jenkins](https://medium.com/stakater/gitops-for-kubernetes-with-jenkins-7db6304216e0)
    - [github.com/stakater/Xposer](https://github.com/stakater/Xposer) (with fabric8 java client library for kubernetes)
- [GitOps with Jenkins and Kubernetes](https://medium.com/@abhishekbhardwaj510/gitops-with-jenkins-and-kubernetes-c20425244c73)
    - [github.com: Opstree-Go-WebApp](https://github.com/opstree/Opstree-Go-WebApp) A loaded GoLang app to do various DevOps POC's
    - [opstree.github.io](https://opstree.github.io/)

### Terraform
- [How to Create a GitOps Workflow with Terraform and Jenkins](https://www.hashicorp.com/resources/how-create-gitops-workflow-terraform-jenkins/)

### Config Sync and Anthos Config Management 
- [Config Sync](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/overview)
- [Anthos Config Management](https://cloud.google.com/anthos/config-management)
- Google built a tool called [Config Sync](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/overview) which acts as the bridge between an external source code repository and the Kubernetes API server. [Anthos Config Management](https://cloud.google.com/anthos/config-management) is based on Config Sync to extend it to multicluster scenarios.

### Portworx AutoPilot
- [Portworx AutoPilot](https://docs.portworx.com/portworx-install-with-kubernetes/autopilot/)
- [portworx.com: Automating Kubernetes Data Management with GitOps & AutoPilot](https://portworx.com/automating-kubernetes-data-management-with-gitops-autopilot)

### OpenShift Applier
- [openshift-applier](https://github.com/redhat-cop/openshift-applier)
- [dzone: GitOps With OpenShift Applier 🌟](https://dzone.com/articles/gitops-with-openshift-applier) GitOps in short is a set of practices to use Git pull requests to manage infrastructure and application configurations.

## GitOps Frameworks
- [dzone: Why Now Is the Time for the Spring Boot of Infrastructure Automation 🌟](https://dzone.com/articles/why-now-is-the-time-for-the-spring-boot-of-infrast) Application teams move fast using frameworks built to boost developer productivity. Learn how a productivity framework can help your DevOps initiative succeed.
- [Kubestack 🌟](https://www.kubestack.com/): [Doc:](https://www.kubestack.com/framework/documentation) Kubestack is an open-source GitOps framework for infrastructure automation built on Terraform and Kustomize. It’s designed for teams that want to automate Kubernetes based infrastructure and not reinvent automation. Think of it this way, Kubestack is to Terraform and infrastructure automation, what Spring Boot is to Java and cloud native applications. The framework supports all three major cloud providers and has been used as the foundation for a number of real world customer projects as part of my colleagues’ and my consulting work. It is fully documented, has a step-by-step tutorial to help users get started and even includes a local [GitOps development lab](https://www.kubestack.com/framework/documentation/tutorial-build-local-lab). So you can test-drive Kubestack and learn more about GitOps for infrastructure automation in the comfort of your own localhost.
	- [thenewstack.io: KubeStack: Towards Full-Stack GitOps](https://thenewstack.io/kubestack-towards-full-stack-gitops/)

## Kubernetes Platforms and GitOps
### OpenShift GitOps
* [blog.openshift.com: Introduction to GitOps with OpenShift](https://blog.openshift.comintroduction-to-gitops-with-openshift/)
* [learn.openshift.com: GitOps introduction](https://learn.openshift.com/introduction/gitops-introduction/)
* [blog.openshift.com: is it too late to integrate GitOps?](https://blog.openshift.comis-it-too-late-to-integrate-gitops/)
* [blog.openshift.com: OpenShift Authentication Integration with ArgoCD](https://blogopenshift.com/openshift-authentication-integration-with-argocd/)
* [openshift.com: From Code to Production with GitOps, Tekton and ArgoCD](https://www.openshift.com/blog/from-code-to-production-with-gitops)
* [medium: GitOps with Istio, Tekton and Argo CD — on OpenShift 4](https://medium.com/@joelkaplan1/gitops-with-istio-tekton-and-argo-cd-on-openshift-4-5e42d22994e3)

### AWS Kubernetes
* [info.acloud.guru: Adopting GitOps for Kubernetes on AWS](https://info.acloud.guru/resources/deploying-kubernetes-with-gitops)

### Weave Kubernetes Platform
* [weave.works: Weave Kubernetes Platform](https://www.weave.works/) Automate Enterprise Kubernetes the GitOps way
* [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave)

### Ubuntu Charmed Kubernetes
* [Charmed Kubernetes](https://ubuntu.com/kubernetes/features)
* [Kubernetes GitOps with Azure Arc and Charmed Kubernetes](https://ubuntu.com/blog/gitops-with-azure-arc-and-charmed-kubernetes)

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: What is GitOps?<br><br>Is this something that you should learn?<br><br>Let&#39;s dive into it. <a href="https://t.co/hsMUesvP23">pic.twitter.com/hsMUesvP23</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1288469479693803525?ref_src=twsrc%5Etfw">July 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>