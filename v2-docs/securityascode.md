# Securityascode

!!! info "Architectural Context"
    Detailed reference for Securityascode in the context of Hardened Infrastructure.

## Cloud Infrastructure

### Kubernetes

#### Policy-as-Code

  - **(2026)** [==Kyverno 🌟==](https://kyverno.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A CNCF graduated Kubernetes-native policy engine.

*   Allows policy definition as standard Kubernetes resources (YAML).
*   Eliminates the need for complex DSLs like Rego.
*   Simplifies admission control, generation, mutation, and validation of workloads.
  - **(2024)** [**kyverno.io: 56 sample policies 🌟**](https://kyverno.io/policies) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A rich library of ready-to-use Kyverno policy definitions. These templates address common cloud security standards (Pod Security Standards, multi-tenancy constraints, best practices, and resource optimization parameters) for instant cluster hardening.
## Cloud Native Security

### Policy Enforcement

#### Open Policy Agent

  - **(2021)** [infracloud.io: Kubernetes Pod Security Policies with Open Policy Agent](https://www.infracloud.io/blogs/kubernetes-pod-security-policies-opa) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Addresses the transition from obsolete Kubernetes Pod Security Policies (PSPs) to Open Policy Agent (OPA) Gatekeeper. Explores how to leverage declarative constraints using the Rego engine to strictly manage admission control actions.
## Identity and Access Management

### Cloud IAM

#### Microsoft Entra

  - **(2024)** [**Configure Microsoft Entra for Increased Security**](https://learn.microsoft.com/en-us/entra/fundamentals/configure-security) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Official documentation outlines hardening parameters for Microsoft Entra ID. Features prescriptive blueprints for setting up conditional access, continuous access evaluation, Multi-Factor Authentication (MFA), and role-based identity management.
## Public Cloud Platforms

### AWS

#### EKS Security and Isolation

##### Policy Management

  - **(2021)** [**aws.amazon.com: Easy as one-two-three policy management with Kyverno on Amazon EKS 🌟**](https://aws.amazon.com/blogs/containers/easy-as-one-two-three-policy-management-with-kyverno-on-amazon-eks) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walkthrough detailing how to manage native policy rules on EKS clusters using Kyverno instead of raw Rego. Illustrates automated resource validation, generation, and mutation patterns to enforce corporate configuration compliance.
## Security

### DevSecOps

#### SAST

  - **(2023)** [GitHub Code Security Risk Assessment: Free Vulnerability Scanning](https://github.blog/security/application-security/how-exposed-is-your-code-find-out-in-minutes-for-free) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to GitHub's native, free vulnerability scanning tools designed to locate security regressions, secrets, and supply chain threats directly within the code repository. It highlights automated security alerts and quick enablement configurations.

---
💡 **Explore Related:** [Devsecops](./devsecops.md) | [Crossplane](./crossplane.md) | [Pulumi](./pulumi.md)

