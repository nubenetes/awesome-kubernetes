# Templating YAML with YAML Processors. Static Checking of Kubernetes YAML Files
- [Templating YAML Files](#templating-yaml-files)
    - [YAML anchors and aliases](#yaml-anchors-and-aliases)
    - [YAML Processors](#yaml-processors)
    - [Kubernetes examples](#kubernetes-examples)
    - [Scaffold. Built in snippets for creating k8s resources](#scaffold-built-in-snippets-for-creating-k8s-resources)
    - [Helm and Kustomize](#helm-and-kustomize)
- [Templating JSON Files](#templating-json-files)
- [Static Checking of Kubernetes YAML Files. Kubernetes YAML Validation Tools](#static-checking-of-kubernetes-yaml-files-kubernetes-yaml-validation-tools)
- [Alternatives](#alternatives)

## Templating YAML Files
- [wikipedia: YAML](https://en.wikipedia.org/wiki/YAML)
- [redhat.com: YAML for beginners](https://www.redhat.com/sysadmin/yaml-beginners) YAML is an easy, expressive, data-oriented language that distinguishes itself from document markup languages.
- [thoughtworks.com: Templating in YAML](https://www.thoughtworks.com/radar/techniques/templating-in-yaml) As infrastructures grow in complexity, so do the configuration files that define them. Tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [Kubernetes](https://www.thoughtworks.com/radar/platforms/kubernetes) and [Helm](https://www.thoughtworks.com/radar/tools/helm) expect configuration files in JSON or YAML syntax, presumably in an attempt to make them easy to write and process. However, in most cases, teams quickly reach the point where they have some parts that are similar but not quite the same, for example, when the same service must be deployed in different regions with a slightly different setup. For such cases tools offer templating in YAML (or JSON), which has caused a huge amount of [frustration with practitioners](https://leebriggs.co.uk/blog/2019/02/07/why-are-we-templating-yaml.html). The problem is that the syntax of JSON and YAML requires all sorts of awkward compromises to graft templating features such as conditionals and loops into the files. **We recommend using an API from a programming language instead or, when this is not an option, a templating system in a programming language, either a general-purpose language such as Python or something specialized such as [Jsonnet](https://jsonnet.org/).**
- [Steve Horsfield: DevOps tricks - Templating YAML files](https://stevehorsfield.wordpress.com/2019/08/13/devops-tricks-templating-yaml-files/) Basic text tools fall foul of YAML’s indentation sensitivity. On the other hand, **YAML tools like [ytt](https://get-ytt.io/) are pretty difficult to interpret.** In my case, I opted for a small [jq](https://stedolan.github.io/jq/) program executed via [yq](https://mikefarah.gitbook.io/yq/).
- [redhat.com: Understanding YAML for Ansible. Validating YAML files with YAMLlint 🌟](https://www.redhat.com/sysadmin/understanding-yaml-ansible) Ansible playbooks are written in YAML, YAML Ain't Markup Language. Understanding YAML syntax is a key to success with Ansible.
- [linuxhandbook.com: YAML Basics Every DevOps Engineer Must Know 🌟](https://linuxhandbook.com/yaml-basics/) 
- [developers.redhat.com: How to configure YAML schema to make editing files easier](https://developers.redhat.com/blog/2020/11/25/how-to-configure-yaml-schema-to-make-editing-files-easier/)
- [kubernetestutorials.com: Kubernetes : Introduction to YAML 🌟](https://kubernetestutorials.com/kubernetes-tutorials/kubernetes-introduction-to-yaml/)
- [betterprogramming.pub: YAML Tutorial: Get Started With YAML in 5 Minutes](https://betterprogramming.pub/yaml-tutorial-get-started-with-yaml-in-5-minutes-549d462972d8) Syntax, salient features, and advanced features.

### YAML anchors and aliases
- [yaml.org: Anchors and Aliases](https://yaml.org/spec/1.2/spec.html#id2765878)
- [support.atlassian.com: YAML anchors and aliases](https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/)
- [medium: Don’t Repeat Yourself with Anchors, Aliases and Extensions in Docker Compose Files](https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd)
- [docs.ansible.com: YAML anchors and aliases: sharing variable values](https://docs.ansible.com/ansible/latest/user_guide/playbooks_advanced_syntax.html#yaml-anchors-and-aliases-sharing-variable-values)

### YAML Processors 
- [github.com/topics/yaml-processor](https://github.com/topics/yaml-processor)
- [ytt](https://get-ytt.io/) is a templating tool that understands YAML structure allowing you to focus on your data instead of how to properly escape it.
- You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/). 
- [yq 🌟](https://mikefarah.gitbook.io/yq/) is a lightweight and portable command-line YAML processor. The aim of the project is to be the [jq](https://github.com/stedolan/jq) or sed of yaml files. `yq` allows to query the yaml tree and highlights it: 
    - ```k get svc a -o yaml | yq r -```
    - [dev.to: yq : A command line tool that will help you handle your YAML resources better 🌟](https://dev.to/vikcodes/yq-a-command-line-tool-that-will-help-you-handle-your-yaml-resources-better-8j9)
- [Kapitan](https://kapitan.dev/) Generic templated configuration management for Kubernetes, Terraform and other things.
- [yaml.sh](https://www.yaml.sh/) A YAML parser completely in bash. [Yaml.sh — YAML Sans Helm](https://medium.com/@KarlKFI/yaml-sh-yaml-sans-helm-e983a3dfdaec) 
- [yh - YAML Highlighter](https://github.com/andreazorzetto/yh) is YAML syntax highlighter that works nicely with kubectl output
- [Kubectl output options 🌟](https://gist.github.com/so0k/42313dbb3b547a0f51a547bb968696ba)

### Kubernetes examples
- [Kubernetes examples 🌟](https://k8s-examples.container-solutions.com/) A series of YAML references with canonical and as-simple-as-possible demonstrations of kubernetes functionality and features.

### Scaffold. Built in snippets for creating k8s resources 
- [cloud.google.com: configuring_with_snippets 🌟](https://cloud.google.com/code/docs/vscode/yaml-editing#configuring_with_snippets) GoogleCloudTech Code has built-in snippets for creating common resources (pod, service, configmap, etc). Plus diffing and dry-run of YAML.

### Helm and Kustomize
- [dex.dev: YAML Templating Solutions: Helm & Kustomize](https://www.dex.dev/dex-videos/templating-solutions) Writing config files by hand is like coding with Notepad instead of an IDE. Let's find a better way, and take an overview of the popular solutions Helm & Kustomize.

## Templating JSON Files
- [wikipedia: JSON](https://en.wikipedia.org/wiki/JSON)
- [json.org: Introducing JSON](https://www.json.org/json-en.html)
- [Jsonnet](https://jsonnet.org/) A data templating language for app and tool developers
- [Building a high performance JSON parser](https://dave.cheney.net/high-performance-json.html)
- [json-schema.org: Understanding JSON Schema 🌟](https://json-schema.org/understanding-json-schema/)

## Static Checking of Kubernetes YAML Files. Kubernetes YAML Validation Tools
- The ecosystem of static checking of Kubernetes YAML files can be grouped in the following categories:
    - **API validators**: Tools in this category validate a given YAML manifest against the Kubernetes API server.
    - **Built-in checkers**: Tools in this category bundle opinionated checks for security, best practices, etc.
    - **Custom validators**: Tools in this category allow writing custom checks in several languages such as Rego and Javascript.
- [Validating Kubernetes YAML for best practice and policies 🌟](https://learnk8s.io/validating-kubernetes-yaml) In this article, you will learn and compare six different tools:
    - [Kubeval](https://www.kubeval.com/)
    - [Kube-score](https://github.com/zegl/kube-score)
    - [Config-lint](https://stelligent.github.io/config-lint)
    - [Copper](https://github.com/cloud66-oss/copper)
    - [Conftest](https://www.conftest.dev/)
    - [Polaris](https://github.com/FairwindsOps/polaris)
- [kubevious.io: Top Kubernetes YAML Validation Tools](https://kubevious.io/blog/post/top-kubernetes-yaml-validation-tools/)

## Alternatives
- [ketch](https://theketch.io) - [civo.com: Deployments without YAML using Ketch](https://www.civo.com/learn/deployments-without-yaml-using-ketch)
    - [ketch: Getting Started](https://learn.theketch.io/docs/getting-started)
    - [github.com/shipa-corp/ketch](https://github.com/shipa-corp/ketch/) Ketch is an application delivery framework that facilitates the deployment and management of applications on Kubernetes using a simple command line interface.
- [shipa.io: DevOps Challenge – Kubernetes Deployment: Ketch vs YAML](https://www.shipa.io/ketch/devops-challenge-kubernetes-deployment-ketch-vs-yaml/)
    