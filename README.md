# Nubenetes: Awesome Kubernetes & Cloud

A curated list of awesome references collected since 2018.

My VSCode's plugins:

- [Agent Shadow Brain](https://github.com/theihtisham/agent-shadow-brain) - Self-evolving AI coding intelligence with infinite memory (TurboQuant), genetic algorithm self-evolution, predictive bug detection, PageRank knowledge graphs, swarm intelligence, and adversarial defense.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) Tables of Contents are automatically generated with this extension.
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- [Omni Skills Forge](https://github.com/theihtisham/omni-skills-forge) - 50,000+ curated AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Cline with visual dashboard, one-click install, and auto-update.

Apparently [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/) requires an indentation of 4 spaces, otherwise nested lists and Tables Of Contents won't be rendered as expected.

My VSCode's settings.json :

```json
{
    "markdown.extension.toc.levels": "2..6",
    "markdown.extension.tableFormatter.normalizeIndentation": true,
    "markdown.extension.toc.slugifyMode": "github",
    "markdown.extension.toc.orderedList": true,
    "markdown.extension.list.indentationSize": "adaptive",
    "files.autoSave": "afterDelay",
    "editor.detectIndentation": false,
    "editor.tabSize": 4,
    "window.zoomLevel": -1,
    "markdownlint.config": {
        "default": true,
        "MD013": false,
        "MD033": false,
        "MD007": { "indent": 4 },
        "no-hard-tabs": false
    },
    "editor.defaultFormatter": "vscode.github",
    "[markdown]": {
        "editor.defaultFormatter": "vscode.github"
    },
    "markdownlint.focusMode": false
}
```
