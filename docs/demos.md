# DevOps Demos, Tutorials & Screencasts
- [DevOps Screencasts](#devops-screencasts)
- [DevOps Blogs](#devops-blogs)
- [Kubernetes Blogs](#kubernetes-blogs)
- [DevOps Demos](#devops-demos)
    - [Container Tools](#container-tools)
    - [Ansible and Ansible Tower](#ansible-and-ansible-tower)
    - [GitOps](#gitops)
- [Kubernetes Demos](#kubernetes-demos)
    - [Postgres Operator](#postgres-operator)
    - [CI/CD with SpringBoot for Kubernetes](#cicd-with-springboot-for-kubernetes)
        - [Deploy a Spring Boot Application to Openshift with Spring Cloud Kubernetes and Fabric 8 Maven Plugin](#deploy-a-spring-boot-application-to-openshift-with-spring-cloud-kubernetes-and-fabric-8-maven-plugin)
        - [Spring Initializr and k8s Initializer](#spring-initializr-and-k8s-initializer)
    - [Kubernetes CKAD Example Exam Questions Practical Challenge Series](#kubernetes-ckad-example-exam-questions-practical-challenge-series)
    - [Istio Service Mesh](#istio-service-mesh)
    - [Envoy Service Mesh](#envoy-service-mesh)
    - [Consul Service Mesh](#consul-service-mesh)
    - [Rancher](#rancher)
    - [GitOps Workflow with Flux](#gitops-workflow-with-flux)
    - [Amazon EKS. Deploy example microservices on EKS](#amazon-eks-deploy-example-microservices-on-eks)
    - [Azure AKS](#azure-aks)
    - [Google Kubernetes Engine GKE](#google-kubernetes-engine-gke)
    - [Environments to learn and practice Kubernetes security](#environments-to-learn-and-practice-kubernetes-security)
- [Red Hat Demo Central](#red-hat-demo-central)
    - [Cloud Native Development Architectural Diagrams Demos](#cloud-native-development-architectural-diagrams-demos)
- [OpenShift Demos](#openshift-demos)
    - [Developer Sandbox](#developer-sandbox)
    - [OpenShift VS Kubernetes](#openshift-vs-kubernetes)
    - [IBM Cloud Pak Playbooks](#ibm-cloud-pak-playbooks)
    - [Knative](#knative)
    - [OpenShift Pipelines Workshop (Tekton)](#openshift-pipelines-workshop-tekton)
    - [ArgoCD](#argocd)
    - [GitLab Pipelines on OpenShift](#gitlab-pipelines-on-openshift)
    - [Deploying Web Applications with Eclipse JKube (formerly known as fabric8)](#deploying-web-applications-with-eclipse-jkube-formerly-known-as-fabric8)
    - [Monitoring Services with OpenShift ServiceMesh](#monitoring-services-with-openshift-servicemesh)
    - [Red Hat Migration Toolkit for Applications](#red-hat-migration-toolkit-for-applications)
    - [Red Hat Advanced Cluster Management RHACM](#red-hat-advanced-cluster-management-rhacm)
    - [OKD](#okd)
    - [Helm 3 on OpenShift](#helm-3-on-openshift)
    - [Writing Kubernetes Operators](#writing-kubernetes-operators)
    - [Customized Reports with Metering Operator (monitoring k8s resources)](#customized-reports-with-metering-operator-monitoring-k8s-resources)
    - [Red Hat AMQ Streams (Kafka)](#red-hat-amq-streams-kafka)
- [Jenkins Demos](#jenkins-demos)
    - [Jenkins Declarative Pipelines with OpenShift](#jenkins-declarative-pipelines-with-openshift)
    - [OpenShift Pipelines with S2i and Jenkins Blue Ocean](#openshift-pipelines-with-s2i-and-jenkins-blue-ocean)
    - [Jenkins Configuration as Code on Kubernetes](#jenkins-configuration-as-code-on-kubernetes)
    - [From Jenkins Freestyle jobs to Pipeline, with JobDSL. Seed jobs](#from-jenkins-freestyle-jobs-to-pipeline-with-jobdsl-seed-jobs)
    - [SDKMAN](#sdkman)
    - [Jenkins Scripts](#jenkins-scripts)
    - [Postman & Newman API Automated Tests](#postman--newman-api-automated-tests)
    - [Monitoring Jenkins with Grafana](#monitoring-jenkins-with-grafana)
- [Jenkins X](#jenkins-x)
- [Spinnaker](#spinnaker)
- [Nexus3 on Kubernetes](#nexus3-on-kubernetes)
- [GitLab](#gitlab)
- [Spring PetClinic Sample Application](#spring-petclinic-sample-application)
    - [Modular Pipeline Library (MPL). Petclinic Pipeline example with MPL](#modular-pipeline-library-mpl-petclinic-pipeline-example-with-mpl)
    - [PetClinic on Kubernetes:](#petclinic-on-kubernetes)
    - [PetClinic Docker images:](#petclinic-docker-images)
    - [OpenShift.io Samples](#openshiftio-samples)
- [AWS Demos](#aws-demos)
- [Azure DevOps Demos](#azure-devops-demos)
- [Google DevOps Demos](#google-devops-demos)
    - [GitOps with Anthos Config Management](#gitops-with-anthos-config-management)
- [Quarkus Demos](#quarkus-demos)
- [Kafka](#kafka)
- [Apache Camel & ActiveMQ. Event driven integration](#apache-camel--activemq-event-driven-integration)
- [Codeless](#codeless)
- [JBoss EAP](#jboss-eap)
- [Terraform](#terraform)
- [Prometheus and Grafana](#prometheus-and-grafana)
- [GitHub Actions](#github-actions)
    - [RedHat GitHub Actions](#redhat-github-actions)
- [Red Hat Process Automation Manager](#red-hat-process-automation-manager)
- [API Testing and Postman](#api-testing-and-postman)
- [Serverless](#serverless)

## DevOps Screencasts
- [SysAdmin Casts 🌟](https://sysadmincasts.com/) 
- [DEVOPS Library 🌟](https://devopslibrary.com/)

## DevOps Blogs
- [DevStack](https://devstack.in/) All about DevOps

## Kubernetes Blogs
- [kubernetes-advocate.medium.com 🌟](https://kubernetes-advocate.medium.com/)

## DevOps Demos
* [RedHatGov.io](http://redhatgov.io) is an open source collection of workshop materials that cover various topics relating to Red Hat's product portfolio.
* [github.com/wardviaene (kubernetes, terraform, ansible, docker, etc) 🌟](https://github.com/wardviaene)
    * [wardviaene/jenkins-course](https://github.com/wardviaene/jenkins-course)
    * [wardviaene/kubernetes-course](https://github.com/wardviaene/kubernetes-course)
* [thoughtworks.com: Modernizing your build pipelines with **Concourse CI** 🌟](https://www.thoughtworks.com/es/insights/blog/modernizing-your-build-pipelines)
    * [github.com/sirech/example-concourse-pipeline](https://github.com/sirech/example-concourse-pipeline)
* [yankils/Simple-DevOps-Project](https://github.com/yankils/Simple-DevOps-Project) 
* [Spring PetClinic Sample Application](#spring-petclinic-sample-application) By following this repository you can able to setup a DevOps CI/CD Pipeline using: git, Jenkins, Maven, Ansible, Docker & Kubernetes
* [swissarmydevops.com](https://swissarmydevops.com/) 
* [dev.to: Build a highly available Node.js application using Docker, NGINX and AWS ELB](https://dev.to/sowmenappd/build-a-highly-available-node-js-application-using-docker-nginx-and-aws-elb-3cjp)
* [towardsdatascience.com: Developing and Deploying a COMPLETE Project Using FastAPI, Jinja2, SQLAlchemy, Docker, and AWS](https://towardsdatascience.com/developing-and-deploying-a-complete-project-using-fastapi-jinja2-sqlalchemy-docker-and-aws-1b504a1a2be4)

### Container Tools
- [dzone Avengers of the Container World, Episode 1: Podman Hands-On 🌟](https://dzone.com/articles/avengers-of-container-world-episode-1-podman-hands) CRI-O and Podman have been widely adapted by most of the modern container platforms. In this blog, we will deep-dive on Podman with a hands-on session.
- [dzone: Avengers of Container World, Episode 2: Buildah and Skopeo Hands-On 🌟](https://dzone.com/articles/avengers-of-container-world-episode-2-buildah-amp) In this post, we will explore Buildah and Skopeo, build a Node.js application container using Buildah, and run it using Podman

### Ansible and Ansible Tower
* [ansible.github.io/workshops/demos : Red Hat Ansible Automation Platform Workshops](https://ansible.github.io/workshops/demos/)
* [Red Hat Ansible Tower - Workshop and Demo](https://github.com/network-automation/tower_workshop)
* [blog.stephane-robert.info: Ansible - Utiliser MySQL comme inventaire dynamique (Use MySQL as a dynamic inventory)](https://blog.stephane-robert.info/post/ansible-utiliser-mysql-comme-inventaire-dynamique/)
* [opensource.com: Build a Kubernetes Minecraft server with Ansible's Helm modules](https://opensource.com/article/20/10/kubernetes-minecraft-ansible) Deploy a Minecraft server into a Kubernetes cluster with Ansible's new collections.
* [developers.redhat.com: Run your first Ansible Playbook (Katakoda)](https://developers.redhat.com/courses/ansible/getting-started)
* [kubernetes-advocate.medium.com: Website Deployment to AWS with Ansible](https://kubernetes-advocate.medium.com/how-to-deploy-a-website-to-aws-with-ansible-e878a63dd93)
* [konstruktoid.medium.com: Running a NGINX container using rootless Docker with Ansible](https://konstruktoid.medium.com/running-a-nginx-container-using-rootless-docker-with-ansible-a2bfcedd3b07)
* [kmahi2600.medium.com: Launching A WordPress Application With MYSQL Database in K8S Cluster On AWS Using Ansible](https://kmahi2600.medium.com/launching-a-wordpress-application-with-mysql-database-in-k8s-cluster-on-aws-using-ansible-a78d6bf12b1a)
* [faun.pub: Automation: Deploying an app in GKE using Ansible](https://faun.pub/automation-deploying-an-app-in-gke-using-ansible-4b6687967ac3) Ansible infrastructure-as-code to automate Nginx deployment in Google Kubernetes Cluster (GKE) on Google Cloud Platform (GCP).

### GitOps 
- [thenewstack.io: GitOps in Multicluster Environments with Anthos Config Management](https://thenewstack.io/tutorial-gitops-in-multicluster-environments-with-anthos-config-management/)
- [kubesandclouds.com: Werf: Fully customizable GitOps 🌟](https://kubesandclouds.com/index.php/2020/09/01/werf-gitops/) Werf builds and publishes images, deploys applications to Kubernetes clusters, and removes unused images based on policies and rules defined in the Git repository.
- [mytechramblings.com: A practical example of GitOps using Azure DevOps, Azure Container Registry, Helm, Flux and Kubernetes](https://www.mytechramblings.com/posts/gitops-with-azure-devops-helm-acr-flux-and-k8s/)

## Kubernetes Demos
* [kubernetesbyexample.com 🌟](http://kubernetesbyexample.com/)
* [github.com/eon01/kubernetes-workshop](https://github.com/eon01/kubernetes-workshop)
* [wardviaene/kubernetes-course](https://github.com/wardviaene/kubernetes-course)
* [github.com/kubernetes-course/container_workshops](https://github.com/kubernetes-course/container_workshops)
* [Mautic](https://github.com/mautic/docker-mautic)
* [howtoforge.com: How to create a Deployment in Kubernetes](https://www.howtoforge.com/create-a-deployment-in-kubernetes/)
* [codeburst.io: getting started with kubernetes, deploy a docker container in 5 minutes](https://codeburst.io/getting-started-with-kubernetes-deploy-a-docker-container-with-kubernetes-in-5-minutes-eb4be0e96370)
* [Kubernetes workshop in a box](https://www.theguild.nl/k8s-workshop-in-a-box/)
    * [GitHub: K8s workshop in a box](https://github.com/kabisa/k8s-workshop-in-a-box)
* [medium.com/@Kubernetes_Advocate 🌟](https://medium.com/@Kubernetes_Advocate)
    * [medium.com/avmconsulting-blog](https://medium.com/avmconsulting-blog)
* [medium: Efficient Node Out-of-Resource Management in Kubernetes](https://medium.com/kubernetes-tutorials/efficient-node-out-of-resource-management-in-kubernetes-67f158da6e59)
* [itnext.io: K8s raise StatefulSet volume size with low impact](https://itnext.io/k8s-raise-statefulset-volume-size-with-low-impact-33fe1e2576f6) Shown step-by-step on a simple example application
* [Kubernetes Examples](https://github.com/ianmiell/kubernetes-examples)
* [medium: Prometheus-Grafana on K8s](https://medium.com/@sdhah1999/prometheus-grafana-on-k8s-6efee4af4036)
* [blog.scottlowe.org: Using kubectl via an SSH Tunnel](https://blog.scottlowe.org/2020/06/16/using-kubectl-via-an-ssh-tunnel/) Learn how to use kubectl via an SSH Tunnel to connect to the Kubernetes API server.
* [trainings.kubernauts.sh](https://trainings.kubernauts.sh/) Learn Kubernetes by doing and run into problems!
* [magalix.com: How To Integrate OPA Into Your Kubernetes Cluster Using Kube-mgmt](https://www.magalix.com/blog/how-to-integrate-opa-into-your-kubernetes-cluster-using-kube-mgmt)
* [itnext.io: Kubernetes Journey — Up and running out of the cloud — How to setup the Masters using kubeadm bootstrap](https://itnext.io/kubernetes-journey-up-and-running-out-of-the-cloud-how-to-setup-the-masters-using-kubeadm-9a496a14fbc1)
* [medium: Build a Federation of Multiple Kubernetes Clusters With Kubefed V2](https://medium.com/better-programming/build-a-federation-of-multiple-kubernetes-clusters-with-kubefed-v2-8d2f7d9e198a)
* [medium: Single Sign-On in Kubernetes](https://medium.com/@andriisumko/single-sign-on-in-kubernetes-1ad9528350ed) This article walks you through creating a service, exposing it with an Ingress, and adding Single Sign On. The article uses Okta (but of course you’re free to use any other OIDC SSO provider you prefer)
* [Free Kubernetes 🌟🌟](https://github.com/learnk8s/free-kubernetes/) List of free Trials/Credit for Managed Kubernetes Services.
* [medium: Kubernetes in a nutshell — tutorial for beginners 🌟🌟](https://medium.com/swlh/kubernetes-in-a-nutshell-tutorial-for-beginners-caa442dfd6c0) Deploy a complete application stack just in a few steps!
* [shipa.io: Developing and deploying applications to Kubernetes locally with Shipa and Minikube](https://www.shipa.io/development/deploying-applications-on-kubernetes/)
* [shipa.io: GitOps in Kubernetes, the easy way–with GitHub Actions and Shipa](https://www.shipa.io/development/gitops/)
* [kruyt.org: Running a mailserver in Kubernetes](https://kruyt.org/running-a-mailserver-in-kubernetes/)
* [piotrminkowski.com: RabbitMQ Monitoring on Kubernetes](https://piotrminkowski.com/2020/09/29/rabbitmq-monitoring-on-kubernetes/?utm_sq=gl0f6vph5e)
* [dzone: Bootstrapping Java Kubernetes Apps With Spring Initializr and K8s Initializer 🌟](https://dzone.com/articles/bootstrapping-java-kubernetes-apps-no-yaml) Build a Spring Boot app and deploy to K8s without writing a single line of YAML.
* [medium: Production Ready CI/CD Pipeline with Kubernetes](https://medium.com/awsblogs/ci-cd-with-kubernetes-3c29e8073c38)
* [myweblearner.com: Kubernetes(k8s) Readiness and Liveness Probe](https://myweblearner.com/springboot_k8s_readiness_liveness.html)
* [medium.com: Attacking Kubernetes clusters using the Kubelet API](https://medium.com/faun/attacking-kubernetes-clusters-using-the-kubelet-api-abafc36126ca) Knock-knockin’ on kubelet’s door. From the doormat to full node access.
* [nfrankel/jvm-controller](https://github.com/nfrankel/jvm-controller) Example on how to write a kubernetes controller in Java. The demo code for nfrankel's talk on Kubernetes operators in Java.
* [matthewpalmer.net: Kubernetes Ingress with Nginx Example 🌟](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-ingress-guide-nginx-example.html)
* [digitalocean.com: How To Deploy a Scalable and Secure Django Application with Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-scalable-and-secure-django-application-with-kubernetes)
* [developers.redhat.com: Deploying Node.js applications to Kubernetes with Nodeshift and Minikube](https://developers.redhat.com/blog/2021/03/09/deploying-node-js-applications-to-kubernetes-with-nodeshift-and-minikube/)
* [itnext.io: Breaking down and fixing Kubernetes](https://itnext.io/breaking-down-and-fixing-kubernetes-4df2f22f87c3) In this article you'll break the cluster, delete certificates and rejoin the nodes without causing any downtime.

### Postgres Operator
- [blog.flant.com: Our experience with Postgres Operator for Kubernetes by Zalando](https://blog.flant.com/our-experience-with-postgres-operator-for-kubernetes-by-zalando/)

### CI/CD with SpringBoot for Kubernetes 
* [CI/CD for Kubernetes through a Spring Boot example (Banzai Cloud CI/CD)](https://teletype.in/@sravancynixit/CcwqFANxY)
* [onlineitguru.com: How to utilize Spring Boot Microservices on Kubernetes?](https://onlineitguru.com/blogger/how-to-utilize-spring-boot-microservices-on-kubernetes)
* [piotrminkowski.com: Spring Boot on Kubernetes with Buildpacks and Skaffold 🌟](https://piotrminkowski.com/2020/12/18/spring-boot-on-kubernetes-with-buildpacks-and-skaffold/)
* [spring.io: YMNNALFT: Easy Docker Image Creation with the Spring Boot Maven Plugin and Buildpacks](https://spring.io/blog/2021/01/04/ymnnalft-easy-docker-image-creation-with-the-spring-boot-maven-plugin-and-buildpacks)

#### Deploy a Spring Boot Application to Openshift with Spring Cloud Kubernetes and Fabric 8 Maven Plugin
* [github: Spring Cloud Kubernetes 🌟](https://github.com/spring-cloud/spring-cloud-kubernetes)
* [baeldung.com: Deploy a Spring Boot Application to OpenShift with Spring Cloud Kubernetes 🌟](https://www.baeldung.com/spring-boot-deploy-openshift)

#### Spring Initializr and k8s Initializer
- [Spring Initializr](https://start.spring.io/)
- [k8s Initializer](https://app.getambassador.io/initializer/)
- [dzone: Bootstrapping Java Kubernetes Apps With Spring Initializr and K8s Initializer](https://dzone.com/articles/bootstrapping-java-kubernetes-apps-no-yaml) Build a Spring Boot app and deploy to K8s without writing a single line of YAML
- [hashicorp.com: Getting Started with Ambassador and Consul Using Kubernetes Initializer](https://www.hashicorp.com/blog/getting-started-with-ambassador-and-consul-using-kubernetes-initializer) Kubernetes Initializer built by Ambassador Labs provides a new experience for simplifying the deployment of Ambassador and Consul in a Sandbox Kubernetes environment.

### Kubernetes CKAD Example Exam Questions Practical Challenge Series
* [Kubernetes CKAD Example Exam Questions Practical Challenge Series](https://codeburst.io/kubernetes-ckad-weekly-challenges-overview-and-tips-7282b36a2681)

### Istio Service Mesh
- [github: redhat-developer-demos Istio Tutorial for Java Microservices](https://github.com/redhat-developer-demos/istio-tutorial)
- [blog.jetstack.io: Istio OIDC Authentication](https://blog.jetstack.io/blog/istio-oidc/) In this article you'll deploy an app and secure it with authenticaiton and authorisation for using Istio

### Envoy Service Mesh
- [loginradius.com: Service Mesh with Envoy](https://www.loginradius.com/blog/async/service-mesh-with-envoy/) This post will cover a working setup of a service mesh architecture using Envoy using a demo application. You will be using Envoy proxy for both control and data plane.

### Consul Service Mesh
- [medium: Consul-Kubernetes Ingress Gateways and L7 Traffic Management](https://medium.com/hashicorp-engineering/consul-kubernetes-ingress-gateways-and-l7-traffic-management-178957dcd934)
    - [github: Andrew-Klaas/hashi-k8s-demo](https://github.com/Andrew-Klaas/hashi-k8s-demo)
- [medium: Kittens-as-a-Service: Layer 7 Traffic Management & Security with Consul Connect](https://medium.com/hashicorp-engineering/kittens-as-a-service-layer-7-traffic-management-security-with-consul-connect-f5965fac5aa)
- [learn.hashicorp.com: Consul Service Discovery and Mesh on Minikube 🌟](https://learn.hashicorp.com/tutorials/consul/kubernetes-minikube?in=consul/kubernetes)
- [consul.io: Ingress Gateways on Kubernetes 🌟](https://www.consul.io/docs/k8s/connect/ingress-gateways)

### Rancher
- [Deploy a Rancher Cluster with GitLab CI and Terraform](https://rancher.com/blog/2020/deploy-with-gitlab-ci)
- [cncf.io: Implementing GitOps on Kubernetes Using K3s, Rancher, Vault and Argo CD](https://www.cncf.io/blog/2020/11/12/implementing-gitops-on-kubernetes-using-k3s-rancher-vault-and-argo-cd/)
- [stackrox.com: Part 1 - Rancher Kubernetes Engine (RKE) Security Best Practices for Cluster Setup 🌟](https://www.stackrox.com/post/2021/01/part-1-rancher-kubernetes-engine-rke-security-best-practices-for-cluster-setup)

### GitOps Workflow with Flux
- [managedkube.com: A Complete Step by Step Guide to Implementing a GitOps Workflow with Flux](https://managedkube.com/gitops/flux/weaveworks/guide/tutorial/2020/05/01/a-complete-step-by-step-guide-to-implementing-a-gitops-workflow-with-flux.html)
- [youtube: GitOps Guide to the Galaxy (Ep 12): Flux On OpenShift](https://www.youtube.com/watch?v=W_rcYPZkhFg&ab_channel=RedHat)

### Amazon EKS. Deploy example microservices on EKS
* [eksworkshop.com](https://eksworkshop.com/ )
* [eksworkshop.com/x-ray/microservices](https://eksworkshop.com/x-ray/microservices/)
* [eksworkshop.com: Configure Cluster Autoscaler (CA)](https://eksworkshop.com/scaling/deploy_ca/)
* [aws.amazon.com: Deploy a kubernetes application](https://aws.amazon.com/getting-started/projects/deploy-kubernetes-app-amazon-eks/)
* [aws blogs: Git Push to Deploy Your App on EKS](https://aws.amazon.com/blogs/opensource/git-push-deploy-app-eks-gitkube/)
* [medium: create your first application on aws eks kubernetes](https://medium.com/faun/create-your-first-application-on-aws-eks-kubernetes-cluster-874ee9681293)
* [dzone: deploying a kubernetes cluster with amazon eks 🌟](https://dzone.com/articles/deploying-a-kubernetes-cluster-with-amazon-eks)
* [stacksimplify.com: DevOps with AWS CodePipeline on AWS EKS](https://www.stacksimplify.com/aws-eks/aws-devops-eks/learn-to-master-devops-on-aws-eks-using-aws-codecommit-codebuild-codepipeline/)
* [medium: AWS App Mesh with EKS and Canary deployment](https://medium.com/@anupam.s1602/aws-app-mesh-with-eks-and-canary-deployment-5503d9ba95d6)
* [github.com/stacksimplify/aws-eks-kubernetes-masterclass 🌟](https://github.com/stacksimplify/aws-eks-kubernetes-masterclass)

### Azure AKS
* [github.com/stacksimplify/azure-aks-kubernetes-masterclass 🌟](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass)
* [channel9.msdn.com: Troubleshoot AKS cluster issues with AKS Diagnostics and AKS Periscope](https://channel9.msdn.com/Shows/Azure-Friday/Troubleshoot-AKS-cluster-issues-with-AKS-Diagnostics-and-AKS-Periscope)

### Google Kubernetes Engine GKE
- [cloud.google.com: Troubleshooting services on Google Kubernetes Engine by example 🌟](https://cloud.google.com/blog/products/operations/troubleshooting-services-on-google-kubernetes-engine)

### Environments to learn and practice Kubernetes security
- [The Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) designed to be intentionally vulnerable cluster environment to learn and practice Kubernetes security.

## Red Hat Demo Central
* [gitlab.com/redhatdemocentral 🌟](https://gitlab.com/redhatdemocentral)
* [redhatdemocentral.gitlab.io](https://redhatdemocentral.gitlab.io)
* [CodeReady Containers - Red Hat Decision Manager Install Demo](https://gitlab.com/redhatdemocentral/rhcs-rhdm-install-demo)
* [youtube: CodeReady Containers - Easy OpenShift Container Platform 4.5 Installation](https://www.youtube.com/watch?v=CJMdSQVFVik)

### Cloud Native Development Architectural Diagrams Demos
* Cloud-native development is an approach to building and running applications to fully exploit the advantages of the cloud computing model (i.e. responsive, elastic and resilient applications).
* [Portfolio Architecture](https://redhatdemocentral.gitlab.io/portfolio-architecture-workshops/#/) Workshops for creating impactful architectural diagrams. This workshop will teach you how to use, design, and create architectural diagrams based on the **draw.io** tooling and Red Hat Portfolio Architecture design elelements. You'll leverage existing portfolio architecture diagrams as starting points.
    * [redhatdemocentral.gitlab.io/portfolio-architecture-tooling](https://redhatdemocentral.gitlab.io/portfolio-architecture-tooling/)
    * [gitlab.com: Project Examples](https://gitlab.com/redhatdemocentral/portfolio-architecture-examples)

## OpenShift Demos
* [developers.redhat.com: Developing on OpenShift (katacoda interactive learning) 🌟](https://developers.redhat.com/courses/openshift/) Learn how to access an OpenShift cluster, manage apps with the odo command-line tool, then try image and source-based deployment techniques.
* [github.com/OpenShiftDemos 🌟](https://github.com/OpenShiftDemos)
* [DockerHub OpenShift Demos](https://hub.docker.com/r/openshiftdemos/)
* [Red Hat Tutorials & Examples: github.com/redhat-developer-demos 🌟](https://github.com/redhat-developer-demos)
* [redhatgov.io](http://redhatgov.io) RedHatGov.io is an open source collection of workshop materials that cover various topics relating to Red Hat's product portfolio.
* [blog.openshift.com: OCP multi-node deployment on **AWS** using CloudFormation and Ansible (quickstart workshop)](https://blog.openshift.com/aws-and-red-hat-quickstart-workshop/)
* [Deploying Docker Images to OpenShift](https://dzone.com/articles/deploying-docker-images-to-openshift) We take a look at how to deploy a Docker image from DockerHub into RedHat's OpenShift environment, bringing added functionality along the way.
* [SonarQube: An OpenShift-focused Docker build of Sonarqube](https://github.com/OpenShiftDemos/sonarqube-openshift-docker)
* [Deploying PostgreSQL in MiniShift/OpenShift 3](https://blog.dbi-services.com/deploying-postgresql-in-minishiftopenshift/)
* [Clustering WildFly on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/clustering-wildfly-on-openshift-using-wildfly-operator)
* [Java EE example on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/java-ee-example-application-on-openshift)
* [Microprofile example on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/running-microprofile-applications-on-openshift)
* [Deploying WildFly apps on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/using-wildfly-on-openshift)
* [Running Thorntail apps on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/thorntail-on-openshift)
* [Running Spring Boot applications on Openshift](http://www.mastertheboss.com/jboss-frameworks/spring/deploy-your-springboot-applications-on-openshift)
* [github.com/openshiftdemos 🌟](https://github.com/openshiftdemos)
* [github.com/openshift-labs 🌟](https://github.com/openshift-labs) 
* [MapIt](https://github.com/siamaksade/mapit-spring) MapIt is a geo-spatial Spring Boot app which shows the location of AirPorts on the Map using Leaflet.
* [openshift.com: Simple Canary Deployments using Kubernetes StatefulSets on OpenShift](https://www.openshift.com/blog/simple-canary-deployments-using-kubernetes-statefulsets-on-openshift)
* [github.com/jbossdemocentral: Red Hat Process Automation Manager Mortgage Demo](https://github.com/jbossdemocentral/rhpam7-mortgage-demo)
* [medium: Tutorial : Secure your API with x509 Mutual Authentication with Spring Boot on OpenShift4](https://medium.com/@erfin.feluzy/tutorial-secure-your-api-with-x509-mutual-authentication-with-spring-boot-on-openshift4-416a00a47af8)
* [medium.com: Red Hat OpenShift Virtualization in nested VMware vSphere Cluster](https://medium.com/@carlosedp/red-hat-openshift-virtualization-in-nested-vmware-vsphere-56c5e5d76a80) In this post, I'll go thru the process of running Virtual Machines on OpenShift Virtualization in a nested setup inside VMware vSphere. This requires both ESXi hosts and a VCenter, both on 6.7U3 or up.
* [schabell.org: CodeReady Containers - Building a Cloud-Native Human Resources Process](https://www.schabell.org/2020/10/codeready-containers-building-cloud-native-hr-process.html)
* [developers.redhat.com: Persistent storage in action: Understanding Red Hat OpenShift’s persistent volume framework 🌟](https://developers.redhat.com/blog/2020/10/22/persistent-storage-in-action-understanding-red-hat-openshifts-persistent-volume-framework/)
* [opensource.com: Set up Minishift and run Jenkins on Linux](https://opensource.com/article/20/11/minishift-linux) Install, configure, and use Minishift to create your first pipeline.
* [dzone: CodeReady Containers - Exploring a home loan mortgage process](https://dzone.com/articles/codeready-containers-exploring-a-home-loan-mortgag) As a cloud-native developer you've installed an OpenShift Container Platform development environment on your local machine, but what's next...
* [Rcarrata's blog](https://rcarrata.com/)
* [JBoss Web Server Operator 🌟](https://access.redhat.com/documentation/en-us/red_hat_jboss_web_server/5.4/html-single/red_hat_jboss_web_server_for_openshift/index#jws_operator) Did you know that you can run Tomcat in Containers on Kubernetes in a easy supported manner? Take a look at the JBoss Web Server (a.k.a. @RedHat 's build of Tomcat) Operator for OpenShift 
* [developers.redhat.com: Containerize and deploy Strapi CMS applications on Kubernetes and Red Hat OpenShift](https://developers.redhat.com/blog/2021/04/09/containerize-and-deploy-strapi-applications-on-kubernetes-and-red-hat-openshift/?sc_cid=7013a0000026GuZAAU)

### Developer Sandbox
* [Developer Sandbox for Red Hat OpenShift 🌟](https://developers.redhat.com/developer-sandbox) Get free access to the Developer Sandbox for Red Hat OpenShift and deploy your application code as a container on this self-service, cloud-hosted experience. Skip installations and deployment and jump directly into OpenShift.
* [developers.redhat.com: How to deploy a Java application on Kubernetes in minutes](https://developers.redhat.com/developer-sandbox/how-to-deploy-java-application-in-kubernetes) Move your legacy Java application into a container and deploy it to Kubernetes. The Developer Sandbox for Red Hat OpenShift is a free OpenShift cluster that gives you access to the cutting-edge technologies built on Kubernetes. A quick sign-up gets you a cluster and access to a set of developer tools and services. Move this Spring Pet Clinic example application into a container using the Source-to-Image (s2i) feature. 

### OpenShift VS Kubernetes
* [developer.ibm.com: Example exercises to differentiate OpenShift and Kubernetes](https://developer.ibm.com/tutorials/examples-differentiate-openshift-kubernetes/) Example exercises to differentiate OpenShift and Kubernetes. Walk through some steps with Red Hat OpenShift on IBM Cloud.

### IBM Cloud Pak Playbooks
* [IBM Cloud Pak Playbook](https://cloudpak8s.io/apps/cp4a_overview/)

### Knative 
* [knative-tutorial](https://github.com/redhat-developer-demos/knative-tutorial) A pratical guide to get started with knative. Knative concepts are explained simple and easy way with lots of demos and exercises.
* [aymen-segni.com: Deploying Serverless Services on Kubernetes using Knative](https://aymen-segni.com/index.php/2020/07/22/deploying-your-serverless-services-on-kubernetes-using-knative/)

### OpenShift Pipelines Workshop (Tekton)
- [Build a Go application using OpenShift Pipelines](https://developers.redhat.com/blog/2020/05/26/build-a-go-application-using-openshift-pipelines/)
    - [openshift-pipelines-workshop](https://redhat-developer-demos.github.io/openshift-pipelines-workshop/) Workshop to demonstrate OpenShift Pipelines (featuring Tekton)
- [OpenShift Pipelines Catalog](https://github.com/openshift/pipelines-catalog)
- [systemcraftsman/lab-tekton-pipelines: OpenShift Pipelines workshop](https://github.com/systemcraftsman/lab-tekton-pipelines)
- [openshift.com: GitOps Using Red Hat OpenShift Pipelines (Tekton) and Red Hat Advanced Cluster Management](https://www.openshift.com/blog/gitops-using-red-hat-openshift-pipelines-tekton-and-red-hat-advanced-cluster-management)
- [Set up continuous integration for .NET Core with OpenShift Pipelines](https://developers.redhat.com/blog/2020/09/24/set-up-continuous-integration-for-net-core-with-openshift-pipelines/)
- [alesnosek.com: CI/CD Pipeline Spanning Multiple OpenShift Clusters (jenkins & tekton)](http://alesnosek.com/blog/2020/06/30/ci-slash-cd-pipeline-spanning-multiple-openshift-clusters/)
- [openshift.com: Guide to OpenShift Pipelines Part 1 - Introducing OpenShift Pipelines](https://www.openshift.com/blog/guide-to-openshift-pipelines-part-1-introducing-openshift-pipelines)
- [kailashyogeshwar.medium.com: How we implemented Reusable CI/CD Pipeline using Git and Tekton](https://kailashyogeshwar.medium.com/how-we-implemented-reusable-ci-cd-pipeline-using-git-and-tekton-503bed91975b)
- [openshift.com: GitOps Using Red Hat OpenShift Pipelines (Tekton) and Red Hat Advanced Cluster Management to Deploy on Multiple Clusters 🌟](https://www.openshift.com/blog/gitops-using-red-hat-openshift-pipelines-tekton-and-red-hat-advanced-cluster-management-to-deploy-on-multiple-clusters)
- [developers.redhat.com: Getting started with Tekton and Pipelines](https://developers.redhat.com/blog/2021/01/13/getting-started-with-tekton-and-pipelines/)

### ArgoCD
- [rromannissen/rhoar-microservices-demo: GitOps for Microservices with Red Hat Runtimes demo](https://github.com/rromannissen/rhoar-microservices-demo) A GitOps pipeline example using ArgoCD, tektoncd and HelmPack for springboot and QuarkusIO microservices. 
- [developers.redhat.com: From code to production with OpenShift Pipelines and Argo CD](https://developers.redhat.com/blog/2020/09/10/from-code-to-production-with-openshift-pipelines-and-argo-cd/)
- [developers.redhat.com: Building modern CI/CD workflows for serverless applications with Red Hat OpenShift Pipelines and Argo CD, Part 1](https://developers.redhat.com/blog/2020/10/01/building-modern-ci-cd-workflows-for-serverless-applications-with-red-hat-openshift-pipelines-and-argo-cd-part-1/)
  - [developers.redhat.com: Building modern CI/CD workflows for serverless applications with Red Hat OpenShift Pipelines and Argo CD, Part 2](https://developers.redhat.com/blog/2020/10/14/building-modern-ci-cd-workflows-for-serverless-applications-with-red-hat-openshift-pipelines-and-argo-cd-part-2/)
- [itnext.io: Deploy Argo CD with Ingress and TLS in Three Steps: No YAML Yak Shaving Required 🌟](https://itnext.io/deploy-argo-cd-with-ingress-and-tls-in-three-steps-no-yaml-yak-shaving-required-bc536d401491)
  - [Ambassador Edge Stack. K8S Initializer  (scaffolding tool) 🌟](https://app.getambassador.io/)
- [developers.redhat.com: Introduction to Tekton and Argo CD for multicluster development](https://developers.redhat.com/blog/2020/09/03/introduction-to-tekton-and-argo-cd-for-multicluster-development/)
- [itnext.io: Solving ArgoCD Secret Management with the argocd-vault-plugin 🌟](https://itnext.io/argocd-secret-management-with-argocd-vault-plugin-539f104aff05)
- [youtube: Exploring The Cloud-native Kubernetes CI/CD Pipeline Tool Landscape](https://www.youtube.com/watch?v=5XWwjyikWMQ&feature=emb_logo&ab_channel=Konveyor) In this meetup, we explore the new era of Kubernetes continuous integration continuous deployment pipelines based on a set of fancy tools as Tekton Pipelines, ArgoCD or Helm. We walk through the new DevOps and GitOps technologies landscape and a real demonstration of how these tools work together in order to make developers and system administrators lives easier. [repo1](https://github.com/acidonper/jump-app-gitops) , [repo2](https://github.com/acidonper/jump-app-docs) , [slides](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTVoMnVrcVR5Tjl0dlBGWkx2UTZzMHA3N1N3QXxBQ3Jtc0tsZkZrcUpfSzhBX1EzdUtOanRqV3o2WDZpdkhPY0NyODhmbERSQUhROFRPa2pZRC13Q3l0ekQ2MjR1LTIyY254VmhwdHVack1XeDJiRWVBMUl6U3RDRHo3cF9XVDVJRTluLWJFVXNYUjF5OFV4ZlN5SQ&q=https%3A%2F%2Fdocs.google.com%2Fpresentation%2Fd%2F14fSLwfEVpDU-3udMGEW9bQATCAOy0F8b6UOgNgDkD3A%2Fedit%3Fusp%3Dsharing)
- [blog.argoproj.io: Introducing the ApplicationSet Controller for Argo CD](https://blog.argoproj.io/introducing-the-applicationset-controller-for-argo-cd-982e28b62dc5)
- [vzilla.co.uk: GitOps - Getting started with ArgoCD](https://vzilla.co.uk/vzilla-blog/gitops-getting-started-with-argocd)

### GitLab Pipelines on OpenShift
- [openshift.com: Building GitLab Pipelines on OpenShift](https://www.openshift.com/blog/building-openshift-pipelines-with-gitlab)

### Deploying Web Applications with Eclipse JKube (formerly known as fabric8)
- [Building and Deploying a Weather Web Application onto Kubernetes/Red Hat OpenShift using Eclipse JKube](https://itnext.io/building-and-deploying-a-weather-web-application-onto-kubernetes-red-hat-openshift-using-eclipse-62bf7c924be4)
- [Java development on top of Kubernetes using Eclipse JKube](https://developers.redhat.com/blog/2020/08/24/java-development-on-top-of-kubernetes-using-eclipse-jkube/)
  - [medium: Deploy Quarkus Todo List App to Kubernetes Using Eclipse JKube](https://medium.com/swlh/deploy-quarkus-todo-list-app-to-kubernetes-using-eclipse-jkube-c774ef6b68f0)
- [youtube: Deploy your Java applications to the Cloud using Eclipse JKube (petclinic) 🌟](https://www.youtube.com/watch?v=vgIwRX4LXfU)

### Monitoring Services with OpenShift ServiceMesh
- [Monitoring Services like an SRE in OpenShift ServiceMesh](https://www.openshift.com/blog/monitoring-services-like-an-sre-in-openshift-servicemesh)

### Red Hat Migration Toolkit for Applications
- [Migration Toolkit for Applications: Getting Started](https://developers.redhat.com/products/mta/getting-started)
- [Migration Toolkit for Applications Demo - June 2020](https://youtu.be/mRCz6Jl0Ds8) Migraiton Toolkit from Applications by Red Hat can help you migrate and/or modernize your applications by analyzing them and finding isses such as use of proprietary classes or behaviousr that are not conformant with 12factor app, in order to help you modernize your app portfolio and make it more cloud & container friendly.
- [dzone: Red Hat’s Migration Toolkit for Applications](https://dzone.com/articles/analyze-monolithic-java-applications-in-multiple-w) This article explains how to analyze monolithic Java applications in multiple workspaces with Red Hat’s migration toolkit for applications.

### Red Hat Advanced Cluster Management RHACM 
- [openshift.com: Applications Here, Applications There! - Part 3 - Application Migration](https://www.openshift.com/blog/applications-here-applications-there-part-3-application-migration)
- [Advanced Cluster Management Demos](https://www.youtube.com/playlist?list=PLbMP1JcGBmSFA56rykbH2fg1F9Tozk4of) Want to manage Kubernetes clusters at scale? Struggle with Application Lifecycle? Need to ensure Security and Compliance policies across clusters? Check out these demos of Red Hat Advanced Cluster Manager (RHACM).
- [redhat.com: ACM Ansible Integration Overview](https://www.redhat.com/en/about/videos/acm-ansible-integration-overview)
- [opensift.com: K8s Integrity Shield (tech-preview): Protecting the Integrity of Kubernetes Resources with Signature](https://www.openshift.com/blog/k8s-integrity-shield-tech-preview-protecting-the-integrity-of-kubernetes-resources-with-signature)

### OKD
* [medium.com: Installing an OKD 4.5 Cluster](https://medium.com/@craig_robinson/guide-installing-an-okd-4-5-cluster-508a2631cbee)
  * [itnext.io: Guide: Installing an OKD 4.5 Cluster](https://itnext.io/guide-installing-an-okd-4-5-cluster-508a2631cbee)
* [openshift.com: Recap: OKD 4 Testing and Deployment Workshop - Videos and Additional Resources](https://www.openshift.com/blog/recap-okd-4-testing-and-deployment-workshop-videos-and-additional-resources?utm_source=thenewstack&utm_medium=twitter&utm_campaign=platform)

### Helm 3 on OpenShift
- [Katacoda Lab: Getting Started with Helm 3 on OpenShift](https://learn.openshift.com/developing-on-openshift/helm/)

### Writing Kubernetes Operators
- [developers.redhat.com: ‘Hello, World’ tutorial with Kubernetes Operators](https://developers.redhat.com/blog/2020/08/21/hello-world-tutorial-with-kubernetes-operators/)

### Customized Reports with Metering Operator (monitoring k8s resources)
- [Writing Customized Reports Using Metering Operator](https://www.openshift.com/blog/writing-customized-reports-using-metering-operator)

### Red Hat AMQ Streams (Kafka)
- [developers.redhat.com: HTTP-based Kafka messaging with Red Hat AMQ Streams](https://developers.redhat.com/blog/2020/08/04/http-based-kafka-messaging-with-red-hat-amq-streams/)
- [developers.redhat.com: Message broker integration made simple with Red Hat Fuse](https://developers.redhat.com/blog/2021/01/08/message-broker-integration-made-simple-with-red-hat-fuse/) This article presents a sample integration between Red Hat AMQ 7 and IBM MQ, using Red Hat Fuse 7 for the integration. Traditionally, developers have used resource adapters for message bridging with external systems. A resource adapter is a system library that provides connectivity to an enterprise information system (EIS). Similar to how a Java Database Connectivity (JDBC) driver provides connectivity to a database management system, a resource adapter plugs into an application server such as Red Hat JBoss Enterprise Application Platform (JBoss EAP). It then connects the application server, enterprise information system, and the enterprise application.

## Jenkins Demos
* [kublr.com: cicd pipeline with jenkins nexus kubernetes](https://kublr.com/blog/cicd-pipeline-with-jenkins-nexus-kubernetes/)
* [bitbucket.org: setting up a cicd pipeline with spring mvc and kubernetes on aws](https://bitbucket.org/blog/setting-up-a-ci-cd-pipeline-with-spring-mvc-jenkins-and-kubernetes-on-aws )
* Medium.com - Simple Spring Boot microservice deployed in Kubernetes using Docker and Nexus 🌟:
    * [Part 1](https://medium.com/@simionrazvan/simple-spring-boot-microservice-deployed-in-kubernetes-using-docker-and-nexus-part-1-b581e3ca8916)
    * [Part 2](https://medium.com/@simionrazvan/simple-spring-boot-microservice-deployed-in-kubernetes-using-docker-and-nexus-part-2-25dc2a3982cf)
* [kubernetes-advocate.medium.com: CI/CD with Dockers and Jenkins 🌟](https://kubernetes-advocate.medium.com/ci-cd-with-dockers-and-jenkins-70b6f801f9f7)
* [medium.com/@devml2016: Let’s Start Automation using Jenkins, Docker, GitHub](https://medium.com/@devml2016/lets-start-automation-using-jenkins-docker-github-d5f8d019ec4a)
* [developers.redhat.com: An easier way to create custom Jenkins containers](https://developers.redhat.com/blog/2020/06/04/an-easier-way-to-create-custom-jenkins-containers) Create your own custom Jenkins container image by aggregating readily available containers in a pod template.
* [medium: Just commit your code and your docker server is ready (jenkins + github + docker)](https://medium.com/@deepanshuyadavv11/task1-integrating-github-jenkins-and-docker-d66a817774be)
* [lambdatest.com: Best Jenkins Pipeline Tutorial For Beginners (Examples) 🌟](https://www.lambdatest.com/blog/jenkins-pipeline-tutorial/)
* [ittroubleshooter.in: Run Parallel Builds in Kubernetes Cluster with Jenkins Pipeline 🌟](https://ittroubleshooter.in/run-parallel-build-kubernetes-cluster-jenkins/)
* [cloudogu/jenkinsfiles 🌟🌟🌟](https://github.com/cloudogu/jenkinsfiles) This project contains examples for the [Jenkins pipeline plugin](https://jenkins.io/solutions/pipeline/), comparing both declarative and scripted syntax. The examples were developed while working on an article series called Coding Continuous Delivery published in [Java aktuell](http://www.ijug.eu/java-aktuell/das-magazin.html). Both English translation and German original can be found on the [Cloudogu Blog](https://cloudogu.com/en/blog).
* [aws.amazon.com: Integrating Jenkins with AWS CodeArtifact to publish and consume Python artifacts](https://aws.amazon.com/blogs/devops/using-jenkins-with-codeartifact/)
* [github.com/monodot/pipeline-library-demo 🌟](https://github.com/monodot/pipeline-library-demo) Demonstrates how to use a Shared Library in Jenkins pipelines. This repository defines a single function, sayHello, which will echo a greeting.
* [piotrminkowski.com: Continuous Integration with Jenkins on Kubernetes 🌟](https://piotrminkowski.com/2020/11/10/continuous-integration-with-jenkins-on-kubernetes/)
* [youtube: Simple DevOps Project | Publish Android APK to App Center | Beginner Pipeline](https://www.youtube.com/watch?v=KgH0QzMHXLs)
* [blog.flant.com: Configuring Continuous Integration for Jenkins & Bitbucket using werf](https://blog.flant.com/configuring-continuous-integration-for-jenkins-bitbucket-using-werf/)
* [lambdatest.com: Comprehensive Guide To Jenkins Declarative Pipeline [With Examples] 🌟](https://www.lambdatest.com/blog/jenkins-declarative-pipeline-examples/)

### Jenkins Declarative Pipelines with OpenShift
* [github.com/openshift: Using Jenkins Declarative Pipelines with OpenShift 🌟](https://github.com/openshift/origin/tree/master/examples/jenkins/pipeline)
* [github.com/gnunn1/openshift-basic-pipeline](https://github.com/gnunn1/openshift-basic-pipeline)
* [github.com/deweya/OpenShift-Jenkins-Lab](https://github.com/deweya/OpenShift-Jenkins-Lab)
* [Red Hat CodeReady Containers (Minishift equivalent for OpenShift 4.2 or newer) - step-by-step demo guides](https://github.com/marcredhat/crcdemos)
* [Grading Pipeline for OpenShift 4 Advanced Application Deployment Homework Assignment](https://github.com/redhat-gpte-devopsautomation/ocp4_app_deploy_homework_grading)
* [github - Demostration of a basic OpenShift CI/CD pipeline deploying an application in Development then Test](https://github.com/gnunn1/openshift-basic-pipeline)

### OpenShift Pipelines with S2i and Jenkins Blue Ocean
- [OpenShift Pipelines with Jenkins Blue Ocean 🌟](https://www.openshift.com/blog/openshift-pipelines-jenkins-blue-ocean)
- [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) Jenkins Blue Ocean for OpenShift Jenkins S2I

### Jenkins Configuration as Code on Kubernetes
* [Demo of Jenkins Configuration-As-Code with Docker and Groovy Hook Scripts (java11-support branch) 🌟🌟](https://github.com/oleg-nenashev/demo-jenkins-config-as-code/tree/java11-support)
* [Configuration as Code of Jenkins (for Kubernetes) 🌟🌟](https://github.com/figaw/configuration-as-code-jenkins-k8s)
* [Jenkins Configuration as Code on Kubernetes 🌟](https://github.com/redhatspain/jenkins-CasC-kubernetes-demo) A Codecentric/Jenkins Helm 3 Sample Chart on Digital Ocean Kubernetes with Spring Petclinic Demo Pipeline

### From Jenkins Freestyle jobs to Pipeline, with JobDSL. Seed jobs
* [Meetup event: From Freestyle jobs to Pipeline, with JobDSL](https://www.meetup.com/Jenkins-online-meetup/events/270600737/)
    * Manually managing Jenkins jobs is painful. Jenkins Pipeline exists, but how do you get started and why should you bother in the first place? Journey with Nicolaj, as he talks about the pains of managing a manually configured job in Jenkins; converts a Freestyle Job to JobDSL, instantly; introduces mechanisms for adding the jobs to Jenkins, as code; and ultimately converts the job to a Jenkins Pipeline!
    * Just like last time, in the talk “Configuration as Code of Jenkins (for Kubernetes),” you’ll see plenty of live demos and get to take home all the code and examples afterwards. Use it as the starting point for taking advantage of the Configuration as Code (CasC) that everyone is talking about, and hopefully it will save you a lot of headache in the future!
    * Agenda:
        * Manual Freestyle jobs, and why they hurt us
        * Introduction to JobDSL and adding JobDSL-jobs to Jenkins
        * From Freestyle Jobs to JobDSL, the beginning of our CasC adventure
        * From JobDSL to Pipeline, all the fun of CasC; with even more resilience!
    * Nicolaj Græsholt is a Continuous Delivery and DevOps Consultant and Trainer from Eficode Praqma. He helps organizations with all things CI/CD, Artifact Management, Git, Docker and Kubernetes, and he’s a Certified Kubernetes Administrator of CNCF.
    * [Slides 🌟🌟🌟](https://github.com/figaw/freestyle-to-pipeline-jenkins/blob/master/from-freestyle-jobs-to-pipeline-with-jobdsl.pdf)
    * [Demo repository 🌟🌟🌟](https://github.com/figaw/freestyle-to-pipeline-jenkins)
* Links of interest provided in the event:
    * [Continuation Passing Style (CPS)](https://github.com/cloudbees/groovy-cps/blob/master/doc/cps-basics.md) is a style of programming in which the remainder of the program is passed explicitly as a parameter, as opposed to that being handled implicitly represented as call stack.
        * [Jenkins Pipeline execution engine based on Continuation Passing Style (CPS) transformation of Groovy scripts. DSL Methods:](https://jenkinsci.github.io/job-dsl-plugin/#plugin/workflow-cps):
            * [cps](https://jenkinsci.github.io/job-dsl-plugin/#method/javaposse.jobdsl.dsl.helpers.workflow.WorkflowDefinitionContext.cps): WorkflowDefinitionContext
            * [cpsScm](https://jenkinsci.github.io/job-dsl-plugin/#method/javaposse.jobdsl.dsl.helpers.workflow.WorkflowDefinitionContext.cpsScm): WorkflowDefinitionContext
        * [Defines a Groovy CPS DSL definition: pipelineJob definition cps script](https://jenkinsci.github.io/job-dsl-plugin/#path/pipelineJob-definition-cps-script)
    * [Jenkins CLI](https://www.jenkins.io/doc/book/managing/cli/)
    * [How to create initial "seed" job](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/seed-jobs.md)
    * [Jenkinsfile Runner Test Framework](https://github.com/jenkinsci/jenkinsfile-runner-test-framework)
    * [Jenkins Pipeline Unit testing framework](https://github.com/jenkinsci/JenkinsPipelineUnit)
    * [Plugin Installation Manager Tool](https://github.com/jenkinsci/plugin-installation-manager-tool)
    * [Jenkins Custom WAR Packager](https://github.com/jenkinsci/custom-war-packager)
    * Jenkins Configuration as Code:
        * [Configuration as Code of Jenkins (for Kubernetes) 🌟](https://github.com/figaw/configuration-as-code-jenkins-k8s)
        * [JEP-224: System Read permission: Improve experience of Jenkins Configuration-as-Code users](https://www.jenkins.io/events/online-hackfest/2020-uiux/) It improves the modifying Web UI configuration controls to support the read-only mode.
    * Plugins:
        * [Plugin Usage](https://plugins.jenkins.io/plugin-usage-plugin/) This plugin gives you the possibility to analyze the usage of your installed plugins.
        * [Pipeline as YAML (Incubated) 🌟](https://plugins.jenkins.io/pipeline-as-yaml/)
        * [Jenkins Job DSL Plugin](https://github.com/jenkinsci/job-dsl-plugin#documentation) A Groovy DSL for Jenkins Jobs - Sweeeeet!
        * [Least Load](https://plugins.jenkins.io/leastload/) This plugin overrides the default Load Balancer behavior and assigns jobs to nodes with the least load
        * [Declarative Pipeline Migration Assistant](https://plugins.jenkins.io/declarative-pipeline-migration-assistant/)
    * Jenkins Job DSL:
        * [Jenkins Job DSL API 🌟](https://jenkinsci.github.io/job-dsl-plugin/)
            * [mavenJob](https://jenkinsci.github.io/job-dsl-plugin/#path/mavenJob)
        * [Example of a pipeline with parameters](https://github.com/polarpoint-io/groovy-jenkins-pipelines/blob/master/jobs/parameterisedPipelines.groovy)
    * [Pipeline Global Library for ci.jenkins.io](https://github.com/jenkins-infra/pipeline-library) Collection of custom steps and variables for our Jenkins instance(s)

<center>
<iframe src="https://www.youtube.com/embed/uhD49XXiRqY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

### SDKMAN 
* [SdkMan](https://sdkman.io/) is a tool for managing parallel versions of multiple Software Development Kits on most Unix based systems. It provides a convenient Command Line Interface (CLI) and API for installing, switching, removing and listing Candidates. Formerly known as **GVM** the **Groovy enVironment Manager**, it was inspired by the very useful [RVM](https://rvm.io/) and [rbenv](https://github.com/sstephenson/rbenv) tools, used at large by the Ruby community.
* [Using Jenkins Pipeline parallel stages to build Maven project with different JDKs](https://e.printstacktrace.blog/using-jenkins-pipeline-parallel-stages-to-build-maven-project-with-different-jdks/)
* **Demo:** A single Jenkinsfile, a Java Maven project, a single Dockerfile, multiple Java versions build and tested in parallel thanks to SDKMAN:
    * [Using SDKMAN! as a docker image for Jenkins Pipeline - a step by step guide 🌟](https://e.printstacktrace.blog/using-sdkman-as-a-docker-image-for-jenkins-pipeline-a-step-by-step-guide/)
    * [Multiple Java versions in a single Jenkins Pipeline using Docker and SDKMAN 🌟](https://www.youtube.com/watch?v=j1lH3vOhucw) In this video, I show you how you can use Jenkins Declarative Pipeline to create a build pipeline that compiles the Maven Java project using three different Java versions (8, 11, and 15.) You will learn how to use a matrix section of the Jenkins Pipeline to define parallel stages, as well as how to create a Docker image that provides both Java and Maven using the powerful SDKMAN command-line tool. After watching this video you should feel comfortable with setting up multiple parallel stages to build your Java project using different versions of the compiler. And what is most important - it does not require creating Dockerfiles for each Java version. I will show you how to build the pipeline using just a single Dockerfile that does the job. 
    * [Jenkins Pipeline Maven build demo](https://github.com/wololock/jenkine-pipeline-maven-demo/tree/sdkman)

<center>
<iframe src="https://www.youtube.com/embed/j1lH3vOhucw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

### Jenkins Scripts
* **cleanup.Jenkinsfile**: Jenkinsfile with Declarative Pipeline Multiline sh that cleanups old builds. All the Stages are now visually monitored. It is triggered every saturday night and ends with jenkins restart. These Multi-line bash commands make easier to read Jenkins Projects.
* **daily_restart.Jenkinsfile**: A script that automatically triggers a daily restart of Jenkins due to performance issues (Jenkins is a Java application). Jenkins with Declarative Pipeline multiline sh that restarts Jenkins every night except on Saturday nights (when cleanup.Jenkinsfile is triggered). 
* **confluence6-docker-build.Jenkinsfile**: Declarative Jenkinsfile for building and uploading a docker image to Openshift-DEV, Dockerhub and Openshift-PROD (Stages are disabled via Conditional Build Steps). Tip: A Docker Plugin for Jenkins can easily replace this Jenkinsfile. 

Grab them from here: [awesome-kubernetes/scripts](https://github.com/redhatspain/awesome-kubernetes/tree/master/scripts)

### Postman & Newman API Automated Tests
- [LerryAlexander: Postman + Newman API Automated Tests running on a Jenkins Pipeline 🌟](https://github.com/LerryAlexander/postman_jenkins_api_tests)
- [praveendavidmathew.medium.com: Data driven testing per request without using data file](https://praveendavidmathew.medium.com/data-driven-testing-per-request-without-using-data-file-aeb573b4f63a)

### Monitoring Jenkins with Grafana
- [Mostrando resultados de Jenkins en Grafana mediante InfluxDB 🌟](https://enmilocalfunciona.io/mostrando-resultados-de-jenkins-en-grafana-mediante-influxdb/)

## Jenkins X
- [blog.testproject.io: Jenkins X Cloud Native CI/CD with TestProject](https://blog.testproject.io/2020/07/09/jenkins-x-cloud-native-ci-cd-with-testproject/)
- [Modernize Your CI/CD Pipeline Using Jenkins X with Amazon EKS](https://aws.amazon.com/blogs/apn/modernize-your-ci-cd-pipeline-using-jenkins-x-with-amazon-eks/)

## Spinnaker
- [Demo/Evaluation Installations](https://spinnaker.io/setup/quickstart/)
* [wardviaene/advanced-kubernetes-course/spinnaker 🌟](https://github.com/wardviaene/advanced-kubernetes-course/tree/master/spinnaker)
- [imperialwicket/spinnaker-demo](https://github.com/imperialwicket/spinnaker-demo)
- [henrybell/spinnaker-demo-app](https://github.com/henrybell/spinnaker-demo-app)
- [codeburst.io: Spinnaker by Example: Part 1](https://codeburst.io/spinnaker-by-example-part-1-c4de9180d689)
- [codeburst.io: Spinnaker by Example: Part 2](https://codeburst.io/spinnaker-by-example-part-2-6f92a1fdaedf)
- [codeburst.io: Spinnaker by Example: Part 3](https://codeburst.io/spinnaker-by-example-part-3-c6ed9ac5f8ce)
- [dzone: Continuous Deployment on Kubernetes With Spinnaker](https://dzone.com/articles/continuous-deployment-on-kubernetes-with-spinnaker) In this article, learn how to setup Spinnaker and integrate it with Gitlab CI and Jenkins to build and run CI and CD pipelines.
- [dzone: Continuous Delivery Pipeline for Kubernetes Using Spinnaker](https://dzone.com/articles/continuous-delivery-pipeline-for-kubernetes-using) This post will focus on pushing out new releases of the application to our Kubernetes cluster i.e. Continuous Delivery.
- [armory.io: How to Set Up Liquibase in Spinnaker](https://www.armory.io/blog/how-to-set-up-liquibase-in-spinnaker/)
- [armory.io: Build a Deployment Pipeline with Spinnaker on Kubernetes](https://www.armory.io/blog/build-a-deployment-pipeline-with-spinnaker-on-kubernetes/)
- [hackernoon: Using Spinnaker with Kubernetes for CI/CD](https://hackernoon.com/using-spinnaker-with-kubernetes-for-cicd-52w3uo9)

## Nexus3 on Kubernetes
* [Proof of Concept: Nexus3 Chart configuration on Kubernetes](https://github.com/redhatspain/nexus3-helm-chart) A choerodon/nexus3 Helm 3 Sample Chart on Digital Ocean Kubernetes

## GitLab 
- [piotrminkowski.com: GitLab CI/CD on Kubernetes](https://piotrminkowski.com/2020/10/19/gitlab-ci-cd-on-kubernetes/)
- [about.gitlab.com: The basics of CI: How to run jobs sequentially, in parallel, or out of order](https://about.gitlab.com/blog/2020/12/10/basics-of-gitlab-ci-updated/) New to continuous integration? Learn how to build your first CI pipeline with GitLab.

## Spring PetClinic Sample Application
* [spring-petclinic.github.io](https://spring-petclinic.github.io)
    * [spring-petclinic.github.io Docs](https://spring-petclinic.github.io/docs/resources.html)
* [github.com/spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)
    * [gitlab.beuth-hochschule.de](https://gitlab.beuth-hochschule.de/s70178/petclinic-ansible-jenkins-ci-cd)
    * [gitlab.comquent.de: Microservices branch](https://gitlab.comquent.de/petclinic/spring-petclinic-microservices)
* [deors/deors-demos-petclinic jenkinsfile](https://github.com/deors/deors-demos-petclinic/blob/master/Jenkinsfile)
* [liatrio.com: building with docker using jenkins pipelines](https://www.liatrio.com/blog/building-with-docker-using-jenkins-pipelines)
* [stackoverflow: How to define BuildConfig object with Jenkins and openshift
](https://stackoverflow.com/questions/52337851/how-to-define-buildconfig-object-with-jenkins-and-openshift)
* [cloudogu.com: CD with Jenkins, Nexus and cloudogu](https://cloudogu.com/en/blog/cd-with-nexus-jenkins-ces)
* [experfy.com e-learning: Effective Jenkins - Continuous Delivery and Continuous Integration](https://www.experfy.com/training/courses/effective-jenkins-continuous-delivery-and-continuous-integration)
* [github.com/redhat-developer-demos/spring-petclinic 🌟](https://github.com/redhat-developer-demos/spring-petclinic)

### Modular Pipeline Library (MPL). Petclinic Pipeline example with MPL  
* [griddynamics/mpl](https://github.com/griddynamics/mpl)
* [blog.griddynamics.com: Developing a modular pipeline library to improve DevOps collaboration](https://blog.griddynamics.comdeveloping-a-modular-pipeline-library-to-improve-devops-collaboration/)
* [youtube: Modular Pipeline Library: 4. Petclinic Pipeline 🌟](https://www.youtube.com/watch?v=GLtvxY1S3Aw) MPL demo video about more or less real petclinic pipeline with selenium tests, comparison to bare jenkinsfile pipeline without mpl, modules override mechanisms.

### PetClinic on Kubernetes:
* [github.com/spring-petclinic/spring-petclinic-kubernetes 🌟](https://github.com/spring-petclinic/spring-petclinic-kubernetes)
    * While waiting for a working version, you could check [this fork](https://github.com/odedia/spring-petclinic-microservices)
* [Spring PetClinic Microservices](https://github.com/spring-petclinic/spring-petclinic-microservices)
    * [Google Cloud Native Spring Boot PetClinic. Spring PetClinic Microservices on GCP 🌟](https://github.com/saturnism/spring-petclinic-gcp) Example Petclinic deployment on Google Cloud Platform into Google Kubernetes Engine with Istio. This is based on [Spring PetClinic Microservices](https://github.com/spring-petclinic/spring-petclinic-microservices). 
* spring-petclinic-microservices renamed to spring-petclinic-cloud 🌟: https://github.com/spring-petclinic/spring-petclinic-cloud 
* [Distributed version of Spring Petclinic built with Spring Cloud 🌟](https://github.com/odedia/spring-petclinic-microservices)
* [github.com/paulczar/k8s-spring-petclinic](https://github.com/paulczar/k8s-spring-petclinic)
* [tech.paulcz.net/blog/spring-into-kubernetes-part-1](https://tech.paulcz.net/blog/spring-into-kubernetes-part-1/)
* [github.com/kohsuke/petclinic Jenkinsfile](https://github.com/kohsuke/petclinic/blob/master/Jenkinsfile)
* [pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images 🌟](https://pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images/)

### PetClinic Docker images:
* [ref 1](https://hub.docker.com/r/ibuchh/petclinic-spinnaker-jenkins)
* [ref 2](https://hub.docker.com/r/sarjunkumar24391/petclinic)
* [ref 3](https://hub.docker.com/r/bmoussaud/petclinic)
* [ref 4](https://hub.docker.com/r/alwin2/petclinic-customers-service)
* [ref 5 arey/springboot-petclinic](https://hub.docker.com/r/arey/springboot-petclinic/)
* [ref 6](https://hub.docker.com/r/anthonydahanne/spring-petclinic)
* [ref 7](https://hub.docker.com/r/jbrisbin/spring-petclinic/)
* [ref 8](https://github.com/spring-projects/spring-petclinic/issues/339)
* [ref 9 - I have a branch that adds Docker, Kubernetes and Knative into the mix - planning on submitting a PR at some point](https://github.com/trisberg/spring-petclinic/tree/kubernetes)

### OpenShift.io Samples 
* [OpenShift.io Samples 🌟🌟](https://che.openshift.io/dashboard/#/getstarted)
* [github.com/che-samples](https://github.com/che-samples)

## AWS Demos
- [github.com/miztiik/AWS-Demos](https://github.com/miztiik/AWS-Demos)
- [github.com/aws-samples](https://github.com/aws-samples)
- [github.com/aws-samples/aws-training-demo](https://github.com/aws-samples/aws-training-demo)
- [cyberciti.biz: How to create MySQL user and grant permissions in AWS RDS](https://www.cyberciti.biz/faq/how-to-create-mysql-user-and-grant-permissions-in-aws-rds/)
- [stacksimplify.com: DevOps with AWS CodePipeline on AWS EKS](https://www.stacksimplify.com/aws-eks/aws-devops-eks/learn-to-master-devops-on-aws-eks-using-aws-codecommit-codebuild-codepipeline/)
- [medium: Fetch Application Inventory using Systems Manager](https://medium.com/cloud-techies/application-inventory-using-system-manager-f3eeb75d3279) Get application inventory from each EC2 instance and store it in centralized account S3 bucket. To query the information from s3 bucket, we are integrating Glue, Athena (from another account).
- [youtube: Build a Music Sharing App with Amazon S3 and AWS Amplify](https://www.youtube.com/watch?v=6W2TuBDaaiI&ab_channel=AliSpittel)
- [freecodecamp.org: How to Deploy a React App to Production Using Docker and NGINX with API Proxies](https://www.freecodecamp.org/news/how-to-deploy-react-apps-to-production/)

## Azure DevOps Demos
- [Azure DevOps Demo Generator 🌟](https://azuredevopsdemogenerator.azurewebsites.net/) Azure DevOps Demo Generator helps you create projects on your Azure DevOps Organization with pre-populated sample content that includes source code, work items, iterations, service endpoints, build and release definitions based on a template you choose. The purpose of this system is to simplify working with the [Azure Devops hands-on-labs 🌟](https://www.azuredevopslabs.com/), demos and other education material provided by the Microsoft Azure Marketing team.
- [Azure DevOps Demo Generator is now open source](https://devblogs.microsoft.com/devops/azure-devops-demo-generator-is-now-open-source/)
- [Get started creating and populating demo Azure DevOps Services projects](https://docs.microsoft.com/en-us/azure/devops/demo-gen/use-demo-generator-v2?view=azure-devops)
- [reddit.com: Automate Infrastructure Deployments on Microsoft Azure with Terraform and Jenkins](https://www.reddit.com/r/Terraform/comments/h0tdq3/automate_infrastructure_deployments_on_microsoft/)

## Google DevOps Demos
- [Terraform Automation Demo using Google Cloud Provider](https://github.com/TerraHubCorp/terraform-google-automation-demo)

### GitOps with Anthos Config Management 
- [Tutorial: Connect Amazon EKS and Azure AKS Clusters with Google Anthos](https://thenewstack.io/tutorial-connect-amazon-eks-and-azure-aks-clusters-with-google-anthos/)
- [Tutorial: GitOps in Multicluster Environments with Anthos Config Management](https://thenewstack.io/tutorial-gitops-in-multicluster-environments-with-anthos-config-management/)
- [Tutorial: Deploy Anthos Apps from GCP Marketplace into Amazon EKS Cluster](https://thenewstack.io/tutorial-deploy-anthos-apps-from-gcp-marketplace-into-amazon-eks-cluster/)

## Quarkus Demos
- [Develop and test a Quarkus client on Red Hat CodeReady Containers with Red Hat Data Grid 8.0](https://developers.redhat.com/blog/2020/06/19/develop-and-test-a-quarkus-client-on-red-hat-codeready-containers-with-red-hat-data-grid-8-0/)
- [aytartana.wordpress.com: Migrating SpringBoot PetClinic REST to Quarkus](https://aytartana.wordpress.com/2020/08/26/migrating-springboot-petclinic-rest-to-quarkus/)

## Kafka
- [medium: Setting up KafkaSource to send data and displayed with Knative event-display](https://medium.com/@jweng1/setting-up-kafkasource-to-send-data-and-displayed-with-knative-event-display-33891b253442)
- [towardsdatascience.com: Kafka, for your data pipeline? Why not?](https://towardsdatascience.com/kafka-for-your-data-pipeline-why-not-5a14b50efe7f)

## Apache Camel & ActiveMQ. Event driven integration
- [tomd.xyz: Event-driven integration on Kubernetes with Camel & KEDA](https://tomd.xyz/kubernetes-event-driven-keda/)

## Codeless
- [github.com/kelseyhightower/nocode](https://github.com/kelseyhightower/nocode)

## JBoss EAP 
- [developers.redhat.com: Red Hat JBoss Enterprise Application Platform expansion pack (JBoss EAP XP) 1.0 released](https://developers.redhat.com/blog/2020/06/17/red-hat-jboss-enterprise-application-platform-expansion-pack-1-0-released/) This version enables JBoss EAP developers to build [Java](https://developers.redhat.com/topics/enterprise-java/) microservices using Eclipse MicroProfile 3.3 APIs while continuing to also support Jakarta EE 8. 

## Terraform
- [terraform.collabnix.com](https://collabnix.github.io/terraform/) An Ultimate Terraform Hands-on Labs. Get access to 50+ tutorials around Terraform, Kubernetes & Cloud.
- [opensource.com: A guide to Terraform for Kubernetes beginners](https://opensource.com/article/20/7/terraform-kubernetes) Learn how to make a Minikube cluster and deploy to it with Terraform.
- [medium: Install Istio on Azure Kubernetes cluster using Terraform](https://medium.com/@vipinagarwal18/install-istio-on-azure-kubernetes-cluster-using-terraform-214f6d3f611)
- [brennerm.github.io: Setting up an EKS cluster with IAM/IRSA integration](https://brennerm.github.io/posts/setting-up-eks-with-irsa-using-terraform.html)
- [betterprogramming.pub: Create an Amazon EKS Fargate Cluster and Managed Node Group Using Terraform](https://betterprogramming.pub/with-latest-updates-create-amazon-eks-fargate-cluster-and-managed-node-group-using-terraform-bc5cfefd5773) Serverless clusters and HashiCorp’s Terraform on AWS
- [azapril.dev: Deploying a LogicApp with Terraform (Bonus: in an AzDO pipeline)](https://azapril.dev/2021/04/12/deploying-a-logicapp-with-terraform/)

## Prometheus and Grafana
- [docker-compose-tpg: Telegraf + Prometheus + Grafana Local Testing Environments](https://github.com/xiaopeng163/docker-compose-tpg) Setup learning environment for Telegraf, Prometheus and Grafana with docker-compose. (include SNMP simulators).

## GitHub Actions
- [linkedin: Test Automation - How To Build a CI/CD Pipeline Using Pytest and GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-build-cicd-pipeline-using-pytest-nir-tal/)

### RedHat GitHub Actions
- [redhat-actions/spring-petclinic](https://github.com/redhat-actions/spring-petclinic)

## Red Hat Process Automation Manager
- [gitlab.com: Red Hat Process Automation Manager - Signal Marketing Demo](https://gitlab.com/bpmworkshop/rhpam-signal-marketing-demo)

## API Testing and Postman
- [developers.redhat.com: Automated API testing for the KIE Server](https://developers.redhat.com/blog/2020/05/01/automated-api-testing-for-the-kie-server/)
- [github.com/microsoft/azure-digital-twins-postman-samples](https://github.com/microsoft/azure-digital-twins-postman-samples) The repo contains a single postman_collection.json file that contains a postman collection of requests to the Azure Digital Twins APIs. Currently the focus of the collection is on on the data plan and includes Models, Query, and Twins.

## Serverless
- [sitepoint.com: A Guide to Serverless Functions and How to Deploy Them](https://www.sitepoint.com/gatsby-mdx-blog/)