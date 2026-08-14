---
description: "Curated, AI-ranked AWS Newfeatures resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Cloud Providers (Hyperscalers))."
---
# AWS New Features

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws-newfeatures/).

!!! info "Architectural Context"
    Detailed reference for AWS New Features in the context of Cloud Providers (Hyperscalers).

## Application Integration

### Serverless Orchestration

#### Step Functions

  - **(2021)** [==infoq.com: AWS Introduces a New Workflow Studio for AWS Step Functions==](https://www.infoq.com/news/2021/06/step-functions-workflow-studio) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A visual, low-code workflow designer that simplifies building distributed state machines on AWS. It allows developers to drag, drop, and configure states, mapping state transitions and payloads directly to downstream AWS services. This visual paradigm significantly accelerates development cycles for complex microservices orchestrations while generating ASL (Amazon States Language) behind the scenes.
  - **(2021)** [==Now — AWS Step Functions Supports 200 AWS Services To Enable Easier Workflow Automation==](https://aws.amazon.com/blogs/aws/now-aws-step-functions-supports-200-aws-services-to-enable-easier-workflow-automation) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Dramatically expands the capabilities of AWS Step Functions by offering direct SDK integration with over 200 AWS services and over 9,000 API actions. This architecture minimizes or completely eliminates custom 'glue' Lambda functions whose sole purpose was calling AWS APIs. It simplifies state machine engineering, reducing latency, maintenance costs, and execution failure risks.
  - **(2021)** [**xataka.com: Hasta AWS se pasa al low-code: Workflow Studio es su primera herramienta de desarrollo de bajo código**](https://www.xataka.com/pro/aws-se-pasa-al-low-code-workflow-studio-su-primera-herramienta-desarrollo-codigo) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Un análisis en español sobre Workflow Studio para AWS Step Functions, detallando cómo la interfaz visual democratiza el diseño de arquitecturas serverless de bajo código (low-code). Permite a desarrolladores y analistas diagramar flujos lógicos, interactuando con otros servicios de AWS de manera intuitiva y reduciendo la complejidad del código.
## Cloud Governance

### Landing Zones

#### Control Tower

  - **(2021)** [**AWS Control Tower now supports nested organizational units**](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-control-tower-supports-nested-organizational-units) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Enables AWS Control Tower to govern up to five levels of nested Organizational Units (OUs), providing fine-grained SCP (Service Control Policy) inheritance inside complex AWS Organizations structures. This allows large enterprises to map organizational hierarchies exactly to their AWS landing zones. It improves permission inheritance modeling and cloud security boundaries without forcing flat structural patterns.
  - **(2021)** [**Migrate AWS Landing Zone solution to AWS Control Tower**](https://aws.amazon.com/blogs/mt/migrate-aws-landing-zone-solution-to-aws-control-tower) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — A technical walkthrough explaining the migration path from legacy, custom-built AWS Landing Zone (ALZ) frameworks to fully managed Control Tower landing zones. It details account enrollment, baseline consolidation, and continuous policy management translations. This migration ensures long-term supportability, lower engineering maintenance, and structured governance.
### Resource Tagging

#### Automation

  - **(2021)** [New AWS Solutions Implementation: Tag Tamer](https://aws.amazon.com/about-aws/whats-new/2021/06/new-aws-solutions-implementation-tag-tamer) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source, reference-architecture tool designed to manage, govern, and remediate tagging compliance across AWS accounts. Featuring a user-friendly UI, it assists organizations in standardizing metadata for cost allocation, access control, and automation. In production, this mitigates drift in tagging schemas, bringing consistency to multi-account landings.
### Service Catalog

#### Operations Automation

  - **(2021)** [**Automate preapproved operations with AWS Service Catalog service actions**](https://aws.amazon.com/blogs/mt/automate-preapproved-operations-with-aws-service-catalog-service-actions) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Enables cloud administrators to associate AWS Systems Manager (SSM) documents with cataloged products, allowing end-users to perform pre-approved operational tasks (like rebooting or scaling). This decouples routine operations from root-access privileges, enforcing zero-trust boundaries. It drastically reduces IT ticketing overhead through self-service infrastructure operations.
## Cloud Infrastructure

### AWS

#### Business Applications

  - **(2016)** [**Amazon WorkMail – Now Generally Available**](https://aws.amazon.com/blogs/aws/amazon-workmail-now-generally-available) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — General availability announcement of Amazon WorkMail. Introduces an enterprise-grade cloud email and calendar service featuring strict security keys and existing corporate directory sync capabilities.
#### Compute

  - **(2015)** [**Coming Soon – EC2 Dedicated Hosts**](https://aws.amazon.com/blogs/aws/coming-soon-ec2-dedicated-hosts) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Details Amazon EC2 Dedicated Hosts, designed to address strict enterprise compliance, hardware isolation requirements, and fine-grained socket-level BYOL software licensing limits.
  - **(2016)** [New – Scheduled Reserved Instances](https://aws.amazon.com/blogs/aws/new-scheduled-reserved-instances) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details Scheduled Reserved Instances, designed to book recurring computational capacity (mostly superseded by dynamic Savings Plans and modern On-Demand capacity reservations).
#### Container Orchestration

  - **(2015)** [**EC2 Container Service Update – Container Registry, ECS CLI, AZ-Aware Scheduling, and More**](https://aws.amazon.com/blogs/aws/ec2-container-service-update-container-registry-ecs-cli-az-aware-scheduling-and-more) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Milestone feature updates outlining the inception of Amazon Elastic Container Registry (ECR), native ECS CLI utilities, and multi-AZ application container scheduler integrations.
#### Governance

  - **(2015)** [**AWS Config Rules – Dynamic Compliance Checking for Cloud Resources**](https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Introduction to AWS Config Rules for dynamic resource auditing. Outlines custom Lambda-backed compliance checks, automated change detection, and state verification rules across multi-account structures.
#### Internet Of Things

  - **(2015)** [**AWS IoT – Cloud Services for Connected Devices**](https://aws.amazon.com/blogs/aws/aws-iot-cloud-services-for-connected-devices) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Core introduction of AWS IoT architecture. Details high-throughput MQTT broker brokers, secure device shadow states, rules engines, and telemetry stream mapping to AWS analytics components.
#### Management Tools

  - **(2020)** [==AWS CloudShell - Command-Line Access to AWS Resources==](https://aws.amazon.com/es/blogs/aws/aws-cloudshell-command-line-access-to-aws-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduction to AWS CloudShell, a browser-based, secure terminal console preconfigured with standard CLI utilities, shell environments, and automatic IAM session credential sharing.
#### Mobile Development

  - **(2015)** [AWS Mobile Hub – Build, Test, and Monitor Mobile Applications](https://aws.amazon.com/blogs/aws/aws-mobile-hub-build-test-and-monitor-mobile-applications) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historic product announcement for AWS Mobile Hub, the predecessor tool used for configuring client-side storage, compute, and cognito authentication (superseded entirely by AWS Amplify).
#### Mobile Testing

  - **(2025)** [**AWS Device Farm: Improve the quality of your web and mobile applications by testing across desktop browsers and real mobile devices hosted in the AWS Cloud**](https://aws.amazon.com/device-farm) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Product brief of AWS Device Farm, an automated application testing service hosting real physical mobile devices and desktop browser stacks for continuous cross-platform validation.
#### Monitoring

  - **(2015)** [==CloudWatch Dashboards – Create & Use Customized Metrics Views==](https://aws.amazon.com/blogs/aws/cloudwatch-dashboards-create-use-customized-metrics-views) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Reference guide detailing custom Amazon CloudWatch Dashboards. Covers metric ingestion, multi-widget graphing configurations, and consolidated cross-region resource alerting models.
  - **(2018)** [**cloudonaut.io: Seamless EC2 monitoring with the Unified CloudWatch Agent**](https://cloudonaut.io/seamless-ec2-monitoring-with-the-unified-cloudwatch-agent) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Architectural guide explaining the transition to the Unified CloudWatch Agent on EC2. Details system-level RAM, disk, and custom application metrics collection policies.
#### Regions

  - **(2015)** [London Calling! An AWS Region is coming to the UK!](https://www.allthingsdistributed.com/2015/11/aws-announces-uk-region.html) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical briefing of AWS network expansion planning for the UK region launch, highlighting sovereignty compliance targets and low-latency availability zone options.
#### Security

  - **(2021)** [**amazon.com: Reduce Unwanted Traffic on Your Website with New AWS WAF Bot Control**](https://aws.amazon.com/blogs/aws/reduce-unwanted-traffic-on-your-web-site-with-aws-bot-control) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Explains AWS WAF Bot Control integration. Discusses using preconfigured rule groups at edge distribution tiers to detect, classify, and isolate automated malicious scraper patterns.
  - **(2020)** [**github.com/hayao-k/cdk-ecr-image-scan-notify**](https://github.com/hayao-k/cdk-ecr-image-scan-notify) <span class='md-tag md-tag--info'>⭐ 29</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d6c5393e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 8 L 20 2 L 30 4 L 40 7 L 50 5" fill="none" stroke="url(#spark-grad-d6c5393e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Community CDK construct that maps AWS EventBridge patterns to detect ECR image vulnerability scans. Automatically processes and delivers structured notifications to Slack/Teams channels using Lambda.
  - **(2015)** [**Amazon Inspector – Automated Security Assessment Service**](https://aws.amazon.com/blogs/aws/amazon-inspector-automated-security-assessment-service) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Architectural overview of Amazon Inspector, an automated vulnerability management service. Details continuous software vulnerability assessments on EC2 instances, ECR container layers, and serverless runtimes.
#### Serverless

  - **(2015)** [==AWS Lambda Update – Python, VPC, Increased Function Duration, Scheduling, and More==](https://aws.amazon.com/blogs/aws/aws-lambda-update-python-vpc-increased-function-duration-scheduling-and-more) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Strategic release notes highlighting early serverless evolutions: introducing Python runtime environments, VPC integration paths, dynamic event scheduling, and longer execution timeout periods.
#### Storage

  - **(2015)** [==Amazon EFS: Amazon Elastic File System – Shared File Storage for Amazon EC2==](https://aws.amazon.com/blogs/aws/amazon-elastic-file-system-shared-file-storage-for-amazon-ec2) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Deep dive into Amazon EFS, offering serverless elastic file sharing based on NFSv4. Integrates natively across EC2 instances, on-premises centers, and container tasks under ECS or EKS.
  - **(2015)** [==New – Encrypted EBS Boot Volumes==](https://aws.amazon.com/blogs/aws/new-encrypted-ebs-boot-volumes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Announcement of native EBS boot volume encryption, leveraging AWS Key Management Service (KMS) without degrading overall instance throughput or input/output latency patterns.
### Compute (1)

#### Auto Scaling

  - **(2021)** [**Amazon EC2 Auto Scaling now lets you control which instances to terminate on scale-in**](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-ec2-auto-scaling-now-lets-you-control-which-instances-to-terminate-on-scale-in) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Offers precise programmatic control over which EC2 instances are terminated first during an Auto Scaling scale-in event. This replaces generic policies, allowing engineers to retain warm instances, protect long-running tasks, or optimize container host terminations. Architecturally, it increases stability for stateful or queue-consuming workers.
#### EC2 Troubleshooting

  - **(2021)** [**infoq.com: AWS Introduces EC2 Serial Console: Troubleshoot Boot and Networking Issues**](https://www.infoq.com/news/2021/04/aws-ec2-serial-console) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Provides secure, interactive access to the physical serial port of EC2 instances, bypassing traditional IP-based network configuration. This enables real-time diagnostic debugging of boot issues, kernel panics, and misconfigured firewall or network interfaces. Architecturally, it serves as a critical break-glass tool for enterprise sysadmins to avoid data loss during OS-level misconfigurations.
#### Multi-region Operations

  - **(2021)** [Amazon EC2 now offers Global View on the console to view all resources across regions together](https://aws.amazon.com/about-aws/whats-new/2021/09/amazon-ec2-global-view-console-regions) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Offers a centralized dashboard on the EC2 Console to view all running instances, volumes, VPCs, and subnets across all AWS Regions simultaneously. This feature drastically improves operational visibility, allowing engineers to track shadow IT, verify multi-region deployments, and quickly locate orphaned resources. It provides a foundational unified pane for multi-region operations.
#### Operating Systems

  - **(2021)** [**linux.slashdot.org: AWS Embraces Fedora Linux for Its Cloud-Based 'Amazon Linux'**](https://linux.slashdot.org/story/21/11/27/0328223/aws-embraces-fedora-linux-for-its-cloud-based-amazon-linux) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Announces Amazon Linux 2022 (later AL2023), transitioning the base operating system platform to Fedora. This shift promises a predictable two-year release cycle, faster access to up-to-date upstream packages, and refined SELinux security defaults. It provides an optimized, modern runtime layer for containerized microservices and virtualized EC2 execution.
#### Spot Instances

  - **(2022)** [Amazon EC2 announces new price and capacity optimized allocation strategy for provisioning Amazon EC2 Spot Instances](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-ec2-price-capacity-optimized-allocation-strategy-provisioning-ec2-spot-instances) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon EC2 introduced the 'price-capacity-optimized' allocation strategy for Spot Instances. It balances cost-efficiency with instance availability by assessing real-time capacity pools, resulting in drastically lower interruption rates for large scale container and big data workloads.
### Console

#### UIUX

  - **(2022)** [Announcing dark mode support in the AWS Management Console](https://aws.amazon.com/about-aws/whats-new/2022/10/dark-mode-support-aws-management-console) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The AWS Management Console released native dark mode support, improving accessibility and visual comfort for operators working across extended monitoring shifts. It introduces a configurable theme preference that persists across sessions.
### Container Orchestration (1)

#### ECS Deployments

  - **(2022)** [Amazon ECS now integrates with Amazon CloudWatch alarms to improve safety for deployments](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-ecs-cloudwatch-alarms-safety-deployments) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon ECS integrated natively with CloudWatch alarms to implement automated deployment rollbacks. If custom indicators (like HTTP 5xx errors) cross alarm thresholds during a rolling update, ECS automatically rolls back the task definitions to the last known stable state.
#### EKS Windows

  - **(2022)** [Amazon EKS launches automated provisioning and lifecycle management for Windows containers](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-eks-automated-provisioning-lifecycle-management-windows-containers) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon EKS automated the deployment and lifecycle management of Windows container nodes. It simplifies AMI updates, security patching, and scaling operations for Windows-based workloads on Kubernetes, aligning them with traditional Linux container management patterns.
#### Storage Integration

  - **(2024)** [Amazon ECS and AWS Fargate now integrate with Amazon EBS](https://aws.amazon.com/about-aws/whats-new/2024/01/amazon-ecs-fargate-integrate-ebs) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon ECS and AWS Fargate introduced native integration with Amazon EBS volumes. This lets serverless container deployments mount high-performance block storage dynamically, accommodating data-intensive file-processing workloads.
### Databases

#### Backup and Recovery

  - **(2022)** [Amazon Timestream now enables you to protect your data through AWS Backup](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-timestream-enables-protect-data-through-aws-backup) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon Timestream integrated with AWS Backup to provide centralized, automated protection for time-series databases. It supports scheduling continuous or periodic backups, meeting compliance targets, and executing point-in-time recoveries easily.
#### Data Migration

  - **(2023)** [New – AWS DMS Serverless: Automatically Provisions and Scales Capacity for Migration and Data Replication](https://aws.amazon.com/blogs/aws/new-aws-dms-serverless-automatically-provisions-and-scales-capacity-for-migration-and-data-replication) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS DMS Serverless automates the provisioning, scaling, and operational management of resources needed for database replication and migration tasks. This reduces hands-on provisioning steps during large-scale enterprise data migrations.
#### RDS Deployments

  - **(2022)** [Announcing Amazon RDS Blue/Green Deployments for safer, simpler, and faster updates](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-rds-blue-green-deployments-safer-simpler-faster-updates) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon RDS Blue/Green Deployments introduced fully managed environment duplication, enabling automated synchronization and safe promotion of databases. This feature significantly limits downtime and rollback complexities during critical minor and major engine updates.
#### Secrets Management

  - **(2022)** [Amazon RDS announces integration with AWS Secrets Manager](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-rds-integration-aws-secrets-manager) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon RDS added native integration with AWS Secrets Manager, allowing the service to automatically generate, rotate, and manage database credential secrets. This eliminates hardcoded application secrets, reducing vulnerability surface areas.
### Edge Compute

#### Local Zones

  - **(2021)** [techcrunch.com: AWS to launch over 30 new Local Zones internationally starting in 2022](https://techcrunch.com/2021/12/02/aws-to-launch-over-30-new-local-zones-starting-in-2022) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines AWS's international expansion of Local Zones to provide low-latency edge computing, storage, and database services in metropolitan areas globally. This addresses strict residency laws and provides sub-10ms performance targets for localized financial systems or real-time gaming backends. Architecturally, it extends public cloud boundaries directly to metropolitan data centers.
### Finops

#### Cost Management

  - **(2022)** [AWS Cost Explorer’s New Look and Common Use Cases](https://aws.amazon.com/ru/blogs/aws-cloud-financial-management/aws-cost-explorers-new-ui-and-common-use-cases) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Cost Explorer received a modernized interface and optimized query layouts to aid FinOps analysis. The upgrade simplifies tracking execution costs, identifying anomalies, and reviewing historical cloud expenditure across complex organizational units.
### Global Infrastructure

#### Regions (1)

  - **(2022)** [Now Open–AWS Region in Spain](https://aws.amazon.com/blogs/aws/now-open-aws-region-in-spain) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS announced the general availability of the Europe (Spain) Region (eu-south-2). This physical infrastructure footprint enables customers to achieve lower latency for local workloads, meet residency and data sovereignty requirements inside the European Union, and build multi-region failover setups.
### Governance (1)

#### AWS Organizations

  - **(2022)** [Announcing delegated administrator for AWS Organizations](https://aws.amazon.com/about-aws/whats-new/2022/11/aws-organizations-delegated-administrator) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS introduced delegated administrator capabilities for AWS Organizations, permitting the management of member policies and organizational hierarchies from a secondary security or utility account. This reduces operational overhead on the organization's root administrative account, minimizing risk exposure.
#### Compliance

  - **(2022)** [Integration of AWS Well-Architected Tool with AWS Organizations](https://aws.amazon.com/about-aws/whats-new/2022/06/aws-well-architected-tool-organizations-integration) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Integration of the AWS Well-Architected Tool with AWS Organizations provides centralized visibility into workload reviews across all member accounts. This structural update enables corporate architects to monitor governance posture, identify common architectural flaws, and establish standardized multi-tenant review patterns across the enterprise landscape.
#### Resource Tracking

  - **(2023)** [AWS Config supports recording exclusions by resource type](https://aws.amazon.com/about-aws/whats-new/2023/06/aws-config-recording-exclusions-resource-type) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Config introduced resource-type exclusions, allowing organizations to exclude high-churn resources from continuous state recording. This helps control tracking costs and reduces noisy alerts on unimportant assets.
#### Systems Management

  - **(2023)** [Announcing the ability to enable AWS Systems Manager by default across all EC2 instances in an account](https://aws.amazon.com/about-aws/whats-new/2023/02/enable-aws-systems-manager-default-all-ec2-instances-account) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Systems Manager launched 'Default Host Management Configuration', enabling standard host management across all EC2 instances inside an account automatically, removing manual profile attachment requirements.
### Identity and Access

#### API Management

  - **(2022)** [Announcing new AWS IAM Identity Center APIs to manage users and groups at scale](https://aws.amazon.com/blogs/security/announcing-new-aws-iam-identity-center-apis-to-manage-users-and-groups-at-scale) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS expanded its IAM Identity Center with programmatic APIs for user and group management. These endpoints facilitate Automated Provisioning (SCIM-based or native) and deep integration with existing external Identity Providers (IdPs) and custom HR software to manage lifecycle identities systematically.
#### Access Control

  - **(2022)** [AWS Single Sign-On (AWS SSO) adds support for AWS Identity and Access Management (IAM) customer managed policies (CMPs)](https://aws.amazon.com/about-aws/whats-new/2022/07/aws-single-sign-on-aws-sso-aws-identity-access-management-iam-customer-managed-policies-cmps) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS SSO (IAM Identity Center) updated its permission set capabilities to reference customer managed policies (CMPs) stored in individual target AWS accounts. This feature simplifies complex migration paths and permits granular, regional policy management without duplicating policy definitions inside the central identity center interface.
#### Directory Services

  - **(2022)** [AWS Single Sign-On launches configurable synchronization for Microsoft Active Directory](https://aws.amazon.com/about-aws/whats-new/2022/04/aws-single-sign-on-configurable-synchronization-microsoft-active-directory) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Single Sign-On (now IAM Identity Center) introduced customizable directory synchronization options for Microsoft Active Directory (AD). This feature allows administrators to select specific AD groups and users for propagation into AWS, optimizing synchronization times and preventing clutter in large-scale multi-account environments.
#### MFA

  - **(2022)** [AWS Identity and Access Management now supports multiple multi-factor authentication (MFA) devices](https://aws.amazon.com/about-aws/whats-new/2022/11/aws-identity-access-management-multi-factor-authentication-devices) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS IAM added support for registering multiple Multi-Factor Authentication (MFA) devices per user. This increases structural resiliency for root and administrative users, allowing the configuration of both physical security keys and authenticator applications to prevent lockout scenarios.
#### Privilege Management

  - **(2023)** [Temporary elevated access management with IAM Identity Center](https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS IAM Identity Center introduced temporary elevated access mechanisms. This feature implements time-bound, audited administrative permissions (just-in-time privilege escalation), mitigating risks from persistently elevated root and operator access.
#### Session Management

  - **(2022)** [IAM Identity Center adds session management features for improved user experience and cloud security](https://aws.amazon.com/about-aws/whats-new/2022/10/iam-identity-center-session-management-features-improved-user-experience-cloud-security) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS IAM Identity Center introduced consolidated session management settings. Security administrators can configure custom session duration limits for both portal and command-line access, enforcing systematic re-authentication and improving overall organizational compliance.
### Market Analysis

#### Critical Review

  - **(2021)** [theregister.com: The big AWS event: 120 announcements but nothing has changed](https://www.theregister.com/off-prem/2021/12/09/the-big-aws-event-120-announcements-but-nothing-has-changed/605657) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a critical perspective on the massive volume of re:Invent releases, arguing that many represent incremental API upgrades rather than fundamental architectural breakthroughs. The article challenges tech teams to focus on core design architectures rather than chasing every new managed wrapper. It serves as a pragmatic guide against architectural over-engineering.
#### Reinvent Announcements

  - **(2021)** [**aws.amazon.com/blogs: Top Announcements of AWS re:Invent 2021**](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2021) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Synthesizes the major platform transformations unveiled at re:Invent 2021, focusing on serverless options for Redshift, EMR, and MSK alongside new Graviton3 silicon. The catalog underscores a massive architectural drive towards serverless operational models across the analytics stack. These updates solidify AWS's platform-as-a-service offerings for enterprise engineering.
  - **(2021)** [**infoq.com: Recap of AWS re:Invent 2021**](https://www.infoq.com/news/2021/12/recap-reinvent-2021) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Delivers an industry analyst review of re:Invent 2021's technical releases, capturing structural advancements across compute, databases, and serverless compute paradigms. Key topics include AWS Mainframe Modernization, IoT FleetWise, and security standard compliance tooling. It maps out these ecosystem developments to long-term enterprise migration strategies.
### Messaging

#### Event-driven

  - **(2022)** [Amazon SNS increases the default quota for subscription filter policies by 50x to 10,000 per account](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-sns-increases-default-quota-subscription-filter-policies-account) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon SNS increased the default subscription filter policy limit 50-fold to 10,000 per account. This enhancement permits highly granular filtering configurations within event-driven architectures, eliminating the need to deploy complex dispatch microservices to parse message payloads.
### Migration

#### VM Import Export

  - **(2021)** [EC2 VM Import/Export now supports migration of virtual machines with Unified Extensible Firmware Interface (UEFI) boot to AWS](https://aws.amazon.com/about-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Extends the VM Import/Export service to support the migration of virtual machines using UEFI (Unified Extensible Firmware Interface) bootloader architectures. This standardizes migration pipelines for modern on-premises systems, bypassing tedious BIOS-conversion steps. It enables automated VM transition directly into modern EC2 nitro-based instance types.
### Networking

#### CDN Security

  - **(2023)** [Amazon CloudFront announces one-click security protections](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-cloudfront-one-click-security-protections) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon CloudFront introduced one-click security enablement, letting users easily provision AWS WAF protection directly from their CDN resource portal, simplifying deployment patterns.
#### Deprecations

  - **(2021)** [**theregister.com: AWS to retire EC2-Classic – the network glue that helped start the IaaS rush**](https://www.theregister.com/off-prem/2021/07/29/aws-to-retire-ec2-classic-the-network-glue-that-helped-start-the-iaas-rush/527489) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Marks the official EOL of AWS's original flat network topology (EC2-Classic), mandating migration to Virtual Private Cloud (VPC) architectures. This deprecation signals the end of shared, non-isolated public IP spaces in cloud compute, enforcing VPC-level security controls, security groups, and routing isolation. Migrations required standardizing VM instances onto modern VPC-only networking models.
  - **(2021)** [**EC2-Classic Networking is Retiring – Here’s How to Prepare**](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Migration guidelines and operational playbooks assisting AWS accounts in transitioning off legacy EC2-Classic networks onto modern Amazon VPC resources. The blueprint outlines migration tools (ClassicLink) and technical paths to reconstruct security policies, network routing, and host configurations within dedicated VPC perimeters.
#### Hybrid Connectivity

  - **(2021)** [AWS Site-to-Site VPN releases updated Download Configuration utility](https://aws.amazon.com/about-aws/whats-new/2021/09/aws-site-to-site-vpn-download-configuration-utility) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An upgraded utility providing customized configuration templates for a wider variety of Customer Gateway (CGW) devices during hybrid VPN setups. This tool streamlines the deployment of secure IPsec tunnels by providing templated scripts for Cisco, Juniper, Fortinet, and generic routers. It guarantees cryptographic and routing parameter parity between on-prem and AWS.
#### Load Balancing

  - **(2021)** [==Application Load Balancer now enables AWS PrivateLink and static IP addresses by direct integration with Network Load Balancer==](https://aws.amazon.com/about-aws/whats-new/2021/09/application-load-balancer-aws-privatelink-static-ip-addresses-network-load-balancer) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces direct, native integration between Application Load Balancers (ALB) and Network Load Balancers (NLB), enabling ALBs to leverage static IP addresses and register with AWS PrivateLink. This native bridge removes the complex AWS Lambda-based IP-sync workarounds. It allows organizations to expose Layer 7 HTTP/HTTPS routing routes securely over private, non-routable VPC endpoints.
  - **(2022)** [Application Load Balancers now support turning off cross zone load balancing per target group](https://aws.amazon.com/about-aws/whats-new/2022/11/application-load-balancers-turning-off-cross-zone-load-balancing-per-target-group) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS ALB added fine-grained control to disable cross-zone load balancing at the target group level rather than globally. This facilitates localized traffic routing within individual Availability Zones, lowering inter-AZ data transfer costs and optimizing latency profiles.
#### NAT Gateway

  - **(2022)** [Amazon NAT Gateway Now Allows You to Select Private IP Address for Network Address Translation](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-nat-gateway-allows-select-private-ip-address-network-address-translation) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon NAT Gateway updated its networking capabilities to let administrators manually assign secondary private IP addresses for outbound traffic. This enables easier integration with transit networks, transit gateways, and hybrid cloud routes where source-IP restrictions apply.
#### Network Security

  - **(2021)** [==New – Amazon VPC Network Access Analyzer==](https://aws.amazon.com/blogs/aws/new-amazon-vpc-network-access-analyzer) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A formal network verification tool that uses mathematical analysis (automated reasoning) to check VPC security policies and network access paths. It helps teams identify unintended network configurations, verify access boundaries, and demonstrate compliance to internal/external security audits. Architecturally, it automates manual firewall reviews and prevents security isolation leaks.
  - **(2021)** [**AWS Network Firewall – Nuevo Servicio Gestionado de Firewall para VPC**](https://aws.amazon.com/es/blogs/aws-spanish/aws-network-firewall-nuevo-servicio-gestionado-de-firewall-para-vpc) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Un análisis en español sobre AWS Network Firewall, detallando cómo este servicio gestionado de seguridad perimetral proporciona inspección de paquetes activa, prevención de intrusiones (IPS) y filtrado de URL. Arquitectónicamente, se integra con Transit Gateway para asegurar de manera centralizada el tráfico de entrada y salida a nivel de VPC corporativo.
#### Security Groups

  - **(2021)** [==Easily Manage Security Group Rules with the New Security Group Rule ID==](https://aws.amazon.com/blogs/aws/easily-manage-security-group-rules-with-the-new-security-group-rule-id) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces a unique identifier for each security group rule (sgr-xxxxxxxx), making rules individually addressable via API, CLI, or IaC. This drastically improves the management of firewall exceptions, allowing developers to target, modify, or audit precise rules without referencing the complete rule block list. It prevents race conditions and conflicts in IaC pipelines like Terraform.
  - **(2021)** [**Amazon Virtual Private Cloud (VPC) customers can now resize their prefix list**](https://aws.amazon.com/about-aws/whats-new/2021/08/amazon-vpc-resize-prefix-list) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Introduces the capability to dynamically resize customer-managed prefix lists, allowing cloud engineers to adjust IP range counts without recreating dependent security groups or route tables. This update simplifies network security operations at scale by removing the rigid limits on custom prefix dimensions. Architecturally, it serves as a critical automation capability for large transit gateway deployments.
#### VPC Addressing

  - **(2021)** [==Amazon Virtual Private Cloud (VPC) customers can now assign IP prefixes to their EC2 instances==](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-virtual-private-cloud-vpc-customers-can-assign-ip-prefixes-ec2-instances) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Identical announcement enabling continuous IP prefixes to be allocated directly to EC2 instances. Architecturally, this bypasses elastic network interface (ENI) private IP limit caps, expanding physical capacity constraints for highly scaled Kubernetes EKS clusters. It simplifies route propagation configurations and scales pod-per-node capacity.
#### VPC Visualization

  - **(2023)** [New – Visualize Your VPC Resources from Amazon VPC Creation Experience](https://aws.amazon.com/blogs/aws/new-visualize-your-vpc-resources-from-amazon-vpc-creation-experience) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The Amazon VPC creation workflow introduced real-time topology visualization. As operators configure subnets, route tables, and internet gateways, the system renders a dynamic layout diagram to prevent configuration errors.
### Observability

#### Managed Monitoring

  - **(2021)** [Amazon Managed Grafana Is Now Generally Available with Many New Features](https://aws.amazon.com/blogs/aws/amazon-managed-grafana-is-now-generally-available-with-many-new-features) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon Managed Grafana (AMG) is a fully managed service that simplifies the deployment, operation, and scaling of Grafana dashboards across diverse data sources. It natively integrates with AWS security and IAM systems, offering high-availability visualization of metrics, logs, and traces without administrative overhead.
#### Metric Extraction

  - **(2023)** [Amazon CloudWatch now supports high resolution metric extraction from structured logs](https://aws.amazon.com/about-aws/whats-new/2023/02/amazon-cloudwatch-high-resolution-metric-extraction-structured-logs) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon CloudWatch introduced high-resolution metric extraction from structured JSON logs. This update enables operators to parse nested log structures in real-time and generate metrics with sub-minute granularity, supporting rapid incident detection in distributed setups.
#### Metrics

  - **(2022)** [Introducing Amazon CloudWatch Metrics Insights (General Availability)](https://aws.amazon.com/about-aws/whats-new/2022/04/amazon-cloudwatch-metrics-insights) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon CloudWatch Metrics Insights is a highly performant SQL-based query engine that allows developers and administrators to analyze system metrics at scale in real-time. It enables querying millions of metrics dynamically, grouping by dimensions, and creating dashboard visualizers to pinpoint anomalous behaviors rapidly across distributed cloud architectures.
#### Multi-account

  - **(2022)** [Amazon CloudWatch launches cross-account observability across multiple AWS accounts](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-cloudwatch-cross-account-observability-multiple-aws-accounts) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon CloudWatch added native cross-account observability, enabling operators to aggregate and query metrics, logs, and traces seamlessly across multiple target accounts in an organization. This removes the need for custom ingestion microservices and pipelines to centralize application telemetry.
### Security (1)

#### Ddos Protection

  - **(2022)** [AWS Shield Advanced now supports Application Load Balancer for automatic application layer DDoS mitigation](https://aws.amazon.com/about-aws/whats-new/2022/04/aws-shield-application-balancer-automatic-ddos-mitigation) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Shield Advanced introduced automatic mitigation of application layer (Layer 7) DDoS attacks for Application Load Balancers (ALB). This capability dynamically creates, tests, and deploys AWS WAF rules on behalf of the user to block malicious traffic patterns, reducing manual intervention and minimizing downstream application downtime during sustained attacks.
#### Key Management

  - **(2022)** [Announcing AWS KMS External Key Store (XKS)](https://aws.amazon.com/blogs/aws/announcing-aws-kms-external-key-store-xks) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS KMS External Key Store (XKS) allows customers to secure cloud-stored data using keys held on hardware security modules (HSMs) outside of AWS. This architectural integration helps enterprises satisfy strict digital sovereignty and regulatory constraints.
#### Network Firewall

  - **(2023)** [AWS Network Firewall now supports tag-based resource groups](https://aws.amazon.com/about-aws/whats-new/2023/02/aws-network-firewall-tag-based-resource-groups) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Network Firewall updated its rules engines to resolve tag-based resource groups dynamically. This modification enables security teams to configure static firewall rules that adapt automatically as VPC networks or instances scale.
#### Policy Generation

  - **(2022)** [IAM Access Analyzer now reviews your AWS CloudTrail history to identify actions used across 140 AWS services and generates fine-grained policies](https://aws.amazon.com/about-aws/whats-new/2022/10/iam-access-analyzer-cloudtrail-history-identify-actions-140-aws-services-fine-grained-policies) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — IAM Access Analyzer expanded its policy generation features by parsing AWS CloudTrail history across 140 AWS services. It identifies the exact actions utilized by an IAM entity over a specific timeframe and translates that history into fine-grained, least-privilege IAM policies, mitigating risks of privilege escalation.
#### Threat Detection

  - **(2023)** [Amazon GuardDuty now available in AWS Europe (Spain) Region](https://aws.amazon.com/about-aws/whats-new/2023/02/amazon-guardduty-aws-europe-spain-region) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS extended the availability of Amazon GuardDuty to the Europe (Spain) region. This deployment supports regional workloads with local threat intelligence and ML-driven behavior detection for AWS accounts, S3, and EKS environments.
#### Threat Hunting

  - **(2023)** [Amazon Detective adds graph visualization for interactive security investigations](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-detective-graph-visualization-interactive-security-investigations) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon Detective updated its threat-hunting capabilities with interactive graph visualizations. Security analysts can trace access relationships, API anomalies, and suspicious activity logs visually across multi-account ecosystems.
#### WAF Rules

  - **(2023)** [AWS WAF enhances rate-based rules to support request headers and composite keys](https://aws.amazon.com/about-aws/whats-new/2023/05/aws-waf-rate-based-rules-request-headers-composite-keys) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS WAF updated rate-limiting rules to support composite key inspection, combining IP with headers, cookies, or query arguments. This helps target and neutralize sophisticated distributed L7 attacks.
### Security and Service Mesh

#### Hashicorp HCP

  - **(2021)** [**thenewstack.io: HashiCorp Adds Consul and Vault to Cloud Platform for AWS**](https://thenewstack.io/hashicorp-adds-consul-and-vault-to-cloud-platform-for-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Launches fully managed Consul and Vault offerings on the HashiCorp Cloud Platform (HCP) integrated with AWS. This allows engineering teams to leverage secure secret storage and high-performance service mesh patterns without operational cluster overhead. Architecturally, it integrates seamlessly into AWS VPC routing and transit gateway topologies.
### Serverless (1)

#### Compute (2)

  - **(2022)** [AWS Lambda Now Supports Up to 10 GB Ephemeral Storage](https://aws.amazon.com/blogs/aws/aws-lambda-now-supports-up-to-10-gb-ephemeral-storage) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Lambda's configuration options permit allocating up to 10 GB of ephemeral /tmp storage, up from the previous 512 MB limit. This architectural enhancement enables serverless executions to process larger datasets, run machine learning inference, and perform intensive ETL operations directly within memory-backed local storage, significantly expanding the viability of serverless data pipelines.
#### Developer Tooling

  - **(2023)** [AWS SAM CLI introduces ‘sam list’ command to inspect AWS SAM resources](https://aws.amazon.com/about-aws/whats-new/2023/02/aws-sam-cli-sam-list-command-inspect-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS SAM CLI introduced the 'sam list' command to improve local diagnostics for serverless stacks. This tool displays resource endpoints, IAM roles, and stack states directly within the terminal, streamlining deployment workflows.
### Storage (1)

#### EFS

  - **(2022)** [**Announcing Amazon Elastic File System Replication**](https://aws.amazon.com/about-aws/whats-new/2022/01/amazon-elastic-file-system-replication) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Launches a native replication solution for EFS, automating the replication of file systems across different AWS Regions or within the same Region. It guarantees point-in-time consistency and helps meet disaster recovery (DR) RPO and RTO compliance goals. This deprecates the need for custom rsync-based replication agents on EC2.
  - **(2022)** [**infoq.com: Amazon Announces Elastic File System Replication for Multi-Region Deployments**](https://www.infoq.com/news/2022/02/aws-efs-replication) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Evaluates the release of native EFS replication, focusing on its integration with hybrid file storage strategies and automated failover pipelines. It details how the sub-minute RPO simplifies business continuity architectures across multi-region EKS stateful workloads. The solution delivers automated metadata synchronization, optimizing engineering resources.
### Storage and Backup

#### Compliance (1)

  - **(2022)** [AWS Backup Audit Manager adds centralized reporting for AWS Organizations](https://aws.amazon.com/about-aws/whats-new/2022/11/aws-backup-audit-manager-centralized-reporting-aws-organizations) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Backup Audit Manager introduced consolidated, cross-account backup compliance reporting across AWS Organizations. Enterprise operators can monitor backup policies, tracking non-compliance trends dynamically from a singular delegator dashboard.
#### S3 Security

  - **(2022)** [Heads-Up: Amazon S3 Security Changes Are Coming in April of 2023](https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS pre-announced default security hardening measures for Amazon S3 buckets. These updates block public access configurations by default and enforce bucket owner-enforced Object Ownership settings to automatically disable ACLs on new bucketing workloads.
### Virtualization

#### VDI

  - **(2022)** [Amazon WorkSpaces Introduces Ubuntu Desktops](https://aws.amazon.com/blogs/aws/amazon-workspaces-introduces-ubuntu-desktops) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon WorkSpaces extended its managed Virtual Desktop Infrastructure (VDI) to offer Ubuntu Desktop environments. Intended primarily for developers, data scientists, and engineers, this addition provides a secure, cloud-hosted Linux workspace preconfigured with developer utilities and standardized enterprise authentication.
## Containers

### Kubernetes

#### EKS Console

  - **(2021)** [**Visualize all your Kubernetes clusters in one place with Amazon EKS Connector, now generally available**](https://aws.amazon.com/about-aws/whats-new/2021/11/visualize-kubernetes-clusters-one-place-amazon-eks-connector-generally-available) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Enables registering and visualizing any Kubernetes cluster—on-premises, on EC2, or other cloud providers—directly inside the AWS EKS console. It acts as an outbound agent, linking remote clusters safely to AWS IAM and AWS Console views. It offers a single-pane-of-glass platform to observe multi-cloud and hybrid Kubernetes estates.
#### EKS Networking

  - **(2021)** [==Amazon VPC CNI plugin increases pods per node limits==](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-vpc-cni-plugin-increases-pods-per-node-limits) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces Prefix Delegation in the AWS VPC CNI, multiplying the number of pods allocatable per node. By assigning /28 IPv4 prefixes to network interfaces instead of single secondary IPs, small-to-medium EC2 instances can support significantly higher container densities. This architecture directly addresses the IP exhaustion problem in enterprise Kubernetes deployments on AWS.
#### EKS Security

  - **(2021)** [==Amazon EKS clusters now support user authentication with OIDC compatible identity providers==](https://aws.amazon.com/about-aws/whats-new/2021/02/amazon-eks-clusters-support-user-authentication-oidc-compatible-identity-providers) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Enables EKS clusters to utilize external OpenID Connect (OIDC) compatible identity providers for user authentication. This decouples Kubernetes RBAC from direct IAM identity mappings, allowing developers to leverage existing SSO solutions like Okta or Keycloak. It simplifies security governance by maintaining enterprise identity standards at the cluster API level.
### Market Analysis (1)

#### Reinvent Announcements (1)

  - **(2021)** [**forbes.com: AWS re:Invent - A Roundup Of Container Services Announcements**](https://www.forbes.com/sites/janakirammsv/2021/12/03/aws-reinventa-roundup-of-container-services-announcements) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Synthesizes containerization announcements from re:Invent 2021, highlighting Karpenter, EKS Anywhere, and ECS Anywhere expansion. This analysis emphasizes AWS's push to support hybrid and multi-cloud Kubernetes deployments. It details how Karpenter challenges standard Cluster Autoscaler architectures with direct, fast provisioning of right-sized EC2 instances.
## Data and Analytics

### Data Protection

#### AWS Backup

  - **(2022)** [==Announcing the general availability of AWS Backup for Amazon S3==](https://aws.amazon.com/about-aws/whats-new/2022/02/general-availability-aws-backup-amazon-s3) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Reaches General Availability, providing complete managed backup, restore, and lifecycle orchestration of Amazon S3 data. It supports cross-region, cross-account capabilities, and immutable backup copies using AWS Backup Vault Lock. Architecturally, it streamlines data compliance audits, proving protection policies for petabyte-scale S3 data lakes.
#### Compliance (2)

  - **(2021)** [**Monitor, Evaluate, and Demonstrate Backup Compliance with AWS Backup Audit Manager**](https://aws.amazon.com/blogs/aws/monitor-evaluate-and-demonstrate-backup-compliance-with-aws-backup-audit-manager) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Introduces AWS Backup Audit Manager, a feature to monitor, evaluate, and demonstrate the compliance posture of data backup operations against pre-defined organizational standard controls. It automates compliance reporting, providing auditor-ready historical evidence. Architecturally, it replaces manual backup audits and ensures strict data governance.
### Data Streaming

#### Kinesis

  - **(2021)** [==infoq.com: AWS Launches Amazon Kinesis Data Streams On-Demand==](https://www.infoq.com/news/2021/12/kinesis-data-streams-ondemand) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces a serverless, on-demand capacity mode for Kinesis Data Streams, automatically scaling write and read throughput to match unpredictable traffic patterns. This model eliminates the requirement for shard planning, capacity monitoring, and custom-scaling scripts. Architecturally, it makes streaming pipelines easier to operate while optimizing costs for variable workloads.
### Data Warehouse

#### Redshift

  - **(2021)** [==Announcing General Availability of Amazon Redshift Cross-account Data Sharing==](https://aws.amazon.com/about-aws/whats-new/2021/08/announcing-general-availability-amazon-redshift-cross-account-data-sharing) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Allows instant, secure data sharing across different Amazon Redshift clusters and AWS accounts without moving or copying data. It decouples storage from compute, allowing downstream analytic nodes or consumers to run isolated queries against shared data structures in real-time. This drastically optimizes data lake engineering architectures.
## Databases (1)

### RDS Proxy

#### Networking (1)

  - **(2021)** [**Amazon RDS Proxy can now be created in a shared Virtual Private Cloud (VPC)**](https://aws.amazon.com/about-aws/whats-new/2021/08/amazon-rds-proxy-created-shared-virtual-private-cloud-vpc) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Extends Amazon RDS Proxy capabilities to shared VPCs (Resource Access Manager environments), allowing centralized application environments to pool and multiplex database connections across multiple AWS accounts. By managing highly volatile database connection limits from serverless microservices, it enhances application performance and resilience. Architecturally, it decouples the database infrastructure layer from consumer VPC microservices.
### Relational Database

#### RDS High Availability

  - **(2022)** [==infoq.com: Amazon RDS Introduces Readable Standby Instances in Multi-AZ Deployments==](https://www.infoq.com/news/2022/01/aws-rds-readable-standby) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces Multi-AZ deployments with two readable standby instances, allowing read queries to be offloaded from the primary instance while offering sub-35 second automatic failovers. Architecturally, this maximizes utilization of standby infrastructure while scaling database read throughput significantly. It is highly beneficial for transaction-heavy workloads with strong analytics or reporting requirements.
## Infrastructure As Code

### Cloudformation

#### State Management

  - **(2021)** [**New for AWS CloudFormation – Quickly Retry Stack Operations from the Point of Failure**](https://aws.amazon.com/es/blogs/aws/new-for-aws-cloudformation-quickly-retry-stack-operations-from-the-point-of-failure) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Introduces the ability to retry failed CloudFormation stack operations from the point of failure, omitting the need to rollback and rebuild the entire deployment from scratch. This drastically optimizes development feedback loops, especially when dealing with flaky external resources or transient timeouts. It dramatically changes IaC debugging workflows on AWS.
## Observability (1)

### Cloudwatch

#### Access Management

  - **(2021)** [aws.amazon.com: Share your Amazon CloudWatch Dashboards with anyone using AWS Single Sign-On](https://aws.amazon.com/blogs/mt/share-your-amazon-cloudwatch-dashboards-with-anyone-using-aws-single-sign-on) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Enables engineers to share CloudWatch dashboards with stakeholders outside the AWS Console using IAM Identity Center (formerly AWS SSO). This decouples operations visualization from root access management, offering a secure path to operational metrics. It ensures fine-grained dashboard sharing across federated organizational entities.
#### Multi-account Monitoring

  - **(2021)** [**infoq.com: Amazon Introduces Cloudwatch Cross Account Alarms to Consolidate Management**](https://www.infoq.com/news/2021/08/aws-cloudwatch-alarms) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Introduces CloudWatch cross-account alarms, enabling teams to aggregate telemetry, trace metrics, and execute operational alerts from multiple AWS accounts under a single monitoring cockpit. It aligns with multi-account architectural landing zones, minimizing alert-routing complexity. It enhances real-time incident remediation by centralizing operational context.
### Grafana

#### Managed Visualization

  - **(2021)** [**Amazon Managed Service for Grafana (AMG) preview updated with new capabilities**](https://aws.amazon.com/blogs/mt/amazon-managed-service-for-grafana-amg-preview-updated-with-new-capabilities) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Outlines preview enhancements to AMG, incorporating support for Grafana Enterprise upgrades, security posture controls, and direct data source connectivity (Prometheus, CloudWatch, OpenSearch). This update automates visualization scaling and secures connection configurations. It forms a central visualization plane across AWS-managed monitoring services.
### Opentelemetry

#### Distributed Tracing

  - **(2021)** [==New for AWS Distro for OpenTelemetry – Tracing Support is Now Generally Available==](https://aws.amazon.com/blogs/aws/new-for-aws-distro-for-opentelemetry-tracing-support-is-now-generally-available) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Generally available, AWS-supported distribution of the CNCF OpenTelemetry standards, specifically optimized for application tracing. It simplifies collecting metadata and correlates application traces across containerized (EKS, ECS) and serverless (Lambda) stacks. It seamlessly forwards telemetry to AWS X-Ray, Amazon OpenSearch, and partner SaaS platforms, eliminating vendor lock-in.
### Prometheus

#### Managed Container Monitoring

  - **(2021)** [==siliconangle.com: Amazon debuts fully managed, Prometheus-based container monitoring service==](https://siliconangle.com/2021/09/29/amazon-debuts-fully-managed-prometheus-based-container-monitoring-service) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Launches a fully managed, Prometheus-compatible monitoring service designed to ingest, store, and query operational metrics from Kubernetes and ECS environments. Architecturally, it scales automatically to billions of metrics, leveraging Cortex technology for high-availability multi-zone persistence. It reduces the administrative overhead of managing large, DIY Prometheus TSDB clusters.
  - **(2021)** [==aws.amazon.com: Amazon Managed Service for Prometheus Is Now Generally Available with Alert Manager and Ruler==](https://aws.amazon.com/blogs/aws/amazon-managed-service-for-prometheus-is-now-generally-available-with-alert-manager-and-ruler) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Reaches General Availability, adding key enterprise capabilities such as Alert Manager and Ruler. Users can define native Prometheus alerting rules and route alerts to downstream incident response hubs like PagerDuty or AWS SNS. It reinforces the managed monitoring story by guaranteeing security, high availability, and out-of-the-box multi-region reliability.
## Security and Compliance

### Cloud Security Posture

#### Security Hub

  - **(2021)** [**AWS Security Hub adds 18 new controls to its Foundational Security Best Practices standard and 8 new partners for enhanced cloud security posture monitoring**](https://aws.amazon.com/about-aws/whats-new/2021/08/aws-security-hub-adds-18-new-controls-foundational-security-best-practices-standard-8-new-partners-enhanced-cloud-security-posture-monitoring) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Expands AWS Security Hub with 18 automated security checks covering IAM, EC2, and S3, alongside new integrations with third-party partners. This upgrade provides continuous compliance checks aligned with the AWS Foundational Security Best Practices standard. It gives security engineers real-time visibility and a consolidated dashboard for vulnerability posture scoring.
### Vulnerability Management

#### Inspector

  - **(2021)** [**AWS announces the new **Amazon Inspector** for continual vulnerability management**](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-inspector-continual-vulnerability-management) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Overhauls Amazon Inspector into a service offering continuous, automated vulnerability management for EC2 and container images. Instead of run-on-demand periodic scans, it dynamically evaluates the environment in response to system changes and newly published CVEs. It integrates with AWS Organizations, allowing security groups to manage scanning centrally.
## Software Engineering

### AI Code Analysis

#### Developer Enablement

  - **(2021)** [Introducing new self-paced courses to improve Java and Python code quality with Amazon CodeGuru](https://aws.amazon.com/blogs/devops/new-self-paced-courses-to-improve-java-and-python-code-quality-with-amazon-codeguru) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Educational curriculum focusing on utilizing CodeGuru's machine-learning engines to detect concurrency bugs, resource leaks, and performance bottlenecks in Java and Python. These courses provide hands-on telemetry guides to maximize DevSecOps efficiency. Architecturally, CodeGuru integrates into CI/CD pipelines to enforce static and dynamic code quality.

---
💡 **Explore Related:** [AWS Storage](./aws-storage.md) | [AWS](./aws.md) | [Azure](./azure.md)

🔗 **See Also:** [Cloud Asset Inventory](./cloud-asset-inventory.md) | [Kubernetes Storage](./kubernetes-storage.md)

