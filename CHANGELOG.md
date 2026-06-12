# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [[2.4.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.4.0) - 2026-06-12

### Changed
- **SEO-Friendly URL Structure**: Reverted the entire ecosystem to use clean directory URLs (e.g., `/demos/` instead of `/demos.html`) by enabling `use_directory_urls: true` in both V1 and V2 configurations.
- **Mandatory Path Standard**: Updated `GEMINI.md` mandates to establish root-relative paths (e.g., `/images/`) as the standard for manual HTML assets to prevent breakage across directory levels.
- **V2 Optimization Automation**: Updated `src/v2_optimizer.py` to ensure all future automated regenerations of the V2 Elite Portal follow the clean URL and absolute path standard.

### Fixed
- **V2 Index Navigation**: Corrected all manual HTML navigation badges in the V2 index to use clean directory paths, resolving 404 errors during the SEO transition.

## [[2.3.44]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.44) - 2026-06-10

### Added
- **Grafana AI Observability Video**: Added "AI Observability Deep Dive Demo | Grafana Cloud" by Ivana Hučková to the V2 Video Hub under the "AI Agents and Observability" section.

## [[2.3.43]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.43) - 2026-06-03

### Fixed
- **Mermaid Diagram Text Overflow**: Wrapped long text strings inside the "4.2. Hardened Architecture (2026)" Mermaid diagram in `README.md` using `<br>` to prevent text clipping and rendering issues in standard Markdown viewers.

## [[2.3.42]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.42) - 2026-06-03

### Fixed
- **Mobile Drawer Contrast (V2)**: Resolved contrast issues in the Nubenetes V2 mobile navigation drawer under dark mode (`slate`) by overriding `.md-nav__title`, logo, icons, and `.md-nav__source` background/foreground colors. This ensures readable white text and visible icons on dark backgrounds.

## [[2.3.41]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.41) - 2026-06-03

### Fixed
- **Agentic Pulse Metadata and Sort Logic**: Corrected the V2 optimizer script (`src/v2_optimizer.py`) to query the correct `year` attribute instead of the non-existent `pub_date` when rendering the Agentic Pulse section on the V2 home page, and introduced fallback sorting logic for entries without explicit publication years to ensure chronological precision.

## [[2.3.40]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.40) - 2026-06-03

### Removed
- **Deprecated AWS Quick Start Reference**: Confirmed retirement of the AWS Quick Starts program (replaced globally by AWS Partner Solutions), removed `https://aws.amazon.com/es/quickstart` from the centralized inventory database, and updated the V1 and V2 documentation files to delete the dead references.

## [[2.3.39]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.39) - 2026-06-02

### Added
- **ClickHouse YouTube Channel Integration**: Registered the official ClickHouse YouTube channel in the centralized inventory and regenerated both the V1 and V2 homepage mosaics, sorting ClickHouse under the Observability, Databases & Cloud Storage category in V2.
- **ClickHouse SVG Logo Asset**: Added a color-coded orange SVG logo for ClickHouse to guarantee legibility across light and dark platforms.

## [[2.3.38]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.38) - 2026-06-02

### Added
- **YouTube Embed Iframe Refusal Fix**: Solved the `www.youtube.com refused to connect` error in video iframe players by implementing a parser (`to_embed_url`) in the generator script to dynamically rewrite standard YouTube watch/shortened URLs into the required embed format, fully preserving start-times (`start=...`) and playlist IDs (`list=...`).

### Fixed
- **MD037 Lint Fix (Video Portal)**: Fixed a markdown linter failure in `v2-docs/videos/cloud-native.md` (and other video documents) by converting asterisk-based bullets (`* `) in video summaries to dash-based bullets (`- `). This avoids syntax collision where the linter parses indented asterisk bullets inside blocks as malformed bold/emphasis markers.

## [[2.3.37]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.37) - 2026-06-02

### Added
- **Programmatic Smart Injection (Option B)**: Replaced legacy full-document rewriting using Gemini Pro with a highly efficient programmatic Markdown injector. The new system uses Gemini Flash 3.5 to choose the target section header, while Python surgically inserts the link. This prevents 429 rate limit blocks and cuts down API costs by 95%.
- **Persisted Raw Impact Score**: Added `impact_score` attribute to evaluations saved inside `data/inventory.yaml`, ensuring that cached resources retain their original AI classification scores.

### Fixed
- **KeyError: 'impact_score'**: Implemented resilient fallback logic in the curation orchestrator to calculate `impact_score` from the `stars` attribute (e.g. `stars * 20`) for cached items that lack the raw `impact_score` field.

## [[2.3.36]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.36) - 2026-05-29

### Fixed
- **Legal Disclaimer Duplication**: Removed duplicate/redundant line of text in README.md section 15.3.

