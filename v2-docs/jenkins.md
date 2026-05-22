# Jenkins

!!! info "Architectural Context"
    Detailed reference for Jenkins in the context of Engineering Pipeline.

## Cloud Infrastructure

### Training

#### AWS Official

  - **(2023)** [community.aws/training: Training and Certification](https://builder.aws.com/learn)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An official community hub connecting cloud builders with modern development labs, learning blueprints, and architectural expert-led events.
## Continuous Integration

### CI Tools

#### Jenkins (1)

  - [openshift-pipeline](https://plugins.jenkins.io/openshift-pipeline) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Allows direct deployment integrations inside Red Hat OpenShift pipelines via Jenkins, automating image building and pipeline orchestrations.
  - [openshift-sync](https://plugins.jenkins.io/openshift-sync) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synchronizes OpenShift environment configs, secrets, build limits, and pod templates automatically to ensure consistent CI runner execution.
  - [openshift-client](https://plugins.jenkins.io/openshift-client) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Exposes OpenShift's command-line tool definitions directly inside Jenkins jobs, enabling custom script actions to command remote clusters safely.
## DevOps

### CI-CD Pipelines

#### Jenkins Ecosystem

  - **(2026)** [==Jenkins Pipeline Syntax: Scripted Syntax (Groovy DSL syntax) & Declarative Syntax 🌟==](https://www.jenkins.io/doc/book/pipeline/syntax) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Authoritative documentation explaining scripted and declarative Jenkins pipeline configuration syntaxes. Breaks down flow control structures, declarative directives, agent allocations, and step definitions essential to enterprise build automation.
## GitOps and Continuous Delivery

### Kubernetes Native CI-CD

#### Argo Workflows

  - **(2023)** [==Migrating CI/CD from Jenkins to Argo Workflows==](https://dev.to/intuitdev/migrating-cicd-from-jenkins-to-argo-1km4) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive real-world migration case study detailing how Intuit transitioned high-volume CI/CD pipelines from Jenkins to Kubernetes-native Argo Workflows. Outlines critical architectural lessons, scale bottlenecks, pipeline-as-code models, and resource optimization.
## Red Hat OpenShift

### CI-CD Pipelines (1)

#### Jenkins Ecosystem (1)

  - **(2018)** [opensource.com: running jenkins builds containers 🌟](https://opensource.com/article/18/4/running-jenkins-builds-containers) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step tutorial addressing the orchestration of containerized workloads inside a Jenkins building phase. Evaluates Docker-in-Docker strategies and Kubernetes dynamic agents to avoid single-host execution bottlenecks and guarantee runtime isolation.
  - **(2018)** [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟](https://www.redhat.com/en/blog/building-declarative-pipelines-openshift-dsl-plugin) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details strategies to compile reliable, declarative Jenkins pipelines utilizing OpenShift DSL plugins. Discusses native methods to trigger S2I builds, promote container images, and securely communicate with Cluster managers.
## Runtime Optimizations

### JVM Tuning

#### Garbage Collection

  - **(2016)** [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟](https://www.jenkins.io/blog/2016/11/21/gc-tuning) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Landmark analytical study detailing optimized GC settings for massive scale Jenkins controller instances. Discusses keeping response times low under heavy CI execution queues.
#### Language Fundamentals

  - **(2021)** [Running Jenkins on Java 11 🌟](https://www.jenkins.io/doc/administration/requirements/jenkins-on-java-11/#:~:text=The%20easiest%20way%20to%20run,images%2C%20use%20the%20jdk11%20tag.) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Administrative guide addressing the platform transition of the Jenkins controller from obsolete Java 8 engines to modern Java 11 runtime profiles.
## Software Engineering

### CICD

#### Trends

  - **(2021)** [sdtimes.com: CI/CD pipelines are expanding 🌟](https://sdtimes.com/devops/ci-cd-pipelines-are-expanding)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores how modern CI/CD pipelines are expanding their scope to integrate security scans, compliance policy engines, and platform provisioning stages.

---
💡 **Explore Related:** [Registries](./registries.md) | [Jenkins Alternatives](./jenkins-alternatives.md) | [Argo](./argo.md)

