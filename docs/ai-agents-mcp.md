# AI Agents and Model Context Protocol (MCP) for Kubernetes

Resources, tools, and projects related to autonomous AI agents, Model Context Protocol (MCP) implementations, and LLM orchestration within Kubernetes environments.

1. [Introduction](#introduction)
2. [AI Agents](#ai-agents)
3. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
4. [LLM Operators and Infrastructure](#llm-operators-and-infrastructure)

## Introduction
  - [Cursor AI Fundamentals Course](https://cursor.com/es/learn) - *(Related to ai topic)*

- [anthropic.com: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [modelcontextprotocol.io: MCP Official Documentation](https://modelcontextprotocol.io/docs/getting-started/intro)

## AI Agents
  - [IBM IAM for AI Agents](https://t.co/EKsVgKA4xn) - This resource discusses how IBM Identity and Access Management (IAM) provides native IAM for AI agents, enabling them to have an identity and deliver least privileged access.
  - [Level Up Your Agents: Announcing Google's Official Skills Repository](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository) 🌟 - This blog post announces the launch of Google's official Agent Skills repository on GitHub, designed to equip AI agents with condensed expertise on specific technologies and tasks. Skills are presented in an open Markdown format, including reference files and code snippets, to provide agent-first documentation. This approach aims to reduce 'context bloat' often encountered when using Model Context Protocol (MCP) servers, leading to more efficient and cost-effective AI agent interactions with Google Cloud products like Gemini API, BigQuery, and GKE.
  - [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) - A GitHub repository focused on 'vibe coding to agentic engineering', providing practices and examples for interacting with AI models like Claude. It includes sections on agents, commands, skills, development workflows, and implementation details.
  - [Kiro: Engineering Rigor for Agentic Development](https://kiro.dev) - Kiro is a tool designed to bring engineering discipline to AI agent development. It focuses on managing intent, handling long-running tasks across large codebases, and validating code correctness through a learning agent. Key features include converting natural language prompts into structured requirements (EARS notation), generating architectural designs, creating implementation plans with discrete, sequenced tasks, and enabling terminal-based interaction for building features, automating workflows, and debugging.
- [HolmesGPT (Robusta)](https://github.com/HolmesGPT/holmesgpt) - An open-source AI agent for investigating Prometheus alerts and Kubernetes incidents. It uses LLMs to triage issues and provide recommended fixes.
- [Skyvern](https://github.com/Skyvern-ai/Skyvern) - Automate browser-based workflows using LLMs and Computer Vision.

## Model Context Protocol (MCP)
  - [Announcing Azure MCP Server 2.0 Stable Release for Self-Hosted Agentic Cloud Automation](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release) 🌟 - This blog post announces the stable release of Azure MCP Server 2.0, an open-source software that implements the Model Context Protocol (MCP) specification. It allows AI agents and developer tools to interact with Azure resources through a standardized tool interface. The key advancement in version 2.0 is the support for self-hosted, remote MCP server deployment, enabling flexible integration into developer workflows for local development, tool integrations, and centralized team/enterprise scenarios with consistent policy and security controls.
  - [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - A curated list of resources related to MCP (Machine Cognitive Progression) servers, focusing on AI and related technologies.
- [PulseMCP](https://pulsemcp.com) - A hosted hub for discovering and using MCP servers.
- [MCPBundles](https://www.mcpbundles.com) - Curated bundles of MCP servers for various use cases (DevOps, Data, Productivity).
- [GitHub MCP Server](https://github.com/modelcontextprotocol/servers) - Interact with GitHub repositories, issues, and PRs via AI agents.
- [Vercel MCP Server](https://github.com/modelcontextprotocol/servers) - Manage Vercel deployments and view logs directly from AI agents.
- [Chroma MCP Server](https://github.com/modelcontextprotocol/servers) - Vector database integration for agentic RAG.
- [Brave Search MCP](https://github.com/modelcontextprotocol/servers) - Grounded web search for AI agents.
- [PostgreSQL MCP Server](https://github.com/modelcontextprotocol/servers) - Secure SQL execution and schema inspection for agents.
- [Google Cloud Managed MCP](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-managed-mcp-for-gemini) - Production-grade MCP service for accessing GCP resources from Gemini.

## LLM Operators and Infrastructure
- [Kube-Ray](https://github.com/ray-project/kuberay) - A toolkit to run Ray applications on Kubernetes.
- [vLLM on Kubernetes](https://github.com/vllm-project/vllm) - High-throughput LLM serving with PagedAttention.
- [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator) - Automates the management of all NVIDIA software components needed to provision GPU.
- [LocalAI](https://github.com/mudler/LocalAI) - Self-hosted, community-driven, local OpenAI-compatible API.