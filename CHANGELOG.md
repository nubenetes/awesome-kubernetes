# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [[2.9.67]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.67) - 2026-10-25

### Added
- **Composite Momentum & Velocity Scoring (`src/enrichment.py`)**: Introduced `compute_momentum_score()` combining log-scaled GitHub stars, monthly star velocity (`gh_stars_per_month`), commit freshness/staleness penalties, and CNCF/LFAI maturity bonuses to surface fast-rising Cloud-Native AI tools alongside foundational standards.
- **Canonical CNCF & LF AI Landscape YAML Integration (`src/enrichment.py`)**: Replaced capped GitHub topic searches with direct parsing of canonical `landscape.yml` files from CNCF and LF AI & Data Foundations (320+ projects across Graduated, Incubating, Sandbox, and Archived).
- **Agent-Ready `llms.txt` Index (`src/v2_optimizer.py`)**: Added automated generation of `v2-docs/llms.txt` during V2 portal builds, exposing the portal's strategic dimensions and top 60 Flagship / High-Momentum references for AI coding agents.
- **Cloud-Native AI & GPU Deep-Dive Topic Hubs (`src/v2_optimizer.py`)**: Added `ai` and `mlops` provider hubs and cross-linked `AI Agents & MCP` and `AI & GPU Workloads` on `kubernetes.md`.
- **In-Page Quick Filters (`docs/static/v2_filter.js`)**: Added `AI & MCP` and `Fresh (2025–2026)` filter pills to the V2 resource filter bar.

### Changed
- **Velocity-Driven GitHub Discovery & Sources (`src/autonomous_discovery.py`, `data/curation_sources.yaml`)**: Expanded autonomous discovery to 20 velocity-sorted GitHub queries with a rolling 180-day `pushed` cutoff covering K8s + AI/LLM/GPU, MCP servers, vLLM, MLOps, and eBPF, and added official Kubernetes, CNCF, HuggingFace, and NVIDIA feeds/accounts.
- **Multi-Agent Debate Protocol Rubric (`src/v2_debate.py`)**: Upgraded SRE and AI Platform Engineer evaluation criteria for Kubernetes-native integration (CRDs, Operators, Gateway API, OpenTelemetry/eBPF) and Cloud-Native AI readiness (`[GPU]`, `[LLM]`, `[MCP]`, `[MLOPS]`).

## [[2.9.61]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.61) - 2026-07-13

### Added
- **Compile-time Safety Assertions for Injections**: Added permanent compiler assertions in `v2_optimizer.py` verifying that JCasC, Pipeline Principles, Best Practices, and OpenShift callout boxes are successfully merged into the V2 Jenkins page, failing the build immediately on any silent regression.

### Fixed
- **Jenkins V2 Featured Callout Boxes Restoration**: Restored the missing Configuration-as-Code and Pipeline callout boxes in `v2-docs/jenkins.md` by updating replacement strings to match the newly normalized headings (`### Configuration As Code` and `## CICD`).
- **Introduction Gold Nuggets Precedence**: Fixed an operator precedence bug in the `is_gold` check (`is_intro and (stars or 0) >= 4` instead of `is_intro and stars or 0 >= 4`), cleaning up incorrect callout boxes for lower-rated resources on `introduction.md`.
- **Health Checker Checkpoint & Progress Persistence**: Added progress checkpointing (`health_check_checkpoint.json`) to persist state across batches and prevent duplication/redos after network validation timeouts.
- **Safer CLI Triage in GHA**: Hardened the GitHub Actions issue triage query against NoneType parser failures when no open issues are found.
- **Semaphore UI Link Correction & Migration**: Updated Semaphore UI references to the official `https://semaphoreui.com/` domain, consolidating duplicate domains in the central database.

## [[2.9.48]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.48) - 2026-06-23

### Fixed
- **Trending Now cards: impact badge no longer overlaps the title**: On the V2 home page "🔥 Trending Now — Cloud Native Intelligence" lane, the `CRITICAL`/`HIGH` impact badge (and the optional `🆕 NEW` pill) was `position: absolute` in the top-right corner, so a long celeste category/title flowing in normal document position could slide right underneath it and become unreadable. The badge is now an in-flow, right-aligned pill (`width: fit-content; margin-left: auto`) on its own line at the top of the card, with the `NEW` pill laid out as a flex sibling (`gap`-spaced) — so the red impact text, the celeste title, and the green `NEW` pill can never overlap, on any card width or title length. Cards with short titles stay just as tight as before. `docs/static/v2_elite.css` only; cache-bust auto-versions from the release tag.

## [[2.9.38]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.38) - 2026-06-20

### Added
- **OpenShift submenu + grouped Kubernetes distros**: The Kubernetes menu's OpenShift entry only linked to the generic overview, hiding the substantial OpenShift 4 page (`ocp4`, 29 links) amid the ocp3-deprecated/openshift/ocp4 confusion. OpenShift is now a nested submenu (OpenShift ▸ → OpenShift 4 (current) · Overview · OpenShift 3 (legacy)), reusing the AWS nested-submenu mechanism. The Kubernetes distributions/platforms are grouped at the end of the menu — Managed K8s · OpenShift ▸ · Rancher · Distros & Alternatives (`kubernetes-alternatives` moved here and relabeled). The 2-column Kubernetes menu was also switched from CSS multicol to a deterministic column-major grid (11 rows × 2 cols, `overflow:visible`), removing a faint sub-pixel scrollbar. Verified in Chrome 148 (Playwright + screenshot): clean 2-column card with no scrollbar at viewport heights 768–1080; the OpenShift submenu opens to the side and keeps the parent open. Cache-bust `?v=2.9.38`; V2-only.

## [[2.9.37]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.37) - 2026-06-20

### Fixed
- **Kubernetes quick-nav menu reliability**: The Kubernetes dropdown (22 items) was the only menu tall enough to need a scrollbar on an anchor-positioned popover, which made it open/behave unreliably compared to the others. It now uses a 2-column layout (`column-count: 2`), halving its height (~731px → ~353px) so it shows in full without a scrollbar at any realistic viewport; multicol is column-major, so reading order is preserved. Also removed `flip-block` from the menu position-try fallbacks (kept `flip-inline`): the quick-nav is a sticky top bar, so a tall menu flipping above would shoot off the top of the screen — menus now always open downward. Verified in Chrome 148 (Playwright) at viewport heights 700–1080. Cache-bust `?v=2.9.37`; V2-only.

## [[2.9.36]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.36) - 2026-06-20

