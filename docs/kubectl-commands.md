# Kubectl commands

1. [Introduction](#introduction)
2. [Kubectl Cheat Sheets](#kubectl-cheat-sheets)
3. [Kubectl aliases](#kubectl-aliases)
4. [Kubectl explain](#kubectl-explain)
5. [Kubectl example](#kubectl-example)
6. [Kubectl Autocomplete](#kubectl-autocomplete)
7. [kubectl exec](#kubectl-exec)
8. [kubectl scale](#kubectl-scale)
9. [kubectl debug](#kubectl-debug)
10. [List all resources and sub resources that you can constrain with RBAC](#list-all-resources-and-sub-resources-that-you-can-constrain-with-rbac)
11. [Copy a configMap in kubernetes between namespaces](#copy-a-configmap-in-kubernetes-between-namespaces)
12. [Copy secrets in kubernetes between namespaces](#copy-secrets-in-kubernetes-between-namespaces)
13. [Export resources with kubectl and python](#export-resources-with-kubectl-and-python)
14. [Buildkit CLI for kubectl a drop in replacement for docker build](#buildkit-cli-for-kubectl-a-drop-in-replacement-for-docker-build)
15. [Kubectl Alternatives](#kubectl-alternatives)
     1. [Manage Kubernetes (K8s) objects with Ansible Kubernetes Module](#manage-kubernetes-k8s-objects-with-ansible-kubernetes-module)
     2. [Jenkins Kubernetes Plugins](#jenkins-kubernetes-plugins)
16. [Videos](#videos)
17. [Tweets](#tweets)

## Introduction

- [itnext.io: Boosting your kubectl productivity](https://itnext.io/boosting-your-kubectl-productivity-b348f7c25712)
- [medium: 4 Simple Kubernetes Terminal Customizations to Boost Your Productivity](https://medium.com/better-programming/4-simple-kubernetes-terminal-customizations-to-boost-your-productivity-deda60a19924)
- [medium: Ready-to-use commands and tips for kubectl](https://medium.com/flant-com/kubectl-commands-and-tips-7b33de0c5476)
- [medium: Be fast with Kubectl 1.19 CKAD/CKA 🌟](https://medium.com/faun/be-fast-with-kubectl-1-18-ckad-cka-31be00acc443) Collection of the fastest ways to create k8s resources using kubectl ≥ 1.18
- [developers.redhat.com: Kubectl: Developer tips for the Kubernetes command line 🌟](https://developers.redhat.com/blog/2020/11/20/kubectl-developer-tips-for-the-kubernetes-command-line/)
- [ibm.com: 8 Kubernetes Tips and Tricks 🌟](https://www.ibm.com/cloud/blog/8-kubernetes-tips-and-tricks) Most of the tips given below are using kubectl, a powerful command-line tool that allows you to execute commands against Kubernetes clusters.
    - Set default namespaces
    - Helpful aliases to save time
    - YAML editing with vi
    - Create YAML from kubectl commands
    - Switching between Kubernetes namespaces
    - Shell auto-completion
    - Viewing resource utilization
    - Extend kubectl and create your own commands using raw outputs
- [pixelstech.net: Update & Delete Kubernetes resources in one-line command](https://www.pixelstech.net/article/1604225312-Update-&amp-Delete-Kubernetes-resources-in-one-line-command)
- [opensource.com: 5 useful ways to manage Kubernetes with kubectl](https://opensource.com/article/21/7/kubectl) Learn kubectl to enhance how you interact with Kubernetes.
- [hackerxone.com: How to Manage Single & Multiple Kubernetes Clusters using kubectl & kubectx in Linux](https://www.hackerxone.com/2021/07/10/how-manage-single-multiple-kubernetes-clusters-using-kubectl-kubectx-linux/)
- [Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere/) This tutorial shows you how to expose your private Kubernetes API server to the Internet, so that you can manage your cluster from anywhere, just like you would with a cloud offering.
- [medium: One CKA/CKAD/CKS requirement: Mastering Kubectl](https://medium.com/nerd-for-tech/one-cka-ckad-cks-requirement-mastering-kubectl-85486bc0a3aa)
- [medium: Replication Controller Vs ReplicaSets in Kubernetes](https://medium.com/geekculture/replication-controller-vs-replicasets-in-kubernetes-7b780e4d09d5) Learn why we need replication and how replication works in Kubernetes. Scale the application using the kubectl scale command.
- [dev.to: Open a command prompt in a Kubernetes cluster](https://dev.to/eldadak/open-a-command-prompt-in-a-kubernetes-cluster-206g) This starts up a pod (in the default namespace by default) and opens a command line in the given container. As I'm running as root, I can install anything I need for debugging and testing right in my cluster.
- [akhilsharma.work: Checking Kubernetes API Calls using kubectl](https://akhilsharma.work/checking-kubernetes-api-calls-using-kubectl/) In order to interact, we can simply use `kubectl`. Just add verbose logging level of 8+ and you will get the API calls!
    - `kubectl get pods -v=8`
    - `kubectl create job my-job --image=busybox --dry-run=server -v8`
- [cloudsavvyit.com: How to Restart Kubernetes Pods with Kubectl](https://www.cloudsavvyit.com/14587/how-to-restart-kubernetes-pods-with-kubectl/)
- [technos.medium.com: How kubectl apply command works?](https://technos.medium.com/how-kubectl-apply-command-works-d092121056d3)
- [blogs.nakam.org: What Happens When? K8s Edition 🌟](https://blogs.nakam.org/what-happens-when-k8s-edition) What happens when you do kubectl create deploy nginx --image=nginx --replicas=3
- [inlets.dev: Fixing the Developer Experience of Kubernetes Port Forwarding](https://inlets.dev/blog/2022/06/24/fixing-kubectl-port-forward.html) This article shows you some of the frustrations of using kubectl for port-forwarding and how to fix the developer experience.
- [==medium.com/swlh: Break Down Kubernetes Server-Side Apply (Advanced kubectl)== 🌟](https://medium.com/swlh/break-down-kubernetes-server-side-apply-5d59f6a14e26) Are you already using the SSA? Do you know the difference between CSA and SSA?
- [containiq.com: Kubectl Config Set-Context | Tutorial and Best Practices](https://www.containiq.com/post/kubectl-config-set-context-tutorial-and-best-practices) Kubernetes comes with many tools to help you manage your clusters, including kubectl set-context. In this guide, you'll learn how to use this command to manipulate contexts in your kubeconfig file, as well as best practices for doing so.
- [blog.devgenius.io: K8s — Manage Multiple Clusters Using kubectl at Scale](https://blog.devgenius.io/k8s-manage-multiple-clusters-using-kubectl-at-scale-9f200c692099) Manage multiple K8s clusters efficiently using kubectl
- [==itnext.io: How to Restart Kubernetes Pods With Kubectl== 🌟](https://itnext.io/how-to-restart-kubernetes-pods-with-kubectl-2a7834a6b961) A pod is the smallest unit in Kubernetes (K8S). They should run until they are replaced by a new deployment. Because of this, there is no way to restart a pod, instead, it should be replaced.
- [awstip.com: Kubernetes — Creating deployments via command line and with YAML files](https://awstip.com/kubernetes-creating-deployments-via-command-line-and-with-yaml-files-783eaad7b3be)
- [superbrothers/zsh-kubectl-prompt 🌟](https://github.com/superbrothers/zsh-kubectl-prompt) Display information about the kubectl current context and namespace in zsh prompt.
- [medium.com/@emmaliaocode: kubectl create vs kubectl apply. What’s the difference?](https://medium.com/@emmaliaocode/kubectl-create-vs-kubectl-apply-whats-the-differences-f6472f4c6c86)
- [hidetatz/kubecolor 🌟](https://github.com/hidetatz/kubecolor) colorizes kubectl output
- [medium.com/codex: Kubectl Output 101](https://medium.com/codex/kubectl-output-101-851f8e61fd51) Cheatsheet & examples of using kubectl get -o
- [lovethepenguin.com: Kubernetes: common pod operations](https://lovethepenguin.com/kubernetes-common-pod-operations-ee23a402b9f4)
- [medium.com/geekculture: kubectl — Best Practices](https://medium.com/geekculture/kubectl-best-practices-c4ff809167dd)
- [==learnitguide.net: How to Create ConfigMap from Properties File Using K8s Client==](https://www.learnitguide.net/2023/04/how-to-create-configmap-from-properties.html)
- [shardul.dev: Most Useful kubectl Plugins](https://shardul.dev/most-useful-kubectl-plugins/) In this article, you will have a look at the following kubectl plugins:
    - neat
    - view-secret
    - access-matrix
    - blame
    - df-pv
    - gke-outdated
- [howtogeek.com: Getting Started With Kubectl to Manage Kubernetes Clusters](https://www.howtogeek.com/devops/getting-started-with-kubectl-to-manage-kubernetes-clusters/) Kubernetes is a container orchestration engine that lets you deploy containerised workloads in a scalable way.
- [medium.com/@jake.page91: The guide to kubectl I never had](https://medium.com/@jake.page91/the-guide-to-kubectl-i-never-had-3874cc6074ff)
- [itnext.io: Kubernetes Contexts: Complete Guide for Developers](https://itnext.io/kubernetes-contexts-complete-guide-for-developers-7ea5b2fc75c7) An introduction to Kubeconfig and Contexts. It’s finally time to understand how kubectl connects to Kubernetes.

## Kubectl Cheat Sheets

- [Kubectl Cheat Sheets](cheatsheets.md)

## Kubectl aliases

- [ahmetb/kubectl-aliases](https://github.com/ahmetb/kubectl-aliases) Programmatically generated handy kubectl aliases. This repository contains a script to generate hundreds of convenient shell aliases for kubectl, so you no longer need to spell out every single command and --flag over and over again
- [blog.devgenius.io: Daily useful Kubernetes aliases](https://blog.devgenius.io/daily-useful-kubernetes-aliases-c35f7f411f39)

## Kubectl explain

- [kubectl explain](https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl_explain/)
- [==itnext.io: Using ‘kubectl explain’ for Custom Resources==](https://itnext.io/understanding-kubectl-explain-9d703396cc8) Goal: Explore if ‘kubectl explain’ can be used to discover static information about Custom Resources

```for r in $(kubectl api-resources|grep -v ^N|awk '{print $1}');do kubectl explain $r --recursive;done```

## Kubectl example

- [github.com/trstringer/kubectl-example](https://github.com/trstringer/kubectl-example) kubectl plugin to dump example helper resource templates

## Kubectl Autocomplete

- [Kubectl Autocomplete](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [kubectl Shell Autocomplete](https://blog.heptio.com/kubectl-shell-autocomplete-heptioprotip-48dd023e0bf3)
- [Kubernetes productivity tips and tricks 🌟](https://www.padok.fr/en/blog/kubernetes-productivity-tips)
- [complete-alias](https://github.com/cykerway/complete-alias) Automagical shell alias completion.

```bash
source <(kubectl completion bash) # setup autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.
```

You can also use a shorthand alias for kubectl that also works with completion:

```bash
alias k=kubectl
complete -F __start_kubectl k
```

## kubectl exec

- [containiq.com: Using kubectl exec | Shell Commands & Examples](https://www.containiq.com/post/using-kubectl-exec-shell-commands-examples) kubectl exec lets you start a shell session to containers running in your Kubernetes cluster. It’s a bit like SSH for Kubernetes. Here’s what you need to know to use this command as part of your cluster management procedures, including the cases where it makes the most sense.
- [itnext.io: Connect to containers using Kubectl Exec](https://itnext.io/connect-to-containers-using-kubectl-exec-b1fb5c171f03) In this article, we will look at the kubectl exec command to show how to get a shell into a running container in your Kubernetes (K8S) cluster, and how to run individual commands on a container with some useful examples.
- [goteleport.com: kubectl exec vs SSH](https://goteleport.com/blog/ssh-vs-kubectl/) This article compares `kubectl exec` and SSH and discusses their strengths and weaknesses

## kubectl scale

- [==containiq.com: Using Kubectl Scale | Tutorial and Best Practices==](https://www.containiq.com/post/kubectl-scale) kubectl scale is one of the many tools that helps you manage your Kubernetes deployments. In this article, you'll learn how this tool can be used, as well as best practices for use.

## kubectl debug

- [hackernoon.com: How to Work With the Kubectl Debug Command](https://hackernoon.com/how-to-work-with-the-kubectl-debug-command)

## List all resources and sub resources that you can constrain with RBAC

- kind of a handy way to see all thing things you can affect with Kubernetes RBAC. This will list all resources and sub resources that you can constrain with RBAC. If you want to see just subresources append "| grep {name}/":

```bash
kubectl get --raw /openapi/v2  | jq '.paths | keys[]'
```

## Copy a configMap in kubernetes between namespaces

- Copy a configMap in kubernetes between namespaces with deprecated "--export" flag:

```bash
kubectl get configmap --namespace=<source> <configmap> --export -o yaml | sed "s/<source>/<dest>/" | kubectl apply --namespace=<dest> -f -
```

- [Flag export deprecated in kubernetes 1.14](https://github.com/kubernetes/kubernetes/pull/73787). Instead following command can be used:

```bash
kubectl get configmap <configmap-name> --namespace=<source-namespace> -o yaml | sed ‘s/namespace: <from-namespace>/namespace: <to-namespace>/’ | kubectl create -f
```

- Reference: [Copy a configMap in kubernetes between namespaces](https://stackoverflow.com/questions/55515594/is-there-a-way-to-share-a-configmap-in-kubernetes-between-namespaces)

## Copy secrets in kubernetes between namespaces

- [Copy secrets between namespaces](https://stackoverflow.com/questions/55515594/is-there-a-way-to-share-a-configmap-in-kubernetes-between-namespaces):

```bash
kubectl get secret <secret-name> --namespace=<source> -o yaml | sed ‘s/namespace: <from-namespace>/namespace: <to-namespace>/’ | kubectl create -f
```

## Export resources with kubectl and python

- Export resources with [zoidbergwill/export.sh](https://gist.github.com/zoidbergwill/6af8c80cc5b706e2adcf25df3dc2f7e1#file-export_resources-py), by [zoidbergwill](https://gist.github.com/zoidbergwill)

## Buildkit CLI for kubectl a drop in replacement for docker build

- [container-registry.com: Lifting Developers’ Productivity 🌟](https://container-registry.com/posts/productivity-lift-buildkit-cli-for-kubectl/) With BuildKit CLI for kubectl a drop in replacement for docker build. In this post, you will learn how to build container images with BuildKit CLI for kubectl (a replacement for the `docker build` command)
- [vmware-tanzu/buildkit-cli-for-kubectl (kubectl plugin)](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl) BuildKit CLI for kubectl is a tool for building container images with your Kubernetes cluster.

## Kubectl Alternatives

- [Helm and Kubernetes](helm.md)
- [Kubectl plugins and tools](kubernetes.md#kubectl-plugins)

### Manage Kubernetes (K8s) objects with Ansible Kubernetes Module

- [Manage Kubernetes (K8s) objects](https://docs.ansible.com/ansible/latest/modules/k8s_module.html)
- [ansibleforkubernetes.com 🌟](https://www.ansibleforkubernetes.com/)

### Jenkins Kubernetes Plugins

- [Jenkins Kubernetes Plugin](https://plugins.jenkins.io/kubernetes/)
- [Kubernetes Continuous Deploy](https://plugins.jenkins.io/kubernetes-cd/)

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/E2pP1MOfo3g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>

## Tweets

??? note "Click to expand!"

    <center>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">TIL: How to create Kubernetes manifests real quick 🤯<br><br>Use kubectl create --dry-run=client -o yaml<br><br>Example:<br><br>```<br>kubectl create deployment foo \<br> --image=nginx:1.21 \<br> --dry-run=client \<br> -o yaml<br>```</p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1483180111579000834?ref_src=twsrc%5Etfw">January 17, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>