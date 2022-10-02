# OpenShift Pipelines

1. [Deploying Jenkins on OpenShift](#deploying-jenkins-on-openshift)
    1. [Jenkins Container Images in OpenShift](#jenkins-container-images-in-openshift)
2. [External Jenkins Integration with OpenShift](#external-jenkins-integration-with-openshift)
3. [Improving Jenkins’ performance on Openshift](#improving-jenkins-performance-on-openshift)
4. [Building applications in OpenShift](#building-applications-in-openshift)
    1. [OpenShift Pipelines with Build Config](#openshift-pipelines-with-build-config)
    2. [OpenShift Pipelines with S2i](#openshift-pipelines-with-s2i)
        1. [OpenShift Pipelines with S2i and Jenkins Blue Ocean. Deploying Blue Ocean on OpenShift](#openshift-pipelines-with-s2i-and-jenkins-blue-ocean-deploying-blue-ocean-on-openshift)
5. [OpenShift Deployments with Deployment Descriptor](#openshift-deployments-with-deployment-descriptor)
6. [OpenShift Deployments with GitHub Actions](#openshift-deployments-with-github-actions)
7. [Deployments with OpenShift HA in Multiple Datacenters](#deployments-with-openshift-ha-in-multiple-datacenters)
8. [ODO - OpenShift Command line for Developers](#odo---openshift-command-line-for-developers)
9. [All about OpenShift Pipelines](#all-about-openshift-pipelines)
    1. [Jenkins CICD Getting started with Groovy and Docker Containers](#jenkins-cicd-getting-started-with-groovy-and-docker-containers)
    2. [Fabric8 Pipeline Library (deprecated)](#fabric8-pipeline-library-deprecated)
    3. [Eclipse JKube Pipeline Library (formerly known as Fabric8 Kubernetes Plugin). Kubernetes & OpenShift Plugins](#eclipse-jkube-pipeline-library-formerly-known-as-fabric8-kubernetes-plugin-kubernetes--openshift-plugins)
    4. [Jenkins Pipelines with OpenShift 3](#jenkins-pipelines-with-openshift-3)
    5. [OpenShift Jenkins Pipeline (DSL) Plugin. Scripted Syntax (Groovy DSL syntax) VS Declarative Syntax](#openshift-jenkins-pipeline-dsl-plugin-scripted-syntax-groovy-dsl-syntax-vs-declarative-syntax)
        1. [Red Hat Communities of Practice](#red-hat-communities-of-practice)
        2. [Jenkins Pipelines in OpenShift 4](#jenkins-pipelines-in-openshift-4)
    6. [OpenShift Pipelines (aka Tekton CI/CD Pipelines)](#openshift-pipelines-aka-tekton-cicd-pipelines)
        1. [Tekton and Tekton Pipelines](#tekton-and-tekton-pipelines)
10. [Videos](#videos)
11. [Slides](#slides)

##  Deploying Jenkins on OpenShift

- [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins)
- [opensource.com: Running Jenkins builds in Openshift containers](https://opensource.com/article/18/4/running-jenkins-builds-containers)
- [blog.openshift.com: Deploying Jenkins on OpenShift: Part 1](https://blog.openshift.com/deploying-jenkins-on-openshift-part-1/)
- [cloudowski.com: Jenkins on OpenShift - how to use and customize it in a cloud-native way 🌟](https://cloudowski.com/articles/jenkins-on-openshift/)
- [developers.redhat.com: An easier way to create custom Jenkins containers in OpenShift 4 🌟](https://developers.redhat.com/blog/2020/06/04/an-easier-way-to-create-custom-jenkins-containers/) Create your own custom Jenkins container image by aggregating readily available containers in a pod template.

### Jenkins Container Images in OpenShift

- [docs.okd.io: Jenkins in Openshift](https://docs.okd.io/latest/using_images/other_images/jenkins.html) Openshift provides a container image for running Jenkins. This image provides a Jenkins server instance, which can be used to set up a basic flow for continuous testing, integration, and delivery.
- [OCP 4.2 - Jenkins image](https://docs.openshift.com/container-platform/4.2/openshift_images/using_images/images-other-jenkins-agent.html)

## External Jenkins Integration with OpenShift

- [**uncontained.io**: External Jenkins Integration 🌟](http://v1.uncontained.io/playbooks/continuous_delivery/external-jenkins-integration.html)

## Improving Jenkins’ performance on Openshift

- [blog.openshift.com: Deploying jenkins on openshift - part 1](https://blog.openshift.com/deploying-jenkins-on-openshift-part-1/)
- [blog.openshift.com: Improving jenkins performance on openshift - part 2](https://blog.openshift.com/improving-jenkins-performance-on-openshift-part-2/)

## Building applications in OpenShift

### OpenShift Pipelines with Build Config

- [Dzone: 4 ways to build applications in openshift](https://dzone.com/articles/4-ways-to-build-applications-in-openshift-1)
- [Dzone: OpenShift Quick Start: Build, Deployment, and Pipeline 🌟](https://dzone.com/articles/openshift-quick-start-build-deployment-and-pipelin) Automation is the key to microservices success. Learn how to use the OpenShift platform to implement a continuous build and deployment platform. 
- [slideshare.net: OpenShift Container Platform CI/CD Build & Deploy 🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy)

### OpenShift Pipelines with S2i

- [developers.redhat.com - S2i](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes/)
- [blog.openshift.com: From zero to container deployment hero with OpenShift 3 and S2i (Video) 🌟](https://blog.openshift.com/openshift-3-walkthrough/)
- [developers.redhat.com: Source versus binary S2I workflows with Red Hat OpenShift Application Runtimes](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes/)

#### OpenShift Pipelines with S2i and Jenkins Blue Ocean. Deploying Blue Ocean on OpenShift

- [OpenShift Pipelines with Jenkins Blue Ocean 🌟](https://www.openshift.com/blog/openshift-pipelines-jenkins-blue-ocean)
- [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) Jenkins Blue Ocean for OpenShift Jenkins S2I

## OpenShift Deployments with Deployment Descriptor

- [Dzone: a quick guide to deploying java apps on openshift](https://dzone.com/articles/a-quick-guide-to-deploying-java-apps-on-openshift)

## OpenShift Deployments with GitHub Actions

- [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository/)

## Deployments with OpenShift HA in Multiple Datacenters

- [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.openshift.com/blog/deploying-openshift-applications-multiple-datacenters)
- [Using **KubeFed** to deploy applications](https://blog.openshift.comusing-kubefed-to-deploy-applications-to-ocp3-and-ocp4-clusters/)

## ODO - OpenShift Command line for Developers

- [ODO: OpenShift Command line for Developers 🌟](https://github.com/redhat-developer/odo) OpenShift Do (Odo) is a CLI tool for developers who are writing, building, and deploying applications on OpenShift. With Odo, developers get an opinionated CLI tool that supports fast, iterative development which abstracts away Kubernetes and OpenShift concepts, thus allowing them to focus on what's most important to them: code.
- [developers.redhat.com: odo Cheat Sheet](https://developers.redhat.com/cheat-sheets/odo-cheat-sheet/)
- [developers.redhat.com: Enterprise Kubernetes development with odo: The CLI tool for developers](https://developers.redhat.com/blog/2020/06/16/enterprise-kubernetes-development-with-odo-the-cli-tool-for-developers/)
- [developers.redhat.com: Kubernetes integration and more in odo 2.0](https://developers.redhat.com/blog/2020/10/06/kubernetes-integration-and-more-in-odo-2-0/)
- [piotrminkowski.com: Java Development on OpenShift with odo](https://piotrminkowski.com/2021/02/05/java-development-on-openshift-with-odo/)
- [developers.redhat.com: Developing your own custom devfiles for odo 2.0](https://developers.redhat.com/blog/2021/02/12/developing-your-own-custom-devfiles-for-odo-2-0/)

## All about OpenShift Pipelines

### Jenkins CICD Getting started with Groovy and Docker Containers

- [medium: Jenkins CICD Getting started with Groovy and Docker Containers — Part 1](https://blog.isaack.io/articles/2016-08/Jenkins-CICD-Getting-Started-With-Groovy-Part-1)
- [medium: Jenkins CICD Getting started with Groovy and Docker Containers — Part 2](https://medium.com/@fvtool/jenkins-cicd-getting-started-with-groovy-and-docker-containers-part-2-b03a1b934a49)
- [openshift.com: Using OpenShift Pipelines to Automate Red Hat Advanced Cluster Security for Kubernetes](https://www.openshift.com/blog/using-openshift-pipelines-to-automate-red-hat-advanced-cluster-security-for-kubernetes)

### Fabric8 Pipeline Library (deprecated)

- [Fabric8](https://fabric8.io/) has been available as a Java client for Kubernetes since 2015, and today is one of the most popular client libraries for Kubernetes (the most popular is [client-go](https://github.com/kubernetes/client-go), which is the client library for the Go programming language on Kubernetes). In recent years, **fabric8 has evolved from a Java client for the Kubernetes REST API to a full-fledged alternative to the kubectl command-line tool for Java-based development**.
- [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client/)
- [CI/CD with fabric8](http://fabric8.io/guide/cdelivery.html)
- [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library)
- [medium - fabric8, please check out jenkins X instead](https://medium.com/@jstrachan/fabric8-please-check-out-jenkins-x-instead-8295a025173a)
- [github - fabric8, maven plugin](https://github.com/fabric8io/fabric8-maven-plugin )

### Eclipse JKube Pipeline Library (formerly known as Fabric8 Kubernetes Plugin). Kubernetes & OpenShift Plugins

- [Eclipse JKube 🌟](https://www.eclipse.org/jkube/) Cloud-Native Java Applications without a hassle. Eclipse JKube is a collection of Maven and Gradle plugins, and libraries that are used for building container images using Docker, JIB or S2I build strategies. Eclipse JKube generates and deploys Kubernetes/OpenShift manifests at compile time too. It brings your Java applications on to Kubernetes and OpenShift by leveraging the tasks required to make your application cloud-native. Eclipse JKube also provides a set of tools such as watch, debug, log, etc. to improve your developer experience.
- [GitHub: Eclipse JKube](https://github.com/eclipse/jkube)

### Jenkins Pipelines with OpenShift 3

- [slideshare.net: CI/CD with Openshift and Jenkins 🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins)
- [github - using jenkins pipelines with OKD](https://github.com/openshift/origin/tree/master/examples/jenkins/pipeline)

### OpenShift Jenkins Pipeline (DSL) Plugin. Scripted Syntax (Groovy DSL syntax) VS Declarative Syntax

- [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟](https://www.openshift.com/blog/building-declarative-pipelines-openshift-dsl-plugin):
    - [Jenkins Pipeline Syntax: Scripted Syntax (Groovy DSL syntax) & Declarative Syntax 🌟](https://www.jenkins.io/doc/book/pipeline/syntax/): 
        - **Version 2.5 of the "Pipeline plugin" released in 2016/05/16 introduces support for Declarative Pipeline syntax**.
        - Declarative Pipeline is a relatively recent addition to Jenkins Pipeline which presents a more simplified and opinionated syntax on top of the Pipeline sub-systems. 
    - **Jenkinsfiles have only become an integral part of Jenkins since version 2** but they have quickly become the de-facto standard for building continuous delivery pipelines with Jenkins. **Jenkinsfile allows defining pipelines as code using a Groovy DSL syntax** and checking it into source version control which allows you to track, review, audit, and manage the lifecycle of changes to the continuous delivery pipelines the same way that you manage the source code of your application. 
    - Although the **Groovy DSL syntax which is referred to as the scripted syntax** is the more well-known and established syntax for building Jenkins pipelines and **was the default when Jenkins 2 was released**, support for a **newer declarative syntax is also added since Jenkins 2.5** in order to offer a simplified way for controlling all aspects of the pipeline. Although the scripted and declarative syntax provides two ways to define your pipeline, they both translate to the same execution blocks in Jenkins and achieve the same result. 
    - The declarative syntax in its simplest form is composed of an agent which defines the Jenkins slave to be used for executing the pipeline and a number of stages and each stage with a number of steps to be performed. 
- [Dzone - Continuous Delivery with OpenShift and Jenkins: A/B Testing 🌟](https://dzone.com/articles/continuous-delivery-with-openshift-and-jenkins-ab)
- [docs.openshift.com: OpenShift 3.11 Pipeline Builds with OpenShift Jenkins Image and OpenShift DSL](https://docs.openshift.com/container-platform/3.11/dev_guide/dev_tutorials/openshift_pipeline.html)

#### Red Hat Communities of Practice

- [OpenShift Container Pipelines Samples 🌟](https://github.com/redhat-cop/container-pipelines)
- [OpenShift Pipeline Library 🌟](https://github.com/redhat-cop/pipeline-library) A repository of Jenkins pipeline files we can reference from elsewhere

#### Jenkins Pipelines in OpenShift 4

- [developers.redhat.com - Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4/)
- [Simply Explained: OpenShift and Jenkins Pipelines](https://www.openshift.com/blog/jenkins-pipelines)

### OpenShift Pipelines (aka Tekton CI/CD Pipelines)

- [openshift.com: Cloud-Native CI/CD with OpenShift Pipelines based on Tekton](https://www.openshift.com/blog/cloud-native-ci-cd-with-openshift-pipelines)
- [github: OpenShift Pipelines Tutorial 🌟](https://github.com/openshift/pipelines-tutorial)
- [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab)
- [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines/)
- [openshift.com: OpenShift Pipelines Advanced Triggers Part 1 - Triggering Different Project Builds in the Same Repository](https://www.openshift.com/blog/openshift-pipelines-advanced-triggers-part-1-triggering-different-project-builds-in-the-same-repository)

#### Tekton and Tekton Pipelines

- [==Tekton and Tekton Pipelines==](tekton.md)

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/IQ8H7XNbQ-8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Slides

<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/GNg4EksIW8cNFg" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins" title="CI/CD with Openshift and Jenkins" target="_blank">CI/CD with Openshift and Jenkins</a> </strong> from <strong><a href="//www.slideshare.net/arilivigni" target="_blank">Ari LiVigni</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/rL59hI2J3e7j6T" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy" title="OPENSHIFT CONTAINER PLATFORM CI/CD Build &amp; Deploy" target="_blank">OPENSHIFT CONTAINER PLATFORM CI/CD Build &amp; Deploy</a> </strong> from <strong><a href="//www.slideshare.net/mozillabros" target="_blank">Natale Vinto</a></strong> </div>
</center>
</details>
