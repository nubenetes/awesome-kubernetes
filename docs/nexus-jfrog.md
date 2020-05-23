# Nexus & JFrog Artifactory
- [Nexus Repository Manager (NXRM) 3](#nexus-repository-manager-nxrm-3)
    - [Getting Started](#getting-started)
    - [Setup Nexus Kubernetes. Run nexus3 with docker in a kubernetes cluster](#setup-nexus-kubernetes-run-nexus3-with-docker-in-a-kubernetes-cluster)
    - [Nexus as a Docker repo](#nexus-as-a-docker-repo)
        - [Secure Docker Registries](#secure-docker-registries)
    - [SSL/TLS Certificates](#ssltls-certificates)
        - [Add Insecure Registry to Docker](#add-insecure-registry-to-docker)
    - [Jenkins Integration with Nexus](#jenkins-integration-with-nexus)
    - [Nexus 3 Configuration as Code](#nexus-3-configuration-as-code)
    - [Nexus CLI](#nexus-cli)
    - [Sonatype Nexus Community](#sonatype-nexus-community)
- [JFrog Artifactory](#jfrog-artifactory)

## Nexus Repository Manager (NXRM) 3
* [sonatype.com/nexus-repository-oss](https://www.sonatype.com/nexus-repository-oss)
* [Nexus Repository Manager (NXRM) 3 🌟](https://help.sonatype.com/repomanager3)

### Getting Started
* [Dzone refcard: Using Repository Managers](https://dzone.com/refcardz/binary-repository-management) The Best Way to Organize, Store, and Distribute Software Components
* [Dzone Refcard: Binary Repository Management](https://dzone.com/refcardz/binary-repository-management)
* [Dzone: Getting started with Nexus](https://dzone.com/articles/getting-started-nexus-maven)
* [Dzone: Nexus Guide Update January 2018](https://dzone.com/articles/nexus-guide-update-january-2018)

### Setup Nexus Kubernetes. Run nexus3 with docker in a kubernetes cluster
* [Sonatype Nexus Community: Nexus Kubernetes OpenShift 🌟](https://github.com/sonatype-nexus-community/nexus-kubernetes-openshift)
* [Devopscube.com: Setup Nexus Kubernetes 🌟](https://devopscube.com/setup-nexus-kubernetes/)
* [stackoverflow: run nexus3 with docker in a kubernetes cluster](https://stackoverflow.com/questions/42766349/run-nexus-3-with-docker-in-a-kubernetes-cluster)
* [https://github.com/jetstack/cert-manager/](https://github.com/jetstack/cert-manager/)

### Nexus as a Docker repo 
* [Docker Registry](https://help.sonatype.com/repomanager3/formats/docker-registry)
* [blog.sonatype.com: Using Nexus 3 as Your Repository – Part 3: Docker Images 🌟](https://blog.sonatype.com/using-nexus-3-as-your-repository-part-3-docker-images)
* [Dzone: Setting up a docker private registry with authentication](https://dzone.com/articles/setting-up-a-docker-private-registry-with-authenti)
* [sonatype: how to delete docker images from Nexus Repository Manager](https://support.sonatype.com/hc/en-us/articles/360009696054-How-to-delete-docker-images-from-Nexus-Repository-Manager)
* [hackermoon.com: cleanup old docker images from nexus repository](https://hackernoon.com/cleanup-old-docker-images-from-nexus-repository-617b1004dad8)

#### Secure Docker Registries
* [guides.sonatype.com: secure docker registries](https://guides.sonatype.com/repo3/technical-guides/secure-docker-registries/)
* [support.sonatype.com: Using self signed certificates with Nexus Repository Manager and Docker Daemon](https://support.sonatype.com/hc/en-us/articles/217542177-Using-Self-Signed-Certificates-with-Nexus-Repository-Manager-and-Docker-Daemon)

### SSL/TLS Certificates
* [guides.sonatype.com: secure docker registries](https://guides.sonatype.com/repo3/technical-guides/secure-docker-registries/)
* [support.sonatype.com: SSL Certificate Guide](https://support.sonatype.com/hc/en-us/articles/213465768-SSL-Certificate-Guide)
* [help.sonatype.com: Inbound SSL - Configuring to Serve Content via HTTPS](https://help.sonatype.com/repomanager3/security/configuring-ssl?_ga=2.250230211.411976214.1575978022-1513910029.1575978022#ConfiguringSSL-InboundSSL-ConfiguringtoServeContentviaHTTPS)
* [nginx.com: Using Free Let’s Encrypt SSL/TLS Certificates with NGINX](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/)

#### Add Insecure Registry to Docker
- [Test an insecure registry 🌟](https://docs.docker.com/registry/insecure/)
- [Configure Docker Service To Use Insecure Registry](https://github.com/Juniper/contrail-docker/wiki/Configure-docker-service-to-use-insecure-registry)
- [Running an insecure registry –insecure-registry](https://forums.docker.com/t/running-an-insecure-registry-insecure-registry/8159)
- [Add Insecure Registry to Docker](https://intellipaat.com/community/19079/add-insecure-registry-to-docker)

### Jenkins Integration with Nexus
* [Nexus Platform Plugin for Jenkins](https://help.sonatype.com/integrations/nexus-and-continuous-integration/nexus-platform-plugin-for-jenkins)
* [Jenkins: Publish Maven Artifacts to Nexus OSS Using Pipelines or Maven Jobs 🌟](https://dzone.com/articles/jenkins-publish-maven-artifacts-to-nexus-oss-using) Check out how following this tutorial to connect Maven and Nexus OSS can help increase your CI/CD pipelines.
* [Continuous Delivery with Sonatype Nexus, Jenkins and the Cloudogu Ecosystem](https://cloudogu.com/en/blog/cd-with-nexus-jenkins-ces)
* [youtube: Jenkins Integration with Nexus](https://www.youtube.com/watch?v=qbO4MTESiJQ)
* [youtube: uploading artifacts from jenkins to nexus](https://www.youtube.com/watch?v=7NmGSnqLd58)

### Nexus 3 Configuration as Code
* [github.com/samrocketman/nexus3-config-as-code](https://github.com/samrocketman/nexus3-config-as-code) 
* [blog.mimacom.com/automate-nexus](https://blog.mimacom.com/automate-nexus/) 
* [github.com/cinhtau/sonatype-nexus-waffle](https://github.com/cinhtau/sonatype-nexus-waffle) 

### Nexus CLI
* [GitHub: Nexus-CLI](https://github.com/mlabouardy/nexus-cli)
* [nexus3-cli.readthedocs.io](https://nexus3-cli.readthedocs.io)

### Sonatype Nexus Community
* [Sonatype Nexus Community 🌟](https://github.com/sonatype-nexus-community)
* Check out the [Nexus3](https://stackoverflow.com/questions/tagged/nexus3) tag on Stack Overflow

## JFrog Artifactory
- [JFrog Artifactory: Your Kubernetes Registry](https://jfrog.com/blog/jfrog-artifactory-kubernetes-registry/)
- [The JFrog journey to kubernetes: best practices for taking your containers all the way to production](https://jfrog.com/whitepaper/the-jfrog-journey-to-kubernetes-best-practices-for-taking-your-containers-all-the-way-to-production/)