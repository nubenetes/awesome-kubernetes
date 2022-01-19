# Argo CD Declarative GitOps for Kubernetes
- [Introduction](#introduction)
- [Argo CD Tools](#argo-cd-tools)
## Introduction
- [Argo CD - Declarative GitOps for Kubernetes](https://argoproj.github.io/argo-cd/) 
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

## Argo CD Tools
- [argoproj-labs/argocd-autopilot: Argo-CD Autopilot](https://github.com/argoproj-labs/argocd-autopilot)  The Argo-CD Autopilot is a tool which offers an opinionated way of installing Argo-CD and managing GitOps epositories. New users to GitOps and Argo CD are not often sure how they should structure their repos, add applications, promote apps across environments, and manage the Argo CD installation itself using GitOps. Argo Autopilot is a project that solves that
- [argoproj-labs/applicationset: Argo CD ApplicationSet Controller](https://github.com/argoproj-labs/applicationset) The ApplicationSet controller is a Kubernetes controller that adds support for a new custom ApplicationSet CustomResourceDefinition (CRD). The ApplicationSet controller manages multiple Argo CD Applications as a single ApplicationSet unit, supporting deployments to large numbers of clusters, deployments of large monorepos, and enabling secure Application self-service. 
- [IBM/argocd-vault-plugin](https://github.com/IBM/argocd-vault-plugin) An ArgoCD plugin to retrieve secrets from Hashicorp Vault and inject them into Kubernetes secrets.
