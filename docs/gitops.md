# GitOps
- [Introduction](#introduction)
- [Git Repositories Structures](#git-repositories-structures)
- [GitOps Tools](#gitops-tools)
    - [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
    - [WKSctl. Weave Kubernetes System Control](#wksctl-weave-kubernetes-system-control)
    - [Helm](#helm)
    - [Jenkins](#jenkins)
    - [Terraform](#terraform)
- [Kubernetes Platforms and GitOps](#kubernetes-platforms-and-gitops)
    - [OpenShift GitOps](#openshift-gitops)
    - [Weave Kubernetes Platform](#weave-kubernetes-platform)
    - [Ubuntu Charmed Kubernetes](#ubuntu-charmed-kubernetes)

## Introduction
- [gitops.tech](https://www.gitops.tech/)
- [weave.works: Guide to GitOps](https://www.weave.works/technologies/gitops/)
- [weave.works: What Is GitOps?](https://www.weave.works/blog/what-is-gitops-really)
- [atlassian.com: Is GitOps the next big thing in DevOps?](https://www.atlassian.com/git/tutorials/gitops)
- [cloudbees.com: What is GitOps?](https://www.cloudbees.com/gitops/what-is-gitops)
- [dzone: What Is GitOps, Really?](https://dzone.com/articles/what-is-gitops-really) This article will help you understand what GitOps really is as a strategy for development, and its benefits over other CI/CD approaches
- [Continuous GitOps, the way to do DevOps in Kubernetes](https://medium.com/@imarunrk/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster  

## Git Repositories Structures
- [GitOps: How to Ops Your Git the Right Way 🌟](https://dzone.com/articles/gitops-how-to-ops-your-git-the-right-way) In this article we’ll look into the specifics of creating Git repositories structures  —  the very core of the GitOps approach.

## GitOps Tools
- [FluxCD, ArgoCD or Jenkins X: Which Is the Right GitOps Tool for You?](https://blog.container-solutions.com/fluxcd-argocd-or-jenkins-x-which-is-the-right-gitops-tool-for-you)
- [slideshare: GitOps, Jenkins X & Future of CI/CD](https://slideshare.net/rakutentech/gitops-jenkins-x-future-of-cicd)

### Flux. The GitOps Operator for Kubernetes
* [Flux](https://fluxcd.io/) The GitOps operator for Kubernetes
* [github: Flux CD](https://github.com/fluxcd/flux)
* [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.

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

## Kubernetes Platforms and GitOps
### OpenShift GitOps
* [blog.openshift.com: Introduction to GitOps with OpenShift](https://blog.openshift.comintroduction-to-gitops-with-openshift/)
* [learn.openshift.com: GitOps introduction](https://learn.openshift.com/introduction/gitops-introduction/)
* [blog.openshift.com: is it too late to integrate GitOps?](https://blog.openshift.comis-it-too-late-to-integrate-gitops/)
* [blog.openshift.com: OpenShift Authentication Integration with ArgoCD](https://blogopenshift.com/openshift-authentication-integration-with-argocd/)
* [openshift.com: From Code to Production with GitOps, Tekton and ArgoCD](https://www.openshift.com/blog/from-code-to-production-with-gitops)

### Weave Kubernetes Platform
* [weave.works: Weave Kubernetes Platform](https://www.weave.works/) Automate Enterprise Kubernetes the GitOps way
* [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave)

### Ubuntu Charmed Kubernetes
* [Charmed Kubernetes](https://ubuntu.com/kubernetes/features)
* [Kubernetes GitOps with Azure Arc and Charmed Kubernetes](https://ubuntu.com/blog/gitops-with-azure-arc-and-charmed-kubernetes)