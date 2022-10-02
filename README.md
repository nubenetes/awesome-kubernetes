# Nubenetes: Awesome Kubernetes & Cloud

A curated list of awesome references collected since 2018.

My VSCode's plugins:

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

Apparently [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/) requires an indentation of 4 spaces, otherwise nested lists and Tables Of Contents won't be rendered as expected.

My VSCode's settings.json :

```json
{
    "markdown.extension.toc.levels": "2..6",
    "markdown.extension.tableFormatter.normalizeIndentation": true,
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
    }
}
```
