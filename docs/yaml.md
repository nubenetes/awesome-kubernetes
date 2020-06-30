# Templating YAML with YAML Processors. Static Checking of Kubernetes YAML Files

## Templating YAML Files
- [wikipedia: YAML](https://en.wikipedia.org/wiki/YAML)
- [thoughtworks.com: Templating in YAML](https://www.thoughtworks.com/radar/techniques/templating-in-yaml) As infrastructures grow in complexity, so do the configuration files that define them. Tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [Kubernetes](https://www.thoughtworks.com/radar/platforms/kubernetes) and [Helm](https://www.thoughtworks.com/radar/tools/helm) expect configuration files in JSON or YAML syntax, presumably in an attempt to make them easy to write and process. However, in most cases, teams quickly reach the point where they have some parts that are similar but not quite the same, for example, when the same service must be deployed in different regions with a slightly different setup. For such cases tools offer templating in YAML (or JSON), which has caused a huge amount of [frustration with practitioners](https://leebriggs.co.uk/blog/2019/02/07/why-are-we-templating-yaml.html). The problem is that the syntax of JSON and YAML requires all sorts of awkward compromises to graft templating features such as conditionals and loops into the files. **We recommend using an API from a programming language instead or, when this is not an option, a templating system in a programming language, either a general-purpose language such as Python or something specialized such as [Jsonnet](https://jsonnet.org/).**
- [Steve Horsfield: DevOps tricks - Templating YAML files](https://stevehorsfield.wordpress.com/2019/08/13/devops-tricks-templating-yaml-files/) Basic text tools fall foul of YAML’s indentation sensitivity. On the other hand, **YAML tools like [ytt](https://get-ytt.io/) are pretty difficult to interpret.** In my case, I opted for a small [jq](https://stedolan.github.io/jq/) program executed via [yq](https://mikefarah.gitbook.io/yq/).

### YAML Processors 
- [github.com/topics/yaml-processor](https://github.com/topics/yaml-processor)
- [ytt](https://get-ytt.io/) is a templating tool that understands YAML structure allowing you to focus on your data instead of how to properly escape it.
- You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/). 
- [yq 🌟](https://mikefarah.gitbook.io/yq/) is a lightweight and portable command-line YAML processor. The aim of the project is to be the [jq](https://github.com/stedolan/jq) or sed of yaml files.

## Templating JSON Files
- [wikipedia: JSON](https://en.wikipedia.org/wiki/JSON)
- [Jsonnet](https://jsonnet.org/) A data templating language for app and tool developers

## Static Checking of Kubernetes YAML Files
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