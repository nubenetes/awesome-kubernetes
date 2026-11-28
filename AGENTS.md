# AGENTS.md — Universal Agent Instructions for Nubenetes

This file is the canonical, vendor-neutral operational guide for **all AI coding agents** working in `nubenetes/awesome-kubernetes` (Antigravity, Gemini CLI, Claude Code, GitHub Copilot, OpenAI Codex, Cursor, Windsurf).

## How Instruction Files Coexist in This Repository

- **`AGENTS.md` (this file)**: Concise operational rules, Trunk-Based Git workflow, Safe PR Gatekeeper governance, coding conventions, and verification commands for all agents.
- **[`GEMINI.md`](GEMINI.md)**: Exhaustive 61-mandate curation constitution and architectural history. **Do not remove or reformat its `## 🧠 Core Mandates` numbered list** — [`src/mandate_ingestor.py`](src/mandate_ingestor.py) parses `GEMINI.md` programmatically at runtime (`Doc-as-Behavior Mandate Bridge`). Keep `AGENTS.md` and `GEMINI.md` aligned when governance rules change.
- **[`CLAUDE.md`](CLAUDE.md)**: Lightweight Claude Code quick-reference synced with `AGENTS.md`.

---

## 1. Dual-Edition Architecture & Source of Truth

- **`docs/` (V1 Exhaustive Archive — Source of Truth)**: 185+ human- and AI-curated category pages (`>20,800` links). Preserve existing titles, manual descriptions, deep links, and `🌟` badges (Mandates 1, 8, 10).
- **`v2-docs/` (V2 Agentic Elite Portal — Derived View)**: Rendered deterministically from `docs/` + `data/inventory.yaml` via `python3 -m src.v2_optimizer --render-only` (`04.1. V2 Publisher`). External contributors never edit `v2-docs/` directly.
- **`data/inventory.sql` & `data/inventory.yaml`**: Coexisting SQLite dump + YAML mirror managed through [`src/inventory_manager.py`](src/inventory_manager.py). Never discard database updates during curation runs.

---

## 2. Git Workflow: Trunk-Based Development

- **`master`**: Single canonical trunk for code, `docs/`, `v2-docs/`, inventory databases, scheduled crons, and GitHub Pages deployments.
- **`feat/*`, `fix/*`, `bot/*`**: Short-lived branches created from `master` and merged back into `master` via Pull Request (`gh pr create --base master`).
- **Protected branches**: `master` and `gh-pages` MUST NEVER be force-pushed or deleted.
- **Releases**: Cut annotated SemVer tags (`git tag -a vX.Y.Z`) and GitHub Releases directly from `master` after PR merge, updating [`CHANGELOG.md`](CHANGELOG.md).

---

## 3. Safe PR Gatekeeper & Auto-Merge Governance (`07.2` -> `07.1`)

Every Pull Request targeting `master` is governed by a **2-Stage Fork-Safe Pipeline** designed for zero "Pwn Request" exposure and €0.00 AI token operation:

1. **Stage 1 — Untrusted PR Sandbox ([`.github/workflows/07.2.markdown_linter.yml`](.github/workflows/07.2.markdown_linter.yml))**:
   - Runs on `pull_request` (`opened`, `synchronize`, `reopened`, `ready_for_review`) with `permissions: contents: read` and **0 secrets**.
   - Validates Markdown syntax via `markdownlint-cli2` without executing Python code from untrusted forks.
