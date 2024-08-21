# Argo Declarative GitOps for Kubernetes

1. [Introduction](#introduction)
2. [Argo CD](#argo-cd)
3. [Argo CD Vulnerabilities](#argo-cd-vulnerabilities)
4. [Argo CD Tools and Plugins](#argo-cd-tools-and-plugins)
5. [Argo Rollouts](#argo-rollouts)
6. [Argo Workflows](#argo-workflows)
7. [Videos](#videos)

## Introduction

- [Cloud Native Computing Foundation Accepts Argo as an Incubator Project](https://www.intuit.com/blog/technology/loud-native-computing-foundation-accepts-argo-as-an-incubator-project/)
- [argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework](https://argoproj.github.io/argo-events/) Argo Events is an event-driven workflow automation framework for Kubernetes which helps you trigger K8s objects, Argo Workflows, Serverless workloads, etc. on events from a variety of sources like webhooks, S3, schedules, messaging queues, etc.
- [Why and when do you need Argo CD?](https://mkdev.me/posts/why-and-when-do-you-need-argo-cd) High-level explanation of in which cases Argo CD makes sense and what you should keep in mind if you want to use it.

## Argo CD

- [argoproj.github.io: Argo CD - Declarative GitOps for Kubernetes](https://argoproj.github.io/argo-cd/)
- [youtube: GitOps with Argo-CD & Kubernetes](https://www.youtube.com/watch?v=QrLwFEXvxbo&ab_channel=HoussemDellai)
- [openshift.com: OpenShift Authentication Integration with ArgoCD](https://www.openshift.com/blog/openshift-authentication-integration-with-argocd)
- [developers.redhat.com: OpenShift joins the Argo CD community (KubeCon Europe 2020)](https://developers.redhat.com/blog/2020/08/17/penshift-joins-the-argo-cd-community-kubecon-europe-2020/)
- [thenewstack.io: Applied GitOps with ArgoCD](https://thenewstack.io/applied-gitops-with-argocd/)
- [thenewstack.io: Why ArgoCD Is the Lifeline of GitOps](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/)
- [openshift.com: Getting Started with ApplicationSets](https://www.openshift.com/blog/getting-started-with-applicationsets) "App of Apps" pattern.
- [medium: Argo CD: A Tool for Kubernetes DevOps](https://medium.com/geekculture/argo-cd-a-tool-for-kubernetes-devops-c46f2881edfe)
- [itnext.io: ArgoCD: users, access, and RBAC](https://itnext.io/argocd-users-access-and-rbac-ddf9f8b51bad)
- [opensource.com: Automatically create multiple applications in Argo CD](https://opensource.com/article/21/7/automating-argo-cd)
- [cloud.redhat.com: How to Use ArgoCD Deployments with GitHub Tokens](https://cloud.redhat.com/blog/how-to-use-argocd-deployments-with-github-tokens)
- [blog.risingstack.com: Argo CD Kubernetes Tutorial](https://blog.risingstack.com/argo-cd-kubernetes-tutorial/)
- [wecloudpro.com: Deploying Helm Charts with ArgoCD](https://www.wecloudpro.com/2021/11/28/Argocd-helm.html)
- [==thenewstack.io: GitOps on Kubernetes: Deciding Between Argo CD and Flux==](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux)
- [medium.com/gumgum-tech: Streamlining your Kubernetes adoption with Helmfile / ArgoCD and GitOps](https://medium.com/gumgum-tech/streamlining-your-kubernetes-adoption-with-helmfile-argocd-and-gitops-211937e21e29)
- [levelup.gitconnected.com: Getting Started With ArgoCD on your Kubernetes Cluster](https://levelup.gitconnected.com/getting-started-with-argocd-on-your-kubernetes-cluster-552ca5d8cf41) A step-by-step guide to set up ArgoCD on your Kubernetes cluster and synchronize your resources with your GitHub repository.
- [digitalocean.com: How to Deploy to Kubernetes using Argo CD and GitOps](https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops)
- [aws.amazon.com: Cloud Native CI/CD with Tekton and ArgoCD on AWS](https://aws.amazon.com/blogs/containers/cloud-native-ci-cd-with-tekton-and-argocd-on-aws/)
- [blog.argoproj.io: New sync and diff strategies in ArgoCD](https://blog.argoproj.io/new-sync-and-diff-strategies-in-argocd-44195d3f8b8c)
- [igboie.medium.com: Kubernetes CI/CD with GitHub, GitHub Actions and Argo CD](https://igboie.medium.com/kubernetes-ci-cd-with-github-github-actions-and-argo-cd-36b88b6bda64)
- [==faun.pub: Manage Prometheus alerting and recording rules using GitOps==](https://faun.pub/manage-prometheus-alerting-and-recording-rules-using-gitops-6c19bd1fd50)
- [medium.com/containers-101: Using GitOps, Multiple Argo Instances, and Environments with Argo CD at Scale](https://medium.com/containers-101/using-gitops-multiple-argo-instances-and-environments-with-argo-cd-at-scale-e6b19c86be36)
- [blog.argoproj.io: Best Practices for Multi-tenancy in Argo CD](https://blog.argoproj.io/best-practices-for-multi-tenancy-in-argo-cd-273e25a047b0)
- [medium.com/@ScrumPokerPro: Cloud native architecture with Kubernetes and ArgoCD](https://medium.com/@ScrumPokerPro/cloud-native-architecture-with-kubernetes-and-argocd-ebecda7784b8)
- [faun.pub: Deploying Argo CD and Sealed Secrets with Helm](https://faun.pub/deploying-argo-cd-and-sealed-secrets-with-helm-8de12f53051b) In this tutorial, you will go over the declarative setup of Argo CD and Sealed Secrets on a Kubernetes cluster. For deploying Argo CD and Sealed Secrets you will be using Helm Charts
- [amralaayassen.medium.com: How to create ArgoCD Applications Automatically using ApplicationSet? “Automation of GitOps”](https://amralaayassen.medium.com/how-to-create-argocd-applications-automatically-using-applicationset-automation-of-the-gitops-59455eaf4f72)
- [blog.getambassador.io: GitOps in Kubernetes with ArgoCD](https://blog.getambassador.io/gitops-in-kubernetes-with-argocd-c6ea0e510741)
- [blog.akuity.io: Unveil the Secret Ingredients of Continuous Delivery at Enterprise Scale with Argo CD](https://blog.akuity.io/unveil-the-secret-ingredients-of-continuous-delivery-at-enterprise-scale-with-argo-cd-7c5b4057ee49) Do you know that Argo CD can support thousands of apps and hundreds of clusters? in this article you will deep dive into Argo CD, bring answers and best practices on operating it at an enterprise scale
- [dev.to: Towards a Modular DevOps Stack](https://dev.to/camptocamp-ops/towards-a-modular-devops-stack-257c) In this article, you will learn how to **modularize your infrastructure using Terraform and ArgoCD**
- [datree.io: ArgoCD Best Practices](https://datree.io/resources/argocd-best-practices-you-should-know) In this article, you'll explore some best practices for ArgoCD:
    - Disallow providing an empty retryStrategy
    - Ensure that Workflow pods are not configured to use the default service account
    - Ensure retry on both Error and TransientError
- [==devops.com: The Argo Project: Making GitOps Practical==](https://devops.com/the-argo-project-making-gitops-practical/)
- [piotrminkowski.com: Manage Kubernetes Cluster with Terraform and Argo CD. Create Kakfa Cluster using GitOps 🌟](https://piotrminkowski.com/2022/06/28/manage-kubernetes-cluster-with-terraform-and-argo-cd/) This article shows how to create and manage Kubernetes (Kind) cluster with Terraform and Argo CD, and install Kafka on it. Terraform is very useful for automating infrastructure. On the other hand, Argo CD helps us implement GitOps and continuous delivery for our applications. It seems that we can successfully combine both these tools. Let’s consider how they can help us to work with Kubernetes in the GitOps style.
- [prashant-48386.medium.com: Continuous Delivery for Kubernetes With Argo CD](https://prashant-48386.medium.com/continuous-delivery-for-kubernetes-with-argo-cd-9d5f3b69f1db)
- [medium.com/@outlier.developer: Getting Started with ArgoCD for GitOps Kubernetes Deployments](https://medium.com/@outlier.developer/getting-started-with-argocd-for-gitops-kubernetes-deployments-fafc2ad2af0)
- [medium.com/@hmquan08011996: Setup Microservices on Kubernetes — Automating Kubernetes with ArgoCD](https://medium.com/@hmquan08011996/setup-microservices-on-kubernetes-automating-kubernetes-with-argocd-cb94622dac5b)
- [datree.io: ArgoCD Best Practices You Should Know](https://www.datree.io/resources/argocd-best-practices-you-should-know) In this article, you'll explore some best practices for ArgoCD:
    - Disallow providing an empty retryStrategy
    - Ensure that Workflow pods are not configured to use the default service account
    - Ensure retry on both Error and TransientError

- [kamsjec.medium.com: ArgoCD Setup on Kubernetes/OpenShift Cluster](https://kamsjec.medium.com/argocd-setup-on-kubernetes-openshift-cluster-f7340344c017) ArgoCD is a declarative GitOps tool built to deploy applications to Kubernetes/OpenShift clusters. ArgoCD is a Kubernetes/OpenShift controller, responsible for continuously monitoring all running applications and comparing their live state to the desired state specified in the Git repository.
- [medium.com/@versentfastforward: GitOps on Kubernetes with ArgoCD](https://medium.com/@versentfastforward/gitops-and-argocd-to-automate-kubernetes-deployments-640f3a086865) This is the first post in our series about Managing Complex Kubernetes Clusters. We introduce how we used ArgoCD to enforce GitOps by preventing any alternate means of deployment to your cluster other than through a commit in your GitOps repo.
    - [medium.com/@versentfastforward: One-click Bootstrap Deployment of ArgoCD](https://medium.com/@versentfastforward/one-click-bootstrap-deployment-of-argocd-e06f848aacc5) This is the second post in our series about Managing Complex Kubernetes Clusters. We describe how to create a bootstrap script that automates key prerequisites: deployment of ArgoCD and pointing it at the repo and cluster that it needs to use for deployments.
    - [medium.com/@versentfastforward: Structuring Your Repo for ArgoCD, Part 1](https://medium.com/@versentfastforward/structuring-your-repo-for-argocd-part-1-582817713b0) This is the third post in our series about Managing Complex Kubernetes Clusters. We address the challenge of eliminating duplication of YAML files and reduce the amount effort required to deploy Kubernetes in multiple environments, as well as the continuous deployment (CD) of containerized workloads without developing complex imperative pipelines.
- [faun.pub: Continuous Deployments of Kubernetes Applications using Argo CD GitOps & Helm Charts](https://faun.pub/continuous-deployments-of-kubernetes-applications-using-argo-cd-gitops-helm-charts-9df917caa2e4)
- [jamalshahverdiev.medium.com: ArgoCD ApplicationSet with Applications, Image Updater and Notification controller with SSO](https://jamalshahverdiev.medium.com/argocd-applicationset-with-applications-image-updater-and-notification-controller-with-sso-bba3182dad8a)
- [kubebyexample.com: Argo CD Overview 🌟](https://kubebyexample.com/learning-paths/argo-cd/argo-cd-overview)
- [faun.pub: Hygiene of an ArgoCD-built automation at a scale](https://faun.pub/hygiene-of-argocd-built-automation-at-a-scale-cf63ee459510) In this article, you will find a list of best practices and tips for using ArgoCD automation at scale
- [blog.devgenius.io: Argo CD Introduction](https://blog.devgenius.io/argo-cd-introduction-4b16f50b0d56) What is ArgoCD and why use it
- [==dev.to: Argo CD and Sealed Secrets is a perfect match==](https://dev.to/timtsoitt/argo-cd-and-sealed-secrets-is-a-perfect-match-1dbf) In this article, you will learn how to configure Sealed Secrets with ArgoCD
- [figments.medium.com: ArgoCD: The first step towards GitOps](https://figments.medium.com/argocd-the-first-step-towards-gitops-899732fbc33e) A core component of GitOps is enforcing the deployment of apps using Git. This means defining the app version and configuration you want in a Git repo, and using a tool like ArgoCD to sync the Git configuration to the deployment. In this article, we’ll look at how we can use ArgoCD to manage automatic Git based deployments of apps.
- [medium.com/@nsfabrice2009: How to install ArgoCD on k8s cluster](https://medium.com/@nsfabrice2009/how-to-install-argocd-on-k8s-cluster-ad9084c71f16)
- [akuity.io: How many do you need? - Argo CD Architectures Explained](https://akuity.io/blog/argo-cd-architectures-explained/)
- [piotrminkowski.com: Manage Multiple Kubernetes Clusters with ArgoCD 🌟](https://piotrminkowski.com/2022/12/09/manage-multiple-kubernetes-clusters-with-argocd/)
- [medium.com/containers-101: How to Install and Upgrade Argo CD](https://medium.com/containers-101/how-to-install-and-upgrade-argo-cd-a64f4635f97b)
- [medium.com/containers-101: Argo CD Best Practices](https://medium.com/containers-101/best-practices-for-argo-cd-8253bcd31897) In this blog post, you'll learn some best practices tied to Argo CD that allow you to leverage GitOps easily within your deployment workflow.
- [github.com/crumbhole/argocd-lovely-plugin: argocd-lovely-plugin](https://github.com/crumbhole/argocd-lovely-plugin) This plugin extends ArgoCD with:
    - Composing multiple things together to form a single app from multiple directories
    - Helm + Kustomize just work
    - You can chain several plugins together
    - When used with application sets, you can apply Kustomizations
- [gokhan-karadas1992.medium.com: ArgoCD + Kubevela Integration](https://gokhan-karadas1992.medium.com/argocd-kubevela-integration-eb88dc0484e0)
- [==blog.tanmaysarkar.tech: Beginners Guide to Argo CD==](https://blog.tanmaysarkar.tech/beginners-guide-to-argo-cd) In this guide, you will learn how to use ArgoCD by practising on a local minikube cluster
- [medium.com/devops-techable: GitOps with ArgoCD running in Kubernetes for deployment processing](https://medium.com/devops-techable/gitops-with-argocd-running-in-kubernetes-for-deployment-processing-c5d21770ca97)
- [seraf.dev: ArgoCD Tutorial — (with Terraform)](https://seraf.dev/argocd-tutorial-with-terraform-af77ddea2e6e) Here we’ll be deploying ArgoCD resources with Terraform on a local Kubernetes Cluster (KIND) for a true IaC infrastructure
- [medium.com/@eduard.mihai.lemnaru: Auto-update helm chart version using ArgoCD](https://medium.com/@eduard.mihai.lemnaru/auto-update-helm-chart-version-using-argocd-4936933a2bac)
- [53jk1.medium.com: ArgoCD: The Continuous Delivery Solution for Kubernetes](https://53jk1.medium.com/argocd-the-continuous-delivery-solution-for-kubernetes-ae5b008e76d1)
- [github.com/myspotontheweb/gitops-workloads-demo](https://github.com/myspotontheweb/gitops-workloads-demo) This repository demonstrates how Helm based work loads can be managed by ArgoCD.
- [medium.com/@jon.mclean: ArgoCD: The GitOps Way](https://medium.com/@jon.mclean/argocd-the-gitops-way-90f7eb0d2606)
- [medium.com/@devopsrockers: Blue-Green Deployment on EKS using Argocd with Kubecost, Istio, External DNS, Grafana-Prometheus and More: “Build, Deploy a Resilient and Observability-Driven Application”](https://medium.com/@devopsrockers/blue-green-deployment-on-eks-using-argocd-with-kubecost-istio-external-dns-grafana-prometheus-d5d5508f0748)
- [medium.com/@samuelbagattin: Partial Helm values encryption using AWS KMS with ArgoCD](https://medium.com/@samuelbagattin/partial-helm-values-encryption-using-aws-kms-with-argocd-aca1c0d36323) In this blog post, you'll learn how to encrypt only specific yaml fields in `values.yaml`, and how to configure ArgoCD to decrypt these secrets on the fly before installing a Helm release
- [blog.devops.dev: GitOps at Scale](https://blog.devops.dev/gitops-at-scale-69639c9a3dd7) Scale your Projects like a Fleet with Argo CD
- [medium.com/@jerome.decoster: Create temporary environment from Pull Request with ArgoCD ApplicationSet](https://medium.com/@jerome.decoster/create-temporary-environment-from-pull-request-with-argocd-applicationset-1cef9803223a) In this post, you'll learn how to create a new environment for each pull request with ArgoCD:
    - Creating a Pull Request creates a new environment
    - Each git push builds an image and updates the app
    - Closing the pull request terminates the environment
- [piotrminkowski.com: Manage Kubernetes Operators with ArgoCD](https://piotrminkowski.com/2023/05/05/manage-kubernetes-operators-with-argocd/)
- [medium.com/@geoffrey.muselli: ArgoCD: Multi-cluster Helm charts management in mono-repo](https://medium.com/@geoffrey.muselli/argocd-multi-cluster-helm-charts-installation-in-mono-repo-0a406ff7c578)
- [itnext.io: Build a Lightweight Internal Developer Platform with Argo CD and Kubernetes Labels](https://itnext.io/build-a-lightweight-internal-developer-platform-with-argo-cd-and-kubernetes-labels-4c0e52c6c0f4) Don’t Underestimate Labels with Kubernetes: Simplify, Don’t Overcomplicate. This article demonstrates how to create a lightweight Internal Developer Platform utilizing GitOps with Argo CD and leveraging Kubernetes labels to offer a streamlined and efficient solution for managing and deploying your infrastructure
- [medium.com/otomi-platform: Helmfile and ArgoCD are better together](https://medium.com/otomi-platform/helmfile-and-argocd-better-together-f8d4587263ff)
- [overcast.blog: GitOps with ArgoCD for Kubernetes](https://overcast.blog/gitops-with-argocd-for-kubernetes-tips-and-tricks-4b926ba75f88)
- [medium.com/globant: Using multiple sources for a Helm Chart deployment in ArgoCD](https://medium.com/globant/using-multiple-sources-for-a-helm-chart-deployment-in-argocd-cf3cd2d598fc)
- [faun.pub: ArgoCD Finalizer Shield: Protecting Your Production Clusters from Unintended Deletion](https://faun.pub/argocd-finalizer-shield-protecting-your-clusters-from-unintended-deletion-c7929a82d983) This article teaches how to protect your ArgoCD clusters from accidental deletion using finalizers, a simple yet powerful mechanism that ensures the integrity of your cloud-native infrastructure
- [overcast.blog: Kubernetes — ArgoCD — Gitlab Webhook Configuration](https://overcast.blog/kubernetes-argocd-gitlab-webhook-configuration-30bc5a75139e)
- [developers.redhat.com: Enhance Kubernetes deployment efficiency with Argo CD and ApplicationSet](https://developers.redhat.com/articles/2024/06/06/enhance-kubernetes-deployment-efficiency-argo-cd-and-applicationset)
- [==dev.to: Extending GitOps: Effortless continuous integration and deployment on Kubernetes==](https://dev.to/amplication/extending-gitops-effortless-continuous-integration-and-deployment-on-kubernetes-1oem) This article discusses using GitOps and Argo CD Image Updater for effortless continuous integration and deployment on Kubernetes
- [dev.to/devsatasurion: Deploying Applications with GitHub Actions and ArgoCD to EKS: Best Practices and Techniques](https://dev.to/devsatasurion/deploying-applications-with-github-actions-and-argocd-to-eks-best-practices-and-techniques-4epc)

## Argo CD Vulnerabilities

- [threatpost.com: Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers](https://threatpost.com/argo-cd-security-bug-kubernetes-cloud-apps/178239/)
- [thehackernews.com: New Argo CD Bug Could Let Hackers Steal Secret Info from Kubernetes Apps](https://thehackernews.com/2022/02/new-argo-cd-bug-could-let-hackers-steal.html)
- [armosec.io: CVE 2022-24348 – Argo CD High Severity Vulnerability and its impact on Kubernetes](https://www.armosec.io/blog/cve-2022-24348-argo-kubernetes/)
- [securityaffairs.co: Argo CD flaw could allow stealing sensitive data from Kubernetes Apps](https://securityaffairs.co/wordpress/127708/hacking/kubernetes-argo-cd-flaw.html) Argo CD is used by hundreds of organizations, including Alibaba Group, BMW Group, Deloitte, IBM, Intuit, Red Hat, Skyscanner, and Swisscom.
- [infoworld.com: How to protect your Kubernetes infrastructure from the Argo CD vulnerability](https://www.infoworld.com/article/3650659/how-to-protect-your-kubernetes-infrastructure-from-the-argo-cd-vulnerability.html) A zero-day vulnerability in Argo CD could be putting sensitive information like passwords and API keys at risk. Are you protected?
- [dnastacio.medium.com: Six critical blindspots while securing Argo CD](https://dnastacio.medium.com/gitops-argocd-security-cbb6fb6378bb) This article shows the core strategies for securing an Argo CD deployment and keeping you ahead of potential exposures:
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
- [==argoproj.github.io: Argo Rollouts - Kubernetes Progressive Delivery Controller==](https://argoproj.github.io/argo-rollouts/) **Argo Rollouts is a Kubernetes controller and set of CRDs which provide advanced deployment capabilities such as blue-green, canary, canary analysis, experimentation, and progressive delivery features to Kubernetes**
- [jijujacob27.medium.com: Sharded applications on Kubernetes using Helm, ArgoCD, and Argo-Rollouts](https://jijujacob27.medium.com/sharded-saas-applications-on-kubernetes-using-helm-argocd-and-argo-rollouts-a683c66f8646) You will use Argo-Rollouts for deploying the app using the Blue/Green strategy.
- [medium.com/@ej.sta.ana: Easy Blue-Green Deployment on Openshift Container Platform using Argo Rollouts](https://medium.com/@ej.sta.ana/easy-blue-green-deployment-on-openshift-container-platform-using-argo-rollouts-4d514b3c5c0f) Argo Rollouts is part of the Argo project which includes the popular ArgoCD gitops tool. Argo Rollouts can help you do blue-green deployment easily on Kubernetes/OpenShift.
- [infracloud.io: Progressive Delivery with Argo Rollouts : Blue-Green Deployment](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-blue-green-deployment/) In this post, you'll learn how to perform a blue-green deployment using the Argo Rollouts controller and CRD.
- [infracloud.io: Progressive Delivery with Argo Rollouts: Canary Deployment](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-canary-deployment/)
- [medium.com/everything-full-stack: Deployment Strategies: Argo Rollouts](https://medium.com/everything-full-stack/deployment-strategies-argo-rollouts-1980fc0685e6)
- [faun.pub: Kubernetes Practice — Automating Blue/Green Deployment with Argo Rollouts](https://faun.pub/kubernetes-practice-automating-blue-green-deployment-with-argo-rollouts-2279aa890c53) In this article, we will learn how to automate Blue/Green Deployment with Argo Rollouts.
- [infracloud.io: How to Setup Blue Green Deployments with DNS Routing 🌟](https://www.infracloud.io/blogs/blue-green-deployments-dns-routing/) This blog post will teach you how to set up blue-green deployments using Argo Rollouts with DNS routing using **Azure Traffic Manager**
- [codefresh.io: Progressive delivery for Kubernetes Config Maps using Argo Rollouts](https://codefresh.io/blog/progressive-delivery-for-kubernetes-config-maps-using-argo-rollouts/) In this tutorial, you will learn how to use Argo Rollouts for settings/ConfigMaps using the Kustomize configmap generators. This is useful during blue/green deployments where you need a (templated) copy of the ConfigMap.
- [faun.pub: How Helm Subcharts Make the Transition to Argo Rollouts a Breeze](https://faun.pub/how-helm-subcharts-make-the-transition-to-argo-rollouts-a-breeze-aaf160924dbf)

## Argo Workflows

- [blog.argoproj.io: What’s new in Argo Workflows v3.3](https://blog.argoproj.io/whats-new-in-argo-workflows-v3-3-dd051d2f1c7)
- [dev.to: The three meanings of "template" in Argo Workflows](https://dev.to/crenshaw_dev/the-three-meanings-of-template-in-argo-workflows-2paf)
- [blog.argoproj.io: Practical Argo Workflows Hardening 🌟](https://blog.argoproj.io/practical-argo-workflows-hardening-dd8429acc1ce) In this post, you'll cover:
    - High-level best practices you should know to secure your workflows
    - The various components that make up Argo, and how to secure those components
    - Dive into operating and using Argo securely

- [blog.argoproj.io: Architecting Workflows For Reliability](https://blog.argoproj.io/architecting-workflows-for-reliability-d33bd720c6cc) Kubernetes is designed for stateless scalable web applications, apps where if one process dies, then another process can be dropped in its place. Kubernetes makes one promise — it will kill your pods. Kubernetes expects applications built on it to be tolerant of both any disruption— so apps must be designed with that in mind.

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

- [medium.com/atlantbh: Implementing CI/CD pipeline using Argo Workflows and Argo Events 🌟](https://medium.com/atlantbh/implementing-ci-cd-pipeline-using-argo-workflows-and-argo-events-6417dd157566)

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/MeU5_k9ssrs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QrLwFEXvxbo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ZzFg59nOp08" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>
