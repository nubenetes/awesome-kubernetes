# Security and DevSecOps. Container Security
- [Introduction](#introduction)
- [Kubernetes Config Security Threats](#kubernetes-config-security-threats)
- [Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers](#multi-level-security-mls-vs-multi-category-security-mcs-make-secure-pipelines-with-podman-and-containers)
- [Project Calico](#project-calico)
- [keycloak](#keycloak)
- [Security Patterns for Microservice Architectures](#security-patterns-for-microservice-architectures)
- [Anchore Container Security Solutions for DevSecOps](#anchore-container-security-solutions-for-devsecops)
    - [Secure Container Based CI/CD Workflows](#secure-container-based-cicd-workflows)
    - [Securing Kubernetes With Anchore](#securing-kubernetes-with-anchore)
- [GitHub security](#github-security)
- [Databases in DMZ and Intranet](#databases-in-dmz-and-intranet)
- [Manage your secrets in Git with SOPS for Kubernetes](#manage-your-secrets-in-git-with-sops-for-kubernetes)
- [Pentesting](#pentesting)
- [HashiCorp Vault](#hashicorp-vault)
- [Serverless Security Best Practices](#serverless-security-best-practices)

## Introduction
- [fiercesw.com: DevOps vs DevSecOps](https://fiercesw.com/devsecops-starter)
- [DevSecOps Explained](https://www.devopszone.info/post/devsecops-explained)

## Kubernetes Config Security Threats
- [cncf.io: Identifying Kubernetes Config Security Threats: Pods Running as Root](https://www.cncf.io/blog/2020/06/16/identifying-kubernetes-config-security-threats-pods-running-as-root/)
- [mirantis.com: Introduction to Istio Ingress: The easy way to manage incoming Kubernetes app traffic](https://www.mirantis.com/blog/introduction-to-istio-ingress-the-easy-way-to-manage-incoming-kubernetes-app-traffic/) Leaving your cluster exposed can be risky. That's why you need Istio Ingress, which only exposes the part that handles incoming traffic & allows routing rules based on routes, headers, IP addresses and more.

## Multi-Level Security (MLS) vs Multi-Category Security (MCS). Make Secure Pipelines with Podman and Containers
- [Why you should be using Multi-Category Security (MCS) for your Linux containers](https://www.redhat.com/en/blog/why-you-should-be-using-multi-category-security-your-linux-containers)
- [Using Podman and Containers to make a more secure pipeline](https://www.redhat.com/en/blog/using-container-technology-make-trusted-pipeline)

## Project Calico
* [Project Calico](https://www.projectcalico.org/) Secure networking for the cloud native era

## keycloak
- [keycloak.org](https://www.keycloak.org/) Open Source Identity and Access Management For Modern Applications and Services

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

## Manage your secrets in Git with SOPS for Kubernetes
- [dev.to: Manage your secrets in Git with SOPS for Kubernetes 🌟](https://dev.to/stack-labs/manage-your-secrets-in-git-with-sops-for-kubernetes-57me)

## Pentesting
- [forbes.com: DevOps Drives Pentesting Delivered As A Service](https://www.forbes.com/sites/chenxiwang/2020/06/17/devops-drives-pentesting-delivered-as-a-service/)

## HashiCorp Vault
- [vaultproject.io](https://www.vaultproject.io/) Manage Secrets and Protect Sensitive Data. Secure, store and tightly control access to tokens, passwords, certificates, encryption keys for protecting secrets and other sensitive data using a UI, CLI, or HTTP API.
- [medium: Coding for Secrets Reliability with HashiCorp Vault](https://medium.com/hashicorp-engineering/coding-for-secrets-reliability-with-hashicorp-vault-2090dd8667e)

## Serverless Security Best Practices
- [10 Serverless security best practices](https://snyk.io/blog/10-serverless-security-best-practices/)