### Changed
- **Quick-nav fully regrouped into 11 thematic menus + nested AWS submenu**: Reorganized the quick-nav into one direct pill (Topic Map) plus 11 category dropdowns that group related topics so every destination has a sensible home: Digest · Kubernetes (Overview · Docker · Tools · Helm · kubectl · all kubernetes-* · Managed · OpenShift · Rancher) · Delivery (GitOps · CI/CD · DevOps · Argo · Flux · Tekton · Jenkins · …) · IaC (Terraform · IaC · Ansible · Pulumi · Crossplane · Kustomize) · Cloud · Network · Security · Observability & SRE · AI & Data · Dev & Platform · More. Docker now lives inside Kubernetes; GitOps + CI/CD + DevOps share Delivery; Terraform + IaC share IaC. **AWS is a nested submenu inside Cloud** (Cloud → AWS ▸ → 8 AWS pages), built with nested Popover API + explicit `anchor()` side-positioning (position-area's horizontal axis isn't honored when the anchor is inside another popover). Pages may appear in more than one menu where it aids discovery; menus get `max-height:82vh` + scroll for the tall Kubernetes menu. Verified in Chrome 148 (Playwright). Cache-bust `?v=2.9.36`; V2-only.
- **AWS + Kubernetes provider hubs now live**: This release also publishes the regenerated v2-docs from v2.9.34/v2.9.35 — the AWS landing page (3 → ~40 links + "Deep-Dive Topic Pages" hub, trivial sub-pages consolidated) and the Kubernetes sub-page hub.

## [[2.9.35]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.35) - 2026-06-20

### Added
- **Kubernetes provider hub**: A fragmentation audit found only two prefix clusters — `aws` (fixed in v2.9.34) and `kubernetes`. Unlike AWS, Kubernetes is well-classified (rich parent at 157 links + substantial distinct children: tools 144, networking 64, security 52, monitoring 24, …), so nothing is merged. This adds a "Deep-Dive Topic Pages" hub to `kubernetes.md` indexing its 14 substantial sub-pages (Tools · Networking · Security · Monitoring · Storage · Autoscaling · Operators · Alternatives · Big Data · Tutorials · Backup & Migrations · Client Libraries · Local Dev · On-Premise) — purely additive navigation, no merging or pruning. Other small pages (pulumi, kustomize, registries, …) are legitimate distinct topics and were intentionally left alone. Generator-only (`src/v2_optimizer.py`); republished on the next curation run.

## [[2.9.34]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.34) - 2026-06-20

### Changed
- **AWS page de-fragmentation + provider hub**: The AWS landing page rendered with only ~3 links because AWS content was split across ~20 granular pages (Azure/GCP use a single rich page each), many with just 1-5 links. Two generator changes in `src/v2_optimizer.py` fix this: (A) `aws.md` now renders a "Deep-Dive Topic Pages" hub linking to the substantial sub-pages that remain (Serverless · Storage · Networking · Security · IaC · Backup · New Features) via a new `subpage_hubs` map; (B) the near-empty / junk-drawer AWS sub-pages (≤7 links + "miscellaneous": aws-pricing, aws-training, aws-data, aws-messaging, aws-tools-scripts, aws-monitoring, aws-architecture, aws-containers, aws-devops, aws-databases, aws-miscellaneous) merge into `aws.md` via the existing `merge_map`, with their slugs removed from `dimensions` so the pipeline prunes the orphans and auto-syncs the nav. Verified with `--render-only`: aws.md goes from 3 to 44 links plus the 7-child hub. V1 (`docs/`) is untouched by design (exhaustive archive + merge source). Generator-only; the AWS pages are republished on the next curation run.

## [[2.9.33]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.33) - 2026-06-20

### Added
- **Quick-nav menu expansion — 38 destinations**: Data-driven expansion of the hybrid quick-nav (ranked by per-page link count + relevance). New 📊 Digest menu pairs both editions (Tech & Cloud Digest + Industry & Geo Digest); new 🧰 K8s menu surfaces the Kubernetes ecosystem (Kubernetes Tools · Helm · Managed K8s · OpenShift · Tutorials). Existing menus grew: ☁️ Cloud += Serverless · FinOps; 🌐 Network += Service Mesh (Istio emoji → ⛵); ⚙️ Ops += IaC · Developer Portals; ⋯ More += Technical Tags · Demos. 38 destinations total across 6 direct pills + 7 Popover menus; chip font trimmed to 0.62rem with tighter gap/padding so all 13 bar chips fit one row down to ~1280px. Verified in Chrome 148 (Playwright): every menu opens below its button, flips near the right edge, and closes on Esc. Cache-bust `?v=2.9.33`; V2-only.

## [[2.9.32]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.32) - 2026-06-20

### Fixed
- **Quick-nav menus open below their button + fit one row**: Fixed two issues in the v2.9.31 hybrid quick-nav (verified in Chrome 148 via Playwright). (1) The Popover category menus did not visibly open on click — they used `position-area: bottom span-inline-end`, which mixes a physical keyword (`bottom`) with a logical one (`span-inline-end`); that is invalid CSS and silently computed to `none`, leaving the menu in its static position on top of the button. Fixed with a valid all-physical `position-area: bottom span-right` plus explicit `anchor-name` / `position-anchor` pairs per button↔menu, so each menu reliably drops below its trigger and auto-flips near the right edge. (2) The bar wrapped to a second row on common displays — reduced the chip font ~1pt (`0.7rem → 0.64rem`) and trimmed the column-gap/padding so all 7 pills + 5 menus fit a single row down to 1280px viewports. Cache-bust `?v=2.9.32`; V2-only, CSS-only.

## [[2.9.31]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.31) - 2026-06-20

### Changed
- **Hybrid quick-nav — direct pills + Popover category menus**: Collapsed the 25-destination quick-nav from 3 wrapped rows to a single slim row that stays one row regardless of how many destinations are added. The most-used flagships remain direct one-click pills (Topic Map · Digest · Kubernetes · Docker · GitOps · Terraform · AI & MCP); the long-tail clusters fold into five category menus — ☁️ Cloud, 🌐 Network, 🔐 Security, ⚙️ Ops, ⋯ More — built with the native HTML Popover API + CSS Anchor Positioning (Baseline 2026), zero JS. Menus drop below their button via `position-area` with flip fallbacks, animate in with `@starting-style`, rotate their caret via `:has()`, and inherit the Popover API's built-in Esc / click-outside dismissal and focus management (identical on touch and desktop); `prefers-reduced-motion` honored. All 25 destinations preserved. Touches `docs/overrides/main.html` + `docs/static/v2_elite.css` (cache-bust `?v=2.9.31`); V2-only, no page regeneration.

## [[2.9.30]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.30) - 2026-06-20

### Changed
- **Quick-nav — networking cluster + DevSecOps**: Grew the quick-nav bar to 25 destinations. Added a new networking cluster after the cloud providers (🌐 Networking · 🕸️ Istio · 🔗 K8s Net) and DevSecOps alongside Security (🔐 Security · 🛡️ DevSecOps), keeping short labels and category grouping. Template-only change to `docs/overrides/main.html` reusing the existing `.nb-quicknav` pill styling — no CSS change, no page regeneration. V2-only.

