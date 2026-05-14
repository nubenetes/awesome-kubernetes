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
  - [Google's Official Skills Repository for AI Agents](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository) 🌟 - Google lanza un repositorio oficial de 'skills' para agentes de IA, utilizando el Model Context Protocol (MCP) para mejorar la eficiencia y reducir el 'context bloat' al interactuar con tecnologías como GKE.
  - [Google Agents CLI: Herramientas para crear y desplegar agentes de IA en Google Cloud](https://github.com/google/agents-cli) 🌟 - El CLI y las habilidades que convierten a cualquier asistente de codificación en un experto en la creación, evaluación y despliegue de agentes de IA en Google Cloud.
  - [Announcing Azure MCP Server 2.0 Stable Release](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) 🌟 - Microsoft anuncia el lanzamiento estable de Azure MCP Server 2.0, que implementa el protocolo MCP para la automatización de flujos de trabajo agentic en Azure, destacando el soporte para servidores MCP auto-alojados.
  - [AZVerify: Conecta diagramas, Bicep y Azure con GitHub Copilot](https://github.com/Azure/AZVerify) 🌟 - AZVerify dota a GitHub Copilot de habilidades para conectar tu diagrama de Azure, plantillas Bicep y entorno en vivo, mitigando la deriva entre fuentes de verdad.
  - [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) - Un repositorio de GitHub que explora las mejores prácticas para codificar con Claude, transitando desde la codificación de vibración hasta la ingeniería agéntica.
  - [Draw.io MCP para Generación de Diagramas](https://thomasthornton.cloud/draw-io-mcp-for-diagram-generation-why-its-worth-using/) 🌟 - Este artículo explora cómo Draw.io MCP puede automatizar la generación de diagramas a partir de datos estructurados, integrándose con flujos de trabajo de ingeniería y herramientas de IA para mantener las arquitecturas como activos vivos.
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