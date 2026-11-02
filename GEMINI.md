# Nubenetes Intelligent Curation: Meta-Instructions & Learning Roadmap

This file contains the accumulated instructions and long-term vision for the autonomous maintenance of Nubenetes.com. AI agents must consult this document in every iteration to ensure learning continuity.

## 🧠 Core Mandates

1.  **Information Preservation**: NEVER delete summaries, comments, or stars (🌟) accompanying links. The bot should only update the URL or reorganize the item's position, never delete the descriptive context.
2.  **Persistent Learning**: Use `src/memory/health_learning.json` to store knowledge about domains (anti-bot blocks, successful strategies) and navigation patterns.
3.  **Minimum Viable Quality (MVQ)**: For GitHub/GitLab repositories, the bot MUST check the last commit date. If the repository has had NO activity (commits) in more than **4 years**, it must receive a significantly lower `impact_score` and be deprioritized, even if the content remains technically relevant. This ensures Nubenetes stays fresh and focuses on maintained projects.
4.  **Style Guide (High-Density Summaries)**: All injected summaries MUST follow a **High-Density Descriptive** style. Avoid generic "clickbait". Instead, apply the **Double-Evidence Synthesis Protocol**: contrast 'Curator Insight' with 'Live Grounding' (MCP) to provide a neutral, professional description of architectural value, key features, and technical significance. Summaries should be 2-5 sentences long and support multi-line Markdown formatting (bullet points).
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
12. **V2 Elite Maintenance**: The Nubenetes V2 (Agentic Elite) edition is a derived view of the V1 archive. It is managed via the `src/v2_optimizer.py` script and stored in the `v2-docs/` directory.
    - **Surgical Cleanup**: The optimizer MUST perform surgical garbage collection in `v2-docs/` after each run, deleting only orphaned files that are no longer part of the current site architecture.
    - **Synchronization**: V2 is updated automatically whenever V1 (`docs/`) changes. Standard curation always targets V1 as the source of truth.
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
    - **Flat Asset Routing (SEO-Friendly)**: To prioritize SEO and clean URLs, both V1 (`mkdocs.yml`) and V2 (`v2-mkdocs.yml`) MUST have `use_directory_urls: true`. This ensures clean directory URLs (e.g., `/kubernetes/` instead of `/kubernetes.html`). Standardize on root-relative paths for assets and `<center markdown="1">` for HTML blocks to prevent any path breakages across directory levels.
20. **V2 Navigation Design**: The V2 top navigation bar MUST maintain a flat structure. All dimensions and categories must be top-level tabs in `v2-mkdocs.yml` to ensure direct discoverability and avoid nested groupings like "Categories".
21. **V2 Impact-Driven Sorting**: The V2 portal MUST prioritize **relevance (Impact) over dates** within sections to provide high-density technical value. Sorting MUST follow: 1. Stars/Relevance (DESC), 2. Year (DESC). The mission statement and descriptions MUST reflect this impact-driven synthesis.
22. **Unified Metadata Database (Fast-Track Single-File)**: All link metadata MUST be managed via the centralized file [`data/inventory.yaml`](data/inventory.yaml).
    - **Monolithic Efficiency**: To maintain simplicity and speed in the "Fast-Track" mode, the inventory is kept as a single, high-density YAML file. This avoids the overhead of sharding and matrix management for standard runs.
    - **Scalable Multiline Support**: The inventory utilizes **YAML Block Scalars (`|`)** for fields like `ai_summary`, enabling the storage of complex technical summaries with paragraphs and bullet points without breaking the database structure.
    - **Platinum Lifecycle Metadata**: The inventory MUST track advanced engineering fields to empower context-aware automation:
        *   `content_hash`: SHA256 fingerprint to detect silent content updates.
        *   `health_score`: 0-100 reliability score based on check history (differentiates flaky from dead).
        *   `source_provenance`: Identifies the origin of the discovery (Twitter, RSS, Manual).
        *   `social_preview_url`: OpenGraph/Social images to enrich the V2 visual experience.
        *   `mentions_count`: Tracks resource popularity/rediscovery frequency.
        *   `addition_method`: Tracks the resource addition origin ('manual' or 'automatic') to facilitate scaling metrics.
    - **Persistence (MANDATORY)**: Every AI agent and workflow MUST load this file at startup, update it, and INJECT the modified YAML into the final PR payload if any change is detected. Discarding the database during a workflow run is a CRITICAL FAILURE.
    - **Exhaustive Initialization**: The system supports a `FORCE_FULL_CHECK` environment variable to bypass all caches (e.g., 21-day health cache) and force a full re-validation and re-enrichment of the entire 17k+ link archive.
    - **No Trusted Bypassing**: All domains, including high-trust ones (GitHub, Google, AWS), MUST be verified for link validity. Trusted status only grants a lower priority for aggressive scraper rotation, not a bypass for existence checks.
    - **URL Protocol Integrity**: All URLs MUST use the complete and correct protocol prefix (`https://` or `http://`). AI agents MUST ensure that automated edits or mass cleanup tasks NEVER corrupt the protocol (e.g., by reducing `https://` to `https:/`).
    - **Manual Priority**: AI agents MUST NOT overwrite existing manual descriptions or stars in the V1 archive files. Enrichment is strictly for the YAML database and the V2 portal.

