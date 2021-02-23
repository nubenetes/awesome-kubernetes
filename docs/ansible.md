# Ansible
- [Configuration Management with Ansible DevOps Tool](#configuration-management-with-ansible-devops-tool)
- [Red Hat Ansible Automation Platform](#red-hat-ansible-automation-platform)
	- [Automation services catalog](#automation-services-catalog)
	- [Red Hat Certified Ansible Content Collections](#red-hat-certified-ansible-content-collections)
- [Ansible Cheat Sheets](#ansible-cheat-sheets)
- [Running Ansible Playbooks](#running-ansible-playbooks)
	- [Running Ansible Playbooks From Jenkins](#running-ansible-playbooks-from-jenkins)
	- [Ansible Tower & Ansible AWX. Running Ansible Playbooks From Ansible Tower](#ansible-tower--ansible-awx-running-ansible-playbooks-from-ansible-tower)
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
* [cloudify.co: Ansible Vs Terraform 🌟](https://cloudify.co/blog/ansible-vs-terraform/)
* [opensource.com: How Ansible got started and grew](https://opensource.com/article/21/2/ansible-origin-story)
* [ansible.com: Announcing the Community Ansible 3.0.0 Package 🌟](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package)
* [toptechskills.com: Ansible Tutorials & Courses 🌟](https://www.toptechskills.com/ansible-tutorials-courses/) Ansible is an agentless infrastructure as code (IAC) tool that is super effective at configuring cloud and bare metal infrastructure.
	* [toptechskills.com: How to Speed Up Your Ansible Playbooks Over 600% 🌟](https://www.toptechskills.com/ansible-tutorials-courses/speed-up-ansible-playbooks-pipelining-mitogen/)

##  Red Hat Ansible Automation Platform
- [redhat.com: Red Hat Ansible Automation Platform Enhancements and New Certified Ansible Content Collections Refine the Automation Experience to Drive Business Imperatives](https://www.redhat.com/en/about/press-releases/red-hat-ansible-automation-platform-enhancements-and-new-certified-ansible-content-collections-refine-automation-experience-drive-business-imperatives) Ready-to-use, curated automation for a wide range of platforms, public clouds, network and security technologies help organizations more easily get started with the latest trusted automation
- [ansible.com: Red Hat Ansible Automation Platform 1.2](https://www.ansible.com/blog/now-available-red-hat-ansible-automation-platform-1.2)

### Automation services catalog
- [ansible.com: Automation services catalog, the newest addition to the Ansible Automation Platform](https://www.ansible.com/products/automation-services-catalog) Provide lifecycle management, provisioning, retirement and cataloging of automation resources to your business

### Red Hat Certified Ansible Content Collections
- [ansible.com: Now Available: Red Hat-Maintained Content Collections on Automation Hub](https://www.ansible.com/blog/now-available-the-new-ansible-content-collections-on-automation-hub)
- [List of Red Hat Supported Maintained Ansible Collections 🌟](https://access.redhat.com/articles/4993781)
- [ansible.com: Automating Red Hat Satellite with Ansible](https://www.ansible.com/blog/automating-red-hat-satellite-with-ansible)
	- [galaxy.ansible.com: letsencrypt](https://galaxy.ansible.com/t_systems_mms/letsencrypt) This collection contains a role for issuing ssl certificates from Let's Encrypt via dns or http-challenge

## Ansible Cheat Sheets
* [Ansible Cheat Sheets](cheatsheets.md)

## Running Ansible Playbooks
* [docs.ansible.com: Working With Playbooks](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html)
* [linuxtechi.com: How to Use Loops in Ansible Playbook](https://www.linuxtechi.com/how-to-use-loops-in-ansible-playbook/)
* [Ansible Let's Encrypt Collection](https://blog.t-systems-mms.com/tech-insights/ansible-lets-encrypt-collection)

### Running Ansible Playbooks From Jenkins
* [Dzone: Running Ansible Playbooks From Jenkins](https://dzone.com/articles/running-ansible-playbooks-from-jenkins)
* [itnext.io: Ansible and Jenkins — automate your scritps 🌟](https://itnext.io/ansible-and-jenkins-automate-your-scritps-8dff99ef653)

### Ansible Tower & Ansible AWX. Running Ansible Playbooks From Ansible Tower
* [Ansible Tower](https://www.ansible.com/products/tower)
* [Ansible AWX](https://github.com/ansible/awx)
* [ansible.com/blog/topic/ansible-tower](https://www.ansible.com/blog/topic/ansible-tower)
* [Red Hat Ansible Tower Monitoring: Using Prometheus + Node Exporter + Grafana](https://www.ansible.com/blog/red-hat-ansible-tower-monitoring-using-prometheus-node-exporter-grafana)
* [linuxsysadmins.com: Install Ansible AWX on Kubernetes in 5 minutes](https://www.linuxsysadmins.com/install-ansible-awx-on-kubernetes/)
* [steampunk.si: Managing infrastructure using Ansible Tower](https://steampunk.si/blog/managing-infrastructure-using-ansible-tower/)

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

## Ansistrano. Deploying applications with Ansible in Capistrano style
- [Ansistrano](https://github.com/ansistrano) 
- [Capistrano](https://capistranorb.com/) A remote server automation and deployment tool written in Ruby.

