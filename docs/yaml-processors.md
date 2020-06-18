# YAML Processors and Static Checking of Kubernetes YAML Files
## YAML Processors
- [wikipedia: YAML](https://en.wikipedia.org/wiki/YAML)
- [github.com/topics/yaml-processor](https://github.com/topics/yaml-processor)
- You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/). 
- [yq 🌟](https://mikefarah.gitbook.io/yq/) is a lightweight and portable command-line YAML processor. The aim of the project is to be the [jq](https://github.com/stedolan/jq) or sed of yaml files.
- [ytt](https://get-ytt.io/) is a templating tool that understands YAML structure allowing you to focus on your data instead of how to properly escape it.

## Static Checking of Kubernetes YAML Files
- The ecosystem of static checking of Kubernetes YAML files can be grouped in the following categories:
    - **API validators**: Tools in this category validate a given YAML manifest against the Kubernetes API server.
    - **Built-in checkers**: Tools in this category bundle opinionated checks for security, best practices, etc.
    - **Custom validators**: Tools in this category allow writing custom checks in several languages such as Rego and Javascript.
- [Validating Kubernetes YAML for best practice and policies 🌟](https://learnk8s.io/validating-kubernetes-yaml#config-lint) In this article, you will learn and compare six different tools:
    - [Kubeval](https://www.kubeval.com/)
    - [Kube-score](https://github.com/zegl/kube-score)
    - [Config-lint](https://stelligent.github.io/config-lint)
    - [Copper](https://github.com/cloud66-oss/copper)
    - [Conftest](https://www.conftest.dev/)
    - [Polaris](https://github.com/FairwindsOps/polaris)