# awesome-2018: Jenkins CI/CD on Openshift Kubernetes
A curated list of awesome references collected in 2018

# Table of Contents
<!-- TOC -->

- [awesome-2018: Jenkins CI/CD on Openshift Kubernetes](#awesome-2018-jenkins-cicd-on-openshift-kubernetes)
- [Table of Contents](#table-of-contents)
- [CI/CD](#cicd)
- [Jenkins](#jenkins)
    - [Performance Testing with Jenkins and JMeter](#performance-testing-with-jenkins-and-jmeter)
    - [Jenkins and Openshift](#jenkins-and-openshift)
- [Kubernetes](#kubernetes)
    - [Docker](#docker)
    - [Openshift Kubernetes](#openshift-kubernetes)
    - [Java and Java Performance Optimization](#java-and-java-performance-optimization)
    - [Debugging java applications on openshift and kubernetes](#debugging-java-applications-on-openshift-and-kubernetes)
    - [Troubleshooting openshift network performance](#troubleshooting-openshift-network-performance)
- [SonarQube](#sonarqube)
- [Nexus](#nexus)
- [Maven](#maven)
- [Git](#git)
- [Visual Studio](#visual-studio)
- [Terraform](#terraform)
- [Ansible](#ansible)
- [Groovy](#groovy)
- [APIs and RESTful Architecture](#apis-and-restful-architecture)
    - [Swagger code generator for REST APIs](#swagger-code-generator-for-rest-apis)

<!-- /TOC -->

# CI/CD
* [opensource.com: What is CI/CD?](https://opensource.com/article/18/8/what-cicd)
* [Awesome Continuous Integration and Continuous Delivery](https://github.com/ciandcd/awesome-ciandcd)
* [DZone: Continuous Integration: Servers and Tools](https://dzone.com/refcardz/continuous-integration-servers) Learning to Utilize DevOps with Servers and Tools

# Jenkins
* [Jenkins.io (new Jenkins 2.0 site)](https://jenkins.io/)
* [jenkins.io: Jenkins CD and Pipelines Microsite](https://jenkins.io/solutions/pipeline/)
* [dzone.com: Jenkins Pipeline - Software Delivery Made Easy](https://dzone.com/articles/jenkins-pipeline-software-delivery-made-easy) Jenkins 2.0 has focused on solving the problem for organizations wanting to continuously deliver software.
* [dzone.com: Jenkins Configuration as Code: Need for Speed! 🌟🌟🌟🌟](https://dzone.com/articles/jenkins-configuration-as-code-need-for-speed)
    * https://github.com/jenkinsci/configuration-as-code-plugin
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟🌟🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [dzone.com: How to Set Up Scalable Jenkins on Top of a Kubernetes Cluster 🌟🌟🌟](https://dzone.com/articles/how-to-setup-scalable-jenkins-on-top-of-a-kubernet)
* [devops.com: Kubernetes Jenkins Master-Slave: Scaling the Scalability Issue](https://devops.com/kubernetes-jenkins-master-slave-scaling-the-scalability-issue/)
* [udemy.com: Master Jenkins CI For DevOps and Developers](https://www.udemy.com/the-complete-jenkins-course-for-developers-and-devops/)
* [udemy.com: Learn DevOps: CI/CD with Jenkins using Pipelines and Docker](https://www.udemy.com/learn-devops-ci-cd-with-jenkins-using-pipelines-and-docker/) Use Jenkins the DevOps way. Automate your Jenkins jobs by using Jenkins Pipelines, Docker, and the Jenkins Job DSL
* [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins)
* [Official Jenkins Docker image](https://github.com/michaelneale/jenkins-ci.org-docker)
* https://github.com/jenkinsci
* https://github.com/jenkinsci/performance-plugin
* https://github.com/geerlingguy/ansible-role-jenkins
* https://github.com/sahilsk/awesome-jenkins
* https://www.reddit.com/r/jenkinsci 🌟🌟
* https://jenkins.io/doc/book/pipeline/jenkinsfile/ 🌟
* [DZone refcard: declarative pipeline with jenkins 🌟🌟](https://dzone.com/refcardz/declarative-pipeline-with-jenkins)
* [Dzone refcard: Continuous Delivery with Jenkins Workflow](https://dzone.com/refcardz/continuous-delivery-with-jenkins-workflow)
* [Dzone refcard: Jenkins on PaaS](https://dzone.com/asset/download/230) Continuous Integration with Jenkins for Java Projects. Includes a review of the most useful plugins, best practices, security, integration to an enterprise environment, and more.
* [7 Ways to Optimize Jenkins](https://www.sitepoint.com/7-ways-optimize-jenkins/)
* [Dzone: Top 10 Best Practices for Jenkins Pipeline](https://dzone.com/articles/top-10-best-practices-for-jenkins-pipeline)
* [opensource.com: Running Jenkins builds in Openshift containers](https://opensource.com/article/18/4/running-jenkins-builds-containers)

## Performance Testing with Jenkins and JMeter
* https://github.com/jenkinsci/performance-plugin
* https://www.blazemeter.com/blog/continuous-integration-101-how-run-jmeter-jenkins 🌟
* https://www.baeldung.com/jenkins-and-jmeter
* https://dzone.com/articles/2-ways-to-integrate-jmeter-tests-into-jenkins
* https://www.guru99.com/jenkins-jmeter-blazemeter.html

## Jenkins and Openshift
* [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟🌟](https://blog.openshift.com/building-declarative-pipelines-openshift-dsl-plugin/)
* [slideshare.net: CI/CD with Openshift and Jenkins 🌟🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins)
* [slideshare.net: OPENSHIFT CONTAINER PLATFORM CI/CD Build & Deploy  🌟🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy)

# Kubernetes
* [youtube: Kubernetes in 5 mins](https://www.youtube.com/watch?v=PH-2FfFD2PU)
* [developers.redhat.com: Why Kubernetes is The New Application Server](https://developers.redhat.com/blog/2018/06/28/why-kubernetes-is-the-new-application-server/)
* [Awesome kubernetes 🌟🌟🌟🌟](https://github.com/ramitsurana/awesome-kubernetes)
* [stackify.com: The Advantages of Using Kubernetes and Docker Together 🌟🌟🌟](https://stackify.com/kubernetes-docker-deployments/)
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
* https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* [developers.redhat.com: Kubernetes Cheat Sheet 🌟](https://developers.redhat.com/cheat-sheets/kubernetes/)
* [Local Install Option 1: Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
* [Local Install Option 2: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [Production Cluster Install Option 3: Kubernetes Cluster with Kops:](https://github.com/kubernetes/kops) 
    * Minikube and docker client are great for local setups, but not for real clusters. Kops and kubeadm are tools to spin up a production cluster. You don't need both tools, just one of them. 
    * On AWS, the best tool is **kops**
    * At some point AWS EKS (hosted kubernetes) will be available, at that point this will probably be the preferred option. (You won't need to maintain the masters).
    * For other installs, or if you can't get kops to work, you can use kubeadm
    * **kubeadm** is an alternative approach, kops is still recommended (on AWS) - you also have AWS integrations with kops automatically
    * Setup **kops** in your windows with **virtualbox.org** and **vagrantup.com** . Once downloaded, to type a new linux VM, just type in cmd/powershell:
    1) Spin up ubuntu via vagrant:
    ```
        C:\ubuntu> vagrant init ubuntu/xenial64
        C:\ubuntu> vagrant up
        [...]
        C:\ubuntu> vagrant ssh-config    
        C:\ubuntu> vagrant ssh
    ```
    2) Runt kops installer:
    ```
        curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
        chmod +x kops-linux-amd64
        sudo mv kops-linux-amd64 /usr/local/bin/kops
    ```
* [Production Cluster Install Option 4: Kubernetes Cluster with Kubeadm](https://github.com/kubernetes/kubeadm) It works on any deb / rpm compatible Linux OS, for example Ubuntu, Debian, RedHat or CentOS. This is the main advantage of kubeadm. The tool itself is still in beta (Q1 2018), but is expected to become stable somewhere this year. It's very easy to use and lets you spin kubernetes cluster in just a couple of minutes.

## Docker
* [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
* [Dzone refcard: Getting Started with Docker](https://dzone.com/refcardz/getting-started-with-docker-1)
* [Dzone refcard: Java Containerization 🌟](https://dzone.com/refcardz/java-containerization)
* [developers.redhat.com: Containers Cheat Sheet](https://developers.redhat.com/cheat-sheets/containers/)
* [americanexpress.io: **Do Not Run Dockerized Applications as Root** 🌟🌟🌟](https://americanexpress.io/do-not-run-dockerized-applications-as-root/)

## Openshift Kubernetes
* [docs.openshift.com](https://docs.openshift.com/)
* [Openshift Awesome 🌟](https://github.com/dudash/openshift-is-awesome)
* [Openshift Awesome List 2](https://github.com/oscp/awesome-openshift3)
* [Dzone: OpenShift Quick Start 🌟🌟](https://dzone.com/articles/openshift-quick-start)
* [blog.openshift.com: Installing OKD 3.10 on a Single Host 🌟🌟🌟🌟](https://blog.openshift.com/installing-okd-3-10-on-a-single-host/)
    * [youtube.com: OpenShift Origin is now OKD. Installation of OKD 3.10 from start to finish](https://www.youtube.com/watch?v=ZkFIozGY0IA)
    * [Install RedHat OKD 3.10 on your development box:](https://github.com/gshipley/installcentos) This repository is a set of scripts that will allow you easily install the latest version (3.10) of OKD in a single node fashion. What that means is that all of the services required for OKD to function (master, node, etcd, etc.) will all be installed on a single host. The script supports a custom hostname which you can provide using the interactive mode.]
    * A few other options to use OKD locally include [oc cluster up](https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md) and [minishift](https://www.okd.io/minishift/). These may be a better fit for your use case if you only need a quick throwaway environment.
* [developers.redhat.com: **Red Hat Container Development Kit** 🌟🌟🌟](https://developers.redhat.com/products/cdk/overview/)
* [udemy.com: Red Hat OpenShift With Jenkins: DevOps For Beginners 🌟🌟🌟🌟](https://www.udemy.com/red-hat-openshift)
* [blog.openshift.com: Introducing Red Hat Quay 🌟](https://blog.openshift.com/introducing-red-hat-quay/)
* [redhat.com: **How to gather and display metrics in Red Hat OpenShift** (Prometheus + Grafana)](https://www.redhat.com/en/blog/how-gather-and-display-metrics-red-hat-openshift)
* [claydesk.com: Google Cloud App Engine Vs Red Hat OpenShift](https://www.claydesk.com/ecampus/google-cloud-app-engine-vs-red-hat/)
* https://github.com/fabric8io/fabric8-pipeline-library
* https://fabric8.io/
* https://twitter.com/openshift 🌟
* [developers.redhat.com: Source versus binary S2I workflows with Red Hat OpenShift Application Runtimes](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes/)
* [O'Reilly Free Book: DevOps with OpenShift 🌟🌟🌟](https://www.openshift.com/devops-with-openshift/)
* [developers.redhat.com: Red Hat OpenShift Container Platform Cheat Sheet](https://developers.redhat.com/cheat-sheets/red-hat-openshift-container-platform/)
* [github.com: Openshift cheat sheet 1](https://github.com/nekop/openshift-sandbox/blob/master/docs/command-cheatsheet.md)
* [gist.github.com: Openshift cheat sheet 2](https://gist.github.com/rafaeltuelho/111850b0db31106a4d12a186e1fbc53e)
* [github.com: openshift cheat sheet 3](https://github.com/mhausenblas/openshift-cheat-sheet)
* [monodot.co.uk: openshift cheat sheet 4](https://monodot.co.uk/openshift-cheatsheet/)
* [Red Hat Consulting DevOps And OpenShift Playbooks 🌟🌟🌟](http://v1.uncontained.io/) Red Hat Consulting DevOps and OpenShift Playbooks are guides for implementing DevOps technical practices and container automation approaches using Red Hat commercial open source products, including OpenShift Enterprise 3. They are intended to reflect real-world experience delivering solutions through these processes and technologies.

## Java and Java Performance Optimization
* [Dzone refcard: Java Peformance Optimization](https://dzone.com/refcardz/java-performance-optimization)
* [Monitorización y análisis de rendimiento de aplicaciones con Dynatrace APM](https://www.adictosaltrabajo.com/tutoriales/monitorizacion-y-analisis-de-rendimiento-de-aplicaciones-con-dynatrace/)
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟🌟🌟🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [blog.openshift.com: Scaling Java Containers 🌟🌟🌟🌟](https://blog.openshift.com/scaling-java-containers/)
* [blog.openshift.com: Performance Metrics (APM) for Spring Boot Microservices on OpenShift](https://blog.openshift.com/performance-metrics-apm-spring-boot-microservices-openshift/)
* [dzone.com: Java RAM Usage in Containers: Top 5 Tips for Not Losing Your Memory](https://dzone.com/articles/java-ram-usage-in-containers-top-5-tips-not-to-los)
* [dzone.com: Running a JVM in a Container Without Getting Killed:](https://dzone.com/articles/running-a-jvm-in-a-container-without-getting-kille) Starting in JDK 9, and earlier if you use JDK 8u131, your JVM can detect how much memory is available when running inside a Docker container.
* [dzone.com: Java Inside Docker: What You Must Know to Not FAIL](https://dzone.com/articles/java-inside-docker-what-you-must-know-to-not-fail) If you've tried Java in containers, particularly Docker, you might have encountered some problems with the JVM and heap size. Here's how to fix it.
* [medium.com/@javachampions : Java is still free](https://itnext.io/java-is-still-free-c02aef8c9e04)
* [Oracle Java 11 and OpenJDK](https://blog.joda.org/2018/09/do-not-fall-into-oracles-java-11-trap.html)
* [developers.redhat.com: The future of Java and OpenJDK updates without Oracle support](https://developers.redhat.com/blog/2018/09/24/the-future-of-java-and-openjdk-updates-without-oracle-support/)

## Debugging java applications on openshift and kubernetes
* [blog.openshift.com: Debugging Java Applications On OpenShift and Kubernetes](https://blog.openshift.com/debugging-java-applications-on-openshift-kubernetes/)

## Troubleshooting openshift network performance
* [blog.openshift.com: Troubleshooting OpenShift network performance with a netperf DaemonSet](https://blog.openshift.com/troubleshooting-openshift-network-performance-with-a-netperf-daemonset/)

# SonarQube
* https://www.sonarqube.org/
* https://dzone.com/articles/code-analysis-part-2-analyzing-code-with-sonarqube

# Nexus
* https://www.sonarqube.org/
* https://dzone.com/articles/code-analysis-part-2-analyzing-code-with-sonarqube

# Maven
* https://maven.apache.org/
* https://dzone.com/articles/starting-with-apache-maven
* https://dzone.com/articles/solving-dependency-conflicts-in-maven

# Git
* https://devdocs.io/git/
* https://git-scm.com/book
* [The awesome git cheat sheet](https://the-awesome-git-cheat-sheet.com/)
* [Git cheat sheet 🌟🌟](https://zeroturnaround.com/wp-content/uploads/2016/02/Git-Cheat-Sheet.png)
* [tutorialzine.com: Learn git in 30 minutes 🌟🌟](https://tutorialzine.com/2016/06/learn-git-in-30-minutes)
* [3 Git Commands I Use Every Day](https://dev.to/gonedark/3-git-commands-i-use-every-day)
* [Git and Github in Plain English](https://red-badger.com/blog/2016/11/29/gitgithub-in-plain-english)
* [opensource.com: How to restore older file versions in Git](https://opensource.com/life/16/7/how-restore-older-file-versions-git)
* [9 awesome git tricks](https://tychoish.com/post/9-awesome-git-tricks/)
* [Awesome Git 🌟](https://github.com/dictcp/awesome-git)
* [dzone.com: intro git 🌟](https://dzone.com/articles/intro-git)
* [dzone.com: refcard - getting started with git](https://dzone.com/refcardz/getting-started-git)
* [dzone.com: Top 20 git commands with examples 🌟](https://dzone.com/articles/top-20-git-commands-with-examples)
* [dzone.com: 8 Useful But Not Well-Known Git Concepts](https://dzone.com/articles/8-useful-but-not-well-known-git-concepts) These lesser-known Git tricks can help you solve problems that are not handled well by the GitHub and BitBucket GUIs
* [dzone.com: Git Commands Tutorial - Part 1](https://dzone.com/articles/git-commands-tutorial-part-1)
* [dzone.com: Git Commands Tutorial - Part 2](https://dzone.com/articles/git-commands-tutorial-part-2)
* [Dzone refcard: Getting started with Git](https://dzone.com/refcardz/getting-started-git)
* [Oh shit, git!](https://ohshitgit.com/)

# Visual Studio
* [Awesome Visual Studio Code](https://github.com/viatsko/awesome-vscode)

# Terraform
* https://www.terraform.io/
* https://github.com/shuaibiyy/awesome-terraform
* https://github.com/Azure/awesome-terraform
* https://github.com/ozbillwang/terraform-best-practices
* [medium.com: Why should Terraform be one of your DevOps tools?](https://medium.com/devopslinks/why-should-terraform-be-one-of-your-devops-tools-29ae15861b1f)
* [dzone: Terraform - IAC Tool](https://dzone.com/articles/terraform-iac-tool) See why Terraform's declarative approach to automation makes it a competitive tool for automating the creation of your infrastructure.
* [dzone: Manage Multiple Environments With Terraform Workspaces](https://dzone.com/articles/manage-multiple-environments-with-terraform-worksp) Read this tutorial to learn about easily setting up Terraform to manage your CI/CD environments and create workspaces.
* [udemy.com: Learn DevOps: Infrastructure Automation With Terraform](https://www.udemy.com/learn-devops-infrastructure-automation-with-terraform/)

# Ansible
* https://github.com/jdauphant/awesome-ansible
* https://github.com/awesome-devops/awesome-ansible
* [Dzone: Ansible: An Effective IT Automation Tool](https://dzone.com/articles/ansible-an-effective-it-automation-tool) Learn about Ansible, a tool for automating application deployments, configuration management, and more in a DevOps environment.
* [Dzone: Getting Started With Ansible](https://dzone.com/articles/getting-started-with-ansible)
* [Dzone: Part 1: Getting Started with Ansible](https://dzone.com/articles/part-1-getting-started-ansible)
* [Dzone: Running Ansible at Scale](https://dzone.com/articles/running-ansible-at-scale)
* [Dzone: Running Ansible Playbooks From Jenkins](https://dzone.com/articles/running-ansible-playbooks-from-jenkins)
* [Udemy.com: Ansible Essentials: Simplicity in Automation](https://www.udemy.com/ansible-essentials-simplicity-in-automation)

# Groovy
* [Dzone: Introduction to Groovy](https://dzone.com/articles/introduction-groovy)
* [Dzone refcard: Groovy, a Rapid-Development JVM Language](https://dzone.com/refcardz/groovy)

# APIs and RESTful Architecture
* API Documentation: https://devdocs.io/
* [Dzone refcard: Foundations of RESTful Architecture 🌟🌟](https://dzone.com/refcardz/rest-foundations-restful)

## Swagger code generator for REST APIs
* https://swagger.io/
* https://github.com/swagger-api/swagger-codegen
* [Dzone: API First Approach and API Management With Swagger](https://dzone.com/articles/api-first-approach-and-api-management-with-swagger) Looking for a new API management tool? Read on to see how one team faired while using Swagger's suite of API development tools.
* [youtube.com: SwaggerHub 101 An Introduction to Getting Started with SwaggerHub](https://www.youtube.com/watch?v=CoUl9_NWdqQ)
* [youtube.com: Building an API with Swagger](https://www.youtube.com/watch?v=PbwQWw7xSOM)
