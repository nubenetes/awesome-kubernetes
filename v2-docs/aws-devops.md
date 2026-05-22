# Aws Devops

!!! info "Architectural Context"
    Detailed reference for Aws Devops in the context of Cloud Providers (Hyperscalers).

## Advanced Orchestration

### Multi Cluster

#### Fargate Integrations

  - **(2020)** [thenewstack.io: Making Kubernetes Serverless and Global with AWS Fargate on EKS and Admiralty](https://thenewstack.io/making-kubernetes-serverless-and-global-with-aws-fargate-on-eks-and-admiralty) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An evaluation of federating multi-region environments using serverless AWS Fargate and Admiralty.
Live Grounding: Details technical patterns to schedule workloads seamlessly between local EKS control planes and globally distributed, dynamic Fargate runtimes.
  - **(2020)** [admiralty.io: Multi-Region AWS Fargate on EKS](https://admiralty.io/docs/tutorials/fargate) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Technical documentation on configuring Multi-Region AWS Fargate nodes with Admiralty.
Live Grounding: Demonstrates step-by-step scheduling configurations, enabling cross-region workload scaling without operating full node instances across geographical environments.
#### Federation

  - **(2021)** [admiralty.io](https://admiralty.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Domain hosting Admiralty, a Kubernetes multi-cluster scheduler platform.
Live Grounding: The active development has stalled, but the architecture remains highly relevant for federation research, featuring cross-cluster pod scheduling and proxy-pods.
## Public Cloud Infrastructure

### AWS Architecture

#### Multi-Region Blueprints

  - **(2021)** [**Multi-Region Infrastructure Deployment**](https://aws.amazon.com/solutions) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: AWS Solutions library offering reference architectures for high-availability setups.
Live Grounding: Provides automated CloudFormation and CDK deployment configurations to orchestrate secure application instances across multiple geographical AWS regions.
### AWS Ecosystem

#### AI Ops

  - **(2021)** [infoq.com: AWS Launches Amazon DevOps Guru](https://www.infoq.com/news/2021/01/aws-devops-guru)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: InfoQ coverage detailing the launch of AWS DevOps Guru, an ML-powered monitoring tool.
Live Grounding: Breaks down how the service analyzes telemetry, logs, and trace patterns to automatically flag operational anomalies and offer remediation instructions.
#### Blogs and Updates

  - **(2021)** [AWS DevOps Blog](https://aws.amazon.com/blogs/devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: AWS official publication hub for cloud DevOps patterns, updates, and releases.
Live Grounding: Essential feed for continuous updates regarding AWS systems manager, ECS integrations, EKS blue-green patterns, and IAM-driven secure delivery strategies.
#### CI CD Orchestration

  - **(2021)** [Continuous Deployment with AWS](https://aws.amazon.com/blogs/devops/tag/continuous-deployment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Aggregation of blogs detailing best practices for deploying continuous deployment on AWS.
Live Grounding: Covers pipeline design principles, canary deployments, safety testing strategies, and blue-green transitions using managed AWS components.
  - **(2020)** [aws.amazon.com: AWS CodePipeline adds support for Branch-based development and Monorepos](https://aws.amazon.com/blogs/devops/aws-codepipeline-adds-support-for-branch-based-development-and-monorepos)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Deep-dive blog introducing native monorepo and branch filters inside CodePipeline.
Live Grounding: Focuses on configuring webhooks and filtering schemas to isolate triggers based on altered directories inside Git repositories.
#### CodePipeline Integrations

  - **(2020)** [AWS Partner Network - CodePipeline Integrations](https://aws.amazon.com/es/codepipeline/product-integrations) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Directory of verified third-party partner integrations for AWS CodePipeline.
Live Grounding: Outlines deployment connectors, security scanners, and test suites that integrate directly into managed pipelines. Spanish localized interface. [SPANISH CONTENT]
#### Deployment Guides

  - **(2020)** [adamtheautomator.com: Getting Started with AWS CodeDeploy](https://adamtheautomator.com/aws-codedeploy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Tutorial introducing AWS CodeDeploy setups for hosting infrastructure applications.
Live Grounding: Details step-by-step agent configurations on target environments, build specs, and continuous rollout patterns using the CodeDeploy service.
#### Infrastructure as Code

  - **(2021)** [aws.amazon.com: Multi-branch pipeline management and infrastructure deployment using AWS CDK Pipelines](https://aws.amazon.com/blogs/devops/multi-branch-pipeline-management-and-infrastructure-deployment-using-aws-cdk-pipelines) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Tutorial for managing multi-branch infrastructures using AWS Cloud Development Kit.
Live Grounding: Explains how to orchestrate automated pipeline synthesis, ensuring branches match dynamic test environments with zero manual intervention.
#### Legacy CI CD Integrations

  - **(2018)** [Setting Up the Jenkins Plugin for AWS CodeDeploy](https://aws.amazon.com/blogs/devops/setting-up-the-jenkins-plugin-for-aws-codedeploy)  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: Guide for setting up AWS CodeDeploy integration hooks inside Jenkins environments.
Live Grounding: While primarily legacy, it outlines key patterns for mapping standard Jenkins build output artifacts directly onto the CodeDeploy engine.
### Cloud Comparison

#### DevOps Methodologies

  - **(2020)** [k21academy.com: AWS DevOps Vs. Azure DevOps](https://k21academy.com/aws-cloud/aws-devops-vs-azure-devops/?utm_source=linkedin&utm_medium=referral&utm_campaign=awsdevops17_dec20_aws_cloud_computing_for_interested_parties__users)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Comprehensive comparison article analyzing features, costs, and tooling differences.
Live Grounding: Detailed comparative resource mapping the architectural equivalents between AWS developer tooling and Azure DevOps systems.

---
💡 **Explore Related:** [Aws Storage](./aws-storage.md) | [Aws Tools Scripts](./aws-tools-scripts.md) | [Aws Databases](./aws-databases.md)