## [[2.3.35]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.35) - 2026-05-28

### Added
- **Grafana Observability Video**: Added the Viktor Farcic video `I Stopped Staring at Dashboards. AI Reads My Grafana Metrics Now.` to the V2 Video Hub under the "AI Agents and MCP" learning path.

## [[2.3.34]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.34) - 2026-05-28

### Added
- **Link Provenance Tracking**: Added `addition_method` metadata attribute to `data/inventory.yaml` to differentiate between manually curated and automatically ingested links.
- **Database Migration**: Migrated all 18,004 existing database entries to have `addition_method: manual` by default.
- **Workflow & Optimizer Integration**: Programmed `src/agentic_curator.py` to mark automatically ingested resources as `automatic`, and updated `src/v2_optimizer.py` to default new V1 Markdown source resources to `manual`.

### Changed
- **Documentation & Memory Systems**: Added documentation for `addition_method` in `README.md`, `GEMINI.md`, and `src/memory/health_learning.json`.

## [[2.3.32]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.32) - 2026-05-28

### Changed
- **Arsys Logo Dark Mode Contrast**: Changed the Arsys logo fill color to a constant corporate electric sky blue (`#00a2e8`) inside the SVG, ensuring maximum contrast on both white (V1) and slate/black (V2) backgrounds.
- **Removed Logo CSS Inversion**: Removed the dark mode CSS filter invert rule in `extra.css` to preserve branding color integrity.

## [[2.3.31]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.31) - 2026-05-28

### Changed
- **Arsys Logo Dark Mode Adaptation**: Embedded light/dark prefers-color-scheme styles inside the Arsys SVG logo and added a CSS invert filter for the slate theme in `extra.css` to fix visibility in dark mode.

## [[2.3.30]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.30) - 2026-05-28

### Fixed
- **Wikimedia Commons URL Correction**: Replaced the broken HTML error page (downloaded due to invalid hash pathing) with a valid vector SVG file by using the correct MD5 filename-derived directory structure (`8/88/Arsys_logo.svg`) on upload.wikimedia.org.

## [[2.3.29]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.29) - 2026-05-28

### Added
- **Arsys Channel Integration**: Registered `https://www.youtube.com/@arsys` in `data/inventory.yaml` under `cloud_providers` (V2) and ordered to append at the end of V1 flat sequence.

### Fixed
- **Video Hub Heading Level Fix**: Fixed a markdown linter error (MD001) in the generated video hub index by changing the heading increment from h3 to h2 (`## Learning Dimensions`).

## [[2.3.28]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.28) - 2026-05-28

### Changed
- **Mandate 23 Documentation**: Updated `GEMINI.md` and `health_learning.json` to formally document the database-driven dual layout design of YouTube mosaics.

## [[2.3.27]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.27) - 2026-05-28

### Added
- **Workflow Automation for Mosaic**: Configured the V2 Publisher workflow to execute `src/reorganize_mosaic.py` automatically on each run.

## [[2.3.26]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.26) - 2026-05-28

### Fixed
- **Video Hub Index Heading Level Correction**: Adjusted generator code to prevent heading hierarchy lint failures.

## [[2.3.25]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.25) - 2026-05-28

### Added
- **Database Migration for YouTube Mosaic**: Migrated YouTube channel mosaic configuration from the deprecated `youtube_channels_mosaic.yaml` to the unified monolithic `data/inventory.yaml` and refactored the layout generator to dynamically read from the database.

## [[2.3.24]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.24) - 2026-05-28

### Changed
- **Restored V1 Flat YouTube Mosaic Layout**: Restored the flat list layout (11 channels per row, sorted by `order_v1`) on the V1 homepage, while preserving the advanced categorized V2 dashboard.

## [[2.3.23]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.23) - 2026-05-28

### Changed
- **Quote Card HTML Structure**: Wrapped the clickable `quote-card-link` in a block-level `div` container to prevent the Markdown processor from wrapping the inline `a` link in a paragraph `<p>` tag. This ensures correct HTML parsing and restores the quote card's dynamic hover animations and transitions.

## [[2.3.22]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.22) - 2026-05-28

### Changed
- **Showcase Image Conformance Footer Bar**: Replaced the absolute badge overlay with an elegant, responsive glassmorphic footer bar `.hero-showcase-footer` beneath the image. This bar contains the CNCF conformance badge alongside an explanatory caption about workload portability, ensuring that no text covers any part of the main showcase image.

## [[2.3.21]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.21) - 2026-05-28

