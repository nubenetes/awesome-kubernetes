"""MkDocs build hooks for the Nubenetes V2 portal.

Auto-versions cache-busted static assets so a CSS/JS change never goes stale
behind a hand-maintained `?v=` query string again (see v2.9.45 regression where
the Trending "Show more" disclosure was invisible to returning visitors because
`?v=` was pinned to 2.9.42).

The version is resolved from, in order:
  1. $SITE_VERSION  (set explicitly by the deploy workflow)
  2. the latest git tag (`git describe --tags --abbrev=0`)
If neither is available (e.g. a local `mkdocs serve` in a shallow checkout),
the asset URLs are left untouched so the build never fails.
"""
import logging
import os
import subprocess
from mkdocs.plugins import event_priority

log = logging.getLogger("mkdocs.hooks")

# Static assets whose URL should carry the release version as a cache-buster.
_VERSIONED_ASSETS = ("v2_elite.css", "v2_filter.js")


def _resolve_version():
    v = os.environ.get("SITE_VERSION", "").strip()
    if not v:
        try:
            v = subprocess.check_output(
                ["git", "describe", "--tags", "--abbrev=0"],
                stderr=subprocess.DEVNULL,
            ).decode().strip()
        except Exception:
            return None
    return v.lstrip("v") or None


def _bump(items, version):
    out = []
    for item in items:
        # extra_javascript entries may be plain strings or ExtraScript objects.
        path = item if isinstance(item, str) else getattr(item, "path", None)
        if path and any(name in path for name in _VERSIONED_ASSETS):
            new_path = f"{path.split('?')[0]}?v={version}"
            if isinstance(item, str):
                out.append(new_path)
            else:
                item.path = new_path
                out.append(item)
        else:
            out.append(item)
    return out


def on_config(config, **kwargs):
    version = _resolve_version()
    if not version:
        return config
    config["extra_css"] = _bump(config.get("extra_css", []), version)
    config["extra_javascript"] = _bump(config.get("extra_javascript", []), version)
    return config


@event_priority(40)
def on_env(env, *, config, files, **kwargs):
    """Guard against mkdocs-material PrivacyPlugin FileNotFoundError on transient network timeouts.

    PrivacyPlugin.on_env (priority 50) appends queued external assets to ``files``
    without verifying that ``_fetch()`` succeeded and wrote ``file.abs_src_path``
    to ``.cache/plugin/privacy``. If any external download times out (5s limit),
    ``files.copy_static_files()`` crashes the build with ``FileNotFoundError``.
    Running at priority 40 prunes any missing privacy-cache files before copy.
    """
    missing = [
        f for f in list(files)
        if getattr(f, "abs_src_path", None)
        and ".cache/plugin/privacy" in str(f.abs_src_path).replace("\\", "/")
        and not os.path.exists(f.abs_src_path)
    ]
    for f in missing:
        log.warning(
            "Pruning missing privacy-cached external asset (download timed out): %s",
            f.src_uri,
        )
        files.remove(f)
    return env
