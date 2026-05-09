# Nubenetes Intelligent Curation: Meta-Instructions & Learning Roadmap

Este archivo contiene las instrucciones acumuladas y la visión de largo plazo para el mantenimiento autónomo de Nubenetes.com. Los agentes de IA deben consultar este documento en cada iteración para garantizar la continuidad del aprendizaje.

## 🧠 Core Mandates (Mandatos Principales)

1.  **Preservación de la Información**: NUNCA elimines resúmenes, comentarios o estrellas (🌟) que acompañan a los enlaces. El bot solo debe actualizar la URL o reorganizar la posición del ítem, nunca borrar el contexto descriptivo.
2.  **Aprendizaje Persistente**: Utiliza `src/memory/health_learning.json` para almacenar el conocimiento sobre dominios (bloqueos anti-bot, estrategias exitosas) y patrones de navegación.
3.  **Resiliencia Total**: El workflow debe ser capaz de continuar incluso si hay errores individuales en validaciones de links o archivos. Prioriza generar un resultado (PR) aunque sea parcial.
4.  **Consolidación de Repositorios**: Ante un fallo en un enlace profundo de GitHub/GitLab, intenta siempre validar la raíz del repositorio antes de darlo por muerto. Preferimos enlaces estables a raíces de repositorios que deep-links volátiles.

## 🛠️ Evolución Estructural (Progressive Reorganization)

*   **Subsecciones Inteligentes**: El sistema debe detectar categorías superpobladas (>15 links) y proponer subdivisiones semánticas usando Gemini.
*   **Integridad de Navegación**: Cada cambio en los archivos markdown debe reflejarse en:
    *   `mkdocs.yml` (Menú horizontal/lateral).
    *   `docs/index.md` (Tabla de contenidos principal).
    *   El TOC interno de cada markdown (si lo tiene).
*   **Curación de Huérfanos**: Audita periódicamente la carpeta `docs/` para encontrar archivos no enlazados e intégralos en la navegación según su temática.

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
