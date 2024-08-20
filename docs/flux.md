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
- [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.
- [A Complete Step by Step Guide to Implementing a GitOps Workflow with Flux 🌟](https://managedkube.com/gitops/flux/weaveworks/guide/tutorial/2020/05/01/a-complete-step-by-step-guide-to-implementing-a-gitops-workflow-with-flux.html)
- [alicegg.tech: Managing a Kubernetes cluster with Helm and FluxCD](https://alicegg.tech/2020/11/09/helm.html)
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
- [thenewstack.io: GitOps at Home: Automate Code Deploys with Kubernetes and Flux](https://thenewstack.io/gitops-at-home-automate-code-deploys-with-kubernetes-and-flux/)
- [medium: Integrating GitOps Deployments in Kubernetes Using Weave Flux](https://medium.com/contino-engineering/integrating-gitops-deployments-in-kubernetes-using-weave-flux-9a617ea17684)
- [alexander.holbreich.org: (Typical) journey towards full GitOps with Flux](https://alexander.holbreich.org/gitops-journey) The 3 stages of GitOps:
    - Repository
    - Deployment with a script
    - Flux
- [cncf.io: Flux: Server-side reconciliation is coming](https://www.cncf.io/blog/2021/10/07/server-side-reconciliation-is-coming/) Server-side reconciliation will make Flux more performant, improve overall observability and going forward will allow us to add new capabilities, like being able to preview local changes to manifests without pushing to upstream.
- [shipa.io: FluxCD and GitOps in the Enterprise](https://shipa.io/2021/10/fluxcd-and-gitops-in-the-enterprise/)
- [solo.io: The 3 best ways to use Flux and Flagger for GitOps with your Envoy Proxy API gateways](https://www.solo.io/blog/the-3-best-ways-to-use-flux-and-flagger-for-gitops-with-your-envoy-proxy-api-gateways)
- [fluxcd/flux2-multi-tenancy](https://github.com/fluxcd/flux2-multi-tenancy) Manage multi-tenant clusters with Flux
- [==flux-subsystem-argo.github.io: GitOps Terraform Resources with Argo CD and Flux Subsystem for Argo==](https://flux-subsystem-argo.github.io/website/tutorials/terraform/) This is a tutorial to show how could we use Flux Subsystem for Argo (FSA) to bring the Terraform management feature from the Flux world to your Argo CD UI. In order to do so, we need Weave GitOps Terraform Controller to help us reconcile our Terraform resources.
- [blog.ediri.io: Flux With Buckets: Is This Still GitOps?](https://blog.ediri.io/flux-with-buckets-is-this-still-gitops) How to use the Flux Bucket component with AWS S3 with Civo and Pulumi. Flux Bucket is a simple way to deploy your kubernetes manifests to a S3 bucket and then use Flux to deploy them
    - [dirien/pulumi-civo-flux-bucket](https://github.com/dirien/pulumi-civo-flux-bucket)
- [fluxcd.io: GitOps Without Leaving your IDE](https://fluxcd.io/blog/2022/09/gitops-without-leaving-your-ide/)
- [fluxcd.io: How to GitOps Your Terraform](https://fluxcd.io/blog/2022/09/how-to-gitops-your-terraform/)
- [thenewstack.io: Deploy Stateful Workloads on Kubernetes with Ondat and FluxCD](https://thenewstack.io/deploy-stateful-workloads-on-kubernetes-with-ondat-and-fluxcd/) GitOps provides a single source of truth for Kubernetes manifests, preventing configuration drift, allowing easy rollbacks and changes to production safely.
- [==gist.github.com: GitOps for Helm Users== 🌟](https://gist.github.com/scottrigby/a1a42c3292ec7899837c578ffdaaf92a) In this step-by-step tutorial, you will learn how to convert a Helm chart into declarative Custom Resources for Flux and gradually migrate your workloads to be GitOps-friendly.
- [levelup.gitconnected.com: Flux CD: Getting Started](https://levelup.gitconnected.com/flux-cd-getting-started-1a06671d718f) This concise tutorial will show you to bootstrap Flux CD on your local cluster and deploy your applications from your GitHub repository.
- [weave.works: Flamingo: Expand Argo CD with Flux](https://www.weave.works/blog/flamingo-expand-argo-cd-with-flux)

## ArgoCD vs FluxCD

- [dzone.com: GitOps: Flux vs Argo CD 🌟](https://dzone.com/articles/gitops-flux-vs-argo-cd)
- [blog.aenix.io: Argo CD vs Flux CD](https://blog.aenix.io/argo-cd-vs-flux-cd-7b1d67a246ca) In this article, Andrei shares his professional experience and compares two popular GitOps tools: Argo CD and Flux CD. He explores their features, use cases, and the specific problems they solve.

## Flux Terraform Controller

- [weaveworks.github.io: Weave GitOps Terraform Controller](https://weaveworks.github.io/tf-controller/)
- [cncf.io: How to GitOps your Terraform](https://www.cncf.io/blog/2022/09/30/how-to-gitops-your-terraform/)
- [github.com/flux-iac/tofu-controller](https://github.com/flux-iac/tofu-controller) Tofu Controller: An IAC Controller for Flux. A GitOps OpenTofu and Terraform controller for Flux. GitOps Terraform Controller is a controller for Flux to reconcile Terraform resources in the GitOps way

## Templates

- [github.com/onedr0p/flux-cluster-template: Template for deploying k3s backed by Flux](https://github.com/onedr0p/flux-cluster-template) Highly opinionated template for deploying a single Kubernetes (k3s) cluster with Ansible and Terraform backed by Flux, SOPS, GitHub Actions, Renovate and more!
