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

- [Wikipedia: Git](https://en.wikipedia.org/wiki/Git)
- [Git](https://git-scm.com/)
    - [git-scm.com/book](https://git-scm.com/book)
- [devdocs.io/git/](https://devdocs.io/git/)
- [tutorialzine.com: Learn git in 30 minutes 🌟](https://tutorialzine.com/2016/06/learn-git-in-30-minutes)
- [3 Git Commands I Use Every Day](https://dev.to/gonedark/3-git-commands-i-use-every-day)
- [Git and Github in Plain English](https://red-badger.com/blog/2016/11/29/gitgithub-in-plain-english)
- [opensource.com: How to restore older file versions in Git](https://opensource.com/life/16/7/how-restore-older-file-versions-git)
- [9 awesome git tricks](https://tychoish.com/post/9-awesome-git-tricks/)
- [Awesome Git 🌟](https://github.com/dictcp/awesome-git)
- [dzone.com: intro git 🌟](https://dzone.com/articles/intro-git)
- [dzone.com: Top 20 git commands with examples 🌟](https://dzone.com/articles/top-20-git-commands-with-examples)
- [dzone.com: 8 Useful But Not Well-Known Git Concepts](https://dzone.com/articles/8-useful-but-not-well-known-git-concepts) These lesser-known Git tricks can help you solve problems that are not handled well by the GitHub and BitBucket GUIs
- [dzone.com: Git Commands Tutorial - Part 1](https://dzone.com/articles/git-commands-tutorial-part-1)
- [dzone.com: Git Commands Tutorial - Part 2](https://dzone.com/articles/git-commands-tutorial-part-2)
- [Dzone refcard: Getting started with Git](https://dzone.com/refcardz/getting-started-git)
- [Oh shit, git!](https://ohshitgit.com/)
- [freecodecamp.org: Learn Git Fundamentals – A Handbook on Day-to-Day Development Tasks 🌟](https://www.freecodecamp.org/news/learn-git-basics/)
- [How to Get More Out of Your Git Commit Message](https://datree.io/blog/git-commit-message-conventions-for-readable-git-log/)
- [10 useful Git commands you wish existed – and their alternatives](https://datree.io/blog/useful-git-commands-list/)
- [github.blog: How to undo (almost) anything with Git](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/)
- [dev.to: Git Explained - The Basics](https://dev.to/milu_franz/git-explained-the-basics-igc)
- [medium: 7 Best Courses to Master Git and Github for Programmers](https://medium.com/javarevisited/7-best-courses-to-master-git-and-github-for-programmers-d671859a68b2) These are the best courses to learn Git from scratch and also advanced concepts like branching and merging. It also includes a free course to learn git.
- [medium: Top 7 Cloud Source Code Management Tools Features and Pricing Plans](https://medium.com/@atif.ramzan89/top-7-cloud-source-code-management-tools-features-and-pricing-plans-105f4eb88a3a)
- [towardsdatascience.com: The 6 Git Commands Data Scientist Should Know](https://towardsdatascience.com/the-only-6-git-commands-you-need-to-know-995065db1ae0) An introduction to using Git for machine learning projects.
- [dev.to: Git Concepts I Wish I Knew Years Ago 🌟](https://dev.to/g_abud/advanced-git-reference-1o9j)
- [opensource.com: 6 best practices for managing Git repos](https://opensource.com/article/20/7/git-repos-best-practices) Resist the urge to add things in Git that will make it harder to manage; here's what to do instead.
- [codeburst.io: Debug your code using git bisect](https://codeburst.io/debug-your-code-using-git-bisect-45db2983cc69)
- [github.blog: Highlights from Git 2.28](https://github.blog/2020-07-27-highlights-from-git-2-28/)
- [codeburst.io: A Resource for all Things Git](https://codeburst.io/a-resource-for-all-things-git-b63d6626beca)
- [Things You Want to Do in Git and How to Do Them](https://stu2b50.dev/posts/things-you-wante9665)
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
- [dzone: GitOps: How to Ops Your Git the Right Way 🌟](https://dzone.com/articles/gitops-how-to-ops-your-git-the-right-way) In this article we’ll look into the specifics of creating Git repositories structures  —  the very core of the GitOps approach.
- [honeybadger.io: Top Ten Git Tips & Tricks](https://www.honeybadger.io/blog/git-tricks/)
- [blog.balasundar.com: Automate Git Operations Using Python](https://blog.balasundar.com/automate-git-operations-using-python) Automate your git operations using GitPython.
- [cloudbees.com: Git Commands: The 13 You Must Know, In Order 🌟](https://www.cloudbees.com/blog/13-git-commands-to-know-in-order)
- [levelup.gitconnected.com: 5 Git Commands to Know Before Your First Tech Job or Internship](https://levelup.gitconnected.com/5-git-commands-to-know-before-your-first-tech-job-or-internship-1b5856313338)
- [dev.to: Master Git in 7 minutes 🌟](https://dev.to/valeriavg/master-git-in-7-minutes-gai)
- [blog.greenroots.info: How NOT to use Git in Practice. Ten Git usages, you should know to avoid](https://blog.greenroots.info/how-not-to-use-git-in-practice-ten-git-usages-you-should-know-to-avoid)
- [integratn.io: My Git Worktree Workflow](https://integratn.io/posts/my-git-worktree-workflow/)
- [livecodestream.dev: Five Advanced Git Concepts that Make You Look Like a Pro](https://livecodestream.dev/post/five-advanced-git-concepts-that-make-you-look-like-a-pro/) Learn how to master GIT with these 5 advanced concepts
- [cloudbees.com: Git Pull: How It Works With Detailed Examples](https://www.cloudbees.com/blog/git-pull-how-it-works-with-detailed-examples)
- [midu.dev: Buenas prácticas para escribir commits en Git](https://midu.dev/buenas-practicas-escribir-commits-git/)
- [cloudbees.com: Git Push: An In-Depth Tutorial With Examples](https://www.cloudbees.com/blog/git-push-an-in-depth-tutorial-with-examples)
- [blog.annamcdougall.com: Git Workflow Tutorial: Start Using Git TODAY with Basic Git Commands](https://blog.annamcdougall.com/git-workflow-tutorial-start-using-git-today-with-basic-git-commands-ckdc1nvfs02zp66s1d4zydz47)
- [thenewstack.io: Git for Managing Small Projects 🌟](https://thenewstack.io/git-for-managing-small-projects/)
- [netflixtechblog.medium.com: Improving Pull Request Confidence for the Netflix TV App](https://netflixtechblog.medium.com/improving-pull-request-confidence-for-the-netflix-tv-app-b85edb05eb65)
- [cloudsavvyit.com: How to Use Git Hooks For Commit Automation 🌟](https://www.cloudsavvyit.com/14036/how-to-use-git-hooks-for-commit-automation/)
- [simplilearn.com: How to Resolve Merge Conflicts in Git?](https://www.simplilearn.com/tutorials/git-tutorial/merge-conflicts-in-git)
- [towardsdatascience.com: How to Learn Git in Simple Words](https://towardsdatascience.com/how-to-learn-git-in-simple-words-263618071dd8) A playbook for protecting your job position as a data scientist
- [blog.argoproj.io: 5 new Git commands and 1 tip you’ll use every day](https://blog.argoproj.io/5-new-git-commands-and-1-tip-youll-use-every-day-3c28e97c9321)
- [dev.to: Open Source: My first Pull Request](https://dev.to/okimotomizuho/open-source-my-first-pull-request-1356)
- [blog.testproject.io: Git 101 From Scratch: The Ultimate Guide for QAs 🌟](https://blog.testproject.io/2021/09/23/git-101-from-scratch-the-ultimate-guide-for-qas)
- [==freecodecamp.org: Git for Professionals – Free Version Control Course== 🌟](https://www.freecodecamp.org/news/git-for-professionals/)
- [towardsdatascience.com: A Git cheatsheet that all coders need](https://towardsdatascience.com/a-git-cheatsheet-that-all-coders-need-bf8ad4d91576) Ever accidentally deleted files or necessary code? Or do you wish to look back at an older version of your code?
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
- [dev.to: How to become a Git expert! 🌟](https://dev.to/sagarbarapatre/how-to-become-a-git-expert-1jl2)
- [c-sharpcorner.com: Top 15 Git Commands With Examples For Every Developers💪](https://www.c-sharpcorner.com/article/top-15-git-commands-with-examples-for-every-developers/)
- [==cloudsavvyit.com: Should You Use HTTPS or SSH For Git?== 🌟](https://www.cloudsavvyit.com/14822/should-you-use-https-or-ssh-for-git/)
- [==marklodato.github.io: A Visual Git Reference== 🌟](https://marklodato.github.io/visual-git-guide/index-en.html)
- [dev.to: Get lazy with lazygit](https://dev.to/tahsinature/get-lazy-with-lazygit-4h37)
- [levelup.gitconnected.com: Top 30 Git Commands You Should Know To Master Git CLI](https://levelup.gitconnected.com/top-30-git-commands-you-should-know-to-master-git-cli-f04e041779bc) Learn the most essential Git commands to boost your productivity, and become a master in managing the GitHub repositories.
- [medium: Forking GitHub Repository with Git and VIM | Swain Dennis](https://medium.com/@swain.dennis1/forking-github-repository-with-git-and-vim-54288dff3801)
- [==dev.to: 10 useful Git tips to improve your workflow== 🌟](https://dev.to/yenyih/10-useful-git-tips-to-improve-your-workflow-kf1)
- [dev.to: Git Organized: A Better Git Flow](https://dev.to/render/git-organized-a-better-git-flow-56go)
- [betterprogramming.pub: How to Filter the Git Logs](https://betterprogramming.pub/how-to-filter-the-git-logs-2dcebf3d12) Practical examples of how you can filter the Git logs
- [thenewstack.io: Development: Introduction to Git Logging](https://thenewstack.io/development-introduction-to-git-logging/)
- [freecodecamp.org: git config – How to Configure Git Settings to Improve Your Development Workflow](https://www.freecodecamp.org/news/git-config-how-to-configure-git-settings/)
- [freecodecamp.org: Git Undo Merge – How to Revert the Last Merge Commit in Git](https://www.freecodecamp.org/news/git-undo-merge-how-to-revert-the-last-merge-commit-in-git/)
- [devconnected.com: How To Delete File on Git](https://devconnected.com/how-to-delete-file-on-git/)
- [infoworld.com: What is Git? Version control for collaborative programming](https://www.infoworld.com/article/3654955/what-is-git-version-control-for-collaborative-programming.html)
- [==dev.to: How Do I Resolve Merge Conflicts?==](https://dev.to/github/how-do-i-resolve-merge-conflicts-5438)
    - [==dev.to: How to Undo Pushed Commits with Git==](https://dev.to/github/how-to-undo-pushed-commits-with-git-2pe6)
- [opensource.com: My guide to using the Git push command safely](https://opensource.com/article/22/4/git-push) Understand the usage and impact of this popular Git command on your project, learn new safer alternatives, and grasp the skills of restoring a broken branch.
- [opensource.com: Make your own Git subcommands](https://opensource.com/article/22/4/customize-git-subcommands) Creating your own Git subcommand makes your custom scripts feel like natural components of Git.
- [betterprogramming.pub: 2 Use Cases of Python Pre-commit Hooks to Tidy Up Your Git Repositories](https://betterprogramming.pub/2-use-cases-of-python-pre-commit-hooks-to-tidy-up-your-git-repositories-8d86c9c4f06b) Strategies to have a better-organized codebase
- [==betterprogramming.pub: Recovering From Common Git Errors==](https://betterprogramming.pub/recovering-from-common-git-errors-eccda7ec6180)
- [github.blog: Improve Git monorepo performance with a file system monitor 🌟](https://github.blog/2022-06-29-improve-git-monorepo-performance-with-a-file-system-monitor/) **Monorepo performance can suffer due to the sheer number of files in your working directory. Git’s new builtin file system monitor makes it easy to speed up monorepo performance.**
- [java67.com: Top 10 Free Git Courses and Tutorials for Beginners in 2022 - Best of Lot](https://www.java67.com/2022/07/10-best-free-git-courses-and-tutorials.html)
- [==medium.com/@ladoui.bilal: 10 Git commands every DevOps should know== 🌟](https://medium.com/@ladoui.bilal/10-git-commands-should-every-devops-should-know-6ae07f5e1989)
- [polarsquad.com: Stop doing pull requests](https://polarsquad.com/blog/stop-doing-pull-requests)
- [medium.com/@datosh18: Gitsign in remote environments](https://medium.com/@datosh18/gitsign-in-remote-environments-6f40f47d289f)
- [medium.com/qe-unit: How Google Does Monorepo (Revisited)](https://medium.com/qe-unit/how-google-does-monorepo-revisited-8c793be20344)
- [dev.to: How atomic Git commits dramatically increased my productivity - and will increase yours too 🌟](https://dev.to/samuelfaure/how-atomic-git-commits-dramatically-increased-my-productivity-and-will-increase-yours-too-4a84)
- [==dev.to: Git fundamentals, a complete guide | Leandro Proença== 🌟🌟](https://dev.to/leandronsp/git-fundamentals-a-complete-guide-do7)
- [freecodecamp.org: Undo Git Add – How to Remove Added Files in Git 🌟](https://www.freecodecamp.org/news/undo-git-add-how-to-remove-added-files-in-git/)
- [==realpython.com: Advanced Git Tips for Python Developers== 🌟](https://realpython.com/advanced-git-for-pythonistas/)
- [cloud-and-devops.hashnode.dev: Git 007 : Learn Advanced GIT topics like a Pro](https://cloud-and-devops.hashnode.dev/git-007-learn-advanced-git-topics-like-a-pro)
- [build5nines.com: Git: Reset / Undo Most Recent Local Commit](https://build5nines.com/git-reset-undo-most-recent-local-commit/)
- [freecodecamp.org: How to Write Commit Messages that Project Maintainers Will Appreciate](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/)
- [==learn.gitkraken.com/courses/git-foundations: Foundations of Git - Certification Course | Enroll for free==](https://learn.gitkraken.com/courses/git-foundations)
- [build5nines.com: How to Determine URL a Local Git Repository was Originally Cloned From](https://build5nines.com/how-to-determine-url-a-local-git-repository-was-originally-cloned-from/)

## Git Releases

- [github.blog: Highlights from Git 2.40](https://github.blog/2023-03-13-highlights-from-git-2-40/) The first Git release of the year is here! Take a look at some of our highlights on what's new in Git 2.40.

## Git stash

- [opensource.com: A practical guide to using the git stash command](https://opensource.com/article/21/4/git-stash) Learn how to use the git stash command and when you should use it.
- [medium.com/featurepreneur: Don’t trash your changes but stash ‘em!](https://medium.com/featurepreneur/dont-trash-your-changes-but-stash-em-2091a191f7db)
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
- [cloudsavvyit.com: How to Delete Git Branches on Local and Remote Repositories](https://www.cloudsavvyit.com/14289/how-to-delete-git-branches-on-local-and-remote-repositories/)
- [dev.to: Open Source: Multiple branches and git merges](https://dev.to/okimotomizuho/open-source-multiple-branches-and-git-merges-2f69)
- [cloudsavvyit.com: How to Move Changes to Another Branch in Git](https://www.cloudsavvyit.com/14710/how-to-move-changes-to-another-branch-in-git/)
- [css-tricks.com: Git: Switching Unstaged Changes to a New Branch](https://css-tricks.com/git-switching-unstaged-changes-to-a-new-branch/)
- [betterprogramming.pub: Leave Aside Git Checkout. Consider Git Switch for a Change](https://betterprogramming.pub/leave-aside-git-checkout-consider-git-switch-for-a-change-7849df8714b0) Switch between branches without checking out
- [freecodecamp.org: Git List Branches – How to Show All Remote and Local Branch Names](https://www.freecodecamp.org/news/git-list-branches-how-to-show-all-remote-and-local-branch-names/)
- [opensource.com: Explaining Git branches with a LEGO analogy](https://opensource.com/article/22/4/git-branches)
- [blog.devops.dev: Stop messing up with Git. Follow this simple and effective strategy to maintain Git branches](https://blog.devops.dev/stop-messing-up-with-git-follow-this-simple-and-effective-strategy-to-maintain-git-branches-cc378468cde6)
- [medium.com/@selvamraju007: GIT Branching Strategies](https://medium.com/@selvamraju007/git-branching-strategies-a6eafe4541ae)
- [dev.to/varbsan: A Simplified Convention for Naming Branches and Commits in Git](https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4)
- [medium.com/@amid.ukr: Agile Git branching strategies in 2023](https://medium.com/@amid.ukr/agile-git-branching-strategies-in-2023-caeead79ddd)

## Git Merge

- [freecodecamp.org: The Git Merge Handbook – Definitive Guide to Merging in Git](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/)
- [freecodecamp.org: How to Fix Merge Conflicts in Git](https://www.freecodecamp.org/news/how-to-fix-merge-conflicts-in-git/)

## Merge Repositories

- [build5nines.com: Git: Merge Repositories with History](https://build5nines.com/git-merge-repositories-with-history/)

## Git Aliases

- [opensource.com: 8 Git aliases that make me more efficient](https://opensource.com/article/20/11/git-aliases) Use aliases to create shortcuts for your most-used or complex Git commands.
- [davidwalsh.name: More Awesome Git Aliases](https://davidwalsh.name/more-awesome-git-aliases)
- [blog.mimacom.com: The Git Commands You Wish You Always Had](https://blog.mimacom.com/git-aliases-you-wished-you-had/)

## Git Rebase

- [dev.to: ELI5: Git Rebase vs. Merge 🌟](https://dev.to/karaluton/explain-like-i-m-five-git-rebase-vs-merging-1k69)
- [==opensource.com: My guide to understanding Git rebase -i==](https://opensource.com/article/22/4/manage-git-commits-rebase-i-command) The git rebase command is one of the most powerful in Git. It can rewrite your repository's commit history by rearranging, modifying, and even deleting commits.
- [freecodecamp.org/news/git-rebase-handbook](https://www.freecodecamp.org/news/git-rebase-handbook/)

## Git and GitHub Backup

- [backhub.co](https://www.backhub.co/) Reliable GitHub repository backup, set up in minutes
- [devops.com: Make GitHub Backups Part of Your Development Process](https://devops.com/make-github-backups-part-of-your-development-process/)
- [dzone.com: Git Clone Command vs. GitHub Backup - Best Practices](https://dzone.com/articles/git-clone-command-vs-github-backup-best-practices) Git clone command vs. GitHub backup - what you should know to keep your git repositories and metadata safe and sound. Check in-depth analysis.
- [dev.to: 3 Ways to Backup Your Code (Even If You Don’t Know Git)](https://dev.to/github/3-ways-to-backup-your-code-even-if-you-dont-know-git-1o5l)

## Cherry-picking

- [opensource.com: 3 reasons I use the Git cherry-pick command](https://opensource.com/article/21/3/git-cherry-pick) Cherry-picking solves a lot of problems in Git repositories. Here are three ways to fix your mistakes with git cherry-pick.
- [jmfloreszazo.com: GIT Mejores prácticas: CHERRY-PICKING](https://jmfloreszazo.com/git-mejores-practicas-cherry-picking/)

## Git Submodules

- [git-scm.com: Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) It often happens that while working on one project, you need to use another project from within it. Perhaps it’s a library that a third party developed or that you’re developing separately and using in multiple parent projects. A common issue arises in these scenarios: you want to be able to treat the two projects as separate yet still be able to use one from within the other.
- [sitepoint.com: Understanding and Working with Submodules in Git](https://www.sitepoint.com/git-submodules-introduction/)

## Shields

- [shields.io 🌟](https://shields.io/)

## Design By Contract

[Wikipedia: Design by contract (DbC)](https://en.wikipedia.org/wiki/Design_by_contract), also known as contract programming, programming by contract and design-by-contract programming, is an approach for designing software.

It prescribes that software designers should define formal, precise and verifiable interface specifications for software components, which extend the ordinary definition of abstract data types with preconditions, postconditions and invariants. These specifications are referred to as "contracts", in accordance with a conceptual metaphor with the conditions and obligations of business contracts.

## Git Cheat Sheets

- [Git and GitHub Cheat Sheets](cheatsheets.md)

## Monorepo VS Polyrepo

- [fourtheorem.com: How to end Microservice pain and embrace the Monorepo](https://www.fourtheorem.com/blog/monorepo)
- [medium: The Pros and Cons of Monorepos, Explained](https://betterprogramming.pub/the-pros-and-cons-monorepos-explained-f86c998392e1) Should you keep all of your code in a single directory?

## Patterns for Managing Source Code Branches (Branching Models/Workflows)

- [paulhammant.com: What is Your Branching Model?:](https://paulhammant.com/2013/12/04/what_is_your_branching_model/) Mainline, Cascade, Trunk-Based Development, Short Lived Feature Branches, Continuous Deployment, Subversion noise on branching, etc.
- [adevait.com: Creating a Branching Strategy for Small Teams](https://adevait.com/software/creating-branching-strategy)
- [atlassian.com: Configuring branching models 🌟](https://confluence.atlassian.com/bitbucketserver/using-branches-in-bitbucket-server-776639968.html#UsingbranchesinBitbucketServer-model)
- [git-scm.com: Git Branching - Branching Workflows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [git-scm.com: Distributed Git - Distributed Workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
    - [Distributed Git - Distributed Workflows - Integration-Manager Workflow](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow)
    - [Setup Git Integration Manager Workflow in Eclipse](https://stackoverflow.com/questions/26003298/how-to-setup-local-git-with-local-blessed-repo-integration-manager-workflow)
- [Dzone refcard: Git Patterns and Anti-Patterns](https://dzone.com/refcardz/git-patterns-and-anti-patterns) Scaling from Workgroup to Enterprise. Suggests patterns and anti-patterns, including Hybrid SCM, Git champions, blessed repository, per-feature topic branches, and ALM integration.
- [Dzone: Basic Git Branching](https://dzone.com/articles/basic-git-branching) In this article, we walk through the basics of branching with Git to get you started with better managing your versioning during projects.
- [martinfowler.com: Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html)
    - [Release Branch Pattern:](https://martinfowler.com/articles/branching-patterns.html#release-branch) A branch that only accepts commits accepted to stabilize a version of the product ready for release.
- [medium: Which Git branching model should I select for my project?](https://medium.com/aventude/which-git-branching-model-should-i-select-73aafc503b5f)
- [speakerdeck.com: 10 Git Anti Patterns You Should be Aware of 🌟](https://speakerdeck.com/lemiorhan/10-git-anti-patterns-you-should-be-aware-of)
- [Dzone: Git Branch Naming Conventions](https://dzone.com/articles/git-branch-naming-conventions-1) A primer on naming branches for modern git workflows.
- [gitkraken.com: Branching in Git 🌟](https://www.gitkraken.com/learn/git/branch)
- [jmfloreszazo.com: Flujos de trabajo de git](https://jmfloreszazo.com/flujos-de-trabajo-de-git/)
- [towardsdatascience.com: How To Structure Your Git Branching Strategy — By A Data Engineer](https://towardsdatascience.com/how-to-structure-your-git-branching-strategy-by-a-data-engineer-45ff96857bb) Data pipelines require version control too!

??? note "Slide: 10 git anti patterns. Click to expand!"

    <center>
    <script async class="speakerdeck-embed" data-id="1eaed7dabacb4f9b9c96b08de38eb9e1" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
    </center>

### Git Workflows

- ```git help workflows```
- [atlassian.com: Comparing Workflows 🌟](https://www.atlassian.com/git/tutorials/comparing-workflows)
- [GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Git DMZ Flow](https://gist.github.com/djspiewak/9f2f91085607a4859a66)
- [kubernetes.dev: GitHub Workflow](https://www.kubernetes.dev/docs/guide/github-workflow/) An overview of the GitHub workflow used by the Kubernetes project. It includes some tips and suggestions on things such as keeping your local environment in sync with upstream and commit hygiene.

### Trunk Based Development

- [Trunk Based Development](https://trunkbaseddevelopment.com/)
- [paulhammant.com: What is Trunk-Based Development?](https://paulhammant.com/2013/04/05/what-is-trunk-based-development/)
- [The Origins of Trunk Based Development](https://dzone.com/articles/origins-trunk-based)
- [quora.com: What is trunk based development?](https://www.quora.com/What-is-trunk-based-development)
- [kean.github.io: Trunk-Based Development](https://kean.github.io/post/trunk-based-development)
- [paulhammant.com: Microsoft's Trunk-Based Development](https://paulhammant.com/2014/04/03/microsofts-trunk-based-development/)
- [devblogs.microsoft.com: Release Flow: How We Do Branching on the VSTS Team](https://devblogs.microsoft.com/devops/release-flow-how-we-do-branching-on-the-vsts-team/)

### Feature Branch Development (aka GitFlow)

- [nvie.com: Feature Branches. A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)

#### Git Flow

- One of the main concepts of **GitFlow** is **feature branches**. The idea is that each feature should be developed in its own branch. When the feature is done, it gets merged into develop branch.
- [devopszone.info: An Introduction To Git-flow Workflow](https://www.devopszone.info/post/an-introduction-to-git-flow-workflow)
- [atlassian.com: Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [gitkraken.com: GitFlow](https://support.gitkraken.com/git-workflows-and-extensions/git-flow/) is a list of rules to keep a repo’s history organized, and is used to make the release process, bug fixes, and feature creation easier.
- [git-flow.readthedocs.io](https://git-flow.readthedocs.io/)
- [medium.com: Gitflow — Branch Guide](https://medium.com/@rafavinnce/gitflow-branch-guide-8a523360c053)
- [medium.com: Git Flow for Beginners](https://medium.com/@thibault60000/git-flow-for-beginners-d7a152b2c1f9)
- [medium.com: What is GitFlow?](https://medium.com/@okandavut/what-is-gitflow-c0be7a659992)
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

- [toptal.com: Trunk-based Development vs. Git Flow](https://www.toptal.com/software/trunk-based-development-git-flow)
- [victorops.com: Source Code Control: Trunk-Based Development vs. GitFlow](https://victorops.com/blog/source-code-control-trunk-based-development-vs-gitflow)
- [medium: GitFlow VS Trunk-Based-Development](https://medium.com/@vafrcor2009/gitflow-vs-trunk-based-development-3beff578030b)
- [Dzone: Why I Prefer Trunk-Based Development Over Feature Branching and GitFlow 🌟](https://dzone.com/articles/why-i-prefer-trunk-based-development-over-feature) Check out the components of Trunk-based Development as implemented by Facebook and Google, and see how it helps resolve and prevent merge conflicts.
- [team-coder.com: From Git Flow to Trunk Based Development](https://team-coder.com/from-git-flow-to-trunk-based-development/)
- [stridenyc.com/podcasts: Trunk Based Development vs Gitflow](https://www.stridenyc.com/podcasts/30-trunk-based-development-vs-gitflow)
- [freecodecamp.org: What is Trunk Based Development? A Different Approach to the Software Development Lifecycle](https://www.freecodecamp.org/news/what-is-trunk-based-development)

### Alternative Branching Models

- [trunkbaseddevelopment.com: Alternative Branching Models](https://trunkbaseddevelopment.com/alternative-branching-models/)

#### Feature Flags (Feature Toggles)

- [featureflags.io: Flags vs Branching](https://featureflags.io/feature-flags-vs-branching/) Branch better with feature flag driven development.
- [martinfowler.com: Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html)
- [#FeatureFlags](https://twitter.com/hashtag/featureflag)
- [CloudBees Releases Another Industry First: Feature Flagging for On-Premise Use 🌟](https://www.previous.cloudbees.com/press/cloudbees-releases-another-industry-first-feature-flagging-premise-use)
- [cioperu.pe: 5 formas de impulsar la utilización de feature flags](https://cioperu.pe/articulo/30477/devops-5-formas-de-impulsar-la-utilizacion-de-feature-flags/)
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
- [Dzone: source control using atlassian bitbucket](https://dzone.com/articles/source-control-using-atlassian-bitbucket)
- [Dzone: how I use bitbucket in my regular routine](https://dzone.com/articles/how-i-use-bitbucket-in-my-regular-routine)

## GitLab

- [gitlab.com](https://gitlab.com/)
- [Dzone: using gitlab API to create projects](https://dzone.com/articles/using-gitlab-rest-api-to-create-projects)
- [gitlab.com: GitLab’s guide to CI/CD for beginners](https://about.gitlab.com/blog/2020/07/06/beginner-guide-ci-cd/) CI/CD is a key part of the DevOps journey. Here’s everything you need to understand about this game-changing process.
- [levelup.gitconnected.com: Automating Integration and Deployment to Remote Server](https://levelup.gitconnected.com/automating-integration-and-deployment-to-remote-server-63a2b6576ebf) GitLab CI/CD
- [about.gitlab.com: Want a more effective CI/CD pipeline? Try our pro tips](https://about.gitlab.com/blog/2020/07/29/effective-ci-cd-pipelines/) Here’s how to take your CI/CD pipeline to the next level with hands on advice about faster builds, better security and more.
- [gitlab.com: How to do GitLab merge request reviews in VS Code](https://about.gitlab.com/blog/2021/01/25/mr-reviews-with-vs-code/)
- [about.gitlab.com: How we used parallel CI/CD jobs to increase our productivity](https://about.gitlab.com/blog/2021/01/20/using-run-parallel-jobs/) GitLab uses parallel jobs to help long-running jobs run faster.
- [about.gitlab.com: How to use GitLab CI to deploy to multiple environments](https://about.gitlab.com/blog/2021/02/05/ci-deployment-and-environments/)
- [about.gitlab.com: Meet Pipeline Editor, your one-stop-shop for building a CI/CD pipeline](https://about.gitlab.com/blog/2021/02/22/pipeline-editor-overview/)
- [about.gitlab.com: A new era of Kubernetes integrations on GitLab.com](https://about.gitlab.com/blog/2021/02/22/gitlab-kubernetes-agent-on-gitlab-com/) The GitLab Kubernetes Agent enables secure deployments from GitLab SaaS to your Kubernetes cluster and provides deep integrations of your cluster to GitLab.
- [docs.gitlab.com: Install GitLab Runner on Red Hat OpenShift](https://docs.gitlab.com/runner/install/openshift.html)
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
- [==redpill-solutions.medium.com: Deploying to Kubernetes with GitLab==](https://redpill-solutions.medium.com/deploying-to-kubernetes-with-gitlab-28c2f1a42e57)
- [==venturebeat.com: GitLab acquires open source observability distribution Opstrace==](https://venturebeat.com/2021/12/14/gitlab-acquires-open-source-observability-distribution-opstrace/)
- [==medium: Kubernetes & Gitlab-CI — Simplified app deployment automation==](https://medium.com/@david.alvares.62/kubernetes-gitlab-ci-simplified-app-deployment-automation-84ad182a59db) In 5 minutes, I explain how to put in an automated GitLab pipeline to deploy your application to Kubernets with Helm.
- [about.gitlab.com: GitLab Chart works towards Kubernetes 1.22](https://about.gitlab.com/blog/2021/12/17/gitlab-chart-works-towards-kubernetes-1-22/)
- [Deploy and Manage Gitlab Runners on Amazon EC2](https://aws.amazon.com/blogs/devops/deploy-and-manage-gitlab-runners-on-amazon-ec2/)
- [freecodecamp.org: DevOps with GitLab CI Course 🌟](https://www.freecodecamp.org/news/devops-with-gitlab-ci-course/)
- [testmo.com: GitLab CI/CD Test Automation Pipeline & Reporting](https://www.testmo.com/guides/gitlab-ci-test-automation)
- [community.ops.io: CI CD 101 with GitLab](https://community.ops.io/jatin/ci-cd-101-with-gitlab-4pol)
- [about.gitlab.com: Simple Kubernetes management with GitLab](https://about.gitlab.com/blog/2022/11/15/simple-kubernetes-management-with-gitlab/)
- [itnext.io: Managing multiple Kubernetes clusters using Git 🌟](https://itnext.io/managing-multiple-kubernetes-clusters-using-git-cd068bbd85ac) Managing multi-cloud Kubernetes clusters in a central location using GitLab
- [renjithvr11.medium.com: Running GitLab Runners on Kubernetes](https://renjithvr11.medium.com/running-gitlab-runners-on-kubernetes-8e7fc9bf75ce)

### GitLab Collective

- [GitLab Collective 🌟](https://stackoverflow.com/collectives/gitlab) Discover and share knowledge about version control, CI/CD, DevSecOps, and all-remote workflows
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
- [GitHub Chaos Actions in Your CI/CD workflow](https://blog.mayadata.io/github-chaos-actions-in-your-ci/cd-workflow-part-1)
- [GitHub's OpenAPI Spec Open-Sourced in Beta](https://www.infoq.com/news/2020/08/GitHub-open-api-spec/)
- [Things you didn't know you could diff in GitHub](https://sebastiandedeyne.com/things-you-didnt-know-you-could-diff-in-github/)
- [github.blog: Set the default branch for newly-created repositories](https://github.blog/changelog/2020-08-26-set-the-default-branch-for-newly-created-repositories/)
- [grafana.com: How we use the Grafana GitHub plugin to track outstanding pull requests](https://grafana.com/blog/2020/09/21/how-we-use-the-grafana-github-plugin-to-track-outstanding-pull-requests/)
- [itnext.io: Build & Ship: GitHub Container Registry & Kubernetes](https://itnext.io/build-ship-github-container-registry-kubernetes-aa06029b3f21)
- [grafana: How we use the Grafana GitHub plugin to track outstanding pull requests](https://grafana.com/blog/2020/09/21/how-we-use-the-grafana-github-plugin-to-track-outstanding-pull-requests/)
- [itnext.io: Build & Ship: GitHub Container Registry & Kubernetes](https://itnext.io/build-ship-github-container-registry-kubernetes-aa06029b3f21)
- [theregister.com: Passwords begone: GitHub will ban them next year for authenticating Git operations](https://www.theregister.com/2020/12/17/github_bans_passwords/)
- [github.blog: Learn about ghapi, a new third-party Python client for the GitHub API](https://github.blog/2020-12-18-learn-about-ghapi-a-new-third-party-python-client-for-the-github-api/)
- [github.blog: Improving how we deploy GitHub](https://github.blog/2021-01-25-improving-how-we-deploy-github/)
- [github.blog: Deployment reliability at GitHub](https://github.blog/2021-02-03-deployment-reliability-at-github/)
- [github.blog: Extending GitOps to reliability-as-code with GitHub and StackPulse](https://github.blog/2021-02-04-extending-gitops-to-reliability-as-code-with-github-and-stackpulse/)
- [GitHub public roadmap 🌟](https://github.com/github/roadmap)
- [github.blog: Solving the innersource discovery problem - Discoverability](https://github.blog/2021-03-23-solving-the-innersource-discovery-problem/)
- [devopstips.net: Create, Host and Share Docker Images with GitHub Packages](https://devopstips.net/create-host-and-share-docker-images-with-github-packages)
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
- [returngis.net: Migrar un repositorio de un BitBucket Server local a GitHub](https://www.returngis.net/2021/11/migrar-un-repositorio-de-un-bitbucket-server-local-a-github/)
- [freecodecamp.org: Git and GitHub Tutorial – Version Control for Beginners 🌟](https://www.freecodecamp.org/news/git-and-github-for-beginners)
- [github/hub 🌟](https://github.com/github/hub) A command-line tool that makes git easier to use with GitHub.
- [cloudsavvyit.com: How To Properly Fork a Github Repository](https://www.cloudsavvyit.com/14640/how-to-properly-fork-a-github-repository)
- [==dev.to: New GitHub Rules Guide [git push -u origin main]==](https://dev.to/bekbrace/new-rules-in-github-git-push-u-origin-main-2k82) This post explains very quickly how to push your code to your GitHub repository following the new rules imposed by GitHub.
- [==dev.to: Learn how to use Git and GitHub in a team like a pro==](https://dev.to/colocodes/learn-how-to-use-git-and-github-in-a-team-like-a-pro-2dk7)
    - [==dev.to: Learn how to use Git and GitHub in a team like a pro (part 2)==](https://dev.to/colocodes/learn-how-to-use-git-and-github-in-a-team-like-a-pro-part-2-11j)
- [==dev.to: Git and GitHub for beginners==](https://dev.to/ericawanja/git-and-github-for-beginners-33a0)
- [==adamtheautomator.com: How to Manage GitHub Actions Environment Variables and Secrets==](https://adamtheautomator.com/github-actions-environment-variables/)
- [dev.to: Introduction to Git and GitHub](https://dev.to/estherwanjiru/introduction-to-git-and-github-25ei)
- [github.blog: Improving GitHub code search](https://github.blog/2021-12-08-improving-github-code-search/)
- [towardsdatascience.com: Git and GitHub basics for Data Scientists](https://towardsdatascience.com/git-and-github-basics-for-data-scientists-b9fd96f8a02a) UCL Data Science Workshop 8: What is Git, Creating a local repository, Committing your first files, Linking to a remote repository
- [github.blog: Lists are now available as a public beta](https://github.blog/changelog/2021-12-09-lists-are-now-available-as-a-public-beta/) Lists level up the starring experience by making it easy to organize and curate your favorite repositories on GitHub. You can create public lists that appear on your stars page at https://github.com/USERNAME?tab=stars.
- [freecodecamp.org: How to Use the .github Repository](https://www.freecodecamp.org/news/how-to-use-the-dot-github-repository/)
- [==about.gitlab.com: How to install and use the GitLab Kubernetes Operator (on OCP)==](https://about.gitlab.com/blog/2021/11/16/gko-on-ocp)
- [alsmola.medium.com: Securing GitHub organizations](https://alsmola.medium.com/securing-github-organizations-9c33c850638)
- [github.blog: Dependency graph now supports GitHub Actions](https://github.blog/2022-01-31-dependency-graph-now-supports-github-actions/) The dependency graph helps developers and maintainers understand the code they depend on, and now includes GitHub Actions!
- [==github.blog: How to build a CI/CD pipeline with GitHub Actions in four simple steps==](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/) A quick guide on the advantages of using GitHub Actions as your preferred CI/CD tool—and how to build a CI/CD pipeline with it.
- [cloudsavvyit.com: How to Use Github Actions to Automate Your Repository Builds](https://www.cloudsavvyit.com/15207/how-to-use-github-actions-to-automate-your-repository-builds/)
- [github.blog: How to start using reusable workflows with GitHub Actions](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/) Reusable workflows offer a simple and powerful way to avoid copying and pasting workflows across your repositories.
- [github.blog: Getting started with project planning on GitHub](https://github.blog/2022-02-11-getting-started-with-project-planning-on-github/) Stop context switching. Keep your team’s project planning next to your code.
- [freecodecamp.org: How to Fork a GitHub Repository – A Complete Workflow](https://www.freecodecamp.org/news/how-to-fork-a-github-repository/)
- [==levelup.gitconnected.com: GitHub may replace DockerHub==](https://levelup.gitconnected.com/github-may-replace-dockerhub-a5da5e547f01)
- [==github.com/Lightning-AI/engineering-class: Lightning Bits: Engineering for Researchers== 🌟](https://github.com/Lightning-AI/engineering-class) **This repository contains additional materials and show notes for the Lightning Bits: Engineering for Researchers video series.**
    - [github.com/Lightning-AI/engineering-class: Episode 8: Creating a Pull Request on GitHub](https://github.com/Lightning-AI/engineering-class/blob/main/ep08-github-pr/Ep08-ShowNotes.md)
    - [github.com/Lightning-AI/engineering-class: Episode 9: Collaborating with Pull Requests using GitHub](https://github.com/Lightning-AI/engineering-class/blob/main/ep09-github-collab/Ep09-ShowNotes.md#syncing-forks-with-upstream)
- [github.com/marketplace: Use AWS Secrets Manager secrets in GitHub jobs 🌟](https://github.com/marketplace/actions/aws-secrets-manager-github-action)
- [tylercipriani.com: GitHub's Missing Merge Option](https://tylercipriani.com/blog/2022/09/30/githubs-missing-merge-option/)
- [==steampipe.io: Top 3 ways to improve GitHub org security==](https://steampipe.io/blog/github-security-tips) Gain some practical tips for securing your GitHub organizations based on findings from common security incidents.
- [dev.to/opensauced: How to Create a Good Pull Request Template (and Why You Should Add Gifs)](https://dev.to/opensauced/how-to-create-a-good-pull-request-template-and-why-you-should-add-gifs-4i0l)
- [==youtube: GitHub Masterclass (Spanish)== 🌟](https://www.youtube.com/playlist?list=PL0pgb_7nDofA1hJpkpPf4qHQTYZbPVT5M)
- [freecodecamp.org: How to Build a GitHub Template Repository for Scaffolding with React, Vite, and TailwindCSS](https://www.freecodecamp.org/news/create-a-github-template-repository-with-react-vite-and-tailwindcss/)
- [alemsbaja.hashnode.dev: Git and GitHub Demystified : A Comprehensive Guide for Version Control System](https://alemsbaja.hashnode.dev/git-and-github-demystified-a-comprehensive-guide-for-version-control-system) A Comprehensive Guide to Mastering Git Version Control System and GitHub with example
- [docs.github.com: Using SSH over the HTTPS port 🌟](https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port) Sometimes, firewalls refuse to allow SSH connections entirely. If using HTTPS cloning with credential caching is not an option, you can attempt to clone using an SSH connection made over the HTTPS port. Most firewall rules should allow this, but proxy servers may interfere.
- [freecodecamp.org: How to Contribute to Open-Source Projects – Git & GitHub Workflow for Beginners](https://www.freecodecamp.org/news/git-and-github-workflow-for-open-source/)
- [==mattias.engineer: Azure Federated Identity Credentials for GitHub==](https://mattias.engineer/blog/2024/azure-federated-credentials-github/)
- [freecodecamp.org: How to Create and Sync Git and GitHub Repositories](https://www.freecodecamp.org/news/create-and-sync-git-and-github-repositories/)

### Fake it til you make it

- [github.com/rakyll/fake-it-til-you-make-it](https://github.com/rakyll/fake-it-til-you-make-it) Have you come across to someone that thinks you don't deserve a job because you don't have GitHub contributions? Never worked for a company who hired based on GitHub contributions alone. If anyone is bugging you because you are not an open source developer or your company doesn't use GitHub, use fake-it-til-you-make-it to generate two years of contributions.

### GitHub Lab

- [==lab.github.com== 🌟](https://lab.github.com) With GitHub Learning Lab, grow your skills by completing fun, realistic projects. Get advice and helpful feedback from our friendly Learning Lab bot.

### GitHub Code Scanner

- https://docs.github.com/en/code-security/code-scanning
- [analyticsindiamag.com: GitHub launches code scanner to flag security vulnerabilities](https://analyticsindiamag.com/github-launches-code-scanner-to-flag-security-vulnerabilities/) The new experimental analysis can have a higher false-positive rate relative to results from standard CodeQL analysis.

### GitHub Discussions

- [github.com/giscus/giscus](https://github.com/giscus/giscus) A comments system powered by [GitHub Discussions](https://docs.github.com/en/discussions). Let visitors leave comments and reactions on your website via GitHub! Heavily inspired by [utterances](https://github.com/utterance/utterances).

### GitHub Actions

- [github.blog: Testing cloud apps with GitHub Actions and cloud-native open source tools](https://github.blog/2020-10-09-devops-cloud-testing/)
- [docker.com: Docker Github Actions](https://www.docker.com/blog/docker-github-actions/)
- [laravel-news.com: Generate GitHub Actions Config for Laravel Projects with Ghygen](https://laravel-news.com/generate-github-actions-config-for-laravel-projects-with-ghygen)
- [blog.codecentric.de: Stop re-writing pipelines! Why GitHub Actions drive the future of CI/CD](https://blog.codecentric.de/en/2021/03/github-actions-nextgen-cicd/)
- [particule.io: CI/CD using Github Actions, AWS ECR and ECS Fargate](https://particule.io/en/blog/cicd-ecr-ecs/)
- [proandroiddev.com: “Continuous Integration/Delivery” for Android with GitHub Actions — Part 1](https://proandroiddev.com/continuous-integration-delivery-for-android-with-github-actions-part-1-b232ed2b1740)
- [github.blog: Implementing least privilege for secrets in GitHub Actions](https://github.blog/2021-04-13-implementing-least-privilege-for-secrets-in-github-actions/)
- [github.blog: Work with GitHub Actions in your terminal with GitHub CLI](https://github.blog/2021-04-15-work-with-github-actions-in-your-terminal-with-github-cli/)
- [github.blog: GitHub Actions: Control permissions for GITHUB_TOKEN 🌟](https://github.blog/changelog/2021-04-20-github-actions-control-permissions-for-github_token/)
- [github.blog: GitHub Actions update: Helping maintainers combat bad actors](https://github.blog/2021-04-22-github-actions-update-helping-maintainers-combat-bad-actors/)
- [github.blog: How we use GitHub Actions to manage GitHub Docs](https://github.blog/2021-04-28-use-github-actions-manage-docs/)
- [vimeo.com: How to Create a CI/CD Pipeline with GitHub Actions and K8s Like a Boss](https://vimeo.com/552276182)
- [medium: Create CI/CD with Github Actions + AWS EC2, CodeDeploy and S3](https://medium.com/codemonday/github-actions-for-ci-cd-with-ec2-codedeploy-and-s3-e93e75bf1ce0)
- [actions-runner-controller 🌟](https://github.com/actions-runner-controller/actions-runner-controller) Kubernetes controller for GitHub Actions self-hosted runnners
- [itnext.io: GitHub Actions for Android Developers](https://itnext.io/github-actions-for-android-developers-9ae606df2bfa)
- [github.com: Branch Cleanup Action 🌟](https://github.com/jessfraz/branch-cleanup-action) A GitHub action to automatically delete the branch after a pull request has been merged.
- [blog.thundra.io: How to Set Up a CI Pipeline in GitHub Actions](https://blog.thundra.io/how-to-set-up-a-ci-pipeline-in-github-actions)
- [github.blog: GitHub Actions: Ephemeral self-hosted runners & new webhooks for auto-scaling](https://github.blog/changelog/2021-09-20-github-actions-ephemeral-self-hosted-runners-new-webhooks-for-auto-scaling/)
- [github.blog: Showing code scanning alerts on pull requests](https://github.blog/changelog/2021-09-27-showing-code-scanning-alerts-on-pull-requests/)
- [blog.thundra.io: Top 10 GitHub Actions You Should Use to set up your CI/CD Pipeline](https://blog.thundra.io/top-10-github-actions-you-should-use-to-set-up-your-ci/cd-pipeline)
- [github.blog: 10 GitHub Actions resources to bookmark from the basics to CI/CD](https://github.blog/2021-11-04-10-github-actions-resources-basics-ci-cd/)
- [==resources.github.com: What is GitHub Actions? How automation & CI/CD work on GitHub (whitepaper/pdf)==](https://resources.github.com/devops/tools/automation/actions)
- [==github.blog: Container signing added to the Publish Docker Container workflow for GitHub Actions==](https://github.blog/changelog/2021-12-06-container-signing-added-to-the-publish-docker-container-workflow-for-github-actions/) We have added support for [sigstore](https://www.sigstore.dev/) container signing to the default GitHub Actions starter workflow for publishing container images. New workflows on public repositories will use this by default. If you have an existing workflow, you will need to update your workflow to take advantage of this capability.
- [dev.to: What's the difference between a GitHub Action and a Workflow?](https://dev.to/github/whats-the-difference-between-a-github-action-and-a-workflow-2gba)
- [github.blog: 5 automations every developer should be running](https://github.blog/2021-12-16-5-automations-every-developer-should-be-running/)
- [==github.blog: Getting started with GitHub Actions just got easier!==](https://github.blog/2021-12-17-getting-started-with-github-actions-just-got-easier/)
- [github.blog: GitHub Actions: Improvements to GitHub Actions starter experience](https://github.blog/changelog/2021-12-17-github-actions-improvements-to-github-actions-starter-experience/)
- [==levelup.gitconnected.com: GitHub may replace DockerHub==](https://levelup.gitconnected.com/github-may-replace-dockerhub-a5da5e547f01)
- [blog.fleetdm.com: 4 tips for GitHub Actions usability (+2 bonus tips for debugging)](https://blog.fleetdm.com/4-tips-for-github-actions-usability-2-debugging-4c0c920adfde)
- [==freecodecamp.org: How to Build Your First JavaScript GitHub Action==](https://www.freecodecamp.org/news/build-your-first-javascript-github-action/)
- [dev.to: Make your first contribution to a GitHub Action!](https://dev.to/github/how-to-edit-a-github-action-3j14)
- [blog.ediri.io: Auto Docs, Test And Release A Helm Chart With GitHub Actions](https://blog.ediri.io/auto-docs-test-and-release-a-helm-chart-with-github-actions)
- [blog.shreyaspatil.dev: Automate library publishing to Maven Central with GitHub Actions Workflow Dispatch](https://blog.shreyaspatil.dev/automate-library-publishing-to-maven-central-with-github-actions-workflow-dispatch)
- [laravel-news.com: Deploy your PHP Codebase with Ansible and GitHub Actions](https://laravel-news.com/deploy-your-php-app-with-ansible-and-github-actions)
- [infoq.com: How GitHub Does DevOps for its iOS and Android Apps](https://www.infoq.com/news/2022/01/GitHub-devops-mobile-apps/)
- [blog.gskinner.com: Flutter: Easily add CI testing with GitHub Actions](https://blog.gskinner.com/archives/2022/01/flutter-easily-add-ci-testing-with-github-actions.html)
- [==devblogs.microsoft.com: .NET 💜 GitHub Actions==](https://devblogs.microsoft.com/dotnet/dotnet-loves-github-actions/)
- [==tonylixu.medium.com: GitOps — Github Actions Docker Build Workflow==](https://tonylixu.medium.com/gitops-github-actions-docker-build-workflow-157cc53e9a0d) GitOps using Github Actions
- [registry.terraform.io/modules/markti/github-runner](https://registry.terraform.io/modules/markti/github-runner/azurerm) Provision a Custom Runner for GitHub Actions
- [build5nines.com: Configuring Manual Triggers in GitHub Actions with `workflow_dispatch`](https://build5nines.com/configuring-manual-triggers-in-github-actions-with-workflow_dispatch/)
- [medium.com/@george_bakas: Mastering GitHub Actions: Environment Variables and Secrets Management](https://medium.com/@george_bakas/mastering-github-actions-environment-variables-and-secrets-management-3daac384477b)
- [build5nines.com: Configuring GitHub Actions to Run Jobs on Specific Branches](https://build5nines.com/configuring-github-actions-to-run-jobs-on-specific-branches/)
- [build5nines.com: GitHub Actions: Get Current Branch Name for Git Repo](https://build5nines.com/github-actions-get-current-branch-name-for-git-repo/)

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
- [hipertextual.com: GitHub une fuerzas con OpenIA para crear una inteligencia artificial capaz de autocompletar código](https://hipertextual.com/2021/06/github-inteligencia-artificial-autocompletar-codigo) GitHub Copilot funciona con la inteligencia artificial de OpenAI. La herramienta busca mejorar el aprendizaje de lenguajes de programación.
- [xataka.com: Para qué programar cuando una máquina lo hace (un poco) por ti: así es Github Copilot, un sistema que se nutre del prodigioso GPT-3](https://www.xataka.com/robotica-e-ia/programar-cuando-maquina-hace-poco-ti-asi-github-copilot-sistema-que-se-nutre-prodigioso-gpt-3)
- [thenewstack.io: GitHub Copilot: A Powerful, Controversial Autocomplete for Developers](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers)
- [xataka.com: Llevo algunos días usando Copilot de GitHub para programar y esta es mi experiencia](https://www.xataka.com/robotica-e-ia/llevo-algunos-dias-usando-copilot-github-para-programar-esta-mi-experiencia)
- [medium: GitHub’s AI Copilot Might Get You Sued If You Use It](https://medium.com/geekculture/githubs-ai-copilot-might-get-you-sued-if-you-use-it-c1cade1ea229) Some are even abandoning GitHub because of it
- [towardsdatascience.com: Can Github Copilot Replace Developers?](https://towardsdatascience.com/can-githubs-copilot-replace-developers-b89f28007c05) Since its release, copilot has become the talk of the town among developers. There are many pros and cons to using it.
- [towardsdatascience.com: Generating Python Scripts with OpenAi’s Github Copilot](https://towardsdatascience.com/generating-python-scripts-with-openais-github-copilot-da0b3fdd989) Using AI to generate Python scripts for simple neural networks, data visualization and more
- [dev.to: GitHub Copilot blew my mind on a code-along exercise](https://dev.to/colocodes/github-copilot-blew-my-mind-on-a-code-along-exercise-186n)
- [medium.com/@eriky: Copilot Is Genuinely Scary And Fascinating At The Same Time](https://medium.com/@eriky/copilot-is-genuinely-scary-and-fascinating-at-the-same-time-63ebcbf80899) It knows more than just programming languages
- [GitHub Copilot is generally available to all developers](https://github.blog/2022-06-21-github-copilot-is-generally-available-to-all-developers/) **We’re making GitHub Copilot, an AI pair programmer that suggests code in your editor, generally available to all developers for $10 USD/month or $100 USD/year. It will also be free to use for verified students and maintainers of popular open source projects.**
- [xataka.com: GitHub Copilot, el asistente para programar basado en IA, ya está disponible para todos: cuánto cuesta y quienes lo pueden usar gratis](https://www.xataka.com/aplicaciones/github-copilot-asistente-para-escribir-codigo-basado-ia-esta-disponible-para-todos-esto-que-costara)
- [genbeta.com: Ya hay organizaciones pro-software libre abandonando GitHub por su uso comercial de proyectos open source en Copilot](https://www.genbeta.com/desarrollo/hay-organizaciones-pro-software-libre-abandonando-github-su-uso-comercial-proyectos-open-source-copilot)
- [xataka.com: Copilot ya escribe el 40% del código de lenguajes como Java o Python que llega a GitHub. En cinco años llegará al 80%](https://www.xataka.com/aplicaciones/copilot-escribe-40-codigo-lenguajes-como-java-python-que-llega-a-github-cinco-anos-llegara-al-80)
- [xataka.com: Copilot es una revolución para programadores (pero también un potencial problema legal para Microsoft)](https://www.xataka.com/robotica-e-ia/copilot-revolucion-para-programadores-tambien-potencial-problema-legal-para-microsoft)
- [github.blog: GitHub Copilot X: The AI-powered developer experience](https://github.blog/2023-03-22-github-copilot-x-the-ai-powered-developer-experience/) GitHub Copilot is evolving to bring chat and voice interfaces, support pull requests, answer questions on docs, and adopt OpenAI’s GPT-4 for a more personalized developer experience.
- [techcommunity.microsoft.com: Coding Frameworks and languages are no longer the point, prompting is](https://techcommunity.microsoft.com/t5/educator-developer-blog/coding-frameworks-and-languages-are-no-longer-the-point/ba-p/3820265)
- [github.blog/developer-skills: 10 unexpected ways to use GitHub Copilot](https://github.blog/developer-skills/programming-languages-and-frameworks/10-unexpected-ways-to-use-github-copilot/) GitHub Copilot is widely known for its code generation feature. Learn how the AI assistant’s abilities can extend beyond just code generation.

#### GitHub CoPilot VS GPT-3

- [python.plainenglish.io: Who Writes Better Code: GitHub CoPilot or GPT-3?](https://python.plainenglish.io/who-writes-better-code-github-copilot-or-gpt-3-9e7441650c9b)

#### GitHub Copilot X

- [computerhoy.com: GitHub Copilot X: así es la nueva IA parecida a ChatGPT y destinada a ayudar a programadores](https://computerhoy.com/software/github-copilot-x-nueva-ia-parecida-chatgpt-destinada-ayudar-programadores-1219266)

#### Alternatives

- [medium.com/geekculture: Hey ChatGPT, Automate These Tasks Using Python](https://medium.com/geekculture/hey-chatgpt-solve-these-coding-tasks-using-python-b2e7482f2c18) Using AI to plot graphs, send emails/messages, and do web scraping in a few seconds.
- [xataka.com: Los programadores ya alucinaban con CoPilot y ChatGPT, pero ahora DeepMind va más allá con AplhaCode](https://www.xataka.com/robotica-e-ia/programadores-alucinaban-copilot-chatgpt-ahora-deepmind-va-alla-aplhacode)
- [lucidrains/PaLM-rlhf-pytorch](https://github.com/lucidrains/PaLM-rlhf-pytorch) The first open source equivalent of ChatGPT. Implementation of RLHF (Reinforcement Learning with Human Feedback) on top of the PaLM architecture. Basically ChatGPT but with PaLM

##### CodiumAI

- [codium.ai: We’ve launched CodiumAI powered by TestGPT and raised $11M. Here’s why](https://www.codium.ai/blog/codiumai-powered-by-testgpt-accounces-beta-and-raised-11m/)

## Gitea

- [Gitea](https://gitea.com/)
- [itnext.io: Setup a Private Git-Repository in Kubernetes with Gitea](https://itnext.io/setup-a-private-git-repository-in-kubernetes-with-gitea-64f5ea1e5070)

## Sapling

- [sapling-scm.com](https://sapling-scm.com/docs/introduction/)
- [betterprogramming.pub: My First Impressions of Sapling — Meta’s New Git Client](https://betterprogramming.pub/four-ways-you-can-experiment-with-sapling-709eec0ffcb1)

## Git Tools

- [Atlassian Sourcetree](https://www.sourcetreeapp.com/)
    - [Sourcetree Cheat Sheet](https://kapeli.com/cheat_sheets/Sourcetree.docset/Contents/Resources/Documents/index)
- [gitkraken.com](https://www.gitkraken.com/)
    - [GitKraken Git Cheat](https://www.gitkraken.com/resources/gitkraken-cheat-sheet)
    - [dzone.com: See What's New in GitKraken v4.0](https://dzone.com/articles/see-whats-new-in-gitkraken-v40)
    - [youtube: GitKraken Tutorials and Tips](https://www.youtube.com/watch?v=gjtXTm_TvvE&list=PLe6EXFvnTV78WqGmGSq8JPnafR3lAa55n)
- [gmaster](https://gmaster.io/)
- [Visual Studio Code (Git Extensions)](visual-studio.md)
- [Visual Studio Online](https://visualstudio.microsoft.com/services/visual-studio-codespaces/)
- [git-lfs/git-lfs: Git Large File Storage](https://github.com/git-lfs/git-lfs) Git extension for versioning large files
- [==github.com/MichaelMure/git-bug==](https://github.com/MichaelMure/git-bug) **Distributed, offline-first bug tracker embedded in git, with bridges**
- [blog.kubesimplify.com: Moving code between GIT repositories with Copybara | Daniele Polencic](https://blog.kubesimplify.com/moving-code-between-git-repositories-with-copybara)

### Git Credential Manager

- [==Git Credential Manager==](https://github.com/GitCredentialManager/git-credential-manager) **Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services.**
- Git Credential Manager (GCM) is a secure Git credential helper built on .NET that runs on Windows, macOS, and Linux.
- [github.blog: Git Credential Manager: authentication for everyone](https://github.blog/2022-04-07-git-credential-manager-authentication-for-everyone/) Ensuring secure access to your source code is more important than ever. Git Credential Manager helps make that easy.

### Semantic-release. CI/CD semantic release workflow (semantic Versioning, commit format and releases)

- [semantic-release.gitbook.io 🌟](https://semantic-release.gitbook.io/semantic-release/) Semantic-release automates the whole package release workflow including: determining the next version number, generating the release notes and publishing the package.
- [css-tricks.com: How to Automate Project Versioning and Releases with Continuous Deployment 🌟](https://css-tricks.com/how-to-automate-project-versioning-and-releases-with-continuous-deployment/)

## Azure DevOps (formerly known as VSTS)

- [Wikipedia: Azure DevOps](https://en.wikipedia.org/wiki/Azure_DevOps)
    - [wikipedia: Azure DevOps Server](https://en.wikipedia.org/wiki/Azure_DevOps_Server) Collaboration software for software development formerly known as Team Foundation Server and Visual Studio Team System
    - [wikipedia: Azure DevOps Services](https://en.wikipedia.org/wiki/Microsoft_Visual_Studio#Azure_DevOps_Services) Cloud service for software development formerly known as Visual Studio Team Services, Visual Studio Online and Team Foundation Service Preview
- [Azure DevOps Labs 🌟](https://azuredevopslabs.com/)
- [twitter.com/azuredevops](https://twitter.com/azuredevops)
- [Microsoft Visual Studio Team Services (VSTS)](https://www.dotnetcurry.com/visualstudio/1322/what-is-visual-studio-team-system-vsts)
- [Microsoft Visual Studio Team Services (VSTS) Tutorial: The Cloud ALM Platform](https://www.softwaretestinghelp.com/microsoft-vsts-tutorial-1/)
- [slideshare.net: Git version control and trunk based approach with VSTS](https://www.slideshare.net/arunmurughan/git-version-control-and-trunk-based-approach-with-vsts)
- [Microsoft Replacing Visual Studio Team Services with Azure DevOps](https://redmondmag.com/articles/2018/09/10/microsoft-replacing-vsts-with-azure-devops.aspx)
- [How We Use Git at Microsoft](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/use-git-microsoft)

## Pre Commit Hooks

- [pre-commit](https://pre-commit.com/) A framework for managing and maintaining multi-language pre-commit hooks.
- [towardsdatascience.com: CI/CD by Example in Python](https://towardsdatascience.com/ci-cd-by-example-in-python-46f1533cb09d) A simple demonstration of CI/CD in Python with poetry and pre-commit hooks, [poetry-template](https://github.com/edkrueger/poetry-template)

## Merge BOTs

- The Merge Bot is a tool to orchestrate pull requests merging into the stable branches.
- [Wikipedia: Software bot](https://en.wikipedia.org/wiki/Software_bot)

### Tips

- Use bots to accomplish tasks like merging PR's that have been approved and automatically updating dependencies. Usage of one of these bots might allow us to trigger certain builds based off of specific GitHub tags,  it would allow us to only selectively run certain test suites and increase the throughput of the build by only testing changes made in a branch / PR.
- Investigate options that are available and see if we can integrate them with CI.
- We should be able to configure this bot to automatically apply labels to PR's based off of what is changed in a PR. For instance, if a PR contains any documentation changes, the area/Documentation label can be applied.

### Jenkins for git merges

- [**Git Plugin**: Merge Extensions](https://plugins.jenkins.io/git/#merge-extensions)
- [**Validated Merge Plugin** for Git in CloudBees Jenkins Enterprise 🌟](https://docs.cloudbees.com/docs/admin-resources/latest/plugins/validated-merge#chapter-validated-merge_validated-merge)
- [How to configure Jenkins for git merge](https://support.cloudbees.com/hc/en-us/articles/227246387-How-to-Configure-Jenkins-for-Git-Merge-)
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
- [How to Implement the Automerge feature that is missing from BitBucket cloud](https://poolofthought.com/how-to-implement-the-automerge-feature-that-is-missing-from-bitbucket-cloud/)
- [Configure bitbucket-pipelines.yml to automatically merge feature branch to master?](https://community.atlassian.com/t5/Bitbucket-questions/configure-bitbucket-pipelines-yml-to-automatically-merge-feature/qaq-p/793222)

### GitLab for git merges

- [Auto-merge between release branches](https://gitlab.com/gitlab-org/gitlab/-/issues/2785)
- [Provide merge bot functionality](https://gitlab.com/gitlab-org/gitlab/-/issues/14595)
- [lab.texthtml.net: Gitlab Merge Bot](https://lab.texthtml.net/gitlab/merge-bot)
    - [DockerHub: Gitlab Merge Bot](https://hub.docker.com/r/texthtml/gitlab-merge-bot/) Bot assistant for code review and merge requests approval for Gitlab
- [Mergecrush](https://www.mergecrush.com/) A email & slack reminder bot for Gitlab merge requests.
- [stackoverflow.com: How can we programmatically approve merge requests in GitLab?](https://stackoverflow.com/questions/58019605/how-can-we-programmatically-approve-merge-requests-in-gitlab)
    - Our group has a bot that creates merge requests for certain mechanical changes to our code base. We'd like these MRs to get merged in automatically if/when the CI pipeline succeeds, but our projects require an approval from a member of our group. This means that right now a human has to manually click on "approve" and "merge" for each bot-created MR. Apparently GitLab doesn't have a way to set different approval rules for some users, so I haven't found a way to make the bot's user immune to this requirement.
    - My current idea is to have a separate process that approves each of the merge requests created by the bot. Is there an easy way to do this programmatically? That is, is there an API (or better yet, a command line tool) that, when given the name of the branch for a merge request, approves the merge request associated with that branch?
    - I'm also open to other ways of getting these changes in with minimal human intervention. I do want them to pass the CI pipeline, though (which is currently accomplished by having them use MRs) and the MRs also help in the rare cases where the pipeline fails, so we can debug what went wrong.

#### Marge GitLab bot

- [Marge-bot: A merge-bot for GitLab](https://github.com/smarkets/marge-bot)
- [Example: gitlab.gnome.org/marge-merge-bot](https://gitlab.gnome.org/marge-merge-bot)
- [Example: Smarkets's Marge-bot for GitLab keeps master always green](https://smarketshq.com/marge-bot-for-gitlab-keeps-master-always-green-6070e9d248df)
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

- [mergify.io](https://mergify.io/)
- [medium: Merging Bots’ Pull Requests Automatically](https://medium.com/mergify/merging-bots-pull-requests-automatically-548ed0b4a424)

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
- [stackoverflow.com: Bot to automatically reverse GitHub pull request merges](https://stackoverflow.com/questions/27820309/bot-to-automatically-reverse-github-pull-request-merges). Maybe it's best to not allow the merges instead of reverting them:
    - [help.github.com: Configuring protected branches](https://help.github.com/en/github/administering-a-repository/configuring-protected-branches)
    - [help.github.com: Enabling required status checks:](https://help.github.com/en/github/administering-a-repository/enabling-required-status-checks)
        - Select Require status checks to pass before merging
        - Choose (create) a status check, that always fails

#### Bors GitHub bot

- [Bors Bot](https://bors.tech/)
- [Bors - Readme](https://bors.tech/devdocs/bors-ng/readme.html)
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
