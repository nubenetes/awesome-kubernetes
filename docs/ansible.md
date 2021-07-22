# Ansible
- [Configuration Management with Ansible DevOps Tool](#configuration-management-with-ansible-devops-tool)
- [Deploying custom files with Jinja2 templates](#deploying-custom-files-with-jinja2-templates)
- [Interview Questions](#interview-questions)
- [Ansible Videos](#ansible-videos)
- [Ansible Collections](#ansible-collections)
- [Red Hat Ansible Automation Platform](#red-hat-ansible-automation-platform)
	- [Automation services catalog](#automation-services-catalog)
	- [Red Hat Certified Ansible Content Collections](#red-hat-certified-ansible-content-collections)
- [Ansible Cheat Sheets](#ansible-cheat-sheets)
- [Running Ansible Playbooks](#running-ansible-playbooks)
	- [Running Ansible Playbooks From Jenkins](#running-ansible-playbooks-from-jenkins)
	- [Ansible Tower and Ansible AWX. Running Ansible Playbooks From Ansible Tower](#ansible-tower-and-ansible-awx-running-ansible-playbooks-from-ansible-tower)
		- [Tower and AWX Installers](#tower-and-awx-installers)
	- [Alternatives to Ansible Tower](#alternatives-to-ansible-tower)
- [Ansible Molecule. Development and Testing of Ansible Roles](#ansible-molecule-development-and-testing-of-ansible-roles)
- [Books](#books)
- [Ansible Galaxy Roles](#ansible-galaxy-roles)
- [Awesome Ansible](#awesome-ansible)
- [Ansible and Public Cloud Guides](#ansible-and-public-cloud-guides)
- [Ansible Kubernetes Module](#ansible-kubernetes-module)
- [NGINX Core Collection for Ansibe](#nginx-core-collection-for-ansibe)
- [Dynatrace with Ansible](#dynatrace-with-ansible)
- [SQL Server with Ansible](#sql-server-with-ansible)
- [OCI Oracle Cloud Infrastructure with Ansible](#oci-oracle-cloud-infrastructure-with-ansible)
- [Oracle Database with Ansible](#oracle-database-with-ansible)
- [Ansistrano. Deploying applications with Ansible in Capistrano style](#ansistrano-deploying-applications-with-ansible-in-capistrano-style)

## Configuration Management with Ansible DevOps Tool
* [ansible.com](https://www.ansible.com/)
* [docs.ansible.com](https://docs.ansible.com/)
* [dureka.co: What Is Ansible?](https://www.edureka.co/blog/what-is-ansible/) Configuration Management And Automation With Ansible
* [Dzone: Getting Started With Ansible](https://dzone.com/articles/getting-started-with-ansible)
* [Dzone: Part 1: Getting Started with Ansible](https://dzone.com/articles/part-1-getting-started-ansible)
* [Dzone: Part 2: Deploying Applications](https://dzone.com/articles/part-2-deploying-applications)
* [Dzone: 10 easy to use modules in ansible](https://dzone.com/articles/10-easy-to-use-modules-in-ansible-1)
* [Dzone: Ansible: An Effective IT Automation Tool](https://dzone.com/articles/ansible-an-effective-it-automation-tool) Learn about Ansible, a tool for automating application deployments, configuration management, and more in a DevOps environment.
* [Dzone: Running Ansible at Scale](https://dzone.com/articles/running-ansible-at-scale)
* [Udemy.com: Ansible Essentials: Simplicity in Automation (Free Tutorial)](https://www.udemy.com/ansible-essentials-simplicity-in-automation)
* [Deployment of Microservices in Cloud With Ansible](https://medium.com/avmconsulting-blog/deploying-microservices-via-ansible-in-cloud-platform-a03d46b7bd68) This tutorial will help you understand how Ansible orchestrates Docker containers at least for a dev environment
* [opensource.com: How to install software with Ansible](https://opensource.com/article/20/9/install-packages-ansible) Automate software installations and updates across your devices with Ansible playbooks.
* [opensource.com: Automate your container orchestration with Ansible modules for Kubernetes 🌟](https://opensource.com/article/20/9/ansible-modules-kubernetes) Combine Ansible with Kubernetes for cloud automation. Plus, get our cheat sheet for using the Ansible k8s module.
* [opensource.com: A quickstart guide to Ansible 🌟](https://opensource.com/article/19/2/quickstart-guide-ansible) Download the Ansible Automation for SysAdmins guide.
* [opensource.com: 7 things you can do with Ansible right now](https://opensource.com/article/20/9/ansible) If Ansible's inclusion as a leader on the Forrester Wave report piqued your interest, here are some ways the automation solution can simplify your life.
* [medium.com: The Ultimate Guide for Ansible Total Domination 🌟](https://medium.com/the-programming-hub/the-ultimate-guide-for-ansible-total-domination-e70bdfc11175)
* [opensource.com: Integrate your calendar with Ansible to avoid schedule conflicts 🌟](https://opensource.com/article/20/10/calendar-ansible) Make sure your automation workflow's schedule doesn't conflict with something else by integrating a calendar app into Ansible.
* [opensource.com: My first day using Ansible](https://opensource.com/article/20/10/first-day-ansible) A sysadmin shares information and advice about putting Ansible into real-world use configuring computers on his network.
* [siliconangle.com: Red Hat ties Ansible automation to Kubernetes cluster management 🌟](https://siliconangle.com/2020/10/13/red-hat-ties-ansible-automation-kubernetes-cluster-management/)
* [sdxcentral.com: Red Hat Links Ansible Automation to Kubernetes Management 🌟](https://www.sdxcentral.com/articles/news/red-hat-links-ansible-automaton-to-kubernetes-management/)
* [thenewstack.io: Red Hat Brings Ansible Automation to Kubernetes 🌟](https://thenewstack.io/red-hat-brings-ansible-automation-to-kubernetes/)
* [openshift.com: Ansible and OpenShift: Connecting for Success 🌟](https://www.openshift.com/blog/ansible-and-openshift-connecting-for-success)
* [zdnet.com: ed Hat expands Ansible ready to run cloud programs 🌟](https://www.zdnet.com/article/red-hat-expands-ansible-ready-to-run-cloud-programs/) And, on top of more plug-and-play Ansible programs, you can now run Ansible hand-in-glove with Red Hat OpenShift.
* [theregister.com: Juggling Ansible, OpenShift and K8s? This is for you: Red Hat couples automation to cluster management](https://www.theregister.com/2020/10/14/redhat_ansible_kubernetes/) 
* [redhat.com: Ansible Essentials: Simplicity in Automation Technical Overview (Free Course) 🌟](https://www.redhat.com/en/services/training/do007-ansible-essentials-simplicity-automation-technical-overview)
* [opensource.com: 10 Ansible modules for Linux system automation c](https://opensource.com/article/20/10/ansible-modules-linux) These handy modules save time and hassle by automating many of your daily tasks, and they're easy to implement with a few commands.
* [redhat.com: Renewing my thrill at work with Ansible](https://www.redhat.com/sysadmin/renewed-thrill-ansible) 
* [opensource.com: Set up an Ansible lab in 20 minutes](https://opensource.com/article/20/12/ansible-lab) Build an environment to support learning and experimenting with new software.
* [opensource.com: 4 lines of code to improve your Ansible play](https://opensource.com/article/21/1/improve-ansible-play)
* [redhat.com: Demystifying Ansible for Linux sysadmins 🌟](https://www.redhat.com/sysadmin/demystifying-ansible-sysadmins) Taking the labor out of labor-intensive tasks is what Ansible is all about. Learn the basics here.
	* [redhat.com: Quick start guide to Ansible for Linux sysadmins 🌟](https://www.redhat.com/sysadmin/ansible-quick-start)
* [opensource.com: 10 ways Ansible is for everyone 🌟](https://opensource.com/article/21/1/ansible) Expand your knowledge and skills with the top 10 Ansible articles plus five news summaries from 2020
* [ansible.com: Ansible Network Resource Modules: Deep Dive on Return Values](https://www.ansible.com/blog/ansible-network-resource-modules-deep-dive-on-return-values)
* [linkedin.com: Ansible what is it and what not](https://www.linkedin.com/pulse/ansible-what-marcel-koert/)
* [redhat.com: How to automate system reboots using the Ansible reboot module](https://www.redhat.com/sysadmin/automate-reboot-ansible) 
* [developer.okta.com: Tutorial: Ansible and Account Automation with Okta](https://developer.okta.com/blog/2021/02/05/okta-ansible)
* [redhat.com: Got automation? Here's a quick guide to get you up to speed on Ansible 🌟](https://www.redhat.com/sysadmin/how-start-ansible) This article gives you a quick, high-level guide on how to start with Ansible
* [opensource.com: How Ansible got started and grew](https://opensource.com/article/21/2/ansible-origin-story)
* [ansible.com: Announcing the Community Ansible 3.0.0 Package 🌟](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package)
* [toptechskills.com: Ansible Tutorials & Courses 🌟](https://www.toptechskills.com/ansible-tutorials-courses/) Ansible is an agentless infrastructure as code (IAC) tool that is super effective at configuring cloud and bare metal infrastructure.
	* [toptechskills.com: How to Speed Up Your Ansible Playbooks Over 600% 🌟](https://www.toptechskills.com/ansible-tutorials-courses/speed-up-ansible-playbooks-pipelining-mitogen/)
* [opensource.com: 5 everyday sysadmin tasks to automate with Ansible 🌟](https://opensource.com/article/21/3/ansible-sysadmin) Get more efficient and avoid errors by automating repeatable daily tasks with Ansible.
* [redhat.com: 8 steps to developing an Ansible role in Linux 🌟](https://www.redhat.com/sysadmin/developing-ansible-role) In this article, an existing Ansible playbook is used to deploy Vim and convert it to a role adding flexibility and reusability.
* [ansible.com: Ansible whitepaper](https://www.ansible.com/resources/whitepapers/ansible-in-depth) Download this paper for a deep dive into Ansible, an open source IT configuration management, deployment, and orchestration tool.
* [redhat.slides.com: Ansible 202 - Best Practices from the field](http://redhat.slides.com/jparrill/ansible-202/fullscreen?token=1hUEEPF4#/11/1) - [asciinema.org/~padajuan](https://asciinema.org/~padajuan)
* [redhat.com: How to use Ansible to send an email using Gmail](https://www.redhat.com/sysadmin/configure-gmail-using-ansible)
* [redhat.com: How to use Ansible to configure a reverse proxy 🌟](https://www.redhat.com/sysadmin/reverse-proxy-ansible) Placing a load balancer in front of your web server infrastructure helps ensure any spike in traffic doesn't bring down the site.
* [Ansible 3.3.0 released](https://groups.google.com/g/ansible-devel/c/CdQ7eWUUm8k?pli=1)
* [fedoramagazine.org: Using Ansible to configure Podman containers 🌟](https://fedoramagazine.org/using-ansible-to-configure-podman-containers/)
* [acloudguru.com: Ansible vs Puppet: Which is right for you?](https://acloudguru.com/blog/engineering/ansible-vs-puppet-which-is-right-for-you)
* [redhat.com: Add a repo and install a package the Ansible way](https://www.redhat.com/sysadmin/install-ansible-way) How to add package repositories and install packages on many hosts by using Ansible.
* [automateinfra.com: Everything about Ansible 🌟](https://automateinfra.com/everything-about-ansible/)
* [redhat.com: Introduction to RHEL System Roles 🌟](https://www.redhat.com/en/blog/introduction-rhel-system-roles) How to use Ansible Roles with RedHat Enterprise Linux 
* [linuxtechlab.com: Ansible Tutorial: Introduction to simple Ansible commands](https://linuxtechlab.com/ansible-tutorial-simple-commands/)
* [k21academy.com: Ansible for Beginners | Overview | Architecture & Use Cases](https://k21academy.com/ansible/ansible-for-beginners)
* [analyticsindiamag.com: Ansible vs Docker: A Detailed Comparison Of DevOps Tools](https://analyticsindiamag.com/ansible-vs-docker-a-detailed-comparison-of-devops-tools)
* [redhat.com: 6 steps to automating code pushes with Ansible Automation Platform 🌟](https://www.redhat.com/sysadmin/6-code-pushes-aap) Use a Git push to trigger an Ansible Automation Platform playbook execution in six easy steps.
* [redhat.com: 4 steps to create Linux users from a csv file with Ansible](https://www.redhat.com/sysadmin/ansible-create-users-csv) Automate Linux user account creation in four simple steps with Ansible.

## Deploying custom files with Jinja2 templates
- [infraxpertzz.com: Deploying Custom Files with Jinja2 Template 🌟](https://infraxpertzz.com/deploying-custom-files-with-jinja2-template/) - [video](https://www.youtube.com/watch?app=desktop&v=jokfVGdhBow&feature=youtu.be&ab_channel=InfraXpertzz)
- [jinja 🌟](https://github.com/pallets/jinja/) Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

## Interview Questions
- [devsecops.co.in: 100+ Ansible Interview Questions and Answers](https://devsecops.co.in/2021/05/18/ansible-interview-questions/)

## Ansible Videos
* [youtube playlist: Ansible Tutorial - by Thetips4you 🌟](https://www.youtube.com/playlist?list=PLVx1qovxj-al0Knm1A0eEXfGyd5kCi16p)
* [youtube playlist: Ansible Tutorial - by Infra Xpertzz 🌟](https://www.youtube.com/playlist?list=PLOwxB_PX3s3WSfhzVtwhxXwy7QpkmtnzR)
	* [youtube.com: Ansible Tutorial Part 8 - Implementing Handlers and Handling Task Failures](https://www.youtube.com/watch?v=pJFZ5h9fT5o&ab_channel=InfraXpertzz)
* [youtube: Ansible for beginners - by XavkiEn](https://www.youtube.com/playlist?list=PLWZKNB9waqIXEL-NIapWwIADPtkspe9vk) - [slides](https://gitlab.com/xavki/devopsland/-/tree/master/ansible)
	* [youtube: Exercises / Monitoring : How to install node exporter 🌟](https://www.youtube.com/watch?v=NgRuap0MmZw&ab_channel=XavkiEn) In this tutorial, we start an exercise to install a monitoring stack. This exercise allows you to add prometheus + grafana on 1 server and node-exporter on all servers.

## Ansible Collections
- [Ansible Collections 🌟](https://github.com/ansible-collections)
- [Amazon AWS Collection 🌟](https://github.com/ansible-collections/amazon.aws)

##  Red Hat Ansible Automation Platform
- [redhat.com: Red Hat Ansible Automation Platform Enhancements and New Certified Ansible Content Collections Refine the Automation Experience to Drive Business Imperatives](https://www.redhat.com/en/about/press-releases/red-hat-ansible-automation-platform-enhancements-and-new-certified-ansible-content-collections-refine-automation-experience-drive-business-imperatives) Ready-to-use, curated automation for a wide range of platforms, public clouds, network and security technologies help organizations more easily get started with the latest trusted automation
- [ansible.com: Red Hat Ansible Automation Platform 1.2](https://www.ansible.com/blog/now-available-red-hat-ansible-automation-platform-1.2)
- [pypi.org: ansible-navigator 🌟](https://pypi.org/project/ansible-navigator/) A text-based user interface (TUI) for the Red Hat Ansible Automation Platform

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
* [Ansible Cheat Sheets](cheatsheets.md)

## Running Ansible Playbooks
* [docs.ansible.com: Working With Playbooks](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html)
* [linuxtechi.com: How to Use Loops in Ansible Playbook](https://www.linuxtechi.com/how-to-use-loops-in-ansible-playbook/)
* [Ansible Let's Encrypt Collection](https://blog.t-systems-mms.com/tech-insights/ansible-lets-encrypt-collection)
* [redhat.com: 6 troubleshooting skills for Ansible playbooks 🌟](https://www.redhat.com/sysadmin/troubleshoot-ansible-playbooks) Here are six ways you can check for problems when running Ansible playbooks.
* [redhat.com: How to pass extra variables to an Ansible playbook](https://www.redhat.com/sysadmin/extra-variables-ansible-playbook) Learn how to pass variables to your Ansible playbooks makes them more portable and flexible.

### Running Ansible Playbooks From Jenkins
* [Dzone: Running Ansible Playbooks From Jenkins](https://dzone.com/articles/running-ansible-playbooks-from-jenkins)
* [itnext.io: Ansible and Jenkins — automate your scritps 🌟](https://itnext.io/ansible-and-jenkins-automate-your-scritps-8dff99ef653)

### Ansible Tower and Ansible AWX. Running Ansible Playbooks From Ansible Tower
* [Ansible Tower](https://www.ansible.com/products/tower)
* [Ansible Tower Docs](https://docs.ansible.com/ansible-tower/index.html)
* [Ansible AWX](https://github.com/ansible/awx)
* [AWX Operator](https://github.com/ansible/awx-operator) An Ansible AWX operator for Kubernetes built with Operator SDK and Ansible. 
* [ansible.com/blog/topic/ansible-tower](https://www.ansible.com/blog/topic/ansible-tower)
* [Red Hat Ansible Tower Monitoring: Using Prometheus + Node Exporter + Grafana](https://www.ansible.com/blog/red-hat-ansible-tower-monitoring-using-prometheus-node-exporter-grafana)
* [linuxsysadmins.com: Install Ansible AWX on Kubernetes in 5 minutes](https://www.linuxsysadmins.com/install-ansible-awx-on-kubernetes/)
* [steampunk.si: Managing infrastructure using Ansible Tower](https://steampunk.si/blog/managing-infrastructure-using-ansible-tower/)
* [maquinasvirtuales.eu: Docker Swarm: Instalar Ansible AWX](https://www.maquinasvirtuales.eu/docker-swarm-instalar-ansible-awx/)
* [miquelmariano.github.io: Instalación de Ansible AWX sobre Centos 7 con Docker](https://miquelmariano.github.io/2020/01/15/instalacion-ansible-awx-docker-centos7/)
* [techsupportpk.com: Install Ansible AWX on CentOS, RHEL 7, 8](https://www.techsupportpk.com/2020/03/how-to-install-ansible-awx-centos-rhel-7-8.html)
* [developer.ibm.com: Automating IT infrastructure using Ansible and AWX](https://developer.ibm.com/technologies/systems/articles/automation-using-ansible-awx-gui/)

#### Tower and AWX Installers
* [galaxy.ansible.com/geerlingguy/awx 🌟](https://galaxy.ansible.com/geerlingguy/awx) Installs and configures AWX (Ansible Tower's open source version).
* [AWX Ansible Collection: galaxy.ansible.com/awx/awx](https://galaxy.ansible.com/awx/awx) This Ansible collection allows for easy interaction with an AWX server via Ansible playbooks.
* [vagrant: ansible tower](https://app.vagrantup.com/ansible/boxes/tower)
* [vagrant: centos-awx](https://app.vagrantup.com/krlex/boxes/centos-awx)
* [github.com/tom-256/ansible-awx-packer](https://github.com/tom-256/ansible-awx-packer) ansible awx golden image based amazon linux
* [github.com/scorputty/packer-centos-awx](https://github.com/scorputty/packer-centos-awx) Packer image build code for Ansible AWX (Tower) Vagrant box
* [github.com/jsmartin/ansible-tower-packer](https://github.com/jsmartin/ansible-tower-packer/)
* [artifacthub.io: Helm Charts - AWX](https://artifacthub.io/packages/search?ts_query_web=awx&sort=relevance&page=1)
* [AWS Marketplace (AMIs): AWX/Tower](https://aws.amazon.com/marketplace/search/results?searchTerms=tower)

### Alternatives to Ansible Tower
* [Jenkins](https://www.jenkins.io/)
* [Foreman](https://www.theforeman.org/)
    * [Ansible Modules to manage Foreman and Katello installations](https://galaxy.ansible.com/theforeman/foreman)
    * [Foreman Ansible Modules (FAM)](https://github.com/theforeman/foreman-ansible-modules) Ansible modules for interacting with the Foreman API and various plugin APIs such as Katello.
    * [RFC: Foreman Operations Ansible Collection](https://community.theforeman.org/t/rfc-operations-ansible-collection/20971)
    * [theforeman.org: Updating Foreman inventory with system facts](https://theforeman.org/2021/01/updating-foreman-inventory-with-system-facts.html)
* [Rundeck](https://www.rundeck.com/ansible)

## Ansible Molecule. Development and Testing of Ansible Roles
* [Ansible Molecule](https://molecule.readthedocs.io/) Molecule project is designed to aid in the development and testing of Ansible roles.
* [Molecule Configuration](https://molecule.readthedocs.io/en/latest/configuration.html)
* [jeffgeerling.com: Testing your Ansible roles with Molecule](https://www.jeffgeerling.com/blog/2018/testing-your-ansible-roles-molecule)
* [PDF: Practical Ansible Testing with Molecule](https://www.ansible.com/hubfs//AnsibleFest%20ATL%20Slide%20Decks/Practical%20Ansible%20Testing%20with%20Molecule.pdf)
* [opensource.com: Testing Ansible roles with Molecule](https://opensource.com/article/18/12/testing-ansible-roles-molecule) Learn how to automate your verifications using Python.
* [medium.com: Test driven Development with Ansible using Molecule](https://medium.com/@moep_moep/test-driven-development-with-ansible-using-molecule-3386cef987ac)

## Books
* [ansiblefordevops.com](https://www.ansiblefordevops.com/)
* [ansibleforkubernetes.com 🌟](https://www.ansibleforkubernetes.com/)
  
## Ansible Galaxy Roles
- [galaxy.ansible.com](https://galaxy.ansible.com/)
- [galaxy.ansible.com/geerlingguy](https://galaxy.ansible.com/geerlingguy)
- [redhat.com: A brief introduction to Ansible roles for Linux system administration 🌟](https://www.redhat.com/sysadmin/ansible-system-role) In this part one of two articles, learn to use rhel-system-roles with your Ansible deployment to better manage functionality such as network, firewall, SELinux, and more on your Red Hat Enterprise Linux servers.
- [Ansible Role: Docker 🌟](https://github.com/geerlingguy/ansible-role-docker) An Ansible Role that installs Docker on Linux. "My Docker role now supports managing the Docker `daemon.json` file, after years of people asking" (Jeff Geerling)

## Awesome Ansible
* [https://github.com/jdauphant/awesome-ansible](https://github.com/jdauphant/awesome-ansible)
* [https://github.com/awesome-devops/awesome-ansible](https://github.com/awesome-devops/awesome-ansible)

## Ansible and Public Cloud Guides
* [Public Cloud Guides 🌟](https://docs.ansible.com/ansible/latest/scenario_guides/cloud_guides.html)
* [Ansible to automate Microsoft Azure](https://www.redhat.com/es/about/videos/ansible-automate-microsoft-azure)
* [medium: AWS Configuration with Web Server in EC2 Using Ansible](https://medium.com/@ayushsingh1525/aws-configuration-with-apache-server-in-ec2-using-ansible-2ef61f98872e)

## Ansible Kubernetes Module
* [Manage Kubernetes (K8s) objects with Ansible Kubernetes Module](https://docs.ansible.com/ansible/latest/modules/k8s_module.html)

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

