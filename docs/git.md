# Git and Patterns for Managing Source Code Branches. CI/CD BOTs
- [Git Distributed Version-Control System](#git-distributed-version-control-system)
- [Design By Contract](#design-by-contract)
- [Git Cheat Sheets](#git-cheat-sheets)
- [Patterns for Managing Source Code Branches (Branching Models/Workflows)](#patterns-for-managing-source-code-branches-branching-modelsworkflows)
    - [Git Workflows](#git-workflows)
    - [Trunk Based Development](#trunk-based-development)
    - [Feature Branch Development (aka GitFlow)](#feature-branch-development-aka-gitflow)
        - [Git Flow](#git-flow)
    - [Trunk-based Development vs. Git Flow](#trunk-based-development-vs-git-flow)
    - [Alternative Branching Models](#alternative-branching-models)
        - [Feature Flags (Feature Toggles)](#feature-flags-feature-toggles)
- [Git Commands](#git-commands)
- [BitBucket](#bitbucket)
- [GitLab](#gitlab)
- [GitHub](#github)
- [Git Tools](#git-tools)
- [Azure DevOps (formerly known as VSTS)](#azure-devops-formerly-known-as-vsts)
- [CI/CD BOTs (aka Merge BOTs)](#cicd-bots-aka-merge-bots)
    - [Tips](#tips)
    - [Jenkins for git merges](#jenkins-for-git-merges)
    - [Bitbucket for git merges](#bitbucket-for-git-merges)
    - [GitLab for git merges](#gitlab-for-git-merges)
        - [Marge GitLab bot](#marge-gitlab-bot)
    - [Jenkins-X bots](#jenkins-x-bots)
    - [Plastic SCM bot](#plastic-scm-bot)
    - [Mergify bot](#mergify-bot)
    - [GitHub bots](#github-bots)
        - [Bors GitHub bot](#bors-github-bot)

## Git Distributed Version-Control System
* [Wikipedia: Git](https://en.wikipedia.org/wiki/Git)
* [Git](https://git-scm.com/)
    * [git-scm.com/book](https://git-scm.com/book)
* [devdocs.io/git/](https://devdocs.io/git/)
* [tutorialzine.com: Learn git in 30 minutes 🌟](https://tutorialzine.com/2016/06/learn-git-in-30-minutes)
* [3 Git Commands I Use Every Day](https://dev.to/gonedark/3-git-commands-i-use-every-day)
* [Git and Github in Plain English](https://red-badger.com/blog/2016/11/29/gitgithub-in-plain-english)
* [opensource.com: How to restore older file versions in Git](https://opensource.com/life/16/7/how-restore-older-file-versions-git)
* [9 awesome git tricks](https://tychoish.com/post/9-awesome-git-tricks/)
* [Awesome Git 🌟](https://github.com/dictcp/awesome-git)
* [dzone.com: intro git 🌟](https://dzone.com/articles/intro-git)
* [dzone.com: Top 20 git commands with examples 🌟](https://dzone.com/articles/top-20-git-commands-with-examples)
* [dzone.com: 8 Useful But Not Well-Known Git Concepts](https://dzone.com/articles/8-useful-but-not-well-known-git-concepts) These lesser-known Git tricks can help you solve problems that are not handled well by the GitHub and BitBucket GUIs
* [dzone.com: Git Commands Tutorial - Part 1](https://dzone.com/articles/git-commands-tutorial-part-1)
* [dzone.com: Git Commands Tutorial - Part 2](https://dzone.com/articles/git-commands-tutorial-part-2)
* [Dzone refcard: Getting started with Git](https://dzone.com/refcardz/getting-started-git)
* [Oh shit, git!](https://ohshitgit.com/)
* [How to Get More Out of Your Git Commit Message](https://datree.io/blog/git-commit-message-conventions-for-readable-git-log/)
* [10 useful Git commands you wish existed – and their alternatives](https://datree.io/blog/useful-git-commands-list/)
* [github.blog: How to undo (almost) anything with Git](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/)
* [dev.to: Git Explained - The Basics](https://dev.to/milu_franz/git-explained-the-basics-igc)

## Design By Contract
[Wikipedia: Design by contract (DbC)](https://en.wikipedia.org/wiki/Design_by_contract), also known as contract programming, programming by contract and design-by-contract programming, is an approach for designing software. 

It prescribes that software designers should define formal, precise and verifiable interface specifications for software components, which extend the ordinary definition of abstract data types with preconditions, postconditions and invariants. These specifications are referred to as "contracts", in accordance with a conceptual metaphor with the conditions and obligations of business contracts.

## Git Cheat Sheets
* [git-scm.com: Git reference](https://git-scm.com/docs)
* [zeroturnaround.com: Git cheat sheet 🌟](https://www.jrebel.com/blog/git-cheat-sheet)
* [ndpsoftware.com: Interactive git cheat sheet 🌟](https://ndpsoftware.com/git-cheatsheet.html)
* [The awesome git cheat sheet](https://the-awesome-git-cheat-sheet.com/)
* [developers.redhat.com: Git cheat sheet](https://developers.redhat.com/cheat-sheetsgit/)
* [atlassian.com: Git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
* [github.github.com/training-kit: Git cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
* [education.github.com: Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [dzone.com: refcard - getting started with git](https://dzone.com/refcardz/getting-started-git)
* [git-tower.com: Git cheat sheet](https://www.git-tower.com/blog/git-cheat-sheet/)
* [rogerdudler.github.io: git - the simple guide 🌟](https://rogerdudler.github.io/git-guide) Just a simple guide for getting started with git. no deep shit ;)
    * [rogerdudler.github.io: git cheat sheet pdf](https://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)

## Patterns for Managing Source Code Branches (Branching Models/Workflows)
* [paulhammant.com: What is Your Branching Model?:](https://paulhammant.com/2013/12/04/what_is_your_branching_model/) Mainline, Cascade, Trunk-Based Development, Short Lived Feature Branches, Continuous Deployment, Subversion noise on branching, etc.
* [adevait.com: Creating a Branching Strategy for Small Teams](https://adevait.com/software/creating-branching-strategy)
* [atlassian.com: Configuring branching models 🌟](https://confluence.atlassian.com/bitbucketserver/using-branches-in-bitbucket-server-776639968.html#UsingbranchesinBitbucketServer-model)
* [git-scm.com: Git Branching - Branching Workflows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
* [git-scm.com: Distributed Git - Distributed Workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
    * [Distributed Git - Distributed Workflows - Integration-Manager Workflow](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
    * [Setup Git Integration Manager Workflow in Eclipse](https://stackoverflow.com/questions/26003298/how-to-setup-local-git-with-local-blessed-repo-integration-manager-workflow)
* [Dzone refcard: Git Patterns and Anti-Patterns](https://dzone.com/refcardz/git-patterns-and-anti-patterns) Scaling from Workgroup to Enterprise. Suggests patterns and anti-patterns, including Hybrid SCM, Git champions, blessed repository, per-feature topic branches, and ALM integration.
* [Dzone: Basic Git Branching](https://dzone.com/articles/basic-git-branching) In this article, we walk through the basics of branching with Git to get you started with better managing your versioning during projects.
* [martinfowler.com: Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html)
    * [Release Branch Pattern:](https://martinfowler.com/articles/branching-patterns.html#release-branch) A branch that only accepts commits accepted to stabilize a version of the product ready for release.
* [medium: Which Git branching model should I select for my project?](https://medium.com/aventude/which-git-branching-model-should-i-select-73aafc503b5f)

### Git Workflows
* ```git help workflows```
* [atlassian.com: Comparing Workflows 🌟](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html)
* [GitHub Flow](https://guides.github.com/introduction/flow/)
* [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
* [Git DMZ Flow](https://gist.github.com/djspiewak/9f2f91085607a4859a66)

### Trunk Based Development
* [Trunk Based Development](https://trunkbaseddevelopment.com/)
* [paulhammant.com: What is Trunk-Based Development?](https://paulhammant.com/2013/04/05/what-is-trunk-based-development/)
* [The Origins of Trunk Based Development](https://dzone.com/articles/origins-trunk-based)
* [quora.com: What is trunk based development?](https://www.quora.com/What-is-trunk-based-development)
* [kean.github.io: Trunk-Based Development](https://kean.github.io/post/trunk-based-development)
* [paulhammant.com: Microsoft's Trunk-Based Development](https://paulhammant.com/2014/04/03/microsofts-trunk-based-development/)
* [devblogs.microsoft.com: Release Flow: How We Do Branching on the VSTS Team](https://devblogs.microsoft.com/devops/release-flow-how-we-do-branching-on-the-vsts-team/)

### Feature Branch Development (aka GitFlow)
* [nvie.com: Feature Branches. A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)

#### Git Flow 
* One of the main concepts of **GitFlow** is **feature branches**. The idea is that each feature should be developed in its own branch. When the feature is done, it gets merged into develop branch. 
* [atlassian.com: Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
* [gitkraken.com: GitFlow](https://support.gitkraken.com/git-workflows-and-extensions/git-flow/) is a list of rules to keep a repo’s history organized, and is used to make the release process, bug fixes, and feature creation easier.
* [git-flow.readthedocs.io](https://git-flow.readthedocs.io/)
* [aprendegit.com: git-flow: la rama develop y uso de feature branches](http://aprendegit.com/git-flow-la-rama-develop-y-uso-de-feature-branches/)
* [medium.com: Gitflow — Branch Guide](https://medium.com/@rafavinnce/gitflow-branch-guide-8a523360c053)
* [medium.com: Git Flow for Beginners](https://medium.com/@thibault60000/git-flow-for-beginners-d7a152b2c1f9)
* [medium.com: What is GitFlow?](https://medium.com/@okandavut/what-is-gitflow-c0be7a659992)
* [gist.github.com/JamesMGreene: A comparison of using `git flow` commands versus raw `git` commands](https://gist.github.com/JamesMGreene/cdd0ac49f90c987e45ac)
* [Git-flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.html)

### Trunk-based Development vs. Git Flow
* [toptal.com: Trunk-based Development vs. Git Flow](https://www.toptal.com/software/trunk-based-development-git-flow)
* [victorops.com: Source Code Control: Trunk-Based Development vs. GitFlow](https://victorops.com/blog/source-code-control-trunk-based-development-vs-gitflow)
* [medium: GitFlow VS Trunk-Based-Development](https://medium.com/@vafrcor2009/gitflow-vs-trunk-based-development-3beff578030b)
* [Dzone: Why I Prefer Trunk-Based Development Over Feature Branching and GitFlow 🌟](https://dzone.com/articles/why-i-prefer-trunk-based-development-over-feature) Check out the components of Trunk-based Development as implemented by Facebook and Google, and see how it helps resolve and prevent merge conflicts.
* [team-coder.com: From Git Flow to Trunk Based Development](https://team-coder.com/from-git-flow-to-trunk-based-development/)
* [stridenyc.com/podcasts: Trunk Based Development vs Gitflow](https://www.stridenyc.com/podcasts/30-trunk-based-development-vs-gitflow)

### Alternative Branching Models
* [trunkbaseddevelopment.com: Alternative Branching Models](https://trunkbaseddevelopment.com/alternative-branching-models/)

#### Feature Flags (Feature Toggles)
* [featureflags.io: Flags vs Branching](https://featureflags.io/feature-flags-vs-branching/) Branch better with feature flag driven development.
* [martinfowler.com: Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html)

## Git Commands
* Show commit logs:
```bash
git log --oneline --all --graph --decorate
```

## BitBucket
* [bitbucket.org](https://bitbucket.org/)
* [Atlassian Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
* [Dzone: source control using atlassian bitbucket](https://dzone.com/articles/source-control-using-atlassian-bitbucket)
* [Dzone: how I use bitbucket in my regular routine](https://dzone.com/articles/how-i-use-bitbucket-in-my-regular-routine)

## GitLab
* [gitlab.com](https://gitlab.com/)
* [Dzone: using gitlab API to create projects](https://dzone.com/articles/using-gitlab-rest-api-to-create-projects)

## GitHub
* [GitHub Codespaces](https://github.com/features/codespaces) Get the full Visual Studio Code experience without leaving GitHub.
* [GitHub CLI](https://cli.github.com/)
    * [github.com/cli/cli](https://github.com/cli/cli)
    * [github.blog: GitHub CLI allows you to close, reopen, and add metadata to issues and pull requests](https://github.blog/changelog/2020-05-11-github-cli-allows-you-to-close-reopen-and-add-metadata-to-issues-and-pull-requests/)

## Git Tools
* [Atlassian Sourcetree](https://www.sourcetreeapp.com/)
* [gitkraken.com](https://www.gitkraken.com/)
    * [dzone.com: See What's New in GitKraken v4.0](https://dzone.com/articles/see-whats-new-in-gitkraken-v40)
    * [youtube: GitKraken Tutorials and Tips](https://www.youtube.com/watch?v=gjtXTm_TvvE&list=PLe6EXFvnTV78WqGmGSq8JPnafR3lAa55n)
* [gmaster](https://gmaster.io/)
* [Visual Studio Code (Git Extensions)](visual-studio.md)
* [Visual Studio Online](https://visualstudio.microsoft.com/services/visual-studio-codespaces/)

## Azure DevOps (formerly known as VSTS) 
* [Wikipedia: Azure DevOps](https://en.wikipedia.org/wiki/Azure_DevOps)
    * [wikipedia: Azure DevOps Server](https://en.wikipedia.org/wiki/Azure_DevOps_Server) Collaboration software for software development formerly known as Team Foundation Server and Visual Studio Team System
    * [wikipedia: Azure DevOps Services](https://en.wikipedia.org/wiki/Microsoft_Visual_Studio#Azure_DevOps_Services) Cloud service for software development formerly known as Visual Studio Team Services, Visual Studio Online and Team Foundation Service Preview
* [Azure DevOps Labs 🌟](https://azuredevopslabs.com/)
* [twitter.com/azuredevops](https://twitter.com/azuredevops)
* [Microsoft Visual Studio Team Services (VSTS)](https://www.dotnetcurry.com/visualstudio/1322/what-is-visual-studio-team-system-vsts)
* [Microsoft Visual Studio Team Services (VSTS) Tutorial: The Cloud ALM Platform](https://www.softwaretestinghelp.com/microsoft-vsts-tutorial-1/)
* [slideshare.net: Git version control and trunk based approach with VSTS](https://www.slideshare.net/arunmurughan/git-version-control-and-trunk-based-approach-with-vsts)
* [Microsoft Replacing Visual Studio Team Services with Azure DevOps](https://redmondmag.com/articles/2018/09/10/microsoft-replacing-vsts-with-azure-devops.aspx)
* [How We Use Git at Microsoft](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/use-git-microsoft)

## CI/CD BOTs (aka Merge BOTs)
* The CI/CD Bot or Merge Bot is a tool to orchestrate pull requests merging into the stable branches.
* [Wikipedia: Software bot](https://en.wikipedia.org/wiki/Software_bot)

### Tips
* Use bots to accomplish tasks like merging PR's that have been approved and automatically updating dependencies. Usage of one of these bots might allow us to trigger certain builds based off of specific GitHub tags,  it would allow us to only selectively run certain test suites and increase the throughput of the build by only testing changes made in a branch / PR.
* Investigate options that are available and see if we can integrate them with CI.
* We should be able to configure this bot to automatically apply labels to PR's based off of what is changed in a PR. For instance, if a PR contains any documentation changes, the area/Documentation label can be applied.

### Jenkins for git merges
* [**Git Plugin**: Merge Extensions](https://plugins.jenkins.io/git/#merge-extensions)
* [**Validated Merge Plugin** for Git in CloudBees Jenkins Enterprise 🌟](https://docs.cloudbees.com/docs/admin-resources/latest/plugins/validated-merge#chapter-validated-merge_validated-merge)
* [How to configure Jenkins for git merge](https://support.cloudbees.com/hc/en-us/articles/227246387-How-to-Configure-Jenkins-for-Git-Merge-)
* [GitHub Pull Request Builder Plugin](https://plugins.jenkins.io/ghprb/) , [github ref](https://github.com/jenkinsci/ghprb-plugin). You should probably migrate to GitHub Branch Source Plugin.
* [GitHub Branch Source Plugin:](https://plugins.jenkins.io/github-branch-source/) Allows you to create a new project based on the repository structure from one or more GitHub users or organizations.

### Bitbucket for git merges
* [Automatic branch merging](https://confluence.atlassian.com/bitbucketserver/automatic-branch-merging-776639993.html)
* [BitBucket Auto Merge](https://github.com/bluefrg/bitbucket-auto-merge) Automatically create and merge pull request to keep branches in sync.
* [BitBucket Bot for Microsoft Teams](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/new-bitbucket-bot-for-microsoft-teams/ba-p/218212)
* [Code Dog](https://code-dog.app/) Merge your Pull Requests sooner. Some of the Slack messages your team sends are critical for productivity.
Automate them.
* [Jenkins Plugin: Bitbucket Push and Pull Request](https://plugins.jenkins.io/bitbucket-push-and-pull-request/)
* [How to Implement the Automerge feature that is missing from BitBucket cloud](https://poolofthought.com/how-to-implement-the-automerge-feature-that-is-missing-from-bitbucket-cloud/)
* [Configure bitbucket-pipelines.yml to automatically merge feature branch to master?](https://community.atlassian.com/t5/Bitbucket-questions/configure-bitbucket-pipelines-yml-to-automatically-merge-feature/qaq-p/793222)

### GitLab for git merges
* [Auto-merge between release branches](https://gitlab.com/gitlab-org/gitlab/-/issues/2785)
* [Provide merge bot functionality](https://gitlab.com/gitlab-org/gitlab/-/issues/14595)
* [lab.texthtml.net: Gitlab Merge Bot](https://lab.texthtml.net/gitlab/merge-bot)
    * [DockerHub: Gitlab Merge Bot](https://hub.docker.com/r/texthtml/gitlab-merge-bot/) Bot assistant for code review and merge requests approval for Gitlab

#### Marge GitLab bot
* [Marge-bot: A merge-bot for GitLab](https://github.com/smarkets/marge-bot)
* [Example: gitlab.gnome.org/marge-merge-bot](https://gitlab.gnome.org/marge-merge-bot)
* [Example: Smarkets's Marge-bot for GitLab keeps master always green](https://smarketshq.com/marge-bot-for-gitlab-keeps-master-always-green-6070e9d248df)
* [Example: GStreamer Merge Bot](https://gitlab.freedesktop.org/gstreamer-merge-bot)

### Jenkins-X bots
* [Jenkins-X UpdateBOT](https://github.com/jenkins-x/updatebot) A simple bot for updating dependencies in source code and automatically generating Pull Requests in downstream projects.

### Plastic SCM bot
* [Plastic SCM DevOps Mergebot to implement a trunk-based development cycle ](https://github.com/PlasticSCM/trunk-mergebot)
* [PlasticSCM MergeBot Jenkins Plugin](https://wiki.jenkins.io/display/JENKINS/PlasticSCM+MergeBot+plugin)

### Mergify bot
* [mergify.io](https://mergify.io/)  
* [medium: Merging Bots’ Pull Requests Automatically](https://medium.com/mergify/merging-bots-pull-requests-automatically-548ed0b4a424)

### GitHub bots
* [github-rebase-bot](https://github.com/nicolai86/github-rebase-bot) A github bot that monitors repository PRs, rebases them and merges them as they pass tests.
* [Bulldozer: GitHub Pull Request Auto-Merge Bot](https://github.com/palantir/bulldozer) 
* [github-merge-bot](https://github.com/depop/github-merge-bot) Automates the process of merging pull requests and keeping them up-to-date.
* [github.com/squalrus/merge-bot: PR Merge Bot](https://github.com/squalrus/merge-bot) A GitHub action that manages pull request integrations
* [Odoo Mergebot](https://github.com/odoo/odoo/wiki/Mergebot)
* [gmaster.io - Mergedroid: Automate merging just by analyzing your GitHub repo.](https://gmaster.io/mergedroid) A BOT that solves conflicts in pull requests without manual intervention.

#### Bors GitHub bot
* [Bors Bot](https://bors.tech/)
* [Bors - Readme](https://bors.tech/devdocs/bors-ng/readme.html)
* [Bors-ng: A merge bot for GitHub Pull Requests](https://github.com/bors-ng/bors-ng)
* [Example: CockroachDB's Bors Merge Bot](https://wiki.crdb.io/wiki/spaces/CRDB/pages/73204099/Bors+Merge+Bot)