## [[2.9.29]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.29) - 2026-06-20

### Changed
- **Quick-nav redesign — centered category-grouped pill chips**: Grew the quick-nav bar to 21 destinations and restyled it as a modern, centered chip bar. Added CI/CD, Ansible, and the three hyperscalers (AWS, Azure, GCP), and reordered every tab into related category clusters with short labels: discovery (Topic Map · Digest · Videos) → platform (Kubernetes · Docker) → delivery (GitOps · CI/CD) → IaC (Terraform · Ansible) → cloud (AWS · Azure · GCP) → security → ops (Observability · SRE · DevOps) → data (Messaging) → AI/ML (AI & MCP · MLOps) → Methodology → V1 Archive (muted). Chip background/border/glow are derived from the theme accent via `color-mix(in srgb, …)` (Chrome 111+) so the bar restyles automatically with the palette; rows are centered (`justify-content: center`) for a balanced multi-row layout, with hover lift, `:focus-visible` outline, `prefers-reduced-motion` support, and a mobile single-row horizontal scroll. Touches `docs/overrides/main.html` + `docs/static/v2_elite.css` (cache-bust `?v=2.9.29`); V2-only, no page regeneration.

## [[2.9.28]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.28) - 2026-06-20

### Changed
- **Expanded quick-nav bar**: Grew the slim quick-nav bar from 6 to 16 curated one-click destinations, surfacing the principal topics across all of Nubenetes from any page. Added the cloud-native pillars (Kubernetes · Docker · GitOps · Terraform · K8s Security · Observability), the ops disciplines (SRE · DevOps), data/messaging (Message Queue), and MLOps alongside the existing AI & MCP hub. Template-only change to `docs/overrides/main.html` (no CSS change, no page regeneration); reuses the existing `.nb-quicknav__link` styling with `flex-wrap` handling density on narrow viewports. Still under the 18-tab overflow line the bar was designed to avoid. V2-only.

## [[2.9.27]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.27) - 2026-06-20

### Added
- **Slim quick-nav bar**: A thin horizontal bar below the header on every V2 page with six curated one-click destinations (Topic Map · Intelligence Digest · Video Hub · AI & MCP · Methodology · V1 Archive). These cross-cutting destinations previously only existed as badge cards on the home; the bar makes them persistently reachable from any depth. Implemented by overriding Material's `tabs` block (empty since `navigation.tabs` is disabled) plus `.nb-quicknav` CSS — so it adds persistent shortcuts WITHOUT reintroducing the 18-tab overflow and WITHOUT collapsing the full collapsible left navigation tree. Template/CSS-only (no page regeneration); V2-only.

## [[2.9.26]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.26) - 2026-06-20

### Changed
- **Collapsible, nested left navigation**: After moving the sections to the left sidebar in 2.9.25, they rendered as a *flat* list of 18 labels with no expand/indent — `navigation.sections` made them non-collapsible group labels and `navigation.prune` stripped the inactive children. Disabled both so the sidebar is now a proper collapsible, nested, indented tree (14 toggles / chevrons, collapsed by default, click to expand). No size penalty (88,213 vs 88,516 bytes per page).

### Added
- **Home section headings**: The V2 home had a single H2, leaving its right-hand "On this page" TOC empty. Added `## Explore the Ecosystem` (badge cards) and `## Trending Now` (Intelligence Digest) alongside the existing `## The Cloud Native Universe We Track`, so the home's right TOC now lists three real sections. Net effect: both side columns are now useful on every page — left = full collapsible directory, right = per-page section map.

## [[2.9.25]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.25) - 2026-06-20

### Changed
- **V2 navigation: tabs → left sidebar**: The 18 top-level sections were rendered as a horizontal tab bar (`navigation.tabs`), whose labels total ~3300px and overflowed a typical ~1400px laptop viewport — forcing horizontal scroll to reach the right-side dimensions and leaving the left sidebar nearly empty on top-level pages like the home. Disabled `navigation.tabs` (+ `.sticky`) so the sections render in the standard vertical left sidebar: it handles all 18 collapsed sections via normal scroll, stays populated on every page (the home's rendered nav goes from 23 links to the full 178-link tree), and nothing clips. Theme-only change preserved across publishes (the optimizer's nav-sync only rewrites the `nav:` block).

## [[2.9.24]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.24) - 2026-06-20

### Added
- **Per-page JSON-LD structured data**: Each V2 content page now emits a second JSON-LD block — a schema.org `CollectionPage` tied to the existing `WebSite`/`Organization` `@graph` — carrying the page name, description, URL, and `datePublished` / `dateModified` fed by the `git-revision-date-localized` plugin's raw ISO dates (the creation/last-update dates from 2.9.23). This enables article/collection rich snippets in search results with real freshness dates. Template-only change (`docs/overrides/main.html`), applied at build time; the homepage is skipped (it is already the `WebSite` entity), and JSON is built with `| tojson` for safe escaping.

## [[2.9.23]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.23) - 2026-06-20

### Changed
- **Richer per-page SEO meta descriptions**: The unique-but-templated descriptions from 2.9.22 now lead with each page's **top-ranked resource names** (long-tail keywords) — e.g. *"Top Kubernetes resources for 2026, AI-ranked: Helm, kube-prometheus and more — curated Cloud Native tools, guides and references."* URL/path-like and emoji-laden titles are filtered out, pages whose top links are all URL-like fall back to the clean template, and the text is capped at ~160 chars on a word boundary. (There is no per-page AI intro to mine, so the page's own top resources are the cleanest source.)

### Added
- **Per-page creation dates**: Enabled `enable_creation_date` on the `git-revision-date-localized` plugin, so every V2 page footer now shows both **Created** and **Last update** — an additional age/freshness signal alongside the last-modified date introduced in 2.9.18.

## [[2.9.22]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.22) - 2026-06-20

### Added
- **robots.txt**: Added `v2-docs/robots.txt` (deployed at the site root) that allows full crawl and references both the V2 (root) and V1 (`/v1/`) sitemaps — previously the site shipped a `sitemap.xml` with no `robots.txt` pointing at it.

### Changed
- **Unique per-page SEO meta descriptions**: Every V2 page previously fell back to the identical global `site_description`, so ~140 pages shared one `<meta name="description">` (a duplicate-content SEO penalty). `v2_optimizer.py` now emits a unique `description:` front-matter per page — derived from the page title and its strategic dimension — which Material renders as `<meta name="description">` and `og:description`. The Topic Map and Methodology pages get tailored descriptions. The 12 redirect-stub pages were intentionally left untouched (they already 0s meta-refresh redirect with `canonical` pointing at the target, which passes authority better than `noindex`).

## [[2.9.21]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.21) - 2026-06-20