### Changed
- **Reordered V2 Homepage Header**: Reorganized the V2 home page layout, placing the large responsive CNCF conformance image showcase first, followed by Horatio's framed interactive quote card, and finally the four flex dashboard cards.
- **Glassmorphic Quote Card**: Replaced the plain text quote with a styled, framed quote card featuring an interactive dashed border, a custom quote icon, and a glowing neon cyan hover state that links directly to Horatio Nelson Jackson's Wikipedia page.
- **Enlarged Conformance Showcase**: Increased the max-width of the CNCF conformance wrapper to 1100px to ensure it remains as large as possible across all high-resolution devices.

## [[2.3.20]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.20) - 2026-05-27

### Changed
- **CNCF Showcase Conformance Image Effects**: Added a glassmorphic wrapper `.hero-showcase-wrapper` to the main CNCF conformance image on the V2 homepage with hover scale effects (`1.03x`), brightness filters, a neon cyan shadow glow, and an interactive overlay badge.
- **V2 Nav and Index Path Fixes**: Resolved broken internal references to `videos.md` in `v2-mkdocs.yml` and the strategic dimensions list by permanently updating the compiler to resolve paths to the modularised `./videos/index.md` location. Integrated MkDocs Material's `navigation.indexes` feature so that clicking the top-level "Agentic Video Hub" menu tab links directly to the Overview page (`videos/index.md`) without sub-navigation redundancy.

## [[2.3.19]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.19) - 2026-05-27

### Added
- **Modularized Video Hub**: Replaced the legacy monolithic `v2-docs/videos.md` with a structured, multi-page directory (`v2-docs/videos/`) separating video resources into AI Agents, DevOps/IaC/SRE, Cloud Native Core, and Fundamentals learning paths.
- **Robust Slugification and Header Cleaning**: Upgraded the slugification and header normalization logic to ensure 100% compatibility with MkDocs anchor resolution, stripping commas, parentheses, slashes, and special symbols to prevent broken internal links.
- **Monthly Video Automation Schedule**: Configured a monthly cron trigger (`0 6 1 * *`) in the V2 Video Hub Builder GitHub action to automate video curation and portal updates.

### Changed
- **Persisted Hero Dashboard Cards**: Integrated the 4 glassmorphic interactive cards directly into the `v2_optimizer.py` compilation script for `v2-docs/index.md`, preventing them from being overwritten during V2 rendering cycles and updating the video link to `./videos/index.html`.

## [[2.3.18]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.18) - 2026-05-27

### Added
- **4-Card Hero Dashboard**: Expanded the V2 homepage header from two to four interactive dashboard cards, adding entry points for "AI & MCP Agents" (with custom purple glow) and "Agentic Video Hub" (with custom pink glow). Improved visual layout structure and updated all card links to point directly to `.html` destinations to prevent 404 compilation target errors.

## [[2.3.17]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.17) - 2026-05-27

### Changed
- **V2 Header Cards Optimization**: Fixed broken `.md` targets in raw HTML header cards by pointing them to compiled `.html` pages. Upgraded card sizing to use a responsive flex layout (`flex: 1; max-width: 280px; min-width: 200px;`) with increased padding and added visual hover highlight states on card icons matching the mosaic aesthetics.

## [[2.3.16]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.16) - 2026-05-27

### Changed
- **V2 Homepage Interactive Header Badges**: Converted the top inline Kubernetes and Hero Car image links on the V2 index page into styled, responsive glassmorphic cards. Kubernetes links to the internal curated Kubernetes resources section rather than the external homepage, improving contextual navigation.

## [[2.3.15]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.15) - 2026-05-27

### Changed
- **Homepage YouTube Mosaic Scaling & Transitions**: Refactored the icon layout styling to use uniform responsive sizing (48px) instead of viewport percentage widths. Added hover micro-animations (scale-up scale factor 1.15x and brightness filters) for both light and dark modes to enhance aesthetic premium quality.

## [[2.3.14]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.14) - 2026-05-27

### Changed
- **Kyndryl YouTube Channel Categorization**: Moved the Kyndryl channel from the Tech E-Learning category to the Cloud Providers & Core Infrastructure category in the homepage mosaic mapping database and files.

## [[2.3.13]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.13) - 2026-05-27

### Changed
- **Homepage YouTube Mosaic Visual Borders**: Replaced category text headers with thin colored outline borders around each channel group inside the mosaic. This restores a continuous, symmetric flow of clickable icons while visually highlighting the different technological categories.

## [[2.3.12]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.12) - 2026-05-27

### Added
- **Homepage YouTube Mosaic Reorganization**: Reorganized the visual channels mosaic on V1 and V2 homepages into logical technology categories (e.g., AI & Advanced Tech, Cloud Providers, Cloud Native, etc.).
- **Mosaic Database Schema**: Introduced `data/youtube_channels_mosaic.yaml` to catalog and preserve the channel classification directly in the repository configuration.