23. **YouTube Mosaic Management & Dual Layout Mandate**: The YouTube channels visual mosaic in `docs/index.md` (V1) and `v2-docs/index.md` (V2) must be generated dynamically from the centralized metadata database `data/inventory.yaml` (using the `youtube_mosaic` metadata block). The layouts for V1 and V2 must remain strictly distinct to satisfy the dual-edition mandate:
    - **V1 Exhaustive Layout**: Must be rendered as a single flat, historically ordered sequence of channel logos (11 per row) using simple inline width styling (`{: style="width:7%"}`). Newly discovered channels must be appended at the end of the flat list (ordered using the `youtube_mosaic.order_v1` field).
    - **V2 Elite Layout**: Must be rendered as an advanced categorized dashboard grouped into custom border-outlined card containers with neon colors corresponding to technical dimensions, optimized dimensions (`width: 48px; height: 48px`), and class hooks (`.channel-logo`) (ordered using the `youtube_mosaic.order_v2` field).
    - **Automation & Persistence**: The automated Publisher and Optimizer bot workflows must execute `src/reorganize_mosaic.py` to regenerate both visual blocks from the database during every pipeline run, ensuring the layout difference persists over the entire lifecycle.

24. **Canonical URL Normalization & Semantic Deduplication**: To prevent duplication and fragmented metadata, all agents MUST normalize URLs before any inventory operation.
    - **Tracking Stripping**: Systematically remove UTM parameters, social media trackers (X.com, LinkedIn), and URL fragments (except technical ones).
    - **Technical Preservation (V1)**: Normalization MUST **preserve line anchors** (e.g., `#L123`) and **respect URL path case-sensitivity**. Technical fragmentation is preferred over data loss for deep-links.
    - **Protocol Uniformity**: Standardize on `https://` whenever possible.
    - **Semantic Merge Logic**: If multiple URLs point to the same technical project (e.g., `user.github.io` vs `github.com/user/repo`), the agent MUST consolidate them into a single canonical reference, prioritizing the primary repository root.
    - **Metadata Merge**: Metadata from multiple sources for the same canonical URL MUST be merged, prioritizing the highest star rating and most recent date.

25. **YouTube Content Enrichment**: Featured videos in the V2 Elite Video Hub and ALL technical YouTube links in curation pipelines MUST be enriched using real-time metadata (titles and descriptions) fetched directly from the source. This raw context MUST be synthesized by AI into high-density "Curator Insights" to ensure that Nubenetes reflects the original technical intent of the authors.

26. **Multi-Source Knowledge Discovery**: The discovery engine MUST be extensible beyond social media. 
    - **Engineering Blogs**: High-depth technical content from engineering blogs (via RSS/Atom) MUST be prioritized for high-impact dimensions.
    - **Source Diversity**: Monitor X.com, GitHub Trending, and RSS Feeds to maintain a balanced flow of technical news and architectural deep-dives.

27. **Tiered Health Monitoring & Incremental Self-Correction**: To balance resource efficiency with high reliability, the system operates on a staggered 3-month cycle:
    - **Incremental Self-Correction (Standard Runs)**: Agents MUST autonomously identify "suspicious" resources in the database (e.g., deep technical links that have defaulted to generic homepages). During standard maintenance cycles, these links MUST be prioritized for re-validation and the **Universal Rescue Protocol**, repairing past precision errors without requiring exhaustive re-runs.
    - **Mid-Quarter Critical Pulse**: High-priority assets (`[DE FACTO STANDARD]` and `[ENTERPRISE-STABLE]`) are verified every 3 months, offset from the full scan.
    - **Quarterly Exhaustive Scan**: The complete 17,000+ link archive undergoes a full health audit every 3 months (Jan, Apr, Jul, Oct).
    - **Margin for Review**: Workflows are orchestrated to ensure at least 45 days between a full scan and a critical pulse, allowing ample time for manual review and safety checks.

28. **Dynamic AI Model Discovery & Resilient Grounding**: To remain at the cutting edge and ensure system stability:
    - **Live Discovery**: Query the `models.list` API at runtime to identify actually available models for each key.
    - **Real-time Web Grounding (MCP-Style)**: Agents MUST use **Google Search Grounding** for high-fidelity tasks, including link rescue and tool maturity verification. This provides a live data filter that ensures architectural decisions are based on the current state of the technical web.
    - **Resilient Fallback**: Automatically transition between models and API keys upon encountering 404 (Unsupported) or 429 (Rate Limit) errors.

