# Cicd Kubernetes Plugins

!!! info "Architectural Context"
    Detailed reference for Cicd Kubernetes Plugins in the context of Engineering Pipeline.

## Continuous Delivery

### GitOps

#### GitLab

  - [**GitLab Kubernetes Agent**](https://docs.gitlab.com/user/clusters/agent) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The GitLab Agent for Kubernetes. Establishes a secure pull-based GitOps connection inside the cluster, avoiding external security exposures.
## Continuous Integration

### CI Tools

#### Jenkins

  - [Jenkins Kubernetes Plugin](https://plugins.jenkins.io/kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The critical Kubernetes integration for Jenkins, executing dynamic agents directly inside cluster pods. Solves pipeline scale issues by tearing down runner instances upon build completion.
  - [Kubernetes Continuous Deploy](https://plugins.jenkins.io/kubernetes-cd) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A traditional Jenkins plugin for deploying build outputs to Kubernetes. Note: Has fallen out of favor in modern GitOps-centric continuous delivery pipelines.
  - [openshift-pipeline](https://plugins.jenkins.io/openshift-pipeline) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Allows direct deployment integrations inside Red Hat OpenShift pipelines via Jenkins, automating image building and pipeline orchestrations.
  - [openshift-sync](https://plugins.jenkins.io/openshift-sync) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synchronizes OpenShift environment configs, secrets, build limits, and pod templates automatically to ensure consistent CI runner execution.
  - [openshift-client](https://plugins.jenkins.io/openshift-client) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Exposes OpenShift's command-line tool definitions directly inside Jenkins jobs, enabling custom script actions to command remote clusters safely.

---
💡 **Explore Related:** [Registries](./registries.md) | [Argo](./argo.md) | [Sonarqube](./sonarqube.md)

