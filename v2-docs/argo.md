# Argo

!!! info "Architectural Context"
    Detailed reference for Argo in the context of Engineering Pipeline.

## Application Delivery

### GitOps

#### AWS EKS

  - **(2023)** [dev.to/devsatasurion: Deploying Applications with GitHub Actions and ArgoCD to EKS: Best Practices and Techniques](https://dev.to/devsatasurion/deploying-applications-with-github-actions-and-argocd-to-eks-best-practices-and-techniques-4epc) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Walkthrough for building a secure deployment pipeline connecting GitHub Actions, Argo CD, and AWS EKS. Live Grounding: Focuses on modern identity protocols like OIDC for IAM role assumption, minimizing the need for static credentials inside CI/CD workflows, and boosting security posture.
#### Architectural Patterns

  - **(2023)** [**akuity.io: How many do you need? - Argo CD Architectures Explained**](https://akuity.io/blog/argo-cd-architectures-explained) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Compares and contrasts different deployment topologies for Argo CD, including mono-cluster, hub-and-spoke, and fully decentralized models. Live Grounding: Essential for cloud architects designing multi-tenant platforms, detailing scaling limits, networking requirements, and blast radius control for high-scale GitOps systems.
#### Argo CD ApplicationSet

  - **(2024)** [==argoproj-labs/applicationset: Argo CD ApplicationSet Controller==](https://github.com/argoproj/applicationset) <span class='md-tag md-tag--info'>⭐ 583</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: The standard orchestrator that extends Argo CD to support multicluster application distribution templates. Live Grounding: Key component that processes multi-source configurations, automates environment scaling, and drastically reduces the maintenance overhead of managing distinct Application manifests.
  - **(2024)** [**developers.redhat.com: Enhance Kubernetes deployment efficiency with Argo CD and ApplicationSet**](https://developers.redhat.com/articles/2024/06/06/enhance-kubernetes-deployment-efficiency-argo-cd-and-applicationset) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: An authoritative Red Hat guide detailing the features and performance metrics of the Argo CD ApplicationSet controller. Live Grounding: Outlines practical implementations of Git, List, and Matrix generators to deploy standardized applications to hundreds of target environments using declarative, single-file templates.
#### Bootstrapping

  - **(2024)** [==argoproj-labs/argocd-autopilot: Argo-CD Autopilot==](https://github.com/argoproj-labs/argocd-autopilot) <span class='md-tag md-tag--info'>⭐ 1117</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: An official Argo project opinionated tool designed to structure, install, and update Argo CD setups automatically. Live Grounding: Uses a clean directory structure separating infrastructure from application manifests, enabling rapid multi-project bootstrap with built-in version tracking and disaster recovery features.
#### CI-CD Integration

  - **(2023)** [dev.to: Extending GitOps: Effortless continuous integration and deployment on Kubernetes](https://dev.to/amplication/extending-gitops-effortless-continuous-integration-and-deployment-on-kubernetes-1oem) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Examines the convergence of Continuous Integration (CI) and GitOps (CD) loops on Kubernetes clusters. Live Grounding: Covers the integration of automated code generation tools like Amplication with declarative Kubernetes pipelines, simplifying lifecycle paths from commit to live release.
#### Infrastructure as Code

  - **(2023)** [seraf.dev: ArgoCD Tutorial — (with Terraform)](https://seraf.dev/argocd-tutorial-with-terraform-af77ddea2e6e) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Illustrates the bootstrap process of Argo CD onto a Kubernetes cluster utilizing the Terraform Helm provider. Live Grounding: Highlights the orchestration boundary between infrastructure provisioning and application GitOps adoption, establishing a reliable continuous delivery baseline.
#### Multi-Cluster

  - **(2022)** [**piotrminkowski.com: Manage Multiple Kubernetes Clusters with ArgoCD 🌟**](https://piotrminkowski.com/2022/12/09/manage-multiple-kubernetes-clusters-with-argocd) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Hands-on walk-through for registering and managing multiple target Kubernetes clusters via a single control-plane Argo CD instance. Live Grounding: Provides practical manifests and CLI examples to manage cluster resources and application distributions efficiently across hybrid cloud boundaries.
#### Operator Lifecycle

  - **(2023)** [piotrminkowski.com: Manage Kubernetes Operators with ArgoCD](https://piotrminkowski.com/2023/05/05/manage-kubernetes-operators-with-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Practical analysis of orchestrating Operator lifecycles and Custom Resource Definitions (CRDs) inside Argo CD synchronization loops. Live Grounding: Explores strategies to prevent the typical race conditions and out-of-sync loops that happen when Argo CD manages system Operators alongside application manifests.
#### Plugins

  - **(2024)** [github.com/crumbhole/argocd-lovely-plugin: argocd-lovely-plugin](https://github.com/crumbhole/argocd-lovely-plugin) <span class='md-tag md-tag--info'>⭐ 487</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A highly flexible custom config management plugin (CMP) for Argo CD designed to combine Helm, Kustomize, and raw YAML seamlessly. Live Grounding: Solves the 'nested tooling' dilemma by processing multiple layers of templating without resorting to complex shell scripts inside the repo, simplifying enterprise GitOps chains.
#### Reference Architectures

  - **(2021)** [github.com/myspotontheweb/gitops-workloads-demo](https://github.com/myspotontheweb/gitops-workloads-demo) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Comprehensive demo repository showcasing real-world GitOps workload configurations, structuring apps and infra dependencies. Live Grounding: Excellent structural blueprint for organizing multi-tenant environments, demonstrating how to decouple cluster-wide configurations from individual application manifests.
#### Secret Management

  - **(2024)** [==argoproj-labs/argocd-vault-plugin==](https://github.com/argoproj-labs/argocd-vault-plugin) <span class='md-tag md-tag--info'>⭐ 965</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: An indispensable Argo CD plugin built to inject secrets dynamically from HashiCorp Vault, AWS Secrets Manager, or GCP Secret Manager. Live Grounding: Replaces custom templating hacks by decrypting and injecting secret values directly into workloads at synchronization time, ensuring zero plaintext secrets enter the Git repository.
  - **(2022)** [dev.to: Argo CD and Sealed Secrets is a perfect match](https://dev.to/timtsoitt/argo-cd-and-sealed-secrets-is-a-perfect-match-1dbf) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Explores the integration of Bitnami Sealed Secrets with Argo CD for safe GitOps secret workflows. Live Grounding: Demonstrates how public cryptography allows storing encrypted secrets safely in Git, which are decrypted only within the target Kubernetes cluster by the Sealed Secrets controller.
  - **(2021)** [github.com/crumbhole/argocd-vault-replacer](https://github.com/crumbhole/argocd-vault-replacer) <span class='md-tag md-tag--info'>⭐ 109</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A specialized replacement utility designed to pull secrets from HashiCorp Vault during the Argo CD rendering phase. Live Grounding: Acts as a lightweight precursor/alternative to full plugin integrations, enabling targeted placeholder substitutions within native Kubernetes manifest streams.
### Infrastructure as Code (1)

#### Terraform Components

  - **(2024)** [AWS EKS Argo CD Terraform Component](https://github.com/cloudposse-terraform-components/aws-eks-argocd) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Enterprise-ready Terraform submodule designed to deploy, configure, and bootstrap Argo CD onto an existing AWS EKS cluster. Live Grounding: Standardizes complex security configuration flags, integrates smoothly with AWS IAM roles for service accounts (IRSA), and provisions preconfigured Helm-based releases.
### Progressive Delivery

#### Argo Rollouts

  - **(2026)** [==argoproj.github.io/argo-rollouts/==](https://argoproj.github.io/argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Main structural index for implementing automated Canary promotions and instant Rollbacks using Prometheus metrics. Live Grounding: Essential for platform engineers aiming to achieve high-availability delivery paradigms with zero downtime by managing precise traffic routing controls.
  - **(2023)** [codefresh.io: Progressive delivery for Kubernetes Config Maps using Argo Rollouts](https://octopus.com/blog/progressive-delivery-for-kubernetes-config-maps-using-argo-rollouts) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Investigates strategies for applying progressive delivery steps directly to Kubernetes ConfigMaps and environment secrets. Live Grounding: Explains how to trigger rollouts upon configuration-only shifts, eliminating the risk of misconfigured environment variables breaking applications silently.
  - **(2022)** [infracloud.io: Progressive Delivery with Argo Rollouts : Blue-Green Deployment](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-blue-green-deployment) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Conceptual and step-by-step technical guide for configuring high-performance Blue-Green deployments with Argo Rollouts. Live Grounding: Explores the implementation of manual approval gates, automated smoke tests, and fallback protocols to transition production workloads safely.
  - **(2022)** [infracloud.io: Progressive Delivery with Argo Rollouts: Canary Deployment](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-canary-deployment) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Comprehensive guide analyzing step-based canary traffic weight shifting with Argo Rollouts. Live Grounding: Explains the integration of real-time monitoring query metrics (such as latency or error rate) to trigger automated canary rollbacks when anomalies are discovered.
#### Traffic Management

  - **(2023)** [**infracloud.io: How to Setup Blue Green Deployments with DNS Routing 🌟**](https://www.infracloud.io/blogs/blue-green-deployments-dns-routing) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Highly technical tutorial showcasing Blue-Green deployment strategies relying on external DNS routing configurations rather than standard Kubernetes Service routing. Live Grounding: Solves edge-case scenarios for non-HTTP traffic, providing patterns for high-performance multi-region workload transitions.
### Security

#### Vulnerabilities

  - **(2022)** [threatpost.com: Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers](https://threatpost.com/argo-cd-security-bug-kubernetes-cloud-apps/178239) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Discloses CVE-2022-24348, a high-severity path traversal flaw allowing unauthorized access to arbitrary cluster repositories in Argo CD. Live Grounding: Essential post-mortem detailing how custom Helm chart parameter configurations bypassed sanity validation, proving the critical need for constant dependency scanning.
  - **(2022)** [thehackernews.com: New Argo CD Bug Could Let Hackers Steal Secret Info from Kubernetes Apps](https://thehackernews.com/2022/02/new-argo-cd-bug-could-let-hackers-steal.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: News analysis of the zero-day path traversal vulnerability in Argo CD's repository rendering process. Live Grounding: Explores structural exploits where malicious manifests loaded by the server could leak other application values, highlighting the immediate need to restrict repository access parameters.
  - **(2022)** [armosec.io: CVE 2022-24348 – Argo CD High Severity Vulnerability and its impact on Kubernetes](https://www.armosec.io/blog/cve-2022-24348-argo-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Detailed technical analysis of CVE-2022-24348, breaking down the exact mechanism of the path traversal payload. Live Grounding: ARMOSec offers explicit remediation actions, network policy guidance, and best practices to isolate and secure Argo CD controller components against credential theft.
  - **(2022)** [infoworld.com: How to protect your Kubernetes infrastructure from the Argo CD vulnerability](https://www.infoworld.com/article/2334525/how-to-protect-your-kubernetes-infrastructure-from-the-argo-cd-vulnerability.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Actionable playbook detailing operational steps to patch and mitigate the path traversal vulnerability in enterprise clusters. Live Grounding: Stresses the significance of continuous configuration auditing, disabling unauthorized repository creation, and using read-only service accounts for the GitOps agent.
  - **(2022)** [securityaffairs.co: Argo CD flaw could allow stealing sensitive data from Kubernetes Apps](https://securityaffairs.com/127708/hacking/kubernetes-argo-cd-flaw.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Coverage of the architectural flaw in Argo CD that exposed critical internal server state and target configuration values. Live Grounding: Emphasizes the risk of multi-tenant environments where shared instances lack sufficient namespace isolation and RBAC constraints, making path traversal exploitation viable.
### Workflow Orchestration

#### Argo Workflows

  - **(2022)** [**blog.argoproj.io: Architecting Workflows For Reliability**](https://blog.argoproj.io/architecting-workflows-for-reliability-d33bd720c6cc) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Investigates patterns to ensure high-scale reliability when running millions of tasks inside Argo Workflows. Live Grounding: Analyzes garbage collection strategies, rate limiting, retry policies, and how to scale the underlying workflow-controller Pods to avoid etcd exhaustion.
  - **(2022)** [blog.argoproj.io: What’s new in Argo Workflows v3.3](https://blog.argoproj.io/whats-new-in-argo-workflows-v3-3-dd051d2f1c7) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Outlines the major architectural enhancements and UI features released in Argo Workflows version 3.3. Live Grounding: Highlights key security patches, multi-template updates, and visual enhancements designed to streamline the debugging of complex cloud-native data-processing pipelines.
  - **(2022)** [dev.to: The three meanings of "template" in Argo Workflows](https://dev.to/crenshaw_dev/the-three-meanings-of-template-in-argo-workflows-2paf) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Decodes the highly overloaded concept of 'templates' inside the Argo Workflows architecture, defining Container, Script, and Resource types. Live Grounding: Provides solid structural patterns for reusable components, enabling platform engineers to build clean, maintainable, and dry workflow definitions.
#### Security (1)

  - **(2022)** [**blog.argoproj.io: Practical Argo Workflows Hardening 🌟**](https://blog.argoproj.io/practical-argo-workflows-hardening-dd8429acc1ce) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: An authoritative security hardening guide designed to lock down Argo Workflows inside shared multi-tenant environments. Live Grounding: Focuses on strict RBAC roles, container security contexts, namespace network policies, and the isolation of high-privilege service accounts to prevent cluster escapes.
## Developer Platforms

### Platform Engineering

#### Architectural Strategy

  - **(2021)** [dev.to: Towards a Modular DevOps Stack](https://dev.to/camptocamp-ops/towards-a-modular-devops-stack-257c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the rise of custom developer platforms. Details how standardizing Kubernetes configuration tools builds resilient, decoupled internal cloud services.
## GitOps (1)

### Continuous Delivery

#### AWS Ecosystem

  - **(2021)** [aws.amazon.com: Cloud Native CI/CD with Tekton and ArgoCD on AWS](https://aws.amazon.com/blogs/containers/cloud-native-ci-cd-with-tekton-and-argocd-on-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Describes combined cloud-native continuous integration using Tekton alongside declarative GitOps via Argo CD on AWS, demonstrating a unified high-performance DevOps pipeline.
#### Architectural Strategy (1)

  - **(2021)** [Why and when do you need Argo CD?](https://mkdev.me/posts/why-and-when-do-you-need-argo-cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Strategic evaluation explaining the architectural differences between pushing configurations via CI and pulling them via declarative GitOps operators, positioning Argo CD's reconciliation loops.
#### Argo CD

  - **(2026)** [==argoproj.github.io: Argo CD - Declarative GitOps for Kubernetes==](https://argoproj.github.io/argo-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Argo CD is a declarative GitOps engine that automates Kubernetes deployments. By continually matching the live cluster state to git specifications, it guarantees robust security and rapid rollback features.
#### Argo CD Features

  - **(2022)** [blog.argoproj.io: New sync and diff strategies in ArgoCD](https://blog.argoproj.io/new-sync-and-diff-strategies-in-argocd-44195d3f8b8c) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines advanced diff and sync customization in modern Argo CD versions, clarifying sync waves and resource skip behaviors for complex helm-based applications.
#### Automation

  - **(2021)** [opensource.com: Automatically create multiple applications in Argo CD](https://opensource.com/article/21/7/automating-argo-cd) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates automated resource creation setups in Argo CD. Guides administrators in defining dynamic generators to instantiate isolated tenant clusters without human manual action.
#### Industry Insights

  - **(2022)** [thenewstack.io: Why ArgoCD Is the Lifeline of GitOps](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry report outlining why Argo CD became a central standard for cloud-native delivery, highlighting its UI, multi-cluster reach, and powerful declarative configuration matching.
  - **(2021)** [devops.com: The Argo Project: Making GitOps Practical](https://devops.com/the-argo-project-making-gitops-practical)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews the strategic goals of the CNCF Argo ecosystem (CD, Workflows, Rollouts, Events), detailing how unified toolchains implement clean production GitOps architectures.
#### Infrastructure Orchestration

  - **(2022)** [piotrminkowski.com: Manage Kubernetes Cluster with Terraform and Argo CD. Create Kakfa Cluster using GitOps 🌟](https://piotrminkowski.com/2022/06/28/manage-kubernetes-cluster-with-terraform-and-argo-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Detailed guide on using Terraform for primary cloud resources alongside Argo CD for application workloads, presenting a complete hybrid IaC and GitOps blueprint.
#### Multi-Tenancy

  - **(2022)** [blog.argoproj.io: Best Practices for Multi-tenancy in Argo CD](https://blog.argoproj.io/best-practices-for-multi-tenancy-in-argo-cd-273e25a047b0) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Official best practices outlining multi-tenant cluster boundaries in Argo CD, explaining AppProjects configurations to isolate resources and limit cluster access vectors safely.
  - **(2021)** [openshift.com: Getting Started with ApplicationSets](https://www.redhat.com/en/blog/getting-started-with-applicationsets) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Introductory guide to Argo CD ApplicationSets. It demonstrates how to templating multi-cluster deployments, generating child resources programmatically from dynamic Git configurations.
#### Practices

  - **(2021)** [thenewstack.io: Applied GitOps with ArgoCD](https://thenewstack.io/applied-gitops-with-argocd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed operational study of applied GitOps. Discusses directory designs, environment divisions, and secrets management when deploying production containers using Argo CD.
#### Red Hat Ecosystem

  - **(2021)** [openshift.com: OpenShift Authentication Integration with ArgoCD](https://www.redhat.com/en/blog/openshift-authentication-integration-with-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Highlights secure integration of OpenShift OAuth mechanisms with Argo CD. Allows platform engineers to enforce central enterprise identities and granular RBAC profiles directly on the gitops console.
#### Security and Governance

  - **(2023)** [datree.io: ArgoCD Best Practices You Should Know](https://www.datree.io/resources/argocd-best-practices-you-should-know) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Datree's policy-as-code guide for Argo CD configurations. Illustrates automatic linting mechanisms inside development environments to filter out schema violations.
  - **(2021)** [itnext.io: ArgoCD: users, access, and RBAC](https://itnext.io/argocd-users-access-and-rbac-ddf9f8b51bad) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Security implementation guide for Argo CD. Illustrates custom user accounts, SSO hookups, and high-fidelity policy-based RBAC enforcement for large cloud-native engineering groups.
  - **(2021)** [cloud.redhat.com: How to Use ArgoCD Deployments with GitHub Tokens](https://www.redhat.com/en/blog/how-to-use-argocd-deployments-with-github-tokens) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Presents security best practices for token management between GitHub and Argo CD deployments, ensuring repository integrations minimize vector attacks.
#### Tool Evaluation

  - **(2022)** [thenewstack.io: GitOps on Kubernetes: Deciding Between Argo CD and Flux](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A critical analysis of Argo CD versus Flux. Compares Argo CD's visual multi-cluster design against Flux's low-footprint git-reconciling architecture to optimize strategic platform choices.
#### Tutorials

  - **(2022)** [digitalocean.com: How to Deploy to Kubernetes using Argo CD and GitOps](https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An easy-to-follow guide from DigitalOcean explaining the deployment of microservices onto managed Kubernetes environments using Argo CD GitOps models.
  - **(2022)** [kubebyexample.com: Argo CD Overview 🌟](https://kubebyexample.com/learning-paths/argo-cd/argo-cd-overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An educational course from KubeByExample. Explains progressive modules detailing Argo CD setups, manifest synchronizations, and self-healing cluster features.
  - **(2020)** [blog.risingstack.com: Argo CD Kubernetes Tutorial](https://blog.risingstack.com/argo-cd-kubernetes-tutorial) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed step-by-step tutorial introducing Argo CD deployment mechanics. Walks engineers through application creation, manual syncs, and automated reconciliation rules.
  - **(2020)** [blog.getambassador.io: GitOps in Kubernetes with ArgoCD](https://blog.getambassador.io/gitops-in-kubernetes-with-argocd-c6ea0e510741) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details GitOps mechanics using Ambassador Edge Stack for ingress and routing alongside Argo CD, ensuring cluster endpoints synchronize with application status definitions.
#### Video Tutorials

  - **(2021)** [youtube: GitOps with Argo-CD & Kubernetes](https://www.youtube.com/watch?v=QrLwFEXvxbo&ab_channel=HoussemDellai)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured step-by-step video tutorial covering Argo CD installations, git hook linkages, and real-time reconciliation operations for local cloud deployments.
### Event-Driven Automation

#### Argo Ecosystem

  - **(2026)** [==argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework==](https://argoproj.github.io/argo-events) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Argo Events is an enterprise-grade, event-driven workflow automation framework. It triggers scalable Kubernetes actions from diverse external inputs (webhooks, storage, message queues), serving as a crucial modern CI/CD cornerstone.
## GitOps and Continuous Delivery

### GitOps (2)

#### Argo CD (1)

  - **(2025)** [==feat(ui): Add AppSet to Application Resource Tree in Argo CD==](https://github.com/argoproj/argo-cd/pull/26601) <span class='md-tag md-tag--info'>⭐ 22950</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official GitHub pull request introducing ApplicationSet rendering directly inside the Argo CD UI Resource Tree. This highly demanded improvement provides cluster administrators with superior visibility into generated application topologies and dependencies directly from the dashboard.
## Platform Engineering (1)

### Internal Developer Platforms

#### Argo CD (2)

  - **(2023)** [**itnext.io: Build a Lightweight Internal Developer Platform with Argo CD and Kubernetes Labels**](https://itnext.io/build-a-lightweight-internal-developer-platform-with-argo-cd-and-kubernetes-labels-4c0e52c6c0f4) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Proposes an innovative model for constructing a lightweight IDP by utilizing simple Kubernetes label configurations mapped to Argo CD ApplicationSets. Live Grounding: Demonstrates how platform teams can abstract direct Kubernetes complexity for application developers, promoting self-service deployment without security compromises.

---
💡 **Explore Related:** [Registries](./registries.md) | [Jenkins Alternatives](./jenkins-alternatives.md) | [Jenkins](./jenkins.md)