### Added
- **README database & lifecycle diagrams**: Added two new collapsible Mermaid diagrams — a **Database Architecture** diagram (§6.1.3) detailing the YAML + SQLite coexistence engine (`inventory.sql` Git source-of-truth → in-memory SQLite → `inventory.yaml` mirror, plus the per-resource schema), and a **full Data Lifecycle** diagram (§6.3) tracing a resource from discovery and ingestion through cached maintenance/enrichment to render and deploy, with background garbage collection.

### Changed
- **Grouped, compact Technical Tags Index TOC**: The `tags.md` table of contents was a flat 80-entry numbered list that buried the 8 maturity tags under a long tail of one-resource "X Content" language tags. It is now grouped into *Maturity and Quality* (numbered) plus *Technical Domains* / *Language and Format* (compact, count-sorted inline rows). Generator (`v2_optimizer.py`) now emits unique explicit heading anchors (`{#slug}`) shared by the TOC and section headers — fixing collisions where `C` / `C#` / `C++` all resolved to `#c-content` — corrects the `1 resource` grammar, and filters non-language values (`En`, `Not Applicable`, `Multi-Language`, `Polyglot`, …) that previously created meaningless tag buckets.
- **README mermaid legibility & accuracy**: Fixed text overflow in four diagrams (Division of Labor, Agentic Data Flow, Debate Protocol, Deployment Lifecycle) by wrapping long node labels, removed a duplicate edge, and refreshed the V2 feature documentation with the v2.9.16–v2.9.20 work (Topic Map & Methodology pages, per-page last-updated dates, JSON-LD, branded 404, deterministic generated artifacts).

## [[2.9.20]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.20) - 2026-06-20

### Fixed
- **RSS feed drift fully eliminated**: The 2.9.19 fix derived the feed's `<lastBuildDate>` from `_meta.last_updated`, but that analysis timestamp is bumped on every publish even when the ranked content is unchanged, so `v2-docs/feed.xml` still drifted between `develop` and `master`. `src/rss_generator.py` now derives `lastBuildDate` from the **freshest item's content date** (the items only change when the ranking actually changes), with `_meta.last_updated`/a constant as fallbacks. Verified deterministic across reruns, and the `develop` and `master` digests both yield `2026-06-18` — so `feed.xml` is now byte-identical across branches and no longer spawns no-op promotion diffs.

## [[2.9.19]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.19) - 2026-06-20

### Fixed
- **Deterministic RSS `lastBuildDate` (residual develop↔master drift)**: `src/rss_generator.py` set the feed's `<lastBuildDate>` to `datetime.utcnow()`, so every republish rewrote it even when the digest was unchanged — leaving a perpetual 1-line diff in `v2-docs/feed.xml` (the last residual after the PR Guardian drift fix in 2.9.18). It now derives the date from the digest's `_meta.last_updated` (the actual analysis timestamp), falling back to the most recent item date then a fixed constant, making the feed a pure function of its input. Verified byte-identical output across repeated runs; the feed now changes only when the digest content actually changes.
- **In-page filter no longer injected on Topic Map & Methodology**: The resource search / maturity-tag widget (`static/v2_filter.js`) auto-injects wherever a page has `<ul><li>` items. Topic Map lists category links (with counts) and Methodology lists legend rows — neither carries `.md-tag` maturity tags, so the pills always filtered to zero and the "Showing X of Y resources" counter mis-counted categories/rows as resources. Added both pages to the widget's existing `<h1>`-based skip-list (alongside the home, Video Hub, Tags and Digest pages). Cache-bust `v2_filter.js?v=2.9.19`.

## [[2.9.18]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.18) - 2026-06-20

### Added
- **Per-page "Last update" dates (SEO freshness)**: Enabled the `git-revision-date-localized` MkDocs plugin on the V2 portal, surfacing a real last-modified date on every page. Added the dependency to `requirements.txt`, configured it in `v2-mkdocs.yml` (`type: date`, `fallback_to_build_date: true` so a missing git history never fails the build), and set `fetch-depth: 0` on the `06.deploy_final.yml` checkout so the plugin reads full history instead of collapsing every page to the build date.
- **JSON-LD structured data**: Injected schema.org `WebSite` (with a sitelinks `SearchAction`) + publishing `Organization` markup via an `extrahead` block in `docs/overrides/main.html`, making the canonical `nubenetes.com` root eligible for richer search results and knowledge-panel association. Validated: build exits 0 and the emitted JSON-LD parses to `[WebSite, Organization]`.

### Fixed
- **`develop ↔ master` cosmetic drift loop (recurring no-op release PRs)**: The PR Guardian (`07.1.pr_guardian.yml` → `src/pr_guardian.py`) ran its auto-formatter ("&"→"and" in headings, URL trailing-slash/tracking-param stripping) on every changed `.md` — including the **generated** `v2-docs/` tree — and committed the result back to the PR branch. Because feature PRs land on `develop` (Guardian runs) but release branches merge to `master` via plain `git merge` (Guardian does not run), `develop` accumulated the normalized form while `master` kept the generator's raw form, producing a perpetual cosmetic diff that spawned recurring no-op "🚀 Release: Agentic V2 Portal Update" PRs (e.g. #399). Since `v2_optimizer.py` is the single source of truth for `v2-docs/` formatting, the Guardian now skips that tree in its auto-format loop and drops it from the auto-commit `git add`; hand-authored `docs/` and `README`/`inventory` are unaffected.

## [[2.9.17]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.17) - 2026-06-20

### Fixed
- **Topic Map heading increment (MD001 lint failure)**: The new `topic-map.md` page emitted its per-dimension headings as `###` (h3) directly under the page `#` (h1) title, skipping h2. This tripped `markdownlint` **MD001/heading-increment**, turning the `07.2. Markdown Linter` workflow red on both `develop` and `master` right after the v2.9.16 release. Fixed the generator (`v2_optimizer.py`) and the committed page to emit dimensions as `##` (h2), and updated the CSS selector to `.topic-map-dim h2`. As a bonus, the h2 dimensions now populate the right-hand "On this page" TOC with a clean per-dimension index. Verified with the exact CI `markdownlint` config (0 errors); cache-bust bumped to `?v=2.9.17`.

## [[2.9.16]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.16) - 2026-06-20

### Added
- **V2 Topic Map page**: A new `topic-map.md` (generated by `v2_optimizer.py`) presents the complete category directory grouped by strategic dimension in a **responsive multi-column CSS grid** (3 → 2 → 1 columns), with a **per-category resource count** badge derived from a recursive walk of each category's link tree. This replaces the ~130-link "Strategic Dimensions" dump that previously bloated the home page, and is reachable from a new hero badge card and the top-level nav.
- **V2 Methodology page**: The Maturity Taxonomy and Technical Impact (star score) legend tables moved out of the home into a dedicated `methodology.md`, leaving the landing page focused while keeping the reference one click away.
- **Branded 404 page** (`docs/overrides/404.html`, shared V1/V2): replaces the theme's bare "404 - Not found" with a helpful page offering Home / Topic Map / V1 Archive — a safety net for the deep-link stability the portal depends on.

