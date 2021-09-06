# Managed Kubernetes in Public Cloud
- [Introduction](#introduction)
- [GKE vs EKS vs AKS](#gke-vs-eks-vs-aks)
- [Other Managed Kubernetes](#other-managed-kubernetes)
- [AWS EKS (Hosted/Managed Kubernetes on AWS)](#aws-eks-hostedmanaged-kubernetes-on-aws)
- [Kubesphere](#kubesphere)
- [Tools for multi-cloud Kubernetes management](#tools-for-multi-cloud-kubernetes-management)

## Introduction
* [infoworld.com: 6 reasons to switch to managed Kubernetes](https://www.infoworld.com/article/3614605/6-reasons-to-switch-to-managed-kubernetes.html) Managed Kubernetes services have matured to the point where many enterprises are handing over the keys to their clusters. Here we identify some of the main drivers behind that trend.

## GKE vs EKS vs AKS
* [medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS](https://medium.com/@Platform9Sys/kubernetes-cloud-services-comparing-gke-eks-and-aks-1fe42770cad3)
* [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.com/post/2020/02/eks-vs-gke-vs-aks/)
* [youtube: Kubernetes Comparison](https://www.youtube.com/watch?v=xM9jpcVGTzY) A beautiful comparison of Kubernetes Services from GCP, AWS and Azure by learnk8s.
    * [learnk8s.io/research:  Comparison of Kubernetes managed services 🌟](https://learnk8s.io/research)
* [medium: State of Managed Kubernetes 2020](https://medium.com/swlh/state-of-managed-kubernetes-2020-4be006643360) EKS vs. AKS vs. GKE from a Developer’s Perspective
* [medium: Managed Kubernetes Services Compared: GKE vs. EKS vs. AKS](https://medium.com/better-programming/managed-kubernetes-services-compared-gke-vs-eks-vs-aks-df1ecb22bba0) Comparing the three most popular managed Kubernetes platforms in features and overall experience.
* [acloudguru.com: AKS vs EKS vs GKE: Managed Kubernetes services compared](https://acloudguru.com/blog/engineering/aks-vs-eks-vs-gke-managed-kubernetes-services-compared)

## Other Managed Kubernetes
- [thenewstack.io: Otomi Container Platform Offers an Integrated Kubernetes Bundle](https://thenewstack.io/otomi-container-platform-offers-an-integrated-kubernetes-bundle/) If you want to enjoy the benefits of Kubernetes, configuring and installing the software itself can be just the first of many deeply technical and oftentimes confusing steps. To simplify this, many major cloud providers offer managed Kubernetes services, but even then you may need to install secondary services to handle tasks such as tracing, logging, monitoring, identity access management, and so on. The Otomi Container Platform looks to address this complexity by bundling together more than 30 different Kubernetes add-ons, as well as providing what it calls an “OSX like interface,” and today the project has open sourced a community edition under the Apache 2.0 license.
    - [otomi.io 🌟](https://otomi.io/)
    - [github: Otomi](https://github.com/redkubes/otomi-core)

<center>
<iframe src="https://www.youtube.com/embed/xM9jpcVGTzY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

## AWS EKS (Hosted/Managed Kubernetes on AWS)
* [dzone: kops vs EKS](https://dzone.com/articles/kops-vs-eks-a-comparison-guide)
* [udemy.com: amazon eks starter kubernetes on aws](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws/)
* [eksctl: EKS installer](https://github.com/weaveworks/eksctl)
* [medium: Implementing Kubernetes Cluster using AWS EKS (AWS Managed Kubernetes)](https://medium.com/@devopsadvocate/how-to-setup-kubernetes-cluster-using-aws-eks-aws-managed-kubernetes-181d5567a8ef)
* [Amazon EKS Security Best Practices](https://www.stackrox.com/post/2019/09/amazon-eks-security-best-practices/)
* [thenewstack.io: Install and Configure OpenEBS on Amazon Elastic Kubernetes Service](https://thenewstack.io/tutorial-install-and-configure-openebs-on-amazon-elastic-kubernetes-service/)
* [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS 🌟](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks/)
* [magalix.com: Deploying Kubernetes Cluster With EKS 🌟](https://www.magalix.com/blog/deploying-kubernetes-cluster-with-eks) Fargate Deployment vs. Linux Workload
* [Deploying Infrastructure (FrontEnd + BackEnd) on AWS using Amazon EKS](https://medium.com/@ghumare64/deploying-infrastructure-frontend-backend-on-aws-using-amazon-eks-5f1f426d618e)
* [EKS Service Accounts Explained](https://fika.works/blog/eks-service-accounts/) In AWS you can assign IAM permissions to pods in your cluster. This article explains how it works.
* [medium: Building the CI/CD of the Future, Creating the EKS Cluster 🌟](https://medium.com/swlh/building-the-ci-cd-of-the-future-creating-the-eks-cluster-e4cce4eb3500)
* [Announcing the AWS Controllers for Kubernetes Preview](https://aws.amazon.com/about-aws/whats-new/2020/08/announcing-the-aws-controllers-for-kubernetes-preview/)
* [daveops.xyz: Administrar usuarios en EKS](https://daveops.xyz/2020/08/25/administrar-usuarios-en-eks/)
* [aws.github.io: AWS Controllers for Kubernetes](https://aws.github.io/aws-controllers-k8s/)
* [stacksimplify.com: AWS ALB Ingress Service - Basics 🌟](https://www.stacksimplify.com/aws-eks/aws-alb-ingress/lean-kubernetes-aws-alb-ingress-basics/)
* [Kubernetes PVCs with EFS provisioner](https://www.padok.fr/en/blog/efs-provisioner-kubernetes)
* [Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
* [Running spot instances effectively with Amazon EKS](https://m.signalvnoise.com/running-spot-instances-effectively-with-amazon-eks)
* [medium: Designing a Kubernetes Cluster with Amazon EKS From Scratch 🌟](https://medium.com/adobetech/designing-a-kubernetes-cluster-with-amazon-eks-from-scratch-4b4ee9d1b8f)
* [en.sokube.ch: AWS + Kubernetes = AWS Elastic Kubernetes Service (EKS) 🌟](https://en.sokube.ch/post/aws-kubernetes-aws-elastic-kubernetes-service-eks)
* [aws.amazon.com: Operating a multi-regional stateless application using Amazon EKS](https://aws.amazon.com/blogs/containers/operating-a-multi-regional-stateless-application-using-amazon-eks/)
* [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform 🌟](https://www.clickittech.com/aws/amazon-ecs-vs-eks/)
* [POKE - Provision Opinionated Kubernetes on EKS](https://github.com/bit-cloner/poke) Poke is infrastructure as software to provision EKS cluster in an opinianated way. Code is written in nodejs utilising pulumi framework. It is opinionated in such a way to improve security and simplicity.Consider this similar to terraform module. This package can be used to provision eks clusters declaratively with immutability and repeatability.
* [clickittech.com: Kubernetes Multi tenancy with Amazon EKS: Best practices and considerations](https://www.clickittech.com/saas/kubernetes-multi-tenancy/)
* [automateinfra.com: Getting Started with Amazon Elastic kubernetes Service (AWS EKS)](https://automateinfra.com/2021/04/01/the-only-ultimate-for-beginners-getting-started-with-amazon-eks/)
* [medium: Run Kubernetes Production Environment on EC2 Spot Instances With Zero Downtime: A Complete Guide](https://medium.com/riskified-technology/run-kubernetes-on-aws-ec2-spot-instances-with-zero-downtime-f7327a95dea)
* [releaseops.io: Scaling Kubernetes Deployments in AWS with Container Insights Metrics](https://releaseops.io/blog/scaling-kubernetes-deployments-in-aws-with-container-insights-metrics)
* [medium: Create Kubernetes Cluster On AWS EKS](https://medium.com/codex/create-kubernetes-cluster-on-aws-eks-6ced4c488e62) Setup AWS credentials and install kubectl, eksctl on Ubuntu. Create Kubernetes cluster using eksctl.
* [Amazon EKS Price Reduction](https://aws.amazon.com/blogs/aws/eks-price-reduction/)
* [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS 🌟](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks/)
* [Amazon EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices/)
* [info.acloud.guru: Scaling the hottest app in tech on AWS and Kubernetes](https://info.acloud.guru/resources/kubernetes-aws-cloud-scaling-hey)
* [itnext.io: Using AWS NLB manually targeting an EKS Service exposing UDP traffic](https://itnext.io/using-aws-nlb-manually-targeting-an-eks-service-exposing-udp-traffic-17053ecd8f52)
* [Amazon EKS Now Supports EC2 Inf1 Instances](https://aws.amazon.com/blogs/aws/amazon-eks-now-supports-ec2-inf1-instances/)
* [Create a pipeline with canary deployments for Amazon EKS with AWS App Mesh 🌟](https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-eks-with-aws-app-mesh/)
* [medium: Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
* [linkedin.com: Amazon EKS Distro (EKS-D): The Kubernetes Distribution Used by Amazon EKS 🌟](https://www.linkedin.com/pulse/amazon-eks-distro-eks-d-kubernetes-distribution-used-gokul-chandra/)
* [aws.amazon.com: Introducing Federated Amazon EKS Clusters on AWS](https://aws.amazon.com/about-aws/whats-new/2021/01/introducing-federated-amazon-eks-clusters-aws/)
* [medium: How to Deploy an EKS stack in AWS?](https://medium.com/avmconsulting-blog/how-to-deploy-an-eks-stack-to-kubernetes-aws-5ec9c5a07247)
* [aws.amazon.com: Fluent Bit Integration in CloudWatch Container Insights for EKS](https://aws.amazon.com/blogs/containers/fluent-bit-integration-in-cloudwatch-container-insights-for-eks/)
* [Optimizing Your Kubernetes Clusters with Rancher and Amazon EKS 🌟](https://aws.amazon.com/blogs/apn/optimizing-your-kubernetes-clusters-with-rancher-and-amazon-eks/)
* [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform 🌟](https://www.clickittech.com/aws/amazon-ecs-vs-eks/)
* [faun.pub: Upgrading and Scaling Kubernetes cluster in AWS](https://faun.pub/upgrading-and-scaling-kubernetes-cluster-in-aws-6971b3936465)
* [youtube/StackSimplify: Kubernetes Deployments on AWS EKS | Amazon Elastic Kubernetes Service | Amazon EKS 🌟](https://www.youtube.com/watch?v=vZK_W-fpft0&ab_channel=StackSimplify)
* [cloudify.co: Simplifying Hybrid Cloud Deployments With AWS EKS And Outpost](https://cloudify.co/blog/simplifying-hybrid-cloud-deployments-with-aws-eks-and-outpost)
* [eksworkshop.com 🌟](https://www.eksworkshop.com/)
* [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes/)
* [cast.ai: 8 best practices to reduce your AWS bill for Kubernetes](https://cast.ai/blog/8-best-practices-to-reduce-your-aws-bill-for-kubernetes)
* [aws whitepapers: Architecting Amazon EKS for PCI DSS Compliance (pdf) 🌟🌟](https://d1.awsstatic.com/whitepapers/architecting-amazon-eks-for-pci-dss-compliance.pdf)
* [github.com/aws/eks-charts 🌟](https://github.com/aws/eks-charts)
* [AWS Load Balancer Controller 🌟](https://kubernetes-sigs.github.io/aws-load-balancer-controller)
* [Updating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/update-managed-node-group.html) amazon eks managed node groups now supports parallel node upgrades
* [particule.io: Create Kubernetes federated clusters on AWS](https://particule.io/en/blog/aws-federated-eks/)
* [aws.github.io/aws-eks-best-practices 🌟](https://aws.github.io/aws-eks-best-practices/)
	* [aws.github.io/aws-eks-best-practices: Networking in EKS](https://aws.github.io/aws-eks-best-practices/reliability/docs/networkmanagement)
* [betterprogramming.pub: Amazon EKS Is Eating My IPs!](https://betterprogramming.pub/amazon-eks-is-eating-my-ips-e18ea057e045) Understand how AWS EKS manages IP addresses and what you can do about it
* [engineering.salesforce.com: Optimizing EKS networking for scale](https://engineering.salesforce.com/optimizing-eks-networking-for-scale-1325706c8f6d)
* [blog.usejournal.com: Spice up Your Kubernetes Environment with AWS Lambda 🌟](https://blog.usejournal.com/spice-up-your-kubernetes-environment-with-aws-lambda-a07d81347607) In this blog you will learn a simple yet effective and secure way to integrate AWS Lambda with an existing Kubernetes environment without codes changes.
* [azon EKS Pod Identity Webhook](https://github.com/aws/amazon-eks-pod-identity-webhook) Amazon EKS Pod Identity Webhook
* [Chaos engineering on Amazon EKS using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/devops/chaos-engineering-on-amazon-eks-using-aws-fault-injection-simulator/)
* [pages.awscloud.com: GitOps on AWS for High Performing Team Operations (eBook)](https://pages.awscloud.com/GLOBAL-partner-DL-DevOps-weaveworks-ebook-2020-learn.html) Realize the full value of Kubernetes by leveraging GitOps to manage operational complexity
* [thenewstack.io: Deploy Gremlin to Amazon EKS Using AWS CloudFormation](https://thenewstack.io/deploy-gremlin-to-amazon-eks-using-aws-cloudformation/)
* [aws.amazon.com: Easy as one-two-three policy management with Kyverno on Amazon EKS 🌟](https://aws.amazon.com/blogs/containers/easy-as-one-two-three-policy-management-with-kyverno-on-amazon-eks/)
* [nextlinklabs.com: Handling Auth in EKS Clusters: Setting Up Kubernetes User Access Using AWS IAM](https://nextlinklabs.com/insights/handling-authentication-in-EKS-clusters-kubernetes-AWS-IAM)
* [neal-davis.medium.com: ECS vs EC2 vs Lambda 🌟](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)
* [faun.pub: Kubernetes Multi-tenancy with Amazon EKS: Best practices and considerations 🌟](https://faun.pub/kubernetes-multi-tenancy-with-amazon-eks-best-practices-and-considerations-60bfd78c2f9a)
* [nginx.com: Deploying NGINX Ingress Controller on Amazon EKS: How We Tested](https://www.nginx.com/blog/deploying-nginx-ingress-controller-on-amazon-eks-how-we-tested)
* [hackerxone.com: 13 Steps Guide to Create Kubernetes Cluster on AWS](https://www.hackerxone.com/2021/08/20/13-steps-guide-to-create-kubernetes-cluster-on-amazon-web-serviceaws/) 
* [hackerxone.com: Steps to Create Amazon EKS node group on Amazon web Service (AWS)](https://www.hackerxone.com/2021/08/25/steps-to-create-amazon-eks-node-group-on-amazon-web-service-aws/)
* [dev.to: EKS IAM Deep Dive 🌟](https://dev.to/aws-builders/eks-iam-deep-dive-136d)

## Kubesphere
- [kubesphere.io](https://kubesphere.io/) The Kubernetes platform tailored for hybrid multicloud. KubeSphere is a distributed operating system managing cloud native applications with Kubernetes as its kernel, and provides plug-and-play architecture for the seamless integration of third-party applications to boost its ecosystem.
- [kubekey](https://github.com/kubesphere/kubekey) The Next-gen Installer: Installing Kubernetes and KubeSphere v3.0.0 fastly, flexibly and easily
- [kubesphere.io: Scaling a Kubernetes Cluster: One of the Best Practices for Using KubeKey](https://kubesphere.io/blogs/scale-kubernetes-cluster-using-kubekey/)
- [itnext.io: Adding Master Nodes to Achieve HA: One of the Best Practices for Using KubeKey](https://itnext.io/adding-master-nodes-to-achieve-ha-one-of-the-best-practices-for-using-kubekey-6207e94b0bdd)
- [youtube: Create a Jenkins Pipeline on Kubernetes with CI/CD Pipeline Template in KubeSphere](https://www.youtube.com/watch?v=MU5LdM83x9s&t=40s&ab_channel=KubeSphere) Two built-in Jenkins pipeline templates are available in KubeSphere 3.1. DevOps team can generate CICD or customize the workflow as you need by simple drag-and-drop.

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
