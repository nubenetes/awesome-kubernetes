# Managed Kubernetes in Public Cloud

1. [Introduction](#introduction)
2. [Terraform Kubernetes Boilerplates](#terraform-kubernetes-boilerplates)
3. [GKE vs EKS vs AKS](#gke-vs-eks-vs-aks)
4. [Other Managed Kubernetes](#other-managed-kubernetes)
5. [AWS EKS (Hosted/Managed Kubernetes on AWS)](#aws-eks-hostedmanaged-kubernetes-on-aws)
    1. [EKS Upgrades](#eks-upgrades)
    2. [EKS and IaC with Crossplane](#eks-and-iac-with-crossplane)
    3. [AWS EKS Vs ECS Vs Fargate](#aws-eks-vs-ecs-vs-fargate)
    4. [EKS Anywhere (on premises)](#eks-anywhere-on-premises)
    5. [EKS Distro (EKS-D)](#eks-distro-eks-d)
    6. [Testing Kubernetes Canary deployment on EKS](#testing-kubernetes-canary-deployment-on-eks)
6. [AKS Azure Kubernetes Service](#aks-azure-kubernetes-service)
    1. [AKS Releases](#aks-releases)
    2. [AKS Lite](#aks-lite)
    3. [Draft 2 on AKS](#draft-2-on-aks)
7. [GKE Google Kubernetes Engine](#gke-google-kubernetes-engine)
8. [IKS IBM Cloud Kubernetes Service](#iks-ibm-cloud-kubernetes-service)
9. [Linode Kubernetes Engine LKE](#linode-kubernetes-engine-lke)
10. [DOKS Digital Ocean Kubernetes](#doks-digital-ocean-kubernetes)
11. [Oracle Cloud Kubernetes](#oracle-cloud-kubernetes)
12. [Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes](#provisioning-cloud-resources-aws-gcp-azure-in-kubernetes)
13. [Kubesphere](#kubesphere)
14. [Giant Swarm](#giant-swarm)
15. [Tools for multi-cloud Kubernetes management](#tools-for-multi-cloud-kubernetes-management)
16. [Videos](#videos)
17. [Tweets](#tweets)

## Introduction

- [infoworld.com: 6 reasons to switch to managed Kubernetes](https://www.infoworld.com/article/3614605/6-reasons-to-switch-to-managed-kubernetes.html) Managed Kubernetes services have matured to the point where many enterprises are handing over the keys to their clusters. Here we identify some of the main drivers behind that trend.
- [Allocatable memory and CPU in Kubernetes Nodes 🌟](https://learnk8s.io/allocatable-resources) Not all CPU and memory in your Kubernetes nodes can be used to run Pods. In this article, you will learn how managed Kubernetes Services such AKS, EKS and GKE reserve resources for workloads, operating systems, daemons and Kubernetes agent.
- [==armosec.io: Which Managed Kubernetes Is Right for Me?==](https://www.armosec.io/blog/which-managed-kubernetes-is-right-for-me) This blog will compare on-premises, or self-hosted,Kubernetes clusters to managed ones, as well as outline your options for Kubernetes in the cloud
- [==infoworld.com: CNCF survey: Managed Kubernetes becomes the norm==](https://www.infoworld.com/article/3649710/cncf-survey-managed-kubernetes-becomes-the-norm.html) Cloud Native Computing Foundation’s latest survey shows that container and Kubernetes usage continues to rise, as managed services ease the operational burden on their teams.
- [redhat.com: What architects need to know about managed Kubernetes](https://www.redhat.com/architect/managed-kubernetes) Should you assemble your own Kubernetes stack or adopt a managed platform such as Red Hat OpenShift? Evaluate the differences.
- [dev.to/thenjdevopsguy: AKS vs EKS vs GKE](https://dev.to/thenjdevopsguy/aks-vs-eks-vs-gke-2459)

{==

## Terraform Kubernetes Boilerplates

- [Terraform Kubernetes Boilerplates 🌟](terraform.md)

==}

## GKE vs EKS vs AKS

- [medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS](https://medium.com/@Platform9Sys/kubernetes-cloud-services-comparing-gke-eks-and-aks-1fe42770cad3)
- [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.com/post/2020/02/eks-vs-gke-vs-aks/)
- [youtube: Kubernetes Comparison](https://www.youtube.com/watch?v=xM9jpcVGTzY) A beautiful comparison of Kubernetes Services from GCP, AWS and Azure by learnk8s.
    - [learnk8s.io/research:  Comparison of Kubernetes managed services 🌟](https://learnk8s.io/research)
- [medium: State of Managed Kubernetes 2020](https://medium.com/swlh/state-of-managed-kubernetes-2020-4be006643360) EKS vs. AKS vs. GKE from a Developer’s Perspective
- [medium: Managed Kubernetes Services Compared: GKE vs. EKS vs. AKS](https://medium.com/better-programming/managed-kubernetes-services-compared-gke-vs-eks-vs-aks-df1ecb22bba0) Comparing the three most popular managed Kubernetes platforms in features and overall experience.
- [acloudguru.com: AKS vs EKS vs GKE: Managed Kubernetes services compared](https://acloudguru.com/blog/engineering/aks-vs-eks-vs-gke-managed-kubernetes-services-compared)

## Other Managed Kubernetes

- [thenewstack.io: Otomi Container Platform Offers an Integrated Kubernetes Bundle](https://thenewstack.io/otomi-container-platform-offers-an-integrated-kubernetes-bundle/) If you want to enjoy the benefits of Kubernetes, configuring and installing the software itself can be just the first of many deeply technical and oftentimes confusing steps. To simplify this, many major cloud providers offer managed Kubernetes services, but even then you may need to install secondary services to handle tasks such as tracing, logging, monitoring, identity access management, and so on. The Otomi Container Platform looks to address this complexity by bundling together more than 30 different Kubernetes add-ons, as well as providing what it calls an “OSX like interface,” and today the project has open sourced a community edition under the Apache 2.0 license.
    - [otomi.io 🌟](https://otomi.io/)
    - [==github: Otomi==](https://github.com/redkubes/otomi-core) GitOps powered K8s app suite with developer self-service

## AWS EKS (Hosted/Managed Kubernetes on AWS)

- [community.aws/kubernetes](https://community.aws/kubernetes) Kubernetes at AWS! Welcome to the hub for all things Kubernetes at AWS.
- [dzone: kops vs EKS](https://dzone.com/articles/kops-vs-eks-a-comparison-guide)
- [udemy.com: amazon eks starter kubernetes on aws](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws/)
- [eksctl: EKS installer](https://github.com/weaveworks/eksctl)
    - [medium.com/@thapliyal705: Create Amazon EKS Cluster from scratch using eksctl](https://medium.com/@thapliyal705/create-amazon-eks-cluster-from-scratch-using-eksctl-67e0d0900245)
- [medium: Implementing Kubernetes Cluster using AWS EKS (AWS Managed Kubernetes)](https://medium.com/@devopsadvocate/how-to-setup-kubernetes-cluster-using-aws-eks-aws-managed-kubernetes-181d5567a8ef)
- [Amazon EKS Security Best Practices](https://www.stackrox.com/post/2019/09/amazon-eks-security-best-practices/)
- [thenewstack.io: Install and Configure OpenEBS on Amazon Elastic Kubernetes Service](https://thenewstack.io/tutorial-install-and-configure-openebs-on-amazon-elastic-kubernetes-service/)
- [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS 🌟](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks/)
- [magalix.com: Deploying Kubernetes Cluster With EKS 🌟](https://www.magalix.com/blog/deploying-kubernetes-cluster-with-eks) Fargate Deployment vs. Linux Workload
- [Deploying Infrastructure (FrontEnd + BackEnd) on AWS using Amazon EKS](https://medium.com/@ghumare64/deploying-infrastructure-frontend-backend-on-aws-using-amazon-eks-5f1f426d618e)
- [EKS Service Accounts Explained](https://fika.works/blog/eks-service-accounts/) In AWS you can assign IAM permissions to pods in your cluster. This article explains how it works.
- [medium: Building the CI/CD of the Future, Creating the EKS Cluster 🌟](https://medium.com/swlh/building-the-ci-cd-of-the-future-creating-the-eks-cluster-e4cce4eb3500)
- [Announcing the AWS Controllers for Kubernetes Preview](https://aws.amazon.com/about-aws/whats-new/2020/08/announcing-the-aws-controllers-for-kubernetes-preview/)
- [daveops.xyz: Administrar usuarios en EKS](https://daveops.xyz/2020/08/25/administrar-usuarios-en-eks/)
- [aws.github.io: AWS Controllers for Kubernetes](https://aws.github.io/aws-controllers-k8s/)
- [stacksimplify.com: AWS ALB Ingress Service - Basics 🌟](https://www.stacksimplify.com/aws-eks/aws-alb-ingress/lean-kubernetes-aws-alb-ingress-basics/)
- [Kubernetes PVCs with EFS provisioner](https://www.padok.fr/en/blog/efs-provisioner-kubernetes)
- [Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
- [Running spot instances effectively with Amazon EKS](https://m.signalvnoise.com/running-spot-instances-effectively-with-amazon-eks)
- [medium: Designing a Kubernetes Cluster with Amazon EKS From Scratch 🌟](https://medium.com/adobetech/designing-a-kubernetes-cluster-with-amazon-eks-from-scratch-4b4ee9d1b8f)
- [en.sokube.ch: AWS + Kubernetes = AWS Elastic Kubernetes Service (EKS) 🌟](https://en.sokube.ch/post/aws-kubernetes-aws-elastic-kubernetes-service-eks)
- [aws.amazon.com: Operating a multi-regional stateless application using Amazon EKS](https://aws.amazon.com/blogs/containers/operating-a-multi-regional-stateless-application-using-amazon-eks/)
- [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform 🌟](https://www.clickittech.com/aws/amazon-ecs-vs-eks/)
- [POKE - Provision Opinionated Kubernetes on EKS](https://github.com/bit-cloner/poke) Poke is infrastructure as software to provision EKS cluster in an opinianated way. Code is written in nodejs utilising pulumi framework. It is opinionated in such a way to improve security and simplicity.Consider this similar to terraform module. This package can be used to provision eks clusters declaratively with immutability and repeatability.
- [clickittech.com: Kubernetes Multi tenancy with Amazon EKS: Best practices and considerations](https://www.clickittech.com/saas/kubernetes-multi-tenancy/)
- [automateinfra.com: Getting Started with Amazon Elastic kubernetes Service (AWS EKS)](https://automateinfra.com/2021/04/01/the-only-ultimate-for-beginners-getting-started-with-amazon-eks/)
- [medium: Run Kubernetes Production Environment on EC2 Spot Instances With Zero Downtime: A Complete Guide](https://medium.com/riskified-technology/run-kubernetes-on-aws-ec2-spot-instances-with-zero-downtime-f7327a95dea)
- [releaseops.io: Scaling Kubernetes Deployments in AWS with Container Insights Metrics](https://releaseops.io/blog/scaling-kubernetes-deployments-in-aws-with-container-insights-metrics)
- [medium: Create Kubernetes Cluster On AWS EKS](https://medium.com/codex/create-kubernetes-cluster-on-aws-eks-6ced4c488e62) Setup AWS credentials and install kubectl, eksctl on Ubuntu. Create Kubernetes cluster using eksctl.
- [Amazon EKS Price Reduction](https://aws.amazon.com/blogs/aws/eks-price-reduction/)
- [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS 🌟](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks/)
- [Amazon EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/)
- [info.acloud.guru: Scaling the hottest app in tech on AWS and Kubernetes](https://info.acloud.guru/resources/kubernetes-aws-cloud-scaling-hey)
- [itnext.io: Using AWS NLB manually targeting an EKS Service exposing UDP traffic](https://itnext.io/using-aws-nlb-manually-targeting-an-eks-service-exposing-udp-traffic-17053ecd8f52)
- [Amazon EKS Now Supports EC2 Inf1 Instances](https://aws.amazon.com/blogs/aws/amazon-eks-now-supports-ec2-inf1-instances/)
- [Create a pipeline with canary deployments for Amazon EKS with AWS App Mesh 🌟](https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-eks-with-aws-app-mesh/)
- [medium: Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
- [linkedin.com: Amazon EKS Distro (EKS-D): The Kubernetes Distribution Used by Amazon EKS 🌟](https://www.linkedin.com/pulse/amazon-eks-distro-eks-d-kubernetes-distribution-used-gokul-chandra/)
- [aws.amazon.com: Introducing Federated Amazon EKS Clusters on AWS](https://aws.amazon.com/about-aws/whats-new/2021/01/introducing-federated-amazon-eks-clusters-aws/)
- [medium: How to Deploy an EKS stack in AWS?](https://medium.com/avmconsulting-blog/how-to-deploy-an-eks-stack-to-kubernetes-aws-5ec9c5a07247)
- [aws.amazon.com: Fluent Bit Integration in CloudWatch Container Insights for EKS](https://aws.amazon.com/blogs/containers/fluent-bit-integration-in-cloudwatch-container-insights-for-eks/)
- [Optimizing Your Kubernetes Clusters with Rancher and Amazon EKS 🌟](https://aws.amazon.com/blogs/apn/optimizing-your-kubernetes-clusters-with-rancher-and-amazon-eks/)
- [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform 🌟](https://www.clickittech.com/aws/amazon-ecs-vs-eks/)
- [faun.pub: Upgrading and Scaling Kubernetes cluster in AWS](https://faun.pub/upgrading-and-scaling-kubernetes-cluster-in-aws-6971b3936465)
- [youtube/StackSimplify: Kubernetes Deployments on AWS EKS | Amazon Elastic Kubernetes Service | Amazon EKS 🌟](https://www.youtube.com/watch?v=vZK_W-fpft0&ab_channel=StackSimplify)
- [cloudify.co: Simplifying Hybrid Cloud Deployments With AWS EKS And Outpost](https://cloudify.co/blog/simplifying-hybrid-cloud-deployments-with-aws-eks-and-outpost)
- [eksworkshop.com 🌟](https://www.eksworkshop.com/)
- [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes/)
- [cast.ai: 8 best practices to reduce your AWS bill for Kubernetes](https://cast.ai/blog/8-best-practices-to-reduce-your-aws-bill-for-kubernetes)
- [aws whitepapers: Architecting Amazon EKS for PCI DSS Compliance (pdf) 🌟🌟](https://d1.awsstatic.com/whitepapers/architecting-amazon-eks-for-pci-dss-compliance.pdf)
- [==github.com/aws/eks-charts== 🌟](https://github.com/aws/eks-charts) Amazon EKS Helm chart repository
- [AWS Load Balancer Controller 🌟](https://kubernetes-sigs.github.io/aws-load-balancer-controller)
    - [Setup External DNS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/integrations/external_dns/)
- [particule.io: Create Kubernetes federated clusters on AWS](https://particule.io/en/blog/aws-federated-eks/)
- [==aws.github.io/aws-eks-best-practices== 🌟](https://aws.github.io/aws-eks-best-practices/) __The primary goal of this project is to offer a set of best practices for day 2 operations for Amazon EKS.__
    - [aws.github.io/aws-eks-best-practices: Networking in EKS](https://aws.github.io/aws-eks-best-practices/reliability/docs/networkmanagement)
- [betterprogramming.pub: Amazon EKS Is Eating My IPs!](https://betterprogramming.pub/amazon-eks-is-eating-my-ips-e18ea057e045) Understand how AWS EKS manages IP addresses and what you can do about it
- [engineering.salesforce.com: Optimizing EKS networking for scale](https://engineering.salesforce.com/optimizing-eks-networking-for-scale-1325706c8f6d)
- [blog.usejournal.com: Spice up Your Kubernetes Environment with AWS Lambda 🌟](https://blog.usejournal.com/spice-up-your-kubernetes-environment-with-aws-lambda-a07d81347607) In this blog you will learn a simple yet effective and secure way to integrate AWS Lambda with an existing Kubernetes environment without codes changes.
- [azon EKS Pod Identity Webhook](https://github.com/aws/amazon-eks-pod-identity-webhook) Amazon EKS Pod Identity Webhook
- [Chaos engineering on Amazon EKS using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/devops/chaos-engineering-on-amazon-eks-using-aws-fault-injection-simulator/)
- [pages.awscloud.com: GitOps on AWS for High Performing Team Operations (eBook)](https://pages.awscloud.com/GLOBAL-partner-DL-DevOps-weaveworks-ebook-2020-learn.html) Realize the full value of Kubernetes by leveraging GitOps to manage operational complexity
- [thenewstack.io: Deploy Gremlin to Amazon EKS Using AWS CloudFormation](https://thenewstack.io/deploy-gremlin-to-amazon-eks-using-aws-cloudformation/)
- [aws.amazon.com: Easy as one-two-three policy management with Kyverno on Amazon EKS 🌟](https://aws.amazon.com/blogs/containers/easy-as-one-two-three-policy-management-with-kyverno-on-amazon-eks/)
- [nextlinklabs.com: Handling Auth in EKS Clusters: Setting Up Kubernetes User Access Using AWS IAM](https://nextlinklabs.com/insights/handling-authentication-in-EKS-clusters-kubernetes-AWS-IAM)
- [neal-davis.medium.com: ECS vs EC2 vs Lambda 🌟](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)
- [faun.pub: Kubernetes Multi-tenancy with Amazon EKS: Best practices and considerations 🌟](https://faun.pub/kubernetes-multi-tenancy-with-amazon-eks-best-practices-and-considerations-60bfd78c2f9a)
- [nginx.com: Deploying NGINX Ingress Controller on Amazon EKS: How We Tested](https://www.nginx.com/blog/deploying-nginx-ingress-controller-on-amazon-eks-how-we-tested)
- [hackerxone.com: 13 Steps Guide to Create Kubernetes Cluster on AWS](https://www.hackerxone.com/2021/08/20/13-steps-guide-to-create-kubernetes-cluster-on-amazon-web-serviceaws/)
- [hackerxone.com: Steps to Create Amazon EKS node group on Amazon web Service (AWS)](https://www.hackerxone.com/2021/08/25/steps-to-create-amazon-eks-node-group-on-amazon-web-service-aws/)
- [dev.to: EKS IAM Deep Dive 🌟](https://dev.to/aws-builders/eks-iam-deep-dive-136d)
- [aws.plainenglish.io: 6 Tips to Improve Availability with AWS Load Balancers and Kubernetes](https://aws.plainenglish.io/6-tips-to-improve-availability-with-aws-load-balancers-and-kubernetes-ad8d4d1c0f61)
- [aws.amazon.com: Using Prometheus Adapter to autoscale applications running on Amazon EKS](https://aws.amazon.com/blogs/mt/automated-scaling-of-applications-running-on-eks-using-custom-metric-collected-by-amazon-prometheus-using-prometheus-adapter/)
- [youtube: CloudGeeks - Terraform Eks Kubernetes RDS Secrets Manager Eksctl Cloudformation ALB Controller (Redmine App)](https://www.youtube.com/watch?v=OFZYIr66Ku4&ab_channel=cloudgeeksinc) - [quickbooks2018/eks-redmin](https://github.com/quickbooks2018/eks-redmin)
- [aws.amazon.com: Kubernetes Ingress with AWS ALB Ingress Controller](https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/)
- [automateinfra.com: The Ultimate Guide on AWS EKS for Beginners (Easiest Way)](https://automateinfra.com/2021/10/19/the-ultimate-guide-on-aws-eks-for-beginners-easiest-way/)
- [==aws/aws-node-termination-handler== 🌟](https://github.com/aws/aws-node-termination-handler) Gracefully handle EC2 instance shutdown within Kubernetes
- [==howtoforge.com: How to Create a Kubernetes Cluster with AWS CLI==](https://www.howtoforge.com/how-to-create-a-kubernetes-cluster-with-the-aws-cli/)
- [blog.searce.com: Optimise cost for AWS EKS cluster using Spotinst 🌟](https://blog.searce.com/optimize-cost-for-aws-eks-cluster-using-spotinst-ffcebe8e3571)
- [thenewstack.io: How We Built Preview Environments on Kubernetes and AWS](https://thenewstack.io/how-we-built-preview-environments-on-kubernetes-and-aws/)
- [aws.amazon.com: Mount Amazon EFS file systems cross-account from Amazon EKS, and utilize AWS Organizations more effectively](https://aws.amazon.com/blogs/storage/mount-amazon-efs-file-systems-cross-account-from-amazon-eks)
- [==Onfido’s Journey to a Multi-Cluster Amazon EKS Architecture==](https://aws.amazon.com/blogs/containers/onfidos-journey-to-a-multi-cluster-amazon-eks-architecture/) In this article, you will learn how moving to an active/active cluster architecture has allowed Onfido to shift traffic away from an Amazon EKS cluster when performing infrastructure maintenance.
- [medium.com/@abhinav.ittekot: Granting IAM permissions to pods in EKS using OIDC](https://medium.com/@abhinav.ittekot/granting-iam-permissions-to-pods-in-eks-using-oidc-f2044c88a53)
- [medium.com/@ishana98dadhich: Integrating AWS Secret Manager with EKS and use Secrets inside the Pods: Part-1](https://medium.com/@ishana98dadhich/integrating-aws-secret-manager-with-eks-and-use-secrets-inside-the-pods-part-1-1938b0c3c2fb) This blog provides you enough details on how you can use secrets (managed by AWS Secrets Manager) inside AWS EKS pods.
- [medium.com/@radha.sable25: Enabling IAM users/roles Access on Amazon EKS cluster](https://medium.com/@radha.sable25/enabling-iam-users-roles-access-on-amazon-eks-cluster-f69b485c674f)
- [aws.amazon.com: Continuous Delivery of Amazon EKS Clusters Using AWS CDK and CDK Pipelines](https://aws.amazon.com/blogs/containers/continuous-delivery-of-amazon-eks-clusters-using-aws-cdk-and-cdk-pipelines)
- [medium.com/avmconsulting-blog: Installing Vault On EKS With TLS And Persistent Storage](https://medium.com/avmconsulting-blog/installing-vault-on-eks-with-tls-and-persistent-storage-98254b4150f3)
- [dzone.com: How to Use AWS IAM Role on AWS EKS PODs 🌟](https://dzone.com/articles/how-to-use-aws-iam-role-on-aws-eks-pods) A native-AWS way to attach an IAM role into the Kubernetes POD, without third-party software, reducing latency and improving your EKS security.
- [aws.amazon.com: Troubleshooting Amazon EKS API servers with Prometheus](https://aws.amazon.com/de/blogs/containers/troubleshooting-amazon-eks-api-servers-with-prometheus/)
- [AWS Controllers for Kubernetes (ACK) 🌟](https://github.com/aws-controllers-k8s/community) AWS Controllers for Kubernetes (ACK) lets you define & use AWS service resources directly from Kubernetes. With ACK, you can take advantage of AWS managed services for your applications without needing to define resources outside of the cluster.
- [itnext.io: Deploy Kubernetes (K8s) on Amazon AWS using mixed on-demand and spot instances 🌟](https://itnext.io/deploy-kubernetes-k8s-on-amazon-aws-using-mixed-on-demand-and-spot-instances-5440e5bece7)
- [==github.com/awslabs: Kubernetes Migration Factory User Guide== 🌟](https://github.com/awslabs/aws-kubernetes-migration-factory) **Kubernetes Migrations Factory (KMF) is a tool developed for migrating docker containers to Amazon EKS.  The Kubernetes Migration Factory solution is an orchestration platform for migrating containers to Amazon EKS at scale.**
- [==github.com/aws-ia/terraform-aws-eks-blueprints (examples) 🌟🌟🌟==](https://github.com/aws-ia/terraform-aws-eks-blueprints/tree/main/examples)
    - [Direction for v5 of Terraform EKS Blueprints](https://github.com/aws-ia/terraform-aws-eks-blueprints/blob/main/docs/v4-to-v5/motivation.md)
- [akintola-lonlon.medium.com: AWS Kubernetes: The #1 Rule You Need To Master Before Going To Production.](https://akintola-lonlon.medium.com/aws-kubernetes-the-1-rule-you-need-to-master-before-going-to-production-628b75ba1b6a) This is the most important thing to consider before going to production on EKS.
- [amod-kadam.medium.com: Are there two Load Balancer Controllers with EKS? 🌟](https://amod-kadam.medium.com/are-there-two-load-balancer-controllers-with-eks-8a7b04db8c93) In this article, you will learn how AWS provision different types of load balancers (Classic vs Network) to expose your applications depending on the annotations that you use.
- [aws.amazon.com: Streaming Kubernetes Events in Slack](https://aws.amazon.com/blogs/containers/streaming-kubernetes-events-in-slack/) This post describes how you can send events from your Kubernetes cluster to a Slack channel using BotKube, a messaging bot for monitoring and debugging Kubernetes clusters.
- [joachim8675309.medium.com: ExternalDNS with EKS and Route53](https://joachim8675309.medium.com/externaldns-with-eks-and-route53-90aa23fa3aba) After deploying a web app on Kubernetes, you might need to update the DNS records. ExternalDNS can automate this process and this tutorial demonstrates how to set up and configure this on Amazon EKS using Amazon Route 53 DNS zones.
- [==aws-quickstart/cdk-eks-blueprints: Amazon EKS Blueprints for CDK==](https://github.com/aws-quickstart/cdk-eks-blueprints) **This repository contains the source code for the eks-blueprints NPM module that can be used to configure and manage complete EKS clusters that are fully bootstrapped with the operational software that is needed to deploy and operate workloads**
- [dev.to: One technique to save your AWS EKS IP addresses 10x](https://dev.to/timtsoitt/one-technique-to-save-your-aws-eks-ip-addresses-10x-2ocn) To increase the number of available IP addresses in your EKS cluster you can:
    - Assign address prefixes to your ENI and
    - Enable the CNI custom networking feature
- [aws.amazon.com: Autoscaling EKS on Fargate with custom metrics](https://aws.amazon.com/blogs/containers/autoscaling-eks-on-fargate-with-custom-metrics/) What follows is a step-by-step guide on configuring the Horizontal Pod Autoscaler with metrics provided by Prometheus to automatically scale pods running on Amazon EKS on AWS Fargate.
    - Autoscaling is an approach to automatically scale up or down workloads based on the resource usage. In Kubernetes, the Horizontal Pod Autoscaler (HPA) can scale pods based on observed CPU utilization and memory usage. Starting with Kubernetes 1.7, an aggregation layer was introduced that allows third-party applications to extend the Kubernetes API by registering themselves as API add-ons. Such an add-on can implement the Custom Metrics API and enable HPA access to arbitrary metrics. What follows is a step-by-step guide on configuring HPA with metrics provided by Prometheus to automatically scale pods running on Amazon EKS on AWS Fargate.
- [==opssorry.substack.com: GitOps: A Simple Approach to using AWS Secrets Manager with Kubernetes== 🌟](https://opssorry.substack.com/p/gitops-a-simple-approach-to-using)
- [==aws.github.io/aws-eks-best-practices: Amazon EKS Best Practices Guides== 🌟🌟🌟](https://aws.github.io/aws-eks-best-practices/networking/index/) **Welcome to the EKS Best Practices Guides. The primary goal of this project is to offer a set of best practices for day 2 operations for Amazon EKS. We elected to publish this guidance to GitHub so we could iterate quickly, provide timely and effective recommendations for variety of concerns, and easily incorporate suggestions from the broader community.**
    - [==Amazon EKS Best Practices Guide for Networking==](https://aws.github.io/aws-eks-best-practices/networking/index/) Intro to Amazon VPC Container Network Interface (VPC CNI) in the context of Kubernetes cluster networking. VPC CNI is the default networking plugin supported by EKS. The VPC CNI is highly configurable to support different use cases.
- [medium.com/@chandranathmondal: ==Self-service Amazon EKS Cluster provisioning with Kubernetes configuration applied== 🌟](https://medium.com/@chandranathmondal/self-service-amazon-eks-cluster-provisioning-with-kubernetes-configuration-applied-372bce839d7)
- [AWS and Kubecost collaborate to deliver cost monitoring for EKS customers](https://aws.amazon.com/blogs/containers/aws-and-kubecost-collaborate-to-deliver-cost-monitoring-for-eks-customers/)
- [eng.grip.security: Enabling AWS IAM Group Access to an EKS Cluster Using RBAC](https://eng.grip.security/enabling-aws-iam-group-access-to-an-eks-cluster-using-rbac) There is no standardized method for providing IAM group access to an EKS cluster or namespace. In this article, you will learn how you can use an IAM role to authenticate the user group automatically and transparently when kubectl is being used.
- [medium.com/@andriikrymus: DNS config for EKS](https://medium.com/@andriikrymus/dns-config-for-eks-61eb70c3e31e) Elastic Kubernetes Service provide coredns add-on for k8s. Unfortunately, this add-on lucks of configuration options (for example, nodeSelector). In this article, you will learn how to patch it, and configure it the way you want it.
- [cast.ai: EKS Security Checklist: 10 Best Practices for a Secure Cluster](https://cast.ai/blog/eks-security-checklist-10-best-practices-for-a-secure-cluster/)
- [==github.com/kubernetes-sigs/aws-load-balancer-controller==](https://github.com/kubernetes-sigs/aws-load-balancer-controller) AWS Load Balancer Controller is a controller to help manage Elastic Load Balancers for a Kubernetes cluster. It satisfies:
    - Ingress resources by provisioning Application Load Balancers
    - Service resources by provisioning Network Load Balancers
- [thenewstack.io: Amazon Web Services Gears Elastic Kubernetes Service for Batch Work](https://thenewstack.io/amazon-web-services-gears-elastic-kubernetes-service-for-batch-jobs/) AWS Batch is ideal for developers looking for a more simplified workflow when it comes to managing Kubernetes clusters and pods to use with their batch jobs.
- [silvr.medium.com: Using Kyverno To Enforce AWS Load Balancer Annotations For Centralized Logging To S3](https://silvr.medium.com/using-kyverno-to-enforce-aws-load-balancer-annotations-for-centralized-logging-to-s3-af5dc1f1f3e0) In this tutorial, you'll learn how to use Kyverno to automatically configure annotations that enable access logs for an AWS Network Load Balancer (NLB) to be forwarded to an S3 bucket for a service of type `LoadBalancer`.
- [blog.jimmyray.io: Kubernetes Workload Identity with AWS SDK for Go v2](https://blog.jimmyray.io/kubernetes-workload-identity-with-aws-sdk-for-go-v2-927d2f258057) Using AWS SDK for Go v2 and AWS IAM Roles for Service Accounts. In this article, you'll learn how to use the AWS SDK for Go v2 and AWS IAM Roles for Service Accounts to grant permissions to access AWS services from wuthin Kubernetes
- [github.com/rebataur/djkube](https://github.com/rebataur/djkube) Tool for Django Developers to setup full stack EKS Kubernetes with all necessary tools including DevSecOps in 40 minutes. If you are a Python Django developer then djkube provides you with best user experience in easily running your full-stack Django apps on Kubernetes in AWS with just a few clicks.
- [==aws.amazon.com: Troubleshooting Amazon EKS API servers with Prometheus and Grafana==](https://aws.amazon.com/blogs/containers/troubleshooting-amazon-eks-api-servers-with-prometheus/)
- [medium.com/geekculture: EKS — Kubernetes — Not Ready nodes](https://medium.com/geekculture/eks-kubernetes-not-ready-nodes-dafb300ed299) Today I’m going to talk about an issue that I encounter a couple of days ago while working on EKS 1.21.
- [==faun.pub: How to access AWS services from EKS==](https://faun.pub/how-to-access-aws-services-from-eks-ab5fa003a1b6) Solutions to access AWS APIs from Kubernetes
- [aws.amazon.com: Persistent storage for Kubernetes](https://aws.amazon.com/blogs/storage/persistent-storage-for-kubernetes/)
- [aws.amazon.com: Machine Learning with Kubeflow on Amazon EKS with Amazon EFS](https://aws.amazon.com/blogs/storage/machine-learning-with-kubeflow-on-amazon-eks-with-amazon-efs/)
- [faun.pub: AWS EKS: The Ultimate Guide To Deploy AWS Load Balancer Controller add-on](https://faun.pub/aws-eks-the-ultimate-guide-to-deploy-an-ingress-controller-on-kubernetes-5952cb27c067) In this article, you'll learn how to set up an Ingress Controller on EKS in 5 steps:
    - Creating a cluster with EKSctl
    - Creating the IAM OIDC provider
    - Creating an IAM Policy
    - Creating the Role
    - Installing the ALB Ingress controller
- [==medium.com/@ankit.wal: Understanding IAM roles for service accounts, IRSA, on AWS EKS==](https://medium.com/@ankit.wal/the-how-of-iam-roles-for-service-accounts-irsa-on-aws-eks-3d76badb8942) A simple visual explanation of how IRSA works to help you understand and remember. IRSA is the AWS EKS native way to allow applications running in EKS pods to access AWS API, using permissions configured in AWS IAM roles. It’s an improvement over the previous architecture of applications running in pods to use the IAM roles of the underlying EKS nodes. Being able to configure access to AWS API per service account tends towards the principle of least privilege, and more secure architecture.
- [blog.realvarez.com: Reduce Amazon EKS cost by scaling node groups to zero 🌟](https://blog.realvarez.com/reduce-amazon-eks-cost-by-scaling-node-groups-to-zero/) - [blog.devops.dev: Reduce Amazon EKS cost by scaling node groups to zero](https://blog.devops.dev/reduce-amazon-eks-cost-by-scaling-node-groups-to-zero-41dce9db50ef) Scaling down to zero can result in significant cost savings when you have workloads that don't run 24x7. In this tutorial, you'll learn how to do that with labels, taints, and the Cluster Autoscaler.
- [dev.to: Autoprovisioning NFS volumes in EKS with CDK](https://dev.to/memark/autoprovisioning-nfs-volumes-in-eks-with-cdk-4fn9)
- [levelup.gitconnected.com: Running Workflows on windows with Jenkins pipeline and Kubernetes](https://levelup.gitconnected.com/running-workflows-on-windows-with-jenkins-pipeline-and-kubernetes-52752a89a0e7)
- [nivogt.medium.com: Boost your Kubernetes cluster’s Autoscaler on AWS EKS with Karpenter](https://nivogt.medium.com/boost-your-kubernetes-clusters-autoscaler-on-aws-eks-with-karpenter-4d23955944f2)
- [awslabs/eks-node-viewer](https://github.com/awslabs/eks-node-viewer) eks-node-viewer is a tool for visualizing dynamic node usage within a cluster. It was originally developed as an internal tool at AWS for demonstrating consolidation with Karpenter.
- [towardsaws.com: Autoscale Kubernetes Metrics Server on Amazon EKS](https://towardsaws.com/autoscale-kubernetes-metrics-server-fa398f8a600a)
- [==aws-samples/hardeneks==](https://github.com/aws-samples/hardeneks) Runs checks to see if an EKS cluster follows EKS Best Practices.
- [faun.pub: Analyze AWS EKS Audit logs with Falco](https://faun.pub/analyze-aws-eks-audit-logs-with-falco-95202167f2e)
- [docs.aws.amazon.com: Managing Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html)
- [docs.aws.amazon.com: Access container applications privately on Amazon EKS using AWS PrivateLink and a Network Load Balancer](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-eks-using-aws-privatelink-and-a-network-load-balancer.html) AWS Prescriptive Guidance includes patterns for EKS.
- [aws.amazon.com: Addressing latency and data transfer costs on EKS using Istio](https://aws.amazon.com/blogs/containers/addressing-latency-and-data-transfer-costs-on-eks-using-istio/) In this blog, you will learn how to use Istio topology-aware routing to reduce latency and data transfer costs between EKS nodes deployed in different Availability Zones
- [aws.amazon.com: Addressing IPv4 address exhaustion in Amazon EKS clusters using private NAT gateways](https://aws.amazon.com/blogs/containers/addressing-ipv4-address-exhaustion-in-amazon-eks-clusters-using-private-nat-gateways/) This post highlights the advantages of implementing a network architecture with a private NAT Gateway to deploy an Amazon EKS cluster. This enables communication across Amazon EKS clusters deployed to VPCs with overlapping CIDRs.
- [hardiks.medium.com: Where should you manage your Kubernetes in 2023? Amazon ECS or EKS](https://hardiks.medium.com/where-should-you-manage-your-kubernetes-in-2023-amazon-ecs-or-eks-6f503e93f7a7)
- [awstip.com: Amazon Elastic Kubernetes Service (Amazon EKS) — The Only Resource Hub You Ever Need](https://awstip.com/amazon-elastic-kubernetes-service-amazon-eks-the-only-resource-hub-you-ever-need-3b802687df36) In this article, you will find a collection of links to learn and master Amazon EKS
- [awstip.com: Working The Amazon EKS Immersion Workshop — Chapter 1 — Deploying A Microservices Application In A Kubernetes Cluster](https://awstip.com/working-the-amazon-eks-immersion-workshop-chapter-1-deploying-a-microservices-application-in-a-9acae5df2f01) This 12-part series covers how to provision an EKS cluster, deploy apps, and route traffic into the cluster using Ingress and the AWS Load Balancer controller
- [Understanding and Cost Optimizing Amazon EKS Control Plane Logs](https://aws.amazon.com/blogs/containers/understanding-and-cost-optimizing-amazon-eks-control-plane-logs/)
- [itnext.io: Top 10 Ways to Protect EKS Workloads from Ransomware](https://itnext.io/top-10-ways-to-protect-eks-workloads-from-ransomware-ae96d1c1e839) Here are the top 10 things you should focus on to protect EKS workloads against ransomware and all intrusions
- [blog.antoinechoula.ga: Native EKS Ingress with AWS Load Balancer Controller](https://blog.antoinechoula.ga/native-eks-ingress-with-aws-load-balancer-controller) This tutorial will teach you how to install and configure the AWS Load Balancer Controller using Terraform and Helm. You will also learn how to manage multiple ingresses and secure the traffic with SSL/TLS
- [devopslearning.medium.com: Lesson learned while scaling Kubernetes cluster to 1000 pods in AWS EKS](https://devopslearning.medium.com/lesson-learned-while-scaling-kubernetes-cluster-to-1000-pods-in-aws-eks-d2d399152bc2) In this article, you will follow Prashant's journey in scaling EKS to 1000+ pods and learn how to overcome these challenges:
    - AWS resource limits
    - IP addresses exhaustion
    - Packets drop
    - Control plane performance issues
- [Scaling Amazon EKS and Cassandra Beyond 1,000 Nodes](https://aws.amazon.com/blogs/containers/scaling-amazon-eks-and-cassandra-beyond-1000-nodes/) This post described a concrete experiment to prove k8ssandra scalability on Amazon EKS. You will also find general performance and scaling configurations of Amazon EKS that enable customers to scale workloads while maintaining linear performance.
- [sitepoint.com: Getting Started With Kubernetes on AWS Tutorial (2023 Update)](https://www.sitepoint.com/kubernetes-aws-tutorial/)
- [medium.com: Saving costs in Google Kubernetes Engine using Spot VMs](https://medium.com/@vaibhav176/saving-costs-in-google-kubernetes-engine-using-spot-vms-2e6d0157815e)
- [medium.com/@benjamin.christmann_12432: Setting up your first EKS cluster on AWS: some practical tips](https://medium.com/@benjamin.christmann_12432/setting-up-your-first-eks-cluster-on-aws-some-practical-tips-60400963c588)
- [blog.ratnopamc.com: Reduce cross-AZ traffic costs on EKS using topology aware hints](https://blog.ratnopamc.com/reduce-cross-az-traffic-costs-on-eks-using-topology-aware-hints) Topology Aware Hints is a new feature in EKS that reduces data transfer costs by keeping traffic within the same availability zone. It uses Pod Topology Spread Constraints to spread Pods evenly onto multiple node topologies
- [itnext.io: Running resilient workloads in EKS using Spot instances](https://itnext.io/running-production-workloads-in-eks-using-spot-instances-fc6808a7b462) In this article, you will learn how giffgaff run all of their applications in an EKS cluster using 100% spot instances and what additional safeguards they put in place to improve reliability
- [Simplifying Amazon EBS volume migration and modification on Kubernetes using the EBS CSI Driver](https://aws.amazon.com/de/blogs/storage/simplifying-amazon-ebs-volume-migration-and-modification-using-the-ebs-csi-driver/)
- [Eliminate Kubernetes node scaling lag with pod priority and over-provisioning](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/) In this post, you'll learn how to over-provision the cluster worker nodes using dummy pods for quicker scaling. The dummy pods contain a pause container that is scheduled by the scheduler according to pod specifications' placements and CPU/memory.
- [==itnext.io: Efficient Kubernetes Cluster Deployment: Accelerating Setup with EKS Blueprints==](https://itnext.io/efficient-kubernetes-cluster-deployment-accelerating-setup-with-eks-blueprints-68324b582ec9)
- [medium.com/@danielresponda: Testing Spot Reclamation Mechanisms with AWS Node Termination Handler and Kubernetes Autoscaler](https://medium.com/@danielresponda/testing-spot-reclamation-mechanisms-with-aws-node-termination-handler-and-kubernetes-autoscaler-43194d05dae0) What happens if a spot instance is reclaimed, but no more capacity is available in the cluster? In this article, you will learn how to use the AWS Node Termination Handler with Kubernetes Autoscaler to handle spot reclamations seamlessly
- [Amazon EKS introduces EKS Pod Identity](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-eks-pod-identity)
- [itnext.io: AWS Elastic Kubernetes Service: RBAC Authorization via AWS IAM and RBAC Groups](https://itnext.io/aws-elastic-kubernetes-service-rbac-authorization-via-aws-iam-and-rbac-groups-7b70ded144b5)
- [medium.com/@leocherian: Simple CDK app to create EKS Cluster](https://medium.com/@leocherian/simple-cdk-app-to-create-eks-cluster-06f651a12ccd)
- [blog.clouddrove.com: AWS EKS Blue/Green Deployment with Best Practices](https://blog.clouddrove.com/aws-eks-blue-green-deployment-with-best-practices-99be4b7baa38)
- [devoriales.com: AWS EKS Secret Encryption: Securing Your EKS Secrets At Rest with AWS KMS](https://devoriales.com/post/329/aws-eks-secret-encryption-securing-your-eks-secrets-at-rest-with-aws-kms)
- [blog.stackademic.com: Create the AWS EKS Cluster with a Managed Node Group Using Custom Launch Templates](https://blog.stackademic.com/create-the-aws-eks-cluster-with-a-managed-node-group-using-custom-launch-templates-185744a0cc79)
- [blog.devops.dev: HACKING KUBERNETES in AWS](https://blog.devops.dev/hacking-kubernetes-in-aws-54f4681f1478) In this article, you'll learn how to secure EKS by intentionally attaching the wrong policies to pods and hacking the cluster. You will misconfigure AWS Identity and Access Management (IAM) roles for the service accounts (IRSA) feature
- [rahulbhatia1998.medium.com: Designing A Multi-Region Kubernetes Cluster For Disaster Recovery On AWS EKS](https://rahulbhatia1998.medium.com/designing-a-multi-region-kubernetes-cluster-for-disaster-recovery-on-aws-eks-0a0a98ad5854)
- [towardsaws.com: From Scratch to Production: Deploying EKS Clusters and Applications with CI/CD using Jenkins and Terraform](https://towardsaws.com/from-scratch-to-production-deploying-eks-clusters-and-applications-with-ci-cd-using-jenkins-and-f27d4686d5fe)
- [awstip.com: Per-pod PIDs limit on EKS](https://awstip.com/per-pod-pids-limit-on-eks-fe320638c7e9)
- [aws.amazon.com: Amazon EKS announces native support for autoscaling CoreDNS Pods](https://aws.amazon.com/about-aws/whats-new/2024/05/amazon-eks-native-support-autoscaling-coredns-pods/)
- [medium.com/ekino-france: Addressing private IPv4 shortage: 5 Strategies for Amazon EKS](https://medium.com/ekino-france/kubernetes-addressing-private-ipv4-shortage-5-strategies-for-amazon-eks-1dc3df270ed8) This article explores 5 strategies for addressing private IPv4 shortage in Amazon EKS. Strategies include tweaking VPC CNI settings, using subnet CIDR reservation, custom networking with internal SNAT, private NAT gateways, and transitioning to IPv6
- [aws.amazon.com: Start Pods faster by prefetching images](https://aws.amazon.com/blogs/containers/start-pods-faster-by-prefetching-images/)

### EKS Upgrades

- [Updating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/update-managed-node-group.html) amazon eks managed node groups now supports parallel node upgrades
- [==aws.amazon.com: Planning Kubernetes Upgrades with Amazon EKS==](https://aws.amazon.com/blogs/containers/planning-kubernetes-upgrades-with-amazon-eks/)
- [==repost.aws: How do I plan an upgrade strategy for an Amazon EKS cluster?==](https://repost.aws/knowledge-center/eks-plan-upgrade-cluster)
- [medium.com/scout24-engineering: How did we upgrade our EKS clusters from 1.15 to 1.22 without K8s knowledge?](https://medium.com/scout24-engineering/how-did-we-upgrade-our-eks-clusters-from-1-15-to-1-22-without-k8s-knowledge-2c96c1a94cc1)
- [marcincuber.medium.com: Amazon EKS Upgrade Journey From 1.24 to 1.25](https://marcincuber.medium.com/amazon-eks-upgrade-journey-from-1-24-to-1-25-e1bcccc2f384)

### EKS and IaC with Crossplane

- [==aws.amazon.com: GitOps model for provisioning and bootstrapping Amazon EKS clusters using Crossplane and Argo CD==](https://aws.amazon.com/blogs/containers/gitops-model-for-provisioning-and-bootstrapping-amazon-eks-clusters-using-crossplane-and-argo-cd/)
- [nivogt.medium.com: [IaC] Continuous Delivery with Crossplane and ArgoCD : how to automate the creation of AWS EKS clusters](https://nivogt.medium.com/iac-continuous-delivery-with-crossplane-and-argocd-how-to-automate-the-creation-of-aws-eks-1523ef0e0aa)

### AWS EKS Vs ECS Vs Fargate

- [cloudify.co: AWS EKS Vs. ECS Vs. Fargate: The Breakdown](https://cloudify.co/blog/aws-eks-vs-ecs-vs-fargate/)

### EKS Anywhere (on premises)

- [EKS Anywhere: github.com/aws/eks-anywhere](https://github.com/aws/eks-anywhere) Run Amazon EKS on your own infrastructure
- [aws.amazon.com: Amazon EKS Anywhere – Now Generally Available to Create and Manage Kubernetes Clusters on Premises](https://aws.amazon.com/blogs/aws/amazon-eks-anywhere-now-generally-available-to-create-and-manage-kubernetes-clusters-on-premises/)
- [solo.io: Connect Your Services Seamlessly with Amazon EKS Anywhere and Istio](https://www.solo.io/blog/amazon-eks-anywhere-and-solo-istio/)
- [anywhere.eks.amazonaws.com: Compare EKS Anywhere and EKS](https://anywhere.eks.amazonaws.com/docs/concepts/eksafeatures/)
- [aws.amazon.com: Getting started with Amazon EKS Anywhere](https://aws.amazon.com/blogs/containers/introducing-general-availability-of-amazon-eks-anywhere/)
- [gokulchandrapr.medium.com: Amazon EKS Anywhere & EKS Connector](https://gokulchandrapr.medium.com/amazon-eks-anywhere-eks-connector-600953aaa42d)
- [ambar-thecloudgarage.medium.com: EKS Anywhere., decoding the architecture.](https://ambar-thecloudgarage.medium.com/eks-anywhere-decoding-the-architecture-fd2741b03e0a) In this article, you will take a deeper look into the EKS Anywhere architecture as well as compare it with EKS Distro. Then, you will discuss the different type of installations:
    - Standalone clusters
    - Distribute environments
- [blog.techknowtrendz.com: Taking Amazon EKS Anywhere for a spin](https://blog.techknowtrendz.com/taking-amazon-eks-anywhere-for-a-spin) Bringing EKS to a datacenter near you
- [rafay.co: Amazon EKS and EKS Anywhere – All You Need To Know](https://rafay.co/the-kubernetes-current/amazon-eks-and-eks-anywhere-all-you-need-to-know/) Take a look into both AmazonEKS and EKSAnywhere and how they are different. By the end of this post, you will be able to pick the right offering for your organization.
- [aws.amazon.com: Blue/Green Kubernetes upgrades for Amazon EKS Anywhere using Flux](https://aws.amazon.com/blogs/containers/blue-green-kubernetes-upgrades-for-amazon-eks-anywhere-using-flux/)

### EKS Distro (EKS-D)

- [==aws/eks-distro==](https://github.com/aws/eks-distro) Amazon EKS Distro (EKS-D) is a Kubernetes distribution based on and used by Amazon Elastic Kubernetes Service (EKS) to create reliable and secure Kubernetes clusters.

### Testing Kubernetes Canary deployment on EKS

- [medium: Kubernetes + EKS + Canary Deployment](https://medium.com/@jerome.decoster/kubernetes-eks-canary-deployment-1ef79ae89dfc)

## AKS Azure Kubernetes Service

- [learn.microsoft.com: Introduction to Kubernetes on Azure](https://learn.microsoft.com/en-us/training/paths/intro-to-kubernetes-on-azure)
- [==azure.github.io/AKS-Construction== 🌟](https://azure.github.io/AKS-Construction/) **AKS Construction Helper**
- [youtube: The AKS Community 🌟](https://www.youtube.com/@theakscommunity)
- [==the-aks-checklist.com: The Azure Kubernetes Service Checklist== 🌟🌟🌟](https://www.the-aks-checklist.com/) This checklist contains a large set of best practices and some of them may not be relevant to your context and thus the rating may be incorrect in your case. Please choose and apply them wisely.
- [Azure Updates AKS 🌟](https://azure.microsoft.com/en-us/updates/?query=AKS)
- [aks-learning.github.io/learningpath: AKS Learning Path](https://aks-learning.github.io/learningpath/)
- [docs.microsoft.com: Baseline architecture for an Azure Kubernetes Service (AKS) cluster 🌟](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks) In this reference architecture, you'll build a baseline infrastructure that deploys an AKS cluster. The article includes recommendations for networking, security, identity, management, and monitoring.
- [docs.microsoft.com: Microservices architecture on Azure Kubernetes Service (AKS) 🌟](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices) This reference architecture shows a microservices application deployed to Azure Kubernetes Service (AKS). It describes a basic AKS configuration that can be the starting point for most deployments. The architecture consists of the following components:
    - Azure Kubernetes Service (AKS)
    - Kubernetes cluster
    - Virtual network
    - Ingress
    - Azure Load Balancer
    - External data stores
    - Azure Active Directory
    - Azure Container Registry
    - Azure Pipelines
    - Helm
    - Azure Monitor
- [docs.microsoft.com: Use kubenet networking with your own IP address ranges in Azure Kubernetes Service (AKS) 🌟](https://docs.microsoft.com/en-us/azure/aks/configure-kubenet)
- [docs.microsoft.com: Configure Azure CNI networking in Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/configure-azure-cni)
- [trstringer.com: Run Kubernetes Pods on Specific VM Types in AKS](https://trstringer.com/run-kubernetes-pods-on-vm-types/)
- [docs.microsoft.com: AKS-managed Azure Active Directory integration](https://docs.microsoft.com/en-us/azure/aks/managed-aad)
- [==stacksimplify.com/azure-aks: Kubernetes On Cloud Roadmap==](https://stacksimplify.com/azure-aks/)
- [build5nines.com: Terraform: Create an AKS Cluster 🌟](https://build5nines.com/terraform-create-an-aks-cluster/)
- [github.com: AKS: Use AAD identity for pods and make your SecOps happy](https://github.com/dfrappart/articles/blob/master/podidentityjourney.md)
- [docs.microsoft.com: Microservices architecture on Azure Kubernetes Service (AKS) 🌟](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices)
- [techcommunity.microsoft.com: Containerize and migrate applications to AKS with the Azure Migrate’s new App Containerization tool](https://techcommunity.microsoft.com/t5/azure-migration/containerize-and-migrate-applications-to-aks-with-the-azure/ba-p/2178551)
- [mehmetozkaya.medium.com: Deploying .Net Microservices to Azure Kubernetes Services(AKS) and Automating with Azure DevOps](https://mehmetozkaya.medium.com/deploying-net-microservices-to-azure-kubernetes-services-aks-and-automating-with-azure-devops-c50bdd51b702)
- [faun.pub: How to implement Azure Kubernetes Service (AKS) in Cloud?](https://faun.pub/azure-kubernetes-service-aks-d1e71c7ecbe6)
- [adamrushuk.github.io: Increasing the volumeClaimTemplates Disk Size in a Statefulset on AKS](https://adamrushuk.github.io/increasing-the-volumeclaimtemplates-disk-size-in-a-statefulset-on-aks/)
- [nillsf.com: Running Windows containers on the Azure Kubernetes Service (AKS)](https://nillsf.com/index.php/2020/11/17/running-windows-containers-on-the-azure-kubernetes-service-aks)
- [itnext.io: Running Your Microservices Securely on AKS](https://itnext.io/running-your-microservices-securely-on-aks-417a110b2e76)
- [docs.microsoft.com: Create an HTTPS ingress controller on Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/ingress-tls)
- [blog.nillsf.com: Customize core dump in Azure Kubernetes](https://blog.nillsf.com/index.php/2020/12/06/customize-core-dump-in-azure-kubernetes/)
- [medium: Secure your Microservices on AKS — Part 1 🌟](https://itnext.io/running-your-microservices-securely-on-aks-417a110b2e76)
    - [medium: Secure your Microservices on AKS — Part 2 🌟](https://medium.com/microsoftazure/secure-your-microservices-on-aks-part-2-5496bf2ba00c)
- [zartis.com: How To Save A Fortune On Azure Kubernetes Service](https://www.zartis.com/minimizing-costs-aks/)
- [itnext.io: AKS Performance: Limit Ranges](https://itnext.io/aks-performance-limit-ranges-8e18cbebe351) Limit Ranges can be used to fine tune your resource consumption by limiting your min/max requests/limits in namespaces.
- [devoteam.com: Azure Kubernetes Service (AKS) with Azure DevOps](https://nl.devoteam.com/en/blog-post/azure-kubernetes-service-aks-with-azure-devops/)
- [itnext.io: Kubernetes Ingress on Azure using the Application Gateway](https://itnext.io/kubernetes-ingress-on-azure-using-the-application-gateway-2779b647deb5) How to expose multiple services on a single host
- [joachim8675309.medium.com: AKS with GRPC and ingress-nginx](https://joachim8675309.medium.com/aks-with-grpc-and-ingress-nginx-32481a792a1) Using GRPC with ingress-nginx add-on with AKS
- [thenewstack.io: Microsoft’s Practical Approach to Kubernetes Management](https://thenewstack.io/microsoft-takes-practical-approach-to-kubernetes-management/)
- [medium: AKS with Calico Network Policies](https://medium.com/geekculture/aks-with-calico-network-policies-8cdfa996e6bb) Using Calico Network Policy with Azure Kubernetes Server
- [itnext.io: Network Isolated AKS — Part 1: Controlling network traffic](https://itnext.io/network-isolated-aks-part-1-controlling-network-traffic-2cd0e045352d)
- [thenewstack.io: Turbocharging AKS Networking with Calico eBPF](https://thenewstack.io/turbocharging-aks-networking-with-calico-ebpf/)
- [carlos.mendible.com: AKS: Persistent Volume Claim with an Azure File Storage protected with a Private Endpoint](https://carlos.mendible.com/2021/08/02/aks-persistent-volume-claim-with-an-azure-file-storage-protected-with-a-private-endpoint/)
- [joachim8675309.medium.com: AKS with Istio Service Mesh](https://joachim8675309.medium.com/istio-service-mesh-on-aks-1b6ed16f6890) Securing traffic with Istio service mesh on AKS
- [optisolbusiness.com: Implementing Microservices Architecture in AKS](https://www.optisolbusiness.com/insight/implementing-microservices-architecture-in-aks)
- [blog.kasten.io: AKS and Storage: How to Design Storage for Cloud Native Applications](https://blog.kasten.io/aks-and-storage-how-to-design-storage-for-cloud-native-applications)
- [blog.kasten.io: AKS and Storage: Performance Differences Among K8s Storage Services](https://blog.kasten.io/aks-and-storage-performance-differences-among-kubernetes-storage-services)
- [medium: AKS — different load balancing options. When to use what?](https://medium.com/microsoftazure/aks-different-load-balancing-options-for-a-single-cluster-when-to-use-what-abd2c22c2825)
- [medium: Going multicloud with kubernetes and Azure Front Door](https://medium.com/microsoftazure/going-multicloud-with-kubernetes-and-azure-front-door-f34a2f39068a) Kubernetes/AKS/GKE/MultiCloud/Azure Front Door
- [docs.microsoft.com: Best practices for cluster isolation in Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/operator-best-practices-cluster-isolation)
- [docs.cloudblue.com: Deploying an AKS Cluster with Custom IP Ranges (ARM template)](https://docs.cloudblue.com/cbc/20.5/premium/content/Deployment-of-Product-to-Azure-Cloud-Guide/Deploying-AKS-Cluster-with-Custom-IP-Ranges.htm)
- [k21academy.com: Azure Kubernetes Service & Azure Container Instances For Beginners 🌟](https://k21academy.com/microsoft-azure/az-303/azure-container-instances-and-kubernetes-service)
- [azurecloudai.blog: Deploy Azure Kubernetes Service (AKS) to a preexisting VNET](https://azurecloudai.blog/2019/09/27/deploy-azure-kubernetes-service-aks-to-a-preexisting-vnet/)
- [tigera.io: Turbocharging AKS networking with Calico eBPF](https://www.tigera.io/blog/turbocharging-aks-networking-with-calico-ebpf/)
- [akhilsharma.work: How to list Azure RBAC Roles to Secure AKS Clusters](https://akhilsharma.work/how-to-list-azure-rbac-roles-to-secure-aks-clusters/)
- [tigera.io: Calico WireGuard support with Azure CNI](https://www.tigera.io/blog/calico-wireguard-support-with-azure-cni/) Last June, Tigera announced a first for Kubernetes: supporting open-source WireGuard for encrypting data in transit within your cluster. We never like to sit still, so we have been working hard on some exciting new features for this technology, the first of which is support for WireGuard on AKS using the Azure CNI.
- [docs.microsoft.com: Use dual-stack (IPv4 and IPv6) kubenet networking in Azure Kubernetes Service (AKS) (Preview)](https://docs.microsoft.com/en-us/azure/aks/configure-kubenet-dual-stack)
- [logz.io: Collecting Metrics from Windows Kubernetes Nodes in AKS 🌟](https://logz.io/blog/windows-kubernetes-nodes-aks-metrics/)
- [dev.to: Moving Azure Functions from AKS to Container Apps](https://dev.to/christle/moving-azure-functions-from-aks-to-container-apps-k60)
- [techcommunity.microsoft.com: Azure Kubernetes Service and Azure Container Registry Service on Azure Stack Hub](https://techcommunity.microsoft.com/t5/azure-stack-blog/azure-kubernetes-service-and-azure-container-registry-service-on/ba-p/3075932)
- [dev.to: Getting started with Windows Containers on Azure Kubernetes Service](https://dev.to/rdvansloten/getting-started-with-windows-containers-on-azure-kubernetes-service-46ce) Windows support has finally arrived in Kubernetes and AKS. Learn how to migrate your workloads and what pitfalls to avoid in this short and sweet introduction to Windows Containers.
- [==mehighlow.medium.com: Hardened-AKS/Secrets==](https://mehighlow.medium.com/hardened-aks-secrets-82351c43eac4) Commonly, an application requires access to data and, usually, such access must be restricted. So, you need to provide your pod/deployment/replicaSet/DaemonSet with secrets. Learn how you can do so in AKS
- [returngis.net: Desescalar nodos de AKS apagando las máquinas en lugar de eliminarlas](https://www.returngis.net/2022/04/desescalar-nodos-de-aks-apagando-las-maquinas-en-lugar-de-eliminarlas/)
- [dev.to/javiermarasco: HTTPs with Ingress controller, cert-manager and DuckDNS (in AKS/Kubernetes)](https://dev.to/javiermarasco/https-with-ingress-controller-cert-manager-and-duckdns-in-akskubernetes-2jd1)
- [==dev.to: Implement Azure AD Workload Identity on AKS with terraform==](https://dev.to/maxx_don/implement-azure-ad-workload-identity-on-aks-with-terraform-3oho) **Azure AD workload identity is designed to associate a pod with an identity in Azure Active Directory so that you can grant permissions to access another resource (i.e. a storage account or an Azure SQL Database)**
- [medium.com/kocsistem: Installation Internal Nginx Ingress for a Private AKS Cluster](https://medium.com/kocsistem/installation-internal-nginx-ingress-for-a-private-aks-cluster-7b6386492d56)
- [pixelrobots.co.uk: Bring your own Container Network Interface (CNI) plugin with Azure Kubernetes Service (AKS) (PREVIEW)](https://pixelrobots.co.uk/2022/04/bring-your-own-container-network-interface-cni-plugin-with-azure-kubernetes-service-aks-preview/) AKS has only officially supported two CNI's: Kubenet and Azure CNI. In this blog post, you will learn how to create an AKS cluster with no CNI and then deploy cilium.
- [joachim8675309.medium.com: ExternalDNS with AKS & Azure DNS](https://joachim8675309.medium.com/externaldns-with-aks-azure-dns-941a1804dc88) ExternalDNS with kubelet identity to access to Azure DNS. After deploying a public facing web application on Kubernetes, you need to update DNS records so that traffic can reach the server. ExternalDNS can automate this process during deployment stage of the web application, so there is no need for extra configuration outside of Kubernetes.
- [medium.com/dzerolabs: Accessing Azure Key Vault Secrets in Azure Kubernetes with Secrets Store CSI Driver 🌟](https://medium.com/dzerolabs/kubernetes-saved-today-f-cked-tomorrow-a-rant-azure-key-vault-secrets-%C3%A0-la-kubernetes-fc3be5e65d18) A little bit of standardization goes a long way. Much better than documenting steps that can soon become outdated. Azure Key Vault Provider for Secrets Store CSI Driver maps a Kubernetes resource called SecretProviderClass to an Azure Key Vault and lets you select which secrets, keys, and/or certificates you'd like to expose.
- [==buchatech.com/2022: A Guide to Navigating the AKS Enterprise Documentation & Scripts== 🌟🌟](https://www.buchatech.com/2022/08/a-guide-to-navigating-the-aks-enterprise-documentation-scripts/) This blog's goal is to guide you through the AKS Enterprise Docs as you architect, deploy, and operate your AKS.
- [docs.microsoft.com: Start and stop an Azure Kubernetes Service (AKS) node pool 🌟](https://docs.microsoft.com/en-us/azure/aks/start-stop-nodepools) Your AKS workloads may not need to run continuously, for example a development cluster that has node pools running specific workloads. To optimize your costs, you can completely turn off (stop) your node pools in your AKS cluster, allowing you to save on compute costs.
- [==dev.to/thenjdevopsguy: Monitoring AKS With Prometheus and Grafana== 🌟](https://dev.to/thenjdevopsguy/monitoring-aks-with-prometheus-and-grafana-9o8)
- [techcommunity.microsoft.com: Azure Kubernetes Service Microsoft Ignite announcements](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/azure-kubernetes-service-microsoft-ignite-announcements/ba-p/3650443)
- [==isovalent.com: Announcing Azure CNI Powered by Cilium==](https://isovalent.com/blog/post/azure-cni-cilium/)
- [==dev.to: Access Secrets in AKV using Managed identities for AKS== 🌟](https://dev.to/vivekanandrapaka/access-secrets-from-akv-using-managed-identities-for-aks-91p) The purpose of this post is to show you how to access secrets from AKS cluster that are stored in Azure Key Vault.
- [==blog.baeke.info: AKS Workload Identity Revisited==](https://blog.baeke.info/2022/11/24/aks-workload-identity-revisited/)
- [==azure.microsoft.com: Private preview: Azure Kubernetes Service (AKS) Backup== 🌟](https://azure.microsoft.com/en-us/updates/private-preview-aks-backup/)
- [==medium.com/@gjoshevski: Reduce the cost of running AKS cluster by leveraging Azure Spot VMs| 70% and more== 🌟🌟](https://medium.com/@gjoshevski/reduce-the-cost-of-running-aks-cluster-by-leveraging-azure-spot-vms-70-and-more-e917f568c3b9)
- [community.ops.io: One day I woke up to a crashed AKS cluster and this is what I did to get it back to life](https://community.ops.io/javi_labs/one-day-wake-up-to-a-crashed-aks-cluster-and-this-is-what-i-did-to-get-it-back-to-life-1592) One day, Javier found a crashed AKS cluster with three nodes stopped and all pods in the "Terminating" state. Learn how Javier debugged the cluster and brought it back to life.
- [Using CDK to perform continuous deployments in multi-region Kubernetes environments](https://aws.amazon.com/blogs/containers/using-cdk-to-perform-continuous-deployments-in-multi-region-kubernetes-environments/) This post demonstrated how to create a continuous deployment pipeline to deploy applications in multiple EKS clusters running in different regions. The accompanying CDK code creates EKS clusters and the CI/CD stack to continuously deploy applications
- [blog.coffeeapplied.com: Securing AKS in peered virtual networks using only network security groups (NSGs)](https://blog.coffeeapplied.com/securing-aks-in-peered-virtual-networks-using-only-network-security-groups-nsgs-c43d6a215f32) When you use peering in AKS, with the "default" AKS deployment, your complete cluster, including all pods, is completely open and addressable from your complete peered network. Learn how to fix in this article.
- [medium.com/@vamsi.lakshman: Overview of Azure Kubernetes Services Networking Models](https://medium.com/@vamsi.lakshman/overview-of-azure-kubernetes-services-networking-models-e3ca0591aebe)
- [techcommunity.microsoft.com: SQL Server containers on Kubernetes with S3-compatible object storage - Getting started](https://techcommunity.microsoft.com/t5/sql-server-blog/sql-server-containers-on-kubernetes-with-s3-compatible-object/ba-p/3717003) Check out this post on the Microsoft Tech Community : SQL Server containers on Kubernetes with S3-compatible object storage - Getting started - Microsoft Community Hub
- [learn.microsoft.com: Connect with RDP to Azure Kubernetes Service (AKS) cluster Windows Server nodes for maintenance or troubleshooting](https://learn.microsoft.com/en-us/azure/aks/rdp)
- [techcommunity.microsoft.com: Azure Kubernetes Service Free tier and Standard tier](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/azure-kubernetes-service-free-tier-and-standard-tier/ba-p/3731432)
- [==medium.com/credera-engineering: How to blue-green deploy an AKS cluster==](https://medium.com/credera-engineering/how-to-blue-green-deploy-an-aks-cluster-ab8f6a2cea9a)
- [community.ops.io: Configuring AKS to read secrets and certificates from Azure KeyVaults](https://community.ops.io/javi_labs/configuring-aks-to-read-secrets-and-certificates-from-azure-keyvaults-17o1) This article will teach you how to configure an AKS cluster to consume secrets, keys and certificates from an Azure KeyVault
- [==medium.com/@danieljimgarcia: The Application Gateway Ingress Controller is broken== 🌟](https://medium.com/@danieljimgarcia/the-application-gateway-ingress-controller-is-broken-6aa9eb229881) The Application Gateway Ingress Controller exposes applications hosted in Kubernetes to the outside world via Azure’s native Application Gateway. However, it has important design flaws, which can cause minutes of downtime when updating your workloads.
- [==kristhecodingunicorn.com: Setting Up OAuth 2.0 Authentication for Applications in AKS With NGINX and OAuth2 Proxy== 🌟🌟](https://kristhecodingunicorn.com/post/k8s_nginx_oauth/)
- [medium.com/@ershivamgupta: Disaster Recovery Solution for Azure Kubernetes Service (AKS) Persistent Volume Storage 🌟](https://medium.com/@ershivamgupta/disaster-recovery-solution-for-azure-kubernetes-service-aks-persistent-volume-storage-f2b3d2aafcf4) This article demonstrates a disaster recovery solution for AKS:
    - Installing Longhorn
    - Setting up an External Backup target
    - Deploying a stateful application
    - Backing up the Persistent Volume
    - Restoring it in a secondary region
- [github.com/OvidiuBorlean/kubectl-windumps](https://github.com/OvidiuBorlean/kubectl-windumps) Network traffic capture in AKS Windows Nodes
- [infoq.com: Microsoft Brings Kubernetes to the Edge with AKS Edge Essentials](https://www.infoq.com/news/2023/03/aks-edge-essentials-ga/)
- [==azuredevopslabs.com: Deploying a multi-container application to Azure Kubernetes Services==](https://azuredevopslabs.com/labs/vstsextend/kubernetes/)
- [danielstechblog.io: Mitigating slow container image pulls on Azure Kubernetes Service](https://www.danielstechblog.io/mitigating-slow-container-image-pulls-on-azure-kubernetes-service/) It is not easy identifying the root cause for slow container image pulls on your AKS. In this article, you'll follow Daniel's journey in debugging the OS disk queue depth and how it affects image pulls.
- [==grafana.com: Scrape Azure metrics and monitor AKS using Grafana Agent== 🌟](https://grafana.com/blog/2023/04/07/scrape-azure-metrics-and-monitor-aks-using-grafana-agent/) In this blog post, we will demonstrate how to configure Grafana Agent to scrape metrics from Microsoft Azure, specifically from AKS, using the newly released [azure_exporter](https://grafana.com/docs/agent/v0.32/configuration/integrations/azure-exporter-config/).
- [medium.com/microsoftazure: Automating Managed Prometheus and Grafana with Terraform for scalable observability on Azure Kubernetes Service and Istio 🌟](https://medium.com/microsoftazure/automating-managed-prometheus-and-grafana-with-terraform-for-scalable-observability-on-azure-4e5c5409a6b1)
- [kristhecodingunicorn.com: Setting Up OAuth 2.0 Authentication for Applications in AKS With NGINX and OAuth2 Proxy](https://www.kristhecodingunicorn.com/post/aks-oauth2-proxy-with-nginx-ingress-controller/)
- [azure.microsoft.com: Announcing the general availability of Azure CNI Overlay in Azure Kubernetes Service](https://azure.microsoft.com/en-us/blog/announcing-the-general-availability-of-azure-cni-overlay-in-azure-kubernetes-service/)
- [medium.com/@GiantSwarm: Deep Dive Into Kubernetes Networking in Azure](https://medium.com/@GiantSwarm/deep-dive-into-kubernetes-networking-in-azure-9f0e85e2ee34) Deep Dive Into Kubernetes Networking in Azure
    - Calico with BGP
    - Azure Container Network
    - Calico Policy-Only + Flannel
    - Best Option
- [returngis.net: Configurar más de un Application Gateway con AGIC para AKS](https://www.returngis.net/2022/05/configurar-mas-de-un-application-gateway-con-agic-para-aks/)
- [returngis.net: Azure Application Gateway con WAF y wildcard + Nginx Controller para AKS](https://www.returngis.net/2021/11/azure-application-gateway-con-waf-y-wildcard-nginx-controller-para-aks/)
- [medium.com/@lfoster49203: Kubernetes on Azure: Setting up a cluster on Microsoft Azure (with Azure AKS)](https://medium.com/@lfoster49203/kubernetes-on-azure-setting-up-a-cluster-on-microsoft-azure-with-azure-aks-d6bee3eaa65)
- [medium.com/@pauldotyu: Effortlessly Deploy to AKS with Open Source Tools Draft and Acorn](https://medium.com/@pauldotyu/app-to-aks-with-draft-and-acorn-2d25f19649b7)
- [techcommunity.microsoft.com: How to install an AKS cluster with the Istio service mesh add-on via Bicep](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/how-to-install-an-aks-cluster-with-the-istio-service-mesh-add-on/ba-p/3802069)
- [adamtheautomator.com: Getting Started with the Azure Kubernetes Service (AKS)](https://adamtheautomator.com/azure-kubernetes-service) In this tutorial, you'll learn how to get started with Microsoft Azure Kubernetes Service (AKS) using the Azure Portal and the Azure CLI
- [techcommunity.microsoft.com: Kubernetes External DNS for Azure DNS & AKS](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/kubernetes-external-dns-for-azure-dns-amp-aks/ba-p/3809393)
- [medium.com/adessoturkey: Azure DevOps Agents on AKS with the kaniko Option](https://medium.com/adessoturkey/azure-devops-agents-on-aks-with-kaniko-option-f672f900a177) In this article, you will learn how to build container images in your Azure DevOps agents using kaniko. kaniko doesn't depend on a Docker daemon and executes each command within a Dockerfile completely in userspace.
- [techcommunity.microsoft.com: Securing Windows workloads on Azure Kubernetes Service with Calico](https://techcommunity.microsoft.com/t5/containers/securing-windows-workloads-on-azure-kubernetes-service-with/ba-p/3815429)
- [infoworld.com: Kubernetes cost management for the real world](https://www.infoworld.com/article/3695569/kubernetes-cost-management-for-the-real-world.html) How much will Kubernetes cost to run? That question has become much easier to answer for Azure Kubernetes Service, thanks to OpenCost integration.
- [==inder-devops.medium.com: AKS Networking Deep Dive: Kubenet vs Azure-CNI vs Azure-CNI (overlay)==](https://inder-devops.medium.com/aks-networking-deep-dive-kubenet-vs-azure-cni-vs-azure-cni-overlay-a51709171ce9) When deploying an AKS cluster, there are three networking models you can choose from:
    - Kubenet
    - Azure CNI
    - Azure CNI Overlay networking
- [returngis.net: Desplegar AGIC en AKS utilizando workload identity](https://www.returngis.net/2023/05/desplegar-agic-en-aks-utilizando-workload-identity/)
- [learn.microsoft.com: Use Application Gateway Ingress Controller (AGIC) with a multitenant Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/aks-agic/aks-agic)
- [returngis.net: Exponer APIs en AKS a través de Azure API Management](https://www.returngis.net/2023/05/exponer-apis-en-aks-a-traves-de-azure-api-management/)
- [==techcommunity.microsoft.com: A Practical Guide to Zone Redundant AKS Clusters and Storage==](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/a-practical-guide-to-zone-redundant-aks-clusters-and-storage/ba-p/4036254)
- [==learn.microsoft.com: AKS landing zone accelerator==](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/aks/landing-zone-accelerator)
- [==piotrminkowski.com: Getting Started with Azure Kubernetes Service== 🌟](https://piotrminkowski.com/2024/02/05/getting-started-with-azure-kubernetes-service/)
- [==techcommunity.microsoft.com: Simplifying Azure Kubernetes Service Authentication Part 2==](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/simplifying-azure-kubernetes-service-authentication-part-2/ba-p/4055332)
- [==learn.microsoft.com: Monitor Azure Kubernetes Service (AKS) control plane metrics (preview)==](https://learn.microsoft.com/en-us/azure/aks/monitor-control-plane-metrics)
- [==github.com/stephaneey/azure-and-k8s-architecture: Azure and K8s Architecture== 🌟](https://github.com/stephaneey/azure-and-k8s-architecture/) The purpose of this repo is to share some real-world inspired Azure and K8s architecture diagrams, that may help organizations accelerate their adoption of Azure and K8s. Each diagram will be accompanied by a textual explanation with the key attention points.
    - [azure-and-k8s-architecture: The API Management Architecture Map](https://github.com/stephaneey/azure-and-k8s-architecture/blob/main/maps/apim.md)
    - [azure-and-k8s-architecture: East-West Traffic shared cluster and shared responsibilities using Calico](https://github.com/stephaneey/azure-and-k8s-architecture/blob/main/networking/azure-kubernetes-service/east-west-traffic/east-west-shared-calico.md)
- [techcommunity.microsoft.com: Running GPU accelerated workloads with NVIDIA GPU Operator on AKS 🌟](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/running-gpu-accelerated-workloads-with-nvidia-gpu-operator-on/ba-p/4061318)
- [dinantpaardenkooper.nl: Azure Day with Kubernetes](https://dinantpaardenkooper.nl/posts/aks-2024-03-18/) Within this blog, I want to give an overview of all the feature which where shared at KubeCon Europe 2024 that becomes available in General Availability, Technical Preview or End of Support by Microsoft. This information can be found at Microsoft [Azure Updates](https://azure.microsoft.com/en-us/updates/?query=AKS).
- [==youtube: Day -25 | No Dockerfile, No K8s Manifests | Setup CI/CD in 5 minutes for any programming language==](https://www.youtube.com/watch?v=io_yBU7vhIo) This video is part of Azure Zero to Hero (Free Azure Course including Azure DevOps). In this video of Automated CI/CD Pipeline Generator. You will learn how to setup and implement automated CI/CD deployment on the AKS platform of Azure. No Dockerfile, No Kubernetes manifests, No CI/CD Pipeline. Everything is generated automatically for you. Best way to start learning CI/CD and automated deployments. This makes life of DevOps Engineers extremely easy.
- [medium.com/@anjkeesari: Install Grafana Loki-Stack Helmchart in Azure Kubernetes Services (AKS)](https://medium.com/@anjkeesari/install-grafana-loki-stack-helmchart-in-azure-kubernetes-services-aks-1359281b3321)
- [==pixelrobots.co.uk: Exploring Azure Kubernetes Service’s Node Autoprovision: A Deep Dive into the Latest Public Preview Feature==](https://pixelrobots.co.uk/2023/12/exploring-azure-kubernetes-services-node-autoprovision-a-deep-dive-into-the-latest-public-preview-feature/)
    - Node Autoprovision (NAP) in AKS is a game-changer for managing node pools. As your workloads expand and diversify in complexity, needing various CPU, memory, and capability configurations, managing your VM configurations can become quite daunting. This is where NAP steps in.
    - NAP dynamically decides the optimal VM configuration for your pending pod resource requirements, ensuring that your workloads run efficiently and cost-effectively. This feature is rooted in the open-source Karpenter project, and its implementation in AKS is also open-source.
- [==blog.teknews.cloud/aks: A look at Retina on AKS (Observability)==](https://blog.teknews.cloud/aks/network/2024/06/29/A_look_at_Retina_on_AKS.html)
- [techcommunity.microsoft.com: Advanced Network Observability for your Azure Kubernetes Service clusters through Azure Monitor](https://techcommunity.microsoft.com/t5/azure-observability-blog/advanced-network-observability-for-your-azure-kubernetes-service/ba-p/4176736)
- [learn.microsoft.com: Deploy AKS and API Management with mTLS](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/mutual-tls-deploy-aks-api-management)
- [blog.stackademic.com: Advanced End-to-End DevSecOps Kubernetes Three-Tier Project using Azure AKS, fluxCD, Prometheus, Grafana, and GitLab](https://blog.stackademic.com/advanced-end-to-end-devsecops-kubernetes-three-tier-project-using-azure-aks-fluxcd-prometheus-cca3c5e61953)
- [faun.pub: External Secret Operator on AKS (with Terraform) for Azure Key Vault Integration (with Workload Identity)](https://faun.pub/external-secret-operator-on-aks-with-terraform-for-azure-key-vault-integration-with-workload-1d0c31082373)
- [techcommunity.microsoft.com: Leveraging Azure Copilot for Azure Kubernetes Services (AKS)](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/leveraging-azure-copilot-for-azure-kubernetes-services-aks/ba-p/4212457)
- [azure.github.io: Using AKS-managed Istio External Ingress Gateway with Gateway API](https://azure.github.io/AKS/2024/08/06/istio-with-gateway-api) Learn how to use the Gateway API to manage the Istio external ingress gateway on AKS.

### AKS Releases

- [dinantpaardenkooper.nl: Microsoft AKS updates 2023 - Q4](https://dinantpaardenkooper.nl/posts/aks23q4/)

### AKS Lite

- [thenewstack.io: Microsoft Takes Kubernetes to the Edge with AKS Lite](https://thenewstack.io/microsoft-takes-kubernetes-to-the-edge-with-aks-lite/) At it Ignite conference, Microsoft announced that a public preview of Azure Kubernetes Service (AKS) on Windows IoT and Windows devices, known as AKS lite, will be available next month.

### Draft 2 on AKS

- [==Azure/Draft== 🌟](https://github.com/Azure/draft)
- [blog.baeke.info: Trying out Draft 2 on AKS](https://blog.baeke.info/2022/06/02/trying-out-draft-2-on-aks/)

## GKE Google Kubernetes Engine

- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
    - One of the most helpful GKE features is the ability to create clusters and node pools with custom kernel parameters. This means you no longer need to use one-off daemonsets, or random workarounds, to tune your machines after cluster creation.
- [Fetches all Primitive and Predefined GCP IAM Roles](https://github.com/darkbitio/gcp-iam-role-permissions)
- [Using new traffic control features in External HTTP(S) load balancer](https://cloudblog.withgoogle.com/products/networking/how-to-use-new-traffic-control-features-in-cloud-load-balancing/amp/)
- [Setting up NodeLocal DNSCache](https://cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
- [Looking ahead as GKE, the original managed Kubernetes, turns 5](https://cloudblog.withgoogle.com/products/containers-kubernetes/5-ways-google-cloud-is-making-gke-the-best-place-to-run-kubernetes/amp/)
- [blog.doit-intl.com: How to Set Up Multi-Cluster Load Balancing with GKE](https://blog.doit-intl.com/how-to-setup-multi-cluster-load-balancing-with-gke-4b407e1f3dff)
- [codeburst.io: Google Kubernetes Engine Logging by Example](https://codeburst.io/google-kubernetes-engine-logging-by-example-df6946dcba6b)
- [cloud.google.com: Discover and invoke services across clusters with GKE multi-cluster services](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-multi-cluster-services)
- [Introducing GKE Autopilot: a revolution in managed Kubernetes 🌟](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-autopilot)
- [techcrunch.com: Google Cloud puts its Kubernetes Engine on autopilot](https://techcrunch.com/2021/02/24/google-cloud-puts-its-kubernetes-engine-on-autopilot/)
- [zdnet.com: Google introduces GKE Autopilot for hands-off Kubernetes](https://www.zdnet.com/article/google-introduces-gke-autopilot-for-hands-off-kubernetes/) The new GKE Autopilot, generally available now, steps up the level of automation involved in Kubernetes management, down to eliminating all node management.
- [thenewstack.io: Google’s New ‘Autopilot’ for Kubernetes](https://thenewstack.io/googles-new-autopilot-for-kubernetes)
- [cloud.google.com: GKE Autopilot 🌟](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
- [medium: How to provision Kubernetes Cluster in GCP Cloud (K8s)? 🌟](https://medium.com/avmconsulting-blog/kubernetes-google-kubernetes-engine-gke-99abf912f912)
- [youtube: GKE Autopilot - Fully Managed Kubernetes Service From Google 🌟](https://youtu.be/Zztufl4mFQ4)
- [insights.project-a.com: Using GitHub Actions to deploy to Kubernetes in GKE 🌟](https://insights.project-a.com/using-github-actions-to-deploy-to-kubernetes-122c653c0b09)
- [faun.pub: How to automate the setup of a Kubernetes cluster on GCP](https://faun.pub/how-to-automate-the-setup-of-a-kubernetes-cluster-on-gcp-e97918bf41de) Using Ansible to install, setup, and configure a Google Kubernetes Cluster (GKE) on Google Cloud Platform (GCP).
- [Kubernetes Cloud DNS](https://cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#vpc_scope_dns) GCP now makes it easy to query DNS for Kubernetes services across multiple clusters from anywhere inside the VPC! The less stuff users have to run in their clusters, the more they can use for their own apps. It was always problematic to make users admin their own DNS.
- [seroter.com: Using the new Google Cloud Config Controller to provision and manage cloud services via the Kubernetes Resource Model](https://seroter.com/2021/08/18/using-the-new-google-cloud-config-controller-to-provision-and-manage-cloud-services-via-the-kubernetes-resource-model/) I look at a new managed service that provisions cloud-native services as if they were k8s resources.
- [cloud.google.com: Announcing Backup for GKE: the easiest way to protect GKE workloads 🌟](https://cloud.google.com/blog/products/storage-data-transfer/google-cloud-launches-backups-for-gke)
- Features of Google Kubernetes Engine that NO other K8s provider has or are rapidly copying:
    - Autopilot
    - Backup
    - Multi-cluster Ingress
    - OOTB SRE Dashboards with ASM
    - Config Management across clouds
- [cloud.google.com: Announcing Spot Pods for GKE Autopilot—save on fault tolerant workloads](https://cloud.google.com/blog/products/containers-kubernetes/announcing-spot-pods-for-gke-autopilot)
- [acloudguru.com: GKE ludicrous speed! GKE Image Streaming speeds up container starts](https://acloudguru.com/blog/engineering/gke-ludicrous-speed-gke-image-streaming-speeds-up-container-starts)
- [cloud.google.com: How to do multi-cluster Kubernetes in the real world—one GKE shop’s approach](https://cloud.google.com/blog/products/containers-kubernetes/multi-cluster-kubernetes-with-gke-at-geotab)
- [cloud.google.com: Know more, spend less: how GKE cost optimization insights help you optimize Kubernetes](https://cloud.google.com/blog/products/containers-kubernetes/gke-cost-optimization-insights-now-ga)
- [medium.com/@glen.yu: Getting started with eBPF and Cilium on GKE](https://medium.com/@glen.yu/getting-started-with-ebpf-and-cilium-on-gke-6553c5d7e02a) Through Cilium, users can add functionality such as encryption and L7 network policy enforcement previously only available in a service mesh — but without the operational complexity of having to manage one.
- [medium.com/@glen.yu: NGINX Ingress or GKE Ingress?](https://medium.com/@glen.yu/nginx-ingress-or-gke-ingress-d87dd9db504c) There are tons of ingress controllers out there in the Kubernetes ecosystem, so how do we know which one is right for you? In this article, you will learn the differences between the NGINX and GKE Ingress.
- [medium.com/google-developer-experts: Getting started with GKE Gateway controller](https://medium.com/google-developer-experts/getting-started-with-gke-gateway-controller-ee45c3bc8996)
- [cloud.google.com: Introducing Kubernetes control plane metrics in GKE](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-control-plane-metrics-are-generally-available)
- [google/gke-policy-automation](https://github.com/google/gke-policy-automation) This repository contains the tool and the policy library for validating GKE clusters against configuration best practices
- [medium.com/google-cloud: Monitoring Kubernetes Clusters on GKE (Google Container Engine)](https://medium.com/google-cloud/gke-monitoring-84170ea44833) This is a hands-on guide to monitoring and logging at different layers in the Kubernetes Engine stack
    - GCP components (compute)
    - Kubernetes objects (cluster nodes)
    - Containerized applications
    - Application specific metrics
- [blog.devgenius.io: Explore API Priority and Fairness to Ease the Load of the APIServer](https://blog.devgenius.io/explore-api-priority-and-fairness-to-ease-the-load-of-the-apiserver-a4fe9c4e7174) Walk through incident remediation using APF
- [faun.pub: Make Your Kubernetes Cluster Highly Available and Fault Tolerant 🌟](https://faun.pub/deploy-active-active-multi-region-kubernetes-cluster-with-terraform-f2652e43f47e) End to End setup of Multi Region Autopilot Kubernetes Cluster with Application Deployment Example
- [medium.com/@pbijjala: reCap: Kube vrs Cloud DNS in GKE](https://medium.com/@pbijjala/recap-kube-vrs-cloud-dns-in-gke-b8d1d407e00d) When deciding on how to use DNS with GKE, what are the available native Kubernetes options, which options exist on Google Cloud for GKE, and how do these two things play together?
- [medium.com/google-cloud: Ingress in Google Kubernetes Products](https://medium.com/google-cloud/ingress-in-google-kubernetes-products-f22ded21f4ed) In this article, you will discuss, enumerate and compare all the options you have to route traffic into a Kubernetes cluster running in Google Cloud (GKE) or on-premise (Anthos on Bare Metal, Anthos on VMware)
- [medium.com/@pbijjala: Considerations for Hardening your GKE, a workload perceptive](https://medium.com/@pbijjala/considerations-for-hardening-your-gke-a-workload-perceptive-943be26949d2) This article has a few tips for hardening your GKE setup:
    - Network policies
    - Custom service accounts
    - Workload identities
    - Pod Security admissions and admission controllers
    - GKE sandbox
- [medium.com/@jjlakis: GCP Secret Manager with self-hosted Kubernetes](https://medium.com/@jjlakis/gcp-secret-manager-with-self-hosted-kubernetes-db35d01d65f0) In this article, you will learn how to use the GCP secret manager to store secrets for an on-prem k3s cluster
- [tech.loveholidays.com: GKE Multi-Cluster Services — one bad probe away from disaster](https://tech.loveholidays.com/gke-multi-cluster-services-one-bad-probe-away-from-disaster-62051fafe84e)
- [Looking for GPU Capacity ? DWS got you covered !](https://medium.com/zencore/looking-for-gpu-capacity-dws-got-you-covered-d736b8c63ba6)
- [medium.com/google-cloud: Understanding health checks in GKE & Gateway API](https://medium.com/google-cloud/understanding-health-checks-in-gke-gateway-api-1c89f82bfba8) This article discusses the difference between Kubernetes readiness and GCP's Application Load Balancer health checks. Despite a pod being marked as unready by Kubernetes, if GCP's health check deems it healthy, traffic will still be forwarded to it

## IKS IBM Cloud Kubernetes Service

- [IKS](https://www.ibm.com/cloud/kubernetes-service)
- [medium: Multizone Kubernetes and VPC Load Balancer Setup with terraform](https://medium.com/vmacwrites/multizone-kubernetes-and-vpc-load-balancer-setup-9664b3c9ea5d)

## Linode Kubernetes Engine LKE

- [Linode Kubernetes Engine (LKE)](https://www.linode.com/products/kubernetes/)
- [medium: Create Kubernetes Cluster Using Linode LKE](https://medium.com/codex/create-kubernetes-cluster-using-linode-lke-4f9c71d03a8d)
- [dev.to: Practical Introduction to Kubernetes Autoscaling Tools with Linode Kubernetes Engine 🌟](https://dev.to/rahulrai/practical-introduction-to-kubernetes-autoscaling-tools-with-linode-kubernetes-engine-2i7k) In this article you will practice scaling apps with the:
    - Horizontal Pod Autoscaler
    - Vertical Pod Autoscaler
    - Proportional Autoscaler
    - Cluster Autoscaler

## DOKS Digital Ocean Kubernetes

- [docs.digitalocean.com: Kubernetes on DigitalOcean](https://docs.digitalocean.com/products/kubernetes/)
- [digitalocean.com: Automating GitOps and Continuous Delivery With DigitalOcean Kubernetes (Terraform, Helm and Flux)](https://www.digitalocean.com/community/tech_talks/automating-gitops-and-continuous-delivery-with-digitalocean-kubernetes)
- [blog.ediri.io: DigitalOcean Kubernetes Challenge](https://blog.ediri.io/digitalocean-kubernetes-challenge) Deploy a GitOps CI/CD implementation
- [digitalocean.com: Kubernetes for startups: Why, when, and how to adopt  ](https://www.digitalocean.com/blog/kubernetes-for-startups-why-when-and-how-to-adopt)

## Oracle Cloud Kubernetes

- [arnoldgalovics.com: GitHub Actions CI/CD For Oracle Cloud Kubernetes](https://arnoldgalovics.com/github-actions-oracle-cloud-kubernetes/) Learn how to create a private container registry with Terraform and deploy a 4 node Kubernetes cluster for free on Oracle Cloud. Then, use GitHub Actions to build ARM Docker containers for your nodes.

## Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes

- [==learnk8s.io: Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes==](https://learnk8s.io/cloud-resources-kubernetes)

## Kubesphere

- [kubesphere.io](https://kubesphere.io/) The Kubernetes platform tailored for hybrid multicloud. KubeSphere is a distributed operating system managing cloud native applications with Kubernetes as its kernel, and provides plug-and-play architecture for the seamless integration of third-party applications to boost its ecosystem.
- [kubekey](https://github.com/kubesphere/kubekey) The Next-gen Installer: Installing Kubernetes and KubeSphere v3.0.0 fastly, flexibly and easily
    - [kubesphere.io: Install Kubernetes 1.22 and containerd the Easy Way with kubekey](https://kubesphere.io/blogs/install-kubernetes-containerd/)
    - [thenewstack.io: Quickly Install a Kubernetes Cluster with KubeKey](https://thenewstack.io/quickly-install-a-kubernetes-cluster-with-kubekey/)
- [kubesphere.io: Scaling a Kubernetes Cluster: One of the Best Practices for Using KubeKey](https://kubesphere.io/blogs/scale-kubernetes-cluster-using-kubekey/)
- [itnext.io: Adding Master Nodes to Achieve HA: One of the Best Practices for Using KubeKey](https://itnext.io/adding-master-nodes-to-achieve-ha-one-of-the-best-practices-for-using-kubekey-6207e94b0bdd)
- [youtube: Create a Jenkins Pipeline on Kubernetes with CI/CD Pipeline Template in KubeSphere](https://www.youtube.com/watch?v=MU5LdM83x9s&t=40s&ab_channel=KubeSphere) Two built-in Jenkins pipeline templates are available in KubeSphere 3.1. DevOps team can generate CICD or customize the workflow as you need by simple drag-and-drop.
- [itnext.io: KubeSphere: A New Pluggable Kubernetes Application Management Platform](https://itnext.io/kubesphere-a-new-pluggable-kubernetes-application-management-platform-bf078b9f3330)

## Giant Swarm

- [Giant Swarm](https://www.giantswarm.io) Giant Swarm offers a fully managed, open source Kubernetes platform with all the flexibility and support you need.
- [giantswarm.io: ](https://www.giantswarm.io/blog/turtles-all-the-way-down-are-still-just-turtles-giant-swarm) We decided to go all-in with Cluster API (CAPI). "Time and again, we have seen open source win. It won with Kubernetes, and it will win with CAPI. We will continue to add our secret sauce to make it easily accessible to enterprise customers."

## Tools for multi-cloud Kubernetes management

- [Banzai Cloud 🌟](https://banzaicloud.com/)
    - [Kubernetes node pool upgrades with Banzai Pipeline](https://banzaicloud.com/blog/kubernetes-nodepool-upgrades/)
- [Compare tools for multi-cloud Kubernetes management 🌟](https://searchcloudcomputing.techtarget.com/tip/Compare-tools-for-multi-cloud-Kubernetes-management)
    - NetApp Kubernetes Service -- formerly StackPointCloud
    - Cloudify
    - Terraform
    - Rancher
    - Platform9 Managed Kubernetes
    - Red Hat OpenShift
    - Juke, from HTBase, now owned by Juniper Networks.

## Videos

- [youtube: The AKS Community](https://www.youtube.com/@theakscommunity)

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/xM9jpcVGTzY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/p6xDCz00TxU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/k-V3_zxRasM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/JGtJj_nAA2s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Cloud providers after selling managed kubernetes <a href="https://t.co/p9jd4Ov4Ej">pic.twitter.com/p9jd4Ov4Ej</a></p>&mdash; memenetes (@memenetes) <a href="https://twitter.com/memenetes/status/1458941321725546498?ref_src=twsrc%5Etfw">November 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Small companies managing their own Kubernetes. <a href="https://t.co/nTHrqPiQnm">pic.twitter.com/nTHrqPiQnm</a></p>&mdash; joshobrien77 (@joshobrien77) <a href="https://twitter.com/joshobrien77/status/1459032252768157696?ref_src=twsrc%5Etfw">November 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">AWS recently released a new version of the AWS-CNI that allows more Pods to be deployed in each EC2 instance.<br><br>More pod density means more efficiency, but how does it work?<br><br>And if it&#39;s that good, why release it only now?<br><br>Let&#39;s see 👇<br><br>🧵 <a href="https://t.co/MHnDrYJUvf">pic.twitter.com/MHnDrYJUvf</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1462751673143611395?ref_src=twsrc%5Etfw">November 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>