### Changed
- **Home landing page restructured for altitude**: Moved the fresh, dynamic **Trending Now / Intelligence Digest** block *above* the signature YouTube channel mosaic (previously the static mosaic pushed the live content below the fold). The mosaic is preserved as a brand showcase and now closes the page under a new **"The Cloud Native Universe We Track"** heading, with a slim reference footer linking the Topic Map, Methodology and Video Hub.
- **YouTube mosaic legibility & performance**: Surfaced the seven per-group category labels that were previously hidden in a `title=` tooltip (visible accent-bordered labels), and added `loading="lazy"` to the ~150 channel logos for a meaningful LCP/initial-load improvement.
- **About page videos hardened**: The two embedded videos now use `youtube-nocookie.com` (no tracking cookies until play — consistent with the active `privacy` plugin), `loading="lazy"`, and a responsive `aspect-ratio` wrapper that no longer overflows on mobile.
- **Collapsed left navigation**: Disabled `navigation.expand` in `v2-mkdocs.yml`; with ~169 nav entries it forced every section open (heavy DOM, overwhelming). The new Topic Map page now serves as the full scannable directory.
- **CSS hygiene**: Hoisted repeated inline styles (hero badge row) into `v2_elite.css` classes and bumped the cache-bust to `?v=2.9.16`.

## [[2.9.15]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.15) - 2026-06-19

### Changed
- **Navigable Intelligence Digest TOC**: The Tech & Cloud and Industry & Geo digest pages now show their sections in the right-hand "On this page" TOC. They were rendered period-first (three time-window tabs, each nesting every category as **bold text**), so the pages had zero real headings and an empty TOC. Inverted the layout in `_generate_digest_pages()` to **category-first**: each category is a real `##` heading (Kubernetes & Orchestration, Containers & Runtime, … / Americas, Europe, Spain, Asia-Pacific), with the three time-windows (3 / 6 / 12 months) as content tabs *inside* each category. The TOC now lists all 22 tech categories and 4 geo regions exactly once, headings sit at column 0 (no more MD023 workaround), and the tabbed UX is preserved.

## [[2.9.14]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.14) - 2026-06-19

### Changed
- **Deterministic V2 Publisher Push (04.1)**: Replaced the fragile rebase + `git checkout --ours/--theirs README.md` self-healing in `04.1.agentic_v2_publish.yml` — which could hang on a non-README conflict and silently discard the bot's README metrics — with the same deterministic model now used by `05.1`. The render is authoritative for its generated surface, so each attempt hard-resets to the freshest `origin/develop` tip, overlays the generated outputs verbatim (`docs/`, `v2-docs/`, `data/inventory.yaml`, `data/inventory.sql`, `data/news_digest.json` — source configs like `link_rules.yaml`/`special_assets.yaml` are deliberately left untouched), regenerates `README.md` on top, then commits and pushes with a 5-attempt retry. This never hangs on a conflict and never loses data. Also pinned `PYTHONPATH` on the step so the in-loop `readme_updater`/`safety_readme` calls always resolve `src`.

## [[2.9.13]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.13) - 2026-06-19

