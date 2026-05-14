# AI Agents and Model Context Protocol (MCP) for Kubernetes

Resources, tools, and projects related to autonomous AI agents, Model Context Protocol (MCP) implementations, and LLM orchestration within Kubernetes environments.

1. [Introduction](#introduction)
2. [AI Agents](#ai-agents)
3. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
4. [LLM Operators and Infrastructure](#llm-operators-and-infrastructure)

## Introduction

- [anthropic.com: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [modelcontextprotocol.io: MCP Official Documentation](https://modelcontextprotocol.io/introduction)

## AI Agents
  - [Skills for Real Engineers](https://github.com/mattpocock/skills) - *(Related to ai topic)*
  - [Level Up Your Agents: Announcing Google's Official Skills Repository](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository) 🌟 - This blog post announces the launch of Google's official Agent Skills repository, hosted on GitHub. Agent Skills are designed to provide AI models with condensed expertise in specific technologies or tasks, written in a simple, open Markdown format. This approach helps reduce 'context bloat' in AI agents by loading information only as needed, contrasting with the direct use of Model Context Protocol (MCP) servers. The initial repository includes thirteen skills focused on Google Cloud technologies such as AlloyDB, BigQuery, Cloud Run, Cloud SQL, Firebase, Gemini API, and Google Kubernetes Engine (GKE), as well as skills related to the Well-Architected Pillars (Security, Reliability, Cost Optimization) and onboarding recipes.
  - [Google Agents CLI for Building and Deploying AI Agents on Google Cloud](https://github.com/google/agents-cli) 🌟 - The `agents-cli` project provides a command-line interface and a set of skills designed to empower coding assistants (like Gemini, Claude Code, Codex) to create, evaluate, and deploy AI agents on Google Cloud. It aims to simplify the process of building enterprise-grade agents by providing the necessary commands and integrating with Google Cloud services.
  - [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) - *(Related to ai topic)*
- [HolmesGPT (Robusta)](https://github.com/robusta-dev/holmesgpt) - An open-source AI agent for investigating Prometheus alerts and Kubernetes incidents. It uses LLMs to triage issues and provide recommended fixes.
- [Skyvern](https://github.com/Skyvern-ai/Skyvern) - Automate browser-based workflows using LLMs and Computer Vision.

## Model Context Protocol (MCP)
- [PulseMCP](https://pulsemcp.com/) - A hosted hub for discovering and using MCP servers.
- [MCPBundles](https://mcpbundles.com/) - Curated bundles of MCP servers for various use cases (DevOps, Data, Productivity).
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
- [LocalAI](https://github.com/go-skynet/LocalAI) - Self-hosted, community-driven, local OpenAI-compatible API.