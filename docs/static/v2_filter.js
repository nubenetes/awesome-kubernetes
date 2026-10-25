// Nubenetes V2 — in-page resource search & tag filter widget.
//
// IMPORTANT: The V2 theme enables `navigation.instant` (SPA-style page swaps),
// so `DOMContentLoaded` fires only on the very first load. We therefore drive
// initialization through Material's `document$` observable, which emits on every
// (instant) navigation. We fall back to `DOMContentLoaded` when the observable
// is unavailable (e.g. instant nav disabled or local preview without the bundle).

(function () {
    "use strict";

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
            // Topic Map / Methodology list categories and legend rows, not
            // tagged resources: their <li> items carry no .md-tag, so the
            // maturity pills would always filter to zero and the "X of Y
            // resources" count is misleading. Skip them.
            h1.textContent.includes("Topic Map") ||
            h1.textContent.includes("Methodology")
        )) {
            return;
        }

        const filterContainer = document.createElement("div");
        filterContainer.className = "v2-filter-container";
        filterContainer.innerHTML = `
            <div class="v2-search-wrapper">
                <input type="text" class="v2-search-input" placeholder="Search resources in this page..." aria-label="Search resources in this page" />
                <span class="v2-search-clear" style="display:none;" title="Clear search">&times;</span>
            </div>
            <div class="v2-tag-pills">
                <button class="v2-pill active" data-filter="all">All</button>
                <button class="v2-pill" data-filter="DE FACTO STANDARD">De Facto Standard</button>
                <button class="v2-pill" data-filter="ENTERPRISE-STABLE">Enterprise Stable</button>
                <button class="v2-pill" data-filter="EMERGING">Emerging</button>
                <button class="v2-pill" data-filter="AI-MCP">AI &amp; MCP</button>
                <button class="v2-pill" data-filter="FRESH-2025-2026">Fresh (2025–2026)</button>
                <button class="v2-pill" data-filter="GUIDE">Guide</button>
                <button class="v2-pill" data-filter="CASE STUDY">Case Study</button>
                <button class="v2-pill" data-filter="COMMUNITY-TOOL">Community Tool</button>
                <button class="v2-pill" data-filter="SPANISH">Spanish</button>
            </div>
            <div class="v2-filter-stats">
                <span>Showing <strong class="v2-visible-count">0</strong> of <strong class="v2-total-count">0</strong> resources</span>
                <span class="v2-active-filters" style="font-style: italic;"></span>
                <span class="v2-no-results" style="display:none; color: var(--md-typeset-color); opacity:.75;">No resources match your filter.</span>
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
        const pills = filterContainer.querySelectorAll(".v2-pill");
        const visibleCountSpan = filterContainer.querySelector(".v2-visible-count");
        const totalCountSpan = filterContainer.querySelector(".v2-total-count");
        const noResultsSpan = filterContainer.querySelector(".v2-no-results");

        // Collect filter targets (resource <li> and details.note blocks).
        const targets = [];
        listItems.forEach(item => {
            if (item.querySelector("a")) {
                targets.push({
                    element: item,
                    type: "li",
                    text: item.textContent.toLowerCase(),
                    tags: Array.from(item.querySelectorAll(".md-tag")).map(t => t.textContent.toUpperCase())
                });
            }
        });
        detailsItems.forEach(detail => {
            const summary = detail.querySelector("summary");
            targets.push({
                element: detail,
                type: "details",
                text: detail.textContent.toLowerCase(),
                tags: summary ? [summary.textContent.toUpperCase()] : []
            });
        });

        totalCountSpan.textContent = targets.length;
        visibleCountSpan.textContent = targets.length;

        let activeFilter = "all";
        let searchText = "";

        function updateFilters() {
            let visibleCount = 0;

            targets.forEach(item => {
                let matchesSearch = true;
                let matchesPill = true;

                if (searchText) {
                    matchesSearch = item.text.includes(searchText);
                }

                if (activeFilter !== "all") {
                    if (activeFilter === "SPANISH") {
                        matchesPill = item.tags.some(tag => tag.includes("SPANISH"));
                    } else if (activeFilter === "AI-MCP") {
                        matchesPill = item.tags.some(tag =>
                            ["[AI]", "[MCP]", "[LLM]", "[GPU]", "[MLOPS]"].some(k => tag.includes(k))
                        ) || /\b(mcp|llm|vllm|gpu|agentic)\b/.test(item.text);
                    } else if (activeFilter === "FRESH-2025-2026") {
                        matchesPill = item.text.includes("(2026)") || item.text.includes("(2025)");
                    } else {
                        matchesPill = item.tags.some(tag => tag.includes(activeFilter));
                    }
                }

                if (matchesSearch && matchesPill) {
                    item.element.classList.remove("v2-filtered-hidden");
                    visibleCount++;
                } else {
                    item.element.classList.add("v2-filtered-hidden");
                }
            });

            visibleCountSpan.textContent = visibleCount;
            noResultsSpan.style.display = visibleCount === 0 ? "inline" : "none";

            // Hide section headings whose every resource is filtered out.
            const headings = Array.from(contentArea.querySelectorAll("h2, h3, h4"));
            headings.forEach(heading => {
                let next = heading.nextElementSibling;
                let totalItemsInSection = 0;
                let hiddenItemsInSection = 0;

                while (next && !["H1", "H2", "H3", "H4"].includes(next.tagName)) {
                    if (next.tagName === "UL") {
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
        }

        searchInput.addEventListener("input", function (e) {
            searchText = e.target.value.toLowerCase().trim();
            searchClear.style.display = searchText ? "block" : "none";
            updateFilters();
        });

        searchClear.addEventListener("click", function () {
            searchInput.value = "";
            searchText = "";
            searchClear.style.display = "none";
            updateFilters();
            searchInput.focus();
        });

        pills.forEach(pill => {
            pill.addEventListener("click", function () {
                pills.forEach(p => p.classList.remove("active"));
                this.classList.add("active");
                activeFilter = this.getAttribute("data-filter");
                updateFilters();
            });
        });
    }

    // Make tag badges anywhere in the content act as filter triggers.
    // Bound once on `document` (which survives instant navigation) and resolves
    // the current page's widget lazily, dispatching native events so the
    // per-page listeners above stay the single source of truth.
    function bindTagClicksOnce() {
        if (window.__v2TagClickBound) return;
        window.__v2TagClickBound = true;

        document.addEventListener("click", function (e) {
            const tagSpan = e.target.closest(".md-tag");
            if (!tagSpan) return;
            if (e.target.closest(".v2-filter-container")) return;

            const filterContainer = document.querySelector(".v2-filter-container");
            if (!filterContainer) return;

            const pills = filterContainer.querySelectorAll(".v2-pill");
            const searchInput = filterContainer.querySelector(".v2-search-input");

            let tagText = tagSpan.textContent.trim().replace(/[\[\]]/g, "").toUpperCase();
            if (tagText.includes("CONTENT")) tagText = tagText.replace(" CONTENT", "");

            const matchingPill = Array.from(pills).find(p => p.getAttribute("data-filter") === tagText);
            if (matchingPill) {
                // Reset search, then activate the matching maturity pill.
                searchInput.value = "";
                searchInput.dispatchEvent(new Event("input", { bubbles: true }));
                matchingPill.click();
            } else {
                // Treat fine-grained technical tags as a search query.
                const allPill = Array.from(pills).find(p => p.getAttribute("data-filter") === "all");
                if (allPill) allPill.click();
                searchInput.value = tagSpan.textContent.trim().toLowerCase();
                searchInput.dispatchEvent(new Event("input", { bubbles: true }));
            }
            filterContainer.scrollIntoView({ behavior: "smooth", block: "nearest" });
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

                this.innerHTML = "";
                this.appendChild(iframe);
                this.style.cursor = "default";
            });
        });
    }

    function init() {
        initFilterWidget();
        initLazyVideos();
    }

    bindTagClicksOnce();

    // Material exposes `document$` (an RxJS observable) that emits on every
    // instant navigation. Prefer it; fall back to DOMContentLoaded otherwise.
    if (typeof window.document$ !== "undefined" && typeof window.document$.subscribe === "function") {
        window.document$.subscribe(init);
    } else {
        document.addEventListener("DOMContentLoaded", init);
    }
})();
