# Argo CD Declarative GitOps for Kubernetes
- [Introduction](#introduction)
- [Argo CD Vulnerabilities](#argo-cd-vulnerabilities)
- [Argo CD Tools](#argo-cd-tools)
- [Videos](#videos)
## Introduction
- [argoproj.github.io: Argo CD - Declarative GitOps for Kubernetes](https://argoproj.github.io/argo-cd/) 
- [youtube: GitOps with Argo-CD & Kubernetes](https://www.youtube.com/watch?v=QrLwFEXvxbo&ab_channel=HoussemDellai)
- [Cloud Native Computing Foundation Accepts Argo as an Incubator Project](https://www.intuit.com/blog/technology/loud-native-computing-foundation-accepts-argo-as-an-incubator-project/)
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
- [blog.argoproj.io: What’s new in Argo Workflows v3.3](https://blog.argoproj.io/whats-new-in-argo-workflows-v3-3-dd051d2f1c7)
- [igboie.medium.com: Kubernetes CI/CD with GitHub, GitHub Actions and Argo CD](https://igboie.medium.com/kubernetes-ci-cd-with-github-github-actions-and-argo-cd-36b88b6bda64)
- [==faun.pub: Manage Prometheus alerting and recording rules using GitOps==](https://faun.pub/manage-prometheus-alerting-and-recording-rules-using-gitops-6c19bd1fd50)
- [medium.com/containers-101: Using GitOps, Multiple Argo Instances, and Environments with Argo CD at Scale](https://medium.com/containers-101/using-gitops-multiple-argo-instances-and-environments-with-argo-cd-at-scale-e6b19c86be36)
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

- [blog.argoproj.io: Best Practices for Multi-tenancy in Argo CD](https://blog.argoproj.io/best-practices-for-multi-tenancy-in-argo-cd-273e25a047b0)
- [argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework](https://argoproj.github.io/argo-events/) Argo Events is an event-driven workflow automation framework for Kubernetes which helps you trigger K8s objects, Argo Workflows, Serverless workloads, etc. on events from a variety of sources like webhooks, S3, schedules, messaging queues, etc.
- [jijujacob27.medium.com: Sharded applications on Kubernetes using Helm, ArgoCD, and Argo-Rollouts](https://jijujacob27.medium.com/sharded-saas-applications-on-kubernetes-using-helm-argocd-and-argo-rollouts-a683c66f8646) You will use Argo-Rollouts for deploying the app using the Blue/Green strategy.
- [medium.com/@ScrumPokerPro: Cloud native architecture with Kubernetes and ArgoCD](https://medium.com/@ScrumPokerPro/cloud-native-architecture-with-kubernetes-and-argocd-ebecda7784b8)
- [faun.pub: Deploying Argo CD and Sealed Secrets with Helm](https://faun.pub/deploying-argo-cd-and-sealed-secrets-with-helm-8de12f53051b) In this tutorial, you will go over the declarative setup of Argo CD and Sealed Secrets on a Kubernetes cluster. For deploying Argo CD and Sealed Secrets you will be using Helm Charts
- [dev.to: The three meanings of "template" in Argo Workflows](https://dev.to/crenshaw_dev/the-three-meanings-of-template-in-argo-workflows-2paf)
- [amralaayassen.medium.com: How to create ArgoCD Applications Automatically using ApplicationSet? “Automation of GitOps”](https://amralaayassen.medium.com/how-to-create-argocd-applications-automatically-using-applicationset-automation-of-the-gitops-59455eaf4f72)
- [==argoproj.github.io: Argo Rollouts - Kubernetes Progressive Delivery Controller==](https://argoproj.github.io/argo-rollouts/) **Argo Rollouts is a Kubernetes controller and set of CRDs which provide advanced deployment capabilities such as blue-green, canary, canary analysis, experimentation, and progressive delivery features to Kubernetes**
- [blog.getambassador.io: GitOps in Kubernetes with ArgoCD](https://blog.getambassador.io/gitops-in-kubernetes-with-argocd-c6ea0e510741)
- [blog.akuity.io: Unveil the Secret Ingredients of Continuous Delivery at Enterprise Scale with Argo CD](https://blog.akuity.io/unveil-the-secret-ingredients-of-continuous-delivery-at-enterprise-scale-with-argo-cd-7c5b4057ee49) Do you know that Argo CD can support thousands of apps and hundreds of clusters? in this article you will deep dive into Argo CD, bring answers and best practices on operating it at an enterprise scale
- [dev.to: Towards a Modular DevOps Stack](https://dev.to/camptocamp-ops/towards-a-modular-devops-stack-257c) In this article, you will learn how to **modularize your infrastructure using Terraform and ArgoCD**

## Argo CD Vulnerabilities
- [threatpost.com: Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers](https://threatpost.com/argo-cd-security-bug-kubernetes-cloud-apps/178239/)
- [thehackernews.com: New Argo CD Bug Could Let Hackers Steal Secret Info from Kubernetes Apps](https://thehackernews.com/2022/02/new-argo-cd-bug-could-let-hackers-steal.html)
- [armosec.io: CVE 2022-24348 – Argo CD High Severity Vulnerability and its impact on Kubernetes](https://www.armosec.io/blog/cve-2022-24348-argo-kubernetes/)
- [securityaffairs.co: Argo CD flaw could allow stealing sensitive data from Kubernetes Apps](https://securityaffairs.co/wordpress/127708/hacking/kubernetes-argo-cd-flaw.html) Argo CD is used by hundreds of organizations, including Alibaba Group, BMW Group, Deloitte, IBM, Intuit, Red Hat, Skyscanner, and Swisscom.
- [infoworld.com: How to protect your Kubernetes infrastructure from the Argo CD vulnerability](https://www.infoworld.com/article/3650659/how-to-protect-your-kubernetes-infrastructure-from-the-argo-cd-vulnerability.html) A zero-day vulnerability in Argo CD could be putting sensitive information like passwords and API keys at risk. Are you protected?

## Argo CD Tools
- [argoproj-labs/argocd-autopilot: Argo-CD Autopilot](https://github.com/argoproj-labs/argocd-autopilot)  The Argo-CD Autopilot is a tool which offers an opinionated way of installing Argo-CD and managing GitOps epositories. New users to GitOps and Argo CD are not often sure how they should structure their repos, add applications, promote apps across environments, and manage the Argo CD installation itself using GitOps. Argo Autopilot is a project that solves that
- [argoproj-labs/applicationset: Argo CD ApplicationSet Controller](https://github.com/argoproj-labs/applicationset) The ApplicationSet controller is a Kubernetes controller that adds support for a new custom ApplicationSet CustomResourceDefinition (CRD). The ApplicationSet controller manages multiple Argo CD Applications as a single ApplicationSet unit, supporting deployments to large numbers of clusters, deployments of large monorepos, and enabling secure Application self-service. 
- [IBM/argocd-vault-plugin](https://github.com/IBM/argocd-vault-plugin) An ArgoCD plugin to retrieve secrets from Hashicorp Vault and inject them into Kubernetes secrets.
- [==argoproj-labs/argocd-vault-plugin==](https://github.com/argoproj-labs/argocd-vault-plugin) ArgoCD-Vault-plugin is an Argo CD plugin to retrieve secrets from various Secret Management tools (HashiCorp Vault, IBM Cloud Secrets Manager, AWS Secrets Manager, etc.) and inject them into Kubernetes resources - https://argocd-vault-plugin.readthedocs.io

## Videos
??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/MeU5_k9ssrs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QrLwFEXvxbo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ZzFg59nOp08" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>
