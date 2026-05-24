# Crossplane

!!! info "Architectural Context"
    Detailed reference for Crossplane in the context of Hardened Infrastructure.

## Standard Reference

  - [medium: Using Crossplane to Provision a Kubernetes Cluster in Google Cloud](https://medium.com/dzerolabs/using-crossplane-to-provision-a-kubernetes-cluster-in-google-cloud-cf5374d765ee)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Defining Infrastructure Declaratively with Crossplane](https://faun.pub/defining-infrastructure-declaratively-with-crossplane-eb9e0a98ae38)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Control Planes

### Cloud Infrastructure As Code

#### Architectural Strategy

  - [Crossplane, a Universal Control Plane API for Cloud Computing](https://www.infoq.com/news/2019/01/upbound-crossplane)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical article introducing Crossplane's architectural strategy. It outlines the core benefits of moving from static execution runs to active, continuously reconciling API-driven cloud control planes.
#### Crossplane (1)

  - **(2026)** [==crossplane.io==](https://www.crossplane.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Crossplane transforms Kubernetes into a universal control plane. By exposing managed cloud infrastructure as custom Resource Definitions (CRDs), it allows platform teams to build native compositions without external IaC tools.
#### Market Evaluation

  - [symphony.is: Crossplane - The New Kid in Town](https://symphony.is/blog/crossplane---the-new-kid-in-town-)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational review of Crossplane's technology, analyzing why real-time cloud infrastructure reconciliation represents the future of cloud resource management.
#### Presentations

  - [Presentation: YAML your cloud](https://docs.google.com/presentation/d/1IZXCiQl_NUawHMvKJANCG2_LIBZseUpY-XyPjlghj9E/edit)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical slide deck focused on using unified YAML for cross-cloud resource control, detailing how standard declarative formats reduce administrative friction.
#### Reference Architectures

  - [upbound/platform-ref-multi-k8s: Upbound's reference platform for multi-cloud' Kubernetes with Crossplane](https://github.com/upbound/platform-ref-multi-k8s) <span class='md-tag md-tag--info'>⭐ 66</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Upbound's standardized reference architecture for running multi-cloud Kubernetes clusters via Crossplane. It highlights production-grade modular design, credential partitioning, and composition patterns.
  - [askmeegs/yaml-your-cloud](https://github.com/askmeegs/yaml-your-cloud) <span class='md-tag md-tag--info'>⭐ 6</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstration codebase representing compositions and templates for unified cloud infrastructure configurations, providing a reference layout for Crossplane training labs.
### Developer Platforms

#### Internal Developer Platforms

  - [Crossplane: A Kubernetes Control Plane to Roll Your Own PaaS](https://thenewstack.io/crossplane-a-kubernetes-control-plane-to-roll-your-own-paas)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses Crossplane's capability to orchestrate complete Internal Developer Platforms (IDPs). Highlights how custom control planes abstract infrastructure complexity, facilitating developer self-service workflows.
### Red Hat Ecosystem

#### OpenShift Integration

  - [Crossplane as an OpenShift Operator to manage and provision cloud-native services](https://blog.crossplane.io/crossplane-openshift-operator-cloud-native-services) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep dive into installing and operating Crossplane within Red Hat OpenShift. Shows how platform administrators can unify container scheduling and cloud service management using OpenShift operators.
## Developer Experience

### Kubernetes Core Concepts

#### Complexity Analysis

  - [itnext.io: Why do developers find Kubernetes so hard?](https://itnext.io/why-do-developers-find-kubernetes-hard-6532e8d6ce7f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry critique analyzing the steep cognitive curve of native Kubernetes. The article provides structured recommendations on how Platform Engineering can establish abstraction layers for developers.
## GitOps

### Continuous Delivery

#### Flux Integration

  - [itnext.io: GitOpsify Cloud Infrastructure with Crossplane and Flux](https://itnext.io/gitopsify-cloud-infrastructure-with-crossplane-and-flux-d605d3043452) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A granular guide on uniting Flux CD and Crossplane. Details the construction of continuous GitOps pipelines where infrastructure drifts are self-reconciled using Flux's lightweight controllers.
#### Infrastructure Orchestration

  - **(2023)** [codefresh.io: Using GitOps for Infrastructure and Applications With Crossplane and Argo CD](https://octopus.com/devops/gitops) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This architectural study outlines the synchronization of infrastructure and application deployments using GitOps principles, examining the strategic union of Crossplane and continuous deployment tools.

---
💡 **Explore Related:** [Kubernetes Security](./kubernetes-security.md) | [Devsecops](./devsecops.md) | [Kustomize](./kustomize.md)

