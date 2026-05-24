# Openshift Pipelines

!!! info "Architectural Context"
    Detailed reference for Openshift Pipelines in the context of Engineering Pipeline.

## Standard Reference

  - [**uncontained.io**: External Jenkins Integration 🌟](http://v1.uncontained.io/playbooks/continuous_delivery/external-jenkins-integration.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OCP 4.2 - Jenkins image](https://docs.openshift.com/container-platform/4.2/openshift_images/using_images/images-other-jenkins-agent.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: 4 ways to build applications in openshift](https://dzone.com/articles/4-ways-to-build-applications-in-openshift-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: a quick guide to deploying java apps on openshift](https://dzone.com/articles/a-quick-guide-to-deploying-java-apps-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Using **KubeFed** to deploy applications](https://blog.openshift.comusing-kubefed-to-deploy-applications-to-ocp3-and-ocp4-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: odo Cheat Sheet](https://developers.redhat.com/cheat-sheets/odo-cheat-sheet)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Jenkins CICD Getting started with Groovy and Docker Containers —' Part 1](https://blog.isaack.io/articles/2016-08/Jenkins-CICD-Getting-Started-With-Groovy-Part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: jenkins cicd getting started with groovy and docker](https://medium.com/@fvtool/jenkins-cicd-getting-started-with-groovy-and-docker-containers-part-2-b03a1b934a49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium - fabric8, please check out jenkins X instead](https://medium.com/@jstrachan/fabric8-please-check-out-jenkins-x-instead-8295a025173a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: CI/CD with Openshift and Jenkins 🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone - Continuous Delivery with OpenShift and Jenkins: A/B Testing 🌟](https://dzone.com/articles/continuous-delivery-with-openshift-and-jenkins-ab)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: OpenShift 3.11 Pipeline Builds with OpenShift Jenkins' Image and OpenShift DSL](https://docs.openshift.com/container-platform/3.11/dev_guide/dev_tutorials/openshift_pipeline.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes/client-go: Go client for Kubernetes 🌟](https://github.com/kubernetes/client-go) <span class='md-tag md-tag--info'>⭐ 9818</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>

## DevOps

### CI-CD Pipelines

#### Jenkins Ecosystem

  - [Jenkins Pipeline Syntax: Scripted Syntax (Groovy DSL syntax) & Declarative' Syntax 🌟](https://www.jenkins.io/doc/book/pipeline/syntax) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Authoritative documentation explaining scripted and declarative Jenkins pipeline configuration syntaxes. Breaks down flow control structures, declarative directives, agent allocations, and step definitions essential to enterprise build automation.
## Hybrid Cloud and Enterprise

### OpenShift

#### Pipelines and CI CD

  - **(2020)** [openshift.com: Cloud-Native CI/CD with OpenShift Pipelines based on Tekton](https://www.redhat.com/en/blog/cloud-native-ci-cd-with-openshift-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An official Red Hat announcement outlining OpenShift Pipelines, the managed implementation of Tekton.
Live Grounding: Details the shift from centralized Jenkins controllers to decoupled, cloud-native container steps executing inside Kubernetes Pods, providing superior resource usage and auto-scaling.
  - **(2020)** [openshift.com: OpenShift Pipelines Advanced Triggers Part 1 - Triggering Different Project Builds in the Same Repository](https://www.redhat.com/en/blog/openshift-pipelines-advanced-triggers-part-1-triggering-different-project-builds-in-the-same-repository) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Deep-dive blog on designing advanced Tekton triggers for complex repository topologies.
Live Grounding: Instructs users on using Interceptors and EventListeners to run different pipelines when updates are detected inside a unified monorepo.
  - **(2019)** [Simply Explained: OpenShift and Jenkins Pipelines](https://www.redhat.com/en/blog/jenkins-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A high-level exploratory blog explaining the integration benefits of Jenkins Pipelines inside OpenShift namespaces.
Live Grounding: Focuses on explaining the fundamental differences between local Jenkins setups and cloud-managed agent clusters run on Kubernetes worker nodes.
  - [OpenShift Container Pipelines Samples 🌟](https://github.com/redhat-cop/container-pipelines) <span class='md-tag md-tag--info'>⭐ 160</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: An educational reference repository containing sample pipelines for Red Hat OpenShift Container Platform.
Live Grounding: Represents historical approaches to Jenkins and Tekton configurations in OCP 3/4 environments. Highly useful as a legacy blueprint reference, but superseded by official Red Hat OpenShift Pipelines operators.
  - [OpenShift Pipeline Library 🌟](https://github.com/redhat-cop/pipeline-library) <span class='md-tag md-tag--info'>⭐ 51</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A collection of shared pipeline libraries for Jenkins implementations on OpenShift.
Live Grounding: While it contains modular Jenkins steps tailored to OpenShift environments, it has limited recent commits. Most enterprise workflows have migrated to native Tekton or declarative Argo CD paths.
  - [developers.redhat.com - Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A technical guide focused on setting up traditional Jenkins CI/CD servers inside OpenShift 4.
Live Grounding: Details the deployment of the OpenShift Jenkins Client Plug-in. It provides historical context on OpenShift Jenkins sync configurations before the cloud-native transition to Tekton.
  - [github.com/openshift/pipelines-tutorial](https://github.com/openshift/pipelines-tutorial) <span class='md-tag md-tag--info'>⭐ 322</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: The primary repository used for training developers on utilizing Tekton triggers and tasks in OpenShift.
Live Grounding: Serves as an excellent hands-on lab environment for configuring Tasks, Pipelines, PipelineRuns, and EventListeners using the OpenShift Pipelines CLI.
  - [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab) <span class='md-tag md-tag--info'>⭐ 5</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: A specialized, quick-start tutorial targeting Node.js deployments with OpenShift Pipelines.
Live Grounding: Illustrates how to configure a build-and-deploy pipeline using standard Node.js source code, demonstrating Source-to-Image capabilities within the Tekton framework.
  - [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift' Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Part 4 of a developer series focusing on deployment pipelines for modern JavaScript web applications.
Live Grounding: Provides practical code examples of utilizing Tekton for building and serving front-end assets on OpenShift, utilizing lightweight Nginx containers.
## Red Hat OpenShift

### CI-CD Pipelines (1)

#### Architecture

  - [slideshare.net: OpenShift Container Platform CI/CD Build & Deploy 🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Structured presentation breaking down multi-stage Continuous Integration and Continuous Deployment processes across OpenShift platforms. Covers Source-to-Image architectures, Jenkins plugins, and blue-green pipeline design.
#### GitHub Actions

  - [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly' from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed instructional guide describing the integration of GitHub Actions runners with OpenShift API end-points. Facilitates smooth continuous deployment routines by using native OpenShift actions directly within external workflows.
#### Java Integrations

  - **(2018)** [CI/CD with fabric8](http://fabric8.io/guide/cdelivery.html) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Archive documentation specifying continuous delivery workflows, pipelines, and integrations built around early Fabric8 architectures. Useful for maintaining or migrating older Java deployments in enterprise settings.
#### Jenkins Ecosystem (1)

  - **(2018)** [**github - using jenkins pipelines with OKD**](https://github.com/openshift/origin/tree/main/examples/jenkins/pipeline) <span class='md-tag md-tag--info'>⭐ 8654</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Repository detailing baseline code configurations, sample pipelines, and deployment manifests engineered to execute scripted Jenkins procedures inside early versions of the OKD community container platform.
  - **(2018)** [blog.openshift.com: Deploying jenkins on openshift - part 1](https://www.redhat.com/en/blog/deploying-jenkins-on-openshift-part-1) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the baseline deployment strategy for standing up Jenkins nodes within OpenShift namespaces. Deeply reviews network configurations, service accounts, and route declarations to enable external webhook communications.
  - **(2018)** [blog.openshift.com: Improving jenkins performance on openshift - part 2](https://www.redhat.com/en/blog/improving-jenkins-performance-on-openshift-part-2) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on maximizing execution speed, tuning garbage collection, allocating resource requests and limits, and resolving scaling bottlenecks in OpenShift Jenkins deployments. Offers proven optimization recipes for larger scale organizations.
  - **(2018)** [OpenShift Pipelines with Jenkins Blue Ocean 🌟](https://www.redhat.com/en/blog/openshift-pipelines-jenkins-blue-ocean) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Combines OpenShift Orchestration APIs with Jenkins Blue Ocean to manage continuous delivery pipelines visually. Promotes clear state-tracking, modular pipeline construction, and simplified debugging metrics.
  - **(2018)** [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟](https://www.redhat.com/en/blog/building-declarative-pipelines-openshift-dsl-plugin) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details strategies to compile reliable, declarative Jenkins pipelines utilizing OpenShift DSL plugins. Discusses native methods to trigger S2I builds, promote container images, and securely communicate with Cluster managers.
  - [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins) <span class='md-tag md-tag--info'>⭐ 260</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Base image definition and custom wrappers designed to run stable Jenkins instances natively within OpenShift v3 clusters. Optimizes master-agent lifecycles, permissions, and localized source-to-image deployments inside early OpenShift platforms.
  - [opensource.com: running jenkins builds containers 🌟](https://opensource.com/article/18/4/running-jenkins-builds-containers) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step tutorial addressing the orchestration of containerized workloads inside a Jenkins building phase. Evaluates Docker-in-Docker strategies and Kubernetes dynamic agents to avoid single-host execution bottlenecks and guarantee runtime isolation.
  - [cloudowski.com: Jenkins on OpenShift - how to use and customize it in a' cloud-native way 🌟](https://cloudowski.com/articles/jenkins-on-openshift) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Cloud-Native custom Jenkins practices optimized specifically for OpenShift environments. Introduces the application of dynamic pod templates, native storage classes, and OAuth-based authentication to maximize pipeline resilience.
  - [developers.redhat.com: An easier way to create custom Jenkins containers](https://developers.redhat.com/blog/2020/06/04/an-easier-way-to-create-custom-jenkins-containers) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains streamlined procedures for producing custom, secure Jenkins container images for deployment. Focuses on minimizing layers, loading plug-ins safely during build time, and injecting enterprise parameters within Red Hat architectures.
  - [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Utility repository hosting configurations to deploy Jenkins Blue Ocean configurations instantly within early Red Hat OpenShift Container Platform environments. Serves as a reference setup for visualized pipeline states.
  - [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library) <span class='md-tag md-tag--info'>⭐ 436</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A reusable Jenkins Pipeline helper library that supports automated environments, build phases, and release setups within OpenShift frameworks. It is largely deprecated, superseded by modern Jenkins plugins or native Tekton pipelines.
#### Multi-Cluster Deployments

  - **(2018)** [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.redhat.com/en/blog/deploying-openshift-applications-multiple-datacenters) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides high-level operational advice for utilizing Jenkins pipelines to orchestrate, sync, and validate application deployments across disparate, multi-region OpenShift datacenters.
### Developer Experience

#### CLI Utilities

  - [ODO: OpenShift Command line for Developers 🌟](https://github.com/redhat-developer/odo) <span class='md-tag md-tag--info'>⭐ 842</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A developer-focused CLI utility for writing, deploying, and debugging cloud-native software directly on OpenShift and general Kubernetes clusters. Cuts deployment friction by enabling developers to focus on active code rather than complex Kubernetes YAML constructs.
  - [developers.redhat.com: Enterprise Kubernetes development with odo: The CLI' tool for developers](https://developers.redhat.com/blog/2020/06/16/enterprise-kubernetes-development-with-odo-the-cli-tool-for-developers) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces the 'odo' command-line application to software engineers targeting Kubernetes clusters. Details workflow optimizations, container build speedups, and localized debugging patterns.
  - [developers.redhat.com: Kubernetes integration and more in odo 2.0](https://developers.redhat.com/blog/2020/10/06/kubernetes-integration-and-more-in-odo-2-0) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses major enhancements in 'odo 2.0', highlighting strict Devfile standards support and the capability to deploy to arbitrary Kubernetes engines instead of being isolated to OpenShift clusters.
  - [piotrminkowski.com: Java Development on OpenShift with odo](https://piotrminkowski.com/2021/02/05/java-development-on-openshift-with-odo) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines Java development pipelines deploying to OpenShift with odo. Demonstrates hot reloading patterns, live-debugging on remote pods, and utilizing Quarkus or Spring Boot container templates.
#### Devfiles

  - [developers.redhat.com: Developing your own custom devfiles for odo 2.0](https://developers.redhat.com/blog/2021/02/12/developing-your-own-custom-devfiles-for-odo-2-0) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Thorough explanation of structuring, writing, and applying custom Devfiles within the odo ecosystem to mandate unified container development environments across large engineering divisions.
#### Java Integrations (1)

  - [Fabric8](https://fabric8.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Historically significant platform offering tools, microservices, and management mechanisms for Java environments on Kubernetes and OpenShift. Now deprecated, but set foundations for contemporary Java developer abstractions.
  - [developers.redhat.com: Getting started with the fabric8 Kubernetes Java' client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical introduction to utilizing the Fabric8 Kubernetes Java Client SDK. Details how to perform CRUD operations on Kubernetes APIs, deploy custom controllers, and stream container logs inside Java runtimes.
#### Maven Plugins

  - **(2025)** [GitHub: Eclipse JKube](https://github.com/eclipse-jkube/jkube) <span class='md-tag md-tag--info'>⭐ 850</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Active repository containing the source code, extensions, and Maven/Gradle plugins for Eclipse JKube. Simplifies localized builds, auto-detects Java application frameworks, and generates matching Kubernetes resource configurations.
#### Source-to-Image

  - [developers.redhat.com - S2i](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Delivers technical insight on Source-to-Image (S2I) execution modes, comparing continuous deployment direct from code versus deploying pre-compiled binaries via specialized pipelines inside Red Hat runtimes.
### Security

#### Continuous Delivery Security

  - **(2021)** [openshift.com: Using OpenShift Pipelines to Automate Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/blog/using-openshift-pipelines-to-automate-red-hat-advanced-cluster-security-for-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines deployment strategies of Red Hat Advanced Cluster Security (RHACS) directly into Tekton-based OpenShift Pipelines. Demonstrates early container image scanning, compliance validations, and proactive security gate blocking.

---
💡 **Explore Related:** [Registries](./registries.md) | [Jenkins](./jenkins.md) | [Cicd](./cicd.md)

