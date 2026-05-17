# Nubenetes Intelligent Curation: Meta-Instructions & Learning Roadmap

This file contains the accumulated instructions and long-term vision for the autonomous maintenance of Nubenetes.com. AI agents must consult this document in every iteration to ensure learning continuity.

## 🧠 Core Mandates

1.  **Information Preservation**: NEVER delete summaries, comments, or stars (🌟) accompanying links. The bot should only update the URL or reorganize the item's position, never delete the descriptive context.
2.  **Persistent Learning**: Use `src/memory/health_learning.json` to store knowledge about domains (anti-bot blocks, successful strategies) and navigation patterns.
3.  **Minimum Viable Quality (MVQ)**: For GitHub/GitLab repositories, the bot MUST check the last commit date. If the repository has had NO activity (commits) in more than **4 years**, it must receive a significantly lower `impact_score` and be deprioritized, even if the content remains technically relevant. This ensures Nubenetes stays fresh and focuses on maintained projects.
4.  **Style Guide (Descriptive Summaries)**: All injected summaries MUST follow a **Descriptive** style. Avoid generic "clickbait" or action-oriented phrases (e.g., "Check this out"). Instead, provide a clear, neutral description of what the resource contains, its scope, and why it is technically significant for the Kubernetes ecosystem.
5.  **Semantic Interlinking**: The bot should identify related categories for each resource. While the full entry is injected into the primary category, a short reference (*"See also: [Title](URL) in [Category]"*) should be added to up to two related categories to improve site navigation.
6.  **Visual Health Dashboard**: Every curation run MUST generate a local `report.html` (outside the repo) for visual validation of metrics, quality (MVQ), and AI decisions.
7.  **Total Resilience**: The workflow must be able to continue even if there are individual errors in link or file validations. Prioritize generating a result (PR) even if it is partial.
8.  **Repository Consolidation & Deep-Link Preservation**: In case of a failure (404) in a deep GitHub/GitLab link, the bot SHOULD try to validate the repository root before considering it dead. However, if a deep link (wiki, PR, tree) is ALIVE, it MUST be preserved. We prefer specific technical context in V1.
9.  **URL Expansion**: All shortened links (t.co, bit.ly, buff.ly, etc.) MUST be expanded to their original long version before being evaluated or injected. This ensures inventory homogeneity and improves global deduplication precision.
10. **Linguistic Diversity & Global Access**:
    - **Primary Language**: English is the official language of the Nubenetes ecosystem.
    - **Native Preservation (V1 Archive)**: For non-English resources (e.g., Spanish repositories, videos, or articles), the V1 description MUST remain in the **resource's native language** to preserve its original context and cater to native speakers.
    - **Global Synthesis (V2 Portal)**: To ensure 100% global discoverability, the V2 Elite summaries (`ai_summary`) MUST always be in **Professional English**, regardless of the source language.
    - **V1 Immutability**: For links already present in the V1 archive, AI agents MUST NOT overwrite manually curated titles, stars, or additional descriptive comments. Only broken URLs or missing metadata fields (like year/language) should be updated.
    - **Rich Metadata Enrichment**: AI agents SHOULD attempt to extract technical authors, video durations (YouTube), and reading times (Blogs) to populate high-density dimensions in the V2 portal.
    - **Safety Guard Validation**: Every automated PR MUST undergo syntax validation and a test MkDocs build to prevent broken rendering or security vulnerabilities in the final site.
    - **Explicit Language Tagging**: All non-English resources in the V2 Portal MUST be explicitly tagged (e.g., `[SPANISH CONTENT]`, `[FRENCH CONTENT]`) at the end of the entry to inform global users before they navigate.
    - **English-First Exceptions**: Global software projects (even if created by Spanish speakers) that use English as their primary interface should be curated entirely in English. Native preservation is for localized content like blogs, videos, and guides.
