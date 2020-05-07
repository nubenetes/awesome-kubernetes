# Git and Patterns for Managing Source Code Branches
- [Git Distributed Version-Control System](#git-distributed-version-control-system)
- [Design By Contract](#design-by-contract)
- [Git Cheat Sheets](#git-cheat-sheets)
- [Patterns for Managing Source Code Branches](#patterns-for-managing-source-code-branches)
    - [Trunk Based Development](#trunk-based-development)
    - [Feature Branch Development (aka GitFlow)](#feature-branch-development-aka-gitflow)
        - [Git Flow](#git-flow)
    - [Trunk-based Development vs. Git Flow](#trunk-based-development-vs-git-flow)
    - [Alternative Branching Models](#alternative-branching-models)
        - [Feature Flags (Feature Toggles)](#feature-flags-feature-toggles)
- [Git Commands](#git-commands)
- [BitBucket](#bitbucket)
- [GitLab](#gitlab)

## Git Distributed Version-Control System
* [Wikipedia: Git](https://en.wikipedia.org/wiki/Git)
* [Git](https://git-scm.com/)
    * [git-scm.com/book](https://git-scm.com/book)
* [devdocs.io/git/](https://devdocs.io/git/)
* [tutorialzine.com: Learn git in 30 minutes 🌟🌟](https://tutorialzine.com/2016/06/learn-git-in-30-minutes)
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

## Patterns for Managing Source Code Branches
* [adevait.com: Creating a Branching Strategy for Small Teams](https://adevait.com/software/creating-branching-strategy)
* [atlassian.com: Comparing Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [git-scm.com: Git Branching - Branching Workflows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
* [git-scm.com: Distributed Git - Distributed Workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
    * [Distributed Git - Distributed Workflows - Integration-Manager Workflow](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
    * [Setup Git Integration Manager Workflow in Eclipse](https://stackoverflow.com/questions/26003298/how-to-setup-local-git-with-local-blessed-repo-integration-manager-workflow)
* [Dzone refcard: Git Patterns and Anti-Patterns](https://dzone.com/refcardz/git-patterns-and-anti-patterns) Scaling from Workgroup to Enterprise. Suggests patterns and anti-patterns, including Hybrid SCM, Git champions, blessed repository, per-feature topic branches, and ALM integration.
* [Dzone: Basic Git Branching](https://dzone.com/articles/basic-git-branching) In this article, we walk through the basics of branching with Git to get you started with better managing your versioning during projects.
* [martinfowler.com: Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html)
    * [Release Branch Pattern:](https://martinfowler.com/articles/branching-patterns.html#release-branch) A branch that only accepts commits accepted to stabilize a version of the product ready for release.

### Trunk Based Development
* [Trunk Based Development](https://trunkbaseddevelopment.com/)
* [paulhammant.com: What is Your Branching Model?:](https://paulhammant.com/2013/12/04/what_is_your_branching_model/) Mainline, Cascade, Trunk-Based Development, Short Lived Feature Branches, Continuous Deployment, Subversion noise on branching, etc.
* [paulhammant.com: What is Trunk-Based Development?](https://paulhammant.com/2013/04/05/what-is-trunk-based-development/)
* [The Origins of Trunk Based Development](https://dzone.com/articles/origins-trunk-based)
* [quora.com: What is trunk based development?](https://www.quora.com/What-is-trunk-based-development)
* [kean.github.io: Trunk-Based Development](https://kean.github.io/post/trunk-based-development)

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

