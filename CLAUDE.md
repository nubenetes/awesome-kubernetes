# CLAUDE.md — Nubenetes Project Instructions for Claude Code

## Git Workflow: Trunk-Based Development

This repository uses **Trunk-Based Development**. All agents MUST follow this branching model:

### Branches
- **`master`** — Canonical trunk (single source of truth for code, docs, inventory, CI schedules, and GitHub Pages deployment). Every release gets a **tag** and a **GitHub Release** directly from `master`.
- **`feat/*`**, **`fix/*`**, **`bot/*`** — Short-lived feature/automation branches created from `master` and merged back to `master` via Pull Request.
- **`gh-pages`** — Deployment artifact branch (if present). Never touch directly.

### Release Process (mandatory for all releases)
1. Create short-lived branch from `master`: `git checkout -b feat/description master`
2. Implement changes, test locally, commit, and push branch
3. Create PR: `gh pr create --base master --head feat/description`
4. Merge PR to `master`: `gh pr merge N --merge --delete-branch`
5. Tag directly on `master`: `git checkout master && git pull origin master && git tag -a vX.Y.Z -m "description"`
6. Push tag: `git push origin vX.Y.Z`
7. Create GitHub Release: `gh release create vX.Y.Z --title "..." --notes "..."`

### Versioning
- Current: `v2.11.1`
- Format: `v{major}.{minor}.{patch}`
- Major: breaking changes or major platform overhauls
- Minor: new features or architectural shifts (like Trunk migration, digest engine, Gen-4 AI selector)
- Patch: bug fixes, config tweaks

### Protected Branches
`master` and `gh-pages` are NEVER deleted. Branch cleanup runs bi-monthly (`08.1`) for merged and stale short-lived branches.

## Repository Structure

### Key Directories
- `docs/` — V1 source (exhaustive archive, source of truth)
- `v2-docs/` — V2 source (AI-curated elite portal, derived from V1)
- `src/` — Python pipeline source code
- `data/` — Inventory (YAML + SQL), config files, digest JSON
- `scripts/` — Utility scripts (backfill, etc.)
- `.github/workflows/` — CI/CD (15 workflows)

### Key Config Files
- `v2-mkdocs.yml` — V2 MkDocs Material configuration
- `mkdocs.yml` — V1 MkDocs configuration
- `data/inventory.yaml` / `data/inventory.sql` — Unified inventory (18K+ entries)
- `data/curation_sources.yaml` — RSS feeds and X/Twitter accounts
- `data/link_rules.yaml` — Curation policies
- `GEMINI.md` — AI mandates and learning roadmap (read by Gemini agents)

### Pipeline Modules
- `src/v2_optimizer.py` — Main rendering engine (V2VisionEngine class)
- `src/news_digest.py` — 26-category temporal digest with Gemini ranking
- `src/enrichment.py` — CNCF Landscape + GitHub activity + license detection
- `src/dedup.py` — URL/hash/title deduplication engine
- `src/agentic_curator.py` — Ingestion pipeline with AI evaluation
- `src/autonomous_discovery.py` — GitHub trending discovery (14 queries)
- `src/gemini_utils.py` — Gemini API wrapper with key rotation
- `src/inventory_manager.py` — Dual YAML+SQL inventory management

## Build and Run

### Local testing (no API keys needed)
```bash
pip install -r requirements.txt
mkdocs serve -f v2-mkdocs.yml          # Preview V2 portal
mkdocs serve -f mkdocs.yml             # Preview V1 portal
```

### Pipeline commands
```bash
python3 -m scripts.backfill_discovered_at   # Backfill discovered_at field
python3 -m src.news_digest                   # Generate digest (needs Gemini API key)
python3 -m src.enrichment                    # CNCF + GitHub enrichment (needs GH_TOKEN)
python3 -m src.dedup                         # Dedup scan (dry-run by default)
python3 -m src.v2_optimizer --render-only    # Render V2 portal (no AI calls)
```

## Coding Conventions
- All Python exceptions must use `except Exception as e: log_event(f"[WARN] context: {str(e)[:100]}")` — never bare `except: pass`
- Use `from src.logger import log_event` for logging
- Use `from src.config import MADRID_TZ` for timezone-aware timestamps
- Inventory fields: `discovered_at` (ISO), `last_ai_eval` (ISO), `company`, `geo_region` must be preserved during merges
- The `update_inventory_entry()` function preserves `discovered_at` — never overwrite it with new data

## URL Policy: Clean URLs, No .html Suffix
Both V1 and V2 MUST use `use_directory_urls: true` in their mkdocs.yml. This produces clean URLs like `/kubernetes/` instead of `/kubernetes.html`. **NEVER** enable the `offline` plugin — it forces `.html` suffixes on all URLs, breaking SEO and existing deep-links. This is a hard rule.

## RSS/Twitter Sources
RSS feeds are limited to those that actually work (many block bots). Don't add new RSS feeds without testing. Current working feeds are defined in `data/curation_sources.yaml`.
