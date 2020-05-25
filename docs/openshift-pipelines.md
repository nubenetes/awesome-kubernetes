# OpenShift Pipelines
- [Deploying Jenkins on OpenShift](#deploying-jenkins-on-openshift)
    - [Jenkins Container Images in OpenShift](#jenkins-container-images-in-openshift)
- [External Jenkins Integration with OpenShift](#external-jenkins-integration-with-openshift)
- [Improving Jenkins’ performance on Openshift](#improving-jenkins-performance-on-openshift)
- [Building applications in OpenShift](#building-applications-in-openshift)
    - [OpenShift Pipelines with Build Config](#openshift-pipelines-with-build-config)
    - [OpenShift Pipelines with S2i](#openshift-pipelines-with-s2i)
        - [OpenShift Pipelines with S2i and Jenkins Blue Ocean. Deploying Blue Ocean on OpenShift](#openshift-pipelines-with-s2i-and-jenkins-blue-ocean-deploying-blue-ocean-on-openshift)
- [OpenShift Deployments with Deployment Descriptor](#openshift-deployments-with-deployment-descriptor)
- [OpenShift Deployments with GitHub Actions](#openshift-deployments-with-github-actions)
- [Deployments with OpenShift HA in Multiple Datacenters](#deployments-with-openshift-ha-in-multiple-datacenters)
- [ODO - OpenShift Command line for Developers](#odo---openshift-command-line-for-developers)
- [OpenShift Pipelines](#openshift-pipelines)
    - [Jenkins CICD Getting started with Groovy and Docker Containers](#jenkins-cicd-getting-started-with-groovy-and-docker-containers)
    - [Fabric8 Pipeline Library](#fabric8-pipeline-library)
    - [Jenkins Pipelines with OpenShift 3](#jenkins-pipelines-with-openshift-3)
    - [OpenShift Jenkins Pipeline (DSL) Plugin](#openshift-jenkins-pipeline-dsl-plugin)
        - [Red Hat Communities of Practice](#red-hat-communities-of-practice)
        - [Jenkins Pipelines in OpenShift 4](#jenkins-pipelines-in-openshift-4)
    - [OpenShift Pipelines (aka Tekton CI/CD Pipelines)](#openshift-pipelines-aka-tekton-cicd-pipelines)
        - [Tekton and Tekton Pipelines](#tekton-and-tekton-pipelines)
- [Slides](#slides)

##  Deploying Jenkins on OpenShift
* [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins)
* [opensource.com: Running Jenkins builds in Openshift containers](https://opensource.com/article/18/4/running-jenkins-builds-containers)
* [blog.openshift.com: Deploying Jenkins on OpenShift: Part 1](https://blog.openshift.com/deploying-jenkins-on-openshift-part-1/)
* [cloudowski.com: Jenkins on OpenShift - how to use and customize it in a cloud-native way 🌟](https://cloudowski.com/articles/jenkins-on-openshift/)

### Jenkins Container Images in OpenShift
* [docs.okd.io: Jenkins in Openshift](https://docs.okd.io/latest/using_images/other_images/jenkins.html) Openshift provides a container image for running Jenkins. This image provides a Jenkins server instance, which can be used to set up a basic flow for continuous testing, integration, and delivery.
* [OCP 4.2 - Jenkins image](https://docs.openshift.com/container-platform/4.2/openshift_images/using_images/images-other-jenkins-agent.html)

## External Jenkins Integration with OpenShift
* [**uncontained.io**: External Jenkins Integration 🌟](http://v1.uncontained.io/playbooks/continuous_delivery/external-jenkins-integration.html)

## Improving Jenkins’ performance on Openshift
* [blog.openshift.com: Deploying jenkins on openshift - part 1](https://blog.openshift.com/deploying-jenkins-on-openshift-part-1/)
* [blog.openshift.com: Improving jenkins performance on openshift - part 2](https://blog.openshift.com/improving-jenkins-performance-on-openshift-part-2/)

## Building applications in OpenShift
### OpenShift Pipelines with Build Config
* [Dzone: 4 ways to build applications in openshift](https://dzone.com/articles/4-ways-to-build-applications-in-openshift-1)
* [Dzone: OpenShift Quick Start: Build, Deployment, and Pipeline 🌟](https://dzone.com/articles/openshift-quick-start-build-deployment-and-pipelin) Automation is the key to microservices success. Learn how to use the OpenShift platform to implement a continuous build and deployment platform. 
* [slideshare.net: OpenShift Container Platform CI/CD Build & Deploy 🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy)

### OpenShift Pipelines with S2i
* [developers.redhat.com - S2i](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes/)
* [blog.openshift.com: From zero to container deployment hero with OpenShift 3 and S2i (Video) 🌟](https://blog.openshift.com/openshift-3-walkthrough/)
* [developers.redhat.com: Source versus binary S2I workflows with Red Hat OpenShift Application Runtimes](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes/)

#### OpenShift Pipelines with S2i and Jenkins Blue Ocean. Deploying Blue Ocean on OpenShift
- [OpenShift Pipelines with Jenkins Blue Ocean 🌟](https://www.openshift.com/blog/openshift-pipelines-jenkins-blue-ocean)
- [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) Jenkins Blue Ocean for OpenShift Jenkins S2I

<center>
<iframe src="https://www.youtube.com/embed/IQ8H7XNbQ-8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

## OpenShift Deployments with Deployment Descriptor
* [Dzone: a quick guide to deploying java apps on openshift](https://dzone.com/articles/a-quick-guide-to-deploying-java-apps-on-openshift)

## OpenShift Deployments with GitHub Actions
* [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository/)

## Deployments with OpenShift HA in Multiple Datacenters
* [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.openshift.com/blog/deploying-openshift-applications-multiple-datacenters)
* [Using **KubeFed** to deploy applications](https://blog.openshift.comusing-kubefed-to-deploy-applications-to-ocp3-and-ocp4-clusters/)

## ODO - OpenShift Command line for Developers
* [ODO: OpenShift Command line for Developers 🌟](https://github.com/redhat-developer/odo) OpenShift Do (Odo) is a CLI tool for developers who are writing, building, and deploying applications on OpenShift. With Odo, developers get an opinionated CLI tool that supports fast, iterative development which abstracts away Kubernetes and OpenShift concepts, thus allowing them to focus on what's most important to them: code.
* [developers.redhat.com: odo Cheat Sheet](https://developers.redhat.com/cheat-sheets/odo-cheat-sheet/)

## OpenShift Pipelines
### Jenkins CICD Getting started with Groovy and Docker Containers
* [medium: Jenkins CICD Getting started with Groovy and Docker Containers — Part 1](https://blog.isaack.io/articles/2016-08/Jenkins-CICD-Getting-Started-With-Groovy-Part-1)
* [medium: Jenkins CICD Getting started with Groovy and Docker Containers — Part 2](https://medium.com/@fvtool/jenkins-cicd-getting-started-with-groovy-and-docker-containers-part-2-b03a1b934a49)

### Fabric8 Pipeline Library
* [Fabric8](https://fabric8.io/) has been available as a Java client for Kubernetes since 2015, and today is one of the most popular client libraries for Kubernetes (the most popular is [client-go](https://github.com/kubernetes/client-go), which is the client library for the Go programming language on Kubernetes). In recent years, **fabric8 has evolved from a Java client for the Kubernetes REST API to a full-fledged alternative to the kubectl command-line tool for Java-based development**.
* [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client/)
* [CI/CD with fabric8](http://fabric8.io/guide/cdelivery.html)
* [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library)
* [medium - fabric8, please check out jenkins X instead](https://medium.com/@jstrachan/fabric8-please-check-out-jenkins-x-instead-8295a025173a)
* [github - fabric8, maven plugin](https://github.com/fabric8io/fabric8-maven-plugin )

### Jenkins Pipelines with OpenShift 3
* [slideshare.net: CI/CD with Openshift and Jenkins 🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins)
* [github - using jenkins pipelines with OKD](https://github.com/openshift/origin/tree/master/examples/jenkins/pipeline)

### OpenShift Jenkins Pipeline (DSL) Plugin
* [Building Declarative Pipelines with OpenShift DSL Plugin 🌟](https://blog.openshift.com/building-declarative-pipelines-openshift-dsl-plugin/)
* [blog.openshift.com - Building Declarative Pipelines with OpenShift DSL Plugin](https://blog.openshift.com/building-declarative-pipelines-openshift-dsl-plugin/)
* [Dzone - Continuous Delivery with OpenShift and Jenkins: A/B Testing 🌟](https://dzone.com/articles/continuous-delivery-with-openshift-and-jenkins-ab)
* [docs.openshift.com: OpenShift 3.11 Pipeline Builds with OpenShift Jenkins Image and OpenShift DSL](https://docs.openshift.com/container-platform/3.11/dev_guide/dev_tutorials/openshift_pipeline.html)

#### Red Hat Communities of Practice
* [OpenShift Container Pipelines Samples 🌟](https://github.com/redhat-cop/container-pipelines)
* [OpenShift Pipeline Library 🌟](https://github.com/redhat-cop/pipeline-library) A repository of Jenkins pipeline files we can reference from elsewhere

#### Jenkins Pipelines in OpenShift 4
* [developers.redhat.com - Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4/)

### OpenShift Pipelines (aka Tekton CI/CD Pipelines)
* [https://blog.openshift.com: Cloud-Native CI/CD with OpenShift Pipelines based on Tekton](https://blog.openshift.com/cloud-native-ci-cd-with-openshift-pipelines/)
* [github: OpenShift Pipelines Tutorial 🌟](https://github.com/openshift/pipelines-tutorial)
* [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab)
* [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines/)

#### Tekton and Tekton Pipelines
* [**tekton.dev**](https://tekton.dev/)
* [tekton.dev/try: Interactive Tutorials](https://tekton.dev/try/)
* [Tekton community](https://github.com/tektoncd/community)
* [github: Tekton Pipelines](https://github.com/tektoncd/pipeline)
* [Tekton Pipelines Docs](https://tekton.dev/docs/pipelines/pipelines/)
* [opensource.googleblog.com: The Tekton Pipelines Beta release](https://opensource.googleblog.com/2020/05/the-tekton-pipelines-beta-release.html)

## Slides
<iframe src="//www.slideshare.net/slideshow/embed_code/key/GNg4EksIW8cNFg" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins" title="CI/CD with Openshift and Jenkins" target="_blank">CI/CD with Openshift and Jenkins</a> </strong> von <strong><a href="https://www.slideshare.net/arilivigni" target="_blank">Ari LiVigni</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/rL59hI2J3e7j6T" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy" title="OPENSHIFT CONTAINER PLATFORM CI/CD Build &amp; Deploy" target="_blank">OPENSHIFT CONTAINER PLATFORM CI/CD Build &amp; Deploy</a> </strong> from <strong><a href="https://www.slideshare.net/mozillabros" target="_blank">Natale Vinto</a></strong> </div>
