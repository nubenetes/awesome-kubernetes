# Visual Studio Code

1. [VSCode](#vscode)
2. [Updates](#updates)
3. [Keyboard shortcuts](#keyboard-shortcuts)
4. [Visual Studio MarketPlace and Extensions](#visual-studio-marketplace-and-extensions)
    1. [Publishers](#publishers)
    2. [Extensions](#extensions)
        1. [More Extensions](#more-extensions)
        2. [GitHub Copilot](#github-copilot)
        3. [More Extensions (Blogs)](#more-extensions-blogs)
        4. [Themes](#themes)
        5. [DevOps Extensions](#devops-extensions)
        6. [Azure DevOps Extensions](#azure-devops-extensions)
        7. [Git Flow Extensions](#git-flow-extensions)
        8. [Jenkins Extensions](#jenkins-extensions)
5. [Integrated Terminal on Visual Studio Code](#integrated-terminal-on-visual-studio-code)
6. [Debugging in VScode](#debugging-in-vscode)
7. [Python in Visual Studio Code](#python-in-visual-studio-code)
8. [Go in Visual Studio Code](#go-in-visual-studio-code)
9. [Bridge to Kubernetes](#bridge-to-kubernetes)
10. [AWS Toolkits](#aws-toolkits)
11. [Cloud Code](#cloud-code)
12. [Alternatives](#alternatives)
     1. [Intellij IDEA](#intellij-idea)
     2. [Online VSCode](#online-vscode)
13. [Youtube Shorts](#youtube-shorts)
14. [Videos](#videos)
15. [Tweets](#tweets)

## VSCode

- [code.visualstudio.com: Visual Studio Code](https://code.visualstudio.com/)
- [vscode.github.com: GitHub and Visual Studio Code 🌟](https://vscode.github.com/) Bring your workflows closer to your code. Learn how Visual Studio Code and GitHub are better together.
- [Visual Studio Online](https://visualstudio.microsoft.com/services/visual-studio-codespaces/)
- [Awesome Visual Studio Code](https://github.com/viatsko/awesome-vscode)
- [Using Version Control in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)
- [deepu.js.org: My VS Code setup - Making the most out of VS Code](https://deepu.js.org/make-the-most-out-of-vscode/)
- [VScode run from WSL in Linux: Cannot activate the 'Atlassian for VSCode (Official)' extension because 'git' extension is not loaded](https://bitbucket.org/atlassianlabs/atlascode/issues/112/cannot-activate-the-atlassian-for-vscode)
- [kite: Code Faster with AI Autocomplete](https://kite.com/)
- [With the Edge (Chromium) Tools for VS Code you can see the browser's Inspector and Dev Tools within VSCode, to debug your front-end code](https://gist.github.com/hxlnt/60d0e62efdb973e221e585e2b990bfd6)
- [docker.com: How to Develop Inside a Container Using Visual Studio Code Remote Containers 🌟](https://www.docker.com/blog/how-to-develop-inside-a-container-using-visual-studio-code-remote-containers/)
- [devblogs.microsoft.com: Need an Intro to VS Code? Let Tech with Tim Help!](https://devblogs.microsoft.com/python/need-an-intro-to-vs-code-let-tech-with-tim-help/)
- [A multi-step tutorial that covers the basics of working with Docker with Visual Studio Code and deploy on Azure](https://docs.microsoft.com/en-us/visualstudio/docker/tutorials/docker-tutorial)
- [thenewstack.io: This Week in Programming: All Hail Visual Studio Code](https://thenewstack.io/this-week-in-programming-all-hail-visual-studio-code/)
- [blogs.windows.com: Bringing the browser developer tools to Visual Studio Code](https://blogs.windows.com/msedgedev/2020/10/01/microsoft-edge-tools-vscode/)
- [visualstudiomagazine.com: Code with Fire! Top VS Code Tips](https://visualstudiomagazine.com/articles/2021/01/29/vs-code-tips.aspx)
- [39digits.com: How to sign your commits to GitHub using Visual Studio Code on Windows 10 and WSL2 🌟](https://www.39digits.com/signed-git-commits-on-wsl2-using-visual-studio-code)
- [jung-christian.de: Ansible support in Visual Studio Code 🌟](https://www.jung-christian.de/post/2021/02/ansible-vscode/)
- [youtube: Source Control Tip 9: Dealing with Merge Conflicts in VS Code](https://www.youtube.com/watch?v=ybCxPHzRJfA&ab_channel=VisualStudioCode)
- [dev.to: Video: Visualize the architecture of your Java app, in VS Code, in 2 ¹/₂ minutes](https://dev.to/appland/video-visualize-the-architecture-of-your-java-app-in-vs-code-in-2-minutes-568j)
- [serverless-stack.com: How to debug Lambda functions with Visual Studio Code](https://serverless-stack.com/examples/how-to-debug-lambda-functions-with-visual-studio-code.html)
- [github.blog: VS Code: Now creating pull requests 🌟](https://github.blog/2019-01-07-create-pull-requests-in-vscode/) Remember all those times you’ve wanted to manage a pull request but didn’t want to leave VS Code? Now they’re in the past. Create and manage them with the GitHub Pull Requests Extension.
- [dev.to: Using VS Code to git rebase](https://dev.to/colbygarland/using-vs-code-to-git-rebase-1lc)
- [freecodecamp.org: 10 VS Code Extensions to Increase Your Productivity](https://www.freecodecamp.org/news/10-vscode-extensions-to-increase-productivity/)
- [softzone.es: Mejora y añade más funciones a Visual Studio Code con plugins](https://www.softzone.es/programas/lenguajes/mejores-plugins-anadir-visual-code/)
- [dzone: VS Code Extensions for Frontend Developers](https://dzone.com/articles/7-vs-code-extensions-for-frontend-developers)
- In code 1.61.0, you can get a colorized bracket pair guide, just enable it by setting:
    - `"editor.guides.bracketPairs": true`
- [dev.to: How to configure VSCode Bracket Pair Colors Natively](https://dev.to/amanhimself/how-to-configure-vscode-bracket-pair-colors-natively-3nl)
- **Zen Mode:** Per user requests, we have added Zen Mode to VS Code. Zen Mode lets you focus on your code by hiding all UI except the editor (no Activity Bar, Status Bar, Sidebar and Panel) and going to full screen. Zen mode can be toggled using the View menu, Command Palette or by the shortcut Ctrl+K Z.
- [realpython.com: Advanced Visual Studio Code for Python Developers](https://realpython.com/advanced-visual-studio-code-python/)
- [blog.openreplay.com: 8 Cool VS Code tips to make your workspace more personal](https://blog.openreplay.com/8-cool-vs-code-tips-to-make-your-workspace-more-personal)
- [dev.to: Visual Studio Code - Tips & Tricks - Command Palette and its friends](https://dev.to/this-is-learning/visual-studio-code-tips-tricks-command-palette-and-its-friends-2bhi)
- [betterprogramming.pub: How To Update Your GitHub Repository in Visual Studio Code](https://betterprogramming.pub/how-to-update-your-github-repository-in-visual-studio-code-7bb9e8549cea) An overview to clone a repository, push changes, and make pull requests in VS code
- [dev.to/this-is-learning: Visual Studio Code - Tips & Tricks - Snippets](https://dev.to/this-is-learning/visual-studio-code-tips-tricks-snippets-5041)
- [dev.to/jcofman: Make VS Code better by editing and updating some settings](https://dev.to/jcofman/make-vs-code-better-by-editing-and-updating-some-settings-4m9a)
- [pythonsimplified.com: How to SSH into EC2 from VS Code](https://pythonsimplified.com/how-to-ssh-into-ec2-from-vs-code/)
- [levelup.gitconnected.com: 12 Visual Studio Code Shortcuts That Every Developer Must Know](https://levelup.gitconnected.com/12-visual-studio-code-shortcuts-that-every-developer-must-know-8d6ce5fc3631) These shortcuts make the lives of developers easier.
- [betterprogramming.pub: Generating Class Diagrams for .Net Core](https://betterprogramming.pub/generating-class-diagrams-for-net-core-c4913db9398b) Use PlantUML directly in the Visual Studio Code
- [freecodecamp.org: Best Colorful VSCode Extensions – How to Personalize Your Editor](https://www.freecodecamp.org/news/best-colorful-vscode-extensions-for-productivity/)
- [dev.to: VSCode Extensions I'm in LOVE with | Tina Huynh](https://dev.to/tmchuynh/vscode-extensions-im-in-love-with-oab)
- [towardsdatascience.com: VS Code for data science](https://towardsdatascience.com/vs-code-for-data-science-aee82fe08bac) How a good Visual Studio Code setup can make you a more productive data scientist
- [betterprogramming.pub: Learn to Code Remotely With VS Code And SSH](https://betterprogramming.pub/learn-to-code-remotely-with-vs-code-and-ssh-68c630759279)
- [austingil.com: VS Code Timeline Restores Lost Work That Git Can’t 🌟](https://austingil.com/vs-code-timeline-restores-work-git-cant/)
- [==developers.redhat.com: Remote container development with VS Code and Podman== 🌟](https://developers.redhat.com/articles/2023/02/14/remote-container-development-vs-code-and-podman)
- [==visualstudio.microsoft.com/services/live-share: Visual Studio Live Share== 🌟](https://visualstudio.microsoft.com/services/live-share/) Real-time collaborative development
- [freecodecamp.org: How to Use Markdown in VSCode – Syntax and Examples](https://www.freecodecamp.org/news/how-to-use-markdown-in-vscode/)
- [gijsreijn.medium.com: Optimizing Your DSC V3 Authoring Experience in VSCode](https://gijsreijn.medium.com/optimizing-your-dsc-v3-authoring-experience-in-vscode-bd8e90c52312)

## Updates

- [VSCode Updates](https://code.visualstudio.com/updates)
- [Flexible layout 🌟](https://code.visualstudio.com/updates/v1_46#_flexible-layout)

## Keyboard shortcuts

- [code.visualstudio.com: keyboard shortcuts for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [code.visualstudio.com: keyboard shortcuts for macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
    - [support.apple.com: Mac keyboard shortcuts](https://support.apple.com/en-us/HT201236)
    - [9to5mac.com: How-To: Remap Windows keyboards to match the Mac keyboard layout](https://9to5mac.com/2016/03/17/how-to-remap-windows-keyboard-buttons-match-mac-layout/)
    - [addictivetips.com: How to remap a Windows keyboard for a Mac](https://www.addictivetips.com/mac-os/remap-a-windows-keyboard-for-a-mac/)
- [code.visualstudio.com: keyboard shortcuts for Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

## Visual Studio MarketPlace and Extensions

- [marketplace.visualstudio.com](https://marketplace.visualstudio.com/)

### Publishers

- [Microsoft 🌟](https://marketplace.visualstudio.com/publishers/Microsoft)
- [Red Hat 🌟](https://marketplace.visualstudio.com/publishers/redhat)
- [AmazonWebServices](https://marketplace.visualstudio.com/publishers/AmazonWebServices)
- [Google Cloud](https://marketplace.visualstudio.com/publishers/GoogleCloudTools)
- [Oracle](https://marketplace.visualstudio.com/publishers/Oracle)

### Extensions

- [GitLens 🌟](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) Git supercharged
    - [GitLens interactive rebase](https://github.com/eamodio/vscode-gitlens#interactive-rebase-editor-)
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) View a Git Graph of your repository, and easily perform Git actions from the graph. Configurable to look the way you want!
- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
- [Markdown All in One 🌟](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
    - [A collapsible section containing markdown](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab)
- [Auto Markdown TOC By AX1](https://marketplace.visualstudio.com/items?itemName=livepdm.auto-markdown-toc-ax1)
- [Prettier:](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) Code formatter
- [Live Share:](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) Real-time collaborative development from the comfort of your favorite tools (pair-programming).
- [EditorConfig:](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) This plugin attempts to override user/workspace settings with settings found in .editorconfig files. No additional or vscode-specific files are required.
- [Polacode](https://marketplace.visualstudio.com/items?itemName=pnp.polacode)
- [ESLint:](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) Integrates [ESLint](https://eslint.org/) JavaScript into VS Code.
- [Indent-Rainbow:](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) Indent-Rainbow
A simple extension to make indentation more readable
- [Live Server:](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) Launch a development local Server with live reload feature for static & dynamic pages
- [SVG:](https://marketplace.visualstudio.com/items?itemName=jock.svg) SVG Coding, Minify, Pretty, Preview All-In-One.
- [Python Visual Studio Code](https://github.com/microsoft/vscode-python)
    - [twitter.com/pythonvscode](https://twitter.com/pythonvscode)
    - [Python in Visual Studio Code – September 2020 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-september-2020-release/)
    - [Python in Visual Studio Code – October 2020 Release. Debugpy 1.0](https://devblogs.microsoft.com/python/python-in-visual-studio-code-october-2020-release/)
- [betterprogramming.pub: The Best VS Code Extensions to Supercharge Your Git](https://betterprogramming.pub/the-best-vs-code-extensions-to-supercharge-your-git-5d5ab3f64f64) Yes, there’s more than GitLens!
- [dzone.com: 10 VS Code Extensions to Fight Technical Debt](https://dzone.com/articles/10-vs-code-extensions-to-fight-technical-debt) The best engineering teams I’ve talked to use the right tools to continuously refactor code, improve their codebase communication, and address technical debt.
- [dev.to: Superb VSCode extensions changing your coding life](https://dev.to/duckinm/superb-vscode-extensions-changing-your-coding-life-2cmb)
- [c-sharpcorner.com: The Best VS Code Extensions For Remote Working](https://www.c-sharpcorner.com/article/the-best-vs-code-extensions-for-remote-working/)
- [freecodecamp.org: VS Code Extensions to Increase Developer Productivity](https://www.freecodecamp.org/news/vs-code-extensions-to-increase-developer-productivity/)
- [dev.to: My Top 5 Visual Studio Code extensions for Azure Developers](https://dev.to/azure/my-top-5-visual-studio-code-extensions-for-azure-developers-1odo)
- [==hashicorp.com: Terraform extension for VS Code speeds up loading of large workspaces==](https://www.hashicorp.com/blog/terraform-extension-for-vs-code-speeds-up-loading-of-large-workspaces) New releases of the HashiCorp Terraform extension for Visual Studio Code and Terraform language server significantly reduce memory usage and start up time for large workspaces.

#### More Extensions

- [Prettier ESLint](https://marketplace.visualstudio.com/items?itemName=rvest.vs-code-prettier-eslint) Extension to format JavaScript code using prettier-eslint package
- [Rainbow Brackets](https://marketplace.visualstudio.com/items?itemName=2gua.rainbow-brackets) A rainbow brackets extension for VS Code.
- [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight) Highlight TODOs, FIXMEs, and any keywords, annotations
- [Todo+](https://marketplace.visualstudio.com/items?itemName=fabiospampinato.vscode-todo-plus) Manage todo lists with ease. Powerful, easy to use and customizable.
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) Show TODO, FIXME, etc. comment tags in a tree view
- [Babel JavaScript](https://marketplace.visualstudio.com/items?itemName=mgmcdermott.vscode-language-babel) VSCode syntax highlighting for today's JavaScript, ported from gandm's language-babel for Atom.
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) Improve highlighting of errors, warnings and other language diagnostics.
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) Makes it easy to create, manage, and debug containerized applications.
- [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv) Support for [DotENV](https://github.com/zaynali53/DotENV) file syntax
- [Jest](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest) Use Facebook's [Jest](https://github.com/facebook/jest), a delightful JavaScript Testing Framework.
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) Launch a development local Server with live reload feature for static & dynamic pages
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) This extension integrates Draw.io into VS Code.
- [Turbo Console Log](https://marketplace.visualstudio.com/items?itemName=ChakrounAnas.turbo-console-log) Automating the process of writing meaningful log messages.
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) Visual Studio Code plugin that autocompletes filenames
- [GitHub Pull Requests and Issues 🌟](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [React Pure To Class](https://marketplace.visualstudio.com/items?itemName=angryobject.react-pure-to-class-vscode) Convert pure react components to class components
- [Helm Intellisense](https://marketplace.visualstudio.com/items?utm_sq=ggv6n6jy52&itemName=Tim-Koehler.helm-intellisense&ssr=false#overview) Helm Intellisense is a Visual Studio Code extension that provides intellisense for helm-templates
- [Azure Resource Manager (ARM) Tools 🌟](https://marketplace.visualstudio.com/items?itemName=msazurermtools.azurerm-vscode-tools) New VS Code extension for working with Azure Resource Manager (ARM) templates that will make your life much easier.
- [developers.redhat.com: Devfiles and Kubernetes cluster support in OpenShift Connector 0.2.0 extension for VS Code 🌟](https://developers.redhat.com/blog/2020/11/16/devfiles-and-kubernetes-cluster-support-in-openshift-connector-0-2-0-extension-for-vs-code/)
    - [OpenShift Connector 🌟](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-openshift-connector)
- [gitlab.com: VS Code extension development with GitLab](https://about.gitlab.com/blog/2020/11/30/vscode-extension-development-with-gitlab/) As VS Code editor increases in popularity, find out how GitLab + VS Code can be used for extension development and how we develop the official GitLab VS Code extension.
- [freecodecamp.org: VS Code Extensions That'll Boost Your Development Productivity 🌟](https://www.freecodecamp.org/news/vs-code-extensions-to-boost-your-development-productivity/)
- [CloudFormation Snippets 🌟](https://marketplace.visualstudio.com/items?itemName=dsteenman.cloudformation-yaml-snippets) Adds autocompletion for all AWS CloudFormation resources. The snippets are updated automatically every week by fetching the data from the official AWS CloudFormation resource specification.
    - [dannys.cloud: Autocomplete your CloudFormation Resources in VS Code](https://dannys.cloud/autocomplete-cloudformation-resources-vs-code)
- [GitHub Actions 🌟](https://marketplace.visualstudio.com/items?itemName=cschleiden.vscode-github-actions)
- [Local History](https://marketplace.visualstudio.com/items?itemName=xyz.local-history) Save files into local history
- [Remote Repositories 🌟](https://code.visualstudio.com/blogs/2021/06/10/remote-repositories) You can now browse or even make edits to any GitHub repo straight from code, instantly WITHOUT having to pull the source down first.
- [marketplace.visualstudio.com: Bridge to Kubernetes (VSCode)](https://marketplace.visualstudio.com/items?itemName=mindaro.mindaro) With Bridge to Kubernetes, the only thing you need to run and debug on your development machine is the microservice you're working on and your preferred dev tools. - [thorsten-hans.com: Debugging apps in Kubernetes with Bridge 🌟](https://www.thorsten-hans.com/debugging-apps-in-kubernetes-with-bridge/) Bridge to Kubernetes simplifies and streamlines the process of debugging applications running in Kubernetes. Debug any language using the tools you prefer and love.
- [Working with Kubernetes in VS Code](https://code.visualstudio.com/docs/azure/kubernetes) Learn how to create a Kubernetes cluster, write a K8s manifest file (YAML), which tells K8s everything it needs to know about app, and finally deploy the app to the K8s cluster.
- [marketplace.visualstudio.com: GitHub Repositories 🌟](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub) Browse and edit code from Github without cloning. You can even review PRs!. The GitHub Repositories extension lets you quickly browse, search, edit, and commit to any remote GitHub repository directly from within Visual Studio Code, with support for Azure repos coming soon.
- [Azure/vscode-kubernetes-tools 🌟](https://github.com/Azure/vscode-kubernetes-tools) Visual Studio Code Kubernetes Tools
- [==snyk.io: Securing your open source dependencies with the Snyk Visual Studio Code extension==](https://snyk.io/blog/securing-open-source-dependencies-snyk-visual-studio-code-extension/)
- [prisma.io: Improving the Prisma Visual Studio Code Extension with WebAssembly 🌟](https://www.prisma.io/blog/vscode-extension-prisma-rust-webassembly) Prisma helps app developers build faster and make fewer errors with an open source database toolkit for PostgreSQL, MySQL, SQL Server, and SQLite. Central to Prisma is the schema - __a declarative way to define your app's data models and their relations that's human-readable__. And you don't have to painstakingly create it from scratch if you already have a database - prisma introspect takes care of that.
- [==IAM Legend==](https://marketplace.visualstudio.com/items?itemName=SebastianBille.iam-legend) IAM policy actions autocomplete, documentation & wildcard resolution. Supports Serverless Framework, AWS SAM, CloudFormation and Terraform.
- [GitLive](https://marketplace.visualstudio.com/items?itemName=TeamHub.teamhub) Extend VS Code with real-time collaborative superpowers
    - [dev.to/gitlive: GitLive now works with any Git repository in VS Code!](https://dev.to/gitlive/gitlive-now-works-with-any-git-repository-in-vs-code-304o)
- [marketplace.visualstudio.com: autoDocstring - Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [marketplace.visualstudio.com: Azure App Service for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice)
- [marketplace.visualstudio.com: CodeSnap](https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap) Take beautiful screenshots of your code
- [marketplace.visualstudio.com: GitOps Tools for Flux 🌟](https://marketplace.visualstudio.com/items?itemName=Weaveworks.vscode-gitops-tools) This is a VS Code extension for GitOps automation tool for continuous delivery of Kubernetes and cloud native applications
- [marketplace.visualstudio.com: Kubernetes Reference Highlighter 🌟](https://marketplace.visualstudio.com/items?itemName=dag-andersen.kubernetes-reference-highlighter) Kubernetes reference highlighter is a plugin for VS Code that highlights references in your Kubernetes YAML files
- [freecodecamp.org: Increase Your VS Code Productivity](https://www.freecodecamp.org/news/increase-your-vs-code-productivity/)
- [marketplace.visualstudio.com: Ruff extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) A Visual Studio Code extension for [Ruff](https://github.com/astral-sh/ruff), an extremely fast Python linter and code formatter, written in Rust.
- [marketplace.visualstudio.com: Learn Cloud 🌟](https://marketplace.visualstudio.com/items?itemName=azurepaas-tools.vscode-learncloud) Guiding first-time cloud users to deploy to Azure PaaS
- [==marketplace.visualstudio.com: Kubernetes YAML Formatter== 🌟](https://marketplace.visualstudio.com/items?itemName=kennylong.kubernetes-yaml-formatter) **A better YAML formatter for DevOps like Kubernetes, Ansible, CI/CD, etc.**

#### GitHub Copilot

- [==GitHub Copilot== 🌟](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [code.visualstudio.com: GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [techcommunity.microsoft.com: Unleashing GitHub Copilot for Infrastructure as Code (powershell, terraform, etc)](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/unleashing-github-copilot-for-infrastructure-as-code/ba-p/4124031)

#### More Extensions (Blogs)

- [Become a VS Code Ninja with these Extensions and Tools [2020]](https://dev.to/vikrantnegi/become-a-vs-code-ninja-with-these-extensions-and-tools-2020-1119)
- [blog.logrocket.com: Top 10 VS Code extensions for 2021](https://blog.logrocket.com/top-10-vs-code-extensions-2021/)
- [dev.to: Thunder Client - Http Client Extension for VS Code](https://dev.to/ranga_vadhineni/thunder-client-http-client-extension-for-vs-code-30i9) - [thunderclient.io 🌟](https://www.thunderclient.io) Hand-crafted lightweight Rest Client for Testing APIs (postman alternative) - [youtube: I Don't Need Postman Anymore!! I Use VS Code Instead...](https://www.youtube.com/watch?v=AbCTlemwZ1k&ab_channel=JamesQQuick)
- [c-sharpcorner.com: The Best VS Code Extensions To Supercharge Git](https://www.c-sharpcorner.com/article/the-best-vs-code-extensions-to-supercharge-git/)
- [dev.to: VS Code extensions to increase your Productivity](https://dev.to/harishash/vs-code-extensions-to-increase-your-productivity-eeb)
- [dev.to: Top 5 Best Git Extensions For VS Code (You must have)](https://dev.to/thenomadevel/top-5-best-git-extensions-for-vs-code-you-must-have-40b6)

#### Themes

- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) Material Design Icons for Visual Studio Code
- [Lucy Theme](https://marketplace.visualstudio.com/items?itemName=juliettepretot.lucy-vscode) Soft but clear syntax theme
- [Monokai Pro Theme](https://marketplace.visualstudio.com/items?itemName=monokai.theme-monokai-pro-vscode) Professional theme and matching icons, from the author of the original Monokai color scheme.
- [Codey Midnight Theme](https://marketplace.visualstudio.com/items?itemName=salesforce.codey-midnight) Dark theme configured for accessibility and Salesforce development
- [1984 Theme](https://marketplace.visualstudio.com/items?itemName=juanmnl.vscode-theme-1984)
- [Dracula Official](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula) Official Dracula Theme. A dark theme for many editors, shells, and more.
    - [Dracula Pro Theme 🌟](https://draculatheme.com/pro)
- [Discord Presence Theme](https://marketplace.visualstudio.com/items?itemName=icrawl.discord-vscode) Update your discord status with the newly added rich presence.
- [GitHub Theme 🌟](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme) GitHub theme for VS Code

#### DevOps Extensions

- [Jira and Bitbucket (Official)](https://marketplace.visualstudio.com/items?itemName=Atlassian.atlascode)
- [GitLab Workflow](https://marketplace.visualstudio.com/items?itemName=fatihacet.gitlab-workflow)
- [Kubernetes (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools) Develop, deploy and debug Kubernetes applications
- [Kubernetes Kind (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.kind-vscode)
- [Docker (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Terraform](https://marketplace.visualstudio.com/items?itemName=mauve.terraform) Syntax highlighting, linting, formatting, and validation for Hashicorp's Terraform
    - [hashicorp.com: Supporting the HashiCorp Terraform Extension for Visual Studio Code](https://www.hashicorp.com/blog/supporting-the-hashicorp-terraform-extension-for-visual-studio-code/)
    - [Announcing the Terraform Visual Studio Code Extension v2.0.0](https://www.hashicorp.com/blog/announcing-the-terraform-visual-studio-code-extension-v2-0-0/)
- [Ansible](https://marketplace.visualstudio.com/items?itemName=vscoss.vscode-ansible)
- [MongoDB for VS Code](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode)
    - [Introducing MongoDB for VS Code](https://www.mongodb.com/blog/post/introducing-mongodb-for-vs-code)

#### Azure DevOps Extensions

- [Azure DevOps 🌟](https://marketplace.visualstudio.com/azuredevops)

#### Git Flow Extensions

- [gitflow by vector-of-bool](https://marketplace.visualstudio.com/items?itemName=vector-of-bool.gitflow) Gitflow integration and support in Visual Studio Code
- [GitFlow 4 Code](https://marketplace.visualstudio.com/items?itemName=GreatMinds.gitflow4code)
- [JirAux (Jira integration)](https://marketplace.visualstudio.com/items?itemName=SemihOnay.jiraux) Extension to list,view and create Git-flow like branches from issues
- [BABA-Git Flow](https://marketplace.visualstudio.com/items?itemName=Fatih.baba-flow)

#### Jenkins Extensions

- [Jenkins JCasC-Plugin](https://marketplace.visualstudio.com/items?itemName=jcasc-developers.jcasc-plugin) This extension is used to integrate a live jenkins instance configuration with your editor. It can be used to edit and validate YAML files.
- [Jenkins Pipeline Linter Connector](https://marketplace.visualstudio.com/items?itemName=janjoerke.jenkins-pipeline-linter-connector) Validates Jenkinsfiles by sending them to the Pipeline Linter of a Jenkins server.
- [secanis.ch: Jenkinsfile Support](https://marketplace.visualstudio.com/items?itemName=secanis.jenkinsfile-support) Adds syntax highlighting support for Jenkinsfile's. In this version, it's the same like Groovy is.
- [ivory-lab: JenkinsFile Support](https://marketplace.visualstudio.com/items?itemName=ivory-lab.jenkinsfile-support) Extension provides basic jenkinsfile support (highlighting, snippets and completion)
- [JM Meessen: Declarative Jenkinsfile Support](https://marketplace.visualstudio.com/items?itemName=jmMeessen.jenkins-declarative-support) Adds syntax highlighting support for the declarative Jenkinsfile format flavour.
- [Alessandro Fragnani: Jenkins Status](https://marketplace.visualstudio.com/items?itemName=alefragnani.jenkins-status)

## Integrated Terminal on Visual Studio Code

- [Integrated Terminal](https://code.visualstudio.com/docs/editor/integrated-terminal)
- This is an example of Visual Studio Code settings when adding Git Bash on Windows:

```pwsh
"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"
```

## Debugging in VScode

- [How to configure Visual Studio Code for test debugging](https://medium.com/guidesmiths-dev/how-to-configure-visual-studio-code-for-test-debugging-39d0d7f24d79)
- [blog.getambassador.io: Debugging Go Microservices in Kubernetes with VScode 🌟](https://blog.getambassador.io/debugging-go-microservices-in-kubernetes-with-vscode-a36beb48ef1) Tutorial: Learn to debug Go microservices locally while testing against dependencies in a remote Kubernetes cluster
- [==developers.redhat.com: Remote debugging on Kubernetes using VS Code==](https://developers.redhat.com/articles/2021/12/13/remote-debugging-kubernetes-using-vs-code#)
- [==metalbear-co/mirrord==](https://github.com/metalbear-co/mirrord) **A Visual Studio Code extension that lets you easily mirror traffic from your Kubernetes cluster to your development environment.** When you start debugging, mirrord will prompt you to select a pod to mirror traffic from. It will then mirror all traffic from that pod to the process you're debugging.
    - [blog.stackademic.com: Debugging Microservices Locally with mirrord](https://blog.stackademic.com/mastering-local-microservices-debugging-with-mirrord-0a99443c1544) On some occasions, you might want to be able to debug code running in pods in a Kubernetes cluster. This article will teach you how to use mirrord to develop your local code against a remote Kubernetes cluster
- [kenneth.io: Introducing remote debugging of Node.js apps on Azure App Service from VS Code](https://kenneth.io/post/introducing-remote-debugging-of-nodejs-apps-on-azure-app-service-from-vs-code-in-public-preview)

## Python in Visual Studio Code

- [Python in Visual Studio Code – September 2020 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-september-2020-release/)
- [Python in Visual Studio Code – January 2021 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-january-2021-release/)
- [realpython.com: Python Development in Visual Studio Code](https://realpython.com/python-development-visual-studio-code/)

## Go in Visual Studio Code

- [github.com/golang/vscode-go 🌟](https://github.com/golang/vscode-go/blob/master/README.md)
- [blog.golang.org: Gopls on by default in the VS Code Go extension](https://blog.golang.org/gopls-vscode-go)

## Bridge to Kubernetes

- [Bridge to Kubernetes 🌟](https://github.com/microsoft/mindaro) Bridge to Kubernetes extends the Kubernetes perimeter to your development computer allowing you to write, test, and debug microservice code while connected to your Kubernetes cluster with the rest of your application or services. With this workflow, there is no need for extra assets, such as a Dockerfile or Kubernetes manifests. You can simply run your code natively on your development workstation while connected to the Kubernetes cluster, allowing you to test your code changes in the context of the larger application.
- [visualstudiomagazine.com: Bridge to Kubernetes Simplifies Microservice Development in Visual Studio/VS Code](https://visualstudiomagazine.com/articles/2020/10/07/bridge-kubernetes.aspx)

## AWS Toolkits

- [AWS Toolkits for Cloud9, JetBrains and VS Code now support interaction with over 200 new resource types 🌟](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-toolkits-cloud9-jetbrains-vs-code/)

## Cloud Code

- [Cloud Code 🌟](https://cloud.google.com/code) Everything you need to write, debug, and deploy your cloud-native applications.

## Alternatives

- [Repl.it](https://repl.it/) Reading code is hard! Don't you wish you could just ask the code what it does? To describe its functions, its types. And maybe... how can it be improved? Introducing: Replit code oracle.
- [==Gitpod Open Sources a ‘Holistic IDE’==](https://thenewstack.io/gitpod-open-sources-a-holistic-ide/)
    - [thenewstack.io: Gitpod Brings Automated Environments to JetBrains IDEs](https://thenewstack.io/gitpod-brings-automated-environments-to-jetbrains-ides/)
- [piotrminkowski.com: Development on Kubernetes: IDE & TOOLS](https://piotrminkowski.com/2020/08/03/development-on-kubernetes-ide-tools/) In this article, you will learn what tools, frameworks, and platforms could help you to speed up the development of JVM microservices on Kubernetes.
- [openshift.com: Visual Web Terminal - A Turbocharged Command Line for Kubernetes and OpenShift](https://www.openshift.com/blog/visual-web-terminal-a-turbocharged-command-line-for-kubernetes-and-openshift)
- [Linux on Chrome OS, sometimes called Crostini 🌟](https://chromeos.dev/en/linux), allows you to run Linux apps for development alongside your usual Chrome OS desktop & apps.
- [==Fleet==](https://www.jetbrains.com/fleet/) Next-generation IDE by JetBrains
    - [softzone.es: Conoce Fleet, el nuevo IDE ultraligero de la mano de JetBrains](https://www.softzone.es/noticias/programas/conoce-fleet-ide-ultraligero-mano-jetbrains/)
- [thenewstack.io: Are Cloud-Based IDEs the Future of Software Engineering?](https://thenewstack.io/are-cloud-based-ides-the-future-of-software-engineering/)

### Intellij IDEA

- [evaizik.medium.com: Setting up a remote debugging for Java microservices running inside Kubernetes pods](https://evaizik.medium.com/setting-up-a-remote-debugging-for-java-microservices-running-inside-kubernetes-pods-d4aab1ff4efa) In this article, you'll learn in detail how to set up remote debugging between IntelliJ IDE and a Java application running inside a Kubernetes pod — without using any additional third-party software
- [betterprogramming.pub: My Top 7 Most Underrated IntelliJ IDEA Features](https://betterprogramming.pub/my-top-7-most-underrated-intellij-idea-features-572b0b706bd6)

### Online VSCode

- [github.dev](https://github.dev)
- [==gitpod.io== 🌟🌟](https://www.gitpod.io/) - [github.com/gitpod-io/gitpod](https://github.com/gitpod-io/gitpod) Gitpod automates the provisioning of ready-to-code development environments. Gitpod is an open-source Kubernetes application for automated and ready-to-code development environments that blends in your existing workflow. It enables you to describe your dev environment as code and start instant and fresh development environments for each new task directly from your browser. Tightly integrated with GitLab, GitHub, and Bitbucket, Gitpod automatically and continuously prebuilds dev environments for all your branches. As a result, team members can instantly start coding with fresh, ephemeral and fully-compiled dev environments - no matter if you are building a new feature, want to fix a bug or do a code review.
    - [gitpod.io: VS Code in the browser for everyone](https://www.gitpod.io/blog/openvscode-server-launch)
    - [thenewstack.io: GitPod OpenVSCode Server Brings Visual Studio Code to the Browser](https://thenewstack.io/gitpod-openvscode-server-brings-visual-studio-code-to-the-browser/)
- [github1s.com 🌟](https://github1s.com/) One second to read GitHub code with VS Code.
- [vscode.dev 🌟](https://vscode.dev/)
    - [code.visualstudio.com: vscode.dev(!)](https://code.visualstudio.com/blogs/2021/10/20/vscode-dev?WT.mc_id=devcloud-46480-cxa)
    - [genbeta.com: Visual Studio Code ya cuenta con una versión web (que te permite mantener tus proyectos en tu disco duro)](https://www.genbeta.com/desarrollo/visual-studio-code-cuenta-version-web-que-te-permite-mantener-tus-proyectos-tu-disco-duro)
    - [css-tricks.com: The Many Faces of VS Code in the Browser](https://css-tricks.com/the-many-faces-of-vs-code-in-the-browser/)

## Youtube Shorts

- [==Visual Studio Code - Shorts==](https://www.youtube.com/@code/shorts)
- [VSCode Profiles](https://www.youtube.com/shorts/WzlpGnbNPH4)
- [Pin VS Code Tabs](https://www.youtube.com/shorts/6NFR5MsHM_4)
- [Markdown Header Magic](https://www.youtube.com/shorts/G5580-DxQuw)
- [Changing Font in VS Code the RIGHT WAY!](https://www.youtube.com/shorts/Q2RrAdWmn_M)
- [ErrorLens! Catch Errors on the Fly!](https://www.youtube.com/shorts/uzC1PP73d9I)
- [Try Maven (and Java) in VS Code!](https://www.youtube.com/shorts/t322UnzV9vM)
- [Extension of the Week: Prettier](https://www.youtube.com/shorts/dDtueNAFELo)
- [Copilot Unit Tessts Like a Boss](https://www.youtube.com/shorts/AGFvs2pT1VQ)
- [STOP Creating New Files This! But Do THIS in VS Code!!!](https://www.youtube.com/shorts/VqOVb76IyI4)
- [Take your extensions with you](https://www.youtube.com/shorts/HyhSDvaaRwM)
- [Java, Gradle, and VS Code](https://www.youtube.com/shorts/0xq_ZYfl6Vk)
- [VS Code February 2023 Release Highlights (v1.76)](https://www.youtube.com/shorts/hdmaP4ibJ4I)
- [Extension of the week: Thunder Client](https://www.youtube.com/shorts/X3wgBid4gO8)
- [Pin VS Code Tabs?](https://www.youtube.com/shorts/6NFR5MsHM_4)
- [Rainbox CSV](https://www.youtube.com/shorts/y55a7NAiHiI)
- [Extensión de Visual Studio Code que genera tests y mejora tu código](https://youtube.com/shorts/hmq195GRYCI?si=8knOM1y50V6JcRlk)
- [Create diagrams in vscode](https://www.youtube.com/shorts/0N-NFIfy5lI)
- [Copilot writing Markdown](https://www.youtube.com/shorts/70voiUcMk_I)
- [Change your Java versions in VS Code!](https://www.youtube.com/shorts/p-H7Q9PtSc8)
- [April 2023 Release Highlights - Profile Templates](https://www.youtube.com/shorts/ToGRhGvo62k)
- [How VS Code Makes Branches](https://www.youtube.com/shorts/-hvEdSI8ziE)
- [Write slides in VS Code](https://www.youtube.com/shorts/cLokEWqTuds)
- [Create guided walkthroughs of your code](https://www.youtube.com/shorts/KQB8FRoJaH4)
- [Minimap Makeover](https://www.youtube.com/shorts/t5vXCNIBVYw)
- [Navigate your code's history](https://www.youtube.com/shorts/6IwjxcDbVW0)
- [Vertical rulers](https://www.youtube.com/shorts/cTE0ec3IurE)
- [Time Travel!](https://www.youtube.com/shorts/0h1xNFsEZBU)
- [Master Git with Git Graph](https://www.youtube.com/shorts/OfsixF-splk)
- [New VS Code features](https://www.youtube.com/shorts/8iVaeLjzY6s)
- [Hacking GitHub?](https://www.youtube.com/shorts/nMJBbH7g1M4)
- [New VS Code Release Highlights v1.86](https://youtube.com/shorts/bVlIo4H0IDU)
- [File Icon Theme](https://youtube.com/shorts/i0V1bHybv5w?si=y42F3QjNFVouu3s8)
- [Learn with Copilot](https://youtube.com/shorts/rjmXBs5l_7M?si=UlQ4q1-B-JOiYwrn)
- [Visualize your git repo in vscode with Git Graph extensions](https://youtube.com/shorts/vpFF1XSqWjw?si=Zr2eW_C3_3hQoXAa)
- [How to be a professional (un)wrapper #vscode #programmingtools #coding](https://youtube.com/shorts/yuzKp_KsGIk?si=ooaqRJzW2cmf6Z2M)
- [Screencast mode](https://www.youtube.com/shorts/KZHI5RMmFk0)

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fnPhJHN0jTE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/VqCgcpAypFQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ijz1mXQm7KU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/AYbgqmyg7dk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/BO-nhyqpm7A" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9O1PZoo0IAU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/PGsMy75ffPM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7FltByLPnrg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/ydj23WqFAjU" title="Stop using find and replace to rename your symbols!" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/RRn6vwbZca0" title="Use Multi Cursors Like a Boss" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/PnAgS0nDTKY" title="VS Code October 2022 Release Highlights (v1.73)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/N6uEF6I4svc" title="What is 'git STASH'?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/017XXz2hcoY" title="Start using emoji syntax in Markdown files! :smile:" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/PrI1m7qOsag" title="Stop searching for the same code over and over again!" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/PGvV-r8IzoI" title="Remote Tunnels #vscode #programming #software #coding" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="469" height="834" src="https://www.youtube.com/embed/0WOx1aoHH1o" title="Favorite VS Code features of 2022" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/QS_bh-3qKdw?si=vWQbX5blfaYnWYKS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>
</details>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Did you know, you can have project specific user settings in VS Code? <br><br>I certainly didn’t, but I needed to make some tweaks for a better live coding experience for workshop attendees.<br><br>Create a .vscode folder in your project then add settings.json in there. <br><br>Handy! <a href="https://t.co/X3PbgwSVWp">pic.twitter.com/X3PbgwSVWp</a></p>&mdash; Andy Bell (@piccalilli_) <a href="https://twitter.com/piccalilli_/status/1337063582790537224?ref_src=twsrc%5Etfw">December 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Today&#39;s <a href="https://twitter.com/code?ref_src=twsrc%5Etfw">@code</a> extension: Github Repositories<br><br>Browse and edit code from <a href="https://twitter.com/github?ref_src=twsrc%5Etfw">@Github</a> without cloning. You can even review PRs!<br><br>It&#39;s kind of like <a href="https://t.co/dqc8Luetlw">https://t.co/dqc8Luetlw</a>, but for desktop VS Code<a href="https://twitter.com/hashtag/code2020?src=hash&amp;ref_src=twsrc%5Etfw">#code2020</a> <a href="https://t.co/ttVstg2HPO">pic.twitter.com/ttVstg2HPO</a></p>&mdash; Matt Bierner (@mattbierner) <a href="https://twitter.com/mattbierner/status/1438573398574215172?ref_src=twsrc%5Etfw">September 16, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If I was forced to use closed source IDE for a paid job, I would go for JetBrains. They are far better than VSCode or anything else ever created. Of course, VIM is my first choice, but sometimes they or other team members are comfier with a professional tool.</p>&mdash; The Best Linux Blog In the Unixverse (@nixcraft) <a href="https://twitter.com/nixcraft/status/1443645958797987855?ref_src=twsrc%5Etfw">September 30, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m currently using the following <a href="https://twitter.com/code?ref_src=twsrc%5Etfw">@code</a> extensions (fundamentally, Python development):<br><br>1. Python<br>2. GitHub Copilot<br>3. Docker<br>4. Jupyter<br>5. Prettier<br>6. YAML<br>7. OpenAPI Swagger<br>8. Bookmarks<br>9. AWS Toolkit<br>10. Cloud Code<br><br>Is there something else that you&#39;d recommend?</p>&mdash; Santiago (@svpino) <a href="https://twitter.com/svpino/status/1448000684176125959?ref_src=twsrc%5Etfw">October 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Did you know that <a href="https://twitter.com/hashtag/vscode?src=hash&amp;ref_src=twsrc%5Etfw">#vscode</a> has so called zen mode, that makes editor fullscreen and removes all the menus, so cool! <a href="https://t.co/My5jelmLnU">pic.twitter.com/My5jelmLnU</a></p>&mdash; Jaka Hudoklin 🤖 5G: 100% (@offlinehacker) <a href="https://twitter.com/offlinehacker/status/1455903658151923717?ref_src=twsrc%5Etfw">November 3, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The brand new Visual Studio Code for the Web looks fantastic, and it&#39;s blazingly fast!<br><br>They say it is &quot;a zero-install experience running entirely in your browser.&quot; <br><br>Your local environment has its days counted.<a href="https://t.co/4XIKBANfxL">https://t.co/4XIKBANfxL</a> <a href="https://t.co/NElvgQq20F">pic.twitter.com/NElvgQq20F</a></p>&mdash; Santiago (@svpino) <a href="https://twitter.com/svpino/status/1458920285164425224?ref_src=twsrc%5Etfw">November 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sometimes I do a bit of coding on my laptop where I don&#39;t have GitHub Copilot installed - and it becomes VERY clear how super productive that tool is making me.<br><br>Without comparison the best addition to VSCode I&#39;ve tried!</p>&mdash; Simon Høiberg (@SimonHoiberg) <a href="https://twitter.com/SimonHoiberg/status/1462031896477634567?ref_src=twsrc%5Etfw">November 20, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">&quot;I joined a company which brands itself as a tech-first company. I was super excited.<br><br>As I was setting up my laptop, I noticed I have no admin rights. Turned out I needed to request permission to install anything. And my request for Visual Studio Code was rejected.&quot;<br><br>🤯</p>&mdash; Gergely Orosz (@GergelyOrosz) <a href="https://twitter.com/GergelyOrosz/status/1510851664399548417?ref_src=twsrc%5Etfw">April 4, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>