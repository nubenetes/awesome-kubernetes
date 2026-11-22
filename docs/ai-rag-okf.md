# AI Knowledge and Retrieval: RAG, OKF, GraphRAG and Agent Memory

Architectural analysis, decision framework, and curated 2026 reference hub for **AI Knowledge Representation and Retrieval** — spanning **Retrieval-Augmented Generation (RAG)**, Google Cloud's **Open Knowledge Format (OKF)** and **LLM Wikis**, **Vectorless Reasoning Retrieval (PageIndex)**, **Cache-Augmented Generation (CAG)**, **GraphRAG and Knowledge Graphs**, **Contextual Retrieval**, and **Persistent Agent Memory** (**Mem0**, **Graphiti**, **Letta**, **Cognee**).

1. [Executive Summary: Beyond Naive Vector RAG](#executive-summary-beyond-naive-vector-rag)
2. [Architectural Comparison Matrix: RAG vs OKF vs GraphRAG vs Vectorless vs CAG vs Agent Memory](#architectural-comparison-matrix-rag-vs-okf-vs-graphrag-vs-vectorless-vs-cag-vs-agent-memory)
3. [The 2026 Hybrid Knowledge Stack Decision Framework](#the-2026-hybrid-knowledge-stack-decision-framework)
4. [Open Knowledge Format (OKF) and LLM Wikis](#open-knowledge-format-okf-and-llm-wikis)
5. [Vectorless Reasoning RAG and Cache-Augmented Generation (CAG)](#vectorless-reasoning-rag-and-cache-augmented-generation-cag)
6. [GraphRAG and Hybrid Knowledge Graphs](#graphrag-and-hybrid-knowledge-graphs)
7. [Modern RAG, Contextual Retrieval and Deep Document Parsing](#modern-rag-contextual-retrieval-and-deep-document-parsing)
8. [Persistent Agent Memory Systems](#persistent-agent-memory-systems)
9. [Vector Databases, Hybrid Search and RAG Evaluation](#vector-databases-hybrid-search-and-rag-evaluation)

## Executive Summary: Beyond Naive Vector RAG

!!! info "The 2026 Paradigm Shift: From Chunk-and-Embed to Layered Knowledge Engineering"
    First-generation enterprise AI relied almost exclusively on **naive Vector RAG**: splitting unstructured PDFs and wikis into fixed-size chunks, embedding them into a vector database, and injecting top-K nearest neighbors into prompts. In production, naive vector RAG frequently fails on **canonical truth vs semantic similarity** (retrieving outdated policies that sound similar to the query), **context fragmentation** (losing table schemas, hierarchies, and cross-references), and **multi-hop reasoning**.

    In 2026, production AI architectures treat knowledge retrieval as a **multi-layered stack** combining deterministic formats, reasoning indexes, graph traversal, prompt caching, and hybrid search:

    - **Open Knowledge Format (OKF) and LLM Wikis**: Vendor-neutral, Git-versioned bundles of Markdown + YAML frontmatter + explicit hyperlinks (spearheaded by Google Cloud and Karpathy's LLM Wiki pattern) that give AI agents deterministic, auditable access to canonical schemas, metrics, and runbooks without vector databases.
    - **Vectorless Reasoning RAG (PageIndex)**: Hierarchical semantic tree indexes navigated directly by LLM reasoning rather than cosine similarity, excelling on dense regulatory, legal, and financial documents.
    - **Cache-Augmented Generation (CAG)**: Preloading bounded, high-value corpora directly into long-context KV caches to eliminate retrieval latency and retrieval errors altogether.
    - **GraphRAG and LightRAG**: Entity-relationship knowledge graphs enabling global synthesis and multi-hop reasoning across disconnected enterprise silos.
    - **Contextual Retrieval and Deep Document RAG**: Prepending document-level context before embedding/BM25 indexing (Anthropic Contextual Retrieval) and layout-aware document parsing (RAGFlow, LlamaIndex, Haystack).
    - **Persistent Agent Memory**: Dynamic, bi-temporal, self-editing memory layers (**Mem0**, **Zep Graphiti**, **Letta**, **Cognee**) that track changing facts and preferences across sessions.

## Architectural Comparison Matrix: RAG vs OKF vs GraphRAG vs Vectorless vs CAG vs Agent Memory

| Paradigm | Core Mechanism | Storage Backend | Best-Fit Workloads | Primary Trade-Off |
| :--- | :--- | :--- | :--- | :--- |
| **Open Knowledge Format (OKF)** | Deterministic navigation of Markdown + YAML frontmatter (`type`, provenance, trust, freshness) + relative links | Git repositories / plain files | High-trust canonical knowledge: schemas, KPI definitions, runbooks, architecture rules | Requires human or AI-assisted wiki curation; not suited for millions of raw unstructured logs |
| **Traditional / Hybrid Vector RAG** | Chunking + Dense Embeddings + BM25 Hybrid Search + Reranking (Contextual Retrieval) | Vector DBs (`Qdrant`, `Weaviate`, `Milvus`, `pgvector`) | Massive, fast-moving, unstructured corpora (support tickets, docs, knowledge bases) | Susceptible to semantic drift, chunk boundary loss, and continuous re-indexing overhead |
| **GraphRAG and LightRAG** | LLM entity/relation extraction + graph community summaries + dual-level traversal | Graph DB (`Neo4j`) or hybrid graph-vector stores | Multi-hop relational queries and global thematic synthesis across large corpora | Higher upfront indexing compute and LLM extraction cost (mitigated by LightRAG) |
| **Vectorless Tree RAG (PageIndex)** | Hierarchical Table-of-Contents tree built over documents + iterative LLM reasoning search | Tree JSON / document store (no vector DB) | Dense structured documents (10-K filings, legal contracts, technical specs) | Higher per-query reasoning latency than sub-50ms ANN vector lookups |
| **Cache-Augmented Generation (CAG)** | Preload full bounded corpus into LLM long-context window and reuse KV / Prompt Cache | Model KV Cache / Prompt Cache | Bounded, stable reference corpora fitting within context limits (<200K–1M tokens) | Bounded by model context window and cache TTL/storage cost |
| **Persistent Agent Memory** | Fact extraction, bi-temporal validity windows, and agent self-edited memory blocks | Temporal graph / hybrid store (`Mem0`, `Graphiti`, `Letta`) | Long-running personalized assistants and stateful multi-session enterprise agents | Needs explicit conflict resolution, privacy governance, and retention policies |

## The 2026 Hybrid Knowledge Stack Decision Framework

!!! success "How Senior AI Architects Combine OKF, RAG, GraphRAG and Memory"
    1. **Layer 1 — Canonical Brain (OKF in Git)**: Store authoritative schemas, business rules, compliance policies, and SRE runbooks as **OKF bundles** versioned in Git with explicit YAML `trust`, `provenance`, and `freshness` signals. Agents traverse `index.md` deterministically with zero vector ambiguity.
    2. **Layer 2 — Bounded Static Context (CAG / Prompt Caching)**: When a reference manual or codebase subset fits cleanly inside the model's prompt cache, skip retrieval pipelines entirely and use **CAG** for zero retrieval error and low TTFT.
    3. **Layer 3 — Long-Tail Unstructured Search (Contextual Hybrid RAG / Vectorless Tree RAG)**: Use **Contextual Retrieval** (hybrid dense + BM25 + reranker) for high-volume unstructured archives, or **PageIndex** when exact hierarchical precision on dense PDFs outweighs sub-50ms latency.
    4. **Layer 4 — Multi-Hop and Temporal State (GraphRAG + Agent Memory)**: Layer **LightRAG / GraphRAG** for cross-document relational synthesis and **Graphiti / Mem0 / Letta** for stateful, time-aware agent memory across conversations.
    5. **Layer 5 — Live Operational Truth (MCP Tool Retrieval)**: Never embed rapidly changing operational state (cluster pod health, live SQL metrics, ticket statuses); fetch live ground truth on demand via **Model Context Protocol (MCP)** servers.

## Open Knowledge Format (OKF) and LLM Wikis

- **(2026)** [Open Knowledge Format (OKF) Official Portal](https://okf.md) 🌟 - Official portal for the Open Knowledge Format (OKF), the Apache 2.0 vendor-neutral specification turning Git-versioned Markdown files with YAML frontmatter and hyperlinks into deterministic, auditable AI agent knowledge bundles.
- **(2026)** [GitHub: open-knowledge-format/open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format) 🌟 - Official vendor-neutral specification (`SPEC.md`), conformance rules, reference bundles, and tooling for OKF (migrated from `GoogleCloudPlatform/open-knowledge-format`).
- **(2026)** [Google Cloud: How the Open Knowledge Format Can Improve Data Sharing (OKF v0.1)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) 🌟 - Launch announcement from Google Cloud Data Cloud introducing OKF to formalize the LLM-wiki pattern and solve enterprise context assembly without proprietary vector lock-in.
- **(2026)** [Google Cloud: OKF v0.2 Adds Trust Signals](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals) 🌟 - Architectural deep dive into OKF v0.2's five opt-in frontmatter trust primitives — provenance, trust, freshness, lifecycle, and attestation — enabling accountable AI-authored knowledge bases at scale.
- **(2026)** [Google Cloud: Introducing OKF v0.3](https://cloud.google.com/blog/products/data-analytics/introducing-okf-v0-3) 🌟 - Release breakdown of OKF v0.3 introducing refined conformance rules, explicit trust tiers, self-describing bundles, and interoperability with agent skills.
- **(2026)** [GitHub: AnswerDotAI/llms-txt (/llms.txt Specification)](https://github.com/AnswerDotAI/llms-txt) 🌟 - Minimalist Markdown standard (`/llms.txt`) for exposing curated, LLM-friendly documentation indexes at web roots so coding and research agents can discover authoritative context without brittle HTML scraping.

## Vectorless Reasoning RAG and Cache-Augmented Generation (CAG)

- **(2026)** [GitHub: VectifyAI/PageIndex (Vectorless Reasoning-Based RAG)](https://github.com/VectifyAI/PageIndex) 🌟 - Leading vectorless, reasoning-based RAG framework that replaces chunking and vector databases with a hierarchical Table-of-Contents semantic tree navigated via LLM tree search for high-accuracy financial, legal, and technical analysis.
- **(2025)** [GitHub: hhhuang/CAG (Cache-Augmented Generation)](https://github.com/hhhuang/CAG) 🌟 - Reference implementation of Cache-Augmented Generation (CAG), preloading bounded document corpora into LLM long-context KV caches to eliminate runtime retrieval latency and ranking errors.
- **(2025)** [arXiv: Don't Do RAG — When Cache-Augmented Generation is All You Need for Knowledge Tasks](https://arxiv.org/abs/2412.15605) 🌟 - Foundational research paper benchmarking Cache-Augmented Generation (CAG) against standard RAG across multi-document QA benchmarks, demonstrating superior speed and accuracy for bounded knowledge bases.

## GraphRAG and Hybrid Knowledge Graphs

- **(2026)** [GitHub: microsoft/graphrag](https://github.com/microsoft/graphrag) 🌟 - Microsoft's modular graph-based Retrieval-Augmented Generation system combining LLM entity extraction, Leiden hierarchical community detection, and global map-reduce summarization for complex multi-hop reasoning.
- **(2026)** [GitHub: HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) 🌟 - Fast, token-efficient dual-level graph-enhanced RAG framework combining low-level entity retrieval with high-level thematic synthesis at a fraction of traditional GraphRAG indexing and query cost.
- **(2026)** [GitHub: neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python) 🌟 - Official Neo4j Python package for building production GraphRAG pipelines combining Cypher graph traversals, vector similarity indexes, and automated knowledge graph construction.
- **(2026)** [GitHub: topoteretes/cognee](https://github.com/topoteretes/cognee) 🌟 - Open-source graph-vector hybrid memory engine using an Extract-Cognify-Load (ECL) pipeline to unify codebases, documents, and databases into traversable knowledge graphs for AI agents and MCP clients.

## Modern RAG, Contextual Retrieval and Deep Document Parsing

- **(2024)** [Anthropic Research: Introducing Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval) 🌟 - Seminal engineering blueprint introducing Contextual Embeddings and Contextual BM25 (accelerated by Prompt Caching), reducing top-20 retrieval failure rates by 49% alone and 67% when paired with reranking.
- **(2026)** [GitHub: infiniflow/ragflow](https://github.com/infiniflow/ragflow) 🌟 - Leading open-source enterprise RAG engine built on deep document understanding (complex layout analysis, tables, charts, OCR), grounded citations, and agentic retrieval workflows.
- **(2026)** [GitHub: run-llama/llama_index](https://github.com/run-llama/llama_index) 🌟 - Flagship open-source data and orchestration framework for Agentic RAG, hybrid retrieval, structured extraction, and multi-step knowledge workflows over enterprise data sources.
- **(2026)** [GitHub: deepset-ai/haystack](https://github.com/deepset-ai/haystack) 🌟 - Production-hardened, modular Python framework for composing hybrid retrieval pipelines (BM25 + dense vectors + rerankers), document ingestion, and Kubernetes-ready search microservices.

## Persistent Agent Memory Systems

- **(2026)** [GitHub: mem0ai/mem0](https://github.com/mem0ai/mem0) 🌟 - Universal memory layer for AI applications and autonomous agents that automatically extracts, consolidates, and retrieves cross-session user, session, and organizational facts via hybrid vector-graph storage.
- **(2026)** [GitHub: getzep/graphiti](https://github.com/getzep/graphiti) 🌟 - Bi-temporal knowledge graph engine by Zep built for dynamic agent memory, tracking when facts became true and when they were superseded so agents reason accurately over evolving enterprise state.
- **(2026)** [GitHub: letta-ai/letta (formerly MemGPT)](https://github.com/letta-ai/letta) 🌟 - Stateful Agent OS enabling LLMs to explicitly manage their own tiered memory hierarchy (in-context core memory vs archival recall storage) across long-running autonomous tasks.

## Vector Databases, Hybrid Search and RAG Evaluation

- **(2026)** [GitHub: qdrant/qdrant](https://github.com/qdrant/qdrant) 🌟 - High-performance Rust vector and hybrid search engine featuring binary/scalar quantization, sparse + dense fusion, payload filtering, and native Kubernetes horizontal sharding.
- **(2026)** [GitHub: weaviate/weaviate](https://github.com/weaviate/weaviate) 🌟 - Cloud-native AI database combining HNSW vector search, BM25 keyword scoring, multi-tenancy isolation, and modular generative search pipelines on Kubernetes.
- **(2026)** [GitHub: milvus-io/milvus](https://github.com/milvus-io/milvus) 🌟 - Distributed, cloud-native vector database architected for billion-scale similarity search with disaggregated compute/storage and official Kubernetes Operator deployment.
- **(2026)** [GitHub: pgvector/pgvector](https://github.com/pgvector/pgvector) 🌟 - Open-source vector similarity search extension (HNSW and IVFFlat indexes) for PostgreSQL, enabling ACID-compliant hybrid SQL + vector retrieval without operating a separate vector database.
- **(2026)** [GitHub: chroma-core/chroma](https://github.com/chroma-core/chroma) 🌟 - Developer-friendly, open-source AI-native search and embedding database supporting local prototyping and distributed cloud-native deployments.
- **(2026)** [GitHub: explodinggradients/ragas](https://github.com/explodinggradients/ragas) 🌟 - De facto open-source evaluation framework for measuring RAG and agentic retrieval quality across faithfulness, answer relevancy, context precision, and context recall in CI/CD pipelines.

---
*See also: [Enterprise AI Platforms](enterprise-ai-platforms.md), [Model Context Protocol (MCP) and AI Agents](ai-agents-mcp.md), [Artificial Intelligence](ai.md), [MLOps](mlops.md), and [Databases](databases.md).*
