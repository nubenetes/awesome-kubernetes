# Argo Declarative GitOps for Kubernetes

1. [Introduction](#introduction)
2. [Argo CD](#argo-cd)
3. [Argo CD Vulnerabilities](#argo-cd-vulnerabilities)
4. [Argo CD Tools and Plugins](#argo-cd-tools-and-plugins)
5. [Argo Rollouts](#argo-rollouts)
6. [Argo Workflows](#argo-workflows)
7. [Videos](#videos)

## Introduction

- [argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework](https://argoproj.github.io/argo-events/) Argo Events is an event-driven workflow automation framework for Kubernetes which helps you trigger K8s objects, Argo Workflows, Serverless workloads, etc. on events from a variety of sources like webhooks, S3, schedules, messaging queues, etc.
- [Why and when do you need Argo CD?](https://mkdev.me/posts/why-and-when-do-you-need-argo-cd) High-level explanation of in which cases Argo CD makes sense and what you should keep in mind if you want to use it.

## Argo CD

- [argoproj.github.io: Argo CD - Declarative GitOps for Kubernetes](https://argoproj.github.io/argo-cd/)
- [youtube: GitOps with Argo-CD & Kubernetes](https://www.youtube.com/watch?v=QrLwFEXvxbo&ab_channel=HoussemDellai)
- [openshift.com: OpenShift Authentication Integration with ArgoCD](https://www.openshift.com/blog/openshift-authentication-integration-with-argocd)
- [thenewstack.io: Applied GitOps with ArgoCD](https://thenewstack.io/applied-gitops-with-argocd/)
- [thenewstack.io: Why ArgoCD Is the Lifeline of GitOps](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/)
- [openshift.com: Getting Started with ApplicationSets](https://www.openshift.com/blog/getting-started-with-applicationsets) "App of Apps" pattern.
- [opensource.com: Automatically create multiple applications in Argo CD](https://opensource.com/article/21/7/automating-argo-cd)
- [cloud.redhat.com: How to Use ArgoCD Deployments with GitHub Tokens](https://cloud.redhat.com/blog/how-to-use-argocd-deployments-with-github-tokens)
- [==thenewstack.io: GitOps on Kubernetes: Deciding Between Argo CD and Flux==](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux)
- [digitalocean.com: How to Deploy to Kubernetes using Argo CD and GitOps](https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops)
- [aws.amazon.com: Cloud Native CI/CD with Tekton and ArgoCD on AWS](https://aws.amazon.com/blogs/containers/cloud-native-ci-cd-with-tekton-and-argocd-on-aws/)
- [blog.getambassador.io: GitOps in Kubernetes with ArgoCD](https://blog.getambassador.io/gitops-in-kubernetes-with-argocd-c6ea0e510741)
- [dev.to: Towards a Modular DevOps Stack](https://dev.to/camptocamp-ops/towards-a-modular-devops-stack-257c) In this article, you will learn how to **modularize your infrastructure using Terraform and ArgoCD**
- [datree.io: ArgoCD Best Practices](https://datree.io/resources/argocd-best-practices-you-should-know) In this article, you'll explore some best practices for ArgoCD:
    - Disallow providing an empty retryStrategy
    - Ensure that Workflow pods are not configured to use the default service account
    - Ensure retry on both Error and TransientError
- [piotrminkowski.com: Manage Kubernetes Cluster with Terraform and Argo CD. Create Kakfa Cluster using GitOps 🌟](https://piotrminkowski.com/2022/06/28/manage-kubernetes-cluster-with-terraform-and-argo-cd/) This article shows how to create and manage Kubernetes (Kind) cluster with Terraform and Argo CD, and install Kafka on it. Terraform is very useful for automating infrastructure. On the other hand, Argo CD helps us implement GitOps and continuous delivery for our applications. It seems that we can successfully combine both these tools. Let’s consider how they can help us to work with Kubernetes in the GitOps style.
- [datree.io: ArgoCD Best Practices You Should Know](https://www.datree.io/resources/argocd-best-practices-you-should-know) In this article, you'll explore some best practices for ArgoCD:
    - Disallow providing an empty retryStrategy
    - Ensure that Workflow pods are not configured to use the default service account
    - Ensure retry on both Error and TransientError

- [kubebyexample.com: Argo CD Overview 🌟](https://kubebyexample.com/learning-paths/argo-cd/argo-cd-overview)
- [==dev.to: Argo CD and Sealed Secrets is a perfect match==](https://dev.to/timtsoitt/argo-cd-and-sealed-secrets-is-a-perfect-match-1dbf) In this article, you will learn how to configure Sealed Secrets with ArgoCD
- [akuity.io: How many do you need? - Argo CD Architectures Explained](https://akuity.io/blog/argo-cd-architectures-explained/)
- [piotrminkowski.com: Manage Multiple Kubernetes Clusters with ArgoCD 🌟](https://piotrminkowski.com/2022/12/09/manage-multiple-kubernetes-clusters-with-argocd/)
- [github.com/crumbhole/argocd-lovely-plugin: argocd-lovely-plugin](https://github.com/crumbhole/argocd-lovely-plugin) This plugin extends ArgoCD with:
    - Composing multiple things together to form a single app from multiple directories
    - Helm + Kustomize just work
    - You can chain several plugins together
    - When used with application sets, you can apply Kustomizations
- [seraf.dev: ArgoCD Tutorial — (with Terraform)](https://seraf.dev/argocd-tutorial-with-terraform-af77ddea2e6e) Here we’ll be deploying ArgoCD resources with Terraform on a local Kubernetes Cluster (KIND) for a true IaC infrastructure
- [github.com/myspotontheweb/gitops-workloads-demo](https://github.com/myspotontheweb/gitops-workloads-demo) This repository demonstrates how Helm based work loads can be managed by ArgoCD.
    - Creating a Pull Request creates a new environment
    - Each git push builds an image and updates the app
    - Closing the pull request terminates the environment
- [piotrminkowski.com: Manage Kubernetes Operators with ArgoCD](https://piotrminkowski.com/2023/05/05/manage-kubernetes-operators-with-argocd/)
- [==dev.to: Extending GitOps: Effortless continuous integration and deployment on Kubernetes==](https://dev.to/amplication/extending-gitops-effortless-continuous-integration-and-deployment-on-kubernetes-1oem) This article discusses using GitOps and Argo CD Image Updater for effortless continuous integration and deployment on Kubernetes
- [dev.to/devsatasurion: Deploying Applications with GitHub Actions and ArgoCD to EKS: Best Practices and Techniques](https://dev.to/devsatasurion/deploying-applications-with-github-actions-and-argocd-to-eks-best-practices-and-techniques-4epc)

## Argo CD Vulnerabilities

- [threatpost.com: Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers](https://threatpost.com/argo-cd-security-bug-kubernetes-cloud-apps/178239/)
- [thehackernews.com: New Argo CD Bug Could Let Hackers Steal Secret Info from Kubernetes Apps](https://thehackernews.com/2022/02/new-argo-cd-bug-could-let-hackers-steal.html)
- [armosec.io: CVE 2022-24348 – Argo CD High Severity Vulnerability and its impact on Kubernetes](https://www.armosec.io/blog/cve-2022-24348-argo-kubernetes/)
- [securityaffairs.co: Argo CD flaw could allow stealing sensitive data from Kubernetes Apps](https://securityaffairs.co/wordpress/127708/hacking/kubernetes-argo-cd-flaw.html) Argo CD is used by hundreds of organizations, including Alibaba Group, BMW Group, Deloitte, IBM, Intuit, Red Hat, Skyscanner, and Swisscom.
- [infoworld.com: How to protect your Kubernetes infrastructure from the Argo CD vulnerability](https://www.infoworld.com/article/3650659/how-to-protect-your-kubernetes-infrastructure-from-the-argo-cd-vulnerability.html) A zero-day vulnerability in Argo CD could be putting sensitive information like passwords and API keys at risk. Are you protected?
    - Use a dedicated project for the control plane
    - Argo resources are for Argo admins only
    - ...
    - Have a CVE response plan ready

## Argo CD Tools and Plugins

- [argoproj-labs/argocd-autopilot: Argo-CD Autopilot](https://github.com/argoproj-labs/argocd-autopilot)  The Argo-CD Autopilot is a tool which offers an opinionated way of installing Argo-CD and managing GitOps epositories. New users to GitOps and Argo CD are not often sure how they should structure their repos, add applications, promote apps across environments, and manage the Argo CD installation itself using GitOps. Argo Autopilot is a project that solves that
- [argoproj-labs/applicationset: Argo CD ApplicationSet Controller](https://github.com/argoproj-labs/applicationset) The ApplicationSet controller is a Kubernetes controller that adds support for a new custom ApplicationSet CustomResourceDefinition (CRD). The ApplicationSet controller manages multiple Argo CD Applications as a single ApplicationSet unit, supporting deployments to large numbers of clusters, deployments of large monorepos, and enabling secure Application self-service.
- [IBM/argocd-vault-plugin](https://github.com/IBM/argocd-vault-plugin) An ArgoCD plugin to retrieve secrets from Hashicorp Vault and inject them into Kubernetes secrets.
- [==argoproj-labs/argocd-vault-plugin==](https://github.com/argoproj-labs/argocd-vault-plugin) ArgoCD-Vault-plugin is an Argo CD plugin to retrieve secrets from various Secret Management tools (HashiCorp Vault, IBM Cloud Secrets Manager, AWS Secrets Manager, etc.) and inject them into Kubernetes resources - https://argocd-vault-plugin.readthedocs.io
- [github.com/crumbhole/argocd-vault-replacer](https://github.com/crumbhole/argocd-vault-replacer) An Argo CD plugin to replace placeholders in Kubernetes manifests with secrets stored in Hashicorp Vault. Scans the current directory recursively for any YAML files and attempts to replace strings following a pattern.

## Argo Rollouts

- [argoproj.github.io/argo-rollouts/](https://argoproj.github.io/argo-rollouts/)
- [infracloud.io: Progressive Delivery with Argo Rollouts : Blue-Green Deployment](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-blue-green-deployment/) In this post, you'll learn how to perform a blue-green deployment using the Argo Rollouts controller and CRD.
- [infracloud.io: Progressive Delivery with Argo Rollouts: Canary Deployment](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-canary-deployment/)
- [infracloud.io: How to Setup Blue Green Deployments with DNS Routing 🌟](https://www.infracloud.io/blogs/blue-green-deployments-dns-routing/) This blog post will teach you how to set up blue-green deployments using Argo Rollouts with DNS routing using **Azure Traffic Manager**
- [codefresh.io: Progressive delivery for Kubernetes Config Maps using Argo Rollouts](https://codefresh.io/blog/progressive-delivery-for-kubernetes-config-maps-using-argo-rollouts/) In this tutorial, you will learn how to use Argo Rollouts for settings/ConfigMaps using the Kustomize configmap generators. This is useful during blue/green deployments where you need a (templated) copy of the ConfigMap.

## Argo Workflows

- [dev.to: The three meanings of "template" in Argo Workflows](https://dev.to/crenshaw_dev/the-three-meanings-of-template-in-argo-workflows-2paf)
    - High-level best practices you should know to secure your workflows
    - The various components that make up Argo, and how to secure those components
    - Dive into operating and using Argo securely


    ```
    Dear user,
    I will kill your pod:

    If I want the node for something more important.
    If I’m draining the node, or scaling down a cluster.
    If it runs out of memory (because you got the config wrong).
    If I overcommitted.
    Hardware failure (computer catches fire).
    Kernel panic.
    Absolutely any reason I feel like.

    I’m sorry — I am who I am.

    All the best,

    Kubernetes xx
    ```


## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/MeU5_k9ssrs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QrLwFEXvxbo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ZzFg59nOp08" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>