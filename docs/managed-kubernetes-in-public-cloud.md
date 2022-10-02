# Managed Kubernetes in Public Cloud

1. [Introduction](#introduction)
2. [Terraform Kubernetes Boilerplates](#terraform-kubernetes-boilerplates)
3. [GKE vs EKS vs AKS](#gke-vs-eks-vs-aks)
4. [Other Managed Kubernetes](#other-managed-kubernetes)
5. [AWS EKS (Hosted/Managed Kubernetes on AWS)](#aws-eks-hostedmanaged-kubernetes-on-aws)
    1. [EKS and IaC with Crossplane](#eks-and-iac-with-crossplane)
    2. [AWS EKS Vs ECS Vs Fargate](#aws-eks-vs-ecs-vs-fargate)
    3. [EKS Anywhere (on premises)](#eks-anywhere-on-premises)
    4. [EKS Distro (EKS-D)](#eks-distro-eks-d)
    5. [Testing Kubernetes Canary deployment on EKS](#testing-kubernetes-canary-deployment-on-eks)
6. [AKS Azure Kubernetes Service](#aks-azure-kubernetes-service)
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

- [dzone: kops vs EKS](https://dzone.com/articles/kops-vs-eks-a-comparison-guide)
- [udemy.com: amazon eks starter kubernetes on aws](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws/)
- [eksctl: EKS installer](https://github.com/weaveworks/eksctl)
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
- [github.com/aws/eks-charts 🌟](https://github.com/aws/eks-charts)
- [AWS Load Balancer Controller 🌟](https://kubernetes-sigs.github.io/aws-load-balancer-controller)
- [Updating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/update-managed-node-group.html) amazon eks managed node groups now supports parallel node upgrades
- [particule.io: Create Kubernetes federated clusters on AWS](https://particule.io/en/blog/aws-federated-eks/)
- [==aws.github.io/aws-eks-best-practices== 🌟](https://aws.github.io/aws-eks-best-practices/)
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
- [==aws.amazon.com: Planning Kubernetes Upgrades with Amazon EKS==](https://aws.amazon.com/blogs/containers/planning-kubernetes-upgrades-with-amazon-eks/)
- [medium.com/@radha.sable25: Enabling IAM users/roles Access on Amazon EKS cluster](https://medium.com/@radha.sable25/enabling-iam-users-roles-access-on-amazon-eks-cluster-f69b485c674f)
- [aws.amazon.com: Continuous Delivery of Amazon EKS Clusters Using AWS CDK and CDK Pipelines](https://aws.amazon.com/blogs/containers/continuous-delivery-of-amazon-eks-clusters-using-aws-cdk-and-cdk-pipelines)
- [medium.com/avmconsulting-blog: Installing Vault On EKS With TLS And Persistent Storage](https://medium.com/avmconsulting-blog/installing-vault-on-eks-with-tls-and-persistent-storage-98254b4150f3)
- [dzone.com: How to Use AWS IAM Role on AWS EKS PODs 🌟](https://dzone.com/articles/how-to-use-aws-iam-role-on-aws-eks-pods) A native-AWS way to attach an IAM role into the Kubernetes POD, without third-party software, reducing latency and improving your EKS security.
- [aws.amazon.com: Troubleshooting Amazon EKS API servers with Prometheus](https://aws.amazon.com/de/blogs/containers/troubleshooting-amazon-eks-api-servers-with-prometheus/)
- [AWS Controllers for Kubernetes (ACK) 🌟](https://github.com/aws-controllers-k8s/community) AWS Controllers for Kubernetes (ACK) lets you define & use AWS service resources directly from Kubernetes. With ACK, you can take advantage of AWS managed services for your applications without needing to define resources outside of the cluster.
- [itnext.io: Deploy Kubernetes (K8s) on Amazon AWS using mixed on-demand and spot instances 🌟](https://itnext.io/deploy-kubernetes-k8s-on-amazon-aws-using-mixed-on-demand-and-spot-instances-5440e5bece7)
- [==github.com/awslabs: Kubernetes Migration Factory User Guide== 🌟](https://github.com/awslabs/aws-kubernetes-migration-factory) **Kubernetes Migrations Factory (KMF) is a tool developed for migrating docker containers to Amazon EKS.  The Kubernetes Migration Factory solution is an orchestration platform for migrating containers to Amazon EKS at scale.**
- [==github.com/aws-ia/terraform-aws-eks-blueprints (examples) 🌟🌟🌟==](https://github.com/aws-ia/terraform-aws-eks-blueprints/tree/main/examples)
- [akintola-lonlon.medium.com: AWS Kubernetes: The #1 Rule You Need To Master Before Going To Production.](https://akintola-lonlon.medium.com/aws-kubernetes-the-1-rule-you-need-to-master-before-going-to-production-628b75ba1b6a) This is the most important thing to consider before going to production on EKS.
- [amod-kadam.medium.com: Are there two Load Balancer Controllers with EKS? 🌟](https://amod-kadam.medium.com/are-there-two-load-balancer-controllers-with-eks-8a7b04db8c93) In this article, you will learn how AWS provision different types of load balancers (Classic vs Network) to expose your applications depending on the annotations that you use.
- [aws.amazon.com: Streaming Kubernetes Events in Slack](https://aws.amazon.com/blogs/containers/streaming-kubernetes-events-in-slack/) This post describes how you can send events from your Kubernetes cluster to a Slack channel using BotKube, a messaging bot for monitoring and debugging Kubernetes clusters.
- [joachim8675309.medium.com: ExternalDNS with EKS and Route53](https://joachim8675309.medium.com/externaldns-with-eks-and-route53-90aa23fa3aba) After deploying a web app on Kubernetes, you might need to update the DNS records. ExternalDNS can automate this process and this tutorial demonstrates how to set up and configure this on Amazon EKS using Amazon Route 53 DNS zones.
- [==aws-quickstart/cdk-eks-blueprints: Amazon EKS Blueprints for CDK==](https://github.com/aws-quickstart/cdk-eks-blueprints) **This repository contains the source code for the eks-blueprints NPM module that can be used to configure and manage complete EKS clusters that are fully bootstrapped with the operational software that is needed to deploy and operate workloads**
- [dev.to: One technique to save your AWS EKS IP addresses 10x](https://dev.to/timtsoitt/one-technique-to-save-your-aws-eks-ip-addresses-10x-2ocn) To increase the number of available IP addresses in your EKS cluster you can:
    - Assign address prefixes to your ENI and
    - Enable the CNI custom networking feature
- [aws.amazon.com: Autoscaling EKS on Fargate with custom metrics](https://aws.amazon.com/blogs/containers/autoscaling-eks-on-fargate-with-custom-metrics/) Autoscaling is an approach to automatically scale up or down workloads based on the resource usage. In Kubernetes, the Horizontal Pod Autoscaler (HPA) can scale pods based on observed CPU utilization and memory usage. Starting with Kubernetes 1.7, an aggregation layer was introduced that allows third-party applications to extend the Kubernetes API by registering themselves as API add-ons. Such an add-on can implement the Custom Metrics API and enable HPA access to arbitrary metrics. What follows is a step-by-step guide on configuring HPA with metrics provided by Prometheus to automatically scale pods running on Amazon EKS on AWS Fargate.
- [==opssorry.substack.com: GitOps: A Simple Approach to using AWS Secrets Manager with Kubernetes== 🌟](https://opssorry.substack.com/p/gitops-a-simple-approach-to-using)
- [medium.com/scout24-engineering: How did we upgrade our EKS clusters from 1.15 to 1.22 without K8s knowledge?](https://medium.com/scout24-engineering/how-did-we-upgrade-our-eks-clusters-from-1-15-to-1-22-without-k8s-knowledge-2c96c1a94cc1)
- [==aws.github.io/aws-eks-best-practices: Amazon EKS Best Practices Guides== 🌟🌟🌟](https://aws.github.io/aws-eks-best-practices/networking/index/) **Welcome to the EKS Best Practices Guides. The primary goal of this project is to offer a set of best practices for day 2 operations for Amazon EKS. We elected to publish this guidance to GitHub so we could iterate quickly, provide timely and effective recommendations for variety of concerns, and easily incorporate suggestions from the broader community.**
    - [==Amazon EKS Best Practices Guide for Networking==](https://aws.github.io/aws-eks-best-practices/networking/index/) Intro to Amazon VPC Container Network Interface (VPC CNI) in the context of Kubernetes cluster networking. VPC CNI is the default networking plugin supported by EKS. The VPC CNI is highly configurable to support different use cases. 

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

### EKS Distro (EKS-D)

- [==aws/eks-distro==](https://github.com/aws/eks-distro) Amazon EKS Distro (EKS-D) is a Kubernetes distribution based on and used by Amazon Elastic Kubernetes Service (EKS) to create reliable and secure Kubernetes clusters.

### Testing Kubernetes Canary deployment on EKS

- [medium: Kubernetes + EKS + Canary Deployment](https://medium.com/@jerome.decoster/kubernetes-eks-canary-deployment-1ef79ae89dfc)

## AKS Azure Kubernetes Service 

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