# Security and DevSecOps. Container Security
- [Introduction](#introduction)
- [Kubernetes Threat Modelling](#kubernetes-threat-modelling)
- [Kubernetes Config Security Threats](#kubernetes-config-security-threats)
- [Security Linting on Kubernetes](#security-linting-on-kubernetes)
- [Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers](#multi-level-security-mls-vs-multi-category-security-mcs-make-secure-pipelines-with-podman-and-containers)
- [Project Calico](#project-calico)
- [Security Patterns for Microservice Architectures](#security-patterns-for-microservice-architectures)
- [Anchore Container Security Solutions for DevSecOps](#anchore-container-security-solutions-for-devsecops)
	- [Secure Container Based CI/CD Workflows](#secure-container-based-cicd-workflows)
	- [Securing Kubernetes With Anchore](#securing-kubernetes-with-anchore)
- [GitHub security](#github-security)
- [Databases in DMZ and Intranet](#databases-in-dmz-and-intranet)
- [Removing Credentials From Git Repo](#removing-credentials-from-git-repo)
- [Pentesting](#pentesting)
- [Credential Managers](#credential-managers)
	- [keycloak](#keycloak)
	- [Git Credential Manager Core](#git-credential-manager-core)
- [GitOps Secret Management](#gitops-secret-management)
	- [HashiCorp Vault](#hashicorp-vault)
	- [CyberArk and Ansible](#cyberark-and-ansible)
	- [SOPS for Kubernetes](#sops-for-kubernetes)
	- [Alternatives](#alternatives)
- [Serverless Security Best Practices](#serverless-security-best-practices)
- [Docker Images & Container Security](#docker-images--container-security)
- [Pod Security Policies](#pod-security-policies)
- [Kubernetes Network Policies](#kubernetes-network-policies)
- [Static Analysis SAST](#static-analysis-sast)
- [Kubernetes Security Tools](#kubernetes-security-tools)
- [Books](#books)

## Introduction
- [fiercesw.com: DevOps vs DevSecOps](https://fiercesw.com/devsecops-starter)
- [devopszone.info: DevSecOps Explained](https://www.devopszone.info/post/devsecops-explained)
- [linkedin: Dear Google, my data has left your building!](https://www.linkedin.com/pulse/dear-google-my-data-has-left-your-building-zakir-khan/)
- [snyk.io: The State of Open Source Security 2020](https://snyk.io/open-source-security-report/)
- [managedsentinel.com: Executive View — Current and Future Cybersecurity Architecture On One Page](https://www.managedsentinel.com/2019/05/23/cybersecurity-roadmap/)
- [Exploring the (lack of) security in a typical Docker and Kubernetes installation](https://www.neowin.net/news/exploring-the-lack-of-security-in-a-typical-docker-and-kubernets-installation/)
- [kalilinuxtutorials.com: Deploying & Securing Kubernetes Clusters](https://kalilinuxtutorials.com/deploying-securing-kubernetes-clusters/)
- [loves.cloud: Creating a fully automated DevSecOps CI/CD Pipeline](https://loves.cloud/creation-of-a-fully-automated-devsecops-cicd-pipeline/)
- [redhat.com: Balancing Linux security with usability](https://www.redhat.com/sysadmin/linux-security-usability) Your system should be secure, but open enough to serve its function. Here are some tips on how to strike that balance.
- [thenewstack.io: Culture, Vulnerabilities and Budget: Why Devs and AppSec Disagree](https://thenewstack.io/culture-vulnerabilities-and-budget-why-devs-and-appsec-disagree/)
- [computing.co.uk: CloudBees gets busy with security, visibility and control as DevOps evolves](https://www.computing.co.uk/news/4020521/cloudbees-busy-security-visibility-control-devops-evolves) CEO Sacha Labourey: 'DevOps is a pretty good proxy for what needs to happen in any organisation'
- [paloaltonetworks.com: Is Your Organization Protected Against IAM Misconfiguration Risks?](https://blog.paloaltonetworks.com/2020/10/cloud-iam-misconfiguration-risks/)
- [devops.com: How to Successfully Integrate Security and DevOps](https://devops.com/how-to-successfully-integrate-security-and-devops/)
- [helpnetsecurity.com: How to make DevSecOps stick with developers](https://www.helpnetsecurity.com/2020/12/14/how-devsecops-developers/)
## Kubernetes Threat Modelling
- [marcolancini.it: The Current State of Kubernetes Threat Modelling](https://www.marcolancini.it/2020/blog-kubernetes-threat-modelling/)

## Kubernetes Config Security Threats
- [cncf.io: Identifying Kubernetes Config Security Threats: Pods Running as Root](https://www.cncf.io/blog/2020/06/16/identifying-kubernetes-config-security-threats-pods-running-as-root/)
- [mirantis.com: Introduction to Istio Ingress: The easy way to manage incoming Kubernetes app traffic](https://www.mirantis.com/blog/introduction-to-istio-ingress-the-easy-way-to-manage-incoming-kubernetes-app-traffic/) Leaving your cluster exposed can be risky. That's why you need Istio Ingress, which only exposes the part that handles incoming traffic & allows routing rules based on routes, headers, IP addresses and more.
- [thenewstack.io: How Kubernetes vulnerabilities have shifted since the first attacks](https://thenewstack.io/how-kubernetes-vulnerabilities-have-shifted-since-the-first-api-attacks/)

## Security Linting on Kubernetes
- [kubeLinter 🌟](https://github.com/stackrox/kube-linter) KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
- [thenewstack.io: StackRox KubeLinter Brings Security Linting to Kubernetes](https://thenewstack.io/stackrox-kubelinter-brings-security-linting-to-kubernetes/)

## Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers
- [Why you should be using Multi-Category Security (MCS) for your Linux containers](https://www.redhat.com/en/blog/why-you-should-be-using-multi-category-security-your-linux-containers)
- [Using Podman and Containers to make a more secure pipeline](https://www.redhat.com/en/blog/using-container-technology-make-trusted-pipeline)

## Project Calico
* [Project Calico](https://www.projectcalico.org/) Secure networking for the cloud native era

## Security Patterns for Microservice Architectures
- [Security Patterns for Microservice Architectures](https://developer.okta.com/blog/2020/03/23/microservice-security-patterns)

## Anchore Container Security Solutions for DevSecOps
- [Anchore](https://anchore.com) Container image inspection and policy-based compliance

### Secure Container Based CI/CD Workflows
- [Secure Container Based CI/CD Workflows](https://anchore.com/cicd/)
- [Jenkins Plugin: Anchore Container Image Scanner](https://plugins.jenkins.io/anchore-container-scanner/)

### Securing Kubernetes With Anchore
- [Securing Kubernetes With Anchore](https://anchore.com/kubernetes/)

## GitHub security
- [GitHub security: what does it take to protect your company from credentials leaking on GitHub? 🌟](https://blog.gitguardian.com/github-security/)

## Databases in DMZ and Intranet
- [Databases in DMZ and Intranet](https://security.stackexchange.com/questions/58167/databases-in-dmz-and-intranet)

## Removing Credentials From Git Repo
- [medium: The Easiest Way To Remove Checked In Credentials From A Git Repo](https://medium.com/@tanmay.avinash.deshpande/the-easiest-way-to-remove-checked-in-credentials-from-a-git-repo-704a373b94e3)

## Pentesting
- [forbes.com: DevOps Drives Pentesting Delivered As A Service](https://www.forbes.com/sites/chenxiwang/2020/06/17/devops-drives-pentesting-delivered-as-a-service/)
- [emagined.com: How to conduct a penetration test](https://www.emagined.com/news-notes/2020/6/8/how-to-conduct-a-penetration-test)

## Credential Managers
### keycloak
- [keycloak.org](https://www.keycloak.org/) Open Source Identity and Access Management For Modern Applications and Services
- [Securing Kubernetes Apps with Keycloak and Gatekeeper](https://fdk.codes/securing-kubernetes-apps-with-keycloak-and-gatekeeper/)
- [Authorizing multi-language microservices with Louketo Proxy](https://developers.redhat.com/blog/2020/08/03/authorizing-multi-language-microservices-with-louketo-proxy/)
- [developers.redhat.com: A deep dive into Keycloak](https://developers.redhat.com/blog/2020/08/07/a-deep-dive-into-keycloak/)
- [blog.getambassador.io: Step-by-Step Centralized Authentication for Kubernetes with Keycloak and the Ambassador Edge Stack](https://blog.getambassador.io/centralized-authentication-with-keycloak-and-ambassador-edge-stack-d509ffbc7b6f)
- [blog.sighup.io: How to run Keycloak in HA on Kubernetes](https://blog.sighup.io/keycloak-ha-on-kubernetes/) How to setup Keycloak, the Open Source Identity and Access Management, in HA on Kubernetes.

### Git Credential Manager Core
- [Git Credential Manager Core](https://github.com/microsoft/Git-Credential-Manager-Core) GCM Core is a free, open-source, cross-platform credential manager for Git.
- [Git Credential Manager Core: Building a universal authentication experience](https://github.blog/2020-07-02-git-credential-manager-core-building-a-universal-authentication-experience/)

## GitOps Secret Management
- [blog.gitguardian.com: Secrets in source code (episode 2/3). Why secrets in git are such a problem](https://blog.gitguardian.com/secrets-credentials-api-git/)

### HashiCorp Vault
- [vaultproject.io](https://www.vaultproject.io/) Manage Secrets and Protect Sensitive Data. Secure, store and tightly control access to tokens, passwords, certificates, encryption keys for protecting secrets and other sensitive data using a UI, CLI, or HTTP API.
- [medium: Coding for Secrets Reliability with HashiCorp Vault](https://medium.com/hashicorp-engineering/coding-for-secrets-reliability-with-hashicorp-vault-2090dd8667e)
- [hashicorp.com: Vault & Kubernetes: Better Together](https://www.hashicorp.com/resources/vault-and-kubernetes-better-together/)
- OpenShift Blogs:
    - https://www.openshift.com/blog/managing-secrets-openshift-vault-integration
    - https://www.openshift.com/blog/vault-integration-using-kubernetes-authentication-method
    - https://www.openshift.com/blog/integrating-vault-with-legacy-applications
    - https://www.openshift.com/blog/integrating-hashicorp-vault-in-openshift-4
- [Vault Learning Resources: Vault 1.5 features and more](https://www.hashicorp.com/blog/learn-vault-1-5)
- [medium: Securing K8s Ingress Traffic with HashiCorp Vault PKIaaS and JetStack Cert-Manager](https://medium.com/hashicorp-engineering/securing-k8s-ingress-traffic-with-hashicorp-vault-pkiaas-and-jetstack-cert-manager-cb46195742ca)
- [hashicorp.com: Automate Secret Injection into CI/CD Workflows with the GitHub Action for Vault](https://www.hashicorp.com/blog/vault-github-action)
- [hashicorp.com: Use AWS Lambda Extensions to Securely Retrieve Secrets From HashiCorp Vault](https://www.hashicorp.com/blog/aws-lambda-extensions-for-hashicorp-vault) Developers no longer have to make their Lambda functions Vault-aware.

### CyberArk and Ansible
- [ansible.com: Simplifying secrets management with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/simplifying-secrets-management-with-cyberark-and-red-hat-ansible-automation-platform)
- [ansible.com: Automating Security with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/automating-security-with-cyberark-and-red-hat-ansible-automation-platform)

### SOPS for Kubernetes
- [dev.to: Manage your secrets in Git with SOPS for Kubernetes 🌟](https://dev.to/stack-labs/manage-your-secrets-in-git-with-sops-for-kubernetes-57me)

### Alternatives
- [GitOps secret management with bitnami-labs Sealed Secret and GoDaddy Kubernetes External Secrets](https://www.openshift.com/blog/gitops-secret-management)

## Serverless Security Best Practices
- [10 Serverless security best practices](https://snyk.io/blog/10-serverless-security-best-practices/)

## Docker Images & Container Security
- [thehackernews.com: Docker Images Containing Cryptojacking Malware Distributed via Docker Hub](https://thehackernews.com/2020/06/cryptocurrency-docker-image.html)
- [sysdig.com: 12 Container image scanning best practices to adopt in production](https://sysdig.com/blog/image-scanning-best-practices/)
- [infracloud.io: The Ten Commandments of Container Security](https://www.infracloud.io/blogs/top-10-things-for-container-security/)
- [medium: KubeSecOps Pipeline(Container security) in a cloudnative ecosystem](https://medium.com/@vaib16dec/kubesecops-pipeline-container-security-in-a-cloudnative-ecosystem-e59bf19a713d)

## Pod Security Policies
- [octetz.com: Setting Up Pod Security Policies](https://octetz.com/docs/2018/2018-12-07-psp/) By default, Kubernetes allows anything capable of creating a Pod to run a fairly privileged container that can compromise a system. Pod Security Policies protect clusters from privileged pods by ensuring the requester is authorised.
- [infracloud.io: Kubernetes Pod Security Policies with Open Policy Agent](https://www.infracloud.io/kubernetes-pod-security-policies-opa/) In this blog post, you will learn about the Pod Security Policy admission controller. Then you will see how Open Policy Agent can implement Pod Security Policies.

## Kubernetes Network Policies
- [medium.com: K8s Network Policies Demystified and Simplified 🌟](https://medium.com/swlh/k8s-network-policies-demystified-and-simplified-18f5ea9848e2)
- [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification/)

## Static Analysis SAST
- [DevSecOps – Static Analysis SAST with Jenkins Pipeline](https://digitalvarys.com/devsecops-static-analysis-sast-with-jenkins-pipeline/)

## Kubernetes Security Tools 
- [europeclouds.com: Implementing Aqua Security to Secure Kubernetes](https://www.europeclouds.com/blog/implementing-aqua-security-to-secure-kubernetes)
- [Pomerium](https://github.com/pomerium/pomerium) is an identity-aware proxy that enables secure access to internal applications. Pomerium brings consistent authz/authn, tooling, and auditing across cloud and on-premise deployments. No VPN or cloud provider account is required

## Books
- [Microservices Security in Action](https://medium.facilelogin.com/microservices-security-in-action-933072043ad7)