## [[2.3.11]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.11) - 2026-05-27

### Added
- **Microsoft Reactor YouTube Channel**: Added Microsoft Reactor to the homepage channels mosaic in V1 and V2, moving Playwright to its own row at the bottom of the mosaic.

## [[2.3.10]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.10) - 2026-05-27

### Added
- **Agentic DevOps Live Playlist**: Integrated the Microsoft/GitHub "Agentic DevOps Live" series into the V2 Video Hub under the AI and Future Operations category, detailing SRE agents, Copilot App Mod agents, and autonomous development loops.

## [[2.3.9]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.9) - 2026-05-27

### Added
- **VS Code Dev Tunnels Video**: Integrated Gisela Torres' tutorial on VS Code Dev Tunnels into the V2 Video Hub, highlighting the secure remote access capabilities and developer productivity benefits. [SPANISH CONTENT]

## [[2.3.8]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.8) - 2026-05-27

### Added
- **Red Hat Summit 2026 Video**: Integrated the Red Hat Summit 2026 interview with Fran Heeran into the Video Hub, detailing the architectural shift of telecommunications providers to unified cloud-native networks using OpenShift Virtualization.

## [[2.3.7]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.7) - 2026-05-26

### Fixed
- **GitHub Actions Version Hardening**: Restored and upgraded all 15 workflows to use verified, true latest stable major versions (v6/v5/v8) across the entire CI/CD pipeline, ensuring maximum stability and security.
- **Deployment Workflow Reliability**: Resolved transient "Failed to download" infrastructure errors in the "06.1. Final Portal Deploy" workflow by aligning with official GitHub Action releases and latest stable tags.

## [[2.3.6]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.6) - 2026-05-26

### Changed
- **Deployment Documentation Sync**: Updated `README.md` to reflect the new deployment workflow name ("06.1. Final Portal Deploy") and its stabilized trigger configuration.
- **Workflow Stabilization**: Renamed the deployment workflow file to `06.deploy_final.yml` to resolve persistent GitHub trigger issues and ensure reliable production releases.

## [[2.3.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.5) - 2026-05-26

### Added
- **Visual Branding Expansion**: Integrated the official **Playwright** YouTube channel into the visual branding mosaic in both V1 and V2 index pages.
- **Visual Asset Integration**: Optimized and integrated the high-resolution logo for the Playwright channel.

## [[2.3.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.4) - 2026-05-25

### Removed
- **Redundant SEO Mitigation Assets**: Deleted the custom `404.md` page in the V2 portal. Under the Hybrid SEO-First architecture, legacy root URLs are now valid (serving V1 content), making the specialized rescue page unnecessary.

## [[2.3.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.3) - 2026-05-25

### Fixed
- **Navigation Loop**: Corrected the "Back to V1" link to point specifically to `https://nubenetes.com/v1/`. This avoids the automatic redirect at the domain root, allowing users to actually reach the exhaustive archive.

## [[2.3.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.2) - 2026-05-25

### Changed
- **Hybrid Sync Standardization**: Unified navigation labels and URLs across `v2-mkdocs.yml` and `src/v2_optimizer.py`. The "Back to V1" link now consistently points to the domain root to leverage SEO-protected legacy paths.

## [[2.3.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.1) - 2026-05-25

### Fixed
- **Deployment Resilience**: Resolved a recursive copy error in the GitHub Pages deployment workflow by implementing a temporary staging area for the V1 build process.

## [[2.3.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.3.0) - 2026-05-25

### Added
- **Hybrid SEO-First Architecture**: Implemented a sophisticated dual-version deployment strategy. V1 is restored to the domain root (`/`) to preserve 6+ years of SEO authority and deep-links, while a root-level redirect guides human traffic to the modern V2 Elite Portal at `/v2/`.

## [[2.2.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.2.4) - 2026-05-25

### Changed
- **Governance & Documentation Sync**: Performed a comprehensive update of `README.md`, `GEMINI.md`, and local session memory to reflect the new architectural standards (V2 at Root), workflow hardening (rebase resilience), and mandatory PR-based governance for production deployments.

## [[2.2.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.2.3) - 2026-05-25

### Fixed
- **Redirect Collision Resolution**: Removed conflicting HTML redirects in the V2 portal that were blocking access to new Elite content with the same filenames as legacy pages.
- **SEO Mitigation Refinement**: Shifted to a "Smart 404" only strategy for the root domain, ensuring that URLs like `kubernetes.html` serve the updated V2 content while missing legacy links are elegantly handled by the custom 404 page.

## [[2.2.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.2.2) - 2026-05-25