11. **Workflow-Config Synchronization**: The GitHub Actions curation workflow form (`agentic_cron.yml`) MUST remain perfectly synchronized with the curation sources configuration file (`data/curation_sources.yaml`). Any addition, removal, or renaming of topics/categories in the configuration file requires a corresponding update to the workflow's input fields (checkboxes) to ensure users can toggle those sources manually. This maintains consistency between data-driven sources and the UI trigger.
12. **V2 Elite Maintenance**: The Nubenetes V2 (Agentic Elite) edition is a derived view of the V1 archive. It is managed via the `src/v2_optimizer.py` script and stored in the `v2-docs/` directory. The `agentic_v2_builder.yml` workflow synchronizes V2 automatically whenever V1 (`docs/`) is updated (manually or via bot). Standard curation and cleaning workflows must always target the `docs/` directory as the primary source of truth.
13. **Detailed Logging for V2**: When running the V2 Optimizer, agents MUST use unbuffered logging and detailed output messages. If the optimizer returns '0 links kept', the agent MUST investigate the logs to determine if it was due to AI selection or a parsing/API error.
14. **Persistent V2 Caching**: The V2 Optimizer MUST use a persistent cache file (`data/centralized YAML inventory`) to store AI evaluations (year, quality, category). This is mandatory to minimize API costs and ensure execution speed across 15k+ links.
15. **GitHub Metadata Enrichment**: For all `github.com` resources, the bot MUST attempt to fetch real-time metadata (stars, last commit) using the GitHub API. This data must be included in the V2 rendering to provide current context.
16. **Resilient Link Health & Global Cleaning**: 
    - **Health Checks**: Every V2 generation and global cleaning cycle MUST perform asynchronous health checks using identity rotation (User-Agents) and multiple attempts (3x). 
    - **V1 Exhaustiveness**: The `IntelligentLinkChecker` operating on V1 MUST preserve all technically valid links regardless of their age. Deletion is strictly reserved for definitively invalid links (404s, dead redirects, etc.).
    - **V2 Elite Selection (MVQ)**: The `V2VisionEngine` MUST continue to apply the **Minimum Viable Quality (MVQ)** logic. GitHub repositories inactive for >4 years with low impact (stars < 30) are deprioritized or excluded ONLY from the V2 Elite edition to ensure freshness.
    - **Foundational Protection**: GitHub and 'Foundational' resources are exempt from automatic removal based on health, but may be flagged for review.
    - **Consolidation & Policy**: Truncation to root is strictly for dead links. Rules MUST follow [data/link_rules.yaml](data/link_rules.yaml).
17. **Unified Curation Chronology**: All curation workflows (V1 and V2) MUST utilize the same chronological and descriptive engine. 
    - **Extraction**: Every new link MUST attempt to extract a publication year (URL, metadata, or AI inference).
    - **Formatting**: New links MUST follow the format `  - **(YYYY)** [Title](URL) 🌟 - Description`. If year is 'N/A', the prefix is omitted.
    - **Elite Descriptions**: AI-generated descriptions MUST be professional, neutral, and focus on the technical value for a 2026 Cloud Architect.
18. **Automated Branch Hygiene**: To keep the repository clean and efficient, an automated cleanup MUST run every 15 days (1st and 15th) to delete remote branches already merged into `develop`. The branches `master`, `develop`, and `gh-pages` are strictly protected and MUST NEVER be deleted.
19. **V1/V2 Asset Integrity & Rendering**: 
    - **Source of Truth**: V1 (`docs/`) is the absolute source of truth for assets. V2 portal (`v2-docs/`) MUST NOT duplicate folders; it uses symlinks or relative paths.
    - **Rendering Fix (HTML in MD)**: All `<center>` tags MUST be defined as `<center markdown="1">` and followed by a mandatory blank line before and after the content. This ensures MkDocs processes the Markdown within the HTML block.
    - **Flat Asset Routing**: To avoid depth-related path breakage, both V1 (`mkdocs.yml`) and V2 (`v2-mkdocs.yml`) MUST have `use_directory_urls: false`. This ensures relative paths (e.g., `images/img.png`) resolve correctly regardless of the page depth.
