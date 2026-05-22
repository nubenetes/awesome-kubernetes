# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0-rc.18] - 2026-05-22

### Added
- **Official YouTube Data API v3 Integration**: Transitioned from brittle scraping to guaranteed 100% fidelity metadata extraction using official Google endpoints.
- **Robust Multimedia Hierarchy**: Implemented a 3-tier extraction fallback (Official API > yt-dlp Mobile > Gemini Pro Grounding) to eliminate generic placeholders and bot-detection blocks.
- **Optional Cache Restoration**: Introduced `restore_cache` manual flag across all V2 workflows to prevent stale automated data from overwriting manual repository updates.
- **Mandate 58 Codification**: Officially established the "Official-First" multimedia extraction protocol and rendering standards in `GEMINI.md`.

### Changed
- **O'Reilly Journey Ordering**: Reorganized the Video Hub to prioritize "Fundamentals and Documentaries" at the top, following a logical architectural learning path.
- **Standardized Workflow Inventory**: Updated documentation to reflect all 15 active automated workflows with their formal GitHub Action names.
- **Production-Grade Video Portal**: Refined Markdown rendering with mandatory multiline indentation and Mandate 19 compliance (blank lines around center tags).

### Fixed
- **Persistent Video Hub Links**: Hardcoded the "Agentic Video Hub" entry in V2 index and navigation to prevent deletion during automated regeneration cycles.
- **Markdown Linting MD058/MD039/MD051**: Resolved table spacing, link syntax, and fragment validation errors across `README.md` and index files.
- **Workflow YAML Syntax**: Fixed duplicated environment keys and indentation errors in `agentic_cron.yml` and `agentic_v2_pr_only.yml`.
- **Bot Permissions**: Added `pull-requests: write` to V2 synchronization workflows to enable automated PR creation.

## [2.0.0-rc.17] - 2026-05-22

### Changed
- **Centralized YouTube Enrichment**: Standardized YouTube metadata extraction across all curation pipelines (V1 and V2). All workflows now fetch real titles and descriptions from YouTube to ensure high-fidelity AI summaries.
- **Workflow Modularization**: Reverted the consolidation of the Video Hub into the Publisher pipeline, maintaining it as a standalone workflow (`agentic_v2_videos.yml`) for better operational flexibility.
- **Improved Video Hub Design**: Redesigned the V2 Elite Video Hub with high-fidelity categorization, technology tags, and individual collapsible blocks for better user experience and flow.

## [2.0.0-rc.14] - 2026-05-22