29. **Special Assets Management (V1 & V2)**: High-value files defined in [`data/special_assets.yaml`](data/special_assets.yaml) require specialized handling:
    - **VIP Status Inheritance**: During project consolidation (semantic dedup), if any link instance originates from a Special Asset, the consolidated entry MUST inherit the protected `is_special` status.
    - **High-Precision Reorganization (V1)**: These files MUST use nested semantic grouping (## and ###) to organize links without ever deleting technically valid content.
    - **Exhaustive Inclusion (V2)**: Unlike standard categories, V2 pages for Special Assets MUST include 100% of the ALIVE links from V1, bypassing standard impact filters.
    - **AI Curation Discovery (Autonomous)**: The discovery engine MUST periodically use **Grounding/MCP** to identify new high-quality curation sources (e.g., emerging "Awesome" repos, engineering blogs) and suggest them for inclusion in `curation_sources.yaml`.

30. **Sophisticated V2 Knowledge Architecture & V1 Structural Stability**: The ecosystem maintains a strict separation of architectural philosophies between editions:
    - **V1 (Archive Stability)**: The V1 archive (`docs/`) prioritized human curation and historical continuity. AI agents MUST NOT perform aggressive structural reorganization, section rebuilding, or automated TOC reconstruction in V1. Injection of new links must follow a "minimal disruption" pattern, placing resources within existing categories without altering the established manual structure.
    - **V2 (O'Reilly Knowledge Flow)**: The V2 Portal (`v2-docs/`) is the innovation layer. It MUST be structured like an advanced technical book:
        *   **Deep Hierarchical Classification**: Resources are organized using the `hierarchy` field (Area > Topic > Subtopics). This is mandatory for V2 generation.
        *   **O'Reilly Learning Flow**: Organization must move from foundational theory to advanced engineering internals in a logical, ordered sequence.
        *   **Dynamic Indexing**: Every V2 page MUST include an automated Table of Contents (TOC) with clickable anchors for all sub-sections.
        *   **Elite Video Hub**: A dedicated dimension for high-impact technical video content, managed by `src/v2_video_portal.py`, with categorized architectural summaries and optimized lazy-loading embeds.
    - **Location-Aware Automation**: Workflows utilize location metadata (`v1_locations`, `v2_locations`) to perform surgical updates. V1 locations are considered "Fixed Anchors," while V2 locations are "Dynamic Clusters."

31. **TOC & Structural Exceptions**: Certain files (configuration-heavy or technical tables like `mkdocs.md` or `matrix-table.md`) are exempt from TOC and deep-hierarchy requirements. These exceptions MUST be respected by all agents to avoid unnecessary structural clutter in non-navigational files as defined in [`data/link_rules.yaml`](data/link_rules.yaml).

32. **Universal Title and TOC Standards**: To ensure robust cross-platform rendering and prevent broken internal links:
    - **No Emojis or Special Characters**: Section titles (H2-H6) and Table of Contents (TOC) entries MUST NOT contain emojis or special symbols.
    - **No Ampersands**: The ampersand character (`&`) MUST be replaced with "and" in all titles and TOCs.
    - **Lowercase Anchors**: All Markdown anchors MUST use strictly lowercase slugs without special characters.

33. **Markdown Standards and Linting Integrity**: To ensure zero-failure in CI/CD pipelines and pristine rendering:
    - **Fenced Code Language**: ALL fenced code blocks MUST have a language specified (e.g., \`\`\`yaml, \`\`\`bash). Use \`\`\`text as the default for logs or plain citations.
    - **No Spaces in Links**: Link text MUST NOT contain leading or trailing spaces within brackets (e.g., use \`[Link]\`, NEVER \`[ Link ]\`). Line breaks inside link text are strictly forbidden.
    - **Table Column Integrity**: Every row in a Markdown table MUST contain the exact number of columns defined in the header. Use \`N/A\` or empty cells \`| |\` to maintain the count; never leave rows "hanging" or truncated.
    - **Image Alt-Text**: All images MUST include a descriptive \`alt\` attribute for accessibility and linter compliance.
    - **Heading Precision**: Headings MUST start at the beginning of the line (no indentation) and MUST have exactly one space between the \`#\` symbols and the title text.
    - **Link Syntax**: Always use standard \`[Text](URL)\` syntax. Verify that brackets and parentheses are not reversed or malformed.

34. **README Cost Analysis (EUR First)**: To align with European operational standards:
    - **Primary Currency**: All cost projections, tables, and analysis in `README.md` (Section 7) MUST use **Euros (€)** as the primary currency.
    - **Conversion Policy**: If USD values are provided for technical reference, they MUST be accompanied by their EUR equivalent using a current market estimate (e.g., 1 USD ≈ 0.92 EUR).
    - **Metric Precision**: Maintain at least two decimal places for EUR values to ensure financial accuracy.

35. **Content-URL Precision Standard**: To prevent misinformation and maintain high-density technical value:
    - **Generic Redirect Detection**: If a technical deep-link redirects to a generic landing page, it is flagged as a precision failure.
    - **Deep Link Rescue (Universal)**: For ALL technical resources, the bot MUST NOT delete the link immediately. Instead, it SHOULD attempt to "rescue" it using the technical title, full V1 description, and **Real-time Web Grounding** (MCP) for high-precision context search.
    - **High-Value Preservation (The 'Review Required' Rule)**: Resources identified as **High-Value** (visually highlighted with bold/highlight, marked with 🌟 stars, or featuring dense technical descriptions) MUST NEVER be automatically deleted. If rescue attempts fail, these links MUST be marked as `status: review_required` and preserved in the archive for manual verification.
    - **Authoritative Preservation**: If a specific technical equivalent is found (e.g., Nginx to F5 migration), the URL MUST be updated to the new specific path.

36. **Social Proof & Reputation Filter**: To eliminate "vaporware" and unstable tools:
    - **Community Vetting**: Curation agents MUST use **Real-time Web Grounding** to cross-reference new tools with community platforms (Reddit, Hacker News).
    - **Reputation Penalty**: If a project is widely reported as abandoned, unstable, or misleading, the agent MUST apply a significant impact penalty or reject the resource entirely.
    - **Reputation Metadata**: The inventory SHOULD track `reputation_status` (Vetted/Suspicious) and a brief `reputation_summary`.

37. **License & Compliance Guard**: To protect the Open Source integrity of the Nubenetes ecosystem:
    - **License Monitoring**: Health agents MUST monitor the `LICENSE` field for all repository resources (GitHub/GitLab).
    - **Non-Free Transition Alert**: If a project transitions from a permissive license (e.g., Apache 2.0, MIT) to a non-free or restrictive license (e.g., BSL, SSPL), the resource MUST be flagged as `status: review_required`.
    - **Impact Adjustment**: Projects that move away from Open Source standards MUST receive an automatic star reduction and be deprioritized in the V2 portal to favor truly open alternatives.

38. **V2 Elite Visual Standards**: All V2 content generation MUST apply the following visual hierarchy:
    - **Platinum Resources (5 stars)**: Use yellow highlighting for the link text (e.g., `==[Link Title]==`).
    - **Gold Resources (4 stars)**: Use bold formatting for the link text (e.g., `**[Link Title]**`).
    - **Multi-Dimensional Tagging**: Every resource in V2 SHOULD have one or more maturity/type tags.
    - **Minimalist Inline Summaries**: High-density summaries MUST be rendered using a **native HTML5 `<details>` element with `inline-block` behavior** (appearing as a "Deep-Dive" tag) to maximize vertical density while providing depth on demand.
    - **Star Consistency**: Maintain the 1-5 star scale for technical impact. Resources with 0 stars are considered "Standard References" and do not display a star prefix/suffix in the V2 UI.

39. **V2 Semantic Connectivity**: All V2 content generation MUST implement the **Semantic Cross-Linking Engine**. AI agents must autonomously identify related architectural patterns within the same strategic dimension and inject "💡 Explore Related" navigation blocks at the end of sections to facilitate a connected knowledge graph.

40. **Industrial Learning Flow**: V2 documents MUST follow an O'Reilly-style technical progression. Organization within sections must move from foundational theory and standards to advanced implementation details and emerging patterns.

41. **Robust AI-Driven Multi-Tagging (Multi-Agent Protocol)**: Every resource evaluation MUST utilize a **Multi-Agent Analyst-Auditor workflow** with **Real-time Web Grounding (MCP)**:
    - **Analyst Role**: Initial technical classification and initial evidence synthesis.
    - **Auditor Role (Grounded)**: Selective verification of high-impact candidates ([DE FACTO STANDARD] or [ENTERPRISE-STABLE]) using Pro models to search for community reputation and stability. AI-assigned tags take precedence over static rules. Fallback to `[COMMUNITY-TOOL]` is only permitted after exhaustive classification failure.

42. **V2 Index Branding Protection**: The header and vision block of the V2 Elite Portal MUST NOT be modified. The title MUST remain "Nubenetes Elite Portal (V2) | Awesome Kubernetes & Cloud [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)" and the abstract MUST use the "The High-Density Vision" text as hardcoded in the optimizer logic to maintain industrial-grade branding.

43. **V2 Index Visual Standard (Automotive Roots)**: The Nubenetes V2 Elite Portal index MUST feature a centered banner image linked to `kubernetes.io`, followed by the Horatio Nelson Jackson quote and the specific automotive container metaphor image (`images/container_with_cars_v2.png`). This image is a manually provided asset and MUST NOT be regenerated by AI to ensure the preservation of the project's established visual identity.

44. **V2 Index Footer Standard**: The V2 index MUST always conclude with the **Maturity Taxonomy** and **Technical Impact** explanation tables. These sections define the industrial-grade classification and visual code (Highlighting/Bold) used throughout the Elite portal and must be preserved across all automated regenerations.

45. **V2 Navigation Standard**: The top navigation bar in `v2-mkdocs.yml` MUST feature the "Agentic Elite Portal" link as the primary entry point to ensure professional consistency across the platform.

46. **Version Control & Changelog Standard**: All significant milestones and architectural shifts MUST be versioned using **Semantic Versioning (SemVer)** and documented in [`CHANGELOG.md`](CHANGELOG.md) following the "Keep a Changelog" standard. This ensures full traceability of the ecosystem's evolution from historical archive to agentic portal.

47. **On-Demand Metadata Enrichment (V2)**: The V2 generation engine MUST support a manual `ENRICH_METADATA` flag. When active, the bot MUST fetch real-time GitHub stars and license data for all repositories missing this metadata in the inventory. This ensures that [DE FACTO STANDARD] and [ENTERPRISE-STABLE] tags are assigned based on current industry momentum rather than stale or missing cache data.

48. **Agentic Presubmit Safeguards (PR Guardian)**: All PRs to `develop` MUST be analyzed by the `PR Guardian` AI agent to ensure compliance with Nubenetes standards (No emojis in headers, valid Markdown, correct URL normalization, high-density descriptions).

49. **Resilient Quota Management (Circuit Breakers)**: AI workflows MUST implement circuit breaker logic (Exit Code 42) to gracefully pause processing and disable the workflow when API quotas (e.g., 429 Too Many Requests) are exhausted, preventing infinite loop failures.

50. **Markdown Linting Continuity**: All files in `docs/` and `v2-docs/` MUST pass the automated `markdownlint` validation to ensure pristine HTML rendering within MkDocs.

51. **Zero-Redundancy Agentic Pipeline (Performance Standard)**: To maintain the **30-minute execution standard**, the V2 ecosystem utilizes a decoupled micro-workflow architecture:
    - **V2 Health Monitor**: Weekly network validation of the link archive.
    - **V2 Metadata Engine**: Bi-weekly extraction of GitHub stars and licenses.
    - **V2 AI Curator**: On-demand deep architectural analysis and hierarchical indexing.
    - **V2 Publisher**: Fast-track rendering of the Elite portal from pre-enriched metadata.
    - **Linear Knowledge Flow**: The workflow follows a strict sequence: 1. Health/Metadata (Decoupled) -> 2. Distributed Inventory -> 3. Fast-Track Optimization (V2 Publisher).
    - **Manual Override Control**: All agents must respect the manual workflow flags (`FORCE_FULL_CHECK`, `FORCE_EVAL`, `ENRICH_METADATA`). When disabled (Standard Run), the system MUST strictly enforce the cache-first policy for maximum efficiency.

52. **Linguistic Uniformity**: All core documentation (index, README, GEMINI.md) and V2 portal summaries MUST be written in **Professional Technical English**. V1 descriptions remain in their native language (Mandate 10).

53. **Flash-First High-Density Curation (Scale Mandate)**: For mass processing (>1,000 resources), the system MUST prioritize **Gemini Flash/Lite** models for the Analyst phase. This ensures high RPM/TPM throughput while maintaining cost efficiency. Pro models are strictly reserved for the Auditor phase or high-value resource verification.

54. **Robust Batch Processing & Rate-Limit Resilience**: Large-scale curation MUST use batch sizes of **50 resources** for Fast-Track processing with a mandatory **2-second safety delay** between batches. 
    - **Incremental Persistence**: The system MUST flush the `inventory.yaml` to disk every 20 batches.
    - **Workflow Resilience**: Workflows MUST utilize GitHub Actions Cache (`actions/cache`) to restore progress at startup and save it `always()` at the end, ensuring zero data loss even upon 6-hour timeout cancellations.

55. **Multi-Tier Agentic Model Selection Policy**: To optimize the balance between reasoning depth, execution speed, and API quota safety, models MUST be selected based on task profile:
    - **Tier 1 (High-Throughput / Formatting)**: Mandatory **Gemini Flash/Lite** (e.g., `gemini-3.8-flash`, `gemini-3.5-flash-lite`, or Gen-4 Flash). Used for: mass classification (V2), formatting audits (PR Guardian), and high-volume link rescue (Health Checker).
    - **Tier 2 (High-Context / Human Interpretation)**: Mandatory **Gemini Pro and Frontier** (e.g., `gemini-3.1-pro-preview`, `gemini-4-argon`, `gemini-4-carbon`). Used for: raw social media curation (X.com/RSS), complex architectural auditing, debate synthesis, and security-critical verification.
    - **Constraint**: Tier 2 tasks MUST be limited to low-volume batches to protect the global RPM quota.

56. **V2 Index Metrics Protocol**: The "Knowledge Architecture and AI Coverage Status" report in the V2 index MUST include a direct comparison between V1 and V2 inventory. This report MUST display: 1. **V1 Base Inventory** (Total resources in the master archive), 2. **V2 Elite Selection** (Count of candidates and the resulting density ratio), 3. **AI Enrichment Coverage**, and 4. **GitHub Metadata Coverage**. This ensures transparency in the knowledge distillation process.

57. **Redundancy-Free Branding**: To ensure professional UI density, the V2 Portal header MUST NOT repeat the "Nubenetes" brand. The title MUST follow the pattern: "Nubenetes Elite Portal (V2) | Awesome Kubernetes and Cloud".

58. **Decoupled Workflow Architecture**: The Agentic V2 ecosystem MUST utilize a decoupled micro-workflow structure (Health Monitor, Metadata Engine, AI Curator, and Publisher) to optimize compute quotas and minimize Gemini token consumption. Any update to the V2 rendering logic MUST use the `--render-only` flag in the Publisher pipeline to maintain execution speed.

59. **High-Fidelity Official Extraction Protocol**: Multimedia curation (YouTube) MUST prioritize the **Official YouTube Data API v3** to ensure 100% fidelity to technical titles, descriptions, and metadata. Brittle scraping fallback (yt-dlp) or AI grounding MUST only be utilized when the official API is unavailable, and all extraction logic MUST support multiline indentation to prevent Markdown rendering breakage.

60. **Granular Versioning and Collaborative History Standard**: All architectural shifts and milestones MUST be versioned using **Semantic Versioning (SemVer)**. The `CHANGELOG.md` MUST follow the 'Keep a Changelog' standard and maintain a granular, exhaustive record including:
    - **Community Recognition**: Explicitly mention external authors and link to their specific Pull Requests (e.g., [PR #XX]).
    - **4-Tier Multimedia Hierarchy**: Clearly document the fallback sequence (Official API > Transcripts > Scraping > Gemini Grounding).
    - **Interactive Navigation**: Version headers MUST be clickable links to the corresponding GitHub Release tag.
    - **Logical Phasing**: Group changes by 'Added', 'Changed', and 'Fixed' to ensure technical traceability.

## 🛠️ Structural Evolution & Navigation

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

1.  **Mandatory Node Label Quoting**: ALWAYS wrap node labels in double quotes (e.g., `A["Label Text"]`). This is a hard requirement for all diagrams to ensure robust rendering and prevent truncation or parsing errors across GitHub, VSCode, and MkDocs.
2.  **Label Length & Multi-line Support**: Keep labels concise (under 25 characters). If a label is longer, you MUST use the HTML `<br/>` tag to force a line break (e.g., `A["Long Label<br/>Split in Two"]`) to prevent horizontal clipping.
3.  **Explicit Direction**: Use `graph TD` (Top-Down) for deep hierarchies and `graph LR` (Left-to-Right) for flat process flows to optimize readability and prevent horizontal clipping.
4.  **Syntax Validation**: Before committing, verify the syntax using a Mermaid previewer. Common pitfalls include:
    *   Unescaped brackets `[` or `]` inside labels.
    *   Missing semicolons or newlines between node definitions.
    *   Recursive loops without proper termination.
5.  **No Special Characters in ID**: Node IDs should be simple alphanumeric strings (e.g., `A`, `B`, `START`). Never use spaces or special characters in the ID itself, only in the quoted label.

## 🛡️ Repository Policies & Branch Protection

To maintain the integrity of the archive and ensure the AI agents operate correctly:

1.  **Branch Hierarchy**:
    *   `master`: Read-only for contributors/bots. Restricted to repository owner only.
    *   `develop`: The only valid target for direct AI commits and Pull Requests.
2.  **Strict Pull Request Policy (No Manual Merges)**:
    *   AI agents MUST always target `develop` for their work.
    *   AI agents MUST NEVER perform manual CLI merges (e.g., `git merge develop`) into `master` or `main`.
    *   To promote changes to `master`, AI agents MUST open a formal Pull Request from `develop` to `master` (e.g., using `gh pr create`) and **STOP**, waiting for the repository owner to review and merge via the GitHub UI. This ensures CI/CD workflows run correctly.
3.  **Owner-Only Merges & Tagging**:
    *   Only the repository owner has the authority to merge `develop` into `master` after verifying the visual health dashboard and metrics.
    *   Creation of version tags (`git tag`) MUST only occur AFTER the PR has been successfully merged into `master` by the owner.

## 📝 README Synchronization & Maintenance Protocols

The `README.md` is the primary entry point for Nubenetes and must accurately reflect the state of both the **V1 (Exhaustive)** and **V2 (Elite)** editions. AI agents and contributors MUST follow these protocols:

### 1. Mandatory Updates on `develop` Branch
Before any Pull Request is merged from `develop` to `master`, the `README.md` must be audited and updated to reflect the latest changes. This is critical for maintaining the "Source of Truth" status.

### 2. Metric Recalculation (Database-First)
Whenever a significant curation cycle (automatic or manual) is completed, the README MUST be updated using the **Unified Metadata Database** (`inventory.yaml`) as the sole source of truth:
*   **Database-Driven Exactness**: Link counts and density tables MUST NOT be derived from `grep` or file-system scans. They must reflect the actual entries in the inventory.
*   **Link Counts:** Update the "Heart of Nubenetes" table with the current total link count and specialized page count.
*   **Top Categories:** Recalculate the density of the top 10 categories based on metadata.
*   **Historical Growth:** Add/update the monthly surge rows in the "2026: The Agentic Monthly Surge" table.

### 3. Visual & Diagram Sync
*   **Mermaid Charts:** 
    - Update the "Major Ecosystem Pillars" pie chart to align with the **Strategic Dimensions** defined in the V2 portal.
    - **Annual Growth Metrics**: Include a Mermaid `xychart-beta` bar chart comparing "Commits" and "Estimated New Refs" side-by-side for each year, perfectly synchronized with the Annual Growth Summary table.
*   **Linguistic Diversity**: Maintain a dedicated chart visualizing the project's commitment to **Global Access** (Mandate 10).
*   **Architecture Flow**: If the Agentic Stack or the deployment lifecycle changes, the corresponding Mermaid diagrams MUST be updated immediately.
*   **Robustness**: Follow the "Mermaid Diagram Best Practices" (node quoting, explicit direction) as defined in this document.

### 4. V1 vs V2 Alignment
*   Ensure any changes to the `V2VisionEngine` or the elite selection criteria are reflected in the "Dual-Edition Architecture" section.
*   Update the "Comparison Matrix" if the technical differences between V1 and V2 evolve.

### 5. Automation vs Manual Intervention
*   **Automated Updates**: The Agentic Bot should ideally include a step to refresh these metrics in its curation PRs.
*   **Manual Fallback**: If a manual update is performed (emergency fixes, structural changes), the human/AI agent is responsible for manually running the metric extraction scripts and updating the `README.md` accordingly.
*   **README Integrity Guardrail**: Whenever `README.md` is modified, the agent MUST execute `python3 src/safety_readme.py`. This tool verifies the presence and correct numbering of all **15 mandatory technical sections**. Any PR that fails this audit MUST NOT be merged.
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
    - **Rendering & Path Resolution**: Restored `use_directory_urls: true` to prioritize SEO and clean URLs. Standardized on root-relative paths for manual HTML assets and `<center markdown="1">` for Markdown content within HTML blocks to prevent asset breakage across directory levels.
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
    - **CI/CD Hardening & Trigger Loop Prevention (May 2026)**:
        - **Trigger Loop Prevention**: Implemented `[skip ci]` message filtering across all workflows to prevent infinite loops after automated merges.
        - **Concurrency Control**: Added mandatory concurrency groups to all workflows to prevent race conditions during parallel automated updates.
        - **Playwright Caching**: Integrated `actions/cache` for Playwright binaries to reduce curation/cleaning setup time by >70%.
        - **Metric Consolidation**: Integrated `README.md` metric synchronization directly into the `V2 Agentic Builder` workflow to reduce redundant maintenance commits on the `develop` branch.
        - **O'Reilly Learning Flow**: Refined the O'Reilly-style technical hierarchy in the V2 portal to ensure a logical knowledge progression from foundations to advanced internals.
    - **Platinum Maintenance & Security (May 2026)**:
        - **Automated Triage System**: The health monitoring engine MUST open/update a GitHub Issue whenever high-value resources (`review_required`) fail validation. This ensures visibility for manual rescue attempts.
        - **OpenGraph Social Cards**: The V2 Portal MUST generate dynamic social sharing cards for every page using the `social` plugin to maximize ecosystem engagement.
        - **Dependency Guard (Dependabot)**: Automated monitoring of Python and GitHub Action dependencies is mandatory. Any security vulnerability MUST be addressed via prioritized bot-generated PRs.

    - **AI Dimension**: Renamed from "Intelligent Control Plane" for better industry alignment.
    - **Zero-to-Hero Grouping**: Implemented complexity-based levels (Fundamentals to Architect) for high-density learning paths.
    - **Special Assets Logic**: Integrated data/special_assets.yaml to ensure exhaustive preservation of critical lists (Introduction, YAML, Awesome repos).
*   **May 2026**: **Modernization of CI/CD, MkDocs Features, and UI (Cyber Cloud)**:
    - **Native GitHub Pages**: Migrated deployment to use native artifacts instead of the `gh-pages` branch for improved security and speed.
    - **CI/CD Caching**: Implemented `cache: pip` via `requirements.txt` to significantly speed up build times.
    - **V2 Elite Cyber Cloud Aesthetic**: Upgraded UI with high-contrast pure black backgrounds, neon cyan accents, advanced glassmorphism, and hover glow effects.
    - **Visual Identity Modernization**: Replaced the legacy car favicon with a new modern "Gemini construction car" PNG (`favicon-car-modern.png`) to improve search engine appearance and brand consistency.
    - **MkDocs Features Enabled**: Activated native Privacy Plugin (GDPR compliance), Pruned Navigation (performance), Social Cards in V1, Code Copy, Tab Sync, and Tooltips.
    - **Announce Banner**: Added a global announcement banner to V1 directing users to the V2 Elite Portal.
    - **Resilient Architectural Refinements (Phase 2)**:
        - **Fast-Track V2 Elite Builder**: Optimized the builder to run sequentially for maximum stability and simplicity, bypassing the overhead of distributed systems.
        - **Workflow Hardening (Race Condition Fix)**: Implemented a mandatory `git pull --rebase` strategy across all automated bots to prevent concurrent push failures.
        - **Ultra-Visible Branding**: Standardized on a minimalist Cyan "N" favicon (`favicon-ultra.png`) and restored the original hero car imagery to the V2 index.
        - **O'Reilly Journey Builder**: Refined the O'Reilly-style technical hierarchy in the V2 portal to ensure a logical knowledge progression from foundations to advanced internals.
        - **Platinum SEO Mitigation**: Implemented a "Smart 404" rescue system and a **Hybrid SEO-First Architecture** that preserves V1 at the root while redirecting human traffic to the V2 Elite Portal.
        *   **May 2026**: **Hybrid SEO-First Architecture Reversion**:
        - **V1 Restoration (Root)**: Restored the V1 Archive to the root (`/`) to protect historical deep-links and SEO authority.
        - **V2 Relocation (/v2/)**: Moved the Elite Portal to a dedicated subdirectory.
        - **Smart Root Redirect**: Implemented an automatic meta-refresh in the root `index.html` to guide human visitors to the V2 experience without breaking search engine indices.
        - **V1 Fallback (/v1/)**: Duplicated the archive to `/v1/` for explicit navigation.
- **V2 Index Metrics Protocol**: The "Knowledge Architecture and AI Coverage Status" report in the V2 index MUST include a direct comparison between V1 and V2 inventory. This report MUST display: 1. **V1 Base Inventory** (Total resources in the master archive), 2. **V2 Elite Selection** (Count of candidates and the resulting density ratio), 3. **AI Enrichment Coverage**, and 4. **GitHub Metadata Coverage**. This ensures transparency in the knowledge distillation process.
- **Redundancy-Free Branding**: To ensure professional UI density, the V2 Portal header MUST NOT repeat the "Nubenetes" brand. The title MUST follow the pattern: "Nubenetes Elite Portal (V2) | Awesome Kubernetes and Cloud".
- **Decoupled Workflow Architecture**: The Agentic V2 ecosystem MUST utilize a decoupled micro-workflow structure (Health Monitor, Metadata Engine, AI Curator, and Publisher) to optimize compute quotas and minimize Gemini token consumption. Any update to the V2 rendering logic MUST use the `--render-only` flag in the Publisher pipeline to maintain execution speed.

## Git Workflow: Gitflow (Mandatory)

This repository uses **Gitflow**. All agents and automated processes MUST follow this branching model:

- **`master`**: Production branch. Only receives merges from `release/*` branches. Every merge to master gets a **semantic version tag** (`vX.Y.Z`) and a **GitHub Release** with detailed release notes.
- **`develop`**: Integration branch. All feature branches merge here via PR. Back-merged from master after each release.
- **`feat/*`**: Feature branches. Created from `develop`, merged back to `develop` via PR.
- **`release/vX.Y.Z`**: Release branches. Created from `develop`, merged to `master` with `--no-ff`, then back-merged to `develop`.
- **`gh-pages`**: Deployment. NEVER modified directly.
- **Protected branches**: `master`, `develop`, `gh-pages` — NEVER deleted.

### Release Sequence
1. Feature branch → PR to `develop` → merge
2. Create `release/vX.Y.Z` from `develop`
3. Merge release to `master` (`--no-ff`)
4. Create annotated tag: `git tag -a vX.Y.Z -m "..."`
5. Push master + tag
6. Back-merge master to develop (`--no-ff`)
7. Create GitHub Release with `gh release create`

### Versioning: `v{major}.{minor}.{patch}`
- **Major**: breaking changes or architectural shifts
- **Minor**: new features (modules, digest categories, new pipelines)
- **Patch**: bug fixes, config tweaks, content updates

## URL Policy: Clean URLs (Mandatory)
Both V1 (`mkdocs.yml`) and V2 (`v2-mkdocs.yml`) MUST use `use_directory_urls: true` to produce clean URLs like `/kubernetes/` instead of `/kubernetes.html`. **NEVER** enable the MkDocs `offline` plugin — it forces `.html` suffixes on all URLs, breaking SEO authority and thousands of existing deep-links. This is a hard, non-negotiable rule.
