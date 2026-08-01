---
description: "Top AWS resources for 2026, AI-ranked: Awesome AWS, AWS Data Pipeline and more — curated Cloud Native tools, guides and references."
---
# Public Cloud Provider. Amazon Web Services

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws/).

!!! info "Architectural Context"
    Detailed reference for Public Cloud Provider. Amazon Web Services in the context of Cloud Providers (Hyperscalers).

!!! abstract "Deep-Dive Topic Pages"
    [Serverless](./aws-serverless/) · [Storage](./aws-storage/) · [Networking](./aws-networking/) · [Security](./aws-security/) · [IaC](./aws-iac/) · [Backup](./aws-backup/) · [New Features](./aws-newfeatures/)

## Application Development

### Container Orchestration

#### App Runner

  - **(2026)** [AWS App Runner 🌟](https://aws.amazon.com/apprunner) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight outlines AWS App Runner as a fully managed container service for rapid web application and API deployment. Live Grounding confirms its position in 2026 as a premier choice for developers wanting to bypass Kubernetes complexity, offering automated load balancing, scaling, and TLS termination directly from source code or ECR.
  - **(2022)** [Architecting for resiliency on AWS App Runner](https://aws.amazon.com/blogs/containers/architecting-for-resiliency-on-aws-app-runner) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on engineering multi-region, high-availability, and fault-tolerant topologies with App Runner. Live Grounding shows that resilient patterns rely on Route 53 routing, pilot light databases, and robust custom health checks to sustain production-grade service availability.
  - **(2021)** [dev.to: AWS App Runner : How to deploy containerized applications using App Runner](https://dev.to/aws-builders/aws-app-runner-how-to-deploy-containerized-applications-using-app-runner-1f7c) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight details the operational steps for configuring and running Dockerized workloads on AWS App Runner. Live Grounding verifies this as a classic, high-value guide for transitioning traditional VMs to serverless containers without having to manage raw ECS or EKS orchestration.
### Frontend and Mobile

#### AWS Amplify

  - **(2026)** [docs.amplify.aws: Set up Amplify Auth](https://docs.amplify.aws/javascript/build-a-backend/auth/set-up-auth) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight provides a guided reference for setting up secure Cognito authentication in JS applications via Amplify. Live Grounding validates this as the standard security integration method for frontend architectures, offering seamless token management, MFA, and federated identity providers out of the box.
  - **(2022)** [blog.logrocket.com: AWS Amplify and React Native: A tutorial](https://blog.logrocket.com/aws-amplify-react-native-tutorial-examples) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight steps through the integration of AWS Amplify into React Native projects for seamless mobile backend generation. Live Grounding confirms this setup remains a highly efficient workflow, though development teams in 2026 now focus heavily on Amplify Gen 2, which utilizes TypeScript-first code-first DX.
  - **(2021)** [dev.to: 10 New AWS Amplify Features to Check Out](https://dev.to/aws/10-new-aws-amplify-features-to-check-out-4291) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight catalogues critical feature updates in AWS Amplify to accelerate full-stack delivery. Live Grounding shows that while these specific features laid the foundation, modern Amplify ecosystems have converged around Next.js SSR support and CDK-based extensibility.
### Microservices

#### E-commerce Reference

  - **(2021)** [Architecting a Highly Available Serverless, Microservices-Based Ecommerce Site](https://aws.amazon.com/blogs/architecture/architecting-a-highly-available-serverless-microservices-based-ecommerce-site) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details the design of a highly available, multi-region e-commerce platform using EventBridge, Cognito, Lambda, and DynamoDB. Live Grounding shows this architecture represents the gold standard for serverless distributed microservices, emphasizing event-driven decoupling and global data consistency.
## Application Integration

### Messaging Services

#### AWS Integration

  - **(2025)** [**Amazon SQS FAQs**](https://aws.amazon.com/sqs/faqs) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The official FAQ suite detailing Amazon SQS's scaling behavior, FIFO queue logic, dead-letter configurations, encryption capabilities, and pricing metrics.
  - **(2023)** [dev.to: Getting started with SNS and SQS](https://dev.to/aws-builders/getting-started-with-sns-and-sqs-3m4i) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a practical introduction to setting up AWS Simple Notification Service (SNS) and Simple Queue Service (SQS) patterns, outlining operational configurations for messaging-driven microservices.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - **(None)** [](https://docs.aws.amazon.com/AmazonECR/latest/userguide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - **(None)** [](https://aws.amazon.com/blogs/big-data/using-spark-sql-for-etl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.amazon.com in the Kubernetes Tools ecosystem.
  - **(None)** [](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - **(None)** [](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - **(None)** [](https://aws.amazon.com/blogs/devops/aws-codedeploy-deploying-from-a-development-account-to-a-production-account)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.amazon.com in the Kubernetes Tools ecosystem.
  - **(None)** [](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - [dzone: AWS Basics](https://dzone.com/articles/aws-basics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: AWS Basics in the Kubernetes Tools ecosystem.
  - [dzone: AWS Basics: Bastion Hosts and NAT](https://dzone.com/articles/aws-basics-bastian-hosts-and-nat)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: AWS Basics: Bastion Hosts and NAT in the Kubernetes Tools ecosystem.
  - [dzone: Five Different Ways to Build AWS Infrastructure](https://dzone.com/articles/five-different-ways-to-build-aws-infrastructure)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Five Different Ways to Build AWS Infrastructure in the Kubernetes Tools ecosystem.
## Artificial Intelligence

### Developer Agents

#### Amazon Q

  - **(2026)** [Amazon CodeWhisperer](https://aws.amazon.com/q/developer) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon Q Developer (formerly CodeWhisperer) is AWS's flagship generative AI-assisted programming agent. It generates real-time, context-aware code suggestions while performing security scanning and structural code upgrades. Live grounding demonstrates its evolution into a highly secure, enterprise-compliant workspace tool with advanced reference tracking mechanisms.
## Cloud Architecture

### Case Studies

#### Enterprise Scale

  - **(2019)** [aws.amazon.com: Trainline Case Study](https://aws.amazon.com/solutions/case-studies) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural case study mapping Trainline's migrations onto AWS using ECS containerized deployments and RDS clusters. Demonstrates successful reduction in database locking periods and outlines zero-downtime blue/green microservice delivery strategies.
## Cloud Computing

### AWS

#### Architecture and Guides

  - **(2026)** [==The Open Guide to Amazon Web Services==](https://github.com/open-guides/og-aws) <span class='md-tag md-tag--info'>⭐ 36426</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-154097fd" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 3 L 20 10 L 30 3 L 40 8 L 50 5" fill="none" stroke="url(#spark-grad-154097fd)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A massive, crowd-sourced encyclopedia offering highly critical, unvarnished technical reference material for AWS services. Distinct from official docs, it focuses on real-world engineering constraints, pricing trade-offs, and operational gotchas across storage, compute, and networking layers.
  - **(2026)** [Implementing Microservices on AWS 🌟](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The premier AWS whitepaper defining the patterns, architectures, and execution strategies for deploying microservices. It covers decomposition patterns, decentralized data management, domain-driven boundaries, service discovery, and inter-service messaging schemes.
  - **(2026)** [dev.to: Disaster Recovery Cheat-sheet/Write-up 🌟](https://dev.to/aws-builders/disaster-recovery-cheat-sheetwrite-up-o62) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A disaster recovery reference sheet translating AWS Well-Architected DR metrics (RTO and RPO) into specific execution patterns. It compares pilot light, warm standby, and active-active multi-region failover models.
  - **(2026)** [dev.to: Best Practices When Designing AWS Architecture 🌟🌟](https://dev.to/aws-builders/best-practices-when-designing-aws-architecture-4c8d) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into the operational best practices of the AWS Well-Architected Framework. Key topics include decoupling architectural dependencies, horizontal scaling mechanisms, and programmatic resource orchestration.
#### CICD and DevOps

  - **(2026)** [infoq.com: AWS Publishes Reference Architecture and Implementations for' Deployment Pipelines](https://www.infoq.com/news/2023/02/aws-deployment-pipelines) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analysis of the official AWS deployment pipeline reference architecture. Illustrates continuous delivery models for multi-environment propagation using standard GitOps patterns, automated integration suites, and strict deployment validation loops.
#### Certification Administration

  - **(2023)** [Schedule an Exam](https://aws.amazon.com/certification/certification-prep/testing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS portal dedicated to scheduling cloud certification exams via Pearson VUE. Provides essential administrative details, policy guidelines, accommodations request forms, and localized testing options.
#### Certification Training

  - **(2023)** [learn.cantrill.io 🌟](https://learn.cantrill.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highly regarded AWS architecture and networking training platform created by Adrian Cantrill. Renowned for its focus on fundamental architecture principles, production-grade labs, and deep network configuration scenarios over rote exam memorization.
  - **(2023)** [aws.amazon.com: Exámenes prácticos gratuitos y 100% en español para que obtenga su certificación](https://aws.amazon.com/es/blogs/aws-spanish/examenes-practicos-gratuitos-y-100-en-espanol-para-que-obtenga-su-certificacion) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spanish-language portal by AWS detailing official, free practice certification exams. Designed to help Spanish-speaking engineers evaluate their readiness for Cloud Practitioner and Solutions Architect exams while familiarizing themselves with localized technical vocabulary.
  - **(2023)** [AWS Certified Solutions Architect Professional – Study Guide](https://blue-clouds.com/category/study-guide) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-level technical study guide mapping key architectural domains of the AWS Certified Solutions Architect - Professional (SAP-C02) exam. Focuses on advanced multi-account design, high availability, massive scale migrations, and complex network structures.
  - **(2022)** [portal.tutorialsdojo.com: AWS Digital Courses (free)](https://portal.tutorialsdojo.com/product-category/aws/aws-digital-courses-2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Features free, highly rated, detailed AWS digital courses hosted on Tutorials Dojo. Renowned for realistic exam simulations, conceptual cheat sheets, and deep architecture breakdowns that help engineers pass AWS Associate and Professional certifications.
  - **(2022)** [linkedin: Sharing My Top 10 resources to use while preparing for AWS Certification Exams](https://www.linkedin.com/pulse/sharing-my-top-10-resources-use-while-preparing-aws-exams-semaan)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated checklist on LinkedIn highlighting ten top-tier learning resources for passing AWS certifications. Evaluates official documentation, third-party sandboxes, video bootcamps, and practice test platforms to optimize self-directed study schedules.
  - **(2022)** [dev.to: How to become a Certified AWS Solution Architect in 2022](https://dev.to/javinpaul/how-to-become-a-certified-aws-solution-architect-in-2022-35ad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed learning pathway on Dev.to detailing how to clear the AWS Certified Solutions Architect Associate (SAA-C03) exam. Recommends courses, study tips, and hands-on scenarios to build well-architected framework design principles.
  - **(2016)** [aws.amazon.com: First AWS Certification Study Guide Now Available](https://aws.amazon.com/es/about-aws/whats-new/2016/10/first-aws-certification-study-guide-now-available)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical announcement of the first official AWS Certified Solutions Architect - Associate Study Guide. While highly informative on classical concepts, modern practitioners must supplement it with current AWS documentation to address the evolved features of modern cloud services.
#### Community Learning

  - **(2023)** [community.aws/training: Training and Certification](https://builder.aws.com/learn)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The centralized AWS Builder community training site featuring articles, community-sourced tutorials, and architectural guidelines written by AWS Heroes and user group leaders worldwide.
  - **(2023)** [awscerts.slack.com](https://awscerts.slack.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated global Slack community focusing on AWS Certifications. Serves as a peer-to-peer discussion hub where developers and architects share study tips, ask technical questions, and exchange real-world infrastructure experience.
#### Containers

  - **(2026)** [==aws/containers-roadmap: AWS Containers Roadmap==](https://github.com/aws/containers-roadmap) <span class='md-tag md-tag--info'>⭐ 5350</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c477822d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 12 L 30 10 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-c477822d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The open-source public roadmap for AWS container services (ECS, EKS, ECR). It bridges developer requirements with core AWS engineering teams, offering a transparent ledger of feature designs, active developments, and historical releases.
  - **(2026)** [thenewstack.io: The AWS Shared Responsibility Model for Kubernetes](https://thenewstack.io/understand-the-aws-shared-responsibility-model-for-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical overview dissecting the limits of responsibility when managing containerized infrastructure on AWS. It contrasts the delineation of security controls between self-managed EC2 EKS node groups, managed node groups, and AWS Fargate abstractions.
  - **(2026)** [lastweekinaws.com: 17 More Ways to Run Containers on AWS](https://www.lastweekinaws.com/blog/17-more-ways-to-run-containers-on-aws) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A pragmatic, humorous breakdown of the sheer density of execution pathways for running containerized workloads on AWS. The catalog contrasts core options like ECS, EKS, App Runner, and Lightsail with lesser-known combinations, advising on cost and operational footprints.
  - **(2026)** [vladionescu.me: Scaling containers on AWS in 2022 (comparison)](https://www.vladionescu.me/posts/scaling-containers-on-aws-in-2022) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A benchmarking comparison of container orchestration engines on AWS. It evaluates cold-start limits, container provisioning metrics, and control plane auto-scaling responsiveness between ECS and EKS under enterprise workloads.
#### Infrastructure

  - **(2026)** [AWS Local Zones locations](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official matrix detailing geographic distributions and architectural specifications of AWS Local Zones. Designed for low-latency processing, these zones deploy compute, storage, and database services adjacent to major industrial hubs, bridging Edge topologies with core Regions.
  - **(2026)** [AWS Marketplace](https://aws.amazon.com/marketplace) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The centralized enterprise portal cataloging certified third-party software, AMI definitions, and SaaS integrations compatible with AWS workloads. It serves as an procurement platform, simplifying image provisioning and licensing configurations.
  - **(2026)** [cloudonaut.io: EC2 Checklist: 7 things to do after launching an instance](https://cloudonaut.io/ec2-checklist-seven-things-to-do-after-launching-an-instance) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural checklist outlining critical optimization practices immediately following EC2 virtual machine instantiation. It targets key parameters like security group isolation, IAM roles, cloud-init configuration, dynamic DNS mapping, and EBS volume performance tuning.
  - **(2026)** [AWS Architecture Blog: What to Consider when Selecting a Region for your' Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Core architectural guidance for choosing geographic AWS regions for enterprise workloads. It details standard evaluation criteria including strict data residency mandates, latency budgets relative to end-users, service availability disparities, and cost profiling.
  - **(2026)** [Building highly resilient applications with on-premises interdependencies using AWS Local Zones](https://aws.amazon.com/blogs/compute/building-highly-resilient-applications-with-on-premises-interdependencies-using-aws-local-zones) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — An enterprise resilience design guide integrating AWS Local Zones with legacy on-premises systems. It addresses key edge architectures, detailing hybrid replication strategies, localized failovers, and latency-sensitive synchronization protocols.
#### Infrastructure As Code

  - **(2021)** [New digital course and lab: AWS Cloud Development Kit (CDK) Primer](https://aws.amazon.com/about-aws/whats-new/2021/01/new-digital-course-and-lab-aws-cloud-development-kit-cdk-primer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Introduction to the AWS Cloud Development Kit (CDK) framework. Teaches developers how to define cloud infrastructure using familiar programming languages (TypeScript, Python) rather than declarative JSON or YAML, maximizing code reusability and CI/CD integration.
#### Learning and News

  - **(2026)** [aws.amazon.com/new: What's New with AWS?](https://aws.amazon.com/new) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Duplicate stream of AWS release announcements tracking core architecture, security, and developer ecosystem changes across globally distributed infrastructure zones.
  - **(2026)** [AWS Ramp-Up Guides](https://aws.amazon.com/es/training/ramp-up-guides) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curated, structured training roadmaps provided by AWS experts to build capability across role-based boundaries (Architect, Developer, DevOps). These paths organize disparate services into digestible, progressive educational units.
  - **(2026)** [dashbird.io: Get started and keep using AWS for free](https://dashbird.io/blog/use-aws-free) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A granular guide explaining strategies to optimize workload structures to remain within AWS Free Tier limits indefinitely. Ideal for early-stage prototyping, it details usage ceilings across EC2, Lambda, S3, and RDS.
  - **(2026)** [linkedin pulse: Listado de todos los Servicios de AWS (actualizado 1 de' Enero 2021)](https://www.linkedin.com/pulse/listado-de-todos-los-servicios-amazon-web-services-daniel-pe%25C3%25B1a-silva) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive directory of AWS services cataloged sequentially in Spanish. While highly structured, cloud practitioners should cross-reference with active product documentations to account for subsequent service refactoring and naming changes.
  - **(2026)** [intellipaat.com: What is AWS?](https://intellipaat.com/blog/what-is-amazon-web-services-aws) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory guide mapping AWS fundamentals, key global infrastructure concepts, and core service offerings (compute, database, and storage abstractions) tailored for engineering personnel initiating cloud transitions.
  - **(2026)** [amazon.qwiklabs.com/catalog](https://amazon.qwiklabs.com/catalog) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The portal for official interactive AWS learning environments. It provides isolated sandboxed accounts for executing practical technical labs spanning serverless orchestration, database scaling, container networking, and security auditing.
  - **(2026)** [freecodecamp.org/news/tag/aws](https://www.freecodecamp.org/news/tag/aws) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dynamic curriculum stream aggregating tutorials focused on AWS design patterns, architectural fundamentals, and software development SDK integrations.
  - **(2026)** [Jayendra's Blog 🌟🌟](https://jayendrapatil.com) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An authoritative engineering study portal focusing on AWS architectures, credential prep, and deep technical summaries of service dependencies. Valuable for validation of edge-case service limits.
  - **(2026)** [Everything AWS | Search and discover 6K+ quality AWS repositories](https://app.polymersearch.com/discover/aws) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source exploration platform indexing over 6,000 AWS repositories. It assists platform architects in discovering community-validated CDK constructs, deployment templates, and cloud helper scripts.
  - **(2026)** [dev.to: Many free and useful AWS official Dev and User guides!](https://dev.to/aws-builders/many-free-and-useful-aws-official-dev-and-user-guides-54ci) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated index compiling official AWS developer guides. It categorizes reference specifications across compute, messaging, and database domains to streamline engineering onboarding.
  - **(2026)** [Amazon Web Services Youtube](https://www.youtube.com/user/AmazonWebServices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main streaming resource channel for AWS, housing re:Invent presentations, high-level architecture reviews, and deep product feature walkthroughs.
  - **(2026)** [AWS Tutorial Series](https://www.youtube.com/user/awstutorialseries) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Educational video series focused on practical system designs on AWS, covering target configurations across networking, security policies, and standard infrastructure frameworks.
  - **(2026)** [AWS Webinar Channel](https://www.youtube.com/user/AWSwebinars) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Interactive webinar collection focusing on corporate cloud migration patterns, cost containment strategies, and AI workloads optimization within AWS environments.
  - **(2026)** [AWS Podcasts](https://aws.amazon.com/podcasts/aws-podcast) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official audio podcast network providing runtime updates, expert discussions, and inside perspectives on architectural patterns directly from AWS developers and clients.
  - **(2026)** [AWS Techchat](https://aws.amazon.com/podcasts/aws-techchat) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Region-specific developer chat podcast providing quick insights, technological reviews, and platform trend discussions for engineers working across the APJ region.
  - **(2026)** [The AWS Developer Blog now includes Python & GoLang](https://aws.amazon.com/blogs/developer) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The core technical blog for AWS developer tooling, highlighting standard SDK architectures for Python and Go, performance benchmarks, and asynchronous pipeline developments.
#### Security

  - **(2026)** [docs.aws.amazon.com: The AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The foundational blueprint for enterprise security governance in AWS. It covers multi-account Landing Zone topologies, IAM Delegations, AWS Organizations integration, Control Tower configurations, and architectural guardrails to assure regulatory compliance.
#### Serverless

  - **(2026)** [serverlessland.com](https://serverlessland.com) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The premier AWS-managed serverless knowledge hub. It serves as an architectural repository for designing events, writing Lambda configurations, orchestrating Step Functions, and keeping abreast of serverless pattern trends globally.
### Training

#### Community Learning (1)

  - **(2022)** [twitch.tv/acloudguruofficial](https://www.twitch.tv/acloudguruofficial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Interactive live streaming channel by A Cloud Guru. Features technical walkthroughs, Q&A sessions, real-time live-labs, and exam prep discussions, serving as a live community resource for DevOps engineers and cloud architects.
#### Educational Resources

  - **(2021)** [analyticsindiamag.com: Free Online Resources To Get Started On Cloud Computing](https://analyticsindiamag.com/free-online-resources-to-get-started-on-cloud-computing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compiles high-quality, free resources to master fundamental cloud computing concepts. Lists tutorials, official cloud vendor training pathways, and community projects to help newcomers build structured knowledge in distributed systems.
#### Multi-cloud Education

  - **(2023)** [acloudguru.com](https://www.pluralsight.com/cloud-guru)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A premier e-learning platform (now part of Pluralsight) specializing in cloud computing, DevOps, and container certifications (AWS, Azure, GCP, Kubernetes). Provides hands-on sandbox environments and deep technical pathways designed to train enterprise-grade engineering organizations.
## Cloud Infrastructure

### AWS (1)

#### Application Deployment

  - **(2016)** [Creating and Deploying PHP Applications on AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP_eb.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step developer guide for compiling, structuring, and launching robust PHP packages on AWS Beanstalk. Documents configuring system environment files and customized runtime settings.
#### Application Platform Updates

  - **(2016)** [AWS Elastic Beanstalk Supports ASP.NET Core and Multi-App .NET Support](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-asp-net-core-and-multi-app-net-support) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the 2016 platform expansion adding native support for ASP.NET Core applications and multi-app configuration models in Elastic Beanstalk Windows instances.
#### Best Practices

  - **(2014)** [AWS Tips I Wish I'd Known Before I Started (Feb 2014)](https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A collection of fundamental AWS operational constraints including early patterns in IAM, billing, and VPC configuration. Although dated, it outlines core architectural traps teams still solve using Control Tower.
#### Cloud Migration

  - **(2016)** [AWS Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — AWS service that inventories and parses physical and virtual systems inside legacy on-premises environments. Maps active server dependencies and gathers CPU, RAM, and network utilization profiles to plan cloud migrations.
  - **(2016)** [AWS Application Discovery Service Update – Agentless Discovery for VMware](https://aws.amazon.com/blogs/aws/aws-application-discovery-service-update-agentless-discovery-for-vmware) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS announcement showing how Application Discovery Service interfaces directly with VMware vCenter environments. Avoids OS agent dependencies to quickly construct VM topology maps.
#### Configuration Management

  - **(2016)** [youtube: AWS OpsWorks Overview and Demo](https://www.youtube.com/watch?v=cj_LoG6C2xk&list=PLR3sVanzLpJN6BiYS20K4BMPpiDGifbZy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual and technical walkthrough demonstrating configuration layers, application deployments, and runtime lifecycle hooks executed via AWS OpsWorks stack engines.
  - **(2013)** [AWS OpsWorks](https://aws.amazon.com) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A managed configuration management platform utilizing Chef or Puppet layers. *2026 Engineering Reality*: Now classified as legacy, with standard DevOps workflows adopting AWS Systems Manager (SSM) and Terraform for infrastructure automation.
#### Container Compute

  - **(2024)** [Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reference manual for the AWS-engineered Amazon Machine Image (AMI) preconfigured with the ECS agent, Docker runtime, and optimal container configurations. Utilizing this specialized OS image ensures maximum orchestration performance, reliable telemetry, and security compliance out of the box.
#### Container Orchestration (1)

  - **(2023)** [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive comparing AWS ECS, EKS, and serverless container execution via AWS Fargate. Synthesizing live cloud architectural trends, it presents insights into financial management, operational simplicity, and dynamic resource scaling, mapping out the trade-offs of using managed VM pools versus completely serverless options.
  - **(2022)** [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform](https://www.clickittech.com/cloud-services/amazon-ecs-vs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This comprehensive comparison highlights the operational differences, cost implications, and architecture layouts of Amazon ECS versus Amazon EKS. EKS targets standard Kubernetes-based deployments requiring high portability, while ECS is a highly optimized, opinionated AWS native orchestrator designed for seamless integration.
  - **(2021)** [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed comparative analysis of scaling strategies between Amazon ECS and EKS clusters. The article walks through key operational considerations, including EC2 Auto Scaling Groups, Karpenter, cluster autoscalers, and resource utilization dynamics, highlighting how choice of orchestration influences microservices scale limits.
#### Container Registries

  - **(2024)** [Amazon EC2 Container Registry Documentation](https://aws.amazon.com/es/documentation/ecr) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official engineering reference for Amazon ECR, a fully managed OCI-compliant container registry. It covers critical security integrations, image scanning capabilities, cross-region replication configurations, and direct integration with Amazon ECS/EKS to facilitate safe, high-speed container pull actions.
#### Continuous Deployment

  - **(2021)** [Automate rollbacks for Amazon ECS rolling deployments with CloudWatch alarms](https://aws.amazon.com/blogs/containers/automate-rollbacks-for-amazon-ecs-rolling-deployments-with-cloudwatch-alarms) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural guide outlining automated deployment rollback capabilities within ECS rolling deployments. It illustrates how CloudWatch alarms can monitor application health (e.g., HTTP 5xx rates) during active deployments and automatically trigger rollbacks to a previously stable revision to maintain high availability.
#### ETL

  - **(2025)** [==AWS Data Pipeline==](https://aws.amazon.com/glue) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official page of AWS Glue, a fully managed serverless data integration service. Identifies structural discovery using AWS Glue Data Catalog, PySpark ETL execution, and schema registry controls.
  - **(2025)** [AWS Data Pipeline Documentation](https://docs.aws.amazon.com/data-pipeline) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Classic developer documentation for AWS Data Pipeline. Details the scheduling of batch workflows across EC2 and EMR resources (largely superseded by modern AWS Glue and Step Functions setups).
  - **(2024)** [AWS Big Data Blog: Category - AWS Data Pipeline](https://aws.amazon.com/blogs/big-data/category/analytics/aws-data-pipeline) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — Technical blog category detailing legacy deployment setups for AWS Data Pipeline, providing structural templates for data movements before cloud-native ETL tools gained dominance.
#### Event Streaming

  - **(2016)** [**Querying Amazon Kinesis Streams Directly with SQL and Spark Streaming**](https://aws.amazon.com/blogs/big-data/querying-amazon-kinesis-streams-directly-with-sql-and-spark-streaming) <span class='md-tag md-tag--warning'>[SCALA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Technical blueprint detailing Spark Streaming integration with Amazon Kinesis streams. Discusses record-processing window optimizations, checkpoint configurations, and SQL querying on live event pipelines.
#### Event-driven Architecture

  - **(2020)** [Building an event-driven application with Amazon EventBridge](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This AWS architecture blog details how to design and build serverless event-driven applications using Amazon EventBridge. It highlights the platform's ability to act as a centralized serverless event bus that simplifies decoupled communication across distributed microservices by routing events using declarative rules. The pattern eliminates custom routing code, improving structural robustness.
#### Governance

  - **(2021)** [AWS Architecture Blog: Use templated answers to perform Well-Architected reviews at scale](https://aws.amazon.com/blogs/architecture/use-templated-answers-to-perform-well-architected-reviews-at-scale) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical review detailing templated governance answers to scale AWS Well-Architected reviews. Offers architects a mechanism to automate and standardise security compliance reviews across decentralized environments.
#### Hybrid Cloud

  - **(2017)** [VMware Cloud on AWS](https://aws.amazon.com/es/vmware) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official architectural landing page for VMware Cloud on AWS. Outlines SDDC framework deployments on bare-metal infrastructure, enabling disaster recovery, capacity bursting, and seamless VM migrations.
#### Infrastructure Apis

  - **(2021)** [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed programmatic standard for the Cloud Control API. Unifies CRUDL interactions across hundreds of AWS resource classes and third-party integration schemas, facilitating custom provisioning engine designs.
  - **(2021)** [AWS Cloud Control API, a Uniform API to Access AWS & Third-Party Services](https://aws.amazon.com/blogs/aws/announcing-aws-cloud-control-api) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official blog introduction announcing the Cloud Control API. Discusses how standardization simplifies life for infrastructure-as-code creators (e.g., Terraform, Pulumi) by delivering instant support for new cloud capabilities.
#### Legacy Systems

  - **(2022)** [cbui.dev: Every company has an "old" production AWS account](https://www.cbui.dev/every-company-has-an-old-production-aws-account) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Explores patterns for managing single legacy production accounts containing unmapped dependencies. Details modernization pathways using AWS Organizations and VPC peering strategies.
#### Legacy Tooling

  - **(2016)** [Using Docker Machine with AWS](https://blog.scottlowe.org/2016/03/22/using-docker-machine-with-aws) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Detailed technical blog post showing how to provision and manage remote Docker engines on AWS using the deprecated Docker Machine utility. While valuable for historical debugging and legacy architecture comprehension, live industry alignment dictates migrating to modern Cloud API alternatives (such as AWS CLI, Terraform, or Rancher).
  - **(2016)** [Docker Datacenter on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/es/about-aws/whats-new/2016/06/docker-datacenter-on-the-aws-cloud-quick-start-reference-deployment) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Quick Start guide detailing the automated orchestration of Docker Datacenter (now Mirantis Kubernetes Engine) on AWS. It serves as an architectural design reference from the pre-Kubernetes dominance era, describing multi-zone registry configurations, control planes, and Swarm-based container engines.
#### Load Balancing

  - **(2016)** [AWS Elastic Beanstalk Supports Application Load Balancer](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-application-load-balancer) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Product release documentation outlining integration of Application Load Balancers (ALBs) with Elastic Beanstalk. Unlocks path-based routing, target group pooling, and secure WebSocket connections.
#### Messaging Services (1)

  - **(2022)** [dev.to: When to SNS or SQS](https://dev.to/aws-builders/when-to-sns-or-sqs-2aji) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical comparison of Amazon Simple Notification Service (SNS) and Simple Queue Service (SQS) within event-driven architectures. It details SNS's pub-sub push mechanism versus SQS's pull-based queueing model, analyzing throughput characteristics and decoupling strategies. This guide clarifies architectural patterns for integrating microservices via point-to-point and fan-out message routing.
#### Paas Architecture

  - **(2016)** [Deploying a High-Availability PHP Application with an External Amazon RDS Database to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-ha-tutorial.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS deployment blueprint detailing how to structure a multi-availability zone PHP application using Beanstalk. Integrates an external multi-AZ Amazon RDS configuration to build failover resilience.
#### Resources

  - **(2026)** [==Awesome AWS 🌟==](https://github.com/donnemartin/awesome-aws) <span class='md-tag md-tag--info'>⭐ 14064</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d21f40c7" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 13 L 20 6 L 30 2 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-d21f40c7)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier reference catalog for Amazon Web Services (AWS), containing curated libraries, open-source utilities, and official whitepapers. It covers key compute, storage, networking, and serverless components. It is universally recognized as the gold standard resource for AWS-centric platform engineering teams seeking validated architectural patterns.
#### Security (1)

  - **(2021)** [thenewstack.io: Avoid the 5 Most Common Amazon Web Services Misconfigurations in Build-Time](https://thenewstack.io/avoid-the-5-most-common-amazon-web-services-misconfigurations-in-build-time) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on build-time CloudFormation and Terraform configuration errors. Outlines practical strategies for shifting infrastructure security check operations left into standard CI/CD pipelines.
#### Security Practices

  - **(2022)** [dev.to: Sharing secrets to ECS in an AWS multi-account architecture](https://dev.to/aws-builders/sharing-secrets-to-ecs-in-an-aws-multi-account-architecture-5h1i) <span class='md-tag md-tag--warning'>[TERRAFORM CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical blueprint for cross-account secret management for Amazon ECS using AWS Secrets Manager and Systems Manager (SSM) Parameter Store. It provides security engineers with an architectural approach to maintain strict separation of concerns, principal-of-least-privilege IAM policies, and cross-account IAM role assumption.
#### Web Servers

  - **(2016)** [AWS Elastic Beanstalk Supports Nginx Proxy Server with Tomcat](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-nginx-proxy-server-with-tomcat) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Feature documentation announcing native Nginx reverse proxy configurations sitting in front of Apache Tomcat platforms in Beanstalk. Optimizes delivery of static assets and client routing.
### AWS Automation

#### Serverless Orchestration

  - **(2026)** [Enhanced Local IDE Experience for AWS Step Functions](https://aws.amazon.com/blogs/compute/introducing-an-enhanced-local-ide-experience-for-aws-step-functions) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details local IDE integration utilities for designing and tracing AWS Step Functions. Enhances developer inner-loops by rendering local visual workflow representations and offering live Amazon States Language schema validation directly in-editor.
### AWS Ecosystem

#### Audio Learning

  - **(2026)** [Stitcher AWS Podcasts](https://www.stitcher.com/podcast/amazon-web-services/aws-podcast)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Stitcher repository hosting the AWS Podcast network. Features architectural retrospectives, engineering deep-dives, and service evolution analyses presented by active cloud product managers.
#### Cloud Services

  - **(2026)** [AWS DevOps 🌟](https://aws.amazon.com/devops) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS’s primary DevOps portal, presenting their native continuous delivery and infrastructure management stack, including CodePipeline, CodeBuild, and CloudFormation. While curator listings highlight frictionless integration with EC2 and ECS, live architectural patterns in 2026 showcase teams frequently combining AWS-native compute with cloud-agnostic deployment runtimes to avoid platform lock-in.
#### Open Source Strategy

  - **(2026)** [infoworld.com: Amazon’s quiet open source revolution](https://www.infoworld.com/article/2338356/amazon-s-quiet-open-source-revolution.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical exploration detailing AWS's transition from open-source software consumer to an active co-developer and primary maintainer. Discusses strategic projects like OpenSearch and Valkey, examining the structural tension and evolving relationships between public clouds and software vendors.
#### Presentation Resources

  - **(2026)** [slideshare.net/AmazonWebServices](https://www.slideshare.net/AmazonWebServices) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — AWS SlideShare platform resource aggregating architectural blueprints, slide decks, and high-impact event summaries. While SlideShare represents a legacy presentation vector, it serves as a historic archive for tracking AWS service launch topologies and historical enterprise cloud migration case studies.
#### Social Channels

  - **(2026)** [twitter.com/awscloud](https://x.com/awscloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS communication broadcast feed utilized for instant notification of novel system capabilities, security alerts, and broad strategic initiatives across the AWS global infrastructure.
  - **(2026)** [twitter.com/AWSreInvent](https://x.com/AWSreInvent)  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Targeted social broadcast hub cataloging major releases, technical breakout session highlights, and real-time architectural reveals emerging from the annual AWS re:Invent technology conference.
  - **(2026)** [twitter.com/jeffbarr](https://x.com/jeffbarr)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Social feed of AWS Chief Evangelist Jeff Barr. Serves as a high-density channel supplying core architectural context, feature releases, and developer-focused service insights.
  - **(2026)** [twitter.com/AWSstartups](https://x.com/AWSstartups)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Targeted channel broadcasting AWS architectural optimizations, funding, and growth accelerators tailored specifically for high-velocity startup infrastructure teams.
  - **(2026)** [twitter.com/AWS_Partners](https://x.com/AWS_Partners)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Partner Network channel presenting compliance benchmarks, MSP programs, system integrator partnerships, and cloud consulting framework updates.
#### Startup Enablement

  - **(2026)** [AWS Activate](https://aws.amazon.com/startups)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Activate platform framework delivering technical resources, infrastructure credits, and active mentorship pathways to startup founders. Promotes rapid prototyping by offloading cloud infrastructure costs and supplying pre-configured template architectures.
### AWS Services

#### Hands-on Tutorials

  - **(2026)** [AWS 10-Minute Tutorials](https://aws.amazon.com/getting-started/hands-on)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An onboarding portal featuring bite-sized, 10-minute technical exercises across core services (EC2, S3, RDS). These tutorials utilize guided steps to help engineers rapidly spin up cloud resources while demonstrating fundamental networking, security, and storage architecture patterns.
#### Interactive Learning

  - **(2026)** [workshops.aws: AWS Workshops](https://builder.aws.com/build/workshops?trk=265ae1c7-2dfc-44c6-bc73-a4d991b8bd7f&sc_channel=el)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS-designed workshop aggregator offering deep, interactive labs on advanced engineering themes. Topics span Elastic Kubernetes Service (EKS) design, serverless microservices pipelines, security automation, and native database configurations under realistic operational profiles.
### Application Integration (1)

#### Serverless Services

  - **(2026)** [k21academy.com: AWS Application Services: Lambda, SES, SNS, SQS, SWF](https://k21academy.com/aws-cloud/aws-application-services)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical review of AWS's modular application integration portfolio. Contrasts serverless compute (Lambda) with asynchronous message queues (SQS), publish-subscribe event routing (SNS), programmatically orchestrated state workflows (SWF/Step Functions), and secure outbound transaction messaging (SES).
### Architecture and Strategy

#### Cloud Adoption Framework

  - **(2021)** [AWS Cloud Adoption Framework (CAF) 3.0 is Now Available](https://aws.amazon.com/blogs/aws/aws-cloud-adoption-framework-caf-3-0-is-now-available) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The AWS Cloud Adoption Framework (CAF) 3.0 provides a strategic roadmap for enterprises migrating workloads to the cloud. Focusing on six foundational perspective areas—Business, People, Governance, Platform, Security, and Operations—this framework incorporates modern cloud-native architectural patterns. It serves as an essential organizational blueprint for accelerating digital transformation while minimizing systemic risk.
### Community and Support

#### AWS Repost

  - **(2021)** [AWS re:Post – A Reimagined Q&A Experience for the AWS Community](https://aws.amazon.com/blogs/aws/aws-repost-a-reimagined-qa-experience-for-the-aws-community) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — AWS re:Post replaces legacy AWS Forums with an interactive, community-driven Q&A platform to accelerate technical troubleshooting and knowledge sharing. Featuring gamified reputation models and expert moderation, it offers verified answers on complex architectural questions. It serves as a vital knowledge repository for builders aiming to resolve configuration anomalies and adopt best-practice designs.
  - **(2021)** [infoq.com: Amazon Introduces re:Post, a "Stack Overflow" for AWS](https://www.infoq.com/news/2021/12/amazon-repost-questions-answers) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An independent review of AWS re:Post, describing it as a specialized, community-driven alternative to general-purpose QA boards like Stack Overflow. The analysis focuses on how verified answers and direct AWS engineer contributions reduce troubleshooting cycles for platform operators. The platform helps developers bypass outdated configuration guides in favor of modern, validated architectural patterns.
### Compliance and Governance

#### AWS Config

  - **(2026)** [acloudguru.com: 12 AWS Config rules that every account should have](https://www.pluralsight.com/resources/blog/cloud/12-aws-config-rules-that-every-account-should-have)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated reference guide identifying 12 essential AWS Config rules required to establish enterprise compliance baselines. Focuses on declarative drift detection including mandatory MFA enforcement, S3 block public access configurations, and unattached volume cleanup.
  - **(2016)** [AWS Config Rules now available in 4 new regions: US West (Oregon), EU (Ireland),' EU (Frankfurt) and Asia Pacific (Tokyo)](https://aws.amazon.com/about-aws/whats-new/2016/04/aws-config-rules-now-available-in-4-new-regions-us-west-oregon-eu-ireland-eu-frankfurt-and-asia-pacific-tokyo) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This release details the regional expansion of AWS Config Rules, enabling continuous compliance auditing and resource monitoring in multiple global zones. AWS Config Rules allow operators to evaluate resource configurations against organizational standards and security policies dynamically. This multi-region support is architecturally significant for companies running highly distributed systems that must comply with regional data governance rules.
### Database Migration

#### Whitepapers

  - **(2019)** [**Whitepaper: Migrating Your Databases to AWS**](https://aws.amazon.com/dms/?audit=2019q1) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight offers a comprehensive methodology and step-by-step guidance for planning and executing database migrations to AWS. Live Grounding reviews key architectural patterns, conversion tools (AWS SCT), and common anti-patterns. Crucial reading for enterprise modernization and cloud adoption planning.
### Databases

#### Managed Mysql

  - **(2021)** [percona.com: The Benefits of Amazon RDS for MySQL](https://www.percona.com/blog/the-benefits-of-amazon-rds-for-mysql) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight emphasizes Percona's neutral evaluation of the trade-offs of hosting MySQL on Amazon RDS. Live Grounding confirms the study analyzes management convenience against limitations in configuration flexibility and performance tuning. Highly useful for database administrators comparing DIY cloud hosting with managed services.
### Ecosystem

#### AWS Partners

  - **(2026)** [AWS Partner Network](https://aws.amazon.com/partners) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the portal for finding verified APN Technology and Consulting partners. Live Grounding shows AWS Partner Network remains the core commercial engine for AWS, facilitating ISV integrations, validated architectures, and professional service engagements globally.
#### Case Studies (1)

  - **(2025)** [AWS Partner Network (APN) blog](https://aws.amazon.com/blogs/apn) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on architecture walkthroughs, such as deploying high-availability services on AWS using Spotinst (now Spot by NetApp) and configuring Active Directory SSO. Live Grounding validates these blog posts as critical operational blueprints for multi-tenant integrations and cost-optimization strategies in enterprise environments.
### Enterprise Migration

#### Frameworks

  - **(2026)** [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The AWS Cloud Adoption Framework (AWS CAF) defines a structured architectural approach to enterprise cloud migration. Evaluates six primary organizational perspectives to securely de-risk large-scale cloud transformations.
### Event Streaming (1)

#### Comparison

  - **(2021)** [**whizlabs.com: AWS Kinesis vs Kafka Apache**](https://www.whizlabs.com/blog/kinesis-vs-kafka) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Comparative architectural review between AWS Kinesis and Apache Kafka. Analyzes data retention policies, throughput capabilities, scaling overheads, and total cost of ownership (TCO) profiles.
### Finops

#### Cost Management

  - **(2015)** [AWS Cost Explorer Update – Access to EC2 Usage Data](https://aws.amazon.com/blogs/aws/aws-cost-explorer-update-access-to-ec2-usage-data) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes early programmatic access to granular EC2 metrics inside Cost Explorer. Provides foundational methodologies for early-stage cloud-native resource optimization and FinOps planning.
#### Cost Optimization

  - **(2023)** [treblle.com: How does Treblle scale on AWS without breaking the bank?](https://treblle.com/blog/how-does-treblle-scale-on-aws-without-breaking-the-bank) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights Treblle’s architectural strategy for processing billions of API requests on AWS affordably. Live Grounding details how modern SaaS platforms leverage spot instances, API gateway caching, serverless scale-to-zero databases, and intensive performance profiling to decouple traffic volume from infrastructure costs.
### Finops and Cloud Optimization

#### Sustainability

  - **(2023)** [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An engineering guide to optimizing AWS compute architectures for sustainability. Explores Graviton migrations, automated container resizing, and target serverless setups to lower carbon emissions.
### Finops and Sustainability

#### Green Ops

  - **(2022)** [aws.amazon.com: Optimize your modern data architecture for sustainability: Part 1 – data ingestion and data lake](https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight introduces architectural paradigms for building carbon-efficient data ingestion pipelines and S3 data lakes on AWS. Live Grounding emphasizes that GreenOps and carbon tracing are major metrics in 2026, where design patterns like intelligent tiering, optimal compression (Parquet), and ARM64-based Graviton instances directly reduce environmental footprint.
### High Performance Computing

#### Life Sciences

  - **(2020)** [aws.amazon.com: Creating a digital map of COVID-19 virus for discovery of new treatment compounds](https://aws.amazon.com/blogs/hpc/creating-a-digital-map-of-covid-19-virus-for-discovery-of-new-treatment-compounds) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight captures the orchestration of highly parallelized, massive HPC grids on AWS to model viral interactions. Live Grounding confirms that AWS's modern HPC offerings (ParallelCluster, Batch, and FSx for Lustre) remain pivotal for global health research, processing exabytes of genomic data in record time.
### Identity and Access

#### Account Administration

  - **(2026)** [How do I create and activate a new Amazon Web Services account?](https://repost.aws/knowledge-center/create-and-activate-aws-account) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Knowledge Center guide outlining the prerequisite multi-step verification, billing enablement, and security configurations required to bootstrap a brand-new AWS root account. Explains the foundational processes necessary to activate core global regions safely.
### Infrastructure As Code (1)

#### AWS CLI

  - **(2026)** [Convert AWS console actions to reusable code with AWS Console-to-Code, now generally available](https://aws.amazon.com/blogs/aws/convert-aws-console-actions-to-reusable-code-with-aws-console-to-code-now-generally-available/?trk=0d3532c8-5f49-4c86-9683-96c2417e9b4b&sc_channel=el) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the GA release of AWS Console-to-Code. This utility records visual, interactive browser actions within the AWS Console and programmatically translates them into clean, reusable Infrastructure-as-Code (IaC) formats, such as AWS CDK and CloudFormation, using generative AI models.
### Iot and Edge

#### AWS Iot Core

  - **(2026)** [What Is AWS IoT?](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight maps AWS IoT as the entry point for connecting physical devices to AWS cloud services. Live Grounding confirms it has evolved into a robust suite of services (Core, Greengrass, Device Defender) handling billions of messages daily. It provides secure, bi-directional communication with MQTT/HTTPS and acts as the foundational layer for enterprise IoT data ingestion.
### Migration

#### AWS MGN

  - **(2026)** [AWS Cloud Endure Migration](https://aws.amazon.com/application-migration-service) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight maps the evolution of CloudEndure into AWS Application Migration Service (AWS MGN). Live Grounding confirms AWS MGN is the primary enterprise engine for lift-and-shift migrations, maintaining block-level replication of physical, virtual, or cloud-based servers directly to AWS target instances.
### Operations

#### Service Quotas

  - **(2026)** [AWS API: get-service-quota](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/get-service-quota.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight describes the AWS CLI reference for auditing specific service limits. Live Grounding highlights its mandatory use in modern GitOps and IaC (Terraform/Pulumi) pipelines to preemptively validate account thresholds before executing large-scale resource provisioning.
  - **(2025)** [How can I troubleshoot errors using the AWS CLI to manage my service quota requests?](https://repost.aws/es/knowledge-center/troubleshoot-service-quotas-cli-commands) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight targets the diagnostics and troubleshooting workflows for managing AWS service quotas programmatically. Live Grounding points to this as a vital operational playbook for SRE teams, helping avoid throttling and deployment blocks during dynamic scaling by automating quota requests via CLI and API.
### Operations and Governance

#### AWS Systems Manager

  - **(2021)** [Multi-account AWS Trusted Advisor summaries now available in AWS Systems Manager Explorer](https://aws.amazon.com/blogs/mt/multi-account-aws-trusted-advisor-summaries-now-available-aws-systems-manager-explorer) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This technical integration consolidates multi-account AWS Trusted Advisor recommendations directly within AWS Systems Manager Explorer. This consolidation provides architects with a single-pane-of-glass dashboard for monitoring cost optimization, security, fault tolerance, and operational efficiency across entire AWS Organizations. Architecturally, it streamlines administrative overhead and improves governance visibility at scale.
### Security and Incident Response

#### AWS Systems Manager (1)

  - **(2021)** [How to automate incident response to security events with AWS Systems Manager Incident Manager](https://aws.amazon.com/blogs/security/how-to-automate-incident-response-to-security-events-with-aws-systems-manager-incident-manager) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This guide outlines how to automate security incident response workflows using AWS Systems Manager Incident Manager. It details how to leverage custom runbooks, notify on-call teams, and orchestrate automated mitigations for resource degradation or security breaches. Utilizing these automated workflows drastically reduces the Mean Time to Resolution (MTTR) while enforcing uniform incident management standards across distributed environments.
### Training (1)

#### Practical Labs

  - **(2021)** [acloudguru.com: 10 fun hands-on projects to learn AWS](https://www.pluralsight.com/resources/blog/cloud/10-fun-hands-on-projects-to-learn-aws)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Suggests 10 hands-on AWS training projects designed for cloud engineers. Covers deploying static architectures under HTTPS, building simple serverless APIs, and setting up automated backup pipelines.
### Troubleshooting

#### DevOps Challenges

  - **(2026)** [acloudguru.com: The Cloud Dictionary of Pain: Five Of AWS’s Toughest Cloud Topics](https://www.pluralsight.com/resources/blog/cloud/the-cloud-dictionary-of-pain-five-of-awss-toughest-cloud-topics) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive technical overview evaluating complex AWS configurations, pinpointing notorious friction points such as IAM policy composition, KMS key management, AWS Billing structures, and hybrid VPC peering. Provides architectural guidance to bypass structural anti-patterns.
### Virtual Private Servers

#### AWS Lightsail

  - **(2026)** [AWS LightSail](https://aws.amazon.com/lightsail) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents AWS Lightsail as a simplified, cost-predictable virtual private server (VPS) alternative to raw EC2. Live Grounding confirms Lightsail is widely used in 2026 for small-scale projects, staging environments, and rapid WP deployments, offering pre-configured blueprints and straightforward billing.
## Cloud Native

### AWS (2)

#### Governance (1)

##### AWS Organizations

  - **(2024)** [AWS Organizations: The Key to Managing Your Cloud Infrastructure Effectively](https://awsfundamentals.com/blog/aws-organizations-the-key-to-managing-your-cloud-infrastructure-effectively)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores core configuration benefits of AWS Organizations for multi-account governance. Highlights service control policies (SCPs), unified billing, and secure programmatic account instantiation using IaC.
### Kubernetes

#### Rancher Management

  - **(2022)** [aws-quickstart.github.io: Rancher on the AWS Cloud. Quick Start Reference Deployment](https://aws-quickstart.github.io/quickstart-eks-rancher) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS Quick Start reference guide for standing up Rancher on AWS. This architecture installs Rancher on an Amazon EKS cluster, giving enterprise operations teams a unified interface to govern multiple downstream clusters, enforce unified RBAC models, and manage complex multi-tenant environments.
## Cloud Native Infrastructure

### Service Mesh

#### AWS (3)

  - **(2022)** [aws.amazon.com/app-mesh](https://aws.amazon.com/app-mesh) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Live Grounding Synthesis: Built on Envoy as AWS's managed service mesh, AWS App Mesh was deprecated in late 2024 and fully sunsetted. Platform teams are urged to transition to Amazon ECS Service Connect or Amazon VPC Lattice.
## Cloud Native Platforms

### AWS (4)

#### Managed Observability

  - **(2026)** [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS fully-managed metric service designed around open-source Cortex core architecture. Automatically scales telemetry storage, ingestion, and query resources in secure enterprise environments.
## Cloud Platform

### AWS Infrastructure

#### CICD

  - **(2026)** [Amazon CodeCatalyst](https://codecatalyst.aws/explore) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon CodeCatalyst is an enterprise-grade cloud development service that streamlines software delivery on AWS. It integrates team collaboration, CI/CD, issue tracking, and cloud development environments (CDEs) under a unified SaaS framework. Crucial for software engineering directors establishing rapid, compliant application delivery loops.
  - **(2021)** [dev.to: Continuous Integration and Deployment on AWS - and a wishlist for CI/CD Tools on AWS](https://dev.to/aws-builders/continuous-integration-and-deployment-on-aws-and-a-wishlist-for-cicd-tools-on-aws-5a13) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Dev.to article discussing CI/CD architectures within AWS environments, containing a developer wishlist for next-generation pipeline features. It compares CodePipeline, GitHub Actions, and custom runners, detailing trade-offs in execution speeds, artifact management, and IAM-gated controls. Perfect for team leads structuring secure platform automation.
#### CLI Tooling

  - **(2026)** [Amazon CLI Documentation](https://aws.amazon.com/cli) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main landing and installation documentation portal for the AWS Command Line Interface. It acts as the definitive source for setting up the CLI across macOS, Linux, and Windows environments. Essential for establishing standard terminal configurations and programmatic environment variables across both developer workstations and CI/CD agents.
  - **(2021)** [Announcing the end of support for Python 2.7 in the AWS SDK for Python and AWS CLI v1](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-python-2-7-in-aws-sdk-for-python-and-aws-cli-v1) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — An official AWS deprecation announcement marking the end of Python 2.7 support within the AWS SDK for Python (Boto3) and AWS CLI v1. It details migration paths to modern Python 3.x runtimes and the container-native AWS CLI v2 architecture. Critical reading for legacy system maintainers undergoing platform modernization initiatives.
#### Cost Optimization (1)

  - **(2026)** [vantage.sh](https://www.vantage.sh) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Vantage.sh is a modern cloud cost management (FinOps) platform providing deep visibility into AWS, Snowflake, and Kubernetes expenditures. It aggregates resource usage metrics to recommend automated saving policies, RI purchasing, and spot transitions. Grounding confirms its role as a premier enterprise tool to manage complex multi-cloud financial posture.
  - **(2021)** [techcrunch.com: Vantage makes managing AWS easier](https://techcrunch.com/2021/01/12/vantage-makes-managing-aws-easier) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A TechCrunch feature analyzing how Vantage simplifies AWS cost tracking and optimization, offering deep contrast to complex cloud bills. The article highlights Vantage's rise as an essential interface for development organizations navigating fine-grained container pricing and resource usage. Key reading for CFOs and cloud finance architects.
#### Developer Sdks

  - **(2026)** [AWS SDK for Java](https://aws.amazon.com/sdk-for-java) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main portal for the AWS SDK for Java, featuring setup guides, performance tuning notes, and integration standards. It is the foundational SDK for Java-based enterprise applications leveraging S3, DynamoDB, or AWS Lambda. Crucial for software engineers designing highly resilient cloud applications using modern async client wrappers.
#### Developer Tooling

  - **(2026)** [AWS Management Tools Blog](https://aws.amazon.com/blogs/mt) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official AWS Management and Governance Tools Blog, serving as the authority on systems manager, Config, CloudTrail, and CloudWatch updates. It hosts standard architectures for designing observability frameworks and cloud optimization. Crucial for enterprise platform administrators ensuring alignment with modern AWS best practices.
  - **(2023)** [aws.amazon.com/blogs: Introducing Amazon CodeWhisperer for command line](https://aws.amazon.com/blogs/devops/introducing-amazon-codewhisperer-for-command-line) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS Developer blog introducing automated command-line capabilities for Amazon CodeWhisperer. It highlights AI-driven command completion and automatic CLI parameter translation directly in modern terminal emulators. Essential for platform engineers aiming to dramatically accelerate shell and infrastructure-as-code scripting efficiency.
  - **(2022)** [genbeta.com: Amazon lanza CodeWhisperer, su propia alternativa a GitHub Copilot… que no insertará código ya licenciado sin avisar](https://www.genbeta.com/desarrollo/amazon-lanza-codewhisperer-su-propia-alternativa-a-github-copilot-que-no-insertara-codigo-licenciado-avisar) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Spanish Genbeta article introducing Amazon CodeWhisperer as AWS's direct competitor to GitHub Copilot, emphasizing its unique compliance filters to avoid licensing violations. While historically accurate regarding CodeWhisperer's initial launch features, the service has since evolved into Amazon Q Developer, with a broader security and multi-file architecture focus.
  - **(2021)** [AWS Toolkits for Cloud9, JetBrains and VS Code now support interaction with over 200 new resource types 🌟](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-toolkits-cloud9-jetbrains-vs-code) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS announcement highlighting the release of updated AWS Toolkits for popular IDEs (Cloud9, JetBrains, VS Code), expanding interaction capabilities to over 200 resource types. This update greatly reduced context switching for developers, enabling local generation of IAM, DynamoDB, and CloudFormation schemas without visiting the AWS web console.
#### Identity Management

  - **(2022)** [dev.to/franciscogm: AWS CLI SSO made easy](https://dev.to/franciscogm/aws-cli-sso-made-easy-3bh9) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A developer-focused guide showing how to simplify multi-account authorization using the AWS CLI and AWS IAM Identity Center (formerly AWS Single Sign-On). It demonstrates optimal config profile structures to enable rapid terminal-based authentication. Highly valued by security administrators striving to eliminate long-term credentials on local workstations.
#### Open Source Ecosystem

  - **(2026)** [OpenSource at AWS](https://aws.github.io) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main portal showcasing AWS's strategic contributions, governance standards, and active open-source projects. It acts as an architectural guide for platform engineers to align with verified cloud-native upstream projects. Grounding in 2026 verifies its status as a critical reference for production-grade SDK patterns and cloud integrations.
#### Reference Architectures

  - **(2026)** [AWS Labs GitHub](https://github.com/awslabs) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — The central AWS Labs GitHub organization housing hundreds of active experimental projects, tooling integrations, and reference CDK blueprints. Live Grounding highlights this hub as a critical launchpad for emerging patterns in infrastructure-as-code and cloud automation. It provides platform engineering teams with robust, peer-reviewed building blocks for accelerated architecture design.
#### Security And Compliance

  - **(2023)** [ermetic.com: Access Undenied on AWS](https://www.tenable.com/blog/access-undenied-on-aws) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The introductory technical blog post outlining the implementation of Access Undenied on AWS. It explains how parsing multi-layered IAM restrictions (such as Permission Boundaries, Service Control Policies, and Session Policies) helps platform teams resolve frustrating 'implicit deny' errors. Essential reading for operations engineers transitioning to strict zero-trust IAM governance.
#### Security Group Management

  - **(2022)** [dev.to: How to Copy a Security Group with Rules from one AWS Account to Another account](https://dev.to/dineshrathee12/how-to-copy-a-security-group-with-rules-from-one-aws-account-to-another-account-36mb) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical technical tutorial detailing programmatic patterns to replicate AWS Security Groups and nested rules across separate AWS accounts. It resolves multi-tenant configuration sync issues using Python and the AWS CLI. This is critical for engineers performing tenant migrations or standing up identical staging environments under modern IAM paradigms.
#### Storage Management

  - **(2023)** [blog.awsfundamentals.com: Step-By-Step: Emptying S3 Buckets and Directories Using the AWS CLI with S3 RM](https://awsfundamentals.com/blog/aws-s3-rm-removing-files) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive tutorial from AWS Fundamentals on how to empty S3 buckets containing millions of objects using the AWS CLI. It highlights the differences between simple deleting, multi-object API commands, and utilizing Lifecycle rules to clean buckets at zero cost. Essential for DevOps engineers avoiding massive API transactional bills.
## Cloud Platforms

### AWS Education

#### Resources (1)

  - **(2025)** [RESOURCE HUB: Eventos y webinars de AWS](https://aws.amazon.com/events) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — The main catalog of upcoming and archived AWS training webinars, events, and bootcamps, detailing multi-region strategy patterns, cloud migration best practices, and serverless architectures.
### AWS Regional Infrastructure

#### Spain

  - **(2023)** [AWS en España](https://aws.amazon.com/es/local/spain) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The landing portal for AWS's infrastructure operations in Spain, outlining local low-latency clusters, geographical redundancy options, and sovereign data residency frameworks for European enterprise workloads.
  - **(2023)** [AWS Transit Gateway is now available in Europe (Spain) Region](https://aws.amazon.com/about-aws/whats-new/2023/04/aws-transit-gateway-europe-spain-region) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Product update announcement covering the launch of AWS Transit Gateway in the Europe (Spain) Region (eu-south-2). Allows complex hub-and-spoke networking architectures to route traffic at regional speed.
  - **(2022)** [xataka.com: Por qué Amazon ha elegido Aragón para instalar sus tres primeros centros de datos en España](https://www.xataka.com/servicios/que-amazon-ha-elegido-aragon-para-instalar-sus-tres-primeros-centros-datos-espana) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical study published by Xataka highlighting why Amazon chose Aragon to construct its major Spanish data center hubs, focusing on physical security, fiber links, and regional green energy availability.
  - **(2022)** [aboutamazon.es: AWS acelera la apertura de la Región AWS Europa (España) para apoyar la transformación digital de España](https://www.aboutamazon.es/noticias/aws/la-region-aws-europa-espana-apoya-la-transformacion-digital-en-el-pais) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An Amazon corporate press announcement documenting the accelerated opening of the AWS Europe (Spain) Region. Outlines how multi-billion-euro long-term infrastructure investments drive digital transformation.
## Cloud Providers

### AWS (5)

#### Operations (1)

  - **(2008)** [AWS Support](https://aws.amazon.com/premiumsupport) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed directory of AWS premium tier services, offering technical case routing, cloud guidance, and access to Trusted Advisor tools to maintain cluster health and SLA commitments.
#### Security and IAM

  - **(2026)** [**docs.aws.amazon.com: Actions, resources, and condition keys for AWS services 🌟🌟🌟**](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) <span class='md-tag md-tag--warning'>[HTML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The definitive AWS reference for constructing fine-grained IAM policies. It outlines exact service actions, resource types, and condition context keys required to enforce the principle of least privilege in enterprise architectures. This resource is indispensable for security engineers building cloud access models.
#### Status Monitoring

  - **(2006)** [status.aws.amazon.com: Service Health Dashboard](https://health.aws.amazon.com/health/status) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS’s central status console reporting operational health of active regions and services, allowing platform engineers to quickly cross-examine deployment anomalies with provider incidents.
## Cloud-native Provisioning

### CICD (1)

#### AWS Codedeploy

  - **(2022)** [adamtheautomator.com: Getting Started with AWS CodeDeploy](https://adamtheautomator.com/aws-codedeploy) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walkthrough outlining primary configuration steps, appspec.yml lifecycle hook schemas, and target group integrations inside the AWS CodeDeploy ecosystem.
#### AWS Codepipeline

  - **(2026)** [AWS Partner Network - CodePipeline Integrations](https://aws.amazon.com/es/codepipeline/product-integrations) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical integration matrix detailing partner-supported build, testing, and security scanning extensions available for AWS CodePipeline deployment pipelines.
  - **(2022)** [aws.amazon.com: AWS CodePipeline adds support for Branch-based development and Monorepos](https://aws.amazon.com/blogs/devops/aws-codepipeline-adds-support-for-branch-based-development-and-monorepos)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Release analysis highlighting newly added monorepo and branch-specific triggers within AWS CodePipeline, optimizing continuous delivery workflows and reducing build execution times.
#### AWS DevOps

  - **(2026)** [AWS DevOps Blog](https://aws.amazon.com/blogs/devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The authoritative AWS blog containing continuous architectural blueprints, release notes, and real-world implementation case studies for optimizing deployment patterns on Amazon Web Services.
  - **(2026)** [Continuous Deployment with AWS](https://aws.amazon.com/blogs/devops/tag/continuous-deployment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curated collection of continuous deployment strategies optimized for AWS runtimes. Explains canary releases, blue/green cluster migrations, and automated rollbacks on ECS and EKS.
#### CDK Pipelines

  - **(2021)** [aws.amazon.com: Multi-branch pipeline management and infrastructure deployment using AWS CDK Pipelines](https://aws.amazon.com/blogs/devops/multi-branch-pipeline-management-and-infrastructure-deployment-using-aws-cdk-pipelines) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Advanced engineering tutorial detailing how to set up dynamic, multi-branch environments using AWS CDK Pipelines, enabling code-driven promotion of cloud architectures.
#### Comparisons

  - **(2021)** [k21academy.com: AWS DevOps Vs. Azure DevOps](https://k21academy.com/aws-cloud/aws-devops-vs-azure-devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comparative structural analysis pitting the AWS DevOps suite against Microsoft Azure DevOps, evaluating build pricing, third-party integrations, and native Kubernetes support configurations.
#### Jenkins Integration

  - **(2021)** [Setting Up the Jenkins Plugin for AWS CodeDeploy](https://aws.amazon.com/blogs/devops/setting-up-the-jenkins-plugin-for-aws-codedeploy) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Step-by-step setup guide for configuring the AWS CodeDeploy Jenkins plugin, allowing legacy, on-prem Jenkins orchestrations to deploy code artifacts directly to AWS cloud groups.
### Observability

#### AWS DevOps Guru

  - **(2021)** [infoq.com: AWS Launches Amazon DevOps Guru](https://www.infoq.com/news/2021/01/aws-devops-guru)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical product announcement introducing Amazon DevOps Guru, an ML-driven operations assistant that parses CloudWatch metrics and traces to proactively alert operators to system anomalies.
## Data Architecture

### Databases (1)

#### Amazon Aurora

  - **(2015)** [InfoWorld Review – Amazon Aurora Rocks MySQL](https://aws.amazon.com/blogs/aws/infoworld-review-amazon-aurora-rocks-mysql) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical analysis validating Amazon Aurora's decoupled compute and storage architecture. In production contexts, it remains a de facto standard for high-throughput, low-latency relational engines.
## Data Engineering

### Data Warehousing

#### ELT Pipeline

  - **(2020)** [**revenuecat.com: Replicating a postgresql cluster to redshift**](https://www.revenuecat.com/blog/engineering/replicating-a-postgresql-cluster-to-redshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight presents RevenueCat's engineering experience replicating high-throughput transactional Postgres databases into AWS Redshift. Live Grounding evaluates the trade-offs of AWS DMS, custom streaming code, and data synchronization patterns. Offers real-world insights on scale, column-mapping issues, and operational bottlenecks.
### Streaming Data

#### Architectural Concepts

  - **(2026)** [What is Streaming Data?](https://aws.amazon.com/what-is/streaming-data)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS conceptual guide delineating the architecture of real-time streaming data pipelines. Compares high-throughput, sequential processing mechanisms against traditional batch structures, referencing Amazon Kinesis and Apache Kafka as key streaming backplanes.
## DevOps

### Continuous Delivery

#### Release Strategies

  - **(2020)** [cloudacademy.com: Blog / DevOpsDevOps: Why Is It Important to Decouple Deployment From Release?](https://platform.qa.com/login) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural analysis of separating physical code deployment from logical user release. Examines the use of feature flag systems and proxy-level traffic management to perform risk-free production promotions.
## Edge and Iot

### AWS (6)

#### Iot Platforms

  - **(2015)** [aws.amazon.com/en/iot](https://aws.amazon.com/iot) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical documentation for AWS IoT Core, a high-throughput managed broker designed to securely route and map billions of device telemetry streams into cloud databases and analysis applications.
## Enterprise Architecture

### Cloud Architecture Best Practices

#### AWS Well-architected

  - **(2023)** [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official documentation framework outlining six fundamental cloud architectural pillars: operational excellence, security, reliability, performance, cost optimization, and sustainability.
  - **(2023)** [aws.amazon.com/well-architected-tool: AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Overview of AWS's native tool designed to assess cloud workloads. Integrates with the Well-Architected Framework to systematically audit infrastructure and highlight configuration risks.
  - **(2023)** [infoq.com: AWS Updates the Well-Architected Framework](https://www.infoq.com/news/2023/04/aws-well-architected-framework)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes key revisions to the AWS Well-Architected Framework. Reviews shifts in security baseline configurations, serverless deployment guidelines, and the sustainability assessment pillar.
#### Cloud Governance

  - **(2023)** [Strategies for consolidating AWS environments](https://aws.amazon.com/de/blogs/mt/strategies-for-consolidating-aws-environments) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details architectural strategies for consolidating multi-account AWS environments. Explores AWS Organizations setups, control tower governance, and billing unification across enterprise structures.
  - **(2023)** [Maintain visibility over the use of cloud architecture patterns](https://aws.amazon.com/blogs/architecture/maintain-visibility-over-the-use-of-cloud-architecture-patterns)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines frameworks and tools to track, map, and enforce specific cloud architecture patterns across decentralized developer teams, helping prevent systemic configuration drift.
#### Design Blueprints

  - **(2023)** [AWS application-architecture](https://www.conceptdraw.com/examples/application-architecture) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architecture drafting resource providing standard AWS application design templates, components, and layout blocks. Essential for mapping out multi-tier cloud services.
  - **(2023)** [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official blog portal showcasing cloud solutions, pattern guides, and engineering strategies written directly by AWS Systems Architects.
#### Engineering Culture

  - **(2023)** [dev.to: How Well-Architected Enables Junior Engineers](https://dev.to/aws-builders/how-well-architected-enables-junior-engineers-24j)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines how the AWS Well-Architected Framework acts as an educational and operational safety net for junior engineers, establishing structured system design patterns across developer teams.
#### Multi-region Architecture

  - **(2023)** [Creating a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of a multi-region deployment guide. Covers DNS failover routing with Route 53, cross-region VPC peering, compute distribution, and unified security controls across AWS regions.
  - **(2023)** [Creating a Multi-Region Application with AWS Services – Part 2, Data and Replication](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-2-data-and-replication) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part two focuses on database replication, global data consistency, storage syncing protocols, and handling split-brain scenarios in multi-region cloud infrastructures.
#### Production Case Studies

  - **(2023)** [This is My Architecture](https://aws.amazon.com/architecture/this-is-my-architecture)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS's premier video and article series showcasing production-grade architectural solutions. Focuses on design tradeoffs, performance strategies, and networking topologies of modern web applications.
## Finops and Cloud Cost

### AWS Optimization

#### Policy Engines

  - **(2024)** [**Cloudburn: An Open-Source Policy Engine for AWS Spending**](https://github.com/towardsthecloud/cloudburn) <span class='md-tag md-tag--info'>⭐ 1765</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-fe15c8c2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 10 L 20 12 L 30 4 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-fe15c8c2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Introduces Cloudburn, an open-source command-line tool designed to audit AWS resource groups. By using declarative policies, it alerts teams to idle resources, non-standard instance types, and unassigned Elastic IPs to keep real-world deployments within budget limits.
## Infrastructure (1)

### DevOps (1)

#### Command Line Utilities

  - **(2016)** [ec2-ssh-yplan: A pair of command line utilities for finding and SSH-ing into your Amazon EC2 instances by tag (such as ‘Name’)](https://pypi.org/project/ec2-ssh-yplan) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents a set of CLI wrappers for resolving AWS EC2 instance metadata to facilitate fast SSH access. Live Grounding indicates that modern secure architectures prioritize AWS Systems Manager Session Manager (SSM) and private endpoint setups over direct, port-22 SSH routing models.
## Infrastructure As Code (2)

### AWS CDK

#### Core Platform

  - **(2026)** [CDK](https://aws.amazon.com/cdk) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the AWS Cloud Development Kit (CDK) for defining cloud infrastructure using familiar programming languages. Live Grounding confirms AWS CDK v2 is the undisputed standard for modern AWS programmatic provisioning, drastically reducing CloudFormation boilerplate via high-level, reusable constructs.
#### Migration Tools

  - **(2023)** [Announcing CDK Migrate: A single command to migrate to the AWS CDK](https://aws.amazon.com/blogs/devops/announcing-cdk-migrate-a-single-command-to-migrate-to-the-aws-cdk) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Curator Insight details the native CDK CLI capability to ingest deployed CloudFormation stacks or raw resources and output fully functional CDK code. Live Grounding demonstrates its extreme usefulness in technical debt remediation, shifting old legacy infrastructure into managed, programmatically modeled code bases.
#### Serverless Applications

  - **(2023)** [freecodecamp.org: AWS CDK v2 Tutorial – How to Create a Three-Tier Serverless Application](https://www.freecodecamp.org/news/aws-cdk-v2-three-tier-serverless-application) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight is a comprehensive, hands-on tutorial for constructing API Gateway, Lambda, and DynamoDB stacks via CDK v2. Live Grounding proves this three-tier serverless pattern remains the gold standard blueprint for robust, scalable web services in AWS.
### Alternative IaC

#### SST

  - **(2024)** [sst.dev: Moving away from CDK: CDK doesn’t create the infrastructure you define](https://sst.dev/blog/moving-away-from-cdk) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight captures the SST team's pivotal decision to transition from AWS CDK to Pulumi/Terraform engines (SST Ion) due to performance bottlenecks and CloudFormation limits. Live Grounding in 2026 highlights this article as a milestone in the serverless community, validating the growing adoption of highly optimized, engine-agnostic IaC tools.
### Boilerplates

#### AWS Templates

  - **(2024)** [AWS Samples (Boilerplates)](https://nubenetes.com/demos/#aws-samples-boilerplates) <span class='md-tag md-tag--warning'>[MULTI-LANGUAGE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A consolidated hub of official and community AWS deployment samples. Houses structured patterns and CloudFormation/Terraform codebases to fast-track prototype development in compliance with AWS architecture standards.
### CICD (2)

#### Self-hosted Runners

  - **(2025)** [RunsOn: Self-hosted GitHub Actions Runners in AWS](https://runs-on.com) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An innovative open-source self-hosting solution that provisions fast, secure, on-demand EC2 single-use runners for GitHub Actions on AWS. Offers extreme cost reductions (up to 10x) utilizing EC2 spot instances with minimal boot delays.
## Kubernetes and Platform Engineering

### Modernization Tools

#### Microservice Migration

  - **(2023)** [AWS App2Container: Migrate your Applications to Containers at Scale](https://aws.amazon.com/blogs/architecture/migrate-your-applications-to-containers-at-scale) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Introduces AWS App2Container, a tool that automates the migration of legacy .NET and Java web applications into containerized structures ready for deployment on Amazon ECS or EKS.
  - **(2023)** [Let’s Architect! Architecting microservices with containers](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-microservices-with-containers)  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A foundational guide for decoupling large legacy applications. Explores container hosting options on ECS and EKS, microservice discovery patterns, and inter-service security standards.
## Multi-cluster and Edge

### Cluster Federation

#### Admiralty

  - **(2026)** [admiralty.io](https://admiralty.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official platform of Admiralty, an advanced multi-cluster proxy scheduler designed to programmatically dispatch workloads across physical, virtual, or serverless Kubernetes namespaces.
#### Serverless Integration

  - **(2021)** [thenewstack.io: Making Kubernetes Serverless and Global with AWS Fargate on EKS and Admiralty](https://thenewstack.io/making-kubernetes-serverless-and-global-with-aws-fargate-on-eks-and-admiralty) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigative analysis showcasing how Admiralty can coordinate with AWS Fargate serverless containers in an EKS environment to deploy globally distributed applications with low operational overhead.
  - **(2021)** [admiralty.io: Multi-Region AWS Fargate on EKS](https://admiralty.io/docs/tutorials/fargate) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Granular implementation tutorial for deploying Admiralty proxy schedulers to configure cross-cluster communication channels that target serverless AWS Fargate environments in multi-region setups.
## Networking and Security

### Identity and Access (1)

#### Secrets Management

  - **(2022)** [dev.to: Automatic API Key rotation for Amazon Managed Grafana](https://dev.to/aws-heroes/automatic-api-key-rotation-for-amazon-managed-grafana-2h68) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight details the step-by-step automation of rotating Grafana API keys using AWS Lambda and Secrets Manager. Live Grounding validates this as a vital security standard, preventing persistent credential leaks and enforcing compliance policies across enterprise monitoring setups.
### Remote Access

#### AWS Systems Manager (2)

  - **(2022)** [aws.amazon.com: AWS Systems Manager announces support for port forwarding to remote hosts using Session Manager](https://aws.amazon.com/about-aws/whats-new/2022/05/aws-systems-manager-support-port-forwarding-remote-hosts-using-session-manager) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight announces native SSM port-forwarding tunnels directly to database endpoints or remote hosts inside private subnets. Live Grounding confirms this is a standard operational practice in 2026, eliminating the security risks, costs, and management overhead of maintaining traditional jump box/bastion host VMs.
### Service Mesh (1)

#### Multi-account

  - **(2021)** [amazon.com: Leveraging App Mesh with Amazon EKS in a Multi-Account environment](https://aws.amazon.com/blogs/containers/leveraging-app-mesh-with-amazon-eks-in-a-multi-account-environment) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents patterns for orchestrating cross-account microservice communication using AWS App Mesh and Amazon EKS. Live Grounding highlights that while the multi-account networking concepts remain structurally valid, the reliance on App Mesh is obsolete; modern architectures deploy VPC Lattice or cross-cluster Istio meshes.
## Observability and Monitoring

### Case Studies (2)

#### Enterprise Scale (1)

  - **(2021)** [How BT uses Amazon CloudWatch to monitor millions of devices](https://aws.amazon.com/blogs/mt/how-bt-uses-amazon-cloudwatch-to-monitor-millions-of-devices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dives into an enterprise architecture deployed by BT utilizing Amazon CloudWatch to ingest, structure, and analyze telemetry streams originating from millions of physical client network units globally.
### Cloudwatch

#### Alerting Systems

  - **(2021)** [Extending and exploring alarm history in Amazon CloudWatch – part 2](https://aws.amazon.com/blogs/mt/extending-and-exploring-alarm-history-in-amazon-cloudwatch-part-2) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates strategies to maintain and analyze deep historical records of CloudWatch alarm states over multi-year thresholds using Kinesis Firehose, S3 object storage targets, and Athena SQL queries.
#### Dashboards

  - **(2020)** [Amazon CloudWatch Dashboards now supports sharing](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-dashboards-supports-sharing) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announces external sharing support for AWS CloudWatch Dashboards, permitting secure read-only console visualizations to key stakeholders outside the immediate AWS organization footprint.
#### Guides Collection

  - **(2021)** [threatstack.com: 50 Best AWS CloudWatch Tutorials](https://www.f5.com/company/blog) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive directory linking to performance tuning guides, log group configurations, and real-time dashboard design patterns inside Amazon CloudWatch. Evaluates fundamental metric generation techniques.
#### Prometheus Integration

  - **(2020)** [Amazon CloudWatch now monitors Prometheus metrics from Container environments](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-monitors-prometheus-metrics-container-environments) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents Amazon CloudWatch Container Insights' ability to ingest, index, and visualize standard Prometheus application metrics directly from Elastic Kubernetes Service (EKS) cluster deployments.
### Enterprise Observability

#### Elastic Stack

  - **(2022)** [elastic.co: Elastic and AWS: Accelerating the cloud migration journey](https://www.elastic.co/blog/elastic-and-aws-accelerate-your-cloud-migration-journey) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores integrations between Elastic Cloud and AWS native logging solutions. Facilitates high-velocity log ingest, distributed tracing across container environments, and simplified security event monitoring across cloud instances.
### Managed Services

#### Announcements

  - **(2021)** [infoq.com: AWS Introduces Amazon Managed Service for Grafana and Amazon Managed Service for Prometheus](https://www.infoq.com/news/2021/01/aws-grafana-prometheus) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural breakdown of AWS's entry into cloud-native managed open-source telemetry tools. Reviews integration advantages, storage strategies, and price efficiencies compared to self-hosted instances on EC2.
#### Grafana

  - **(2024)** [Amazon Managed Service for Grafana](https://aws.amazon.com/grafana) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Managed visualization console offering direct enterprise integrations with SSO and IAM setups. Allows telemetry aggregation from diverse cloud datasources (S3, Prometheus, CloudWatch, Opensearch) under unified dynamic views.
## Operations (2)

### Local Environment Setup

#### Package Management

  - **(2023)** [DevOps Made Easy: Install AWS CLI, ECS CLI, Docker & Terraform Using Chocolatey](https://dev.to/aws-builders/devops-made-easy-install-aws-cli-ecs-cli-docker-terraform-using-chocolatey-2lld)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A step-by-step local workstation bootstrapping guide using the Windows Chocolatey package manager. Instructs how to quickly establish consistent local administration tooling, installing docker-cli, terraform, aws-cli, and ecs-cli to prepare for cloud resource management.
## Organizational Culture

### Migration Journeys

#### Trainline

  - **(2016)** [London DevOps - Trainline, A DevOps Journey - Chris Turvil](https://www.youtube.com/watch?v=IUvUmqu1MBQ) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight tracks the cultural and technical journey of Trainline’s DevOps transition during their full AWS migration. Live Grounding points to this talk as a textbook cultural reference, showing that microservices and infrastructure modernization fail without a parallel shift in organizational communication and delivery practices.
## Security and Governance

### Cloud Governance (1)

#### Compliance and Audit

  - **(2022)** [How to use AWS Config and CloudTrail to find who made changes to a resource](https://aws.amazon.com/blogs/mt/how-to-use-aws-config-and-cloudtrail-to-find-who-made-changes-to-a-resource) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to correlate events from AWS Config history with CloudTrail api audit logs. Provides an audit mechanism to pinpoint precise user identities, timestamps, and parameters related to unauthorized resource alterations.
## Serverless (1)

### Voice User Interfaces

#### Alexa Skills

  - **(2017)** [New Alexa Skills Kit Template: Build a Trivia Skill in under an Hour](https://developer.amazon.com) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Step-by-step developer tutorial detailing integration patterns between the Alexa Skills Kit and AWS Lambda serverless functions. Marked legacy as current conversational AI models have largely replaced basic programmatic trivia setups in production.
## Service Discovery

### AWS Cloud Map

#### Health Checks

  - **(2022)** [Custom Health Check: HealthCheckCustomConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official reference guide for Cloud Map API's custom health checks. Explains dynamic service discovery patterns for serverless workloads where traditional load balancer health checks are inapplicable.
## Testing and Chaos

### Chaos Engineering

#### AWS FIS

  - **(2020)** [techcrunch.com: AWS introduces new Chaos Engineering as a Service offering](https://techcrunch.com/2020/12/15/aws-introduces-new-chaos-engineering-as-a-service-offering) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight documents the launch of AWS Fault Injection Simulator (FIS) to facilitate managed chaos engineering. Live Grounding demonstrates that FIS has transitioned from a new offering to a deeply integrated resilience tool in 2026, standardizing controlled failure injection across EC2, EKS, and RDS clusters.
### Debugging

#### AWS Troubleshooting

  - **(2021)** [thenewstack.io: Remote Debugging in AWS: The Missing Link in Your Debugging Toolset](https://thenewstack.io/remote-debugging-in-aws-the-missing-link-in-your-debugging-toolset) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight exposes methodologies for live-debugging cloud-hosted microservices without causing disruption. Live Grounding tracks the evolution of these techniques into sophisticated cloud-native debugging proxies and observability integrations (like OpenTelemetry and Telepresence), bridging local IDEs with remote VPC resources.
### Local Emulation

#### AWS Emulation

  - **(2026)** [localstack.cloud](https://www.localstack.cloud) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the enterprise cloud platform offering advanced local emulation of AWS services. Live Grounding reinforces that LocalStack has become the industry standard for offline AWS cloud development, supporting complex services like IAM, EKS, and RDS, which radically reduces cloud spend and speeds up inner-loop iteration cycles.

---
💡 **Explore Related:** [AWS Storage](./aws-storage.md) | [Digitalocean](./digitalocean.md) | [AWS Backup](./aws-backup.md)

🔗 **See Also:** [AWS Pricing](./aws-pricing.md) | [Ansible](./ansible.md)

