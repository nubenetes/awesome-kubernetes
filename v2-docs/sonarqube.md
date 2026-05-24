# Sonarqube

!!! info "Architectural Context"
    Detailed reference for Sonarqube in the context of Engineering Pipeline.

## Standard Reference

  - [wikipedia: SonarQube](https://en.wikipedia.org/wiki/SonarQube)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: Why SonarQube](https://dzone.com/articles/why-sonarqube-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: How to quickly get started with Sonar](https://dzone.com/articles/how-quickly-get-started-sonar)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: Sonarqube scanning in 15 minutes](https://dzone.com/articles/sonarqube-scanning-in-15-minutes-2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: Quick start with sonarqube for static code analysis](https://dzone.com/articles/quick-start-witj-sonarqube-for-static-code-analysi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone.com: Code Analysis Part 1 - Analyzing Code with SonarQube](https://dzone.com/articles/code-analysis-with-sonarqube-part-1-setup)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: SonarCloud integration with SpringBoot Maven](https://dzone.com/articles/sonarcloud-integration-with-springboot-maven)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Running SonarQube on Kubernetes](https://medium.com/@akamenev/running-sonarqube-on-azure-kubernetes-92a1b9051120)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## DevSecOps

### Continuous Inspection

#### Static Code Analysis

##### Execution

  - [thenewstack.io: How to Analyze Code and Find Vulnerabilities with SonarQube](https://thenewstack.io/how-to-analyze-code-and-find-vulnerabilities-with-sonarqube)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Hands-on guide to running static analyzers against real codebases using SonarQube scanners, configuring quality gates, and reviewing vulnerability alerts.
##### Installation

  - [thenewstack.io: How to Install the SonarQube Security Analysis Platform](https://thenewstack.io/how-to-install-the-sonarqube-security-analysis-platform)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step deployment guide detailing how to host SonarQube locally or on dedicated infrastructure, including database dependencies and JVM configurations.
##### SonarQube

  - **(2026)** [==Sonarqube.org==](https://www.sonarsource.com/products/sonarqube) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The leading platform for continuous inspection of code quality, executing automatic reviews with static analysis of code to detect bugs, security vulnerabilities, and code smells across 30+ programming languages.
##### SonarQube Scanner

  - **(2026)** [**SonarQube Scanner Overview**](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Core index for the official SonarQube scanner integrations, providing detailed configurations for popular build tools and continuous integration platforms like Gradle, MSBuild, Maven, Jenkins, and Azure DevOps.
### Continuous Integration

#### Jenkins Pipelines

##### Dockerized Scans

  - [itnext.io: SonarQube: running tests from Jenkins Pipeline in Docker](https://itnext.io/sonarqube-running-tests-from-jenkins-pipeline-from-docker-7740702b6f42)  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Deep technical guide showing how to architect a Jenkins pipeline that runs unit tests and executes SonarQube code coverage scans natively inside transient Docker containers.
### Kubernetes Native

#### Google Cloud Platform

##### Blueprints

  - [click-to-deploy/sonarqube](https://github.com/GoogleCloudPlatform/click-to-deploy/tree/master/k8s/sonarqube) <span class='md-tag md-tag--info'>⭐ 771</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Google Cloud Platform blueprint repository designed to ease the deployment of SonarQube on Google Kubernetes Engine (GKE) via highly standardized manifest suites.
#### Helm Deployments

##### SonarQube (1)

  - **(2024)** [hub.helm.sh/charts/oteemo/sonarqube](https://artifacthub.io/packages/helm/oteemo/sonarqube) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Helm chart repository listing for deploying SonarQube on Kubernetes, complete with configurations for persistence, ingress routing, and integrated database deployments.
#### Local Environments

##### Video Tutorials

  - [youtube: Installation of Sonarqube on Kubernetes/Minikube](https://www.youtube.com/watch?v=_cT-kkvw3NQ)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Video guide demonstrating how to spin up a SonarQube server inside Minikube, configured for localized developer playground environments.

---
💡 **Explore Related:** [Registries](./registries.md) | [Jenkins](./jenkins.md) | [Cicd](./cicd.md)