### Added
- **SEO Mitigation (Smart 404)**: Implemented a custom 404 page in the V2 portal (`404.md`) to guide users from broken historical links to the new V1 archive location.
- **HTML Redirects**: Integrated the `mkdocs-redirects` plugin and configured 301-style HTML redirects for the top 12 legacy URLs, preserving search engine authority and user experience during the root migration.

## [[2.2.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.2.1) - 2026-05-25

### Changed
- **Default Landing Page (V2 at Root)**: Promoted the Nubenetes Elite Portal (V2) to the root of the domain (`https://nubenetes.com/`) to provide a modern, AI-curated default experience.
- **V1 Archive Relocation**: Moved the exhaustive V1 archive to the `/v1/` subdirectory (`https://nubenetes.com/v1/`).
- **Navigation Synchronization**: Updated all navigation links and announce banners across both versions to ensure seamless switching between the Elite Portal and the Exhaustive Archive.
- **Workflow Realignment**: Reconfigured the GitHub Pages deployment pipeline to support the new directory structure while maintaining zero-downtime synchronization.

## [[2.2.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.2.0) - 2026-05-25

### Fixed
- **Workflow Resilience (Race Conditions)**: Implemented a mandatory `git pull --rebase` strategy across all five automated workflows (Metadata, AI Curator, Video Hub, Publisher, and README Sync). This prevents "rejected push" errors by allowing concurrent bot executions to automatically integrate sibling commits before pushing back to the `develop` branch.

## [[2.1.9]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.9) - 2026-05-25

### Changed
- **Visual Identity (Ultra-Visible "N" Favicon)**: Redesigned the favicon to follow the high-visibility patterns of X.com, GitHub, and LinkedIn. The new design features a massive, bold cyan "N" on a solid black background, maximizing clarity and brand recognition in browser tabs.
- **Index Brand Restoration**: Restored the original "Gemini construction car" as the primary hero image in the V2 portal's header, maintaining the project's established visual identity while separating it from the functional favicon.

## [[2.1.8]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.8) - 2026-05-25

### Fixed
- **Configuration Integrity**: Fixed a YAML syntax error in `mkdocs.yml` (corrupted trailing line) that was causing GitHub Pages deployment failures.

## [[2.1.7]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.7) - 2026-05-25

### Changed
- **Visual Identity (Ultra-Visible Favicon)**: Replaced the complex favicon with an ultra-minimalist, high-contrast design (Cyan "N" on dark background) to ensure maximum visibility in browser tabs, following the design patterns of X, GitHub, and LinkedIn.
- **Index Branding Restoration**: Reverted the header image on the V2 index page to the "Gemini construction car" (now standardized as `hero-car.png`) to maintain the project's established visual impact while keeping a separate, cleaner icon for navigation tabs.

## [[2.1.6]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.6) - 2026-05-25

### Changed
- **Visual Identity (Custom Logo)**: Replaced the generic car icon with a custom-engineered minimalist logo ("Nubenetes Nano Logo"). The new design features a high-contrast Cyber Cloud vehicle with Kubernetes helm wheels, ensuring superior perception and brand recognition as a favicon.
- **Asset Optimization**: Standardized the new logo as an SVG source and a 256x256 transparent PNG for cross-platform clarity.

## [[2.1.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.5) - 2026-05-25

### Changed
- **Automated Workflow Optimization**: Refactored V2 ecosystem workflows (Metadata, AI Curator, Video Hub, and Publisher) to utilize direct git push to the `develop` branch instead of creating redundant Pull Requests. This eliminates manual overhead and confusion while ensuring derived content is seamlessly synchronized using `[skip ci]` flags.
- **Workflow Observability**: Integrated GitHub Artifacts for automated architecture audits and decision matrices, replacing redundant PR comments.

## [[2.1.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.4) - 2026-05-25

### Added
- **Leading AI Channels Mosaic**: Expanded the visual branding mosaic in V1 and V2 portals to include the official YouTube channels for **Google Gemini**, **Google DeepMind**, **Anthropic**, **Microsoft Copilot**, **OpenAI**, and **Meta AI**.
- **Visual Asset Integration**: Optimized and integrated high-resolution logos for the new AI channels to maintain high-density visual standards.

## [[2.1.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.3) - 2026-05-25

### Fixed
- **Definitive AVM Video Correction**: Applied a surgical fix to the "Azure Verified Modules" video metadata in the V2 portal and inventory. Corrected the title and summary to accurately reflect the session's focus on Spec-Driven Development, the "Spec Kit" framework, and Well-Architected Azure workloads using GitHub Copilot.

## [[2.1.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.2) - 2026-05-25

