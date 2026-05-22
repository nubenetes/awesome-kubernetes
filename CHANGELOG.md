# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0-rc.7] - 2026-05-22

### Fixed
- **GitHub Metadata Metrics**: Corrected the coverage calculation logic in `v2_optimizer.py` to properly identify GitHub repositories by ensuring URLs are correctly injected into the resource objects during the audit phase.
- **Knowledge Graph Integrity**: Resolved the 0% reporting bug in the V2 Portal index, ensuring accurate tracking of resource maturity.

### Changed
- **Pipeline Orchestration**: Successfully validated the new decoupled workflow system by performing a manual execution of the Metadata and Publisher engines.


## [2.0.0-rc.6] - 2026-05-22

### Added
- **High-Density Inline Summaries**: Replaced collapsible blocks with always-visible summaries appended directly to the resource line using an em-dash (—) separator for immediate readability.

### Fixed
- **V2 Rendering Engine**: Resolved a critical `TypeError` caused by incorrect indentation in the link rendering logic.
- **Workflow Reliability**: Standardized all GitHub Actions to use Python module execution mode (`python -m src.module`), eliminating `ModuleNotFoundError` issues.

## [2.0.0-rc.5] - 2026-05-22

### Added
- **Decoupled V2 Architecture**: Refactored the monolithic V2 builder into four specialized micro-workflows (**Health Monitor**, **Metadata Engine**, **AI Curator**, and **Publisher**) to optimize compute quotas and Gemini token consumption.
- **Minimalist Inline UI**: Implemented native HTML5 `<details>` summaries with `inline-block` behavior in the V2 Portal, significantly increasing vertical information density.
- **Knowledge Coverage Metrics**: Integrated real-time AI Enrichment and GitHub Metadata coverage tracking into PR reports and the V2 index.
- **Automated Scheduling**: Configured monthly automated runs for Health (1st) and Metadata (15th) agents.

### Fixed
- **V2 Rendering Logic**: Fixed a bug where links without a defined hierarchy or at top-level categories were omitted; introduced the **Standard Reference** fallback section.
- **Markdown Linting**: Resolved TOC anchor broken links (MD051) in `README.md`.

## [2.0.0-rc.4] - 2026-05-22

### Added
- **Mosaic Expansion**: Added Olena Kutsenko's YouTube channel to the index mosaic on both V1 and V2, including custom profile picture extraction and asset synchronization.

## [2.0.0-rc.3] - 2026-05-21

### Added
- **Flash-First Architecture**: Strategic transition to Gemini Flash/Lite models for high-density analysis, achieving >90% cost reduction and radical throughput gains.
- **Multi-Phase Incremental Persistence**: Dual-layer auto-save mechanism (Metadata & AI phases) ensuring zero data loss during long-running CI/CD workflows.
- **Industrial Telemetry Layer**: Deep AI observability with token counting, payload estimation, and transparent error diagnostics.
- **GitHub Actions Cache Integration**: High-resilience persistence layer to reuse enriched metadata across interrupted or queued runs.
- **Emergency PR Workflow**: Lightweight "Safety Off-ramp" to publish current cached state without AI overhead.

### Changed
- **Optimized Batching Strategy**: Balanced batch sizes (50 items) and safety delays (2s) to maximize API quota utilization (TPM/RPM).
- **Hardened Error Handling**: Transitioned from silent failure loops to strict Circuit Breaker (Exit Code 42) logic.
- **Unified Global Logging**: Enforced `PYTHONUNBUFFERED` logging across the entire workflow ecosystem for real-time transparency.
- **V2 UI Refinement**: Optimized header contrast for Light/Dark modes and fixed semantic cross-link duplication.

### Fixed
- **API Timeout Bottleneck**: Increased HTTP request timeouts to 180s to accommodate high-density token generation.
- **Markdown Linter Compliance**: Resolved MD024, MD025, MD031, and MD039 violations through "Nuclear" whitespace sanitization and header depth management.
- **Workflow Permissions**: Optimized security model to allow automated PRs without requiring conflictive workflow-write permissions.

## [2.0.0-rc.2] - 2026-05-20

### Added
- **Announce Banner**: Added a global announcement banner to V1 directing users to the V2 Elite Portal.
- **Dependency Caching**: Implemented `cache: pip` via `requirements.txt` to significantly speed up build times.
- **MkDocs Features**: Activated native Privacy Plugin, Pruned Navigation, Social Cards in V1, Code Copy, Tab Sync, and Tooltips.

### Changed
- **CI/CD Deployment**: Migrated deployment to use native GitHub Pages artifacts (`upload-pages-artifact`, `deploy-pages`) instead of the `gh-pages` branch.
- **V2 Elite Aesthetic**: Upgraded UI to "Cyber Cloud" style featuring high-contrast pure black backgrounds, neon cyan accents, and advanced glassmorphism.

## [2.0.0-rc.1] - 2026-05-19

### Added
- **Nubenetes Elite Portal (V2)**: A high-density, agentic-curated edition of the archive.
- **Automotive Container Metaphor**: New modernized visual identity with a custom PNG asset.
- **Agentic AI Orchestration**: Multi-tier model coordination (Gemini Pro/Flash) with adaptive rate limiting.
- **Maturity Taxonomy**: Professional 5-tier classification system for all Elite resources.
- **Semantic Cross-Linking**: Autonomous identification of related architectural patterns.
- **Platinum Maintenance Suite**: Automated triage, social preview cards, and dependency guarding.
- **Real-time Web Grounding**: Live data verification using MCP-style search for high-precision curation.
- **Industrial Learning Flow**: O'Reilly-style technical progression in V2 documentation.

### Changed
- **Unified Metadata Database**: Centralized all link lifecycle data in `data/inventory.yaml`.
- **Global Currency Standard**: Adopted Euro (€) as the primary currency for all cost and economic analysis.
- **Navigation Overhaul**: Flat, high-density navigation structure for the Elite portal.
- **README Metrics Engine**: Transitioned to a fully database-driven metric extraction system.

### Fixed
- **Image Path Resolution**: Implemented flat asset routing to prevent broken relative paths.
- **Markdown Rendering**: Fixed HTML/Markdown interop using `markdown="1"` attributes.
- **Trigger Loop Prevention**: Hardened CI/CD workflows against infinite automation loops.
- **URL Normalization**: Standardized canonical formats to prevent semantic drift.

### Security
- **Credential Protection**: Hardened environment variable management across all agentic scripts.
- **License Guard**: Automated monitoring of permissive-to-restrictive license transitions.

---
*Generated by Nubenetes Agentic Intelligence*
