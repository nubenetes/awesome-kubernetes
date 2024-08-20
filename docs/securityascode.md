# Security Policy as Code

1. [Introduction](#introduction)
2. [Open Policy Agent (OPA)](#open-policy-agent-opa)
    1. [Open Policy Agent in Kubernetes](#open-policy-agent-in-kubernetes)
    2. [Open Policy Agent in OpenShift](#open-policy-agent-in-openshift)
    3. [Open Policy Agent in Cloudflare Workers](#open-policy-agent-in-cloudflare-workers)
    4. [Policy as Code in Terraform Cloud](#policy-as-code-in-terraform-cloud)
    5. [Other OPA based solutions](#other-opa-based-solutions)
3. [Other Policy as Code Scanning Tools](#other-policy-as-code-scanning-tools)
4. [Kyverno](#kyverno)
    1. [Kyverno E-Learning](#kyverno-e-learning)
5. [Cloud Custodian](#cloud-custodian)
6. [Apolicy](#apolicy)
7. [Azure Policy](#azure-policy)

## Introduction

- [Dzone: DevOps Security at Scale - Security Policy as Code](https://dzone.com/articles/devops-security-at-scale)
- [searchitoperations.techtarget.com: Kubernetes policy project takes enterprise IT by storm](https://searchitoperations.techtarget.com/news/252467102/Kubernetes-policy-project-takes-enterprise-IT-by-storm) A Kubernetes-friendly compliance as code project hosted by the CNCF has caught on among large enterprises in the first half of 2019, largely through word of mouth.
- [amazon.com: Policy-based countermeasures for Kubernetes – Part 1](https://aws.amazon.com/blogs/containers/policy-based-countermeasures-for-kubernetes-part-1/)
- [medium: Automate policies enforcement with Policy-as-Code 🌟](https://medium.com/airwalk/automate-policies-enforcement-with-policy-as-code-2f20aac9e2b0)
- [blog.gitguardian.com: What is Policy-as-Code? An Introduction to Open Policy Agent](https://blog.gitguardian.com/what-is-policy-as-code-an-introduction-to-open-policy-agent/) Learn the benefits of policy as code and start testing your policies for cloud-native environments.

## Open Policy Agent (OPA)

- [OPA Open Policy Agent 🌟](https://www.openpolicyagent.org/)
- OPA is most often used as an admission controller in Kubernetes. An admission controller is where all the semantic validation of Kubernetes resources occur before resources are persisted to etcd and controllers go off and start doing work.
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
    - Trusted Repo
    - Label Safety
    - Privileged Mode
    - Ingress
    - Egress
- [thenewstack.io: Getting Open Policy Agent Up and Running](https://thenewstack.io/getting-open-policy-agent-up-and-running/)
- [siegert-maximilian.medium.com: Ensure Content Trust on Kubernetes using Notary and Open Policy Agent](https://siegert-maximilian.medium.com/ensure-content-trust-on-kubernetes-using-notary-and-open-policy-agent-485ab3a9423c) A detailed guide to help you to ensure that only signed images can get deployed on the cluster
- [blog.styra.com: Policy-based infrastructure guardrails with Terraform and OPA 🌟](https://blog.styra.com/blog/policy-based-infrastructure-guardrails-with-terraform-and-opa)
- [medium: Automated Manifest File Validation Using Open Policy Agent and GitHub Actions | Ravindu Sandeepa Rathugama](https://medium.com/@ravindursr/automated-manifest-file-validation-using-open-policy-agent-and-github-actions-697fa9fd74f0)
- [thenewstack.io: Weaveworks Adds Policy as Code to Secure Kubernetes Apps (Magalix)](https://thenewstack.io/weaveworks-adds-policy-as-code-to-secure-kubernetes-apps/) - [Magalix](https://www.magalix.com)
- [fugue.co: Securing a Kubernetes pod with Regula and Open Policy Agent](https://www.fugue.co/blog/securing-a-kubernetes-pod-with-regula-and-open-policy-agent)
- [dev.to: Load external data into OPA: The Good, The Bad, and The Ugly](https://dev.to/permit_io/load-external-data-into-opa-the-good-the-bad-and-the-ugly-26lc) There are several ways to create a data fetching mechanism for the Open Policy Agent - each of them has its pros and cons. In this guide, you will compare and decide which one is the best for you.
- [inspektor.cloud: Evaluating open policy agent in rust using wasm](https://inspektor.cloud/blog/evaluating-open-policy-agent-in-rust-using-wasm/)
- [medium.com/4th-coffee: What is Policy-as-Code? An Introduction to Open Policy Agent](https://medium.com/4th-coffee/what-is-policy-as-code-an-introduction-to-open-policy-agent-6098463f8461)

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
- [medium.com/gitguardian: What is Policy-as-Code? An Introduction to Open Policy Agent](https://medium.com/gitguardian/what-is-policy-as-code-an-introduction-to-open-policy-agent-dba1400bb030)

### Open Policy Agent in OpenShift

- [blog.openshift.com: Fine-Grained Policy Enforcement in OpenShift with Open Policy Agent 🌟](https://blog.openshift.com/fine-grained-policy-enforcement-in-openshift-with-open-policy-agent/)

### Open Policy Agent in Cloudflare Workers

- [compile OpenPolicyAgent policies into WebAssembly and run them on the edge](https://github.com/open-policy-agent/contrib/tree/master/wasm/cloudflare-worker)

### Policy as Code in Terraform Cloud

- [hashicorp.com: Securing Infrastructure In Application Pipelines](https://www.hashicorp.com/resources/securing-infrastructure-in-application-pipelines/) Learn how to use policy as code in Terraform Cloud to securely deliver applications.

### Other OPA based solutions

- [Fugue: Container and Kubernetes. Runtime infrastructure security](https://www.fugue.co/container-kubernetes) - [darkreading.com: Fugue Adds Kubernetes Security Checks to Secure Infrastructure-as-Code](https://www.darkreading.com/dr-tech/fugue-adds-kubernetes-security-checks-to-secure-infrastructure-as-code) Developers can apply proper security controls as they programmatically deploy Kubernetes clusters.

## Other Policy as Code Scanning Tools

- [thenewstack.io: Yor Automates Tagging for Infrastructure as Code](https://thenewstack.io/yor-automates-tagging-for-infrastructure-as-code/)
- [yor.io](https://yor.io/) Automated IaC tag and trace. Yor is an open-source tool that automatically tags infrastructure as code (IaC) templates with attribution and ownership details, unique IDs that get carried across to cloud resources, and any other need-to-know information. Run Yor as a pre-commit hook or in your CI/CD pipeline for code to cloud traceability and auditability.
- [checkov.io](https://www.checkov.io/) policy as code scanning tool
- [aws.amazon.com: Policy-based countermeasures for Kubernetes – Part 1](https://aws.amazon.com/es/blogs/containers/policy-based-countermeasures-for-kubernetes-part-1/) Choosing the right policy-as-code solution for your Kubernetes cluster:
    - OPA
    - Gatekeeper
    - Kyverno
    - k-rail
    - [MagTape](https://github.com/tmobile/magtape) Policy as code for kubernetes
- [Selefra: Selefra is an open-source policy-as-code software that provides analytics for multi-cloud and SaaS.](https://github.com/selefra/selefra) Selefra means "select * from infrastructure". It is an open-source infrastructure-as-code software that provides analysis for multi-cloud and SaaS environments, including over 30 services such as AWS, GCP, Azure, Alibaba Cloud, Kubernetes, Github, Cloudflare, and Slack.

## Kyverno

- [Kyverno 🌟](https://kyverno.io/) Kubernetes Native Policy Management. Open Policy Agent? That’s old school. Securely manage workloads on your kubernetesio clusters with this handy new tool, Kyverno.Kyverno is a policy engine designed for Kubernetes. With Kyverno, policies are managed as Kubernetes resources and no new language is required to write policies. This allows using familiar tools such as kubectl, git, and kustomize to manage policies. Kyverno policies can validate, mutate, and generate Kubernetes resources. The Kyverno CLI can be used to test policies and validate resources as part of a CI/CD pipeline. [youtube: The Way of the Future | Kubernetes Policy Management with Kyverno](https://www.youtube.com/watch?v=8fgrjBnxqi0&t=270s&ab_channel=AppSecEngineer)
- [venturebeat.com: How Nirmata plans to ‘conquer Kubernetes complexity’ with open source Kyverno](https://venturebeat.com/2021/08/10/how-nirmata-plans-to-conquer-kubernetes-complexity-with-open-source-kyverno/)
- [neonmirrors.net: Kubernetes Policy Comparison: OPA/Gatekeeper vs Kyverno 🌟](https://neonmirrors.net/post/2021-02/kubernetes-policy-comparison-opa-gatekeeper-vs-kyverno/)
- [kyverno.io: 56 sample policies 🌟](https://kyverno.io/policies/)
- [dev.to: Using Kyverno To Enforce EKS Best Practices](https://dev.to/rinkiyakedad/using-kyverno-to-enforce-eks-best-practices-cad)
- Tip: Use kyverno to monitor for usage of deprecated resources ahead of the Kubernetes 1.22 release (validation check to scan and report usage of deprecated resources) - [ref](https://github.com/kyverno/policies/issues/80#issuecomment-882332198) - [ref2](https://twitter.com/Marcus_Noble_/status/1417007780888825856)
- [aws.amazon.com: Easy as one-two-three policy management with Kyverno on Amazon EKS 🌟](https://aws.amazon.com/blogs/containers/easy-as-one-two-three-policy-management-with-kyverno-on-amazon-eks/)
- [kyverno.io: Mutating Resources](https://kyverno.io/docs/writing-policies/mutate/) Modify resources during admission control (Kyverno supports mutating resources).
- [squadcast.com: Kyverno - Policy Management in Kubernetes 🌟](https://www.squadcast.com/blog/kyverno-policy-management-in-kubernetes)
- [neonmirrors.net: Exploring Kyverno: Part 3, Generation](https://neonmirrors.net/post/2020-12/exploring-kyverno-part3/)
- [kyverno.io: Check deprecated APIs 🌟](https://kyverno.io/policies/best-practices/check_deprecated_apis/) Kubernetes APIs are sometimes deprecated and removed after a few releases. As a best practice, older API versions should be replaced with newer versions. This policy validates for APIs that are deprecated or scheduled for removal. Note that checking for some of these resources may require modifying the Kyverno ConfigMap to remove filters.
- [kyverno.io: Generating resources into existing namespaces](https://kyverno.io/docs/writing-policies/generate/#generating-resources-into-existing-namespaces)
- [kyverno.io: Add Pod Proxies](https://kyverno.io/policies/other/add-pod-proxies/) A kyverno policy to inject K8s Pod proxy env variables.
- [kyverno.io: Auto-Gen Rules for Pod Controllers](https://kyverno.io/docs/writing-policies/autogen/) Automatically generate rules for Pod controllers.
- [kyverno.io: Require PodDisruptionBudget](https://kyverno.io/policies/other/require_pdb/) Use this kyverno sample to prevent app downtime by requiring all kubernetesio Deployments have a corresponding PodDisruptionBudget.
- [nirmata.com: Kubernetes Supply Chain Policy Management with Cosign and Kyverno](https://nirmata.com/2021/08/12/kubernetes-supply-chain-policy-management-with-cosign-and-kyverno/)
- [neonmirrors.net: Exploring Kyverno: Introduction 🌟](https://neonmirrors.net/post/2020-11/exploring-kyverno-intro/)
- [nirmata.com: Introducing Kyverno 1.4.2: Trusted And More Efficient!](https://nirmata.com/2021/08/18/introducing-kyverno-1-4-2-trusted-and-more-efficient/)
- [searchitoperations.techtarget.com: CNCF policy-as-code project bridges Kubernetes security gaps](https://searchitoperations.techtarget.com/news/252505548/CNCF-policy-as-code-project-bridges-Kubernetes-security-gaps) Kyverno, a CNCF policy-as-code sandbox project, can help platform engineers navigate the transition toward the successor to Kubernetes pod security policies.
- [Policy Reporter 🌟](https://github.com/kyverno/policy-reporter) Creates Prometheus Metrics for PolicyReports and ClusterPolicyReports. Ships with an optional Web UI and can send new Results to different Clients like Loki and Elasticsearch. Provides a optional Monitoring Subchart with a ServiceMonitor and Grafana Dashboards for the Prometheus Operator.
- [sesin.at: Securing Kubernetes with Kyverno: How to Protect Your Users From Themselves by Ritesh Patel](https://www.sesin.at/2021/08/28/securing-kubernetes-with-kyverno-how-to-protect-your-users-from-themselves-by-ritesh-patel/)
- [movi.hashnode.dev: Simplify Kubernetes Cluster Management with Kyverno](https://movi.hashnode.dev/simplify-kubernetes-cluster-management-with-kyverno-ckt6yxjqy0duy95s14groe7h4) Kyverno, a policy engine designed specifically for Kubernetes.
- [arun-sisodiya.medium.com: Kyverno — A Kubernetes native policy manager (Policy as Code)](https://arun-sisodiya.medium.com/kyverno-a-policy-manager-for-kubernetes-286f6e082062)
- [dev.to: Default Kyverno Policies for OpenEBS](https://dev.to/niveditacoder/default-kyverno-policies-for-openebs-4abf)
- [cloud.redhat.com: Automate Your Security Practices and Policies on OpenShift With Kyverno 🌟](https://cloud.redhat.com/blog/automate-your-security-practices-and-policies-on-openshift-with-kyverno)
- [A Kyverno policy to block custom snippet configurations for Kubernetes Nginx ingress (CVE-2021-25742](https://github.com/kubernetes/ingress-nginx/issues/7837)
- [==kyverno.io: Restrict Image Registries==](https://kyverno.io/policies/best-practices/restrict_image_registries/restrict_image_registries/) kyverno
 has a solid set of kubernetes policies and excellent documentation out of the box!
- [dev.to: Using Kyverno Policies for Kubernetes Governance](https://dev.to/mda590/using-kyverno-policies-for-kubernetes-governance-3e17)
- [kyverno.io: Implementing your best practices is simple with kyverno](https://kyverno.io/policies/best-practices/require_probes/require_probes/)
    1. Startup Probe
    2. Liveness Probe
    3. Readiness Probe
    4. Graceful shutdown - be able to handle a sigterm in kubernetes

- [medium.com/compass-true-north: Governing Multi-Tenant Kubernetes Clusters with Kyverno](https://medium.com/compass-true-north/governing-multi-tenant-kubernetes-clusters-with-kyverno-3e11ba4a64ad)
- [medium.com/@haseebshaukat2: Kyverno — Policy Engine for Kubernetes | Muhammad Haseeb Shaukat](https://medium.com/@haseebshaukat2/kyverno-policy-engine-for-kubernetes-b49f3fac43b9)
- [youtube: The Rise of Kubernetes Policy Engine | Ep 57](https://www.youtube.com/watch?v=0TvhTXddRGE&t=12s) Learn how to prepare for Pod Security Policies removal in Kubernetes V1.25 with Kyverno 1.8:
    - YAML signing and verification
    - Pod security admission integrations
    - Clone multiple resources
    - OpenTelemetry
    - Multi-tenancy
- [medium.com/compass-true-north: Governing Multi-Tenant Kubernetes Clusters with Kyverno](https://medium.com/compass-true-north/governing-multi-tenant-kubernetes-clusters-with-kyverno-3e11ba4a64ad) With Kyverno:
    - Invalid resources can be blocked with helpful errors
    - Misconfigured resources can be corrected on the fly
    - New resources can be dynamically generated
- [blog.sigstore.dev: How to verify container images with Kyverno using KMS, Cosign, and Workload Identity](https://blog.sigstore.dev/how-to-verify-container-images-with-kyverno-using-kms-cosign-and-workload-identity-1e07d2b85061/)
- [medium.com/@glen.yu: Why I prefer Kyverno over Gatekeeper for native Kubernetes policy management](https://medium.com/@glen.yu/why-i-prefer-kyverno-over-gatekeeper-for-native-kubernetes-policy-management-35a05bb94964) I used to use Open Policy Agent Gatekeeper for Kubernetes policies but personally found writing new policies to be quite difficult with a steep learning curve. I then decided to give Kyverno a try and was really impressed with how easy it was to use.

### Kyverno E-Learning

- [appsecengineer.com: Kubernetes Policy Management with Kyverno](https://appsecengineer.com/courses/kubernetes-policy-management-with-kyverno/)

## Cloud Custodian

- [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian) is a rules engine for managing public cloud accounts and resources. It allows users to define policies to enable a well managed cloud infrastructure, that's both secure and cost optimized.

## Apolicy

- [Apolicy](https://apolicy.io/)
- [sysdig.com: Sysdig and Apolicy join forces to help customers secure Infrastructure As Code and automate remediation](https://sysdig.com/blog/sysdig-and-apolicy-join-forces-to-help-customer-secure-infrastructure-as-code/)

## Azure Policy

- [Azure Policy](azure.md)