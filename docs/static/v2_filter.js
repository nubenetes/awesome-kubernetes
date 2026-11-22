// Nubenetes V2 — in-page multi-filter, client-side sort, URL state & lazy video widget.
//
// IMPORTANT: The V2 theme enables `navigation.instant` (SPA-style page swaps),
// so `DOMContentLoaded` fires only on the very first load. We drive
// initialization through Material's `document$` observable, falling back to
// `DOMContentLoaded` when unavailable.

(function () {
    "use strict";

    function extractYear(text) {
        const match = text.match(/\((\d{4})\)/);
        return match ? parseInt(match[1], 10) : 0;
    }

    function extractGitHubStars(li) {
        const tags = li.querySelectorAll(".md-tag");
        for (const tag of tags) {
            const m = tag.textContent.match(/⭐\s*(\d+)/);
            if (m) return parseInt(m[1], 10);
        }
        return -1;
    }

    function initFilterWidget() {
        const contentArea = document.querySelector(".md-content__inner");
        if (!contentArea) return;

        // Guard against double-injection (document$ can emit more than once).
        if (contentArea.querySelector(".v2-filter-container")) return;

        // Only inject where there are resources to filter.
        const listItems = Array.from(contentArea.querySelectorAll("ul > li"));
        const detailsItems = Array.from(contentArea.querySelectorAll("details.note"));
        if (listItems.length === 0 && detailsItems.length === 0) return;

        // Skip on curated landing/index pages where the widget adds no value.
        const h1 = contentArea.querySelector("h1");
        if (h1 && (
            h1.textContent.includes("Nubenetes Elite Portal (V2)") ||
            h1.textContent.includes("Agentic Video Hub") ||
            h1.textContent.includes("Technical Tags Index") ||
            h1.textContent.includes("Intelligence Digest") ||
            h1.textContent.includes("Topic Map") ||
            h1.textContent.includes("Methodology")
        )) {
            return;
        }

        const filterContainer = document.createElement("section");
        filterContainer.className = "v2-filter-container";
        filterContainer.setAttribute("aria-label", "Resource filters");
        filterContainer.innerHTML = `
            <div class="v2-filter-top">
                <div class="v2-search-wrapper">
                    <label for="v2-search-input" class="visually-hidden">Search resources on this page</label>
                    <input id="v2-search-input" name="q" type="search" class="v2-search-input" placeholder="Search resources on this page..." autocomplete="off" />
                    <button type="button" class="v2-search-clear" hidden aria-label="Clear search">&times;</button>
                </div>
                <div class="v2-sort-group">
                    <label for="v2-sort-select" class="v2-sort-label">Sort</label>
                    <select id="v2-sort-select" name="sort" class="v2-sort-select">
                        <option value="default" selected>Impact (Default)</option>
                        <option value="newest">Newest Year</option>
                        <option value="stars">GitHub Stars</option>
                    </select>
                </div>
            </div>
            <div class="v2-tag-pills" role="group" aria-label="Filter by maturity, stack, or freshness">
                <button type="button" class="v2-pill active" data-filter="all" aria-pressed="true">All</button>
                <button type="button" class="v2-pill" data-filter="FRESH-2025-2026" aria-pressed="false">Fresh (2025–2026)</button>
                <button type="button" class="v2-pill" data-filter="HIDE-LEGACY" aria-pressed="false">Hide Legacy</button>
                <button type="button" class="v2-pill" data-filter="DE FACTO STANDARD" aria-pressed="false">De Facto Standard</button>
                <button type="button" class="v2-pill" data-filter="ENTERPRISE-STABLE" aria-pressed="false">Enterprise Stable</button>
                <button type="button" class="v2-pill" data-filter="EMERGING" aria-pressed="false">Emerging</button>
                <button type="button" class="v2-pill" data-filter="AI-MCP" aria-pressed="false">AI &amp; MCP</button>
                <button type="button" class="v2-pill" data-filter="RAG-OKF" aria-pressed="false">RAG &amp; OKF</button>
                <button type="button" class="v2-pill" data-filter="GITHUB" aria-pressed="false">GitHub</button>
                <button type="button" class="v2-pill" data-filter="GUIDE" aria-pressed="false">Guide</button>
                <button type="button" class="v2-pill" data-filter="CASE STUDY" aria-pressed="false">Case Study</button>
                <button type="button" class="v2-pill" data-filter="SPANISH" aria-pressed="false">Spanish</button>
            </div>
            <div class="v2-filter-stats">
                <span class="v2-stats-summary" aria-live="polite" aria-atomic="true">
                    Showing <strong class="v2-visible-count">0</strong> of <strong class="v2-total-count">0</strong> resources
                </span>
                <span class="v2-no-results" hidden>No resources match your active filters.</span>
            </div>
        `;

        // Insert directly after the main H1.
        if (h1 && h1.nextSibling) {
            h1.parentNode.insertBefore(filterContainer, h1.nextSibling);
        } else {
            contentArea.insertBefore(filterContainer, contentArea.firstChild);
        }

        const searchInput = filterContainer.querySelector(".v2-search-input");
        const searchClear = filterContainer.querySelector(".v2-search-clear");
        const sortSelect = filterContainer.querySelector(".v2-sort-select");
        const pills = Array.from(filterContainer.querySelectorAll(".v2-pill"));
        const allPill = pills.find(p => p.getAttribute("data-filter") === "all");
        const visibleCountSpan = filterContainer.querySelector(".v2-visible-count");
        const totalCountSpan = filterContainer.querySelector(".v2-total-count");
        const noResultsSpan = filterContainer.querySelector(".v2-no-results");

        // Collect filter targets (resource <li> and details.note blocks) with metadata for sort/filter.
        const targets = [];
        const sortableLists = new Map();
        let originalIndex = 0;

        listItems.forEach(item => {
            const anchor = item.querySelector("a[href]");
            if (!anchor) return;
            const textLower = item.textContent.toLowerCase();
            const tagsUpper = Array.from(item.querySelectorAll(".md-tag")).map(t => t.textContent.toUpperCase());
            const hrefLower = (anchor.getAttribute("href") || "").toLowerCase();
            const year = extractYear(textLower);
            const ghStars = extractGitHubStars(item);
            const idx = originalIndex++;
            const isCncfActive = tagsUpper.some(t => t.includes("CNCF GRADUATED") || t.includes("CNCF INCUBATING"));
            const isLegacy = tagsUpper.some(t => t.includes("LEGACY")) || Boolean(item.closest("details.archive")) || (year > 0 && year <= 2021 && !isCncfActive);

            const meta = {
                element: item,
                type: "li",
                text: textLower,
                tags: tagsUpper,
                isGitHub: hrefLower.includes("github.com/"),
                year,
                ghStars,
                isLegacy,
                originalIndex: idx
            };
            targets.push(meta);

            const parentUl = item.parentElement;
            if (parentUl && parentUl.tagName === "UL") {
                if (!sortableLists.has(parentUl)) sortableLists.set(parentUl, []);
                sortableLists.get(parentUl).push(meta);
            }
        });

        detailsItems.forEach(detail => {
            const summary = detail.querySelector("summary");
            const textLower = detail.textContent.toLowerCase();
            const year = extractYear(textLower);
            targets.push({
                element: detail,
                type: "details",
                text: textLower,
                tags: summary ? [summary.textContent.toUpperCase()] : [],
                isGitHub: textLower.includes("github.com"),
                year,
                ghStars: -1,
                isLegacy: year > 0 && year <= 2021,
                originalIndex: originalIndex++
            });
        });

        totalCountSpan.textContent = targets.length;
        visibleCountSpan.textContent = targets.length;

        const activeFilters = new Set();
        let searchText = "";
        let activeSort = "default";
        let liveDebounceTimer = null;

        function matchesSingleFilter(item, filterKey) {
            if (filterKey === "SPANISH") {
                return item.tags.some(tag => tag.includes("SPANISH"));
            }
            if (filterKey === "AI-MCP") {
                return item.tags.some(tag =>
                    ["[AI]", "[MCP]", "[LLM]", "[GPU]", "[MLOPS]", "[CLOUD-AI]"].some(k => tag.includes(k))
                ) || /\b(mcp|llm|vllm|gpu|agentic)\b/.test(item.text);
            }
            if (filterKey === "RAG-OKF") {
                return item.tags.some(tag =>
                    ["[RAG]", "[OKF]", "[GRAPHRAG]"].some(k => tag.includes(k))
                ) || /\b(rag|okf|open knowledge format|graphrag|pageindex|vectorless|mem0|graphiti|letta)\b/.test(item.text);
            }
            if (filterKey === "FRESH-2025-2026") {
                return item.year >= 2025;
            }
            if (filterKey === "HIDE-LEGACY") {
                return !item.isLegacy;
            }
            if (filterKey === "GITHUB") {
                return item.isGitHub;
            }
            return item.tags.some(tag => tag.includes(filterKey));
        }

        function syncPillStates() {
            const isAll = activeFilters.size === 0;
            pills.forEach(pill => {
                const key = pill.getAttribute("data-filter");
                const isActive = key === "all" ? isAll : activeFilters.has(key);
                pill.classList.toggle("active", isActive);
                pill.setAttribute("aria-pressed", String(isActive));
            });
        }

        function syncUrlState() {
            try {
                const url = new URL(window.location.href);
                if (searchText) {
                    url.searchParams.set("q", searchText);
                } else {
                    url.searchParams.delete("q");
                }
                if (activeFilters.size > 0) {
                    url.searchParams.set("f", Array.from(activeFilters).join(","));
                } else {
                    url.searchParams.delete("f");
                }
                if (activeSort !== "default") {
                    url.searchParams.set("sort", activeSort);
                } else {
                    url.searchParams.delete("sort");
                }
                window.history.replaceState(null, "", url.pathname + url.search + url.hash);
            } catch (_) {
                // Ignore history restrictions in sandboxed/file contexts.
            }
        }

        function applySort() {
            sortableLists.forEach((items, ul) => {
                if (items.length < 2) return;
                const sorted = items.toSorted((a, b) => {
                    if (activeSort === "newest") {
                        return (b.year - a.year) || (b.ghStars - a.ghStars) || (a.originalIndex - b.originalIndex);
                    }
                    if (activeSort === "stars") {
                        return (b.ghStars - a.ghStars) || (b.year - a.year) || (a.originalIndex - b.originalIndex);
                    }
                    return a.originalIndex - b.originalIndex;
                });
                const existingNonTargets = Array.from(ul.children).filter(child => !items.some(m => m.element === child));
                ul.replaceChildren(...sorted.map(m => m.element), ...existingNonTargets);
            });
        }

        function updateFilters(pushUrl = true) {
            let visibleCount = 0;

            targets.forEach(item => {
                const matchesSearch = !searchText || item.text.includes(searchText);
                let matchesAllPills = true;
                for (const key of activeFilters) {
                    if (!matchesSingleFilter(item, key)) {
                        matchesAllPills = false;
                        break;
                    }
                }

                if (matchesSearch && matchesAllPills) {
                    item.element.classList.remove("v2-filtered-hidden");
                    visibleCount++;
                } else {
                    item.element.classList.add("v2-filtered-hidden");
                }
            });

            // Auto-expand archive blocks when search matches inside them, or hide empty archive blocks.
            const hasActiveQuery = Boolean(searchText) || activeFilters.size > 0;
            contentArea.querySelectorAll("details.archive").forEach(archiveEl => {
                const archiveItems = Array.from(archiveEl.querySelectorAll("ul > li"));
                if (archiveItems.length === 0) return;
                const visibleArchive = archiveItems.filter(li => !li.classList.contains("v2-filtered-hidden")).length;
                if (visibleArchive === 0) {
                    archiveEl.classList.add("v2-filtered-hidden");
                } else {
                    archiveEl.classList.remove("v2-filtered-hidden");
                    if (searchText) {
                        archiveEl.open = true;
                    } else if (!hasActiveQuery) {
                        archiveEl.open = false;
                    }
                }
            });

            // Hide section headings whose every resource is filtered out.
            const headings = Array.from(contentArea.querySelectorAll("h2, h3, h4"));
            headings.forEach(heading => {
                let next = heading.nextElementSibling;
                let totalItemsInSection = 0;
                let hiddenItemsInSection = 0;

                while (next && !["H1", "H2", "H3", "H4"].includes(next.tagName)) {
                    if (next.tagName === "UL" || (next.tagName === "DETAILS" && next.classList.contains("archive"))) {
                        Array.from(next.querySelectorAll("li")).forEach(li => {
                            if (targets.some(t => t.element === li)) {
                                totalItemsInSection++;
                                if (li.classList.contains("v2-filtered-hidden")) hiddenItemsInSection++;
                            }
                        });
                    } else if (next.tagName === "DETAILS" && next.classList.contains("note")) {
                        totalItemsInSection++;
                        if (next.classList.contains("v2-filtered-hidden")) hiddenItemsInSection++;
                    }
                    next = next.nextElementSibling;
                }

                if (totalItemsInSection > 0 && totalItemsInSection === hiddenItemsInSection) {
                    heading.classList.add("v2-filtered-hidden");
                } else {
                    heading.classList.remove("v2-filtered-hidden");
                }
            });

            // Debounce live-region count announcements to avoid screen-reader spam while typing.
            clearTimeout(liveDebounceTimer);
            liveDebounceTimer = setTimeout(() => {
                visibleCountSpan.textContent = String(visibleCount);
                noResultsSpan.hidden = visibleCount !== 0;
            }, 150);

            if (pushUrl) {
                syncUrlState();
            }
        }

        // Restore shareable filter state from URLSearchParams on initial load.
        const initialParams = new URLSearchParams(window.location.search);
        const initQ = (initialParams.get("q") || "").trim();
        const initF = (initialParams.get("f") || "").trim();
        const initSort = (initialParams.get("sort") || "").trim();
        if (initQ) {
            searchInput.value = initQ;
            searchText = initQ.toLowerCase();
            searchClear.hidden = false;
        }
        if (initF) {
            const validKeys = new Set(pills.map(p => p.getAttribute("data-filter")));
            initF.split(",").forEach(k => {
                const trimmed = k.trim();
                if (trimmed && trimmed !== "all" && validKeys.has(trimmed)) {
                    activeFilters.add(trimmed);
                }
            });
            syncPillStates();
        }
        if (initSort && ["default", "newest", "stars"].includes(initSort)) {
            activeSort = initSort;
            sortSelect.value = initSort;
            applySort();
        }
        if (initQ || activeFilters.size > 0) {
            updateFilters(false);
        }

        searchInput.addEventListener("input", function (e) {
            searchText = e.target.value.toLowerCase().trim();
            searchClear.hidden = !searchText;
            updateFilters();
        });

        searchClear.addEventListener("click", function () {
            searchInput.value = "";
            searchText = "";
            searchClear.hidden = true;
            updateFilters();
            searchInput.focus();
        });

        sortSelect.addEventListener("change", function (e) {
            activeSort = e.target.value;
            applySort();
            syncUrlState();
        });

        pills.forEach(pill => {
            pill.addEventListener("click", function () {
                const key = this.getAttribute("data-filter");
                if (key === "all") {
                    activeFilters.clear();
                } else if (activeFilters.has(key)) {
                    activeFilters.delete(key);
                } else {
                    activeFilters.add(key);
                }
                syncPillStates();
                updateFilters();
            });
        });

        // Allow programmatic reset from tag-click handler.
        filterContainer.__resetAndFilter = function (tagText, rawText) {
            const matchingPill = pills.find(p => p.getAttribute("data-filter") === tagText);
            activeFilters.clear();
            if (matchingPill && tagText !== "all") {
                searchInput.value = "";
                searchText = "";
                searchClear.hidden = true;
                activeFilters.add(tagText);
                syncPillStates();
                updateFilters();
            } else {
                syncPillStates();
                searchInput.value = rawText;
                searchText = rawText.toLowerCase();
                searchClear.hidden = !searchText;
                updateFilters();
            }
            if (allPill) syncPillStates();
            filterContainer.scrollIntoView({ behavior: "smooth", block: "nearest" });
        };
    }

    // Make tag badges anywhere in the content act as filter triggers.
    function bindTagClicksOnce() {
        if (window.__v2TagClickBound) return;
        window.__v2TagClickBound = true;

        document.addEventListener("click", function (e) {
            const tagSpan = e.target.closest(".md-tag");
            if (!tagSpan) return;
            if (e.target.closest(".v2-filter-container")) return;

            const filterContainer = document.querySelector(".v2-filter-container");
            if (!filterContainer || typeof filterContainer.__resetAndFilter !== "function") return;

            let tagText = tagSpan.textContent.trim().replace(/[\[\]]/g, "").toUpperCase();
            if (tagText.includes("CONTENT")) tagText = tagText.replace(" CONTENT", "");
            filterContainer.__resetAndFilter(tagText, tagSpan.textContent.trim());
        });
    }

    // Lazy YouTube playback: click a poster to swap in the iframe.
    function initLazyVideos() {
        document.querySelectorAll(".video-lazy-container").forEach(container => {
            if (container.dataset.lazyBound) return;
            container.dataset.lazyBound = "1";
            container.addEventListener("click", function () {
                const videoUrl = this.getAttribute("data-video-url");
                const videoId = this.getAttribute("data-video-id");
                if (!videoUrl || !videoId) return;

                const iframe = document.createElement("iframe");
                iframe.setAttribute("width", "720");
                iframe.setAttribute("height", "405");
                const autoplayUrl = videoUrl.includes("?") ? `${videoUrl}&autoplay=1` : `${videoUrl}?autoplay=1`;
                iframe.setAttribute("src", autoplayUrl);
                iframe.setAttribute("title", "YouTube Video");
                iframe.setAttribute("frameborder", "0");
                iframe.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");
                iframe.setAttribute("allowfullscreen", "true");
                iframe.style.border = "none";
                iframe.style.width = "100%";
                iframe.style.height = "100%";
                iframe.style.borderRadius = "8px";

                this.replaceChildren(iframe);
                this.style.cursor = "default";
            });
        });
    }

    function init() {
        initFilterWidget();
        initLazyVideos();
    }

    bindTagClicksOnce();

    if (typeof window.document$ !== "undefined" && typeof window.document$.subscribe === "function") {
        window.document$.subscribe(init);
    } else {
        document.addEventListener("DOMContentLoaded", init);
    }
})();
