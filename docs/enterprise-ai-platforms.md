# Enterprise AI Platforms: Cloud AI Control Planes vs Kubernetes

Architectural analysis, decision framework, and curated reference guide for **Public Cloud and Enterprise AI Platforms** (**Microsoft Azure AI Foundry**, **AWS Amazon Bedrock and Bedrock AgentCore**, **Google Cloud Vertex AI and Agent Builder**, **Red Hat OpenShift AI (RHOAI)**, **IBM watsonx**, **Databricks Mosaic AI**, and **Cloudflare Agents Platform**) and their hybrid integration with Kubernetes (**AKS**, **EKS**, **GKE**, and **OpenShift**).

1. [Executive Summary: The 2026 Architectural Shift](#executive-summary-the-2026-architectural-shift)
2. [Architectural Comparison Matrix: Managed Cloud AI vs Hybrid K8s AI vs DIY Kubernetes](#architectural-comparison-matrix-managed-cloud-ai-vs-hybrid-k8s-ai-vs-diy-kubernetes)
3. [Strategic Decision Framework: When Enterprise AI Platforms Beat Kubernetes and When K8s Wins](#strategic-decision-framework-when-enterprise-ai-platforms-beat-kubernetes-and-when-k8s-wins)
4. [Microsoft Azure AI Foundry and AKS Integration](#microsoft-azure-ai-foundry-and-aks-integration)
5. [AWS Amazon Bedrock, AgentCore, and SageMaker on EKS](#aws-amazon-bedrock-agentcore-and-sagemaker-on-eks)
6. [Google Cloud Vertex AI, Agent Builder, and GKE Integration](#google-cloud-vertex-ai-agent-builder-and-gke-integration)
7. [Red Hat OpenShift AI (RHOAI), OpenDataHub, and llm-d](#red-hat-openshift-ai-rhoai-opendatahub-and-llm-d)
8. [Data, Sovereign, and Edge AI Platforms](#data-sovereign-and-edge-ai-platforms)

## Executive Summary: The 2026 Architectural Shift

!!! info "Architectural Paradigm Shift: The Managed Agentic Control Plane (2026)"
    Between 2023 and 2024, running enterprise AI on Kubernetes meant assembling a complex **DIY Kubernetes AI Stack** from scratch (installing NVIDIA GPU Operator, KubeRay, Kubeflow, KServe, vLLM, vector databases, LangChain/LangGraph containers, custom Redis state stores, and OpenTelemetry collectors).

    In 2025–2026, public cloud hyperscalers and enterprise Kubernetes platform vendors introduced a major new architectural layer — **Unified Enterprise AI and Agentic Platforms**:

    - **Microsoft Azure**: [Microsoft Azure AI Foundry](https://ai.azure.com) (*Microsoft Foundry*) + [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) + [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) + [KAITO](https://github.com/kaito-project/kaito)
    - **AWS**: [Amazon Bedrock](https://aws.amazon.com/bedrock) + [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore) + [Strands Agents SDK](https://github.com/strands-agents/harness-sdk) + [Amazon SageMaker AI (HyperPod on EKS)](https://aws.amazon.com/sagemaker/ai/)
    - **Google Cloud**: [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) + [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) + [Google Agent Development Kit (ADK)](https://github.com/google/adk-python)
    - **Red Hat and OpenShift**: [Red Hat OpenShift AI (RHOAI)](https://www.redhat.com/en/products/ai/openshift-ai) + [OpenDataHub Operator](https://github.com/opendatahub-io/opendatahub-operator) + [llm-d](https://github.com/llm-d/llm-d) + [InstructLab](https://github.com/instructlab/instructlab)
    - **Data and Edge Clouds**: [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence), [IBM watsonx](https://www.ibm.com/products/watsonx), and [Cloudflare Agents Platform](https://developers.cloudflare.com/agents)

    Unlike first-generation ML platforms, these platforms natively solve the **five hardest production challenges of GenAI and multi-agent systems** at the control-plane layer:

    1.  **Stateful Agent Execution and Memory Persistence**: Managed durable conversation threads, episodic/long-term memory, and isolated execution sandboxes (e.g., MicroVM-isolated 8-hour agent sessions and code interpreters in Bedrock AgentCore and Foundry Agent Service) without building custom Kubernetes stateful orchestration.
    2.  **Native MCP (Model Context Protocol) and A2A (Agent2Agent) Gateways**: Managed protocol gateways that turn existing enterprise REST/OpenAPI services, databases, and serverless functions into authenticated **MCP tool servers** and enable cross-platform multi-agent collaboration (**A2A**).
    3.  **Enterprise Identity and Zero-Trust Agent Security**: First-class cloud identities for autonomous agents (**Microsoft Entra Agent ID**, **AWS IAM Identity Center for AgentCore**, **GCP IAM**) with automatic document-level RBAC enforced during RAG retrieval (**Azure AI Search / Foundry IQ**, **Bedrock Knowledge Bases**, **Vertex AI Search**).
    4.  **Serverless Multi-Provider Model Routing and Guardrails**: Unified API gateways providing instant access to 200+ frontier and open-weight models with built-in PII redaction, prompt-injection shields, hallucination grounding checks, and continuous evaluation pipelines.
    5.  **Zero Idle GPU Tax**: Pay-per-token model endpoints and pay-per-second serverless agent runtimes eliminate the cost of underutilized H100/B200 GPU nodes sitting idle in Kubernetes clusters during off-peak hours.

## Architectural Comparison Matrix: Managed Cloud AI vs Hybrid K8s AI vs DIY Kubernetes

| Architectural Dimension | Managed Public Cloud AI Platforms (Azure AI Foundry, Bedrock AgentCore, Vertex AI) | Hybrid Turnkey K8s AI Platforms (Red Hat OpenShift AI, KAITO, SageMaker HyperPod) | Standard DIY Kubernetes AI Stack (Self-managed KServe + vLLM + KubeRay + Kubeflow) |
| :--- | :--- | :--- | :--- |
| **Time to Production** | **Days** (managed model catalog, RAG, agent state, and guardrails out-of-the-box) | **1–2 Weeks** (operator-managed pre-validated stack on OpenShift, AKS, or EKS) | **3–6 Months** (manual integration of 10+ CNCF/open-source operators and CRDs) |
| **Operational Overhead (Day-2 SRE)** | **Near Zero** (cloud provider manages GPU drivers, model scaling, and runtime patching) | **Low–Medium** (automated via OpenDataHub, RHOAI, and KAITO operators) | **Very High** (CUDA/driver upgrades, KV-cache tuning, Kueue/Ray upgrades, CRD drift) |
| **Agent State, Memory and MCP Tooling** | **Built-in Managed Service** (Foundry Agent Service, Bedrock AgentCore, Vertex Agent Engine) | **Framework-based** (Llama Stack, Microsoft Agent Framework, LangGraph on K8s) | **100% Custom Build** (self-hosted Redis/Postgres state + custom MCP sidecars) |
| **Cost Profile (FinOps)** | **Best for Variable and Spiky Traffic** (pay-per-token or pay-per-second; zero idle GPU waste) | **Best for Sustained Enterprise Baselines** (predictable cluster licensing + auto-provisioned GPUs) | **Best Only at Massive 24/7 Utilization** (>70% continuous GPU saturation with dedicated SREs) |
| **Enterprise Governance and IAM** | **Turnkey** (Entra Agent ID, AWS IAM, built-in content safety, EU AI Act audit logs) | **Strong** (OpenShift RBAC, TrustyAI, Kueue multi-tenant quotas) | **Fragmented** (requires stitching OPA/Kyverno, Istio, and custom auth proxies) |
| **Data Sovereignty and Air-Gapped Portability** | **Cloud-Bound** (tied to public cloud regions, though SDKs like ADK and Strands are portable) | **100% Portable and Air-Gap Ready** (runs on-prem, bare-metal, sovereign clouds, or public cloud) | **100% Portable** (zero vendor lock-in; runs on any CNCF-conformant Kubernetes cluster) |
| **Hardware and Kernel-Level Control** | **Abstracted** (limited control over custom CUDA kernels, MIG slicing, or disaggregated KV cache) | **High** (`llm-d` disaggregated prefill/decode, NVIDIA GPU Operator, DRA, RoCE/InfiniBand) | **Total Control** (custom schedulers, custom vLLM builds, custom kernel/eBPF tuning) |

## Strategic Decision Framework: When Enterprise AI Platforms Beat Kubernetes and When K8s Wins

!!! success "The 2026 Enterprise Decision Framework"
    1.  **For 80–90% of Enterprise GenAI, RAG, and Agentic Applications — Managed Enterprise AI Platforms are a significantly superior alternative to DIY Kubernetes**:
        If your goal is to build, govern, and scale autonomous AI agents, enterprise RAG copilots, and multi-model workflows using frontier or standard open-weight models, assembling a raw Kubernetes AI stack from scratch is now an engineering anti-pattern (*undifferentiated heavy lifting*). **Microsoft Azure AI Foundry**, **Amazon Bedrock AgentCore**, and **Google Cloud Vertex AI Agent Builder** deliver faster time-to-market, native enterprise IAM/RBAC, built-in MCP/A2A interoperability, automated evaluation guardrails, and lower Total Cost of Ownership (TCO) for variable workloads.
    2.  **When Kubernetes-Native AI Platforms Remain Superior (The 10–20% High-Control and Sovereign Tier)**:
        - **Data Sovereignty, Regulatory Compliance, and Disconnected/Air-Gapped Environments**: Financial, defense, healthcare, and sovereign workloads that cannot send weights or prompts to multi-tenant public cloud APIs. Here, **Red Hat OpenShift AI (RHOAI)** and **IBM watsonx** provide the exact same turnkey platform experience (model registry, vLLM/`llm-d` serving, agent frameworks, governance) natively on Kubernetes.
        - **Sustained 24/7 High-Volume Open-Weight Inference**: Once token volume crosses a high sustained threshold where per-token API fees exceed dedicated GPU reservation costs, serving open-weight models (Llama, DeepSeek, Qwen, Mistral, Granite) on Kubernetes using **`llm-d`**, **vLLM**, **KServe**, and **KAITO** with the **Kubernetes Gateway API Inference Extension** reduces unit inference costs by **40–70%**.
        - **Massive Distributed Training and Custom Fine-Tuning**: Multi-node pre-training, RLHF/DPO, or custom CUDA kernel workloads across hundreds of GPUs/TPUs require **KubeRay**, **Kueue**, **Volcano**, or **Amazon SageMaker HyperPod on EKS**.
    3.  **The 2026 Hybrid Reference Architecture (Cloud AI Control Plane + Kubernetes Execution Plane)**:
        Every major cloud provider now converges its Managed AI Platform with Kubernetes rather than treating them as mutually exclusive silos:
        - **Microsoft Azure**: Models and agents governed in **Azure AI Foundry** deploy seamlessly onto **AKS** via **KAITO** (CNCF Sandbox) and the open-source **Microsoft Agent Framework**.
        - **AWS**: Agents built with **Strands Agents SDK** run portably across **Amazon Bedrock AgentCore** and **Amazon EKS**, while **SageMaker HyperPod** and **AI on EKS** use EKS directly as their distributed GPU orchestrator.
        - **Google Cloud**: Agents engineered with **Google ADK** deploy with a single command to either **Vertex AI Agent Engine** or **GKE**, while **`llm-d`** brings disaggregated vLLM inference natively to GKE.
        - **Red Hat OpenShift**: **Red Hat OpenShift AI (RHOAI)** and **`llm-d`** unify the entire open-source AI stack into an enterprise-supported platform across any on-premises or hybrid OpenShift Kubernetes cluster.

## Microsoft Azure AI Foundry and AKS Integration

- **(2026)** [Microsoft Azure AI Foundry](https://ai.azure.com) 🌟 - Microsoft's unified enterprise AI application and agent factory combining the Foundry Model Catalog (serverless MaaS and Managed Compute), Azure AI Agent Service, Prompt Flow, evaluation guardrails, and native integration with AKS and Azure Container Apps.
- **(2026)** [Azure AI Foundry Architecture and Documentation](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) 🌟 - Official architectural documentation for Microsoft Foundry, covering hub-and-project governance, Entra Agent ID, Foundry IQ enterprise RAG via Azure AI Search, and hybrid deployment to Kubernetes.
- **(2026)** [Azure AI Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) 🌟 - Fully managed stateful agent runtime in Azure AI Foundry supporting multi-agent orchestration, OpenAPI/MCP tool calling, code interpreter sandboxes, and enterprise grounding with Azure AI Search and Bing.
- **(2026)** [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) 🌟 - Open-source framework (unifying Semantic Kernel and AutoGen) for building, orchestrating, and deploying single- and multi-agent workflows in Python and .NET with native Azure AI Foundry and OpenTelemetry integration.
- **(2026)** [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) 🌟 - Comprehensive 18-lesson curriculum and reference code from Microsoft covering agentic design patterns, tool use, MCP integration, and production deployment on Azure AI Foundry.
- **(2026)** [Azure AI Foundry Agent Service Starter Samples](https://github.com/Azure-Samples/get-started-with-ai-agents) 🌟 - Production-ready starter templates for deploying AI agent web applications using Azure AI Foundry SDKs, Bicep/Terraform IaC, and Azure Developer CLI (`azd`).
- **(2026)** [Azure Search OpenAI Enterprise RAG Demo](https://github.com/Azure-Samples/azure-search-openai-demo) 🌟 - Flagship Microsoft reference architecture for enterprise Retrieval-Augmented Generation (RAG) using Azure AI Foundry, Azure OpenAI, and Azure AI Search with document-level RBAC.
- **(2026)** [KAITO: Kubernetes AI Toolchain Operator](https://github.com/kaito-project/kaito) 🌟 - CNCF Sandbox operator (originated by Microsoft Azure) that automates open-weight LLM inference, fine-tuning, and GPU node provisioning on AKS and upstream Kubernetes.

## AWS Amazon Bedrock, AgentCore, and SageMaker on EKS

- **(2026)** [Amazon Bedrock](https://aws.amazon.com/bedrock) 🌟 - AWS's fully managed serverless platform for foundation models, enterprise RAG Knowledge Bases, Guardrails, and multi-agent collaboration without managing underlying GPU infrastructure.
- **(2026)** [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore) 🌟 - Managed serverless agent runtime on AWS providing persistent session microVMs, built-in memory, identity, code interpreter sandboxes, and native Model Context Protocol (MCP) tool hosting.
- **(2026)** [Strands Agents SDK](https://github.com/strands-agents/harness-sdk) 🌟 - AWS open-source model-driven agent harness and SDK for building production AI agents in Python and TypeScript across Amazon Bedrock, AgentCore, and Kubernetes (EKS).
- **(2026)** [Amazon SageMaker AI (HyperPod on EKS)](https://aws.amazon.com/sagemaker/ai/) 🌟 - Unified AWS ML and GenAI platform featuring SageMaker HyperPod on Amazon EKS for resilient multi-node distributed LLM training, automated node recovery, and governed model deployment.
- **(2026)** [AI on EKS (awslabs/ai-on-eks)](https://github.com/awslabs/ai-on-eks) 🌟 - Official AWS Labs Terraform/Helm blueprints for running high-scale generative AI, vLLM, Ray, KServe, and GPU inference workloads on Amazon EKS alongside Amazon Bedrock.
- **(2026)** [Amazon Bedrock Official Samples](https://github.com/aws-samples/amazon-bedrock-samples) 🌟 - Official AWS reference implementations for Amazon Bedrock covering foundation model inference, Knowledge Bases, Guardrails, and enterprise GenAI architectures.
- **(2026)** [Amazon Bedrock Agent Samples](https://github.com/awslabs/amazon-bedrock-agent-samples) 🌟 - Curated blueprints and notebooks from AWS Labs demonstrating multi-agent orchestration, tool invocation, and production workflows with Amazon Bedrock Agents.

## Google Cloud Vertex AI, Agent Builder, and GKE Integration

- **(2026)** [Google Cloud Vertex AI Platform](https://cloud.google.com/vertex-ai) 🌟 - Google Cloud's unified enterprise AI platform providing access to 200+ foundation models in Model Garden (Gemini, Claude, Llama, DeepSeek), Ray on Vertex AI, and end-to-end MLOps.
- **(2026)** [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) 🌟 - Managed enterprise platform on Google Cloud for building, grounding, and orchestrating multi-agent systems with Vertex AI Agent Engine, native MCP/A2A protocols, and Google Search/Enterprise data grounding.
- **(2026)** [Google Cloud Vertex AI and Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) 🌟 - Google Cloud's unified enterprise AI platform featuring Model Garden, Vertex AI Agent Builder, managed Agent Engine runtime, Grounding with Google Search, and seamless portability to GKE.
- **(2026)** [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) 🌟 - Google's open-source, code-first Python toolkit for building, evaluating, and deploying deterministic and dynamic multi-agent systems natively on Vertex AI Agent Engine or Kubernetes (GKE).
- **(2026)** [Google Cloud Generative AI Samples](https://github.com/GoogleCloudPlatform/generative-ai) 🌟 - Official repository of production notebooks, sample apps, and reference architectures for Gemini and Vertex AI on Google Cloud.
- **(2026)** [Vertex AI Code Samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples) 🌟 - Official Google Cloud sample notebooks and pipelines for Vertex AI custom training, Model Garden serving, and MLOps automation.

## Red Hat OpenShift AI (RHOAI), OpenDataHub, and llm-d

- **(2026)** [Red Hat OpenShift AI (RHOAI)](https://www.redhat.com/en/products/ai/openshift-ai) 🌟 - Enterprise Kubernetes-native AI and MLOps platform built on Red Hat OpenShift, integrating vLLM, KServe, Kubeflow, Ray, Kueue, and InstructLab for hybrid cloud and disconnected on-premise GPU deployments.
- **(2026)** [Red Hat OpenShift AI Official Documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed) 🌟 - Complete architectural and operations documentation for deploying and managing Red Hat OpenShift AI across self-managed OpenShift and hybrid cloud environments.
- **(2026)** [Open Data Hub Operator](https://github.com/opendatahub-io/opendatahub-operator) 🌟 - Upstream Kubernetes operator powering Red Hat OpenShift AI, orchestrating the full lifecycle of model serving, distributed training, and data science pipelines on OpenShift.
- **(2026)** [llm-d: Kubernetes-Native Distributed LLM Inference](https://github.com/llm-d/llm-d) 🌟 - Open-source distributed inference framework (co-created by Red Hat, Google, IBM, and CoreWeave) leveraging vLLM, KV-cache-aware routing, and disaggregated prefill/decode on Kubernetes.
- **(2026)** [InstructLab](https://github.com/instructlab/instructlab) 🌟 - Open-source LLM alignment and synthetic-data taxonomy project (created by Red Hat and IBM Research) integrated into RHEL AI and OpenShift AI for efficient domain-specific model tuning.
- **(2026)** [KServe](https://github.com/kserve/kserve) 🌟 - CNCF Incubation standardized serverless ML and generative AI inference platform on Kubernetes supporting vLLM, Triton, HuggingFace, autoscaling, and OpenAI-compatible Generative AI gateways.
- **(2026)** [Kubernetes Kueue](https://github.com/kubernetes-sigs/kueue) 🌟 - Kubernetes-native job queueing controller for batch, AI/ML training, and multi-tenant GPU quota management with fair-sharing, preemption, and topology-aware scheduling.

## Data, Sovereign, and Edge AI Platforms

- **(2026)** [IBM watsonx](https://www.ibm.com/products/watsonx) 🌟 - Enterprise AI and data platform (`watsonx.ai`, `watsonx.data`, `watsonx.governance`) architected on Red Hat OpenShift for regulated hybrid-cloud AI workloads and model compliance.
- **(2026)** [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence) 🌟 - Unified Data Intelligence platform for building, evaluating, and governing enterprise AI agents, RAG vector indexes, and fine-tuned models directly alongside Lakehouse data with MLflow 3.0.
- **(2026)** [Cloudflare Agents Platform](https://developers.cloudflare.com/agents) 🌟 - Serverless edge-native platform for deploying stateful, durable AI agents using Cloudflare Workers, Durable Objects, Workers AI, and AI Gateway.

---
*See also: [AI Agents and Model Context Protocol (MCP)](ai-agents-mcp.md), [MLOps](mlops.md), [Microsoft Azure](azure.md), [Amazon Web Services (AWS)](aws.md), [Google Cloud Platform (GCP)](GoogleCloudPlatform.md), and [Red Hat OpenShift](openshift.md).*
