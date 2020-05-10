# Awesome Kubernetes: CI/CD for Microservices with OpenShift and Jenkins (Software Delivery Pipeline) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<img alt="Container with cars" src="images/container_with_cars.png"> 
<head>
<meta property="og:image" content="https://awesome-kubernetes.readthedocs.io/images/container_with_cars.png">
</head>
A curated list of awesome references collected since 2018.
Microservices architectures rely on DevOps practices, automation, CI/CD (continuous integration and delivery), and API—focused designs.

"I do not believe you can do today's job with yesterday's methods and be in business tomorrow." ([Horatio Nelson Jackson](https://www.history.com/news/the-first-great-american-road-trip))
<center>

|[![openshift videos](images/docker_kubernetes_openshift.png)](https://www.youtube.com/user/rhopenshift)|[![jenkins videos](images/jenkins-logo.png)](https://www.youtube.com/user/CloudBeesTV)|
|:---:|:---:|

</center>
<div id="player"></div>

## Table of Contents

1. [Introduction. Openshift VS Kubernetes](introduction.md)
    - [microservices.io](https://microservices.io/)
    - [landscape.cncf.io](https://landscape.cncf.io/)
        - [Certified Kubernetes offerings](https://www.cncf.io/certification/software-conformance/)
    - [agilemethodology.org](http://agilemethodology.org/)
    - [agilemanifesto.org](http://agilemanifesto.org/)
    - [12factor.net](https://12factor.net/)
    - [roadmap.sh](https://roadmap.sh/) 
    - [API Landscape](https://www.apidays.co/api-landscape)
    - [From Java EE To Cloud Native](javaee-to-cloud-native.md)
    - [Microservices FAQ & Kubernetes Native](faq.md)
2. [DevOps](devops.md)
3. [CI/CD - Continuous Integration & Continuous Delivery](cicd.md)
    - [Git & Git Patterns. Git Flow & Trunk. CI/CD BOTs 🌟](git.md)
4. [TestOps](testops.md)
5. [Docker](docker.md)
6. [Kubernetes 🌟🌟🌟](kubernetes.md)
    - [Kubernetes Matrix Table](matrix-table.md)
    - [Kubernetes Alternatives](kubernetes-alternatives.md)
7. [Openshift 🌟🌟🌟](openshift.md)
    - [Monitoring and Performance 🌟](monitoring.md)
    - [Java Performance Optimization](java-and-java-performance-optimization.md)
        - [Java Parameters Matrix Table 🌟](jvm-parameters-matrix-table.md)
    - [Red Hat Developer @Youtube](https://www.youtube.com/channel/UC7noUdfWp-ukXUlAsJnSm-Q)
8. [Jenkins & CloudBees 😀 🌟🌟🌟](jenkins.md)
    - [Performance testing with Jenkins and JMeter or Gatling](performance-testing-with-jenkins-and-jmeter.md)
    - [OpenShift Pipelines with Jenkins, Tekton and more... 🌟](openshift-pipelines.md)
    - [Groovy](groovy.md)
    - [Jenkins Scripts](scripts/README.md)
    - [Jenkins Alternatives for Continuous Integration](jenkins-alternatives.md)
9.  Toolchain
    - [Maven](maven.md)
    - [Gradle](gradle.md)
    - [Podman & Buildah](podman.md)
    - [SonarQube](sonarqube.md)
    - [Nexus](nexus.md)
    - [JFrog Artifactory](artifactory.md)
    - [Apache](apache.md)
    - [HAProxy](haproxy.md)
    - [Payara](payara.md)
    - [Undertow](http://undertow.io/)
    - [Zephyr (Jira plugin)](zephyr.md)
    - [Selenium](selenium.md)
    - [Appium](appium.md)
    - [SSH](ssh.md)
    - [OpenProject](https://www.openproject.org/)
    - [Work From Home](workfromhome.md)
    - [Appointment Scheduling](appointment-scheduling.md)
10. Configuration Management
    - [Terraform & Packer](terraform.md)
    - [Ansible](ansible.md)
    - [Liquibase](liquibase.md)
11. Databases on Kubernetes
    - [Relational Databases](databases.md)
    - [NoSQL Databases](nosql.md)
12. [Streaming & Messaging. Cloud Based Integration 🌟](message-queue.md) 
13. [Caching Solutions](caching.md)
14. [Service Mesh](servicemesh.md)
    - [Consul](consul.md)
    - [Envoy & xDS protocol](envoyproxy.md)
    - [Istio](istio.md)
    - [Linkerd](linkerd.md)
    - [Maesh](maesh.md)
    - [Traffic Director](trafficdirector.md)
15. [Security Policy as Code](securityascode.md)
16. [Cloud Native Storage](storage.md)
17. [APIs with SOAP, REST and gRPC 🌟](api.md)
    - [Swagger code generator for REST APIs](swagger-code-generator-for-rest-apis.md)
    - [Test Automation with Postman](postman.md)
    - [API Marketplaces and Developer Portals🌟](developerportals.md)
        - [3scale API Management](3scale.md)
18. Frameworks
    - [Angular](angular.md)
    - [Java - Spring Framework](SpringFramework.md)
    - [Java - SpringBoot](SpringBoot.md)
    - [Java - Spring Cloud](SpringCloud.md)
    - [Java - Jakarta EE](https://jakarta.ee/)
    - [Java - Quarkus](quarkus.md)
    - [JavaScript - node.js & npm](javascript.md)
    - [Python - Django & Flask](python.md)
    - [Xamarin](xamarin.md)
19. [Serverless Architectures & Frameworks. OpenFaaS, Knative & Kubeless](serverless.md)
20. Dev Environment    
    - [Visual Studio Code 🌟](visual-studio.md)
    - [GitKraken](gitkraken.md)
    - [Atlassian Sourcetree](https://www.sourcetreeapp.com/)
    - [WSL: Linux Dev Environment on Windows](linux-dev-env.md)
    - [Scaffolding Tools](scaffolding.md)
21. [Demos](demos.md)
22. Public Cloud
    - [Public Cloud Solutions](public-cloud-solutions.md)
    - [Edge Computing](edge-computing.md)
    - [Cloud Architecture Diagram Tools](cloud-arch-diagrams.md)
    - [AWS](aws.md)
    - [Google Cloud Platform](GoogleCloudPlatform.md)
    - [Microsoft Azure](azure.md)
    - [Oracle Cloud](oraclecloud.md)
    - [Digital Ocean](digitalocean.md)
    - [Cloudflare](cloudflare.md)
23. [E-Learning](elearning.md)
24. [Customer Success Stories 🌟](customer.md)
25. [Subreddits and Newsfeeds](newsfeeds.md)
26. [Other Awesome Lists 🌟🌟🌟](other-awesome-lists.md)

<!-- El fin de la memoria? Documental 
<center>
    
<div class="container">
<iframe src="https://www.youtube.com/embed/tentcmxz3Bo?start=633&end=654" frameborder="0" allowfullscreen class="video"></iframe>	
</div>
</br>
-->
<center>
[![automated_ansible](images/automated_ansible.jpg)](https://www.ansible.com/blog/migrating-the-runbook-a-journey-from-legacy-to-devops)
</center>
