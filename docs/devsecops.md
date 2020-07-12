# Security and DevSecOps. Container Security
- [Introduction](#introduction)
- [Kubernetes Threat Modelling](#kubernetes-threat-modelling)
- [Kubernetes Config Security Threats](#kubernetes-config-security-threats)
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
- [Docker Images](#docker-images)
- [Pod Security Policies](#pod-security-policies)
- [Kubernetes Network Policies](#kubernetes-network-policies)

## Introduction
- [fiercesw.com: DevOps vs DevSecOps](https://fiercesw.com/devsecops-starter)
- [devopszone.info: DevSecOps Explained](https://www.devopszone.info/post/devsecops-explained)
- [linkedin: Dear Google, my data has left your building!](https://www.linkedin.com/pulse/dear-google-my-data-has-left-your-building-zakir-khan/)
- [snyk.io: The State of Open Source Security 2020](https://snyk.io/open-source-security-report/)
- [managedsentinel.com: Executive View — Current and Future Cybersecurity Architecture On One Page](https://www.managedsentinel.com/2019/05/23/cybersecurity-roadmap/)

## Kubernetes Threat Modelling
- [marcolancini.it: The Current State of Kubernetes Threat Modelling](https://www.marcolancini.it/2020/blog-kubernetes-threat-modelling/)

## Kubernetes Config Security Threats
- [cncf.io: Identifying Kubernetes Config Security Threats: Pods Running as Root](https://www.cncf.io/blog/2020/06/16/identifying-kubernetes-config-security-threats-pods-running-as-root/)
- [mirantis.com: Introduction to Istio Ingress: The easy way to manage incoming Kubernetes app traffic](https://www.mirantis.com/blog/introduction-to-istio-ingress-the-easy-way-to-manage-incoming-kubernetes-app-traffic/) Leaving your cluster exposed can be risky. That's why you need Istio Ingress, which only exposes the part that handles incoming traffic & allows routing rules based on routes, headers, IP addresses and more.

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

### Git Credential Manager Core
- [Git Credential Manager Core](https://github.com/microsoft/Git-Credential-Manager-Core) GCM Core is a free, open-source, cross-platform credential manager for Git.
- [Git Credential Manager Core: Building a universal authentication experience](https://github.blog/2020-07-02-git-credential-manager-core-building-a-universal-authentication-experience/)

## GitOps Secret Management
### HashiCorp Vault
- [vaultproject.io](https://www.vaultproject.io/) Manage Secrets and Protect Sensitive Data. Secure, store and tightly control access to tokens, passwords, certificates, encryption keys for protecting secrets and other sensitive data using a UI, CLI, or HTTP API.
- [medium: Coding for Secrets Reliability with HashiCorp Vault](https://medium.com/hashicorp-engineering/coding-for-secrets-reliability-with-hashicorp-vault-2090dd8667e)
- [hashicorp.com: Vault & Kubernetes: Better Together](https://www.hashicorp.com/resources/vault-and-kubernetes-better-together/)
- OpenShift Blogs:
    - https://www.openshift.com/blog/managing-secrets-openshift-vault-integration
    - https://www.openshift.com/blog/vault-integration-using-kubernetes-authentication-method
    - https://www.openshift.com/blog/integrating-vault-with-legacy-applications
    - https://www.openshift.com/blog/integrating-hashicorp-vault-in-openshift-4

### CyberArk and Ansible
- [ansible.com: Simplifying secrets management with CyberArk and Red Hat Ansible Automation Platform](https://www.ansible.com/blog/simplifying-secrets-management-with-cyberark-and-red-hat-ansible-automation-platform)

### SOPS for Kubernetes
- [dev.to: Manage your secrets in Git with SOPS for Kubernetes 🌟](https://dev.to/stack-labs/manage-your-secrets-in-git-with-sops-for-kubernetes-57me)

### Alternatives
- [GitOps secret management with bitnami-labs Sealed Secret and GoDaddy Kubernetes External Secrets](https://www.openshift.com/blog/gitops-secret-management)

## Serverless Security Best Practices
- [10 Serverless security best practices](https://snyk.io/blog/10-serverless-security-best-practices/)

## Docker Images
- [thehackernews.com: Docker Images Containing Cryptojacking Malware Distributed via Docker Hub](https://thehackernews.com/2020/06/cryptocurrency-docker-image.html)

## Pod Security Policies
- [octetz.com: Setting Up Pod Security Policies](https://octetz.com/docs/2018/2018-12-07-psp/) By default, Kubernetes allows anything capable of creating a Pod to run a fairly privileged container that can compromise a system. Pod Security Policies protect clusters from privileged pods by ensuring the requester is authorised.
- [infracloud.io: Kubernetes Pod Security Policies with Open Policy Agent](https://www.infracloud.io/kubernetes-pod-security-policies-opa/) In this blog post, you will learn about the Pod Security Policy admission controller. Then you will see how Open Policy Agent can implement Pod Security Policies.

## Kubernetes Network Policies
- [medium.com: K8s Network Policies Demystified and Simplified 🌟](https://medium.com/swlh/k8s-network-policies-demystified-and-simplified-18f5ea9848e2)