# Openshift Pipelines

!!! info "Architectural Context"
    Detailed reference for Openshift Pipelines in the context of Engineering Pipeline.

## Hybrid Cloud and Enterprise

### OpenShift

#### Pipelines and CI CD

  - **(2021)** [**github.com/openshift/pipelines-tutorial**](https://github.com/openshift/pipelines-tutorial) <span class='md-tag md-tag--info'>⭐ 322</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: The primary repository used for training developers on utilizing Tekton triggers and tasks in OpenShift.
Live Grounding: Serves as an excellent hands-on lab environment for configuring Tasks, Pipelines, PipelineRuns, and EventListeners using the OpenShift Pipelines CLI.
  - **(2020)** [OpenShift Container Pipelines Samples 🌟](https://github.com/redhat-cop/container-pipelines) <span class='md-tag md-tag--info'>⭐ 160</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: An educational reference repository containing sample pipelines for Red Hat OpenShift Container Platform.
Live Grounding: Represents historical approaches to Jenkins and Tekton configurations in OCP 3/4 environments. Highly useful as a legacy blueprint reference, but superseded by official Red Hat OpenShift Pipelines operators.
  - **(2020)** [OpenShift Pipeline Library 🌟](https://github.com/redhat-cop/pipeline-library) <span class='md-tag md-tag--info'>⭐ 51</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A collection of shared pipeline libraries for Jenkins implementations on OpenShift.
Live Grounding: While it contains modular Jenkins steps tailored to OpenShift environments, it has limited recent commits. Most enterprise workflows have migrated to native Tekton or declarative Argo CD paths.
  - **(2020)** [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab) <span class='md-tag md-tag--info'>⭐ 5</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: A specialized, quick-start tutorial targeting Node.js deployments with OpenShift Pipelines.
Live Grounding: Illustrates how to configure a build-and-deploy pipeline using standard Node.js source code, demonstrating Source-to-Image capabilities within the Tekton framework.
  - **(2020)** [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Part 4 of a developer series focusing on deployment pipelines for modern JavaScript web applications.
Live Grounding: Provides practical code examples of utilizing Tekton for building and serving front-end assets on OpenShift, utilizing lightweight Nginx containers.
  - **(2020)** [openshift.com: OpenShift Pipelines Advanced Triggers Part 1 - Triggering Different Project Builds in the Same Repository](https://www.redhat.com/en/blog/openshift-pipelines-advanced-triggers-part-1-triggering-different-project-builds-in-the-same-repository) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Deep-dive blog on designing advanced Tekton triggers for complex repository topologies.
Live Grounding: Instructs users on using Interceptors and EventListeners to run different pipelines when updates are detected inside a unified monorepo.
  - **(2019)** [developers.redhat.com - Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A technical guide focused on setting up traditional Jenkins CI/CD servers inside OpenShift 4.
Live Grounding: Details the deployment of the OpenShift Jenkins Client Plug-in. It provides historical context on OpenShift Jenkins sync configurations before the cloud-native transition to Tekton.
  - **(2019)** [Simply Explained: OpenShift and Jenkins Pipelines](https://www.redhat.com/en/blog/jenkins-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A high-level exploratory blog explaining the integration benefits of Jenkins Pipelines inside OpenShift namespaces.
Live Grounding: Focuses on explaining the fundamental differences between local Jenkins setups and cloud-managed agent clusters run on Kubernetes worker nodes.
## Red Hat OpenShift

### CI-CD Pipelines

#### Architecture

  - **(2018)** [slideshare.net: OpenShift Container Platform CI/CD Build & Deploy 🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Structured presentation breaking down multi-stage Continuous Integration and Continuous Deployment processes across OpenShift platforms. Covers Source-to-Image architectures, Jenkins plugins, and blue-green pipeline design.
#### GitHub Actions

  - **(2020)** [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed instructional guide describing the integration of GitHub Actions runners with OpenShift API end-points. Facilitates smooth continuous deployment routines by using native OpenShift actions directly within external workflows.
#### Java Integrations

  - **(2018)** [CI/CD with fabric8](http://fabric8.io/guide/cdelivery.html) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Archive documentation specifying continuous delivery workflows, pipelines, and integrations built around early Fabric8 architectures. Useful for maintaining or migrating older Java deployments in enterprise settings.
#### Jenkins Ecosystem

  - **(2018)** [**github - using jenkins pipelines with OKD**](https://github.com/openshift/origin/tree/main/examples/jenkins/pipeline) <span class='md-tag md-tag--info'>⭐ 8654</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Repository detailing baseline code configurations, sample pipelines, and deployment manifests engineered to execute scripted Jenkins procedures inside early versions of the OKD community container platform.
  - **(2018)** [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins) <span class='md-tag md-tag--info'>⭐ 260</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Base image definition and custom wrappers designed to run stable Jenkins instances natively within OpenShift v3 clusters. Optimizes master-agent lifecycles, permissions, and localized source-to-image deployments inside early OpenShift platforms.
  - **(2018)** [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library) <span class='md-tag md-tag--info'>⭐ 436</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A reusable Jenkins Pipeline helper library that supports automated environments, build phases, and release setups within OpenShift frameworks. It is largely deprecated, superseded by modern Jenkins plugins or native Tekton pipelines.
  - **(2018)** [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Utility repository hosting configurations to deploy Jenkins Blue Ocean configurations instantly within early Red Hat OpenShift Container Platform environments. Serves as a reference setup for visualized pipeline states.
  - **(2018)** [blog.openshift.com: Deploying jenkins on openshift - part 1](https://www.redhat.com/en/blog/deploying-jenkins-on-openshift-part-1) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the baseline deployment strategy for standing up Jenkins nodes within OpenShift namespaces. Deeply reviews network configurations, service accounts, and route declarations to enable external webhook communications.
  - **(2018)** [cloudowski.com: Jenkins on OpenShift - how to use and customize it in a cloud-native way 🌟](https://cloudowski.com/articles/jenkins-on-openshift) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Cloud-Native custom Jenkins practices optimized specifically for OpenShift environments. Introduces the application of dynamic pod templates, native storage classes, and OAuth-based authentication to maximize pipeline resilience.
  - **(2018)** [blog.openshift.com: Improving jenkins performance on openshift - part 2](https://www.redhat.com/en/blog/improving-jenkins-performance-on-openshift-part-2) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on maximizing execution speed, tuning garbage collection, allocating resource requests and limits, and resolving scaling bottlenecks in OpenShift Jenkins deployments. Offers proven optimization recipes for larger scale organizations.
  - **(2016)** [slideshare.net: CI/CD with Openshift and Jenkins 🌟](https://www.slideshare.net/slideshow/cicd-with-openshift-and-jenkins/57944430) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Historical slide collection detailing standard Continuous Integration patterns on OpenShift using custom-built Jenkins controllers. Evaluates legacy deployment triggers and localized container build flows.
#### Multi-Cluster Deployments

  - **(2018)** [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.redhat.com/en/blog/deploying-openshift-applications-multiple-datacenters) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides high-level operational advice for utilizing Jenkins pipelines to orchestrate, sync, and validate application deployments across disparate, multi-region OpenShift datacenters.
### Developer Experience

#### CLI Utilities

  - **(2025)** [**ODO: OpenShift Command line for Developers 🌟**](https://github.com/redhat-developer/odo) <span class='md-tag md-tag--info'>⭐ 842</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A developer-focused CLI utility for writing, deploying, and debugging cloud-native software directly on OpenShift and general Kubernetes clusters. Cuts deployment friction by enabling developers to focus on active code rather than complex Kubernetes YAML constructs.
  - **(2021)** [piotrminkowski.com: Java Development on OpenShift with odo](https://piotrminkowski.com/2021/02/05/java-development-on-openshift-with-odo) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines Java development pipelines deploying to OpenShift with odo. Demonstrates hot reloading patterns, live-debugging on remote pods, and utilizing Quarkus or Spring Boot container templates.
  - **(2020)** [developers.redhat.com: Enterprise Kubernetes development with odo: The CLI tool for developers](https://developers.redhat.com/blog/2020/06/16/enterprise-kubernetes-development-with-odo-the-cli-tool-for-developers) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces the 'odo' command-line application to software engineers targeting Kubernetes clusters. Details workflow optimizations, container build speedups, and localized debugging patterns.
  - **(2020)** [developers.redhat.com: Kubernetes integration and more in odo 2.0](https://developers.redhat.com/blog/2020/10/06/kubernetes-integration-and-more-in-odo-2-0) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses major enhancements in 'odo 2.0', highlighting strict Devfile standards support and the capability to deploy to arbitrary Kubernetes engines instead of being isolated to OpenShift clusters.
#### Devfiles

  - **(2021)** [developers.redhat.com: Developing your own custom devfiles for odo 2.0](https://developers.redhat.com/blog/2021/02/12/developing-your-own-custom-devfiles-for-odo-2-0) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Thorough explanation of structuring, writing, and applying custom Devfiles within the odo ecosystem to mandate unified container development environments across large engineering divisions.
#### Source-to-Image

  - **(2018)** [developers.redhat.com - S2i](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Delivers technical insight on Source-to-Image (S2I) execution modes, comparing continuous deployment direct from code versus deploying pre-compiled binaries via specialized pipelines inside Red Hat runtimes.
### Security

#### Continuous Delivery Security

  - **(2021)** [openshift.com: Using OpenShift Pipelines to Automate Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/blog/using-openshift-pipelines-to-automate-red-hat-advanced-cluster-security-for-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines deployment strategies of Red Hat Advanced Cluster Security (RHACS) directly into Tekton-based OpenShift Pipelines. Demonstrates early container image scanning, compliance validations, and proactive security gate blocking.

---
💡 **Explore Related:** [Registries](./registries.md) | [Jenkins Alternatives](./jenkins-alternatives.md) | [Argo](./argo.md)

