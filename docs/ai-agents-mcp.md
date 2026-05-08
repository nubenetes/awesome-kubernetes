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
- [HolmesGPT (Robusta)](https://github.com/robusta-dev/holmesgpt) - An open-source AI agent for investigating Prometheus alerts and Kubernetes incidents. It uses LLMs to triage issues and provide recommended fixes.
- [Agentic Alert Investigation with HolmesGPT and Robusta](https://robusta.dev/blog/holmesgpt-agentic-alert-investigation)
- [Skyvern](https://github.com/Skyvern-ai/Skyvern) - Automate browser-based workflows using LLMs and Computer Vision.

## Model Context Protocol (MCP)
- [PulseMCP](https://pulsemcp.com/) - A hosted hub for discovering and using MCP servers.
- [MCPBundles](https://mcpbundles.com/) - Curated bundles of MCP servers for various use cases (DevOps, Data, Productivity).
- [GitHub MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - Interact with GitHub repositories, issues, and PRs via AI agents.
- [Vercel MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/vercel) - Manage Vercel deployments and view logs directly from AI agents.
- [Chroma MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/chroma) - Vector database integration for agentic RAG.
- [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Grounded web search for AI agents.
- [PostgreSQL MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - Secure SQL execution and schema inspection for agents.
- [Google Cloud Managed MCP](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-managed-mcp-for-gemini) - Production-grade MCP service for accessing GCP resources from Gemini.

## LLM Operators and Infrastructure
- [Kube-Ray](https://github.com/ray-project/kuberay) - A toolkit to run Ray applications on Kubernetes.
- [vLLM on Kubernetes](https://github.com/vllm-project/vllm) - High-throughput LLM serving with PagedAttention.
- [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator) - Automates the management of all NVIDIA software components needed to provision GPU.
- [LocalAI](https://github.com/go-skynet/LocalAI) - Self-hosted, community-driven, local OpenAI-compatible API.