20. **V2 Navigation Design**: The V2 top navigation bar MUST maintain a flat structure. All dimensions and categories must be top-level tabs in `v2-mkdocs.yml` to ensure direct discoverability and avoid nested groupings like "Categories".
21. **V2 Impact-Driven Sorting**: The V2 portal MUST prioritize **relevance (Impact) over dates** within sections to provide high-density technical value. Sorting MUST follow: 1. Stars/Relevance (DESC), 2. Year (DESC). The mission statement and descriptions MUST reflect this impact-driven synthesis.
22. **Unified Metadata Database (Local Storage & Persistence)**: All link metadata MUST be managed via the centralized [`data/inventory.yaml`](data/inventory.yaml).
    - **`inventory.yaml`**: The single source of truth for years, stars (0-5), descriptions, physical locations (`v1_locations`, `v2_locations`), and visual formatting. This eliminates the need for external mapping files (like the legacy `structure_map.yaml`) and ensures full lifecycle visibility.
    - **Platinum Lifecycle Metadata**: The inventory MUST track advanced engineering fields to empower context-aware automation:
        *   `content_hash`: SHA256 fingerprint to detect silent content updates.
        *   `health_score`: 0-100 reliability score based on check history (differentiates flaky from dead).
        *   `source_provenance`: Identifies the origin of the discovery (Twitter, RSS, Manual).
        *   `social_preview_url`: OpenGraph/Social images to enrich the V2 visual experience.
        *   `mentions_count`: Tracks resource popularity/rediscovery frequency.
    - **Persistence (MANDATORY)**: Every AI agent and workflow MUST load this file at startup, update it, and INJECT the modified YAML into the final PR payload if any change is detected. Discarding the database during a workflow run is a CRITICAL FAILURE.
    - **Exhaustive Initialization**: The system supports a `FORCE_FULL_CHECK` environment variable to bypass all caches (e.g., 21-day health cache) and force a full re-validation and re-enrichment of the entire 17k+ link archive.
    - **No Trusted Bypassing**: All domains, including high-trust ones (GitHub, Google, AWS), MUST be verified for link validity. Trusted status only grants a lower priority for aggressive scraper rotation, not a bypass for existence checks.
    - **Manual Priority**: AI agents MUST NOT overwrite existing manual descriptions or stars in the V1 archive files. Enrichment is strictly for the YAML database and the V2 portal.

23. **Canonical URL Normalization & Semantic Deduplication**: To prevent duplication and fragmented metadata, all agents MUST normalize URLs before any inventory operation.
    - **Tracking Stripping**: Systematically remove UTM parameters, social media trackers (X.com, LinkedIn), and URL fragments (except technical ones).
    - **Technical Preservation (V1)**: Normalization MUST **preserve line anchors** (e.g., `#L123`) and **respect URL path case-sensitivity**. Technical fragmentation is preferred over data loss for deep-links.
    - **Protocol Uniformity**: Standardize on `https://` whenever possible.
    - **Semantic Merge Logic**: If multiple URLs point to the same technical project (e.g., `user.github.io` vs `github.com/user/repo`), the agent MUST consolidate them into a single canonical reference, prioritizing the primary repository root.
    - **Metadata Merge**: Metadata from multiple sources for the same canonical URL MUST be merged, prioritizing the highest star rating and most recent date.
24. **Multi-Source Knowledge Discovery**: The discovery engine MUST be extensible beyond social media. 
    - **Engineering Blogs**: High-depth technical content from engineering blogs (via RSS/Atom) MUST be prioritized for high-impact dimensions.
    - **Source Diversity**: Monitor X.com, GitHub Trending, and RSS Feeds to maintain a balanced flow of technical news and architectural deep-dives.
25. **Tiered Health Monitoring Strategy (Quarterly Cycle)**: To balance resource efficiency with high reliability, the system operates on a staggered 3-month cycle:
    - **Mid-Quarter Critical Pulse**: High-priority assets (`[DE FACTO STANDARD]` and `[ENTERPRISE-STABLE]`) are verified every 3 months, offset from the full scan (e.g., Feb, May, Aug, Nov) to ensure essential tools remain online with high visibility.
    - **Quarterly Exhaustive Scan**: The complete 17,000+ link archive undergoes a full health audit every 3 months (Jan, Apr, Jul, Oct). This cycle manages massive cleanup, orphaned metadata pruning, and canonical updates.
    - **Margin for Review**: Workflows are orchestrated to ensure at least 45 days between a full scan and a critical pulse, allowing ample time for manual review and safety checks.