### Fixed
- **README Sync Dirty-Tree / Race Failure (root cause)**: `05.1.readme_sync.yml` modified `README.md` in earlier steps and then ran `git pull`, which aborted with *"Your local changes to README.md would be overwritten by merge"* — guaranteed to fail whenever a concurrent bot commit (e.g. the V2 Publisher's `[skip ci]` sync) advanced `develop` first. Rewrote the commit step as a `fetch → reset --hard origin/develop → regenerate → commit → push` retry loop. Since `README.md` is a *pure function* of the inventory, hard-resetting to the freshest remote tip is always safe and removes the merge-conflict and `--ours/--theirs` confusion classes entirely. A push is now only rejected if the remote advances mid-attempt, in which case it retries from the new tip.

### Changed
- **Inventory Push Retries (03.1 / 03.2 / 03.3)**: The metadata, AI-analysis and Video-Hub workflows did a single `git pull --rebase && git push` with no retry, so any rejection from a concurrent push failed the run. Wrapped each in a 5-attempt rebase+push loop (matching the proven `09.weekly_digest.yml` idiom).
- **PR Guardian is now advisory (07.1)**: The AI presubmit is a heuristic that can misattribute pre-existing lines or mischaracterize a PR (it flagged an untouched `about.md` line on PR #392). It still posts its findings as a PR comment, but `continue-on-error: true` stops a non-zero exit from showing the PR as a blocking red ❌. Added PR-scoped `concurrency` so superseded runs are cancelled (saving CI minutes and Gemini calls).
- **Markdown Linter concurrency (07.2)**: Added PR/branch-scoped `concurrency` with `cancel-in-progress` so new commits supersede in-flight lint runs.

## [[2.9.12]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.12) - 2026-06-19

### Fixed
- **V2 In-Page Search/Tag Filter Disappeared**: The per-page resource search box with maturity tag-pills (`static/v2_filter.js`) stopped appearing on every page after `navigation.instant` was enabled in the `2026-06-19` MkDocs UX overhaul. The widget hooked only `DOMContentLoaded`, which under Material's instant (SPA) navigation fires solely on the first load — subsequent in-nav page swaps never re-injected it. Reworked the script to initialize through Material's `document$` observable (emits on every instant navigation, with a `DOMContentLoaded` fallback), guard against double-injection, bind the clickable-tag delegation once on `document`, and show a "no results" state. Cache-bust bumped to `?v=2.9.12`.

### Changed
- **Removed Redundant In-Page Table of Contents**: Dropped the Markdown `## Table of Contents` block from all 156 V2 content pages and from the renderer (`v2_optimizer.py`). It duplicated the theme's heading index and, on large pages, forced hundreds of links of scroll before any content (e.g. `kubernetes-tools` 297 lines, `kubernetes` 295, `demos` 227). Replaced by the MkDocs Material native sticky **"On this page"** TOC: removed `toc.integrate` and added `toc.follow` in `v2-mkdocs.yml` so headings render in the right sidebar and track scroll position. The `tags.md` index page keeps its TOC (it *is* a navigation index).

## [[2.9.10]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.10) - 2026-06-19

### Fixed
- **README Sync Push Loop**: Rewrote the `05.1.readme_sync.yml` retry logic to use a push-first / merge-on-rejection loop instead of a pull-first / rebase loop. The old rebase loop never attempted a push after self-healing — it cycled back to `git pull --rebase`, hitting a fresh conflict on every iteration (×5) because a concurrent V2 sync workflow kept advancing `develop`. Additionally, `--ours` during a rebase refers to the *upstream* side, so the bot's README metrics were silently discarded each round. The fix: pull latest before committing (shrinks conflict window), then retry with `git merge -X ours` (correct semantics) after each rejected push.
- **Digest Table Broken by Pipe in Title**: Titles containing ` | ` (e.g. "Neo, Now in the Terminal | Pulumi Blog") broke the Markdown table in `tech-digest.md` because the unescaped pipe was parsed as a column separator. Root cause in `v2_optimizer.py`: the `why` column escaped pipes (`.replace("|", "-")`) but the link title `t` did not. Fixed with `.replace("|", r"\|")` on the title. The 4 already-rendered broken entries in `tech-digest.md` are corrected directly.

## [[2.9.9]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.9) - 2026-06-19

### Changed
- **Changelog Backfill**: Reconstructed the missing `2.6.0`–`2.9.1` entries from the GitHub Release notes, closing the gap where `CHANGELOG.md` had stalled at `2.5.8` while releases reached `2.9.x`. The changelog is now complete and continuous.

## [[2.9.8]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.8) - 2026-06-19

### Changed
- **Inventory `gh_pushed` Data Cleanup**: Normalized 281 existing inventory entries whose `gh_pushed` date field held the literal string `"N/A"` to `null`, completing the `2.9.4` source fix. Deterministic and CI-reproducible (`last_checked` already migrated to integer by the pipeline).
- **Changelog Maintenance**: Documented releases `2.9.2`–`2.9.8` in `CHANGELOG.md`.

## [[2.9.7]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.7) - 2026-06-19

### Fixed
- **Hero Card Height Consistency**: Aligned the emoji-based "Intelligence Digest" hero card with the other four logo cards on the V2 index by giving `.hero-badge-icon` a 100px flex-centered box in `v2_elite.css` (was ~32px tall). Cache-bust bumped to `?v=2.9.7`.

## [[2.9.6]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.6) - 2026-06-19

### Fixed
- **Deterministic Inventory Dump**: Stored `last_checked` as an `INTEGER` (epoch seconds) instead of a `REAL` in `inventory_manager.py`, normalizing the value on the entry before both the SQL and YAML dump. SQLite's version-specific `REAL`→text float printing previously rewrote ~every row of `inventory.sql` when regenerated outside CI. Verified `load→save` idempotent and byte-identical between local SQLite 3.40.1 and the CI-equivalent `python:3.11` (SQLite 3.46.1).

## [[2.9.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.5) - 2026-06-19

### Fixed
- **Index Outage (Runaway YouTube Mosaic)**: Fixed `reorganize_mosaic.load_inventory_channels()` selecting channels by `'youtube_mosaic' in entry` (key presence). Because the SQL round-trip materializes that column as an empty dict `{}` on every entry, the filter matched all ~18,647 inventory entries and emitted ~18.6k inline image links on a single line — producing a 4 MB `v2-docs/index.md` (and 2.9 MB `docs/index.md`) that hung both the V1 and V2 index pages. Now only entries with a non-empty `youtube_mosaic` dict and a logo image are rendered (136 curated channels).

## [[2.9.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.4) - 2026-06-19

### Fixed
- **`gh_pushed` Source Normalization**: The enrichment writers (`fast_enrich.py`, `gemini_utils.py`) now store `gh_pushed` as `None` when GitHub data is unavailable, instead of the string `"N/A"` that reached `datetime.fromisoformat()` downstream. `gh_license` keeps its displayed `"N/A"` string sentinel.
- **Curator Date-Parse Hardening**: Guarded the twin `fromisoformat()` call in `agentic_curator.py`'s MVQ-penalty check so a bad date value can't crash a curation batch.

### Added
- **Inventory Migration Script**: Added `scripts/normalize_gh_pushed.py` to clean existing `gh_pushed: "N/A"` rows.

## [[2.9.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.3) - 2026-06-19

### Fixed
- **Platinum Audit Null Handling**: Hardened `safety_guard.py` against null/`"N/A"` inventory fields. The MVQ compliance check no longer passes `"N/A"` to `datetime.fromisoformat()` or multiplies a `None` star count; the linguistic-tagging check no longer calls `None.lower()` on a null `language` (which had aborted the entire audit). Each mandate now runs in isolation so one bad entry cannot kill the whole report.

## [[2.9.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.2) - 2026-06-19

### Fixed
- **Dark-Theme CSS Flashes**: Removed `content-visibility: auto` from broad `<ul>`/`<ol>` selectors and `.v2-tag-section` in `v2_elite.css`. On the slate (dark) theme it caused black flashes while scrolling and made link lists below the index mosaic appear collapsed (intrinsic-size mismatch). The tags page already uses collapsed `<details>` for native render-skipping, so the optimization was redundant. Cache-bust bumped to `?v=2.9.2`.

## [[2.9.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.1) - 2026-06-19

### Changed
- **Incremental Digest Engine**: Each `(category × period)` cell in `news_digest.json` now stores a fingerprint (`entry_hash`, `entry_count`, `last_analyzed`, `method`) of its entry pool. Before calling Gemini, the engine checks the hash and staleness (`MAX_STALENESS_DAYS=30`) and reuses the stored result on a match — dropping Gemini calls from 66 to 0 when the inventory is unchanged, and to ~5–10 for a new ingestion batch.
- **Trending Badge Source**: The freshness badge now shows the actual Gemini analysis date from `_meta.last_updated`.

### Removed
- Redundant GitHub Actions digest cache (the committed `news_digest.json` is the persistent store) and the invalid `extra_head` key from `v2-mkdocs.yml`.

## [[2.9.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.9.0) - 2026-06-19

### Fixed
- **Portal Outage — Publisher/Deploy Safety**: Resolved a multi-bug portal outage. Pruning and nav sync are now skipped entirely in `--render-only` mode (CI uses it, and pruning had deleted pages that the render pass didn't regenerate); page deletion is gated on `_sync_enterprise_navigation` returning success; the fragile `nav:` regex was replaced with a string split; and the deploy now verifies the V2 build has a minimum page count (50+ HTML pages + `index.html`) before overwriting V1, falling back to V1-only if V2 looks broken. Pages in `self.dimensions` are never pruned.

## [[2.8.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.8.5) - 2026-06-19

### Fixed
- **V2 Build**: Removed the invalid `extra_head` key from `v2-mkdocs.yml` (was breaking V2 HTML generation) and fixed a broken `digital-money.md → finops.md` redirect (now points to `kubernetes.md` since `finops.md` was removed by the publisher).

## [[2.8.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.8.4) - 2026-06-19

### Fixed
- **Comprehensive None-Stars Guard**: Replaced all `.get('stars', 0)` patterns in `v2_optimizer.py` with `.get('stars') or 0`, fixing `TypeError: '>=' not supported between NoneType and int` in `_render_single_link` and 13 other comparison/arithmetic sites.

## [[2.8.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.8.3) - 2026-06-19

### Added
- **Digest Cache**: The publisher and weekly cron now cache `data/news_digest.json` with a day-scoped key (`news-digest-YYYY-MM-DD`). Same-day re-runs restore from cache and skip Gemini entirely (~20 min CI + 66 API calls saved per skipped run).

## [[2.8.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.8.2) - 2026-06-19

### Fixed
- **None-Stars Sort Crashes**: Fixed three `-x.get('stars', default)` sites in `v2_optimizer.py` that crashed with `TypeError: bad operand for unary -: 'NoneType'` when `stars` was null, using the `-(x.get('stars') or default)` pattern (`sort_rec`, `trending_pool`, `sorted_links`).

## [[2.8.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.8.1) - 2026-06-19

### Fixed
- **None `resource_type` Crash**: Fixed `AttributeError: 'NoneType' object has no attribute 'lower'` in `_calculate_tags` when `resource_type` was present but null, via `(item.get('resource_type') or 'Reference')`.

## [[2.8.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.8.0) - 2026-06-19

### Added
- **geo_region Inference**: `_infer_geo_from_url()` maps URL TLDs to regions (`.es`→España, EU TLDs→Europe, APAC TLDs→Asia-Pacific, Americas TLDs→Americas), populating the industry digest.
- **Freshness Badge**: The Trending section header shows an `Updated <date>` pill derived from `news_digest.json` mtime.
- **Search Boost**: `tech-digest.md` and `industry-digest.md` are generated with `search.boost: 2` frontmatter.
- **RSS Feed**: New `src/rss_generator.py` emits `v2-docs/feed.xml` (top-20 from the 3-month digest) with autodiscovery links, at `https://nubenetes.com/feed.xml`.
- **Weekly Cron**: `.github/workflows/09.weekly_digest.yml` runs Mondays 06:00 UTC to regenerate the digest and trigger the publisher.

## [[2.7.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.7.1) - 2026-06-19

### Changed
- **Cleaner Index**: Removed the `digest-preview` list from the index — the trending cards already show the same content with better design. Flow is now hero amber card → trending cards → `/tech-digest/`.

## [[2.7.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.7.0) - 2026-06-19

### Added
- **Intelligence Digest Hero Card**: New amber `Intelligence Digest` card on the V2 index linking to `/tech-digest/`, plus a `digest-preview` mini-block showing the top pick from 5 priority categories. New `hero-badge-card--amber` and `digest-preview` CSS components.

## [[2.6.9]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.9) - 2026-06-19

### Fixed
- **NoneType Crashes Across Pipeline**: Inventory entries with `stars: null` crashed `_calculate_tags` (`v2_optimizer.py`), the title-dedup index and entry scoring (`dedup.py`), and category sorting (`news_digest.py`). Replaced `.get("stars", 0)` with `.get("stars") or 0`.

## [[2.6.8]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.8) - 2026-06-19

### Fixed
- **Unbounded License Check**: `detect_license_changes()` iterated every entry with `gh_license` set (thousands of GitHub API calls). Applied the `MAX_REPOS_DEFAULT=200` cap, bringing total enrichment time to ~3–4 min.

## [[2.6.7]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.7) - 2026-06-19

### Changed
- **Enrichment 7.5× Faster**: Reduced GitHub activity enrichment from 2 API calls/repo to 1 (`open_issues_count` already includes PRs), capped at 200 repos/run, 0.5s delay, with 429 backoff — ~100s vs 12.5 min.

## [[2.6.6]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.6) - 2026-06-19

### Fixed
- **CNCF Enrichment API**: The CNCF Landscape API became a SPA and stopped returning JSON. Enrichment now queries the GitHub Search API with official CNCF maturity topics (`cncf-graduated`/`cncf-incubating`/`cncf-sandbox`) using the existing `GH_TOKEN`.

## [[2.6.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.4) - 2026-06-19

### Fixed
- **Differentiated Digest Periods**: 3/6/12-month windows now yield 10/15/20 items per category; backfilled `discovered_at` entries appear in wider windows; null-`stars` entries no longer crash the generator.

## [[2.6.3]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.3) - 2026-06-19

### Added
- **First Real Intelligence Digest**: Generated locally with 0 Gemini tokens — 22 categories, 660 items (220 per period) from the 18,647-entry inventory, with star-based ranking (upgrades to AI ranking on the next keyed pipeline run).

## [[2.6.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.2) - 2026-06-19

### Fixed
- **Clean URL Policy**: Removed the `offline` plugin that forced `.html` suffixes on all V2 URLs (breaking SEO/deep-links) and added placeholder `tech-digest.md`/`industry-digest.md` pages to prevent 404s before the first Gemini run. `use_directory_urls: true` is now mandatory and `offline` permanently forbidden (documented in `CLAUDE.md`/`GEMINI.md`/`README`).

## [[2.6.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.1) - 2026-06-19

### Added
- **Agent Instructions**: Created `CLAUDE.md` (Gitflow, repo structure, build commands, conventions) and added a Gitflow section to `GEMINI.md` so both AI agents follow the branching model automatically.

## [[2.6.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.6.0) - 2026-06-19

### Added
- **AI-Powered Intelligence Digest**: 26-category news digest engine with Gemini ranking, 3/6/12-month temporal panels, Trending Now cards, and dedicated `tech-digest`/`industry-digest` pages with company & geo_region extraction.
- **Data Quality Pipeline**: CNCF Landscape integration, GitHub activity enrichment, license-change detection, a deduplication engine (URL + content-hash + 85% title similarity), and AI re-evaluation flagging for stale entries.
- **MkDocs UX Overhaul**: Enabled tags/RSS/minify/PWA plugins, instant navigation with prefetch, breadcrumbs, footer nav, and an announcement bar (28 improvements across 31 files, 4 new modules, 18,647 entries backfilled).

### Fixed
- **Disabled Plugins**: Fixed plugins being nested under `theme:` in MkDocs config (silently disabled since deployment).

## [[2.5.8]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.8) - 2026-06-18

### Added
- **Debate & Ingestion Documentation**: Documented the Fast-Pass screening evaluator, Twikit toggle, failure-aware domain timeouts, mobile identity rotation, and tag pagination limits in `README.md`.
- **Consensus Flow Visualization**: Redesigned the multi-agent consensus protocol Mermaid diagram in `README.md` to map the Fast-Pass screening logic.

## [[2.5.7]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.7) - 2026-06-18

### Added
- **Fast-Pass Debate Evaluator (Recommendation #3)**: Optimized the consensus debate engine in `src/v2_debate.py` with a Fast-Pass Evaluator tier using a single Flash model call. Borderline scores between 60 and 75 escalate to the full Multi-Agent panel (Security, SRE, AI Architect), while clear cases bypass it.
- **Resilient Health Checking (Recommendation #2)**: Introduced the `ENABLE_TWITTER_CURATION` toggle to optionally bypass Twikit/Playwright scraping. Integrates domain failure tracking in `src/memory/health_learning.json` to dynamically adjust timeouts and rotate User-Agents under consecutive failure conditions.
- **Tag Page Cap (Recommendation #5)**: Prevented tag page DOM bloat in `v2-docs/tags.md` by capping the rendered links per tag to 100 (sorted by stars and year) and adding fallback links to the V1 Historical Archive.

## [[2.5.6]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.6) - 2026-06-18

### Added
- **AI Agent Skill Runbook**: Integrated a local workspace operations skill at `.gemini/skills/awesome-kubernetes-ops/SKILL.md` to guide Antigravity interactive assistant commands, test checks, and release promotions.
- **AI Operations Documentation**: Expanded the `README.md` with a detailed collapsible section and Mermaid architecture diagram explaining the Division of Labor between automated cloud runners (`GEMINI.md` curation rules) and local interactive coding assistants (`SKILL.md` runbook).

## [[2.5.5]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.5) - 2026-06-18

### Added
- **Modern CSS Enhancements**: Implemented browser-native CSS enhancements in `v2_elite.css` including typographic header balancing (`text-wrap: balance`), orphan word prevention (`text-wrap: pretty`), native auto-sizing form inputs (`field-sizing: content`), and coarser target sizes (`min-block-size: 44px`) for mobile tag/button targets.
- **Unified Pipeline Concurrency**: Set up a shared static concurrency group `develop-git-write-lock` across workflows (`03.1`, `03.2`, `03.3`, `04.1`, `05.1`) to prevent git push race conditions on the `develop` branch.
- **Push Fail Recovery**: Enhanced the git push rebase retry loops in publisher and sync workflows to verify push success and back-off before retrying.

### Fixed
- **Markdown Horizontal Rule Linting**: Corrected horizontal rule style in `docs/about.md` to use four-hyphen `----` to comply with markdownlint rules.

## [[2.5.4]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.4) - 2026-06-18

### Added
- **AI Tool Integration**: Integrated verified references for Cursor AI Code Editor (`https://cursor.com`), Google Antigravity Agentic Platform (`https://antigravity.google`), Anthropic Claude Code CLI (`https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview`), GitHub Copilot Workspace, Copilot Agent Mode, and GitHub Actions continuous delivery best practices.
- **Centralized Metadata Registry**: Registered all new developer productivity and AI agent tools in the centralized `data/inventory.yaml` database.

### Fixed
- **V2 Link Parsing Regex**: Modified the parser in `v2_optimizer.py` to correctly identify and process links prefixed with `**(YYYY)**` year metadata.

## [[2.5.2]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.2) - 2026-06-18

### Added
- **V2 Root Relocation**: Relocated the V2 Elite Portal to the root domain (`/`) as the default experience for human visitors, resolving browser redirect lag.
- **V1 Subdirectory Migration**: Placed the exhaustive V1 Archive under the `/v1/` subdirectory to maintain the historical documentation hub.
- **V1 Fallback Routing**: Integrated a fallback mechanism in the deployment build script to copy V1 files to the root, preventing 404 errors on historical deep-links not present in V2.
- **Premium Hero Cross-Reference Banners**: Added highly visible tip banners on both V1 and V2 pages to easily cross-reference and navigate between the AI-Curated Elite portal and the Exhaustive Archive.

### Fixed
- **PR Guardian AI Fallback**: Fixed local git diff retrieval in `pr_guardian.py` under GHA shallow checkouts by enforcing `check=True` and automatically falling back to downloading the diff from the GitHub PR URL when local diff is empty.

## [[2.5.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.1) - 2026-06-18

### Added
- **Collapsible Tag Index Sections**: Wrapped heavy resource listings under each heading in `tags.md` inside `<details>` and `<summary>` blocks (collapsed by default).
- **CSS-Based Deferred Rendering**: Added `.v2-tag-section` CSS styles utilizing `content-visibility: auto` to defer layout and paint computations for offscreen tag listings.
- **Centralized Language Indexing**: Grouped Spanish-language and other non-English resources under their own language headings (e.g. `## Spanish Content`) in the tag index page.

### Changed
- **Taxonomy Table Color Consistency**: Aligned the `[SPANISH CONTENT]` tag color to `md-tag--warning` (orange) inside the home page taxonomy table.
- **Clickable Filter Anchors**: Updated the "Maturity Taxonomy" homepage table to point directly to the correct slug anchors in the technical tags index (e.g. `./tags/#spanish-content`).

### Fixed
- **Tags Page Performance Lag**: Excluded `v2_filter.js` from executing on the tags index page, resolving browser lockups and main-thread blocking caused by looping over 15,000 DOM elements.
- **Duplicate Type Tags**: Prevented redundant double-rendering of resource type tags (e.g. `[GUIDE]`) when they are already listed in the resource's tag metadata.

## [[2.5.0]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.5.0) - 2026-06-18

### Added
- **Interactive V2 Portal Tagging System (Phase 3)**: Introduced a robust technical tagging database and clickable tag filters in the V2 Elite Portal, complete with custom color badges and an autogenerated `tags.md` index file.
- **Client-Side Search and Filter**: Implemented an interactive client-side search/filter widget for the V2 Elite Portal, allowing real-time searching and filtering of resources.
- **Multi-Agent Debate Explanation**: Added documentation and a Mermaid diagram explaining the multi-agent debate simulator architecture to the README.
- **Offline Mock Debate Simulator**: Implemented a mock debate simulator framework (`MOCK_DEBATE=true`) for local validation and testing without hitting Gemini API quotas.

### Changed
- **SEO-Friendly Clean V2 URLs**: Enabled `use_directory_urls: true` for the V2 Elite Portal, removing the `.html` suffix globally to optimize search engine positioning.
- **V2 Video Hub Grid Layout**: Upgraded the V2 Video Hub overview and sections to display as high-density glassmorphic cards grids.
- **Updated Curation Mandates**: Revised Rule 19 in `GEMINI.md` to formally require `use_directory_urls: true` for both V1 and V2, ensuring absolute path robustness across all platforms.

### Fixed
- **Ecosystem Restoration from Corruption**: Reverted temporary database corruption in `data/inventory.yaml` and regenerated both V1 and V2 homepage channel mosaics.
- **Linter and Formatting Alignment**: Resolved markdown list syntax warnings and normalized URLs to maintain strict linting compliance.

## [[2.4.1]](https://github.com/nubenetes/awesome-kubernetes/releases/tag/v2.4.1) - 2026-06-15

### Changed
- **V2 Default Theme to Dark Mode**: Set the "slate" (dark) theme as the default for the V2 Elite Portal, ensuring a high-density "Cyber Cloud" first impression.
- **Theme Resilience**: Removed system color scheme preference detection for V2 to prevent automatic switching to light mode, while preserving the manual toggle for user choice.

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
