# Security Policy as Code 
- [Introduction](#introduction)
- [Open Policy Agent (OPA)](#open-policy-agent-opa)
    - [Open Policy Agent in Kubernetes](#open-policy-agent-in-kubernetes)
    - [Open Policy Agent in OpenShift](#open-policy-agent-in-openshift)
    - [Open Policy Agent in Cloudflare Workers](#open-policy-agent-in-cloudflare-workers)
    - [Policy as Code in Terraform Cloud](#policy-as-code-in-terraform-cloud)
- [Kyverno](#kyverno)
- [Cloud Custodian](#cloud-custodian)

## Introduction
- [Dzone: DevOps Security at Scale - Security Policy as Code](https://dzone.com/articles/devops-security-at-scale)
- [searchitoperations.techtarget.com: Kubernetes policy project takes enterprise IT by storm](https://searchitoperations.techtarget.com/news/252467102/Kubernetes-policy-project-takes-enterprise-IT-by-storm) A Kubernetes-friendly compliance as code project hosted by the CNCF has caught on among large enterprises in the first half of 2019, largely through word of mouth.
- [amazon.com: Policy-based countermeasures for Kubernetes – Part 1](https://aws.amazon.com/blogs/containers/policy-based-countermeasures-for-kubernetes-part-1/)

## Open Policy Agent (OPA)
- [OPA Open Policy Agent 🌟](https://www.openpolicyagent.org/)
- [magalix.com: Integrating Open Policy Agent (OPA) With Kubernetes 🌟](https://www.magalix.com/blog/integrating-open-policy-agent-opa-with-kubernetes-a-deep-dive-tutorial)
- [fugue.co: 5 tips for using the Rego language for Open Policy Agent (OPA)](https://www.fugue.co/blog/5-tips-for-using-the-rego-language-for-open-policy-agent-opa)
- [PolicyHub CLI, a CLI tool that makes Rego policies searchable 🌟](https://github.com/policy-hub/policy-hub-cli) a list of community OPA policies
- [blog.styra.com: Integrating Identity: OAUTH2 and OPENID CONNECT in Open Policy Agent](https://blog.styra.com/blog/integrating-identity-oauth2-and-openid-connect-in-open-policy-agent)
- [blog.styra.com: Rego Unit Testing](https://blog.styra.com/blog/rego-unit-testing)
- [github.com/instrumenta/policies: A set of shared policies for use with Conftest and other Open Policy Agent tools](https://github.com/instrumenta/policies)
- [itprotoday.com: Who Needs Open Policy Agent?](https://www.itprotoday.com/devops-and-software-development/who-needs-open-policy-agent) Open Policy Agent makes it possible to create a single set of configuration rules and deploy them automatically across a large-scale environment.
- [blog.styra.com: Dynamic Policy Composition for OPA](https://blog.styra.com/blog/dynamic-policy-composition-for-opa)
- [blog.styra.com: 5 OPA Deployment Performance Models for Microservices](https://blog.styra.com/blog/5-opa-deployment-performance-models-for-microservices)
- [blog.styra.com: Open Policy Agent: The Top 5 Kubernetes Admission Control Policies](https://blog.styra.com/blog/open-policy-agent-the-top-5-kubernetes-admission-control-policies)
- [thenewstack.io: Getting Open Policy Agent Up and Running](https://thenewstack.io/getting-open-policy-agent-up-and-running/)

### Open Policy Agent in Kubernetes
- [infracloud.io: Kubernetes Pod Security Policies with Open Policy Agent](https://www.infracloud.io/kubernetes-pod-security-policies-opa/)
- [banzaicloud.com: Istio and Kubernetes ft. OPA policies](https://banzaicloud.com/blog/istio-opa/)
- [fugue.co: 5 tips for using the Rego language for Open Policy Agent (OPA)](https://www.fugue.co/blog/5-tips-for-using-the-rego-language-for-open-policy-agent-opa)
- [medium: Ensure Content Trust on Kubernetes using Notary and Open Policy Agent](https://medium.com/@siegert.maximilian/ensure-content-trust-on-kubernetes-using-notary-and-open-policy-agent-485ab3a9423c) A detailed guide to help you to ensure that only signed images can get deployed on the cluster. In this blog post you will learn how to enforce image trust on your Kubernetes Cluster by fully relying on two well known CNCF hosted open source solutions: Notary and Open Policy Agent (OPA).
- [kubermatic.com: Using Open Policy Agent With Kubermatic Kubernetes Platform](https://www.kubermatic.com/blog/using-open-policy-agent-with-kubermatic/)
- [k8s-security-policies](https://github.com/raspbernetes/k8s-security-policies) This repository provides a security policies library that is used for securing Kubernetes clusters configurations. The security policies are created based on CIS Kubernetes benchmark and rules defined in Kubesec.io. The policies are written in Rego, a high-level declarative language, its purpose-built for expressing policies over complex hierarchical data structures. For detailed information on Rego see the Policy Language documentation.
- [medium: Deploying Open Policy Agent (OPA) on a GKE cluster — Step by Step](https://medium.com/linkbynet/deploying-opa-on-a-gke-cluster-da4d3d77812c)
- [github.com/instrumenta/policies: A set of shared policies for use with Conftest and other Open Policy Agent tools 🌟](https://github.com/instrumenta/policies)
- [blog.styra.com: Using OPA with GitOps to speed Cloud-Native development](https://blog.styra.com/blog/using-opa-with-gitops-to-speed-cloud-native-development)

### Open Policy Agent in OpenShift
- [blog.openshift.com: Fine-Grained Policy Enforcement in OpenShift with Open Policy Agent 🌟](https://blog.openshift.com/fine-grained-policy-enforcement-in-openshift-with-open-policy-agent/)

### Open Policy Agent in Cloudflare Workers
* [compile OpenPolicyAgent policies into WebAssembly and run them on the edge](https://github.com/open-policy-agent/contrib/tree/master/wasm/cloudflare-worker)

### Policy as Code in Terraform Cloud
- [hashicorp.com: Securing Infrastructure In Application Pipelines](https://www.hashicorp.com/resources/securing-infrastructure-in-application-pipelines/) Learn how to use policy as code in Terraform Cloud to securely deliver applications.

## Kyverno
- [Kyverno 🌟](https://kyverno.io/) Kubernetes Native Policy Management. Open Policy Agent? That’s old school. Securely manage workloads on your kubernetesio clusters with this handy new tool, Kyverno.Kyverno is a policy engine designed for Kubernetes. With Kyverno, policies are managed as Kubernetes resources and no new language is required to write policies. This allows using familiar tools such as kubectl, git, and kustomize to manage policies. Kyverno policies can validate, mutate, and generate Kubernetes resources. The Kyverno CLI can be used to test policies and validate resources as part of a CI/CD pipeline. [youtube: The Way of the Future | Kubernetes Policy Management with Kyverno](https://www.youtube.com/watch?v=8fgrjBnxqi0&t=270s&ab_channel=AppSecEngineer)
- [neonmirrors.net: Kubernetes Policy Comparison: OPA/Gatekeeper vs Kyverno 🌟](https://neonmirrors.net/post/2021-02/kubernetes-policy-comparison-opa-gatekeeper-vs-kyverno/)
- [kyverno.io: 56 sample policies 🌟](https://kyverno.io/policies/)

## Cloud Custodian
- [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian) is a rules engine for managing public cloud accounts and resources. It allows users to define policies to enable a well managed cloud infrastructure, that's both secure and cost optimized.