26. **Dynamic AI Model Discovery**: To remain at the cutting edge and ensure system stability, all agents MUST use the dynamic model discovery engine.
    - **Live Discovery**: Query the `models.list` API at runtime to identify actually available models for each key.
    - **Scoring & Ranking**: Prioritize models using the established 2026 hierarchy (Generation 3.x > 2.x > 1.x; Pro > Flash).
    - **Resilient Fallback**: Automatically transition between models and API keys upon encountering 404 (Unsupported) or 429 (Rate Limit) errors.

27. **Special Assets Management (V1 & V2)**: High-value files defined in [`data/special_assets.yaml`](data/special_assets.yaml) require specialized handling:
    - **High-Precision Reorganization (V1)**: These files MUST use nested semantic grouping (## and ###) to organize links without ever deleting technically valid content.
    - **Exhaustive Inclusion (V2)**: Unlike standard categories, V2 pages for Special Assets MUST include 100% of the ALIVE links from V1.
    - **AI Curation Discovery**: The discovery engine MUST actively search for new high-quality curation sources (e.g., "Awesome" repos) and suggest them for inclusion in `curation_sources.yaml`.
28. **Sophisticated V2 Knowledge Architecture**: The V2 Portal MUST be structured like an advanced O'Reilly technical book:
    - **Deep Hierarchical Classification**: Resources MUST be organized using the `hierarchy` metadata field (a list of up to 10 strings: Area > Topic > Subtopics). This structure is mandatory for both V1 reorganization and V2 generation to ensure perfect consistency.
    - **Location-Aware Automation**: Workflows MUST utilize the location metadata in the inventory (`v1_locations`, `v2_locations`) to perform surgical updates without redundant repository scans.
    - **Structural Intelligence Persistence**: All agents MUST store and reuse the `hierarchy` and location metadata in the centralized inventory. This ensures zero-cost structural updates and industrial-grade scalability.
    - **O'Reilly Learning Flow**: The organization must facilitate knowledge assimilation, moving from foundational theory to advanced engineering internals in a logical, ordered sequence.
    - **Dynamic Indexing**: Every V2 page MUST include a Table of Contents (TOC) with clickable anchors for all technical sub-sections.
    - **AI Dimension Naming**: Prioritize industry-standard terms (e.g., "AI and Artificial Intelligence" instead of internal jargon) for top-level navigation.
    - **Content Extraction**: High-value sub-topics may be extracted into dedicated documents (e.g., "Microservices" content extracted from `introduction.md` into `microservices.md`) to maintain high-density focus.

29. **TOC & Structural Exceptions**: Certain files (configuration-heavy or technical tables like `mkdocs.md` or `matrix-table.md`) are exempt from TOC and deep-hierarchy requirements. These exceptions MUST be respected by all agents to avoid unnecessary structural clutter in non-navigational files as defined in [`data/link_rules.yaml`](data/link_rules.yaml).

30. **Universal Title and TOC Standards**: To ensure robust cross-platform rendering and prevent broken internal links:
    - **No Emojis or Special Characters**: Section titles (H2-H6) and Table of Contents (TOC) entries MUST NOT contain emojis or special symbols.
    - **No Ampersands**: The ampersand character (`&`) MUST be replaced with "and" in all titles and TOCs.
    - **Lowercase Anchors**: All Markdown anchors MUST use strictly lowercase slugs without special characters.

## 🛠️ Structural Evolution & Navigation
...
*   **No Link Limits**: There are NO hard limits on the number of links per page or per section (##/###). Nubenetes is built to host thousands of references.
*   **TOC Consistency**: Every `.md` page (including the main index `docs/index.md`) MUST maintain an internal Table of Contents (TOC) at the beginning. This TOC must include all sections (##) and subsections (###) nested correctly using a numbered list format with working anchors.
*   **Relative References & Anchors**:
    *   **Internal**: Use simplified lowercase slugs for anchors (remove special characters, replace spaces with hyphens).
    *   **External/Cross-page**: Ensure references between different `.md` files are correct and up-to-date.
*   **Main Index Maintenance (`docs/index.md`)**:
    *   `docs/index.md` is the landing page for nubenetes.com and the primary entry point. It MUST be updated whenever a new page is added or a major category is renamed.
    *   **Top Links Preservation**: The "Motivation" section in `docs/index.md` contains highly relevant links. These MUST be preserved even if they are duplicated in other thematic pages. The AI should prioritize keeping this index curated and high-signal.
*   **Intelligent Internal Reorganization**:
    *   **No File Splitting**: Do NOT create new `.md` files unless strictly necessary for a major new theme. Prefer creating new sub-sections (## or ###) within existing files to maintain order.
    *   **Semantic Polish**: When a section becomes excessively flat, the AI should propose and implement a reorganization into logical sub-sections purely to improve readability and classification, without restricting the volume of content.
*   **Navigation Integrity**: Every structural change must be reflected in:
    *   `mkdocs.yml` (Navigation menu).
    *   `v2-mkdocs.yml` (V2 Navigation menu).
    *   `docs/index.md` (Main Table of Contents).
    *   The internal TOC of the modified page.
*   **Orphan Curation**: Periodically audit the `docs/` folder to find unlinked files and integrate them into the navigation based on their topic.

## 📊 Mermaid Diagram Best Practices

To ensure robust rendering across GitHub, VSCode, and MkDocs, follow these standards when creating or modifying Mermaid diagrams:

1.  **Node Label Quoting**: ALWAYS wrap node labels in double quotes (e.g., `A["Label Text"]`) if they contain spaces, special characters (parentheses, brackets, dots), or reserved words. This prevents parse errors in more restrictive environments.
2.  **Explicit Direction**: Use `graph TD` (Top-Down) for deep hierarchies and `graph LR` (Left-to-Right) for flat process flows to optimize readability and prevent horizontal clipping.
3.  **Label Length**: Keep labels concise (under 25 characters). If a longer description is needed, use a tooltip or sub-text.
4.  **Syntax Validation**: Before committing, verify the syntax using a Mermaid previewer. Common pitfalls include:
    *   Unescaped brackets `[` or `]` inside labels.
    *   Missing semicolons or newlines between node definitions.
    *   Recursive loops without proper termination.
5.  **Integration with MkDocs**: Ensure `pymdownx.superfences` is configured in `mkdocs.yml` to support Mermaid blocks within Markdown.

## 🛡️ Repository Policies & Branch Protection

To maintain the integrity of the archive and ensure the AI agents operate correctly:

1.  **Branch Hierarchy**:
    *   `master`: Read-only for contributors/bots. Restricted to repository owner only.
    *   `develop`: The only valid target for Pull Requests.
2.  **Pull Request Policy**:
    *   AI agents MUST always target `develop`.
    *   Manual contributions (human PRs) targeting `master` must be automatically or manually redirected to `develop`.
3.  **Owner-Only Merges**: Only the repository owner has the authority to merge `develop` into `master` after verifying the visual health dashboard and metrics.

## 📝 README Synchronization & Maintenance Protocols

The `README.md` is the primary entry point for Nubenetes and must accurately reflect the state of both the **V1 (Exhaustive)** and **V2 (Elite)** editions. AI agents and contributors MUST follow these protocols:

### 1. Mandatory Updates on `develop` Branch
Before any Pull Request is merged from `develop` to `master`, the `README.md` must be audited and updated to reflect the latest changes. This is critical for maintaining the "Source of Truth" status.

### 2. Metric Recalculation
Whenever a significant curation cycle (automatic or manual) is completed:
*   **Link Counts:** Update the "Heart of Nubenetes" table with the current total link count and specialized page count.
*   **Top Categories:** Recalculate the density of the top 10 categories.
*   **Historical Growth:** Add/update the monthly surge rows in the "2026: The Agentic Monthly Surge" table.
*   **Reference Estimates:** Use the established ratio (~4.13 links/commit) to estimate new reference growth if exact numbers aren't extracted by the bot.

### 3. Visual & Diagram Sync
*   **Mermaid Charts:** If new top-level categories are created or existing ones grow significantly, update the "Major Ecosystem Pillars" and "Specialized Sub-ecosystems" pie charts.
*   **Architecture Flow:** If the Agentic Stack or the deployment lifecycle changes (e.g., new workflows, different dependencies), the corresponding Mermaid diagrams MUST be updated immediately.
*   **Robustness:** Follow the "Mermaid Diagram Best Practices" (node quoting, explicit direction) as defined in this document.

### 4. V1 vs V2 Alignment
*   Ensure any changes to the `V2VisionEngine` or the elite selection criteria are reflected in the "Dual-Edition Architecture" section.
*   Update the "Comparison Matrix" if the technical differences between V1 and V2 evolve.

### 5. Automation vs Manual Intervention
*   **Automated Updates:** The Agentic Bot should ideally include a step to refresh these metrics in its curation PRs.
*   **Manual Fallback:** If a manual update is performed (emergency fixes, structural changes), the human/AI agent is responsible for manually running the metric extraction scripts and updating the `README.md` accordingly.
*   **Algorithm-README Sync**: Whenever the AI curation logic, model tiering, or the extraction algorithm is modified (e.g., `src/gemini_utils.py` or `src/v2_optimizer.py`), the `README.md` MUST be updated to reflect these technical changes in the "Agentic Stack" and "Architectural Shift" sections.
*   **Hierarchical README Maintenance**: Whenever `README.md` is modified, the Table of Contents (TOC) MUST be updated to reflect all changes in sections (H2) and subsections (H3). All titles in the document MUST include hierarchical numbering (e.g., "1. Section", "1.1. Subsection") perfectly synchronized with the TOC.
*   **Universal Title Standards**: Emojis and ampersands (&) MUST NOT be used in any section titles or Table of Contents. Ampersands MUST be replaced with "and". All anchors MUST be lowercase slugs (Mandate 30).
*   **Asset Inventory and Configuration**: The `README.md` MUST maintain a "Repository Inventory and Configuration" section (Section 13) that provides an exhaustive list of all key configuration files, centralized metadata databases, autonomous workflows, and core source code files. Each item MUST be linked using a relative Markdown path (e.g., `[file.yaml](data/file.yaml)`) to facilitate direct navigation.
*   **Source Transparency**: Specific curation sources (e.g., X.com accounts) MUST be documented in the "Agentic AI Engine" section of the `README.md`. Any addition or removal of primary sources in `data/curation_sources.yaml` requires a corresponding update to the documentation.

## 🚀 Block Evasion Strategies

The bot must rotate between profiles to avoid detection:
1.  **Desktop/Google**: Standard desktop request.
2.  **Mobile/Twitter**: Mobile request with Twitter Referer (high success rate).
3.  **Playwright/LinkedIn**: Real navigation with JS enabled.
4.  **Firefox/Reddit**: Alternative desktop profile.

## 📈 Learning Diary (Improvement History)

*   **May 2026**: Initial implementation of the autonomous engine with Playwright and GitHub API.
*   **May 2026**: Added Multidimensional Evasion system (5 attempts, profile rotation).
*   **May 2026**: Creation of `AgenticCurator` for navigation audit and repository consolidation.
*   **May 2026**: Generation of PRs with visual analytics (Mermaid) and Health Matrix.
*   **May 2026**: Implementation of Backup-based Curation (JSON/MD) to avoid X.com blocks.
*   **May 2026**: Implementation of multi-source curation and category-based filtering in GitHub Workflow.
*   **May 2026**: Introduction of **Nubenetes V2 (Agentic Elite)** architecture. Implemented persistent `v2-docs/` storage, the `v2_optimizer.py` engine for 2026 standard filtering, and a dual-deployment pipeline to host both V1 (Exhaustive) and V2 (Elite) versions in parallel.
*   **May 2026**: **V1 Restoration & V2 Optimization**:
    - **V1 Integrity Restored**: Recovered all V1 files in `docs/` to ensure original descriptive content and images are preserved.
    - **V2 Navigation Fixed**: Converted V2 top bar to a flat structure for better UX and link stability.
    - **Relative Asset Routing**: Updated all V2 image and configuration paths to point relatively to `../docs/` to avoid asset duplication.
    - **Rendering & Path Resolution**: Implemented `<center markdown="1">` and `use_directory_urls: false` across V1 and V2 to resolve persistent image path breakage and ensure proper Markdown rendering within HTML tags.
    - **Optimizer Alignment**: Hardened `src/v2_optimizer.py` to enforce these architectural rules (flat navigation, relative paths, and resilient V1 content extraction).
    - **Incremental Elite Engine**: Implemented a sophisticated V2 sync strategy using `data/centralized YAML inventory`.
        - **Automatic Detection**: The `agentic_v2_builder.yml` workflow now triggers automatically whenever `docs/` changes or after a curation run.
        - **Cost Efficiency**: Only NEW links from V1 are sent to Gemini. Existing links use cached AI evaluations but are locally "upgraded" with real-time GitHub metadata (stars/dates) and dynamic maturity tagging.
        - **Maturity Taxonomy**: Replaced generic labels with a professional 5-tier system (`[DE FACTO STANDARD]`, `[ENTERPRISE-STABLE]`, `[EMERGING]`, `[LEGACY]`, `[GUIDE]`) explained in the V2 Index.
        - **Mandatory Descriptions**: Every resource in V2 MUST have a description. If the V1 source is missing one, the Optimizer uses Gemini to generate a professional 1-2 sentence summary and caches it.
        - **Manual Control**: The workflow supports a `force_reevaluate` flag for full architectural refreshes.
*   **May 2026**: **V2 UI Hardening & Unified Curation Engine**:
    - **Highlighting Fixed**: Enabled `pymdownx.mark` in V2 and implemented strategic highlighting (`==text==`) for top-tier/Standard resources.
    - **Clean Chronology**: Refined V1 and V2 engines to hide `(N/A)` dates, providing a cleaner UI.
    - **Impact-Driven Synthesis**: Shifted V2 mission from pure "chronological clarity" to "impact-driven synthesis", prioritizing Stars/Impact over dates while maintaining chronological data.
    - **Relevance-First Sorting**: Updated V2 logic to prioritize Stars/Impact over dates within dimension categories.
    - **Unified Metadata Engine**: Integrated V2's year extraction and professional description logic into the main V1 curation workflow (`src/agentic_curator.py`).
    - **Advanced MVQ Cleaning**: Upgraded the `IntelligentLinkCleaner` to use V2's MVQ logic (GitHub activity checks) and unbuffered real-time logging.
    - **Smart Batching (Performance Fix)**: AI enrichment MUST exclusively use batch processing (e.g., 10 links per prompt). Individual AI calls within large loops are strictly forbidden to prevent 429 rate limit deadlocks and workflow hangs.
    - **Maturity Audit Transparency**: All curation workflows MUST maintain the **Maturity Audit Log** (`v2-docs/audit-log.md`) to document technical promotions, reclassifications, and AI-driven curation decisions.
    - **Database-First Resilience**: Implemented a global YAML inventory as the system's "Persistent Memory," reducing AI costs by >90% through metadata reuse.
    - **Technical Immutability (V1)**: Established strict preservation rules for human-curated titles, stars, and deep-links to ensure AI optimization never sacrifices technical depth.
    - **Self-Healing Infrastructure**: Added automatic GitHub branch recovery (master -> main) and parked domain detection to rescue broken links and eliminate expired content.
    *   **AI Observability & Transparency (May 2026)**:
        - **Session Tracking**: Every AI call MUST be tracked via `SESSION_TRACKER` to record model usage and key health.
        - **Infrastructure Reporting**: All curation PRs MUST include the `Intelligence Report` to provide transparency on models used (Pro vs Flash) and API key identities (Identity A/B).
        - **Dynamic Discovery**: Agents MUST utilize the dynamic discovery engine to automatically adopt the newest Gemini models and rotate keys upon reaching quotas.
    - **Engineering Blog Discovery**: Integrated RSS/Atom ingestion into the curation engine to source high-depth architectural content directly from top-tier technical companies.

    - **AI and Artificial Intelligence Dimension**: Renamed from "Intelligent Control Plane" for better industry alignment.
    - **Zero-to-Hero Grouping**: Implemented complexity-based levels (Fundamentals to Architect) for high-density learning paths.
    - **Special Assets Logic**: Integrated data/special_assets.yaml to ensure exhaustive preservation of critical lists (Introduction, YAML, Awesome repos).
