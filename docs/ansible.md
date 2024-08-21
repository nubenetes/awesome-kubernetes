# Configuration Management. Ansible

1. [Configuration Management with Ansible DevOps Tool](#configuration-management-with-ansible-devops-tool)
2. [Ansible AI](#ansible-ai)
3. [Ansible UI](#ansible-ui)
4. [Deploying custom files with Jinja2 templates](#deploying-custom-files-with-jinja2-templates)
5. [Writing an Ansible module](#writing-an-ansible-module)
6. [Interacting with REST API](#interacting-with-rest-api)
    1. [Writing an Ansible module for a REST API](#writing-an-ansible-module-for-a-rest-api)
7. [Ansible Videos](#ansible-videos)
8. [Ansible Playbooks](#ansible-playbooks)
9. [Ansible Collections](#ansible-collections)
10. [Red Hat Ansible Automation Platform](#red-hat-ansible-automation-platform)
     1. [Automation services catalog](#automation-services-catalog)
     2. [Red Hat Certified Ansible Content Collections](#red-hat-certified-ansible-content-collections)
11. [Ansible Cheat Sheets](#ansible-cheat-sheets)
12. [Running Ansible Playbooks](#running-ansible-playbooks)
     1. [Running Ansible Playbooks From Jenkins](#running-ansible-playbooks-from-jenkins)
     2. [Ansible Tower and Ansible AWX. Running Ansible Playbooks From Ansible Tower](#ansible-tower-and-ansible-awx-running-ansible-playbooks-from-ansible-tower)
         1. [Tower and AWX Installers](#tower-and-awx-installers)
     3. [Alternatives to Ansible Tower](#alternatives-to-ansible-tower)
13. [Ansible Kubernetes Operators](#ansible-kubernetes-operators)
14. [Ansible Molecule. Development and Testing of Ansible Roles](#ansible-molecule-development-and-testing-of-ansible-roles)
15. [Books](#books)
16. [Ansible Galaxy Roles](#ansible-galaxy-roles)
17. [More Ansible Roles](#more-ansible-roles)
18. [Ansible scripts](#ansible-scripts)
19. [Ansible with Helm](#ansible-with-helm)
20. [Awesome Ansible](#awesome-ansible)
21. [Ansible and Public Cloud Guides](#ansible-and-public-cloud-guides)
22. [Ansible Kubernetes Module](#ansible-kubernetes-module)
23. [NGINX Core Collection for Ansibe](#nginx-core-collection-for-ansibe)
24. [Dynatrace with Ansible](#dynatrace-with-ansible)
25. [SQL Server with Ansible](#sql-server-with-ansible)
26. [OCI Oracle Cloud Infrastructure with Ansible](#oci-oracle-cloud-infrastructure-with-ansible)
27. [Oracle Database with Ansible](#oracle-database-with-ansible)
28. [Ansistrano. Deploying applications with Ansible in Capistrano style](#ansistrano-deploying-applications-with-ansible-in-capistrano-style)
29. [Anacron and Ansible](#anacron-and-ansible)
30. [Tweets](#tweets)
31. [Videos](#videos)

## Configuration Management with Ansible DevOps Tool

- [ansible.com](https://www.ansible.com/)
- [docs.ansible.com](https://docs.ansible.com/)
- [dureka.co: What Is Ansible?](https://www.edureka.co/blog/what-is-ansible/) Configuration Management And Automation With Ansible
- [Dzone: Getting Started With Ansible](https://dzone.com/articles/getting-started-with-ansible)
- [Dzone: Part 1: Getting Started with Ansible](https://dzone.com/articles/part-1-getting-started-ansible)
- [Dzone: Part 2: Deploying Applications](https://dzone.com/articles/part-2-deploying-applications)
- [Dzone: 10 easy to use modules in ansible](https://dzone.com/articles/10-easy-to-use-modules-in-ansible-1)
- [Dzone: Ansible: An Effective IT Automation Tool](https://dzone.com/articles/ansible-an-effective-it-automation-tool) Learn about Ansible, a tool for automating application deployments, configuration management, and more in a DevOps environment.
- [Dzone: Running Ansible at Scale](https://dzone.com/articles/running-ansible-at-scale)
- [Udemy.com: Ansible Essentials: Simplicity in Automation (Free Tutorial)](https://www.udemy.com/ansible-essentials-simplicity-in-automation)
- [Deployment of Microservices in Cloud With Ansible](https://medium.com/avmconsulting-blog/deploying-microservices-via-ansible-in-cloud-platform-a03d46b7bd68) This tutorial will help you understand how Ansible orchestrates Docker containers at least for a dev environment
- [opensource.com: How to install software with Ansible](https://opensource.com/article/20/9/install-packages-ansible) Automate software installations and updates across your devices with Ansible playbooks.
- [opensource.com: Automate your container orchestration with Ansible modules for Kubernetes 🌟](https://opensource.com/article/20/9/ansible-modules-kubernetes) Combine Ansible with Kubernetes for cloud automation. Plus, get our cheat sheet for using the Ansible k8s module.
- [opensource.com: A quickstart guide to Ansible 🌟](https://opensource.com/article/19/2/quickstart-guide-ansible) Download the Ansible Automation for SysAdmins guide.
- [opensource.com: 7 things you can do with Ansible right now](https://opensource.com/article/20/9/ansible) If Ansible's inclusion as a leader on the Forrester Wave report piqued your interest, here are some ways the automation solution can simplify your life.
- [medium.com: The Ultimate Guide for Ansible Total Domination 🌟](https://medium.com/the-programming-hub/the-ultimate-guide-for-ansible-total-domination-e70bdfc11175)
- [opensource.com: Integrate your calendar with Ansible to avoid schedule conflicts 🌟](https://opensource.com/article/20/10/calendar-ansible) Make sure your automation workflow's schedule doesn't conflict with something else by integrating a calendar app into Ansible.
- [opensource.com: My first day using Ansible](https://opensource.com/article/20/10/first-day-ansible) A sysadmin shares information and advice about putting Ansible into real-world use configuring computers on his network.
- [siliconangle.com: Red Hat ties Ansible automation to Kubernetes cluster management 🌟](https://siliconangle.com/2020/10/13/red-hat-ties-ansible-automation-kubernetes-cluster-management/)
- [sdxcentral.com: Red Hat Links Ansible Automation to Kubernetes Management 🌟](https://www.sdxcentral.com/articles/news/red-hat-links-ansible-automaton-to-kubernetes-management/)
- [thenewstack.io: Red Hat Brings Ansible Automation to Kubernetes 🌟](https://thenewstack.io/red-hat-brings-ansible-automation-to-kubernetes/)
- [openshift.com: Ansible and OpenShift: Connecting for Success 🌟](https://www.openshift.com/blog/ansible-and-openshift-connecting-for-success)
- [zdnet.com: ed Hat expands Ansible ready to run cloud programs 🌟](https://www.zdnet.com/article/red-hat-expands-ansible-ready-to-run-cloud-programs/) And, on top of more plug-and-play Ansible programs, you can now run Ansible hand-in-glove with Red Hat OpenShift.
- [theregister.com: Juggling Ansible, OpenShift and K8s? This is for you: Red Hat couples automation to cluster management](https://www.theregister.com/2020/10/14/redhat_ansible_kubernetes/)
- [redhat.com: Ansible Essentials: Simplicity in Automation Technical Overview (Free Course) 🌟](https://www.redhat.com/en/services/training/do007-ansible-essentials-simplicity-automation-technical-overview)
- [opensource.com: 10 Ansible modules for Linux system automation c](https://opensource.com/article/20/10/ansible-modules-linux) These handy modules save time and hassle by automating many of your daily tasks, and they're easy to implement with a few commands.
- [redhat.com: Renewing my thrill at work with Ansible](https://www.redhat.com/sysadmin/renewed-thrill-ansible)
- [opensource.com: Set up an Ansible lab in 20 minutes](https://opensource.com/article/20/12/ansible-lab) Build an environment to support learning and experimenting with new software.
- [opensource.com: 4 lines of code to improve your Ansible play](https://opensource.com/article/21/1/improve-ansible-play)
- [redhat.com: Demystifying Ansible for Linux sysadmins 🌟](https://www.redhat.com/sysadmin/demystifying-ansible-sysadmins) Taking the labor out of labor-intensive tasks is what Ansible is all about. Learn the basics here.
    - [redhat.com: Quick start guide to Ansible for Linux sysadmins 🌟](https://www.redhat.com/sysadmin/ansible-quick-start)
- [opensource.com: 10 ways Ansible is for everyone 🌟](https://opensource.com/article/21/1/ansible) Expand your knowledge and skills with the top 10 Ansible articles plus five news summaries from 2020
- [ansible.com: Ansible Network Resource Modules: Deep Dive on Return Values](https://www.ansible.com/blog/ansible-network-resource-modules-deep-dive-on-return-values)
- [linkedin.com: Ansible what is it and what not](https://www.linkedin.com/pulse/ansible-what-marcel-koert/)
- [redhat.com: How to automate system reboots using the Ansible reboot module](https://www.redhat.com/sysadmin/automate-reboot-ansible)
- [developer.okta.com: Tutorial: Ansible and Account Automation with Okta](https://developer.okta.com/blog/2021/02/05/okta-ansible)
- [redhat.com: Got automation? Here's a quick guide to get you up to speed on Ansible 🌟](https://www.redhat.com/sysadmin/how-start-ansible) This article gives you a quick, high-level guide on how to start with Ansible
- [opensource.com: How Ansible got started and grew](https://opensource.com/article/21/2/ansible-origin-story)
- [ansible.com: Announcing the Community Ansible 3.0.0 Package 🌟](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package)
- [toptechskills.com: Ansible Tutorials & Courses 🌟](https://www.toptechskills.com/ansible-tutorials-courses/) Ansible is an agentless infrastructure as code (IAC) tool that is super effective at configuring cloud and bare metal infrastructure.
    - [toptechskills.com: How to Speed Up Your Ansible Playbooks Over 600% 🌟](https://www.toptechskills.com/ansible-tutorials-courses/speed-up-ansible-playbooks-pipelining-mitogen/)
- [opensource.com: 5 everyday sysadmin tasks to automate with Ansible 🌟](https://opensource.com/article/21/3/ansible-sysadmin) Get more efficient and avoid errors by automating repeatable daily tasks with Ansible.
- [redhat.com: 8 steps to developing an Ansible role in Linux 🌟](https://www.redhat.com/sysadmin/developing-ansible-role) In this article, an existing Ansible playbook is used to deploy Vim and convert it to a role adding flexibility and reusability.
- [ansible.com: Ansible whitepaper](https://www.ansible.com/resources/whitepapers/ansible-in-depth) Download this paper for a deep dive into Ansible, an open source IT configuration management, deployment, and orchestration tool.
- [redhat.slides.com: Ansible 202 - Best Practices from the field](http://redhat.slides.com/jparrill/ansible-202/fullscreen?token=1hUEEPF4#/11/1) - [asciinema.org/~padajuan](https://asciinema.org/~padajuan)
- [redhat.com: How to use Ansible to send an email using Gmail](https://www.redhat.com/sysadmin/configure-gmail-using-ansible)
- [redhat.com: How to use Ansible to configure a reverse proxy 🌟](https://www.redhat.com/sysadmin/reverse-proxy-ansible) Placing a load balancer in front of your web server infrastructure helps ensure any spike in traffic doesn't bring down the site.
- [Ansible 3.3.0 released](https://groups.google.com/g/ansible-devel/c/CdQ7eWUUm8k?pli=1)
- [fedoramagazine.org: Using Ansible to configure Podman containers 🌟](https://fedoramagazine.org/using-ansible-to-configure-podman-containers/)
- [acloudguru.com: Ansible vs Puppet: Which is right for you?](https://acloudguru.com/blog/engineering/ansible-vs-puppet-which-is-right-for-you)
- [redhat.com: Add a repo and install a package the Ansible way](https://www.redhat.com/sysadmin/install-ansible-way) How to add package repositories and install packages on many hosts by using Ansible.
- [automateinfra.com: Everything about Ansible 🌟](https://automateinfra.com/everything-about-ansible/)
- [redhat.com: Introduction to RHEL System Roles 🌟](https://www.redhat.com/en/blog/introduction-rhel-system-roles) How to use Ansible Roles with RedHat Enterprise Linux
- [linuxtechlab.com: Ansible Tutorial: Introduction to simple Ansible commands](https://linuxtechlab.com/ansible-tutorial-simple-commands/)
- [k21academy.com: Ansible for Beginners | Overview | Architecture & Use Cases 🌟](https://k21academy.com/ansible/ansible-for-beginners)
    - [k21academy.com: Ansible for Beginners Day2 Live Session Review and Q/A 🌟](https://k21academy.com/ansible/day2-live-session-review-and-q-a/)
- [analyticsindiamag.com: Ansible vs Docker: A Detailed Comparison Of DevOps Tools](https://analyticsindiamag.com/ansible-vs-docker-a-detailed-comparison-of-devops-tools)
- [redhat.com: 6 steps to automating code pushes with Ansible Automation Platform 🌟](https://www.redhat.com/sysadmin/6-code-pushes-aap) Use a Git push to trigger an Ansible Automation Platform playbook execution in six easy steps.
- [redhat.com: 4 steps to create Linux users from a csv file with Ansible](https://www.redhat.com/sysadmin/ansible-create-users-csv) Automate Linux user account creation in four simple steps with Ansible.
- [cyberciti.biz: How to define multiple when conditions in Ansible](https://www.cyberciti.biz/faq/how-to-define-multiple-when-conditions-in-ansible/)
- [dev.to: DevOps 101 : Introduction to Ansible](https://dev.to/grayhat/devops-101-introduction-to-ansible-1n64)
- [redhat.com: How to set up and use Python virtual environments for Ansible](https://www.redhat.com/sysadmin/python-venv-ansible) Python's venv module gives you freedom to test new Ansible features before deploying them to production and without disturbing your system install.
- [redhat.com: Deep dive into Ansible ad hoc commands](https://www.redhat.com/sysadmin/ansible-ad-hoc-commands) Make life easier when dealing with Ansible automation by using ad hoc commands.
- [redhat.com: How to install software packages with an Ansible playbook](https://www.redhat.com/sysadmin/software-packages-ansible) Learn how to install new software packages on all your managed hosts with a single Ansible playbook.
- [getbetterdevops.io: Build Docker Images Using Ansible and Packer](https://getbetterdevops.io/build-docker-images-using-ansible-and-packer/) Build Image from Ansible code and persist them on local or in AWS ECR
- [developers.redhat.com: Automate Red Hat JBoss Web Server deployments with Ansible](https://developers.redhat.com/articles/2021/08/30/automate-red-hat-jboss-web-server-deployments-ansible)
- [redhat.com: How to create dynamic configuration files using Ansible templates](https://www.redhat.com/sysadmin/ansible-templates-configuration) Ansible templates extend your ability to configure applications quickly and easily. This example uses a template to configure Vim.
- [redhat.com: 16 AnsibleFest presentations for sysadmins](https://www.redhat.com/sysadmin/ansiblefest-sysadmins) AnsibleFest offers a lot of information to help sysadmins automate better.
- [opensource.com: How I keep my file folders tidy with Ansible](https://opensource.com/article/21/9/keep-folders-tidy-ansible) I try to use Ansible often, even for tasks that I know how to do with a shell script because I know that Ansible is easy to scale.
- [developers.redhat.com: Four reasons developers should use Ansible](https://developers.redhat.com/articles/2021/09/27/four-reasons-developers-should-use-ansible)
- [opensource.com: How I keep my file folders tidy with Ansible](https://opensource.com/article/21/9/keep-folders-tidy-ansible) I try to use Ansible often, even for tasks that I know how to do with a shell script because I know that Ansible is easy to scale.
- [vitux.com: How to speed-up an Ansible Playbook 🌟](https://vitux.com/how-to-speed-up-an-ansible-playbook/)
- [youtube: Ansible Automation | How to Secure and Protect Critical Information Playbooks Using Ansible Vault](https://www.youtube.com/watch?v=mc20VwxYaGE&t=3s&ab_channel=CLOUDLEARNHUB)
- [==opensource.com: 9 ways to learn Ansible this year== 🌟](https://opensource.com/article/22/1/learn-ansible) Ansible is an open source automation tool that can be used in a variety of ways. Here are a few examples of last year's most popular Ansible tutorials and stories.
- [redhat.com: Top 10 Ansible tutorials of 2021](https://www.redhat.com/sysadmin/top-ansible-articles-2021) Whether you're new to Ansible or looking to level up your automation skills, you'll find something of value in 2021's top Ansible articles.
- [cloud.google.com: How to deploy the Google Cloud Ops Agent with Ansible](https://cloud.google.com/blog/products/operations/use-ansible-to-deploy-the-google-cloud-ops-agent)
- [cloudbees.com: Getting Started Quickly With Ansible Ad Hoc Commands](https://www.cloudbees.com/blog/getting-started-quickly-with-ansible-ad-hoc-commands)
- [redhat.com: 8 ways to speed up your Ansible playbooks](https://www.redhat.com/sysadmin/faster-ansible-playbook-execution) Here's how to optimize your Ansible playbooks to make them run faster.
- [middlewareinventory.com: Ansible List Examples – How to create and append items to List 🌟](https://www.middlewareinventory.com/blog/ansible-list-examples-how-to-create-and-append-items-to-list/)
- [middlewareinventory.com: Ansible Dictionary – How to create and add items to dict](https://www.middlewareinventory.com/blog/ansible-dict/)
- [middlewareinventory.com: How to use ansible with S3 – Ansible aws_s3 examples | Devops Junction](https://www.middlewareinventory.com/blog/ansible-aws_s3-example/)
- [techbeatly.com: Ansible for Infrastructure Provisioning in AWS | Ansible Real Life Series - youtube](https://www.techbeatly.com/ansible-for-infrastructure-provisioning-in-aws-ansible-real-life-series/)
- [==redhat.com: How to create dynamic inventory files in Ansible==](https://www.redhat.com/sysadmin/ansible-dynamic-inventories) Learn how to use the host_list and Nmap plugins to build inventory files for your Ansible playbooks.
    - [==redhat.com: How to write a Python script to create dynamic Ansible inventories==](https://www.redhat.com/sysadmin/ansible-dynamic-inventory-python) Write a script in Python that fetches hosts using Nmap to generate dynamic inventories.
    - [==redhat.com: How to write an Ansible plugin to create inventory files==](https://www.redhat.com/sysadmin/ansible-plugin-inventory-files)
- [dlford.io: Orchestrate Your Systems with Ansible Playbooks - How to Home Lab Part 10 🌟](https://www.dlford.io/ansible-orchestration-how-to-home-lab-part-10/) Ansible is an administrative tool that aims to make server management easier by using declarative and idempotent configuration files.
- [learning-devops-tools-with-nandita.blogspot.com: Overview of Ansible and Ansible Playbooks](https://learning-devops-tools-with-nandita.blogspot.com/2022/08/overview-of-ansible-and-ansible.html)
- [blog.learncodeonline.in: Everything about Ansible Variables 🌟](https://blog.learncodeonline.in/everything-about-ansible-variables)
- [blog.learncodeonline.in: Managing File Operations With Ansible 🌟](https://blog.learncodeonline.in/managing-file-operations-with-ansible)
- [developers.redhat.com: How to install VMs and Ansible Automation Platform on Mac M1](https://developers.redhat.com/articles/2022/10/25/how-install-vms-and-ansible-automation-platform-mac-m1)
- [devopscube.com: How to Setup Ansible AWS Dynamic Inventory](https://devopscube.com/setup-ansible-aws-dynamic-inventory/)
- [ansible.com: Creating Custom Rules for Ansible Lint](https://www.ansible.com/blog/creating-custom-rules-for-ansible-lint) What's “linting?” Its objective is to promote proven behaviors, patterns, and practices while avoiding typical traps that can quickly result in errors or make code more difficult to maintain.
- [ansible.com: The Top 10 Ansible Blogs of 2022](https://www.ansible.com/blog/top-10-ansible-blogs-2022)
- [tomsitcafe.com: Getting started with Ansible playbooks: more steps towards DevOps](https://tomsitcafe.com/2023/02/14/getting-started-with-ansible-playbooks-more-steps-towards-devops/)
- [tomsitcafe.com: Conditional statements – making decisions in Ansible code](https://tomsitcafe.com/2023/02/17/conditional-statements-making-decisions-in-ansible-code/)
- [tomsitcafe.com: How to implement and use handlers in Ansible code?](https://tomsitcafe.com/2023/03/06/how-to-implement-and-use-handlers-in-ansible-code/)
- [tomsitcafe.com: Configuration file blueprints: Jinja2 templates in the Ansible code](https://tomsitcafe.com/2023/03/13/configuration-file-blueprints-jinja2-templates-in-the-ansible-code/)
- [tomsitcafe.com: Handling sensitive data with Ansible Vault: encrypting strings instead of files](https://tomsitcafe.com/2023/03/16/handling-sensitive-data-with-ansible-vault-encrypting-strings-instead-of-files/)
- [ansible.com: Kubernetes Meets Event-Driven Ansible 🌟](https://www.ansible.com/blog/kubernetes-meets-event-driven-ansible)
- [==sayali.hashnode.dev: Day 56: Understanding Ad-hoc commands in Ansible== 🌟](https://sayali.hashnode.dev/day-56-understanding-ad-hoc-commands-in-ansible)
- [tomsitcafe.com: Let’s use a more flexible directory structure for an Ansible project](https://tomsitcafe.com/2023/05/11/lets-use-a-more-flexible-directory-structure-for-an-ansible-project/)
- [tomsitcafe.com: Enhancing Ansible Automation: Exploring the Power of Ansible Semaphore, a Modern Open-Source GUI](https://tomsitcafe.com/2023/05/15/ansible-semaphore-a-modern-open-source-gui-for-our-ansible-automation/)
- [tomsitcafe.com: Mastering Ansible: Navigating the Most Common Errors and Mistakes](https://tomsitcafe.com/2023/06/02/mastering-ansible-navigating-the-most-common-errors-and-mistakes/)
- [tomsitcafe.com: Automating APIs with Ansible: A Comprehensive Guide](https://tomsitcafe.com/2023/06/09/automating-apis-with-ansible-a-comprehensive-guide/)
- [medium.com/@Techie1: Networking tasks in production using Ansible](https://medium.com/@Techie1/networking-tasks-in-production-using-ansible-b09d0a6121f7)
- [medium.com/cloud-native-daily: Getting Started with Ansible: A Comprehensive Guide for DevOps Beginners](https://medium.com/cloud-native-daily/getting-started-with-ansible-a-comprehensive-guide-for-devops-beginners-fd2fb3fd7a40) Automate complex tasks, manage your Docker containers effortlessly, and even enhance collaboration using Ansible
- [devopsinside.com: Is Kubernetes killing tools like Ansible?](https://devopsinside.com/how-kubernetes-is-killing-tools-like-ansible/)
    - Kubernetes is not a replacement for ansible: Despite their overlapping functionality, it is important to note that Kubernetes is not a replacement for ansible. Both tools have their own strengths and use cases, and they can be used together to achieve different goals.
    - Kubernetes and ansible can be used together: Kubernetes and ansible can be used together to complement each other. For example, ansible can be used to automate the provisioning and configuration of Kubernetes clusters, while Kubernetes can be used to manage the deployment and scaling of applications within those clusters.
- [community.ibm.com: Red Hat Ansible Automation Platform on IBM Z and IBM LinuxONE is generally available now!](https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/daniel-jast1/2023/12/07/red-hat-aap-on-ibm-z-and-linuxone)
- [intellipaat.com: Ansible vs Kubernetes vs Docker](https://intellipaat.com/blog/ansible-vs-kubernetes-vs-docker/)
- [redhat.com/sysadmin/ansible-lists-dictionaries-yaml: How to work with lists and dictionaries in Ansible 🌟](https://www.redhat.com/sysadmin/ansible-lists-dictionaries-yaml)
- [github.com/naveensilver/Ansible](https://github.com/naveensilver/Ansible) My Ansible Notes (Beginner to Advanced) : Repository to learn Ansible from Zero. This repository covers the complete Ansible fundamentals along with examples required for a DevOps Engineer.

## Ansible AI

- [==ansible.ai==](https://ansible.ai)
- [redhat.com: Red Hat Ansible Lightspeed with IBM watsonx Code Assistant](https://www.redhat.com/en/technologies/management/ansible/ansible-lightspeed) Red Hat® Ansible® Lightspeed with IBM watsonx Code Assistant helps automation teams learn, create, and maintain Red Hat Ansible Automation Platform content more efficiently.

## Ansible UI

- [==Semaphore UI== 🌟](https://www.semui.co/)
- [thenewstack.io: How to Put a GUI on Ansible, Using Semaphore](https://thenewstack.io/how-to-put-a-gui-on-ansible-using-semaphore/) Ansible can be great for automating routine IT tasks, but some may feel stymied by the command line. Here's how to install the Semaphore graphical user interface.

## Deploying custom files with Jinja2 templates

- [infraxpertzz.com: Deploying Custom Files with Jinja2 Template 🌟](https://infraxpertzz.com/deploying-custom-files-with-jinja2-template/) - [video](https://www.youtube.com/watch?app=desktop&v=jokfVGdhBow&feature=youtu.be&ab_channel=InfraXpertzz)
- [jinja 🌟](https://github.com/pallets/jinja/) Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

## Writing an Ansible module

- [docs.ansible.com: Developing Ansible modules](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
- [techforce1.nl: Creating your first Ansible module](https://techforce1.nl/creating-your-first-ansible-module)

## Interacting with REST API

- [linuxctl.com: Ansible - Interacting with external REST API](https://linuxctl.com/2017/01/ansible---interacting-with-external-rest-api/) Ansible has many powerful modules. One of which is called uri which is capable of sending any kind of HTTP request. Using this module, it is fairly simple to allow ansible to intelligently talk to a REST API. This will come in handy during for automation of the sensu monitoring docker infrastructure I am currently working on.
- [steampunk.si: Let us give Ansible a REST](https://steampunk.si/blog/let-us-give-ansible-a-rest/)
- [netways.de: Ansible puede hablar con tu API favorita](https://www.netways.de/blog/2019/04/26/ansible-can-talk-to-your-favorite-api/)
- [redhat.com: Using Ansible to interact with web endpoints](https://www.redhat.com/sysadmin/ansible-web-endpoints) How about an Ansible use case that you can implement today?
- [opensource.com: Using Ansible with REST APIs](https://opensource.com/article/21/9/ansible-rest-apis) You may have queried APIs with a web browser or curl, but one of the overlooked capabilities of Ansible is how well it can leverage APIs as part of any playbook.

### Writing an Ansible module for a REST API

- [ansible.com: Automating your business application's REST API with Ansible](https://www.ansible.com/automating-business-applications-rest-api) You will learn how you can use Ansible to talk to your business application's REST API - and to develop your own Ansible modules doing just that.
- [liquidat.wordpress.com: [Howto] Writing an Ansible module for a REST API](https://liquidat.wordpress.com/2016/06/27/howto-writing-an-ansible-module-for-a-rest-api/)

## Ansible Videos

- [youtube playlist: Ansible Tutorial - by Thetips4you 🌟](https://www.youtube.com/playlist?list=PLVx1qovxj-al0Knm1A0eEXfGyd5kCi16p)
- [youtube playlist: Ansible Tutorial - by Infra Xpertzz 🌟](https://www.youtube.com/playlist?list=PLOwxB_PX3s3WSfhzVtwhxXwy7QpkmtnzR)
    - [youtube.com: Ansible Tutorial Part 8 - Implementing Handlers and Handling Task Failures](https://www.youtube.com/watch?v=pJFZ5h9fT5o&ab_channel=InfraXpertzz)
- [youtube: Ansible for beginners - by XavkiEn](https://www.youtube.com/playlist?list=PLWZKNB9waqIXEL-NIapWwIADPtkspe9vk) - [slides](https://gitlab.com/xavki/devopsland/-/tree/master/ansible)
    - [youtube: Exercises / Monitoring : How to install node exporter 🌟](https://www.youtube.com/watch?v=NgRuap0MmZw&ab_channel=XavkiEn) In this tutorial, we start an exercise to install a monitoring stack. This exercise allows you to add prometheus + grafana on 1 server and node-exporter on all servers.

## Ansible Playbooks

- [github.com/k3s-io/k3s-ansible 🌟](https://github.com/k3s-io/k3s-ansible) Build a Kubernetes cluster using Ansible with k3s.
- [github.com/PyratLabs/ansible-role-k3s 🌟](https://github.com/PyratLabs/ansible-role-k3s) Ansible role for installing k3s as either a standalone server or HA cluster.
- [developers.redhat.com: Set up mod_cluster for Red Hat JBoss Web Server with Ansible](https://developers.redhat.com/articles/2021/09/28/set-modcluster-red-hat-jboss-web-server-ansible)
- [==middlewareinventory.com: Ansible Playbook Examples – Sample Ansible Playbooks | Devops Junction==](https://www.middlewareinventory.com/blog/ansible-playbook-example/)

## Ansible Collections

- [Ansible Collections 🌟](https://github.com/ansible-collections)
- [Amazon AWS Collection 🌟](https://github.com/ansible-collections/amazon.aws)
- [Radware/radware-ansible: Radware Ansible Collection](https://github.com/Radware/radware-ansible)
- [ansible.com: Fundamentals of Network Automation with Ansible Validated Content using the network.base collection](https://www.ansible.com/blog/based-validated-network-content) Ansible validated content is use cases-focused automation packaged as Collections. They include plugins, roles and playbooks that can be used as an automation job through RedHat Ansible Automation Platform. Here's how to use the network.base Collection.

## Red Hat Ansible Automation Platform

- [redhat.com: Red Hat Ansible Automation Platform Enhancements and New Certified Ansible Content Collections Refine the Automation Experience to Drive Business Imperatives](https://www.redhat.com/en/about/press-releases/red-hat-ansible-automation-platform-enhancements-and-new-certified-ansible-content-collections-refine-automation-experience-drive-business-imperatives) Ready-to-use, curated automation for a wide range of platforms, public clouds, network and security technologies help organizations more easily get started with the latest trusted automation
- [ansible.com: Red Hat Ansible Automation Platform 1.2](https://www.ansible.com/blog/now-available-red-hat-ansible-automation-platform-1.2)
- [pypi.org: ansible-navigator 🌟](https://pypi.org/project/ansible-navigator/) A text-based user interface (TUI) for the Red Hat Ansible Automation Platform
- [ansible.com: Introducing Ansible Automation Platform 2](https://www.ansible.com/blog/introducing-ansible-automation-platform-2)
- [redhat.com: From the datacenter to the edge: The open hybrid cloud vision for Red Hat Ansible Automation Platform 2](https://www.redhat.com/en/blog/datacenter-edge-open-hybrid-cloud-vision-red-hat-ansible-automation-platform-2)
- [redhat.com: Redefining the possibilities of IT automation across your ecosystem with Red Hat partners](https://www.redhat.com/en/blog/redefining-possibilities-it-automation-across-your-ecosystem-red-hat-partners)
- [crn.com: IBM’s Red Hat Reveals Ansible Automation Platform 2 Early Access](https://www.crn.com/news/cloud/ibm-s-red-hat-reveals-ansible-automation-platform-2-early-access) ‘Automation is foundational. Not an option. Not tactical,’ Massimo Ferrari, Red Hat’s management strategy director, tells CRN in an interview. “You need automation, otherwise you won‘t be able to do many other things, whether that be DevOps, whether that be digital transformation.”
- [devops.com: Red Hat Extends Scope of Ansible Automation Ambitions](https://devops.com/red-hat-extends-scope-of-ansible-automation-ambitions/) Red Hat announced the availability of a preview edition of Red Hat Ansible Automation Platform 2 that is intended to make it easier to automate IT processes at scale.
- [redhat.com: Red Hat Ansible Automation Platform 2 Drives Cloud-Native Automation and Helps Developers Become Automators](https://www.redhat.com/en/about/press-releases/red-hat-ansible-automation-platform-2-drives-cloud-native-automation-and-helps-developers-become-automators) Industry’s leading IT automation platform now re-architected for deploying portable automation at massive scale across hybrid clouds and edge environments while shifting automation left into application development
- [ansible.com: What's new in Ansible Automation Platform 2: automation controller](https://www.ansible.com/blog/whats-new-in-ansible-automation-platform-2-automation-controller)
    - [ansible.com: What's new in Ansible Automation Platform 2: automation content navigator](https://www.ansible.com/blog/whats-new-in-ansible-automation-platform-2-automation-content-navigator)
- [venturebeat.com: Red Hat brings Ansible IT automation engine to Azure](https://venturebeat.com/2021/12/08/red-hat-brings-its-ansible-it-automation-engine-to-azure/)
- [redhat.com: Red Hat Brings Industry-Leading Ansible Automation Platform to **Microsoft Azure**](https://www.redhat.com/en/about/press-releases/red-hat-brings-industry-leading-ansible-automation-platform-microsoft-azure) Customers can more easily automate across hybrid clouds, IoT and edge deployments with Red Hat Ansible Automation Platform on Microsoft Azure
- [==redhat.com: Red Hat Ansible Automation Platform 2 (ebook)==](https://www.redhat.com/en/resources/ansible-automation-platform-2-ebook)
- [wraltechwire.com: Red Hat expands hybrid cloud efforts in Ansible deal with Microsoft Azure](https://www.wraltechwire.com/2021/12/11/red-hat-expands-hybrid-cloud-efforts-in-ansible-deal-with-microsoft-azure/)

### Automation services catalog

- [ansible.com: Automation services catalog, the newest addition to the Ansible Automation Platform](https://www.ansible.com/products/automation-services-catalog) Provide lifecycle management, provisioning, retirement and cataloging of automation resources to your business

### Red Hat Certified Ansible Content Collections

- [ansible.com: Now Available: Red Hat-Maintained Content Collections on Automation Hub](https://www.ansible.com/blog/now-available-the-new-ansible-content-collections-on-automation-hub)
- [List of Red Hat Supported Maintained Ansible Collections 🌟](https://access.redhat.com/articles/4993781)
- [ansible.com: Automating Red Hat Satellite with Ansible](https://www.ansible.com/blog/automating-red-hat-satellite-with-ansible)
    - [galaxy.ansible.com: letsencrypt](https://galaxy.ansible.com/t_systems_mms/letsencrypt) This collection contains a role for issuing ssl certificates from Let's Encrypt via dns or http-challenge
- [opensource.com: 5 tips for choosing an Ansible collection that's right for you](https://opensource.com/article/21/3/ansible-collections) Try these strategies to find and vet collections of Ansible plugins and modules before you install them.
- [ansible.com: Announcing the Red Hat Enterprise Linux Certified Ansible Collection 🌟](https://www.ansible.com/blog/announcing-the-red-hat-enterprise-linux-certified-ansible-collection)
- [youtube: Ansible Collections 🌟](https://www.youtube.com/watch?app=desktop&v=AXnDrGgLaF0&feature=share&ab_channel=RobertdeBock)

## Ansible Cheat Sheets

- [Ansible Cheat Sheets](cheatsheets.md)

## Running Ansible Playbooks

- [docs.ansible.com: Working With Playbooks](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html)
- [linuxtechi.com: How to Use Loops in Ansible Playbook](https://www.linuxtechi.com/how-to-use-loops-in-ansible-playbook/)
- [Ansible Let's Encrypt Collection](https://blog.t-systems-mms.com/tech-insights/ansible-lets-encrypt-collection)
- [redhat.com: 6 troubleshooting skills for Ansible playbooks 🌟](https://www.redhat.com/sysadmin/troubleshoot-ansible-playbooks) Here are six ways you can check for problems when running Ansible playbooks.
- [redhat.com: How to pass extra variables to an Ansible playbook](https://www.redhat.com/sysadmin/extra-variables-ansible-playbook) Learn how to pass variables to your Ansible playbooks makes them more portable and flexible.

### Running Ansible Playbooks From Jenkins

- [Dzone: Running Ansible Playbooks From Jenkins](https://dzone.com/articles/running-ansible-playbooks-from-jenkins)
- [itnext.io: Ansible and Jenkins — automate your scritps 🌟](https://itnext.io/ansible-and-jenkins-automate-your-scritps-8dff99ef653)

### Ansible Tower and Ansible AWX. Running Ansible Playbooks From Ansible Tower

- [Ansible Tower](https://www.ansible.com/products/tower)
- [Ansible Tower Docs](https://docs.ansible.com/ansible-tower/index.html)
- [Ansible AWX](https://github.com/ansible/awx)
- [AWX Operator](https://github.com/ansible/awx-operator) An Ansible AWX operator for Kubernetes built with Operator SDK and Ansible.
- [ansible.com/blog/topic/ansible-tower](https://www.ansible.com/blog/topic/ansible-tower)
- [Red Hat Ansible Tower Monitoring: Using Prometheus + Node Exporter + Grafana](https://www.ansible.com/blog/red-hat-ansible-tower-monitoring-using-prometheus-node-exporter-grafana)
- [linuxsysadmins.com: Install Ansible AWX on Kubernetes in 5 minutes](https://www.linuxsysadmins.com/install-ansible-awx-on-kubernetes/)
- [steampunk.si: Managing infrastructure using Ansible Tower](https://steampunk.si/blog/managing-infrastructure-using-ansible-tower/)
- [maquinasvirtuales.eu: Docker Swarm: Instalar Ansible AWX](https://www.maquinasvirtuales.eu/docker-swarm-instalar-ansible-awx/)
- [miquelmariano.github.io: Instalación de Ansible AWX sobre Centos 7 con Docker](https://miquelmariano.github.io/2020/01/15/instalacion-ansible-awx-docker-centos7/)
- [techsupportpk.com: Install Ansible AWX on CentOS, RHEL 7, 8](https://www.techsupportpk.com/2020/03/how-to-install-ansible-awx-centos-rhel-7-8.html)
- [developer.ibm.com: Automating IT infrastructure using Ansible and AWX](https://developer.ibm.com/technologies/systems/articles/automation-using-ansible-awx-gui/)
- [medium: Ansible AWX: from scratch to REST API (part 4 of 8)](https://medium.com/@claudio.domingos/ansible-awx-from-scratch-to-rest-api-part-4-of-8-4aa860d823f6) Playbook to automate AWX REST API interactions

#### Tower and AWX Installers

- [galaxy.ansible.com/geerlingguy/awx 🌟](https://galaxy.ansible.com/geerlingguy/awx) Installs and configures AWX (Ansible Tower's open source version).
- [AWX Ansible Collection: galaxy.ansible.com/awx/awx](https://galaxy.ansible.com/awx/awx) This Ansible collection allows for easy interaction with an AWX server via Ansible playbooks.
- [vagrant: ansible tower](https://app.vagrantup.com/ansible/boxes/tower)
- [vagrant: centos-awx](https://app.vagrantup.com/krlex/boxes/centos-awx)
- [github.com/tom-256/ansible-awx-packer](https://github.com/tom-256/ansible-awx-packer) ansible awx golden image based amazon linux
- [github.com/scorputty/packer-centos-awx](https://github.com/scorputty/packer-centos-awx) Packer image build code for Ansible AWX (Tower) Vagrant box
- [github.com/jsmartin/ansible-tower-packer](https://github.com/jsmartin/ansible-tower-packer/)
- [artifacthub.io: Helm Charts - AWX](https://artifacthub.io/packages/search?ts_query_web=awx&sort=relevance&page=1)
- [AWS Marketplace (AMIs): AWX/Tower](https://aws.amazon.com/marketplace/search/results?searchTerms=tower)

### Alternatives to Ansible Tower

- [Jenkins](https://www.jenkins.io/)
- [Foreman](https://www.theforeman.org/)
    - [Ansible Modules to manage Foreman and Katello installations](https://galaxy.ansible.com/theforeman/foreman)
    - [Foreman Ansible Modules (FAM)](https://github.com/theforeman/foreman-ansible-modules) Ansible modules for interacting with the Foreman API and various plugin APIs such as Katello.
    - [RFC: Foreman Operations Ansible Collection](https://community.theforeman.org/t/rfc-operations-ansible-collection/20971)
    - [theforeman.org: Updating Foreman inventory with system facts](https://theforeman.org/2021/01/updating-foreman-inventory-with-system-facts.html)
    - [theforeman.org: Foreman 3.0 is here!](https://theforeman.org/2021/09/foreman-30-is-here.html)
- [Rundeck](https://www.rundeck.com/ansible)

## Ansible Kubernetes Operators

- [ansible.com: Fast vs Easy: Benchmarking Ansible Operators for Kubernetes](https://www.ansible.com/blog/fast-vs-easy-benchmarking-ansible-operators-for-kubernetes)

## Ansible Molecule. Development and Testing of Ansible Roles

- [Ansible Molecule](https://molecule.readthedocs.io/) Molecule project is designed to aid in the development and testing of Ansible roles.
- [Molecule Configuration](https://molecule.readthedocs.io/en/latest/configuration.html)
- [jeffgeerling.com: Testing your Ansible roles with Molecule](https://www.jeffgeerling.com/blog/2018/testing-your-ansible-roles-molecule)
- [PDF: Practical Ansible Testing with Molecule](https://www.ansible.com/hubfs//AnsibleFest%20ATL%20Slide%20Decks/Practical%20Ansible%20Testing%20with%20Molecule.pdf)
- [opensource.com: Testing Ansible roles with Molecule](https://opensource.com/article/18/12/testing-ansible-roles-molecule) Learn how to automate your verifications using Python.
- [medium.com: Test driven Development with Ansible using Molecule](https://medium.com/@moep_moep/test-driven-development-with-ansible-using-molecule-3386cef987ac)
- [tomsitcafe.com: How to test Ansible code with Molecule](https://tomsitcafe.com/2023/04/27/how-to-test-ansible-code-with-molecule/)

## Books

- [ansiblefordevops.com](https://www.ansiblefordevops.com/)
- [ansibleforkubernetes.com 🌟](https://www.ansibleforkubernetes.com/)
- [redhat.com: The Automated Enterprise](https://www.redhat.com/en/engage/automated-enterprise-ebook-20171107) Transform your business with an automation platform that unifies your people and processes.
- [github.com/automateyournetwork/automate_your_network: Automate Your Network - John Capobianco - July 1st 2023](https://github.com/automateyournetwork/automate_your_network)

## Ansible Galaxy Roles

- [galaxy.ansible.com](https://galaxy.ansible.com/)
- [galaxy.ansible.com/geerlingguy](https://galaxy.ansible.com/geerlingguy)
- [redhat.com: A brief introduction to Ansible roles for Linux system administration 🌟](https://www.redhat.com/sysadmin/ansible-system-role) In this part one of two articles, learn to use rhel-system-roles with your Ansible deployment to better manage functionality such as network, firewall, SELinux, and more on your Red Hat Enterprise Linux servers.
- [Ansible Role: Docker 🌟](https://github.com/geerlingguy/ansible-role-docker) An Ansible Role that installs Docker on Linux. "My Docker role now supports managing the Docker `daemon.json` file, after years of people asking" (Jeff Geerling)

## More Ansible Roles

- [Tronde/ansible-role-rhel-patchmanagement](https://github.com/Tronde/ansible-role-rhel-patchmanagement) Use Ansible and some custom scripts to deploy advisories and patches to RHEL servers.

## Ansible scripts

- [konstruktoid/ansible-hvault-inventory: Dynamic Ansible inventory using HashiCorp Vault SSH OTP and local password rotation](https://github.com/konstruktoid/ansible-hvault-inventory) Using HashiCorp Vault as a dynamic Ansible inventory and authentication service

## Ansible with Helm

- [medium.com/opstree-technology: Understanding Ansible: Helm diff plugin 🌟](https://medium.com/opstree-technology/ansible-helm-diff-plugin-63e1cda299a3) Here in this blog, we’ll discuss how we can leverage the validate & dry-run option in Ansible with Ansible: Helm diff plugin.
- [docs.ansible.com: kubernetes.core.helm module – Manages Kubernetes packages with the Helm package manager](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_module.html)
- [docs.ansible.com: kubernetes.core.helm_plugin module – Manage Helm plugins](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_plugin_module.html)

## Awesome Ansible

- [https://github.com/jdauphant/awesome-ansible](https://github.com/jdauphant/awesome-ansible)
- [https://github.com/awesome-devops/awesome-ansible](https://github.com/awesome-devops/awesome-ansible)

## Ansible and Public Cloud Guides

- [Public Cloud Guides 🌟](https://docs.ansible.com/ansible/latest/scenario_guides/cloud_guides.html)
- [Ansible to automate Microsoft Azure](https://www.redhat.com/es/about/videos/ansible-automate-microsoft-azure)
- [medium: AWS Configuration with Web Server in EC2 Using Ansible](https://medium.com/@ayushsingh1525/aws-configuration-with-apache-server-in-ec2-using-ansible-2ef61f98872e)

## Ansible Kubernetes Module

- [==docs.ansible.com: kubernetes.core.k8s – Manage Kubernetes (K8s) objects==](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_module.html)
- [adamtheautomator.com: How to Use the Ansible Kubernetes Module](https://adamtheautomator.com/ansible-kubernetes/) The Ansible Kubernetes module allows you to access the full range of Kubernetes APIs and create objects such as deployments, services, and so on. Learn how to use it in this step-by-step tutorial.

## NGINX Core Collection for Ansibe

- [galaxy.ansible.com/nginxinc/nginx_core](https://galaxy.ansible.com/nginxinc/nginx_core)
- [nginx.com: Announcing the NGINX Core Collection for Ansible](https://www.nginx.com/blog/announcing-nginx-core-collection-ansible/)

## Dynatrace with Ansible

- [dynatrace.com: Achieve faster time to value by deploying thousands of OneAgents at once with Ansible (Preview)](https://www.dynatrace.com/news/blog/achieve-faster-time-to-value-by-deploying-thousands-of-oneagents-at-once-with-ansible-preview/)

## SQL Server with Ansible

- [redhat.com: Using Ansible to deploy Microsoft SQL Server 2019 on Red Hat Enterprise Linux 8](https://www.redhat.com/sysadmin/mssql-linux-easy)

## OCI Oracle Cloud Infrastructure with Ansible

- [oci-ansible-collection.readthedocs.io](https://oci-ansible-collection.readthedocs.io/)

## Oracle Database with Ansible

- [github.com/oravirt/ansible-oracle](https://github.com/oravirt/ansible-oracle)
- [github.com/oravirt/ansible-oracle-modules](https://github.com/oravirt/ansible-oracle-modules) Oracle modules for Ansible
- [oravirt.wordpress.com: Getting started with ansible-oracle](https://oravirt.wordpress.com/2014/10/01/getting-started-with-ansible-oracle/)
- [oravirt.wordpress.com: Changes in ansible-oracle v1.2](https://oravirt.wordpress.com/2014/11/05/changes-in-ansible-oracle-v1-2/)
- [github.com/abessifi/ansible-sqlplus](https://github.com/abessifi/ansible-sqlplus) Ansible role to install sqlplus tool to connect to an Oracle database server
- [stackoverflow.com: Ansible playbook to execute Oracle script](https://stackoverflow.com/questions/41796466/ansible-playbook-to-execute-oracle-script)
- [stackoverflow.com: Running Oracle SQL scripts with Ansible playbook](https://stackoverflow.com/questions/41341823/running-oracle-sql-scripts-with-ansible-playbook)

## Ansistrano. Deploying applications with Ansible in Capistrano style

- [Ansistrano](https://github.com/ansistrano)
- [Capistrano](https://capistranorb.com/) A remote server automation and deployment tool written in Ruby.

## Anacron and Ansible

- [opensource.com: How I use Ansible and anacron for automation](https://opensource.com/article/21/9/ansible-anacron-automation) With anacron, I can drop scripts and Ansible playbooks into place for all manner of trivial tasks.
- [opensource.com: Use anacron for a better crontab](https://opensource.com/article/21/2/linux-automation) Instead of manually performing repetitive tasks, let Linux do them for you.

## Tweets

??? note "Click to expand!"

    <center>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">How to manage Windows hosts with Ansible!<br><br>A Short Thread 👇 <a href="https://t.co/NGRqym4c91">pic.twitter.com/NGRqym4c91</a></p>&mdash; Rakesh Jain (@devops_tech) <a href="https://twitter.com/devops_tech/status/1629453865308536832?ref_src=twsrc%5Etfw">February 25, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Ansible vs Terraform<br><br>Explaining the differences and the better choice for you!<br><br>A Thread 👇 <a href="https://t.co/maKVIdHXki">pic.twitter.com/maKVIdHXki</a></p>&mdash; Rakesh Jain (@devops_tech) <a href="https://twitter.com/devops_tech/status/1672637966743896066?ref_src=twsrc%5Etfw">June 24, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>

## Videos

??? note "Click to expand!"

	<center>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/1id6ERvfozo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/lhFvMsy6VX8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/goclfp6a2IQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/_TVNCTK808I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/rx4Uh3jv1cA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</center>