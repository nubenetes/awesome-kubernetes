# Openshift Pipelines

!!! info "Architectural Context"
    Detailed reference for Openshift Pipelines in the context of Engineering Pipeline.

## Table of Contents

---

  - [blog.openshift.com: Deploying Jenkins on OpenShift: Part 1](https://www.redhat.com/en/blog/deploying-jenkins-on-openshift-part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OCP 4.2 - Jenkins image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.2/html/images/using-images#images-other-jenkins-agent)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: Improving jenkins performance on openshift - part 2](https://www.redhat.com/en/blog/improving-jenkins-performance-on-openshift-part-2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift Pipelines with Jenkins Blue Ocean 🌟](https://www.redhat.com/en/blog/openshift-pipelines-jenkins-blue-ocean)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.redhat.com/en/blog/deploying-openshift-applications-multiple-datacenters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: odo Cheat Sheet](https://developers.redhat.com/cheat-sheets)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: Using OpenShift Pipelines to Automate Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/blog/using-openshift-pipelines-to-automate-red-hat-advanced-cluster-security-for-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [CI/CD with fabric8](http://fabric8.io/guide/cdelivery.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: CI/CD with Openshift and Jenkins 🌟](https://www.slideshare.net/slideshow/cicd-with-openshift-and-jenkins/57944430)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github - using jenkins pipelines with OKD](https://github.com/openshift/origin/tree/main/examples/jenkins/pipeline)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟](https://www.redhat.com/en/blog/building-declarative-pipelines-openshift-dsl-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Jenkins Pipeline Syntax: Scripted Syntax (Groovy DSL syntax) & Declarative Syntax 🌟](https://www.jenkins.io/doc/book/pipeline/syntax)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: OpenShift 3.11 Pipeline Builds with OpenShift Jenkins Image and OpenShift DSL](https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/developer_guide/tutorials#dev-guide-openshift-pipeline-builds)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Simply Explained: OpenShift and Jenkins Pipelines](https://www.redhat.com/en/blog/jenkins-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: Cloud-Native CI/CD with OpenShift Pipelines based on Tekton](https://www.redhat.com/en/blog/cloud-native-ci-cd-with-openshift-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: OpenShift Pipelines Advanced Triggers Part 1 - Triggering Different Project Builds in the Same Repository](https://www.redhat.com/en/blog/openshift-pipelines-advanced-triggers-part-1-triggering-different-project-builds-in-the-same-repository)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: running jenkins builds containers 🌟](https://opensource.com/article/18/4/running-jenkins-builds-containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudowski.com: Jenkins on OpenShift - how to use and customize it in a cloud-native way 🌟](https://cloudowski.com/articles/jenkins-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: An easier way to create custom Jenkins containers](https://developers.redhat.com/blog/2020/06/04/an-easier-way-to-create-custom-jenkins-containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: OpenShift Container Platform CI/CD Build & Deploy 🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com - S2i](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ODO: OpenShift Command line for Developers 🌟](https://github.com/redhat-developer/odo)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Enterprise Kubernetes development with odo: The CLI tool for developers](https://developers.redhat.com/blog/2020/06/16/enterprise-kubernetes-development-with-odo-the-cli-tool-for-developers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Kubernetes integration and more in odo 2.0](https://developers.redhat.com/blog/2020/10/06/kubernetes-integration-and-more-in-odo-2-0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [piotrminkowski.com: Java Development on OpenShift with odo](https://piotrminkowski.com/2021/02/05/java-development-on-openshift-with-odo)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Developing your own custom devfiles for odo 2.0](https://developers.redhat.com/blog/2021/02/12/developing-your-own-custom-devfiles-for-odo-2-0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Fabric8](https://fabric8.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift Container Pipelines Samples 🌟](https://github.com/redhat-cop/container-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift Pipeline Library 🌟](https://github.com/redhat-cop/pipeline-library)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com - Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/openshift/pipelines-tutorial](https://github.com/openshift/pipelines-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
