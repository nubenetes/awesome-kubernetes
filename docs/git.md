# Git and Patterns for Managing Source Code Branches. Merge BOTs

1. [Git Distributed Version-Control System](#git-distributed-version-control-system)
2. [Git Releases](#git-releases)
3. [Git stash](#git-stash)
4. [Git Squash](#git-squash)
5. [Git Branches](#git-branches)
6. [Git Merge](#git-merge)
7. [Merge Repositories](#merge-repositories)
8. [Git Aliases](#git-aliases)
9. [Git Rebase](#git-rebase)
10. [Git and GitHub Backup](#git-and-github-backup)
11. [Cherry-picking](#cherry-picking)
12. [Git Submodules](#git-submodules)
13. [Shields](#shields)
14. [Design By Contract](#design-by-contract)
15. [Git Cheat Sheets](#git-cheat-sheets)
16. [Monorepo VS Polyrepo](#monorepo-vs-polyrepo)
17. [Patterns for Managing Source Code Branches (Branching Models/Workflows)](#patterns-for-managing-source-code-branches-branching-modelsworkflows)
     1. [Git Workflows](#git-workflows)
     2. [Trunk Based Development](#trunk-based-development)
     3. [Feature Branch Development (aka GitFlow)](#feature-branch-development-aka-gitflow)
         1. [Git Flow](#git-flow)
         2. [Git Flow is a bad idea](#git-flow-is-a-bad-idea)
     4. [Trunk-based Development vs. Git Flow](#trunk-based-development-vs-git-flow)
     5. [Alternative Branching Models](#alternative-branching-models)
         1. [Feature Flags (Feature Toggles)](#feature-flags-feature-toggles)
             1. [Keystone Interface and Keystone Flags](#keystone-interface-and-keystone-flags)
18. [Git Commands](#git-commands)
19. [BitBucket](#bitbucket)
20. [GitLab](#gitlab)
     1. [GitLab Collective](#gitlab-collective)
21. [GitHub](#github)
     1. [Fake it til you make it](#fake-it-til-you-make-it)
     2. [GitHub Lab](#github-lab)
     3. [GitHub Code Scanner](#github-code-scanner)
     4. [GitHub Discussions](#github-discussions)
     5. [GitHub Actions](#github-actions)
         1. [GitHub Actions Marketplace](#github-actions-marketplace)
     6. [GitHub Actions and OpenShift](#github-actions-and-openshift)
     7. [GitHub Copilot](#github-copilot)
         1. [GitHub CoPilot VS GPT-3](#github-copilot-vs-gpt-3)
         2. [GitHub Copilot X](#github-copilot-x)
         3. [Alternatives](#alternatives)
             1. [CodiumAI](#codiumai)
22. [Gitea](#gitea)
23. [Sapling](#sapling)
24. [Git Tools](#git-tools)
     1. [Git Credential Manager](#git-credential-manager)
     2. [Semantic-release. CI/CD semantic release workflow (semantic Versioning, commit format and releases)](#semantic-release-cicd-semantic-release-workflow-semantic-versioning-commit-format-and-releases)
25. [Azure DevOps (formerly known as VSTS)](#azure-devops-formerly-known-as-vsts)
26. [Pre Commit Hooks](#pre-commit-hooks)
27. [Merge BOTs](#merge-bots)
     1. [Tips](#tips)
     2. [Jenkins for git merges](#jenkins-for-git-merges)
     3. [Bitbucket for git merges](#bitbucket-for-git-merges)
     4. [GitLab for git merges](#gitlab-for-git-merges)
         1. [Marge GitLab bot](#marge-gitlab-bot)
     5. [Jenkins-X bots](#jenkins-x-bots)
     6. [Plastic SCM bot](#plastic-scm-bot)
     7. [Mergify bot](#mergify-bot)
     8. [GitHub bots](#github-bots)
         1. [Bors GitHub bot](#bors-github-bot)
28. [Videos](#videos)
29. [Slides](#slides)
30. [Tweets](#tweets)

## Git Distributed Version-Control System

- [Git](https://git-scm.com/)
    - [git-scm.com/book](https://git-scm.com/book)
- [devdocs.io/git/](https://devdocs.io/git/)
- [tutorialzine.com: Learn git in 30 minutes 🌟](https://tutorialzine.com/2016/06/learn-git-in-30-minutes)
- [3 Git Commands I Use Every Day](https://dev.to/gonedark/3-git-commands-i-use-every-day)
- [opensource.com: How to restore older file versions in Git](https://opensource.com/life/16/7/how-restore-older-file-versions-git)
- [9 awesome git tricks](https://tychoish.com/post/9-awesome-git-tricks/)
- [Awesome Git 🌟](https://github.com/dictcp/awesome-git)
- [Oh shit, git!](https://ohshitgit.com/)
- [freecodecamp.org: Learn Git Fundamentals – A Handbook on Day-to-Day Development Tasks 🌟](https://www.freecodecamp.org/news/learn-git-basics/)
- [How to Get More Out of Your Git Commit Message](https://datree.io/blog/git-commit-message-conventions-for-readable-git-log/)
- [10 useful Git commands you wish existed – and their alternatives](https://datree.io/blog/useful-git-commands-list/)
- [github.blog: How to undo (almost) anything with Git](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/)
- [dev.to: Git Explained - The Basics](https://dev.to/milu_franz/git-explained-the-basics-igc)
- [dev.to: Git Concepts I Wish I Knew Years Ago 🌟](https://dev.to/g_abud/advanced-git-reference-1o9j)
- [opensource.com: 6 best practices for managing Git repos](https://opensource.com/article/20/7/git-repos-best-practices) Resist the urge to add things in Git that will make it harder to manage; here's what to do instead.
- [github.blog: Highlights from Git 2.28](https://github.blog/2020-07-27-highlights-from-git-2-28/)
- [livecodestream.dev: Git Concepts and Workflow for Beginners](https://livecodestream.dev/post/2020-08-21-git-concepts-and-workflow-for-beginners/)
- [thenextweb.com: A beginner’s guide to the most popular Git commands](https://thenextweb.com/syndication/2020/09/02/a-beginners-guide-to-the-most-popular-git-commands/)
- [julien.danjou.info: Stop merging your pull requests manually 🌟](https://julien.danjou.info/stop-merging-your-pull-request-manually/) -> [mergify 🌟](https://mergify.io/)
- [gitlab.com: How to keep your Git history clean with interactive rebase](https://about.gitlab.com/blog/2020/11/23/keep-git-history-clean-with-interactive-rebase/) Interactive rebase is one of Git’s most versatile tools. Here's how to use it to correct commit messages, fix mistakes, and more.
- [gitkraken.com: Git Tutorials: Instructional Training Videos 🌟](https://www.gitkraken.com/learn/git/tutorials)
- [github.blog: Token authentication requirements for Git operations](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/)
- [github.blog: Commits are snapshots, not diffs](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
- [github.blog: Get up to speed with partial clone and shallow clone](https://github.blog/2020-12-21-get-up-to-speed-with-partial-clone-and-shallow-clone/)
- [about.gitlab.com: How Git Partial Clone lets you fetch only the large file you need](https://about.gitlab.com/blog/2020/03/13/partial-clone-for-massive-repositories/)
- [intellipaat.com: Git Tutorial - Learn Git 🌟](https://intellipaat.com/blog/tutorial/devops-tutorial/git-tutorial/)
- [freecodecamp.org: How to Use Multiple Git Configs on One Computer 🌟](https://www.freecodecamp.org/news/how-to-handle-multiple-git-configurations-in-one-machine/)
- [dev.to: Git for beginners](https://dev.to/purveshshende2/git-for-beginners-3il6)
- [blog.gitguardian.com: Rewriting your git history, removing files permanently - cheatsheet & guide](https://blog.gitguardian.com/rewriting-git-history-cheatsheet/)
- [smashingmagazine.com: Getting The Most Out Of Git](https://www.smashingmagazine.com/2021/02/getting-the-most-out-of-git/)
- [thenewstack.io: Why Open Source Project Maintainers are Reluctant to use Digital Signatures, Two-Factor Authentication](https://thenewstack.io/why-open-source-project-maintainers-are-reluctant-to-use-digital-signatures-two-factor-authentication/)
- [geeksforgeeks.org: How to Write Good Commit Messages in GitHub?](https://www.geeksforgeeks.org/how-to-write-good-commit-messages-in-github/)
- [freecodecamp.org: What is Git? A Beginner's Guide to Git Version Control](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control)
- [c-sharpcorner.com: 0 Git Commands You Should Know](https://www.c-sharpcorner.com/article/20-git-commands-you-should-know/)
- [opensource.com: Find what changed in a Git commit](https://opensource.com/article/21/4/git-whatchanged) Git offers several ways you can quickly see which files changed in a commit.
- [freecodecamp.org: How to Use Git and Git Workflows – a Practical Guide](https://www.freecodecamp.org/news/practical-git-and-git-workflows/)
- [about.gitlab.com: Why small merge requests are key to a great review 🌟](https://about.gitlab.com/blog/2021/03/18/iteration-and-code-review/)
- [honeybadger.io: Top Ten Git Tips & Tricks](https://www.honeybadger.io/blog/git-tricks/)
- [blog.balasundar.com: Automate Git Operations Using Python](https://blog.balasundar.com/automate-git-operations-using-python) Automate your git operations using GitPython.
- [cloudbees.com: Git Commands: The 13 You Must Know, In Order 🌟](https://www.cloudbees.com/blog/13-git-commands-to-know-in-order)
- [dev.to: Master Git in 7 minutes 🌟](https://dev.to/valeriavg/master-git-in-7-minutes-gai)
- [livecodestream.dev: Five Advanced Git Concepts that Make You Look Like a Pro](https://livecodestream.dev/post/five-advanced-git-concepts-that-make-you-look-like-a-pro/) Learn how to master GIT with these 5 advanced concepts
- [cloudbees.com: Git Pull: How It Works With Detailed Examples](https://www.cloudbees.com/blog/git-pull-how-it-works-with-detailed-examples)
- [midu.dev: Buenas prácticas para escribir commits en Git](https://midu.dev/buenas-practicas-escribir-commits-git/)
- [cloudbees.com: Git Push: An In-Depth Tutorial With Examples](https://www.cloudbees.com/blog/git-push-an-in-depth-tutorial-with-examples)
- [thenewstack.io: Git for Managing Small Projects 🌟](https://thenewstack.io/git-for-managing-small-projects/)
- [simplilearn.com: How to Resolve Merge Conflicts in Git?](https://www.simplilearn.com/tutorials/git-tutorial/merge-conflicts-in-git)
- [dev.to: Open Source: My first Pull Request](https://dev.to/okimotomizuho/open-source-my-first-pull-request-1356)
- [==freecodecamp.org: Git for Professionals – Free Version Control Course== 🌟](https://www.freecodecamp.org/news/git-for-professionals/)
- [r-bloggers.com: Git: Moving from Master to Main](https://www.r-bloggers.com/2021/10/git-moving-from-master-to-main/)
- [css-tricks.com: Advanced Git series. 1 Creating the Perfect Commit in Git](https://css-tricks.com/creating-the-perfect-commit-in-git/)
    - [css-tricks.com: Advanced Git series. 2 Branching Strategies in Git](https://css-tricks.com/branching-strategies-in-git/)
    - [css-tricks.com: Advanced Git series. 3 Better Collaboration With Pull Requests](https://css-tricks.com/better-collaboration-with-pull-requests/)
    - [css-tricks.com: Advanced Git series. 4 Merge Conflicts: What They Are and How to Deal with Them​](https://css-tricks.com/merge-conflicts-what-they-are-and-how-to-deal-with-them/)
    - [css-tricks.com: Advanced Git series. 5 Rebase vs. Merge: Integrating Changes in Git](https://css-tricks.com/rebase-vs-merge-integrating-changes-in-git/)
    - [css-tricks.com: Advanced Git series. 6 Interactive Rebase: Clean up your Commit History](https://css-tricks.com/interactive-rebase-clean-up-your-commit-history/)
    - [css-tricks.com: Cherry-Picking Commits in Git](https://css-tricks.com/cherry-picking-commits-in-git/)
    - [css-tricks.com: Using the Reflog to Restore Lost Commits](https://css-tricks.com/using-the-reflog-to-restore-lost-commits/)
- [cloudbees.com: Git Reset Clearly Explained: How to Undo Your Changes 🌟](https://www.cloudbees.com/blog/git-reset-undo-changes)
- [c-sharpcorner.com: Top 15 Git Commands With Examples For Every Developers💪](https://www.c-sharpcorner.com/article/top-15-git-commands-with-examples-for-every-developers/)
- [==marklodato.github.io: A Visual Git Reference== 🌟](https://marklodato.github.io/visual-git-guide/index-en.html)
- [dev.to: Get lazy with lazygit](https://dev.to/tahsinature/get-lazy-with-lazygit-4h37)
- [==dev.to: 10 useful Git tips to improve your workflow== 🌟](https://dev.to/yenyih/10-useful-git-tips-to-improve-your-workflow-kf1)
- [dev.to: Git Organized: A Better Git Flow](https://dev.to/render/git-organized-a-better-git-flow-56go)
- [thenewstack.io: Development: Introduction to Git Logging](https://thenewstack.io/development-introduction-to-git-logging/)
- [freecodecamp.org: git config – How to Configure Git Settings to Improve Your Development Workflow](https://www.freecodecamp.org/news/git-config-how-to-configure-git-settings/)
- [freecodecamp.org: Git Undo Merge – How to Revert the Last Merge Commit in Git](https://www.freecodecamp.org/news/git-undo-merge-how-to-revert-the-last-merge-commit-in-git/)
- [infoworld.com: What is Git? Version control for collaborative programming](https://www.infoworld.com/article/3654955/what-is-git-version-control-for-collaborative-programming.html)
- [==dev.to: How Do I Resolve Merge Conflicts?==](https://dev.to/github/how-do-i-resolve-merge-conflicts-5438)
    - [==dev.to: How to Undo Pushed Commits with Git==](https://dev.to/github/how-to-undo-pushed-commits-with-git-2pe6)
- [opensource.com: My guide to using the Git push command safely](https://opensource.com/article/22/4/git-push) Understand the usage and impact of this popular Git command on your project, learn new safer alternatives, and grasp the skills of restoring a broken branch.
- [opensource.com: Make your own Git subcommands](https://opensource.com/article/22/4/customize-git-subcommands) Creating your own Git subcommand makes your custom scripts feel like natural components of Git.
- [github.blog: Improve Git monorepo performance with a file system monitor 🌟](https://github.blog/2022-06-29-improve-git-monorepo-performance-with-a-file-system-monitor/) **Monorepo performance can suffer due to the sheer number of files in your working directory. Git’s new builtin file system monitor makes it easy to speed up monorepo performance.**
- [java67.com: Top 10 Free Git Courses and Tutorials for Beginners in 2022 - Best of Lot](https://www.java67.com/2022/07/10-best-free-git-courses-and-tutorials.html)
- [polarsquad.com: Stop doing pull requests](https://polarsquad.com/blog/stop-doing-pull-requests)
- [dev.to: How atomic Git commits dramatically increased my productivity - and will increase yours too 🌟](https://dev.to/samuelfaure/how-atomic-git-commits-dramatically-increased-my-productivity-and-will-increase-yours-too-4a84)
- [==dev.to: Git fundamentals, a complete guide | Leandro Proença== 🌟🌟](https://dev.to/leandronsp/git-fundamentals-a-complete-guide-do7)
- [freecodecamp.org: Undo Git Add – How to Remove Added Files in Git 🌟](https://www.freecodecamp.org/news/undo-git-add-how-to-remove-added-files-in-git/)
- [==realpython.com: Advanced Git Tips for Python Developers== 🌟](https://realpython.com/advanced-git-for-pythonistas/)
- [build5nines.com: Git: Reset / Undo Most Recent Local Commit](https://build5nines.com/git-reset-undo-most-recent-local-commit/)
- [freecodecamp.org: How to Write Commit Messages that Project Maintainers Will Appreciate](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/)
- [build5nines.com: How to Determine URL a Local Git Repository was Originally Cloned From](https://build5nines.com/how-to-determine-url-a-local-git-repository-was-originally-cloned-from/)

## Git Releases

- [github.blog: Highlights from Git 2.40](https://github.blog/2023-03-13-highlights-from-git-2-40/) The first Git release of the year is here! Take a look at some of our highlights on what's new in Git 2.40.

## Git stash

- [opensource.com: A practical guide to using the git stash command](https://opensource.com/article/21/4/git-stash) Learn how to use the git stash command and when you should use it.
- [dev.to: How to Use Git Stash Command](https://dev.to/mwafrika/how-to-use-git-stash-command-22bk)

## Git Squash

- [cloudbees.com: Git Squash: How to Condense Your Commit History](https://www.cloudbees.com/blog/git-squash-how-to-condense-your-commit-history)
- [devroom.io: Git Squash your latests commits into one](https://www.devroom.io/2011/07/05/git-squash-your-latests-commits-into-one/)
- [freecodecamp.org: Git Squash Commits – Squashing the Last N Commits into One Commit](https://www.freecodecamp.org/news/git-squash-commits/)

## Git Branches

- [==learngitbranching.js.org: Learn Git Branching== 🌟](https://learngitbranching.js.org/) An interactive Git visualization tool to educate and challenge!
- [gitkraken.com: How do you rename a Git branch?](https://www.gitkraken.com/learn/git/problems/rename-git-branch)
- [freecodecamp.org: Git Checkout Remote Branch Tutorial](https://www.freecodecamp.org/news/git-checkout-remote-branch-tutorial/)
- [freecodecamp.org: How to Use Branches in Git – the Ultimate Cheatsheet 🌟](https://www.freecodecamp.org/news/how-to-use-branches-in-git/)
- [stackoverflow.blog: A look under the hood: how branches work in Git](https://stackoverflow.blog/2021/04/05/a-look-under-the-hood-how-branches-work-in-git/) Git branches allow you to keep different versions of your code cleanly separated. Here's a look at how they work and why you should know about them.
- [opensource.com: 4 tips for context switching in Git](https://opensource.com/article/21/4/context-switching-git) Compare the pros and cons of four options to switch branches while working in Git.
- [freecodecamp.org: Git Push to Remote Branch – How to Push a Local Branch to Origin](https://www.freecodecamp.org/news/git-push-to-remote-branch-how-to-push-a-local-branch-to-origin/)
- [freecodecamp.org: How Git Branches Work](https://www.freecodecamp.org/news/how-git-branches-work/)
- [dev.to: Open Source: Multiple branches and git merges](https://dev.to/okimotomizuho/open-source-multiple-branches-and-git-merges-2f69)
- [css-tricks.com: Git: Switching Unstaged Changes to a New Branch](https://css-tricks.com/git-switching-unstaged-changes-to-a-new-branch/)
- [freecodecamp.org: Git List Branches – How to Show All Remote and Local Branch Names](https://www.freecodecamp.org/news/git-list-branches-how-to-show-all-remote-and-local-branch-names/)
- [opensource.com: Explaining Git branches with a LEGO analogy](https://opensource.com/article/22/4/git-branches)
- [dev.to/varbsan: A Simplified Convention for Naming Branches and Commits in Git](https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4)

## Git Merge

- [freecodecamp.org: The Git Merge Handbook – Definitive Guide to Merging in Git](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/)
- [freecodecamp.org: How to Fix Merge Conflicts in Git](https://www.freecodecamp.org/news/how-to-fix-merge-conflicts-in-git/)

## Merge Repositories

- [build5nines.com: Git: Merge Repositories with History](https://build5nines.com/git-merge-repositories-with-history/)

## Git Aliases

- [opensource.com: 8 Git aliases that make me more efficient](https://opensource.com/article/20/11/git-aliases) Use aliases to create shortcuts for your most-used or complex Git commands.
- [davidwalsh.name: More Awesome Git Aliases](https://davidwalsh.name/more-awesome-git-aliases)

## Git Rebase

- [dev.to: ELI5: Git Rebase vs. Merge 🌟](https://dev.to/karaluton/explain-like-i-m-five-git-rebase-vs-merging-1k69)
- [==opensource.com: My guide to understanding Git rebase -i==](https://opensource.com/article/22/4/manage-git-commits-rebase-i-command) The git rebase command is one of the most powerful in Git. It can rewrite your repository's commit history by rearranging, modifying, and even deleting commits.
- [freecodecamp.org/news/git-rebase-handbook](https://www.freecodecamp.org/news/git-rebase-handbook/)

## Git and GitHub Backup

- [dev.to: 3 Ways to Backup Your Code (Even If You Don’t Know Git)](https://dev.to/github/3-ways-to-backup-your-code-even-if-you-dont-know-git-1o5l)

## Cherry-picking

- [opensource.com: 3 reasons I use the Git cherry-pick command](https://opensource.com/article/21/3/git-cherry-pick) Cherry-picking solves a lot of problems in Git repositories. Here are three ways to fix your mistakes with git cherry-pick.
- [jmfloreszazo.com: GIT Mejores prácticas: CHERRY-PICKING](https://jmfloreszazo.com/git-mejores-practicas-cherry-picking/)

## Git Submodules

- [git-scm.com: Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) It often happens that while working on one project, you need to use another project from within it. Perhaps it’s a library that a third party developed or that you’re developing separately and using in multiple parent projects. A common issue arises in these scenarios: you want to be able to treat the two projects as separate yet still be able to use one from within the other.

## Shields

- [shields.io 🌟](https://shields.io/)

## Design By Contract


It prescribes that software designers should define formal, precise and verifiable interface specifications for software components, which extend the ordinary definition of abstract data types with preconditions, postconditions and invariants. These specifications are referred to as "contracts", in accordance with a conceptual metaphor with the conditions and obligations of business contracts.

## Git Cheat Sheets

- [Git and GitHub Cheat Sheets](cheatsheets.md)

## Monorepo VS Polyrepo

- [fourtheorem.com: How to end Microservice pain and embrace the Monorepo](https://www.fourtheorem.com/blog/monorepo)

## Patterns for Managing Source Code Branches (Branching Models/Workflows)

- [paulhammant.com: What is Your Branching Model?:](https://paulhammant.com/2013/12/04/what_is_your_branching_model/) Mainline, Cascade, Trunk-Based Development, Short Lived Feature Branches, Continuous Deployment, Subversion noise on branching, etc.
- [adevait.com: Creating a Branching Strategy for Small Teams](https://adevait.com/software/creating-branching-strategy)
- [atlassian.com: Configuring branching models 🌟](https://confluence.atlassian.com/bitbucketserver/using-branches-in-bitbucket-server-776639968.html#UsingbranchesinBitbucketServer-model)
- [git-scm.com: Git Branching - Branching Workflows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [git-scm.com: Distributed Git - Distributed Workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
- [martinfowler.com: Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html)
- [speakerdeck.com: 10 Git Anti Patterns You Should be Aware of 🌟](https://speakerdeck.com/lemiorhan/10-git-anti-patterns-you-should-be-aware-of)
- [gitkraken.com: Branching in Git 🌟](https://www.gitkraken.com/learn/git/branch)
- [jmfloreszazo.com: Flujos de trabajo de git](https://jmfloreszazo.com/flujos-de-trabajo-de-git/)

??? note "Slide: 10 git anti patterns. Click to expand!"

    <center>
    <script async class="speakerdeck-embed" data-id="1eaed7dabacb4f9b9c96b08de38eb9e1" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
    </center>

### Git Workflows

- ```git help workflows```
- [atlassian.com: Comparing Workflows 🌟](https://www.atlassian.com/git/tutorials/comparing-workflows)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Git DMZ Flow](https://gist.github.com/djspiewak/9f2f91085607a4859a66)
- [kubernetes.dev: GitHub Workflow](https://www.kubernetes.dev/docs/guide/github-workflow/) An overview of the GitHub workflow used by the Kubernetes project. It includes some tips and suggestions on things such as keeping your local environment in sync with upstream and commit hygiene.

### Trunk Based Development

- [Trunk Based Development](https://trunkbaseddevelopment.com/)
- [paulhammant.com: What is Trunk-Based Development?](https://paulhammant.com/2013/04/05/what-is-trunk-based-development/)
- [kean.github.io: Trunk-Based Development](https://kean.github.io/post/trunk-based-development)
- [paulhammant.com: Microsoft's Trunk-Based Development](https://paulhammant.com/2014/04/03/microsofts-trunk-based-development/)
- [devblogs.microsoft.com: Release Flow: How We Do Branching on the VSTS Team](https://devblogs.microsoft.com/devops/release-flow-how-we-do-branching-on-the-vsts-team/)

### Feature Branch Development (aka GitFlow)


#### Git Flow

- One of the main concepts of **GitFlow** is **feature branches**. The idea is that each feature should be developed in its own branch. When the feature is done, it gets merged into develop branch.
- [devopszone.info: An Introduction To Git-flow Workflow](https://www.devopszone.info/post/an-introduction-to-git-flow-workflow)
- [atlassian.com: Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [gitkraken.com: GitFlow](https://support.gitkraken.com/git-workflows-and-extensions/git-flow/) is a list of rules to keep a repo’s history organized, and is used to make the release process, bug fixes, and feature creation easier.
- [git-flow.readthedocs.io](https://git-flow.readthedocs.io/)
- [gist.github.com/JamesMGreene: A comparison of using `git flow` commands versus raw `git` commands](https://gist.github.com/JamesMGreene/cdd0ac49f90c987e45ac)
- [Git-flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.html)
- [aprendegit.com: git-flow: la rama develop y uso de feature branches](http://aprendegit.com/git-flow-la-rama-develop-y-uso-de-feature-branches/)

#### Git Flow is a bad idea

- [thinkinglabs.io: Feature Branching considered Evil](https://thinkinglabs.io/talks/2016/10/29/feature-branching-considered-evil.html)
    - [youtube: Feature Branching is Evil (Thierry de Pauw, Belgium)](https://www.youtube.com/watch?v=h4DM-Wa0aDQ&t=38s&ab_channel=XPDaysUkraine)
    - Feature branching is again gaining in popularity due to the rise of distributed version control systems. Although branch creation has become very easy, it comes with a certain cost. Long living branches break the flow of the software delivery process, impacting throughput and stability.
    - This session explores why teams are using feature branches, what problems are introduced by using them and what techniques exist to avoid them altogether. It explores exactly what’s evil about feature branches, which is not necessarily the problems they introduce - but rather, the real reasons why teams are using them.
- [youtube: Git Flow Is A Bad Idea - Dave Farley ](https://www.youtube.com/watch?v=_w6TwnLCFwA&ab_channel=ContinuousDelivery) What is GitFlow and why is it a bad idea if you want to practice Continuous Delivery or Continuous Integration? GitFlow is a feature branching strategy that adds several extra layers of complexity. Git Flow is bad when we need fast feedback and a clear picture of the quality and 'releasability' of our work, so how do we adapt to get that faster feedback and a clearer picture?

### Trunk-based Development vs. Git Flow

- [victorops.com: Source Code Control: Trunk-Based Development vs. GitFlow](https://victorops.com/blog/source-code-control-trunk-based-development-vs-gitflow)
- [team-coder.com: From Git Flow to Trunk Based Development](https://team-coder.com/from-git-flow-to-trunk-based-development/)
- [freecodecamp.org: What is Trunk Based Development? A Different Approach to the Software Development Lifecycle](https://www.freecodecamp.org/news/what-is-trunk-based-development)

### Alternative Branching Models

- [trunkbaseddevelopment.com: Alternative Branching Models](https://trunkbaseddevelopment.com/alternative-branching-models/)

#### Feature Flags (Feature Toggles)

- [featureflags.io: Flags vs Branching](https://featureflags.io/feature-flags-vs-branching/) Branch better with feature flag driven development.
- [martinfowler.com: Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html)
- [cloudbees.com: Testing with Feature Flags to Improve Developer Productivity](https://www.cloudbees.com/blog/feature-flags-improve-developer-productivity)
- [cloudbees.com: Goodbye Sleepless Nights: De-Risking Deployments with Feature Flags](https://www.cloudbees.com/case-study/petdesk)
- [thenewstack.io: Wave Goodbye to Release Nights](https://thenewstack.io/wave-goodbye-to-release-nights/)
- [infoworld.com: Why aren’t you using feature flags?](https://www.infoworld.com/article/3600150/why-arent-you-using-feature-flags.amp.html) Software development is changing. If you’re still focused on release management rather than feature management, then you’re doing it wrong.
- [cloudbees.com: How to Grow Continuous Delivery Maturity Using Feature Flags](https://www.cloudbees.com/blog/grow-cd-maturity)
- [cloudbees.com: Feature Flag Best Practices: Change Management in Production](https://www.cloudbees.com/blog/change-management-in-production)
- [cloudbees.com: Feature Flag Best Practices: Understanding the Feature Flag Lifecycle](https://www.cloudbees.com/blog/feature-flag-lifecycle)
- [github.blog: How we ship code faster and safer with feature flags](https://github.blog/2021-04-27-ship-code-faster-safer-feature-flags/)
- [cloudbees.com: The Importance of Feature Flags in CI/CD](https://www.cloudbees.com/blog/the-importance-of-feature-flags-in-cicd)
- [infoworld.com: 5 devops use cases for developing with feature flags](https://www.infoworld.com/article/3638153/5-devops-use-cases-for-developing-with-feature-flags.html) Feature flags boost integrations with analytics, provide feature controls to product owners, and improve app rollouts.
- [reflectoring.io: Feature Flags with Spring Boot](https://reflectoring.io/spring-boot-feature-flags/)

##### Keystone Interface and Keystone Flags

- [martinfowler.com: KeystoneInterface](https://martinfowler.com/bliki/KeystoneInterface.html)
- [split.io: Keystone Flags: Feature Flagging With Less Mess](https://split.io/blog/keystone-feature-flags/)

## Git Commands

- Show commit logs:

```bash
git log --oneline --all --graph --decorate
```

- [Removing the last commit](https://gist.github.com/CrookedNumber/8964442):

```bash
git reset --hard HEAD^
git push origin -f
```

- Undoing commits. In case you pushed a wrong change and you want to remove it totally the following commands explain how to do it in soft, mixed and hard mode:

```bash
git reset --soft HEAD^ # Removes the last commit, keeps changed staged
git reset --mixed HEAD^ # Unstages the changes as well
git reset --hard HEAD^ # Discards local changes
```

- Reverting commits:

```bash
git revert 72856ea # Reverts the given commit
git revert HEAD~3.. # Reverts the last three commits
git revert --no-commit HEAD~3..
```

- Recovering lost commits. We can list all last changes and recover back any commit we would like to get again:

```bash
git reflog # Shows the history of HEAD
git reflog show bugfix # Shows the history of bugfix pointer
```

- Amending the last commit. Let’s suppose that you commit a wrong log message and you would like to fix it without changing the commit. — amend flag will allow us to do it:

```bash
git commit --amend
```

- Interactive rebasing. Interactive rebasing can be used for changing commits in many ways such as editing, deleting, and squashing:

```bash
git rebase -i HEAD~5
```

## BitBucket

- [bitbucket.org](https://bitbucket.org/)
- [Atlassian Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

## GitLab

- [gitlab.com](https://gitlab.com/)
- [gitlab.com: GitLab’s guide to CI/CD for beginners](https://about.gitlab.com/blog/2020/07/06/beginner-guide-ci-cd/) CI/CD is a key part of the DevOps journey. Here’s everything you need to understand about this game-changing process.
- [about.gitlab.com: Want a more effective CI/CD pipeline? Try our pro tips](https://about.gitlab.com/blog/2020/07/29/effective-ci-cd-pipelines/) Here’s how to take your CI/CD pipeline to the next level with hands on advice about faster builds, better security and more.
- [gitlab.com: How to do GitLab merge request reviews in VS Code](https://about.gitlab.com/blog/2021/01/25/mr-reviews-with-vs-code/)
- [about.gitlab.com: How we used parallel CI/CD jobs to increase our productivity](https://about.gitlab.com/blog/2021/01/20/using-run-parallel-jobs/) GitLab uses parallel jobs to help long-running jobs run faster.
- [about.gitlab.com: How to use GitLab CI to deploy to multiple environments](https://about.gitlab.com/blog/2021/02/05/ci-deployment-and-environments/)
- [about.gitlab.com: Meet Pipeline Editor, your one-stop-shop for building a CI/CD pipeline](https://about.gitlab.com/blog/2021/02/22/pipeline-editor-overview/)
- [about.gitlab.com: A new era of Kubernetes integrations on GitLab.com](https://about.gitlab.com/blog/2021/02/22/gitlab-kubernetes-agent-on-gitlab-com/) The GitLab Kubernetes Agent enables secure deployments from GitLab SaaS to your Kubernetes cluster and provides deep integrations of your cluster to GitLab.
- [devclass.com: Git a March on: GitLab 13.10 ramps up security, adds support for OpenShift, DORA](https://devclass.com/2021/03/23/gitlab-march-release-focuses-on-security-and-scalability-pops-in-support-for-red-hat-openshift)
- [about.gitlab.com: GitLab 13.11 released with Kubernetes Agent and Pipeline Compliance](https://about.gitlab.com/releases/2021/04/22/gitlab-13-11-released/)
- [lambdatest.com: How To Use GitLab CI To Run Tests Locally? 🌟](https://www.lambdatest.com/blog/use-gitlab-ci-to-run-test-locally/)
- [sdtimes: GitLab 14 aims to do away with DIY DevOps toolchains 🌟](https://sdtimes.com/devops/gitlab-14-aims-to-do-away-with-diy-devops-toolchains/)
- [about.gitlab.com: GitLab 14.1 released with Helm Chart Registry and Escalation Policies](https://about.gitlab.com/releases/2021/07/22/gitlab-14-1-released/)
- [about.gitlab.com: The new Git default branch name](https://about.gitlab.com/blog/2021/03/10/new-git-default-branch-name/)
- [about.gitlab.com: How GitLab's 5 new code review features will make life easier](https://about.gitlab.com/blog/2021/09/09/5-code-review-features/)
- [pythonspeed.com: Building Docker images on GitLab CI: Docker-in-Docker and Podman 🌟](https://pythonspeed.com/articles/gitlab-build-docker-image/)
- [about.gitlab.com: Why we built GitDock, our desktop app to navigate your GitLab activities](https://about.gitlab.com/blog/2021/10/05/gitpod-desktop-app-personal-activities)
- [about.gitlab.com: GitLab’s Kubernetes Operator with support for Red Hat OpenShift is now generally available](https://about.gitlab.com/blog/2021/10/12/open-shift-ga/)
- [containerjournal.com: GitLab Brings Kubernetes Operator to Red Hat OpenShift](https://containerjournal.com/features/gitlab-brings-kubernetes-operator-to-red-hat-openshift/)
- [vadosware.io: Level 1 Automated K8S Deployments With GitLab CI](https://vadosware.io/post/level-one-automated-k8s-deployments-with-gitlab-ci/)
- [about.gitlab.com: GitLab Chart works towards Kubernetes 1.22](https://about.gitlab.com/blog/2021/12/17/gitlab-chart-works-towards-kubernetes-1-22/)
- [Deploy and Manage Gitlab Runners on Amazon EC2](https://aws.amazon.com/blogs/devops/deploy-and-manage-gitlab-runners-on-amazon-ec2/)
- [freecodecamp.org: DevOps with GitLab CI Course 🌟](https://www.freecodecamp.org/news/devops-with-gitlab-ci-course/)
- [testmo.com: GitLab CI/CD Test Automation Pipeline & Reporting](https://www.testmo.com/guides/gitlab-ci-test-automation)
- [community.ops.io: CI CD 101 with GitLab](https://community.ops.io/jatin/ci-cd-101-with-gitlab-4pol)
- [about.gitlab.com: Simple Kubernetes management with GitLab](https://about.gitlab.com/blog/2022/11/15/simple-kubernetes-management-with-gitlab/)

### GitLab Collective

- [stackoverflow.blog: GitLab launches Collective on Stack Overflow](https://stackoverflow.blog/2021/09/22/gitlab-launches-collective-on-stack-overflow/)

## GitHub

- [githubstatus.com 🌟](https://www.githubstatus.com/)
- [buttons.github.io: GitHub Buttons](https://buttons.github.io/)
- [GitHub Codespaces](https://github.com/features/codespaces) Get the full Visual Studio Code experience without leaving GitHub.
    - [infoq.com: GitHub Codespaces Can Now Be Templated to Improve Performance](https://www.infoq.com/news/2022/02/github-codespaces-templates/)
    - [infoworld.com: GitHub Codespaces freely available to all GitHub users](https://www.infoworld.com/article/3679948/github-codespaces-freely-available-to-all-github-users.html) All GitHub users can use the GitHub-hosted development environments free for up to 60 hours per month. Codespaces also added JetBrains IDE, JupyterLab, and GPU support.
- [GitHub CLI](https://cli.github.com/)
    - [github.com/cli/cli](https://github.com/cli/cli)
    - [github.blog: GitHub CLI allows you to close, reopen, and add metadata to issues and pull requests](https://github.blog/changelog/2020-05-11-github-cli-allows-you-to-close-reopen-and-add-metadata-to-issues-and-pull-requests/)
    - [github.blog: Mark pull requests as ready for review, view the diff, review, and merge from GitHub CLI](https://github.blog/changelog/2020-05-26-mark-pull-requests-as-ready-for-review-review-and-merge-from-github-cli/)
- [githubstatus.com/uptime 🌟](https://www.githubstatus.com/uptime)
- [github.blog: How we launched docs.github.com](https://github.blog/2020-07-02-how-we-launched-docs-github-com/)
- [Introducing GitHub’s OpenAPI Description](https://github.blog/2020-07-27-introducing-githubs-openapi-description/)
- [GitHub public roadmap 🌟](https://github.com/github/roadmap)
- [Token authentication requirements for API and Git operations](https://github.blog/2020-07-30-token-authentication-requirements-for-api-and-git-operations/)
- [GitHub's OpenAPI Spec Open-Sourced in Beta](https://www.infoq.com/news/2020/08/GitHub-open-api-spec/)
- [Things you didn't know you could diff in GitHub](https://sebastiandedeyne.com/things-you-didnt-know-you-could-diff-in-github/)
- [github.blog: Set the default branch for newly-created repositories](https://github.blog/changelog/2020-08-26-set-the-default-branch-for-newly-created-repositories/)
- [grafana.com: How we use the Grafana GitHub plugin to track outstanding pull requests](https://grafana.com/blog/2020/09/21/how-we-use-the-grafana-github-plugin-to-track-outstanding-pull-requests/)
- [theregister.com: Passwords begone: GitHub will ban them next year for authenticating Git operations](https://www.theregister.com/2020/12/17/github_bans_passwords/)
- [github.blog: Learn about ghapi, a new third-party Python client for the GitHub API](https://github.blog/2020-12-18-learn-about-ghapi-a-new-third-party-python-client-for-the-github-api/)
- [github.blog: Improving how we deploy GitHub](https://github.blog/2021-01-25-improving-how-we-deploy-github/)
- [github.blog: Deployment reliability at GitHub](https://github.blog/2021-02-03-deployment-reliability-at-github/)
- [github.blog: Extending GitOps to reliability-as-code with GitHub and StackPulse](https://github.blog/2021-02-04-extending-gitops-to-reliability-as-code-with-github-and-stackpulse/)
- [github.blog: Solving the innersource discovery problem - Discoverability](https://github.blog/2021-03-23-solving-the-innersource-discovery-problem/)
- [blog.gruntwork.io: Introducing git-xargs: an open source tool to update multiple GitHub repos](https://blog.gruntwork.io/introducing-git-xargs-an-open-source-tool-to-update-multiple-github-repos-753f9f3675ec)
- [github.blog: Security keys are now supported for SSH Git operations 🌟](https://github.blog/2021-05-10-security-keys-supported-ssh-git-operations/)
- [education.github.com](https://education.github.com/) Real-world tools, engaged students. GitHub Education helps students, teachers, and schools access the tools and events they need to shape the next generation of software development.
- [github.blog: GitHub brings supply chain security features to the Go community](https://github.blog/2021-07-22-github-supply-chain-security-features-go-community/)
- [dev.to: How to never type passwords when using Git](https://dev.to/github/how-to-never-type-passwords-when-using-git-18bb) We're deprecating password support for Git operations to keep you more secure. You can authenticate Git actions using:
    - SSH keys
    - Personal Access Tokens
    - OAuth Apps
    - Credential Manager
    - GH Desktop
    - GH CLI
    - Physical keys
- [dev.to: 10 Fun Things You Can Do With GitHub.dev 😎](https://dev.to/lostintangent/10-awesome-things-you-can-do-with-github-dev-5fm7)
- [github.blog: GitHub CLI 2.0 includes extensions!](https://github.blog/2021-08-24-github-cli-2-0-includes-extensions/)
- [dev.to: Git and GitHub: The Complete Guides - Chapter 6: GitHub Merging](https://dev.to/ifierygod/git-and-github-the-complete-guides-chapter-6-2c74)
- [github.blog: Improved pull request file filtering](https://github.blog/changelog/2021-09-27-improved-pull-request-file-filtering/) Filtered files on the Pull Request Files Changed tab are now completely hidden from view (not just collapsed). This helps decrease distractions and lets you focus on just the files you need to review.
- [dev.to: Git and GitHub Series' Articles - The Complete Guides 🌟](https://dev.to/ifierygod/series/14420)
- [infoworld.com: GitHub introduces code review controls 🌟](https://www.infoworld.com/article/3639588/github-introduces-code-review-controls.html) New controls in the popular code-sharing site are designed to deal with ‘drive-by‘ pull request approvals and ‘spammy’ change requests.
- [freecodecamp.org: Git and GitHub Tutorial – Version Control for Beginners 🌟](https://www.freecodecamp.org/news/git-and-github-for-beginners)
- [github/hub 🌟](https://github.com/github/hub) A command-line tool that makes git easier to use with GitHub.
- [==dev.to: New GitHub Rules Guide [git push -u origin main]==](https://dev.to/bekbrace/new-rules-in-github-git-push-u-origin-main-2k82) This post explains very quickly how to push your code to your GitHub repository following the new rules imposed by GitHub.
- [==dev.to: Learn how to use Git and GitHub in a team like a pro==](https://dev.to/colocodes/learn-how-to-use-git-and-github-in-a-team-like-a-pro-2dk7)
    - [==dev.to: Learn how to use Git and GitHub in a team like a pro (part 2)==](https://dev.to/colocodes/learn-how-to-use-git-and-github-in-a-team-like-a-pro-part-2-11j)
- [==dev.to: Git and GitHub for beginners==](https://dev.to/ericawanja/git-and-github-for-beginners-33a0)
- [==adamtheautomator.com: How to Manage GitHub Actions Environment Variables and Secrets==](https://adamtheautomator.com/github-actions-environment-variables/)
- [dev.to: Introduction to Git and GitHub](https://dev.to/estherwanjiru/introduction-to-git-and-github-25ei)
- [github.blog: Improving GitHub code search](https://github.blog/2021-12-08-improving-github-code-search/)
- [github.blog: Lists are now available as a public beta](https://github.blog/changelog/2021-12-09-lists-are-now-available-as-a-public-beta/) Lists level up the starring experience by making it easy to organize and curate your favorite repositories on GitHub. You can create public lists that appear on your stars page at https://github.com/USERNAME?tab=stars.
- [freecodecamp.org: How to Use the .github Repository](https://www.freecodecamp.org/news/how-to-use-the-dot-github-repository/)
- [==about.gitlab.com: How to install and use the GitLab Kubernetes Operator (on OCP)==](https://about.gitlab.com/blog/2021/11/16/gko-on-ocp)
- [github.blog: Dependency graph now supports GitHub Actions](https://github.blog/2022-01-31-dependency-graph-now-supports-github-actions/) The dependency graph helps developers and maintainers understand the code they depend on, and now includes GitHub Actions!
- [==github.blog: How to build a CI/CD pipeline with GitHub Actions in four simple steps==](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/) A quick guide on the advantages of using GitHub Actions as your preferred CI/CD tool—and how to build a CI/CD pipeline with it.
- [github.blog: How to start using reusable workflows with GitHub Actions](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/) Reusable workflows offer a simple and powerful way to avoid copying and pasting workflows across your repositories.
- [github.blog: Getting started with project planning on GitHub](https://github.blog/2022-02-11-getting-started-with-project-planning-on-github/) Stop context switching. Keep your team’s project planning next to your code.
- [freecodecamp.org: How to Fork a GitHub Repository – A Complete Workflow](https://www.freecodecamp.org/news/how-to-fork-a-github-repository/)
- [==github.com/Lightning-AI/engineering-class: Lightning Bits: Engineering for Researchers== 🌟](https://github.com/Lightning-AI/engineering-class) **This repository contains additional materials and show notes for the Lightning Bits: Engineering for Researchers video series.**
    - [github.com/Lightning-AI/engineering-class: Episode 8: Creating a Pull Request on GitHub](https://github.com/Lightning-AI/engineering-class/blob/main/ep08-github-pr/Ep08-ShowNotes.md)
    - [github.com/Lightning-AI/engineering-class: Episode 9: Collaborating with Pull Requests using GitHub](https://github.com/Lightning-AI/engineering-class/blob/main/ep09-github-collab/Ep09-ShowNotes.md#syncing-forks-with-upstream)
- [github.com/marketplace: Use AWS Secrets Manager secrets in GitHub jobs 🌟](https://github.com/marketplace/actions/aws-secrets-manager-github-action)
- [tylercipriani.com: GitHub's Missing Merge Option](https://tylercipriani.com/blog/2022/09/30/githubs-missing-merge-option/)
- [==steampipe.io: Top 3 ways to improve GitHub org security==](https://steampipe.io/blog/github-security-tips) Gain some practical tips for securing your GitHub organizations based on findings from common security incidents.
- [dev.to/opensauced: How to Create a Good Pull Request Template (and Why You Should Add Gifs)](https://dev.to/opensauced/how-to-create-a-good-pull-request-template-and-why-you-should-add-gifs-4i0l)
- [==youtube: GitHub Masterclass (Spanish)== 🌟](https://www.youtube.com/playlist?list=PL0pgb_7nDofA1hJpkpPf4qHQTYZbPVT5M)
- [freecodecamp.org: How to Build a GitHub Template Repository for Scaffolding with React, Vite, and TailwindCSS](https://www.freecodecamp.org/news/create-a-github-template-repository-with-react-vite-and-tailwindcss/)
- [docs.github.com: Using SSH over the HTTPS port 🌟](https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port) Sometimes, firewalls refuse to allow SSH connections entirely. If using HTTPS cloning with credential caching is not an option, you can attempt to clone using an SSH connection made over the HTTPS port. Most firewall rules should allow this, but proxy servers may interfere.
- [freecodecamp.org: How to Contribute to Open-Source Projects – Git & GitHub Workflow for Beginners](https://www.freecodecamp.org/news/git-and-github-workflow-for-open-source/)
- [==mattias.engineer: Azure Federated Identity Credentials for GitHub==](https://mattias.engineer/blog/2024/azure-federated-credentials-github/)
- [freecodecamp.org: How to Create and Sync Git and GitHub Repositories](https://www.freecodecamp.org/news/create-and-sync-git-and-github-repositories/)

### Fake it til you make it

- [github.com/rakyll/fake-it-til-you-make-it](https://github.com/rakyll/fake-it-til-you-make-it) Have you come across to someone that thinks you don't deserve a job because you don't have GitHub contributions? Never worked for a company who hired based on GitHub contributions alone. If anyone is bugging you because you are not an open source developer or your company doesn't use GitHub, use fake-it-til-you-make-it to generate two years of contributions.

### GitHub Lab


### GitHub Code Scanner

- https://docs.github.com/en/code-security/code-scanning
- [analyticsindiamag.com: GitHub launches code scanner to flag security vulnerabilities](https://analyticsindiamag.com/github-launches-code-scanner-to-flag-security-vulnerabilities/) The new experimental analysis can have a higher false-positive rate relative to results from standard CodeQL analysis.

### GitHub Discussions

- [github.com/giscus/giscus](https://github.com/giscus/giscus) A comments system powered by [GitHub Discussions](https://docs.github.com/en/discussions). Let visitors leave comments and reactions on your website via GitHub! Heavily inspired by [utterances](https://github.com/utterance/utterances).

### GitHub Actions

- [github.blog: Testing cloud apps with GitHub Actions and cloud-native open source tools](https://github.blog/2020-10-09-devops-cloud-testing/)
- [laravel-news.com: Generate GitHub Actions Config for Laravel Projects with Ghygen](https://laravel-news.com/generate-github-actions-config-for-laravel-projects-with-ghygen)
- [blog.codecentric.de: Stop re-writing pipelines! Why GitHub Actions drive the future of CI/CD](https://blog.codecentric.de/en/2021/03/github-actions-nextgen-cicd/)
- [github.blog: Implementing least privilege for secrets in GitHub Actions](https://github.blog/2021-04-13-implementing-least-privilege-for-secrets-in-github-actions/)
- [github.blog: Work with GitHub Actions in your terminal with GitHub CLI](https://github.blog/2021-04-15-work-with-github-actions-in-your-terminal-with-github-cli/)
- [github.blog: GitHub Actions: Control permissions for GITHUB_TOKEN 🌟](https://github.blog/changelog/2021-04-20-github-actions-control-permissions-for-github_token/)
- [github.blog: GitHub Actions update: Helping maintainers combat bad actors](https://github.blog/2021-04-22-github-actions-update-helping-maintainers-combat-bad-actors/)
- [github.blog: How we use GitHub Actions to manage GitHub Docs](https://github.blog/2021-04-28-use-github-actions-manage-docs/)
- [vimeo.com: How to Create a CI/CD Pipeline with GitHub Actions and K8s Like a Boss](https://vimeo.com/552276182)
- [actions-runner-controller 🌟](https://github.com/actions-runner-controller/actions-runner-controller) Kubernetes controller for GitHub Actions self-hosted runnners
- [github.com: Branch Cleanup Action 🌟](https://github.com/jessfraz/branch-cleanup-action) A GitHub action to automatically delete the branch after a pull request has been merged.
- [github.blog: GitHub Actions: Ephemeral self-hosted runners & new webhooks for auto-scaling](https://github.blog/changelog/2021-09-20-github-actions-ephemeral-self-hosted-runners-new-webhooks-for-auto-scaling/)
- [github.blog: Showing code scanning alerts on pull requests](https://github.blog/changelog/2021-09-27-showing-code-scanning-alerts-on-pull-requests/)
- [github.blog: 10 GitHub Actions resources to bookmark from the basics to CI/CD](https://github.blog/2021-11-04-10-github-actions-resources-basics-ci-cd/)
- [==resources.github.com: What is GitHub Actions? How automation & CI/CD work on GitHub (whitepaper/pdf)==](https://resources.github.com/devops/tools/automation/actions)
- [==github.blog: Container signing added to the Publish Docker Container workflow for GitHub Actions==](https://github.blog/changelog/2021-12-06-container-signing-added-to-the-publish-docker-container-workflow-for-github-actions/) We have added support for [sigstore](https://www.sigstore.dev/) container signing to the default GitHub Actions starter workflow for publishing container images. New workflows on public repositories will use this by default. If you have an existing workflow, you will need to update your workflow to take advantage of this capability.
- [dev.to: What's the difference between a GitHub Action and a Workflow?](https://dev.to/github/whats-the-difference-between-a-github-action-and-a-workflow-2gba)
- [github.blog: 5 automations every developer should be running](https://github.blog/2021-12-16-5-automations-every-developer-should-be-running/)
- [==github.blog: Getting started with GitHub Actions just got easier!==](https://github.blog/2021-12-17-getting-started-with-github-actions-just-got-easier/)
- [github.blog: GitHub Actions: Improvements to GitHub Actions starter experience](https://github.blog/changelog/2021-12-17-github-actions-improvements-to-github-actions-starter-experience/)
- [blog.fleetdm.com: 4 tips for GitHub Actions usability (+2 bonus tips for debugging)](https://blog.fleetdm.com/4-tips-for-github-actions-usability-2-debugging-4c0c920adfde)
- [==freecodecamp.org: How to Build Your First JavaScript GitHub Action==](https://www.freecodecamp.org/news/build-your-first-javascript-github-action/)
- [dev.to: Make your first contribution to a GitHub Action!](https://dev.to/github/how-to-edit-a-github-action-3j14)
- [blog.shreyaspatil.dev: Automate library publishing to Maven Central with GitHub Actions Workflow Dispatch](https://blog.shreyaspatil.dev/automate-library-publishing-to-maven-central-with-github-actions-workflow-dispatch)
- [laravel-news.com: Deploy your PHP Codebase with Ansible and GitHub Actions](https://laravel-news.com/deploy-your-php-app-with-ansible-and-github-actions)
- [infoq.com: How GitHub Does DevOps for its iOS and Android Apps](https://www.infoq.com/news/2022/01/GitHub-devops-mobile-apps/)
- [blog.gskinner.com: Flutter: Easily add CI testing with GitHub Actions](https://blog.gskinner.com/archives/2022/01/flutter-easily-add-ci-testing-with-github-actions.html)
- [==devblogs.microsoft.com: .NET 💜 GitHub Actions==](https://devblogs.microsoft.com/dotnet/dotnet-loves-github-actions/)
- [registry.terraform.io/modules/markti/github-runner](https://registry.terraform.io/modules/markti/github-runner/azurerm) Provision a Custom Runner for GitHub Actions
- [build5nines.com: Configuring Manual Triggers in GitHub Actions with `workflow_dispatch`](https://build5nines.com/configuring-manual-triggers-in-github-actions-with-workflow_dispatch/)

#### GitHub Actions Marketplace

- [flat-data](https://github.com/marketplace/actions/flat-data) Flat Data is a GitHub action which makes it easy to fetch data and commit it to your repository as flatfiles. The action is intended to be run on a schedule, retrieving data from any supported target and creating a commit if there is any change to the fetched data.

### GitHub Actions and OpenShift

- [redhat.com: Red Hat and GitHub Collaborate to Expand the Developer Experience on Red Hat OpenShift with GitHub Actions 🌟](https://www.redhat.com/en/about/press-releases/red-hat-and-github-collaborate-expand-developer-experience-red-hat-openshift-github-actions) Industry’s leading enterprise Kubernetes platform now integrates with GitHub, bringing DevOps automation tools from the world’s largest developer platform into the OpenShift ecosystem
- [openshift.com: Deploying to OpenShift using GitHub Actions](https://www.openshift.com/blog/deploying-to-openshift-using-github-actions)
- [github.com: RedHat Actions 🌟](https://github.com/redhat-actions)
- [github.com: OpenShift GitHub Actions Runner 🌟](https://github.com/redhat-actions/openshift-actions-runner)
- [github.com: OpenShift GitHub Actions Runner Chart 🌟](https://github.com/redhat-actions/openshift-actions-runner-chart)

### GitHub Copilot

- [GitHub Copilot 🌟](https://copilot.github.com/) Your AI pair programmer. With GitHub Copilot, get suggestions for whole lines or entire functions right inside your editor.
- [xataka.com: Para qué programar cuando una máquina lo hace (un poco) por ti: así es Github Copilot, un sistema que se nutre del prodigioso GPT-3](https://www.xataka.com/robotica-e-ia/programar-cuando-maquina-hace-poco-ti-asi-github-copilot-sistema-que-se-nutre-prodigioso-gpt-3)
- [thenewstack.io: GitHub Copilot: A Powerful, Controversial Autocomplete for Developers](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers)
- [xataka.com: Llevo algunos días usando Copilot de GitHub para programar y esta es mi experiencia](https://www.xataka.com/robotica-e-ia/llevo-algunos-dias-usando-copilot-github-para-programar-esta-mi-experiencia)
- [dev.to: GitHub Copilot blew my mind on a code-along exercise](https://dev.to/colocodes/github-copilot-blew-my-mind-on-a-code-along-exercise-186n)
- [GitHub Copilot is generally available to all developers](https://github.blog/2022-06-21-github-copilot-is-generally-available-to-all-developers/) **We’re making GitHub Copilot, an AI pair programmer that suggests code in your editor, generally available to all developers for $10 USD/month or $100 USD/year. It will also be free to use for verified students and maintainers of popular open source projects.**
- [xataka.com: GitHub Copilot, el asistente para programar basado en IA, ya está disponible para todos: cuánto cuesta y quienes lo pueden usar gratis](https://www.xataka.com/aplicaciones/github-copilot-asistente-para-escribir-codigo-basado-ia-esta-disponible-para-todos-esto-que-costara)
- [genbeta.com: Ya hay organizaciones pro-software libre abandonando GitHub por su uso comercial de proyectos open source en Copilot](https://www.genbeta.com/desarrollo/hay-organizaciones-pro-software-libre-abandonando-github-su-uso-comercial-proyectos-open-source-copilot)
- [xataka.com: Copilot ya escribe el 40% del código de lenguajes como Java o Python que llega a GitHub. En cinco años llegará al 80%](https://www.xataka.com/aplicaciones/copilot-escribe-40-codigo-lenguajes-como-java-python-que-llega-a-github-cinco-anos-llegara-al-80)
- [xataka.com: Copilot es una revolución para programadores (pero también un potencial problema legal para Microsoft)](https://www.xataka.com/robotica-e-ia/copilot-revolucion-para-programadores-tambien-potencial-problema-legal-para-microsoft)
- [github.blog: GitHub Copilot X: The AI-powered developer experience](https://github.blog/2023-03-22-github-copilot-x-the-ai-powered-developer-experience/) GitHub Copilot is evolving to bring chat and voice interfaces, support pull requests, answer questions on docs, and adopt OpenAI’s GPT-4 for a more personalized developer experience.
- [techcommunity.microsoft.com: Coding Frameworks and languages are no longer the point, prompting is](https://techcommunity.microsoft.com/t5/educator-developer-blog/coding-frameworks-and-languages-are-no-longer-the-point/ba-p/3820265)
- [github.blog/developer-skills: 10 unexpected ways to use GitHub Copilot](https://github.blog/developer-skills/programming-languages-and-frameworks/10-unexpected-ways-to-use-github-copilot/) GitHub Copilot is widely known for its code generation feature. Learn how the AI assistant’s abilities can extend beyond just code generation.

#### GitHub CoPilot VS GPT-3


#### GitHub Copilot X

- [computerhoy.com: GitHub Copilot X: así es la nueva IA parecida a ChatGPT y destinada a ayudar a programadores](https://computerhoy.com/software/github-copilot-x-nueva-ia-parecida-chatgpt-destinada-ayudar-programadores-1219266)

#### Alternatives

- [xataka.com: Los programadores ya alucinaban con CoPilot y ChatGPT, pero ahora DeepMind va más allá con AplhaCode](https://www.xataka.com/robotica-e-ia/programadores-alucinaban-copilot-chatgpt-ahora-deepmind-va-alla-aplhacode)
- [lucidrains/PaLM-rlhf-pytorch](https://github.com/lucidrains/PaLM-rlhf-pytorch) The first open source equivalent of ChatGPT. Implementation of RLHF (Reinforcement Learning with Human Feedback) on top of the PaLM architecture. Basically ChatGPT but with PaLM

##### CodiumAI

- [codium.ai: We’ve launched CodiumAI powered by TestGPT and raised $11M. Here’s why](https://www.codium.ai/blog/codiumai-powered-by-testgpt-accounces-beta-and-raised-11m/)

## Gitea

- [Gitea](https://gitea.com/)

## Sapling

- [sapling-scm.com](https://sapling-scm.com/docs/introduction/)

## Git Tools

- [Atlassian Sourcetree](https://www.sourcetreeapp.com/)
    - [Sourcetree Cheat Sheet](https://kapeli.com/cheat_sheets/Sourcetree.docset/Contents/Resources/Documents/index)
- [gitkraken.com](https://www.gitkraken.com/)
    - [GitKraken Git Cheat](https://www.gitkraken.com/resources/gitkraken-cheat-sheet)
    - [youtube: GitKraken Tutorials and Tips](https://www.youtube.com/watch?v=gjtXTm_TvvE&list=PLe6EXFvnTV78WqGmGSq8JPnafR3lAa55n)
- [Visual Studio Code (Git Extensions)](visual-studio.md)
- [Visual Studio Online](https://visualstudio.microsoft.com/services/visual-studio-codespaces/)
- [git-lfs/git-lfs: Git Large File Storage](https://github.com/git-lfs/git-lfs) Git extension for versioning large files
- [==github.com/MichaelMure/git-bug==](https://github.com/MichaelMure/git-bug) **Distributed, offline-first bug tracker embedded in git, with bridges**

### Git Credential Manager

- [==Git Credential Manager==](https://github.com/GitCredentialManager/git-credential-manager) **Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services.**
- Git Credential Manager (GCM) is a secure Git credential helper built on .NET that runs on Windows, macOS, and Linux.
- [github.blog: Git Credential Manager: authentication for everyone](https://github.blog/2022-04-07-git-credential-manager-authentication-for-everyone/) Ensuring secure access to your source code is more important than ever. Git Credential Manager helps make that easy.

### Semantic-release. CI/CD semantic release workflow (semantic Versioning, commit format and releases)

- [semantic-release.gitbook.io 🌟](https://semantic-release.gitbook.io/semantic-release/) Semantic-release automates the whole package release workflow including: determining the next version number, generating the release notes and publishing the package.
- [css-tricks.com: How to Automate Project Versioning and Releases with Continuous Deployment 🌟](https://css-tricks.com/how-to-automate-project-versioning-and-releases-with-continuous-deployment/)

## Azure DevOps (formerly known as VSTS)

- [Azure DevOps Labs 🌟](https://azuredevopslabs.com/)
- [Microsoft Visual Studio Team Services (VSTS)](https://www.dotnetcurry.com/visualstudio/1322/what-is-visual-studio-team-system-vsts)
- [Microsoft Visual Studio Team Services (VSTS) Tutorial: The Cloud ALM Platform](https://www.softwaretestinghelp.com/microsoft-vsts-tutorial-1/)
- [slideshare.net: Git version control and trunk based approach with VSTS](https://www.slideshare.net/arunmurughan/git-version-control-and-trunk-based-approach-with-vsts)
- [How We Use Git at Microsoft](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/use-git-microsoft)

## Pre Commit Hooks

- [pre-commit](https://pre-commit.com/) A framework for managing and maintaining multi-language pre-commit hooks.

## Merge BOTs

- The Merge Bot is a tool to orchestrate pull requests merging into the stable branches.

### Tips

- Use bots to accomplish tasks like merging PR's that have been approved and automatically updating dependencies. Usage of one of these bots might allow us to trigger certain builds based off of specific GitHub tags,  it would allow us to only selectively run certain test suites and increase the throughput of the build by only testing changes made in a branch / PR.
- Investigate options that are available and see if we can integrate them with CI.
- We should be able to configure this bot to automatically apply labels to PR's based off of what is changed in a PR. For instance, if a PR contains any documentation changes, the area/Documentation label can be applied.

### Jenkins for git merges

- [**Git Plugin**: Merge Extensions](https://plugins.jenkins.io/git/#merge-extensions)
- [GitHub Pull Request Builder Plugin](https://plugins.jenkins.io/ghprb/) , [github ref](https://github.com/jenkinsci/ghprb-plugin). You should probably migrate to GitHub Branch Source Plugin.
- [GitHub Branch Source Plugin:](https://plugins.jenkins.io/github-branch-source/) Allows you to create a new project based on the repository structure from one or more GitHub users or organizations.

### Bitbucket for git merges

- [Automatic branch merging](https://confluence.atlassian.com/bitbucketserver/automatic-branch-merging-776639993.html)
- [BitBucket Auto Merge](https://github.com/bluefrg/bitbucket-auto-merge) Automatically create and merge pull request to keep branches in sync.
- [Checks for merging pull requests](https://confluence.atlassian.com/bitbucketserver/checks-for-merging-pull-requests-776640039.html)
- [BitBucket Bot for Microsoft Teams](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/new-bitbucket-bot-for-microsoft-teams/ba-p/218212)
- [Code Dog](https://code-dog.app/) Merge your Pull Requests sooner. Some of the Slack messages your team sends are critical for productivity.
Automate them.
- [Jenkins Plugin: Bitbucket Push and Pull Request](https://plugins.jenkins.io/bitbucket-push-and-pull-request/)
- [Configure bitbucket-pipelines.yml to automatically merge feature branch to master?](https://community.atlassian.com/t5/Bitbucket-questions/configure-bitbucket-pipelines-yml-to-automatically-merge-feature/qaq-p/793222)

### GitLab for git merges

- [Auto-merge between release branches](https://gitlab.com/gitlab-org/gitlab/-/issues/2785)
- [Provide merge bot functionality](https://gitlab.com/gitlab-org/gitlab/-/issues/14595)
- [lab.texthtml.net: Gitlab Merge Bot](https://lab.texthtml.net/gitlab/merge-bot)
    - [DockerHub: Gitlab Merge Bot](https://hub.docker.com/r/texthtml/gitlab-merge-bot/) Bot assistant for code review and merge requests approval for Gitlab
    - Our group has a bot that creates merge requests for certain mechanical changes to our code base. We'd like these MRs to get merged in automatically if/when the CI pipeline succeeds, but our projects require an approval from a member of our group. This means that right now a human has to manually click on "approve" and "merge" for each bot-created MR. Apparently GitLab doesn't have a way to set different approval rules for some users, so I haven't found a way to make the bot's user immune to this requirement.
    - My current idea is to have a separate process that approves each of the merge requests created by the bot. Is there an easy way to do this programmatically? That is, is there an API (or better yet, a command line tool) that, when given the name of the branch for a merge request, approves the merge request associated with that branch?
    - I'm also open to other ways of getting these changes in with minimal human intervention. I do want them to pass the CI pipeline, though (which is currently accomplished by having them use MRs) and the MRs also help in the rare cases where the pipeline fails, so we can debug what went wrong.

#### Marge GitLab bot

- [Marge-bot: A merge-bot for GitLab](https://github.com/smarkets/marge-bot)
- [Example: gitlab.gnome.org/marge-merge-bot](https://gitlab.gnome.org/marge-merge-bot)
- [Example: GStreamer Merge Bot](https://gitlab.freedesktop.org/gstreamer-merge-bot)

### Jenkins-X bots

- [Jenkins-X UpdateBOT](https://github.com/jenkins-x/updatebot) A simple bot for updating dependencies in source code and automatically generating Pull Requests in downstream projects.

### Plastic SCM bot

- [Plastic SCM](https://www.plasticscm.com/)
- [blog.plasticscm.com: Add a mergebot to your repo!](http://blog.plasticscm.com/2018/09/add-mergebot-to-your-repo.html)
- [Plastic SCM DevOps Mergebot to implement a trunk-based development cycle ](https://github.com/PlasticSCM/trunk-mergebot)
- [PlasticSCM MergeBot Jenkins Plugin](https://wiki.jenkins.io/display/JENKINS/PlasticSCM+MergeBot+plugin)
- [genbeta.com: Plastic SCM Mergebot: automatizando tu pipeline de desarrollo](https://www.genbeta.com/desarrollo/plastic-scm-mergebot-automatizando-tu-pipeline-desarrollo)

### Mergify bot


### GitHub bots

- [github-rebase-bot](https://github.com/nicolai86/github-rebase-bot) A github bot that monitors repository PRs, rebases them and merges them as they pass tests.
- [Bulldozer: GitHub Pull Request Auto-Merge Bot](https://github.com/palantir/bulldozer)
- [github-merge-bot](https://github.com/depop/github-merge-bot) Automates the process of merging pull requests and keeping them up-to-date.
- [github.com/squalrus/merge-bot: PR Merge Bot](https://github.com/squalrus/merge-bot) A GitHub action that manages pull request integrations
- [Odoo Mergebot](https://github.com/odoo/odoo/wiki/Mergebot)
- [gmaster.io - Mergedroid: Automate merging just by analyzing your GitHub repo.](https://gmaster.io/mergedroid) A BOT that solves conflicts in pull requests without manual intervention.
- [Kodiak](https://kodiakhq.com/) GitHub bot for updating and merging pull requests
- [Rultor](http://www.rultor.com/) A merging bot for Github pull requests
    - [Rultor, a Merging Bot](https://www.yegor256.com/2014/07/24/rultor-automated-merging.html)
    - [help.github.com: Enabling required status checks:](https://help.github.com/en/github/administering-a-repository/enabling-required-status-checks)
        - Select Require status checks to pass before merging
        - Choose (create) a status check, that always fails

#### Bors GitHub bot

- [Bors Bot](https://bors.tech/)
- [Bors-ng: A merge bot for GitHub Pull Requests](https://github.com/bors-ng/bors-ng)
- [Example: CockroachDB's Bors Merge Bot](https://wiki.crdb.io/wiki/spaces/CRDB/pages/73204099/Bors+Merge+Bot)

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/R8_veQiYBjI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/HlmZLXMOpEM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/PGyhBwLyK2U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="469" height="834" src="https://www.youtube.com/embed/o3qURBllpGM" title="GitHub CoPilot is like a second brain" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/e2IbNHi4uCI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/U_IFGpJDbeU?si=XzHSGU9dTH-1_0EW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </center>

## Slides

??? note "Click to expand!"

    <center>
    <iframe src="//www.slideshare.net/slideshow/embed_code/key/ju2kFOuS5w1jk4" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/kobac/async-code-reviews-are-killing-your-companys-throughput-248758692" title="Async Code Reviews Are Killing Your Company’s Throughput - Dragan Stepanović" target="_blank">Async Code Reviews Are Killing Your Company’s Throughput - Dragan Stepanović</a> </strong> from <strong><a href="//www.slideshare.net/kobac" target="_blank">Dragan Stepanović</a></strong> </div>
    </center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="es" dir="ltr">No, ninguna inteligencia artificial te va a quitar tu trabajo como data scientist o developer.<br><br>La automatización de <a href="https://twitter.com/github?ref_src=twsrc%5Etfw">@github</a> CoPilot creará más trabajos de los que destruirá.<br><br>Acá te explico porque 👇🧵</p>&mdash; Xavier Carrera (@XaviGrowth) <a href="https://twitter.com/XaviGrowth/status/1410040729305485317?ref_src=twsrc%5Etfw">June 30, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m using GitHub Copilot in the last few hours and all I&#39;m going to say that it is magic. It really helps me with dealing with the boilerplate, writing code comments, and avoiding antipatterns. It also is occasionally reading my mind.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1413006071627583488?ref_src=twsrc%5Etfw">July 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">GitHub&#39;s Copilot would benefit from a compliance feature to help developers detect when any code, hand written or auto generated, possibly violates another projects license or copyright.</p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1412975901277671426?ref_src=twsrc%5Etfw">July 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Today&#39;s <a href="https://twitter.com/code?ref_src=twsrc%5Etfw">@code</a> tip: the git stash commands<br><br>Create, apply, and manage <a href="https://twitter.com/hashtag/git?src=hash&amp;ref_src=twsrc%5Etfw">#git</a> stashes using VS Code commands.<br><br>Stashes let you quickly save off your workspace changes and restore them when they are needed again<a href="https://twitter.com/hashtag/code2020?src=hash&amp;ref_src=twsrc%5Etfw">#code2020</a> <a href="https://t.co/VPursGdRka">pic.twitter.com/VPursGdRka</a></p>&mdash; Matt Bierner (@mattbierner) <a href="https://twitter.com/mattbierner/status/1276915695788470273?ref_src=twsrc%5Etfw">June 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Writing good Git commit messages matters!<br><br>A thread about how to write clean commit messages:<br><br>🧵 👇</p>&mdash; Deni Moka⚡ (@dmokafa) <a href="https://twitter.com/dmokafa/status/1351152452179996682?ref_src=twsrc%5Etfw">January 18, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Here are _some_ of the most essential git operations you will need when working as a developer.<br><br>🧵🔽 <a href="https://t.co/ZTUUObuj70">pic.twitter.com/ZTUUObuj70</a></p>&mdash; Oliver Jumpertz (@oliverjumpertz) <a href="https://twitter.com/oliverjumpertz/status/1374323799991054339?ref_src=twsrc%5Etfw">March 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Git is by far the most used source control management tool out there.<br><br>It is basially an essential to know. And this justifies knowing a few of the most important git commands you need in your daily work.<br><br>Here are 19 that any developer should know.<br><br>A thread. ↓ <a href="https://t.co/nLglrUWp6o">pic.twitter.com/nLglrUWp6o</a></p>&mdash; Oliver Jumpertz (@oliverjumpertz) <a href="https://twitter.com/oliverjumpertz/status/1425461523426725891?ref_src=twsrc%5Etfw">August 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Really cool and cute way to explain git commands.<br><br>By <a href="https://twitter.com/girlie_mac?ref_src=twsrc%5Etfw">@girlie_mac</a> <br><br>If you like this kind of tech doodles, check out her Github repo: <a href="https://t.co/2J3vEt6Eb9">https://t.co/2J3vEt6Eb9</a> <a href="https://t.co/wkBqlg9584">pic.twitter.com/wkBqlg9584</a></p>&mdash; Alex Xu (@alexxubyte) <a href="https://twitter.com/alexxubyte/status/1537825597413478401?ref_src=twsrc%5Etfw">June 17, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Best Free Git Courses for beginners<br>1. Git Started With GitHub -<a href="https://t.co/ajJlJUz34i">https://t.co/ajJlJUz34i</a><br>2. Introduction to Git - <a href="https://t.co/T0mIUkIBbB">https://t.co/T0mIUkIBbB</a><br>2. GIT 5-day Challenge - <a href="https://t.co/bj687fKJ8Y">https://t.co/bj687fKJ8Y</a><br>4. Command Line Essentials: - <a href="https://t.co/us18hMcw9P">https://t.co/us18hMcw9P</a><br>5. Git expert - <a href="https://t.co/AmRMZznQzu">https://t.co/AmRMZznQzu</a> <a href="https://t.co/FM6Oh2KGMD">pic.twitter.com/FM6Oh2KGMD</a></p>&mdash; javinpaul (@javinpaul) <a href="https://twitter.com/javinpaul/status/1545716033302003713?ref_src=twsrc%5Etfw">July 9, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If you&#39;re a programmer, these 10 git commands will save you hours of research🧵👇</p>&mdash; Ujjwal Chadha (@ujjwalscript) <a href="https://twitter.com/ujjwalscript/status/1560115594640310272?ref_src=twsrc%5Etfw">August 18, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">As a Developer, how much do you use Github?</p>&mdash; • nanou • (@NanouuSymeon) <a href="https://twitter.com/NanouuSymeon/status/1586245047850237955?ref_src=twsrc%5Etfw">October 29, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">99% of the programmers only know the basic git commands (push, pull and commit)<br><br>These 10 git commands will save you hours of research time when you&#39;re stuck:</p>&mdash; Ujjwal Chadha (@ujjwalscript) <a href="https://twitter.com/ujjwalscript/status/1593143603001708548?ref_src=twsrc%5Etfw">November 17, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If you want to master Git, watch these YouTube videos:</p>&mdash; Nikki Siapno (@NikkiSiapno) <a href="https://twitter.com/NikkiSiapno/status/1597836278543880193?ref_src=twsrc%5Etfw">November 30, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How to organizing GitHub repositories for your project?<br><br>A thread 👇 <a href="https://t.co/QSnnyDyupe">pic.twitter.com/QSnnyDyupe</a></p>&mdash; Rakesh Jain (@devops_tech) <a href="https://twitter.com/devops_tech/status/1655208517903740928?ref_src=twsrc%5Etfw">May 7, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>