### Added
- **Visual Branding Expansion**: Integrated **ITOpsTalk** (Microsoft Azure) and **Google Cloud Tech** official channels into the visual branding mosaic in both V1 and V2 index pages.
- **Azure Verified Modules (AVM) Integration**: Added the technical session on building secure Azure workloads using AVM and GitHub Copilot to the V2 Elite Video Hub. The summary highlights spec-driven development and the "Spec Kit" framework for reliable AI-assisted IaC.

## [[2.1.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.1) - 2026-05-25

### Added
- **Stanford CS229 LLM Session**: Integrated the Stanford CS229 lecture on "Building Large Language Models" into the V2 Elite Video Hub. The architectural summary focuses on LLM orchestration, alignment (DPO/RLHF), and systems optimization for 2026 AI infrastructure.

## [[2.1.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.1.0) - 2026-05-25

### Added
- **Dual-Logo Branding Header**: Integrated a new dual-logo header in the V2 portal, featuring the transparent Kubernetes logo alongside the modern Gemini construction car icon. The Gemini icon serves as a shortcut to the project's introduction page.

### Changed
- **Visual Balance**: Resized visual assets to ensure architectural symmetry between the Kubernetes and Gemini logos in the portal's main entry point.

## [[2.0.9]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.9) - 2026-05-25

### Changed
- **Visual Optimization**: Resized the transparent Kubernetes logo to 150px to ensure it remains subtle and professional as a header icon, matching the visual balance of the original design while maintaining modern transparency.

## [[2.0.8]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.8) - 2026-05-25

### Fixed
- **Terminology Standardization**: Standardized the use of "AI" across the entire V2 ecosystem, updating the builder script (`src/v2_optimizer.py`), global configurations (`data/special_assets.yaml`), and all related documentation pages. This prevents the redundant "AI and Artificial Intelligence" title from reappearing during portal regeneration.

## [[2.0.7]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.7) - 2026-05-25

### Fixed
- **Visual Integration**: Replaced the opaque Kubernetes logo (black background) with a high-quality transparent PNG version. This ensures seamless visual integration across both light and dark modes in the V1 and V2 portals.

## [[2.0.6]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.6) - 2026-05-25

### Changed
- **Branding & Social Identity**: Renamed the modern favicon to `favicon-car-modern.png` and configured the MkDocs `social` plugin to utilize it as the default OpenGraph logo across V1 and V2 portals. This ensures a consistent, modern visual identity whenever documentation pages are shared on social platforms.

## [[2.0.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.5) - 2026-05-25

### Changed
- **Visual Identity Modernization**: Replaced the legacy car favicon with a modern "Gemini construction car" PNG (256x256) across all portal versions (V1, V2, and Archive) to improve search engine presentation and brand aesthetics.

## [[2.0.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.4) - 2026-05-25

### Added
- **Claude Code Integration**: Added the "Mastering Claude Code" technical session to the V2 Elite Video Hub with a high-density summary of agentic CLI operations and MCP integration.
- **Hosted Control Planes (HyperShift)**: Integrated the GitOps Guide to the Galaxy session on HCP/HyperShift to provide architectural depth on multi-tenant Kubernetes control planes.

### Fixed
- **Video Metadata Accuracy**: Corrected a significant metadata mismatch where the GitOps Guide to the Galaxy playlist was mislabeled as "Kubernetes: The Documentary".
- **Inventory Precision**: Synchronized `data/inventory.yaml` with corrected video identities and professional summaries.

## [[2.0.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.3) - 2026-05-25

### Changed
- **AI Navigation Simplification**: Renamed the "AI and Artificial Intelligence" category to just **AI** in the V2 portal to eliminate redundancy and improve UI density.
- **Documentation Alignment**: Updated `GEMINI.md` to reflect the standardized "AI Dimension" naming convention.

## [[2.0.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.2) - 2026-05-24

### Added
- **YouTube Mosaic Enrichment**: Added official channels for **CloudNativeMadrid** and **Kyndryl** to the visual mosaic in both V1 and V2 index pages.
- **Visual Assets**: Integrated new high-resolution logos for the added YouTube channels into the repository's image library.

## [[2.0.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.1) - 2026-05-24

### Fixed
- **V2 Page Stability**: Implemented multi-location support using `v1_locations` to prevent accidental pruning of technical pages (e.g., `angular.md`, `introduction.md`).
- **Branding Protection**: Restored and locked the V2 Index visual identity, including the Kubernetes banner, automotive container metaphor, and the complete YouTube logo mosaic.
- **Acronym Normalization**: Standardized short titles in navigation and index to correctly preserve acronyms like **AI**, **MCP**, **IaC**, **AWS**, and **GCP**.
- **AI Rescue Hardening**: Fixed the AI-driven link rescue logic to reject generic redirects (e.g., `/learn`, `/about`) ensuring high-precision technical links.
- **URL Normalization trackers**: Added stripping for industrial trackers like `intcmp`, `mc_cid`, and `mc_eid` to maintain inventory canonical integrity (Mandate 24).
- **YAML Syntax Integrity**: Repaired critical syntax errors in `inventory.yaml` and established automated title quoting/escaping.

