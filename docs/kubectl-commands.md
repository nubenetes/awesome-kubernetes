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

- [ibm.com: 8 Kubernetes Tips and Tricks 🌟](https://www.ibm.com/cloud/blog/8-kubernetes-tips-and-tricks) Most of the tips given below are using kubectl, a powerful command-line tool that allows you to execute commands against Kubernetes clusters.
    - Set default namespaces
    - Helpful aliases to save time
    - YAML editing with vi
    - Create YAML from kubectl commands
    - Switching between Kubernetes namespaces
    - Shell auto-completion
    - Viewing resource utilization
    - Extend kubectl and create your own commands using raw outputs
- [opensource.com: 5 useful ways to manage Kubernetes with kubectl](https://opensource.com/article/21/7/kubectl) Learn kubectl to enhance how you interact with Kubernetes.
- [hackerxone.com: How to Manage Single & Multiple Kubernetes Clusters using kubectl & kubectx in Linux](https://www.hackerxone.com/2021/07/10/how-manage-single-multiple-kubernetes-clusters-using-kubectl-kubectx-linux/)
- [Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere/) This tutorial shows you how to expose your private Kubernetes API server to the Internet, so that you can manage your cluster from anywhere, just like you would with a cloud offering.
- [dev.to: Open a command prompt in a Kubernetes cluster](https://dev.to/eldadak/open-a-command-prompt-in-a-kubernetes-cluster-206g) This starts up a pod (in the default namespace by default) and opens a command line in the given container. As I'm running as root, I can install anything I need for debugging and testing right in my cluster.
- [akhilsharma.work: Checking Kubernetes API Calls using kubectl](https://akhilsharma.work/checking-kubernetes-api-calls-using-kubectl/) In order to interact, we can simply use `kubectl`. Just add verbose logging level of 8+ and you will get the API calls!
    - `kubectl get pods -v=8`
    - `kubectl create job my-job --image=busybox --dry-run=server -v8`
- [inlets.dev: Fixing the Developer Experience of Kubernetes Port Forwarding](https://inlets.dev/blog/2022/06/24/fixing-kubectl-port-forward.html) This article shows you some of the frustrations of using kubectl for port-forwarding and how to fix the developer experience.
- [superbrothers/zsh-kubectl-prompt 🌟](https://github.com/superbrothers/zsh-kubectl-prompt) Display information about the kubectl current context and namespace in zsh prompt.
- [hidetatz/kubecolor 🌟](https://github.com/hidetatz/kubecolor) colorizes kubectl output
- [==learnitguide.net: How to Create ConfigMap from Properties File Using K8s Client==](https://www.learnitguide.net/2023/04/how-to-create-configmap-from-properties.html)
- [shardul.dev: Most Useful kubectl Plugins](https://shardul.dev/most-useful-kubectl-plugins/) In this article, you will have a look at the following kubectl plugins:
    - neat
    - view-secret
    - access-matrix
    - blame
    - df-pv
    - gke-outdated
- [howtogeek.com: Getting Started With Kubectl to Manage Kubernetes Clusters](https://www.howtogeek.com/devops/getting-started-with-kubectl-to-manage-kubernetes-clusters/) Kubernetes is a container orchestration engine that lets you deploy containerised workloads in a scalable way.

## Kubectl Cheat Sheets

- [Kubectl Cheat Sheets](cheatsheets.md)

## Kubectl aliases

- [ahmetb/kubectl-aliases](https://github.com/ahmetb/kubectl-aliases) Programmatically generated handy kubectl aliases. This repository contains a script to generate hundreds of convenient shell aliases for kubectl, so you no longer need to spell out every single command and --flag over and over again

## Kubectl explain

- [kubectl explain](https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl_explain/)

```for r in $(kubectl api-resources|grep -v ^N|awk '{print $1}');do kubectl explain $r --recursive;done```

## Kubectl example

- [github.com/trstringer/kubectl-example](https://github.com/trstringer/kubectl-example) kubectl plugin to dump example helper resource templates

## Kubectl Autocomplete

- [Kubectl Autocomplete](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
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

- [goteleport.com: kubectl exec vs SSH](https://goteleport.com/blog/ssh-vs-kubectl/) This article compares `kubectl exec` and SSH and discusses their strengths and weaknesses

## kubectl scale


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


## Copy secrets in kubernetes between namespaces


```bash
kubectl get secret <secret-name> --namespace=<source> -o yaml | sed ‘s/namespace: <from-namespace>/namespace: <to-namespace>/’ | kubectl create -f
```

## Export resources with kubectl and python


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