2. **Stage 2 — Trusted Gatekeeper & Auto-Merger ([`.github/workflows/07.1.pr_guardian.yml`](.github/workflows/07.1.pr_guardian.yml) + [`src/pr_guardian.py`](src/pr_guardian.py))**:
   - Triggered via `workflow_run` after `07.2. Markdown Linter` completes, hourly `schedule` (with fast-exit check so idle sweeps consume `0` setup/AI tokens), or manually via `workflow_dispatch` with a PR number or `all_open`.
   - **Security Invariant**: Checks out **ONLY `ref: master`** and reads PR file lists, patches, and blobs as untrusted data via the GitHub API.
   - **Author Authority Tiers**:
     - **Maintainer (`inafev`)**: Full structural authority across V1, V2, `src/`, `data/`, `.github/`, `README.md`, and MkDocs configs. Auto-approved and merged (`€0.00` / 0 AI tokens) once Stage 1 lint, 15-section `README.md` validation, and Clean URL config checks pass.
     - **Trusted Automation (`dependabot[bot]` & same-repo `bot/*` branches)**: Auto-approved and merged (`€0.00` / 0 AI tokens) for minor/patch dependency updates and passing `SafetyGuard` curation runs; major SemVer jumps or code/workflow edits are held open for `@inafev`.
     - **External Contributors (`author != 'inafev'`) — 4-Gate Funnel**:
       1. **Gate 1 — Deterministic Structural Lock (0 tokens)**: Only `modified` files in existing `docs/<category>.md` pages (excluding `docs/index.md` and `docs/about.md`, max 5 files / 10 new links). Any touch to `v2-docs/**`, `mkdocs.yml`, `v2-mkdocs.yml`, `src/**`, `data/**`, `.github/**`, `README.md`, file additions/deletions/renames, `#`–`######` headings, TOC entries, raw HTML, or removal/modification of existing curated lines causes the bot to **leave the PR open**, apply `needs-maintainer-review`, and post a clear explanation for `@inafev`.
       2. **Gate 2 — Live URL & MVQ Verification (0 tokens)**: Multi-profile HTTP probe requiring `200 OK`, blocking soft-404s, parked domains, URL shorteners, tracking params (`utm_*`), and generic-homepage redirects (Mandate 35), plus GitHub REST API checks (`archived == false`, last push `<= 4` years per Mandate 3, permissive FOSS license per Mandate 37).
       3. **Gate 3 — Semantic Category & Section Fit (€0.00 Free Tier -> Flash-Lite)**: Compares the submitted entry against live-scraped `<title>`, `<meta description>`, and GitHub `topics` + 3 sibling links in the exact target `## / ###` section. Cascades from **GitHub Models (`permissions: models: read`, €0.00)** -> **`GEMINI_FREE_PR_KEY` (€0.00)** -> **Tier-1 Gemini Flash-Lite (~350 tokens)**, requiring `confidence >= 0.85` (fail-closed on outage).
       4. **Gate 4 — Auto-Approve, Merge & V2 Sync**: Approves, merges to `master` (or queues external fork PRs verified during `workflow_run` without an `AUTOMERGE_PAT` under label `automerge-verified`, completed in `0` AI tokens by the hourly `07.1` scheduled sweep running with `GITHUB_TOKEN`), and signals [`04.1. V2 Publisher`](.github/workflows/04.1.agentic_v2_publish.yml) (`--render-only`, 0 AI tokens) -> [`06.deploy_final.yml`](.github/workflows/06.deploy_final.yml) via `workflow_run`.

---

## 4. Non-Negotiable Engineering Guardrails

- **Clean URLs Policy**: Both [`mkdocs.yml`](mkdocs.yml) and [`v2-mkdocs.yml`](v2-mkdocs.yml) MUST keep `use_directory_urls: true`. **NEVER** enable the MkDocs `offline` plugin (forces `.html` suffixes and breaks SEO/deep links).
- **Zero-Token V2 Publisher**: [`04.1.agentic_v2_publish.yml`](.github/workflows/04.1.agentic_v2_publish.yml) MUST NOT reference `GEMINI_API_KEY` or `src.news_digest`.
- **README 15-Section Integrity**: Whenever modifying [`README.md`](README.md), preserve all 15 numbered `## N.` sections, synchronize the Table of Contents, avoid emojis and `&` (use `and`) in headings/TOC, use Euros (`€`) as primary currency in Section 7, and run `python3 src/safety_readme.py`.
- **Markdown & Mermaid Standards**: Every fenced code block must declare a language; link brackets must have no inner padding (`[Title](URL)`); Mermaid diagrams must quote node labels (`A["Label"]`) and wrap lines with `<br/>` (`<= 30` chars per line).
- **Python Error Handling**: Never use bare `except: pass`. Log exceptions via `from src.logger import log_event` (`except Exception as e: log_event(f"[WARN] context: {str(e)[:100]}")`) and use `MADRID_TZ` from `src.config` for timestamps.

---

## 5. Verification & Local Commands

```bash
# Run pipeline, model-selector, and PR Gatekeeper unit tests
python3 -m unittest discover -s tests -v

# Validate README 15-section and TOC integrity
python3 src/safety_readme.py

# Refresh MandateIngestor prompt cache after editing GEMINI.md
python3 -m src.mandate_ingestor

# Deterministic V2 portal render (0 AI tokens)
python3 -m src.v2_optimizer --render-only

# Preview portals locally
mkdocs serve -f v2-mkdocs.yml
mkdocs serve -f mkdocs.yml
```
