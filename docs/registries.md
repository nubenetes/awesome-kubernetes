# Docker Registries. Quay, Nexus, JFrog Artifactory, Harbor and more

1. [Introduction](#introduction)
2. [OpenShift Registry](#openshift-registry)
3. [Quay Registry](#quay-registry)
4. [Nexus Repository Manager (NXRM) 3](#nexus-repository-manager-nxrm-3)
    1. [Getting Started](#getting-started)
    2. [Setup Nexus Kubernetes. Run nexus3 with docker in a kubernetes cluster](#setup-nexus-kubernetes-run-nexus3-with-docker-in-a-kubernetes-cluster)
    3. [Nexus as a Docker repo](#nexus-as-a-docker-repo)
        1. [Secure Docker Registries](#secure-docker-registries)
    4. [SSL/TLS Certificates](#ssltls-certificates)
        1. [Add Insecure Registry to Docker](#add-insecure-registry-to-docker)
    5. [Jenkins Integration with Nexus](#jenkins-integration-with-nexus)
    6. [Nexus 3 Configuration as Code](#nexus-3-configuration-as-code)
    7. [Nexus CLI](#nexus-cli)
    8. [Sonatype Nexus Community](#sonatype-nexus-community)
5. [JFrog Artifactory](#jfrog-artifactory)
6. [Harbor. Cloud native repository for Kubernetes](#harbor-cloud-native-repository-for-kubernetes)
7. [Other Alternatives](#other-alternatives)

## Introduction

- A Docker registry is a place to store and distribute Docker images.
- It serves as a target for your docker push and docker pull commands.
- [Dzone refcard: Using Repository Managers](https://dzone.com/refcardz/binary-repository-management) The Best Way to Organize, Store, and Distribute Software Components
- [Dzone Refcard: Binary Repository Management](https://dzone.com/refcardz/binary-repository-management)

## OpenShift Registry

- [docs.openshift.com: Integrated OpenShift Container Platform registry](https://docs.openshift.com/container-platform/4.8/registry/architecture-component-imageregistry.html)
- [cloudowski.com: Openshift ImageStreams](https://cloudowski.com/articles/why-managing-container-images-on-openshift-is-better-than-on-kubernetes/)
- The registry in OCP4 is now managed by an Operator instead of ```oc adm``` registry.

## Quay Registry

- [Quay.io](https://quay.io/) is a hosted Docker registry from CoreOS:
    - Main features:
        - “Powerful build triggers” 
        - “Advanced team permissions”
        - “Secure storage”
    - One of the more enterprise-friendly options out there, offering fine-grained permission controls.
    - They support any git server and let you build advanced workflows by doing things like mapping git branches to Docker tags so that when you commit code it automatically builds a corresponding image.
    - Quay offers unlimited free public repositories. Otherwise, you pay by the number of private repositories. There’s no extra charge for storage or bandwidth.
- [Quay 3.0 released in May 2019](https://www.redhat.com/en/blog/introducing-red-hat-quay-3-registry-your-linux-and-windows-containers): support for multiple architectures, Windows containers, and a [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)-based image to this container image registry.
- [Quay 3.1 released in September 2019](https://www.redhat.com/en/blog/red-hat-quay-31-now-even-better-across-distributed-environments): The newest Quay feature is repository mirroring, which complements our existing geographic replication features. Repository mirroring reflects content between distinct, different registries. With this, you can synchronize whitelisted repositories or a source registry subset into Quay. This makes it much easier to distribute images and related data through Quay. 
- [Quay Community Edition operator](https://github.com/redhat-cop/quay-operator)
- [Quay 3.1 Certified Operator is not available in Openshift and must be purchased](https://www.openshift.com/products/quay)
- Open Source [ProjectQuay.io](https://www.projectquay.io/) Container Registry: 
    - [Red Hat Introduces open source Project Quay container registry](https://www.redhat.com/en/blog/red-hat-introduces-open-source-project-quay-container-registry) 
    - [github.com/quay](https://github.com/quay)
- [openshift.com: Keep Your Applications Secure With Automatic Rebuilds](https://www.openshift.com/blog/keep-your-applications-secure-with-automatic-rebuilds)

## Nexus Repository Manager (NXRM) 3

- [sonatype.com/nexus-repository-oss](https://www.sonatype.com/nexus-repository-oss)
- [Nexus Repository Manager (NXRM) 3 🌟](https://help.sonatype.com/repomanager3)

### Getting Started

- [Dzone: Getting started with Nexus](https://dzone.com/articles/getting-started-nexus-maven)
- [Dzone: Nexus Guide Update January 2018](https://dzone.com/articles/nexus-guide-update-january-2018)

### Setup Nexus Kubernetes. Run nexus3 with docker in a kubernetes cluster

- [Sonatype Nexus Community: Nexus Kubernetes OpenShift 🌟](https://github.com/sonatype-nexus-community/nexus-kubernetes-openshift)
- [Devopscube.com: Setup Nexus Kubernetes 🌟](https://devopscube.com/setup-nexus-kubernetes/)
- [stackoverflow: run nexus3 with docker in a kubernetes cluster](https://stackoverflow.com/questions/42766349/run-nexus-3-with-docker-in-a-kubernetes-cluster)
- [https://github.com/jetstack/cert-manager/](https://github.com/jetstack/cert-manager/)

### Nexus as a Docker repo

- [Docker Registry](https://help.sonatype.com/repomanager3/formats/docker-registry)
- [blog.sonatype.com: Using Nexus 3 as Your Repository – Part 3: Docker Images 🌟](https://blog.sonatype.com/using-nexus-3-as-your-repository-part-3-docker-images)
- [Dzone: Setting up a docker private registry with authentication](https://dzone.com/articles/setting-up-a-docker-private-registry-with-authenti)
- [sonatype: how to delete docker images from Nexus Repository Manager](https://support.sonatype.com/hc/en-us/articles/360009696054-How-to-delete-docker-images-from-Nexus-Repository-Manager)
- [hackermoon.com: cleanup old docker images from nexus repository](https://hackernoon.com/cleanup-old-docker-images-from-nexus-repository-617b1004dad8)

#### Secure Docker Registries

- [guides.sonatype.com: secure docker registries](https://guides.sonatype.com/repo3/technical-guides/secure-docker-registries/)
- [support.sonatype.com: Using self signed certificates with Nexus Repository Manager and Docker Daemon](https://support.sonatype.com/hc/en-us/articles/217542177-Using-Self-Signed-Certificates-with-Nexus-Repository-Manager-and-Docker-Daemon)

### SSL/TLS Certificates

- [guides.sonatype.com: secure docker registries](https://guides.sonatype.com/repo3/technical-guides/secure-docker-registries/)
- [support.sonatype.com: SSL Certificate Guide](https://support.sonatype.com/hc/en-us/articles/213465768-SSL-Certificate-Guide)
- [help.sonatype.com: Inbound SSL - Configuring to Serve Content via HTTPS](https://help.sonatype.com/repomanager3/security/configuring-ssl?_ga=2.250230211.411976214.1575978022-1513910029.1575978022#ConfiguringSSL-InboundSSL-ConfiguringtoServeContentviaHTTPS)
- [nginx.com: Using Free Let’s Encrypt SSL/TLS Certificates with NGINX](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/)

#### Add Insecure Registry to Docker

- [Test an insecure registry 🌟](https://docs.docker.com/registry/insecure/)
- [Configure Docker Service To Use Insecure Registry](https://github.com/Juniper/contrail-docker/wiki/Configure-docker-service-to-use-insecure-registry)
- [Running an insecure registry –insecure-registry](https://forums.docker.com/t/running-an-insecure-registry-insecure-registry/8159)
- [Add Insecure Registry to Docker](https://intellipaat.com/community/19079/add-insecure-registry-to-docker)

### Jenkins Integration with Nexus

- [Nexus Platform Plugin for Jenkins](https://help.sonatype.com/integrations/nexus-and-continuous-integration/nexus-platform-plugin-for-jenkins)
- [Jenkins: Publish Maven Artifacts to Nexus OSS Using Pipelines or Maven Jobs 🌟](https://dzone.com/articles/jenkins-publish-maven-artifacts-to-nexus-oss-using) Check out how following this tutorial to connect Maven and Nexus OSS can help increase your CI/CD pipelines.
- [Continuous Delivery with Sonatype Nexus, Jenkins and the Cloudogu Ecosystem](https://cloudogu.com/en/blog/cd-with-nexus-jenkins-ces)
- [youtube: Jenkins Integration with Nexus](https://www.youtube.com/watch?v=qbO4MTESiJQ)
- [youtube: uploading artifacts from jenkins to nexus](https://www.youtube.com/watch?v=7NmGSnqLd58)

### Nexus 3 Configuration as Code

- [github.com/samrocketman/nexus3-config-as-code](https://github.com/samrocketman/nexus3-config-as-code) 
- [blog.mimacom.com/automate-nexus](https://blog.mimacom.com/automate-nexus/) 
- [github.com/cinhtau/sonatype-nexus-waffle](https://github.com/cinhtau/sonatype-nexus-waffle) 

### Nexus CLI

- [GitHub: Nexus-CLI](https://github.com/mlabouardy/nexus-cli)
- [nexus3-cli.readthedocs.io](https://nexus3-cli.readthedocs.io)

### Sonatype Nexus Community

- [Sonatype Nexus Community 🌟](https://github.com/sonatype-nexus-community)
- Check out the [Nexus3](https://stackoverflow.com/questions/tagged/nexus3) tag on Stack Overflow

## JFrog Artifactory

- [JFrog Artifactory: Your Kubernetes Registry](https://jfrog.com/blog/jfrog-artifactory-kubernetes-registry/)
- [JFrog Container Registry](https://jfrog.com/container-registry/) The world’s most advanced, powerful, hybrid Docker and Helm registry. Power your world of Docker without limits.
- [The JFrog journey to kubernetes: best practices for taking your containers all the way to production](https://jfrog.com/whitepaper/the-jfrog-journey-to-kubernetes-best-practices-for-taking-your-containers-all-the-way-to-production/)
- [jfrog.com: Control Your Kubernetes Voyage with JFrog Artifactory 🌟](https://jfrog.com/blog/control-your-kubernetes-voyage-with-artifactory/) 5-Step Kubernetes CI/CD Process using Artifactory & Helm
- [openshift.com: Cloud DevOps With OpenShift and JFrog](https://www.openshift.com/blog/cloud-devops-with-openshift-and-jfrog)
- [jfrog.com: JFrog and Docker Partner to Combine the Power of JFrog Artifactory and Docker Hub to Improve Quality, Performance, and Developer Experience for Modern Application Development](https://jfrog.com/press/jfrog-docker-partner-to-combine-the-power-jfrog-artifactory-docker-hub/)
- [jfrog.com: How I Leaped Forward My Jenkins Build with JFrog Pipelines](https://jfrog.com/blog/how-i-leaped-forward-my-jenkins-build-with-jfrog-pipelines/)
- [jfrog.com: GitHub vs JFrog: Who Can do the Job for DevOps?](https://jfrog.com/blog/github-vs-jfrog-who-can-do-the-job-for-devops/)
- [seekingalpha.com: JFrog Reminds Me Of MongoDB](https://seekingalpha.com/article/4427517-jfrog-reminds-me-of-mongodb) JFrog’s software is similarly disruptive as MongoDB’s, and likewise its cloud offering is growing faster than the overall company.
- [jfrog.com: Kubernetes Helm Chart Repositories 🌟](https://www.jfrog.com/confluence/display/JFROG/Kubernetes+Helm+Chart+Repositories)
- [jfrog.com: What Artifactory as your kubernetes docker registry means to you](https://jfrog.com/integration/kubernetes-docker-registry/)
- [openshift.com: Using JFrog's Artifactory and Red Hat OpenShift Together](https://www.openshift.com/blog/18333-2)

## Harbor. Cloud native repository for Kubernetes

- [Harbor](https://goharbor.io/) 
- [goharbor.io: Deploy Harbor with the Quick Installation Script](https://goharbor.io/docs/2.0.0/install-config/quick-install-script/)
- [nicholasamorim/ansible-role-harbor](https://github.com/nicholasamorim/ansible-role-harbor)
- [mramanathan/ansible-harbor](https://github.com/mramanathan/ansible-harbor) Ansible playbook to install and setup Harbor
- [galaxy.ansible.com/mkgin/vmware-harbor](https://galaxy.ansible.com/mkgin/vmware-harbor) An Ansible role Installs Harbor from VMware as the dependancies from Docker.
- [freesoft.dev: Ansible Role: Harbor API Codifying](https://freesoft.dev/program/126957220) An Ansible Role to manage Harbor API

## Other Alternatives

- [uber/kraken](https://github.com/uber/kraken) P2P Docker registry capable of distributing TBs of data in seconds
- [medium.com/swlh: Deploy Your Private Docker Registry as a Pod in Kubernetes](https://medium.com/swlh/deploy-your-private-docker-registry-as-a-pod-in-kubernetes-f6a489bf0180) In this tutorial, you'll deploy a TLS-enabled Private Docker Registry as a Pod. This will help you to push your custom-built images to the registry, which later can be pulled by any of the worker nodes.