### Changed
- **Evolutionary V2 Integration**: Refactored the V2 Publisher to faithfully integrate new inventory data without radically altering the established v2.0.0 layout.
- **Resilient Rendering**: Enabled conservative link inclusion in `render-only` mode to preserve "Standard References" while pending AI hierarchical evaluation.

## [[2.0.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.0) - 2026-05-22

### Added
- **Official YouTube Data API v3 Integration**: Guaranteed 100% fidelity metadata extraction and elimination of bot-detection blocks.
- **Robust Multimedia Hierarchy**: 3-tier fallback (Official API > yt-dlp > Gemini Pro Grounding) for high-fidelity technical summaries.
- **Optional Cache Restoration**: Controlled via `restore_cache` flag across all V2 workflows to protect manual repository updates.
- **Mandate 58 Codification**: "Official-First" protocol for multimedia and multiline rendering standards established in [`GEMINI.md`](GEMINI.md).
- **Automated Video Enrichment**: Implementation of `src/enrich_videos.py` with O'Reilly Journey builder.

### Changed
- **Standardized Workflow Sequencing**: Implemented a numeric 01-08 nomenclature for all 15 workflows to clarify the execution lifecycle.
- **Physical Workflow Refactoring**: Renamed all [`.github/workflows/`](.github/workflows/) files with numeric prefixes to enforce logical ordering in the GitHub Actions UI.
- **O'Reilly Journey Architecture**: Prioritized "Fundamentals and Documentaries" in the Video Hub to provide a logical learning flow for users.
- **Categorized Workflow Matrix**: Enhanced [`README.md`](README.md) section 9.1 with a "Phase / Category" column and direct clickable links to each workflow UI.

### Fixed
- **Anonymized Site Metadata**: Removed personal names and emails from MkDocs configuration (V1 and V2) to ensure privacy and prevent Google indexing of contributor identities.
- **YouTube Mosaic Rendering**: Resolved a critical newline bug breaking the first icon (Docker) in both V1 and V2 index pages.
- **Persistent V2 Navigation**: Hardcoded Video Hub links in the V2 Index and navigation to ensure stability during automated regeneration.
- **Markdown Rendering Hardening**: Resolved indentation bugs and Mandate 19 violations (blank lines around center tags).
- **YAML Syntax and Permissions**: Fixed duplicated keys and added `pull-requests: write` permissions.

## [[2.0.0-agentic]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.0.0-agentic) - 2026-05-15

### Added
- **Agentic AI Orchestration Core**: Inception of the autonomous engine for discovery and evaluation.
- **Nubenetes V2 (Agentic Elite)**: Implementation of the high-density curated edition optimized for 2026 standards.
- **Visual Health Dashboard**: Automated HTML reports and GitHub Issue notifications for curation visibility.
- **Maturity Scoring Engine**: AI-driven classification (De Facto Standard, Enterprise-Stable, etc.).
- **Flash-First High-Density Curation**: Throughput optimization using Gemini Flash for mass processing.
- **Community Contribution**: Initial bot-driven dependency updates (Contribution by **dependabot[bot]**).

## [[1.9.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.9.5) - 2025-01-31

### Added
- **Kanvas Snapshot Support**: Integration of emerging visualization plugins for k8s (Contribution by **Vivek Vishal**).
- **Meshery Integration**: Added service mesh management tools (Contribution by **Vivek Vishal**).
- **API Testing Expansion**: Inclusion of Mockapy and modern REST testing tools (Contribution by **n0rdd3v**).

## [[1.9.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.9.0) - 2024-01-16

