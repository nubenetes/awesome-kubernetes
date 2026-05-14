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
8.  **Repository Consolidation**: In case of a failure in a deep GitHub/GitLab link, always try to validate the repository root before considering it dead. We prefer stable links to repository roots over volatile deep-links.
9.  **URL Expansion**: All shortened links (t.co, bit.ly, buff.ly, etc.) MUST be expanded to their original long version before being evaluated or injected. This ensures inventory homogeneity and improves global deduplication precision.
10. **Official Language (English Only)**: All injected content (titles, descriptions, headers), execution logs, and automated communications (PRs) MUST be exclusively in ENGLISH. Nubenetes is a global resource and linguistic consistency is critical.
11. **Workflow-Config Synchronization**: The GitHub Actions curation workflow form (`agentic_cron.yml`) MUST remain perfectly synchronized with the curation sources configuration file (`data/curation_sources.yaml`). Any addition, removal, or renaming of topics/categories in the configuration file requires a corresponding update to the workflow's input fields (checkboxes) to ensure users can toggle those sources manually. This maintains consistency between data-driven sources and the UI trigger.

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
    *   `docs/index.md` (Main Table of Contents).
    *   The internal TOC of the modified page.
*   **Orphan Curation**: Periodically audit the `docs/` folder to find unlinked files and integrate them into the navigation based on their topic.

## 🚀 Block Evasion Strategies

The bot must rotate between profiles to avoid detection:
1.  **Desktop/Google**: Standard desktop request.
2.  **Mobile/Twitter**: Mobile request with Twitter Referer (high success rate).
3.  **Playwright/LinkedIn**: Real navigation with JS enabled.
4.  **Firefox/Reddit**: Alternative desktop profile.

## 📈 Learning Diary (Improvement History)

*   **May 2026**: Initial implementation of the autonomous engine with Playwright and Wayback Machine.
*   **May 2026**: Added Multidimensional Evasion system (5 attempts, profile rotation).
*   **May 2026**: Creation of `AgenticCurator` for navigation audit and repository consolidation.
*   **May 2026**: Generation of PRs with visual analytics (Mermaid) and Health Matrix.
*   **May 2026**: Implementation of Backup-based Curation (JSON/MD) to avoid X.com blocks.
*   **May 2026**: Implementation of multi-source curation and category-based filtering in GitHub Workflow.
