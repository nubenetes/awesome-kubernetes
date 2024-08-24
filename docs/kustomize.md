# Template-Free Configuration Customization with Kustomize (Kubernetes Native Configuration Management)

1. [Introduction](#introduction)
2. [Secretize plugin](#secretize-plugin)
3. [Comparison between Helm and Kustomize for Kubernetes yaml management](#comparison-between-helm-and-kustomize-for-kubernetes-yaml-management)
4. [Boilerplate](#boilerplate)
5. [Videos](#videos)

## Introduction

- [kustomize.io 🌟](https://kustomize.io/)
    - Kustomize introduces a template-free way to customize application configuration that simplifies the use of off-the-shelf applications. Now, built into ```kubectl``` as ```apply -k```.
    - Kustomize traverses a Kubernetes manifest to add, remove or update configuration options without forking.
    - __It is available both as a standalone binary and as a native feature of kubectl.__
- [kubernetes.io: Introducing kustomize; Template-free Configuration Customization for Kubernetes](https://kubernetes.io/blog/2018/05/29/introducing-kustomize-template-free-configuration-customization-for-kubernetes/) If you run a Kubernetes environment, chances are you’ve customized a Kubernetes configuration — you've copied some API object YAML files and edited them to suit your needs. But there are drawbacks to this approach — it can be hard to go back to the source material and incorporate any improvements that were made to it. Today Google is announcing kustomize, a command-line tool contributed as a subproject of SIG-CLI. The tool provides a new, purely declarative approach to configuration customization that adheres to and leverages the familiar and carefully designed Kubernetes API.
- [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
- [blog.tomarrell.com: Kustomize: Traefik v2.2 as a Kubernetes Ingress Controller](https://blog.tomarrell.com/post/traefik_v2_on_kubernetes)
- [Kubestack Gitops Framework](https://github.com/kbst/terraform-kubestack) is a Gitops framework built on Terraform and Kustomize
- [3 ways to customize off-the-shelf Helm charts with Kustomize - Kubernetes](https://tech.aabouzaid.com/2020/09/3-ways-to-customize-off-the-shelf-helm-charts-with-kustomize-kubernetes.html)
- [dex.dev: YAML Templating Solutions: Helm & Kustomize](https://www.dex.dev/dex-videos/templating-solutions) Writing config files by hand is like coding with Notepad instead of an IDE. Let's find a better way, and take an overview of the popular solutions Helm & Kustomize.
- [blog.stack-labs.com: Kustomize - The right way to do templating in Kubernetes](https://blog.stack-labs.com/code/kustomize-101/)
- [opensource.com: Modify your Kubernetes manifests with Kustomize](https://opensource.com/article/21/6/kustomize-kubernetes) Modify your Kubernetes manifests without losing control of what's in the original versions.
- [dev.to: Introduction to Kustomize - How to customize Kubernetes objects kubernetes](https://dev.to/katiatalhi/introduction-to-kustomize-how-to-customize-kubernetes-objects-3e08)
- [mirantis.com: Kustomize Tutorial: Creating a Kubernetes app out of multiple pieces](https://www.mirantis.com/blog/introduction-to-kustomize-part-1-creating-a-kubernetes-app-out-of-multiple-pieces/)
- [codefresh.io: Applied GitOps with Kustomize](https://codefresh.io/about-gitops/applied-gitops-with-kustomize) In this article, you will learn Kustomize and how it can help deploy Kubernetes manifest with GitOps. This will allow you to leverage the power of Kustomize to define YAML files without using a templating engine
- [tech.aabouzaid.com: Set OpenAPI patch strategy for Kubernetes Custom Resources - Kustomize](https://tech.aabouzaid.com/2022/11/set-openapi-patch-strategy-for-kubernetes-custom-resources-kustomize.html) Kustomize supports 2 main client-side patching methods for Kubernetes manifests: JSON Patching and Strategic Merge Patch. This article discusses the pros and cons and shows how to add a merging strategy extension for Custom Resources.
- [nakamasato.medium.com: Comparison between Helm and Kustomize for Kubernetes yaml management](https://nakamasato.medium.com/comparison-between-helm-and-kustomize-for-kubernetes-yaml-management-aed32cef2627)
- [pauldally.medium.com: Kustomize Best Practices (Part 1)](https://pauldally.medium.com/kustomize-best-practices-part-1-86f9f22d2f20) Kubectl includes a very useful command called kustomize that allows a template-free way to customize Kubernetes application configuration.
    - [pauldally.medium.com: Kustomize Best Practices (Part 2)](https://pauldally.medium.com/kustomize-best-practices-part-2-c560f1fa1409)
- [notmattlucas.com: Kubernetes Configuration with Kustomize](https://notmattlucas.com/kubernetes-configuration-with-kustomize-f4dbba250f3)
- [medium.com/@nanditasahu031: How to Start with Kustomize — it’s Features](https://medium.com/@nanditasahu031/how-to-start-with-kustomize-its-features-dd541c3d2fa8)
- [harness.io: Comparing Helm vs Kustomize](https://harness.io/blog/helm-vs-kustomize)
- [nicolasbarlatier.hashnode.dev: Introduction Kubernetes and Kustomize: How to easily customize any resource configuration with Kustomize?](https://nicolasbarlatier.hashnode.dev/introduction-kubernetes-and-kustomize-how-to-easily-customize-any-resource-configuration-with-kustomize) In this tutorial, you will learn how to use Kustomize to template the number of replicas in a workload based on the environment (e.g. 1 pod in dev, 10 pods in prod)
- [==github.com/kostis-codefresh: How to Model Your Gitops Environments with kustomize== 🌟](https://github.com/kostis-codefresh/gitops-environment-promotion) In this repository, you'll find an example of how to model Kustomize folders for a GitOps application and promote releases between environments
- [dev.to: Kubernetes Kustomize Tutorial: A Beginner-Friendly Developer Guide!](https://dev.to/pavanbelagatti/kubernetes-kustomize-tutorial-a-beginner-friendly-developer-guide-322n)
- [pauldally.medium.com: Kustomize Best Practices (part 3)](https://pauldally.medium.com/kustomize-best-practices-part-3-1dbaa15fd16a)
- [levelup.gitconnected.com: Helm vs. Kustomize: Navigating Kubernetes Configuration Complexity](https://levelup.gitconnected.com/helm-vs-kustomize-navigating-kubernetes-configuration-complexity-ae86596c3cf2)
- [==devopscube.com/kustomize-tutorial: Kustomize Tutorial: Comprehensive Guide For Beginners== 🌟](https://devopscube.com/kustomize-tutorial)
- [blog.devgenius.io: Kustomize — K8 manifest patching](https://blog.devgenius.io/kustomize-simple-manifest-manipulation-9330f7f40d5d) In this tutorial, you will learn how to manipulate YAML files using Kustomize
- [faun.pub: How to build a GitOps workflow with ArgoCD, Kustomize and GitHub Actions](https://faun.pub/how-to-build-a-gitops-workflow-with-argocd-kustomize-and-github-actions-f919e7443295) Gain speed and clarity by adopting GitOps for your deployments
- [==techiescamp.com: Kubernetes Kustomize Crash Course==](https://techiescamp.com/courses/kubernetes-kustomize/) In this Kustomize crash course, you will learn all the Kustomize concepts and deploy an application using Kustomize on a Kubernetes cluster.
- [==devopscube.com/kuztomize-configmap-generators: Kuztomize Secret & Configmap Generators [Practical Examples]==](https://devopscube.com/kuztomize-configmap-generators/)
- [==itnext.io: Generating, transforming, and patching Kubernetes configuration with Kustomize==](https://itnext.io/generating-transforming-and-patching-kubernetes-configuration-with-kustomize-fb7b02476a1b)

## Secretize plugin

- [Secretize 🌟](https://github.com/bbl/secretize) Secretize is a kustomize plugin that helps generating kubernetes secrets from various sources such as AWS Secret Manager & Azure Vault. It's like a swiss army knife, but for kubernetes secrets.

## Comparison between Helm and Kustomize for Kubernetes yaml management

- [itnext.io: Helm Is Not Enough, You Also Need Kustomize](https://itnext.io/helm-is-not-enough-you-also-need-kustomize-82bae896816e) Customize the YAML’s to enforce policies from application operators, security operators, and cluster operators.
- [harness.io: Comparing Helm vs Kustomize 🌟](https://harness.io/blog/devops/helm-vs-kustomize/)
- [nakamasato.medium.com: Comparison between Helm and Kustomize for Kubernetes yaml management](https://nakamasato.medium.com/comparison-between-helm-and-kustomize-for-kubernetes-yaml-management-aed32cef2627) Helm and Kustomize are often compared with each other in the context of managing Kubernetes manifest file. Although those two tools have similar features, they are fundamentally different. In this post, I’ll compare them from several points of view with a sample application.

## Boilerplate

- [chrisns/k8s-opa-boilerplate](https://github.com/chrisns/k8s-opa-boilerplate) Boilerplate example of managing OPA with kustomize

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/1fCAwFGX38U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>