### Added
- **Platform Engineering Surge**: Major inclusion of IDP and platform engineering resources (Contribution by **Daniel Bryant** in [PR #52](https://github.com/nubenetes/awesome-kubernetes/pull/52)).
- **Security Scanners**: Integration of Chainsaw for Kubernetes testing (Contribution by **Charles-Edouard Brétéché**).
- **simplyblock Integration**: Added low-latency storage resources (Contribution by **Christoph Engelbert** in [PR #49](https://github.com/nubenetes/awesome-kubernetes/pull/49)).

### Changed
- **Structural Pivot**: Reorganized core repository structures to align with declarative management patterns.
- **Kustomize Focus**: Major surge in Kustomize-based deployment documentation.

## [[1.8.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.8.0) - 2023-01-01

### Added
- **Automation Phase**: Integration of Jenkins automation for repository cleanup and maintenance.
- **Remote Job surge**: Dedicated tracking for Cloud Native career opportunities (Contribution by **Anthony Palomarez**).
- **EKS 1.22 Support**: Detailed upgrade tutorials and lifecycle management (Contribution by **itamarb8** in [PR #19](https://github.com/nubenetes/awesome-kubernetes/pull/19)).
- **m9sweeper Integration**: Added Kubernetes security platform (Contribution by **Jacob Beasley** in [PR #33](https://github.com/nubenetes/awesome-kubernetes/pull/33)).

## [[1.7.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.7.0) - 2022-01-10

### Changed
- **Ecosystem Hardening**: Massive verification cycle of 2020-2021 links to ensure archive validity.
- **Contributor Influence**: Significant content refinement from **Gerard Braad** ([PR #28](https://github.com/nubenetes/awesome-kubernetes/pull/28)) and **Dmitry Shurupov** ([PR #29](https://github.com/nubenetes/awesome-kubernetes/pull/29)).
- **Kubernetes Newsletters**: Initial curated list of ecosystem newsletters (Contribution by **Daniele Polencic** in [PR #31](https://github.com/nubenetes/awesome-kubernetes/pull/31)).

## [[1.6.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.6.0) - 2021-01-03

### Added
- **Post-Expansion Refinement**: Strategic consolidation of the massive 2020 "Great Expansion" surge.
- **Enterprise Patterns**: Inclusion of production-grade architectural blueprints for large-scale Kubernetes fleets.
- **Devtron Integration**: Added end-to-end Kubernetes delivery workflow (Contribution by **Arushi Shukla** in [PR #13](https://github.com/nubenetes/awesome-kubernetes/pull/13)).

## [[1.5.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.5.0) - 2020-05-01

### Added
- **The Great Expansion Peak**: Vertical surge in technical references (8k+ new entries).
- **Multi-Cloud Supremacy**: Significant expansion into AWS Architecture, Azure DevOps, and Google Cloud platform internals.
- **Serverless and Mesh Inception**: Dedicated sections for Istio, Linkerd, Knative, and emerging Cloud Native patterns.
- **O'Reilly Journey Navigation**: Overhaul of the navigation menu to follow a logical, architectural learning journey.
- **Developer Portals**: Added Backstage and emerging internal developer platform (IDP) tools.

## [[1.4.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.4.0) - 2020-01-20

### Added
- **Multi-Cloud Foundations**: Initial dedicated sections for AWS, Azure, and DigitalOcean.
- **Kubernetes Alternatives**: Inclusion of Nomad, Swarm, and other orchestrators for architectural comparison.

## [[1.3.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.3.0) - 2020-01-09

### Added
- **CI/CD Pillar**: Major expansion into Jenkins alternatives, GitOps (Flux/Argo), and modern pipeline tools.
- **Database Evolution**: Significant additions to NoSQL, NewSQL, and cloud-native database management.

## [[1.2.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.2.0) - 2019-12-09

### Added
- **Troubleshooting Masterclass**: Integration of learnk8s.io troubleshooting guides.

- **Famous Kubernetes Resources 2019**: First annual curation of the most impactful ecosystem assets.
- **External Validation**: Merged major OpenShift documentation improvements (Contribution by **Francesco Marchioni** in [PR #3](https://github.com/nubenetes/awesome-kubernetes/pull/3)).

## [[1.1.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.1.0) - 2019-04-28

### Added
- **Git Mastery**: Enhanced Git resources and README synchronization (Contribution by **Eyar Zilberman** in [PR #1](https://github.com/nubenetes/awesome-kubernetes/pull/1)).
- **MkDocs Integration**: First deployment of the structured MkDocs site for better web accessibility.

## [[1.0.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v1.0.0) - 2018-10-21

### Added
- **Munich Era Baseline**: Establishment of industrial-grade engineering standards from the Deloitte/BMW IT-Zentrum environment.
- **Architectural Relevance Protocol**: First implementation of the star (🌟) rating system to identify high-impact resources.
- **Core Technology Foundations**: Consolidated collection of Kubernetes, Terraform, Ansible, and Java Performance Optimization.

## [[0.5.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v0.5.0) - 2018-09-29

### Added
- **Documentation Foundations**: First implementation of `mkdocs.yml` and ReadTheDocs integration.
- **Thematic Segmentation**: Separation of content into specialized `.md` files (Docker, Ansible, Java).

## [[0.1.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v0.1.0) - 2018-09-24

### Added
- **Alpha Inception**: Initial repository creation and genesis of the Cloud Native knowledge base.
- **BMW IT-Zentrum Era**: Foundation of the Munich-based engineering standards and self-service developer platform patterns.
dation of the Munich-based engineering standards and self-service developer platform patterns.
