# Nubenetes Intelligent Curation: Meta-Instructions & Learning Roadmap

Este archivo contiene las instrucciones acumuladas y la visión de largo plazo para el mantenimiento autónomo de Nubenetes.com. Los agentes de IA deben consultar este documento en cada iteración para garantizar la continuidad del aprendizaje.

## 🧠 Core Mandates (Mandatos Principales)

1.  **Preservación de la Información**: NUNCA elimines resúmenes, comentarios o estrellas (🌟) que acompañan a los enlaces. El bot solo debe actualizar la URL o reorganizar la posición del ítem, nunca borrar el contexto descriptivo.
2. **Aprendizaje Persistente**: Utiliza `src/memory/health_learning.json` para almacenar el conocimiento sobre dominios (bloqueos anti-bot, estrategias exitosas) y patrones de navegación.
3. **Minimum Viable Quality (MVQ)**: For GitHub/GitLab repositories, the bot MUST check the last commit date. If the repository has had NO activity (commits) in more than **4 years**, it must receive a significantly lower `impact_score` and be deprioritized, even if the content remains technically relevant. This ensures Nubenetes stays fresh and focuses on maintained projects.
4. **Style Guide (Descriptive Summaries)**: All injected summaries MUST follow a **Descriptive** style. Avoid generic "clickbait" or action-oriented phrases (e.g., "Check this out"). Instead, provide a clear, neutral description of what the resource contains, its scope, and why it is technically significant for the Kubernetes ecosystem.
5. **Semantic Interlinking**: The bot should identify related categories for each resource. While the full entry is injected into the primary category, a short reference (*"See also: [Title](URL) in [Category]"*) should be added to up to two related categories to improve site navigation.
6. **Visual Health Dashboard**: Every curation run MUST generate a local `report.html` (outside the repo) for visual validation of metrics, quality (MVQ), and AI decisions.
7. **Resiliencia Total**: El workflow debe ser capaz de continuar incluso si hay errores individuales en validaciones de links o archivos. Prioriza generar un resultado (PR) aunque sea parcial.
8. **Consolidación de Repositorios**: Ante un fallo en un enlace profundo de GitHub/GitLab, intenta siempre validar la raíz del repositorio antes de darlo por muerto. Preferimos enlaces estables a raíces de repositorios que deep-links volátiles.
9. **Expansión de URLs**: Todos los enlaces acortados (t.co, bit.ly, buff.ly, etc.) DEBEN ser expandidos a su versión larga original antes de ser evaluados o inyectados. Esto garantiza la homogeneidad del inventario y mejora la precisión de la deduplicación global.
10. **Idioma Oficial (English Only)**: Todo el contenido inyectado (títulos, descripciones, encabezados), los logs de ejecución y las comunicaciones automatizadas (PRs) DEBEN ser exclusivamente en INGLÉS. Nubenetes es un recurso global y la consistencia lingüística es crítica.
11. **Workflow-Config Synchronization**: The GitHub Actions curation workflow form (`agentic_cron.yml`) MUST remain perfectly synchronized with the curation sources configuration file (`data/curation_sources.yaml`). Any addition, removal, or renaming of topics/categories in the configuration file requires a corresponding update to the workflow's input fields (checkboxes) to ensure users can toggle those sources manually. This maintain consistency between data-driven sources and the UI trigger.

## 🛠️ Structural Evolution & Navigation (Evolución Estructural)

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

## 🚀 Estrategias de Evasión de Bloqueos

El bot debe rotar entre perfiles para evitar ser detectado:
1.  **Desktop/Google**: Petición estándar de escritorio.
2.  **Mobile/Twitter**: Petición móvil con Referer de Twitter (alta tasa de éxito).
3.  **Playwright/LinkedIn**: Navegación real con JS habilitado.
4.  **Firefox/Reddit**: Perfil alternativo de escritorio.

## 📈 Diario de Aprendizaje (Historial de Mejoras)

*   **Mayo 2026**: Implementación inicial del motor autónomo con Playwright y Wayback Machine.
*   **Mayo 2026**: Añadido sistema de Evasión Multidimensional (5 intentos, rotación de perfiles).
*   **Mayo 2026**: Creación del `AgenticCurator` para auditoría de navegación y consolidación de repositorios.
*   **Mayo 2026**: Generación de PRs con analíticas visuales (Mermaid) y Matriz de Salud.
*   **Mayo 2026**: Implementación de Curaduría vía Backup (JSON/MD) para evitar bloqueos de X.com.
