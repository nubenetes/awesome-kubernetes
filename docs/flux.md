# Flux. The GitOps operator for Kubernetes

1. [Introduction](#introduction)
2. [ArgoCD vs FluxCD](#argocd-vs-fluxcd)
3. [Flux Terraform Controller](#flux-terraform-controller)
4. [Templates](#templates)

## Introduction

- [Flux](https://fluxcd.io/) The GitOps operator for Kubernetes
- [docs.fluxcd.io](https://docs.fluxcd.io/)
- [github: Flux](https://github.com/fluxcd/flux)
- [github: Flux Version 2](https://github.com/fluxcd/flux2)
- [toolkit.fluxcd.io: GitOps Toolkit 🌟](https://toolkit.fluxcd.io/) Great docs for the GitOps toolkit
    - https://github.com/fluxcd/toolkit
- [A Complete Step by Step Guide to Implementing a GitOps Workflow with Flux 🌟](https://managedkube.com/gitops/flux/weaveworks/guide/tutorial/2020/05/01/a-complete-step-by-step-guide-to-implementing-a-gitops-workflow-with-flux.html)
- [alicegg.tech: Managing a Kubernetes cluster with Helm and FluxCD](https://alicegg.tech/2020/11/09/helm.html)
- [acloudguru.com: Adopting GitOps for Kubernetes on AWS 🌟](https://acloudguru.com/blog/engineering/adopting-gitops-for-kubernetes-on-aws?utm_source=linkedin&utm_medium=social&utm_campaign=kubernetesblog) Tips for adopting GitOps for your Kubernetes workload in AWS:
    - Use Git as your source of truth
    - Use a Git branch per environment
    - Practice proper change management
    - Roll back with Git
    - Automate everything
- [blog.sldk.de: Introduction to GitOps on Kubernetes with Flux v2 🌟](https://blog.sldk.de/2021/02/introduction-to-gitops-on-kubernetes-with-flux-v2/)
- [docs.microsoft.com: Configurations and GitOps with Azure Arc enabled Kubernetes](https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-configurations)
- [thenewstack.io: GitOps at Home: Automate Code Deploys with Kubernetes and Flux](https://thenewstack.io/gitops-at-home-automate-code-deploys-with-kubernetes-and-flux/)
- [alexander.holbreich.org: (Typical) journey towards full GitOps with Flux](https://alexander.holbreich.org/gitops-journey) The 3 stages of GitOps:
    - Repository
    - Deployment with a script
    - Flux
- [solo.io: The 3 best ways to use Flux and Flagger for GitOps with your Envoy Proxy API gateways](https://www.solo.io/blog/the-3-best-ways-to-use-flux-and-flagger-for-gitops-with-your-envoy-proxy-api-gateways)
- [fluxcd/flux2-multi-tenancy](https://github.com/fluxcd/flux2-multi-tenancy) Manage multi-tenant clusters with Flux
- [==flux-subsystem-argo.github.io: GitOps Terraform Resources with Argo CD and Flux Subsystem for Argo==](https://flux-subsystem-argo.github.io/website/tutorials/terraform/) This is a tutorial to show how could we use Flux Subsystem for Argo (FSA) to bring the Terraform management feature from the Flux world to your Argo CD UI. In order to do so, we need Weave GitOps Terraform Controller to help us reconcile our Terraform resources.
    - [dirien/pulumi-civo-flux-bucket](https://github.com/dirien/pulumi-civo-flux-bucket)
- [fluxcd.io: GitOps Without Leaving your IDE](https://fluxcd.io/blog/2022/09/gitops-without-leaving-your-ide/)
- [fluxcd.io: How to GitOps Your Terraform](https://fluxcd.io/blog/2022/09/how-to-gitops-your-terraform/)
- [thenewstack.io: Deploy Stateful Workloads on Kubernetes with Ondat and FluxCD](https://thenewstack.io/deploy-stateful-workloads-on-kubernetes-with-ondat-and-fluxcd/) GitOps provides a single source of truth for Kubernetes manifests, preventing configuration drift, allowing easy rollbacks and changes to production safely.
- [==gist.github.com: GitOps for Helm Users== 🌟](https://gist.github.com/scottrigby/a1a42c3292ec7899837c578ffdaaf92a) In this step-by-step tutorial, you will learn how to convert a Helm chart into declarative Custom Resources for Flux and gradually migrate your workloads to be GitOps-friendly.
- [weave.works: Flamingo: Expand Argo CD with Flux](https://www.weave.works/blog/flamingo-expand-argo-cd-with-flux)

## ArgoCD vs FluxCD


## Flux Terraform Controller

- [github.com/flux-iac/tofu-controller](https://github.com/flux-iac/tofu-controller) Tofu Controller: An IAC Controller for Flux. A GitOps OpenTofu and Terraform controller for Flux. GitOps Terraform Controller is a controller for Flux to reconcile Terraform resources in the GitOps way

## Templates

- [github.com/onedr0p/flux-cluster-template: Template for deploying k3s backed by Flux](https://github.com/onedr0p/flux-cluster-template) Highly opinionated template for deploying a single Kubernetes (k3s) cluster with Ansible and Terraform backed by Flux, SOPS, GitHub Actions, Renovate and more!