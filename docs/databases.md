# Relational Databases on Kubernetes. Database DevOps
- [Introduction](#introduction)
- [How to choose the right database for your service](#how-to-choose-the-right-database-for-your-service)
- [Database Load Balancer](#database-load-balancer)
- [SQL](#sql)
- [Stored Procedures](#stored-procedures)
- [Performance](#performance)
- [Stateful and Stateless Applications](#stateful-and-stateless-applications)
- [Serverless Databases](#serverless-databases)
- [DataOps](#dataops)
- [Database Continuous Integration](#database-continuous-integration)
- [Databases on Kubernetes](#databases-on-kubernetes)
- [Database DevOps](#database-devops)
- [KubeDB Cloud Native Postgress Database](#kubedb-cloud-native-postgress-database)
- [Cockroach Cloud Native Database](#cockroach-cloud-native-database)
- [Operator Lifecycle Manager (OLM)](#operator-lifecycle-manager-olm)
- [Spilo PostgreSQL Operator](#spilo-postgresql-operator)
- [Zalando PostgreSQL Operator](#zalando-postgresql-operator)
- [Crunchy Data PostgreSQL Operator](#crunchy-data-postgresql-operator)
    - [Crunchy Data Developer Portal](#crunchy-data-developer-portal)
    - [Crunchy Data Postgres Operator in OpenShift 4. Overview & Proof of Concept](#crunchy-data-postgres-operator-in-openshift-4-overview--proof-of-concept)
        - [Crunchydata Postgres Operator 3.5](#crunchydata-postgres-operator-35)
        - [Crunchydata Postgres Operator 4.0.1](#crunchydata-postgres-operator-401)
        - [Crunchydata Postgres Operator 4.0.1 Community Edition](#crunchydata-postgres-operator-401-community-edition)
            - [Service Accounts](#service-accounts)
            - [Roles assigned to Service Accounts](#roles-assigned-to-service-accounts)
            - [Security Context Constraints (SCC)](#security-context-constraints-scc)
                - [SCC Recommendations](#scc-recommendations)
            - [Add a SCC to a Project](#add-a-scc-to-a-project)
                - [Workflow1 without custom Service Account and without DeploymentConfig](#workflow1-without-custom-service-account-and-without-deploymentconfig)
                - [Workflow2 with custom Service Account and without DeploymentConfig](#workflow2-with-custom-service-account-and-without-deploymentconfig)
                - [Workflow3 with custom service Account and DeploymentConfig](#workflow3-with-custom-service-account-and-deploymentconfig)
            - [Environment setup. Port Forward and WSL](#environment-setup-port-forward-and-wsl)
            - [Cluster Deployment and Operation with pgo](#cluster-deployment-and-operation-with-pgo)
            - [Psql access from postgres operator POD](#psql-access-from-postgres-operator-pod)
            - [List Databases with psql](#list-databases-with-psql)
            - [Access from another POD within the cluster with psql client](#access-from-another-pod-within-the-cluster-with-psql-client)
            - [Access from another POD within the cluster with Pgadmin4 of Crunchy containers Community Edition](#access-from-another-pod-within-the-cluster-with-pgadmin4-of-crunchy-containers-community-edition)
            - [Debugging Crunchydata Postgres Operator 4.0.1 Community Edition](#debugging-crunchydata-postgres-operator-401-community-edition)
        - [Certified Crunchydata Postgres Operator (OLM/OperatorHub). Manual Setup](#certified-crunchydata-postgres-operator-olmoperatorhub-manual-setup)
- [Oracle 12c on OpenShift Container Platform](#oracle-12c-on-openshift-container-platform)
- [Oracle Database Operator for Kubernetes](#oracle-database-operator-for-kubernetes)
- [SQL Server](#sql-server)
- [MySQL](#mysql)
- [MariaDB](#mariadb)
- [PostgreSQL](#postgresql)
- [Percona MySQL](#percona-mysql)
- [Percona PostgreSQL Operator](#percona-postgresql-operator)
- [Redis](#redis)
- [Rockset](#rockset)
- [Clickhouse](#clickhouse)
- [Apache Ignite](#apache-ignite)
- [Tools](#tools)
- [Time-Series Database](#time-series-database)
- [Data Analytics and Visualization Tools](#data-analytics-and-visualization-tools)
- [Data Lakes](#data-lakes)
- [Graph Databases](#graph-databases)
- [Tweets](#tweets)

## Introduction
- [thenewstack.io: How Database Load Balancing Completes the 3-Tiered Architecture 🌟](https://thenewstack.io/database-load-balancing-and-the-delusion-of-3-tiered-architecture/)
- [sqlshack.com: SQL Database on Kubernetes: Considerations and Best Practices 🌟](https://www.sqlshack.com/sql-database-on-kubernetes-considerations-and-best-practices/)
- [thenewstack.io: Just How Challenging Is State in Kubernetes? 🌟](https://thenewstack.io/just-how-challenging-is-state-in-kubernetes/)
- [theregister.com: 75% of databases to be cloud-hosted by 2022, says Gartner while dishing on the weak points of each provider](https://www.theregister.com/2020/12/02/gartner_cloud_dbms/)
- [thenewstack.io: What Is Data Management in the Kubernetes Age?](https://thenewstack.io/what-is-data-management-in-the-kubernetes-age/)
- [thenewstack.io: A Case for Databases on Kubernetes from a Former Skeptic](https://thenewstack.io/a-case-for-databases-on-kubernetes-from-a-former-skeptic/)
- [hackernoon.com: Database Vs Data Warehouse Vs Data Lake: A Simple Explanation](https://hackernoon.com/database-vs-data-warehouse-vs-data-lake-a-simple-explanation-hz2k33rm)
* [percona.com: DBaaS on Kubernetes: Under the Hood 🌟](https://www.percona.com/blog/2021/02/08/dbaas-on-kubernetes-under-the-hood/)
* [blog.crunchydata.com: Using Kubernetes? Chances Are You Need a Database 🌟](https://blog.crunchydata.com/blog/using-kubernetes-chances-are-you-need-a-database)
* [thenewstack.io: Databases — Finally — Get Containerized](https://thenewstack.io/databases-finally-get-containerized/)
* [percona.com: Autoscaling Databases in Kubernetes for MongoDB, MySQL, and PostgreSQL](https://www.percona.com/blog/2021/06/23/autoscaling-databases-in-kubernetes-for-mongodb-mysql-and-postgresql/)
* [levelup.gitconnected.com: How to design a system to scale to your first 100 million users](https://levelup.gitconnected.com/how-to-design-a-system-to-scale-to-your-first-100-million-users-4450a2f9703d) Think Big, Do Small, Learn Fast
* [magalix.com: Kubernetes And Databases 🌟](https://www.magalix.com/blog/kubernetes-and-database)
* [towardsdatascience.com: SQL vs. NoSQL: How to Select from 12 Database Types 🌟🌟](https://towardsdatascience.com/datastore-choices-sql-vs-nosql-database-ebec24d56106) When to use SQL vs. NoSQL database? Deep dive, differences, decision tree, and cloud cheatsheet to choose the best database for your data type and use case.
* [andrewlock.net: Running database migrations when deploying to Kubernetes 🌟](https://andrewlock.net/deploying-asp-net-core-applications-to-kubernetes-part-7-running-database-migrations/) Deploying ASP.NET Core applications to Kubernetes - Part 7. Learn how to run database migrations with init containers and Jobs in Kubernetes.
* [redislabs.com: What is a “Databaseless” (DBLess) Architecture, and Why It’s the Future 🌟](https://redislabs.com/blog/dbless-architecture-and-why-its-the-future/) DBLess architecture provides a new approach to data pipeline and backend architecture. Just like the terms serverless, stateless, and NoSQL, it attempts to provide more options for architects to think about.
* [red-gate.com: Designing Highly Scalable Database Architectures](https://www.red-gate.com/simple-talk/databases/sql-server/performance-sql-server/designing-highly-scalable-database-architectures/)
* [dev.to: Introduction Migrations](https://dev.to/mahmoudessa/introduction-migrations-8me)
* [medium: Not using trendy technologies is the best thing for your Startup!](https://medium.com/dataseries/not-using-nosql-is-good-i-stuck-to-sql-4504a67972f0) I refused to use MongoDB and I convinced my company to use a SQL relational database system.
* [thenewstack.io: Database-as-a-Service: A Key Technology for Agile Growth](https://thenewstack.io/database-as-a-service-a-key-technology-for-agile-growth/)
* [cloud.redhat.com: OpenShift Commons Briefing: Database Disaster Recovery Made Easy with Annette Clewett (Red Hat) and Andrew L'Ecuyer (Crunchy Data)](https://cloud.redhat.com/blog/openshift-commons-briefing-database-disaster-recovery-made-easy-with-annette-clewett-red-hat-and-andrew-lecuyer-crunchy-data)
* [thenewstack.io: A Case for Databases on Kubernetes from a Former Skeptic](https://thenewstack.io/a-case-for-databases-on-kubernetes-from-a-former-skeptic)
* [hackernoon.com: Practical Transaction Handling in Microservice Architecture](https://hackernoon.com/practical-transaction-handling-in-microservice-architecture-5x1631ke)
* [thenewstack.io: Data on Kubernetes: Operators, Tools Need Standardization](https://thenewstack.io/data-on-kubernetes-operators-tools-need-standardization/)
* [medium: How to Put a Database in Kubernetes](https://medium.com/building-the-open-data-stack/how-to-put-a-database-in-kubernetes-ab7c21540ec2) For example, a deployment of Apache Cassandra will typically use a StatefulSet to launch pods across available Kubernetes worker nodes, with each Cassandra pod having its own PersistentVolumeClaim that can be preserved and reused if the pod needs to be replaced.
* [thenewstack.io: Kubernetes Will Revolutionize Enterprise Database Management](https://thenewstack.io/kubernetes-will-revolutionize-enterprise-database-management/)
* [dok.community: Data on Kubernetes 2021 Report](https://dok.community/dokc-2021-report/) Standardization, consistency and the ability for developers to self-manage - are among the top 3 important factors in the organization's decision to run stateful workloads on Kubernetes. 
* [cloud.redhat.com: Simplifying Database Cloud Service Access](https://cloud.redhat.com/blog/simplifying-database-cloud-service-access)
* [venturebeat.com: The rise of Kubernetes and its impact on enterprise databases](https://venturebeat.com/2021/11/03/the-rise-of-kubernetes-and-its-impact-on-enterprise-databases/)
* [vladmihalcea.com: Single-Primary Database Replication](https://vladmihalcea.com/single-primary-database-replication/)
* [treblle.com: How does Treblle scale on AWS without breaking the bank?](https://treblle.com/blog/how-does-treblle-scale-on-aws-without-breaking-the-bank) A completely scalable intake solution that didn't require a database because all the data was stored on S3.

## How to choose the right database for your service 
* [medium.com: How to choose the right database for your service 🌟](https://medium.com/wix-engineering/how-to-choose-the-right-database-for-your-service-97b1670c5632)

## Database Load Balancer
- [severalnines.com: How Does a Database Load Balancer Work?](https://severalnines.com/database-blog/how-does-database-load-balancer-work)

## SQL
- [digitalocean.com: How To Use WHERE Clauses in SQL](https://www.digitalocean.com/community/tutorials/how-to-use-where-clauses-in-sql)
- [intellipaat.com: SQL vs MySQL - Key Differences Between SQL and MySQL](https://intellipaat.com/blog/sql-vs-mysql-difference/)
- [vettabase.com: How slow is SELECT * ?](https://vettabase.com/blog/how-slow-is-select/)
- [towardsdatascience.com: How to Use SQL Cross Joins](https://towardsdatascience.com/how-to-use-sql-cross-joins-5653fe7d353) The SQL join you never knew existed
- [vladmihalcea.com: SQL EXISTS and NOT EXISTS](https://vladmihalcea.com/sql-exists/)
- [vladmihalcea.com: Default Database Primary, Foreign, and Unique Key Indexing](https://vladmihalcea.com/default-database-key-indexing/)
- [blog.jooq.org](https://blog.jooq.org) JAVA, SQL AND JOOQ. Best Practices and Lessons Learned from Writing Awesome Java and SQL Code. Get some hands-on insight on what's behind developing jOOQ.

## Stored Procedures
- [blog.yugabyte.com: Are Stored Procedures and Triggers Anti-Patterns in the Cloud Native World?](https://blog.yugabyte.com/are-stored-procedures-and-triggers-anti-patterns-in-the-cloud-native-world/)
- [stackoverflow.com: Is the usage of stored procedures a bad practice?](https://stackoverflow.com/questions/1761601/is-the-usage-of-stored-procedures-a-bad-practice)
- [softwareengineering.stackexchange.com: What is the best practice about microservice architecture for consuming many stored procedures in the same database?](https://softwareengineering.stackexchange.com/questions/436567/what-is-the-best-practice-about-microservice-architecture-for-consuming-many-sto)

## Performance
- [betterprogramming.pub: 8 Techniques To Speed up Your Database](https://betterprogramming.pub/8-techniques-to-speed-up-your-database-292754ff7739) “If everything seems under control, you’re not going fast enough”
## Stateful and Stateless Applications
* [xenonstack.com: Stateful and Stateless Applications Best Practices and Advantages](https://www.xenonstack.com/insights/stateful-and-stateless-applications/)
* [threadreaderapp.com:  Kelsey Hightower: "Kubernetes has made huge improvements in the ability to run stateful workloads including databases and message queues, but I still prefer not to run them on Kubernetes" 🌟](https://threadreaderapp.com/thread/963413508300812295.html)
* [thenewstack.io: Data on Kubernetes: The Next Frontier](https://thenewstack.io/data-on-kubernetes-the-next-frontier/) “The interesting opportunity I see in the Kubernetes ecosystem,” Evenson continued, “is that, with the advent of custom resources and Kubernetes, you can build bespoke APIs for your application really easily. We’re in the world of operator explosion. In essence, it makes Kubernetes applications aware.”
* [dzone: Kubernetes and Running Stateful Workloads 🌟](https://dzone.com/articles/kubernetes-and-running-stateful-workloads)
* [towardsdatascience.com: Understanding the Relational Model of Database Management Systems 🌟](https://towardsdatascience.com/understanding-the-relational-model-of-database-management-systems-56f17db99f56)
* [openshift.com: OpenShift, Databases and You: When to Put Containerized Database Workloads on OpenShift 🌟](https://www.openshift.com/blog/openshift-databases-and-you-when-to-put-containerized-database-workloads-on-openshift) 
* [sixfold.medium.com: Reducing database queries to a minimum with DataLoaders](https://sixfold.medium.com/reducing-database-queries-to-a-minimum-with-dataloaders-cc98c25e54ce)
* [stackexchange.com/performance 🌟](https://stackexchange.com/performance)

<center>
[![Statefull and Stateless Aplications](images/stateful-and-stateless-applications.png)](https://www.xenonstack.com/insights/stateful-and-stateless-applications/)
</center>

## Serverless Databases
- [thenewstack.io: How to Ensure Your Serverless Database Stays Serverless](https://thenewstack.io/how-to-ensure-your-serverless-database-stays-serverless/)

## DataOps
- [dzone: 2021: The Year of DataOps](https://dzone.com/articles/2021-the-year-of-dataops) Centralizing an organization's data in a cloud data warehouse gives all stakeholders big-picture access to everything going on at the company.
- [thenewstack.io: The Benefits and Drawbacks of DataOps in Practice](https://thenewstack.io/the-benefits-and-drawbacks-of-dataops-in-practice/)

## Database Continuous Integration
- [cloudbees.com: Introductory Handbook for Database Continuous Integration](https://www.cloudbees.com/blog/database-continuous-integration)

## Databases on Kubernetes
* [cloud.google.com: To run or not to run a database on Kubernetes - What to consider](https://cloud.google.com/blog/products/databases/to-run-or-not-to-run-a-database-on-kubernetes-what-to-consider)
* [reddit.com: What's the best, proper way of running a database cluster on top of Kubernetes?](https://www.reddit.com/r/kubernetes/comments/9d8on5/whats_the_best_proper_way_of_running_a_database/)
* [caylent.com: The Pros and Cons of Running Production Databases as Containers](https://caylent.com/the-pros-and-cons-of-running-production-databases-as-containers)
* [learnk8s.io: Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes](https://learnk8s.io/cloud-resources-kubernetes)
* [cloudsavvyit.com: Should You Run a Database in Docker?](https://www.cloudsavvyit.com/5414/should-you-run-a-database-in-docker/)

## Database DevOps
- [informationweek.com: Can Enterprises Benefit From Adopting Database DevOps?](https://www.informationweek.com/devops/can-enterprises-benefit-from-adopting-database-devops/a/d-id/1337238)
- [medium: DevOps and Databases — The forgotten automation](https://medium.com/devops-dudes/devops-and-databases-the-forgotten-automation-95325b2d3c89)

## KubeDB Cloud Native Postgress Database
* [kubedb.com](https://kubedb.com/) Run production-grade databases easily on Kubernetes

## Cockroach Cloud Native Database
* [Wikipedia: CockroachDB](https://en.wikipedia.org/wiki/Cockroach_Labs) is a project that is designed to store copies of data in multiple locations in order to deliver speedy access. It is described as a scalable, consistently-replicated, transactional datastore.
* [Cockroach](https://www.cockroachlabs.com/docs/stable/orchestration.html)

## Operator Lifecycle Manager (OLM)
- [itnext.io: Operator Lifecycle Manager](https://itnext.io/wth-is-a-operator-lifecycle-manager-873cf1661b04)

## Spilo PostgreSQL Operator
* [Spilo: HA PostgreSQL Clusters with Docker](https://github.com/zalando/spilo) Spilo is a Docker image that provides PostgreSQL and Patroni bundled together. Patroni is a template for PostgreSQL HA. 
* [Patroni](https://github.com/zalando/patroni)
* [How I've Set Up HA PostgreSQL on Kubernetes (powered by Patroni, a template for PostgreSQL HA)](https://disaev.me/p/how-i-have-set-up-ha-postgresql-on-kubernetes/)

## Zalando PostgreSQL Operator
* [Zalando Postgres Operator](https://github.com/zalando/postgres-operator) Postgres operator creates and manages PostgreSQL clusters running in Kubernetes
* [vitobotta.com: Postgres on Kubernetes with the Zalando operator](https://vitobotta.com/2020/02/05/postgres-kubernetes-zalando-operator/)

## Crunchy Data PostgreSQL Operator
* [crunchydata.com](https://www.crunchydata.com/)
* [redhat.com: Overview - Crunchy Data PostgreSQL on Red Hat OpenShift Container Storage 🌟](https://www.redhat.com/en/resources/crunchy-data-postgresql-overview)
* [learn.crunchydata.com 🌟](https://learn.crunchydata.com/)
* [github.com/CrunchyData](https://github.com/CrunchyData)
* [github.com/CrunchyData/postgres-operator](https://github.com/CrunchyData/postgres-operator)
* [Documentation: Crunchy Data Container Suite 🌟](https://access.crunchydata.com/documentation/crunchy-postgres-containers/latest/)
* [crunchydata blog: Deploying Active-Active PostgreSQL on Kubernetes](https://info.crunchydata.com/blog/active-active-on-kubernetes)
* [crunchydata blog: What's New in Crunchy PostgreSQL Operator 4.0](https://info.crunchydata.com/blog/crunchy-postgres-kubernetes-operator-4.0)
* [slideshare.net: Deploying PostgreSQL on Kubernetes](https://www.slideshare.net/vyruss000/deploying-postgresql-on-kubernetes)
* [slideshare.net: Operating PostgreSQL at Scale with Kubernetes](https://www.slideshare.net/jkatz05/operating-postgresql-at-scale-with-kubernetes-137132067)
* [Youtube: Demo of Crunchy Data Postgres Operator v1.0.0 (2017)](https://www.youtube.com/watch?v=HX10WWTRiTY)
* [Youtube: Crunchy PostgreSQL Operator for Kubernetes 3.4 Overview (2018)](https://www.youtube.com/watch?v=gaXlrlz7GVc)
* [Youtube: OpenShift Meetup Tokyo #05 - Operator and Operator Lifecycle Manager on OpenShift (2019, openshift 4.1)](https://www.youtube.com/watch?v=X4vuktlK0Tg)
* [info.crunchydata.com: Monitoring PostgreSQL clusters in kubernetes](https://info.crunchydata.com/blog/monitoring-postgresql-clusters-in-kubernetes)
* [info.crunchydata.com: Deploy High-Availability PostgreSQL Clusters on Kubernetes by Example](https://info.crunchydata.com/blog/deploy-high-availability-postgresql-on-kubernetes)
* [info.crunchydata.com: Migrating from Oracle to PostgreSQL: Tips and Tricks](https://info.crunchydata.com/blog/migrating-from-oracle-to-postgresql-questions-and-considerations)
* [info.crunchydata.com: Scheduled PostgreSQL Backups and Retention Policies with Kubernetes](https://info.crunchydata.com/blog/schedule-postgresql-backups-and-retention-with-kubernetes)
* [info.crunchydata.com: Guard Against Transaction Loss with PostgreSQL Synchronous Replication](https://info.crunchydata.com/blog/synchronous-replication-in-the-postgresql-operator-for-kubernetes-guarding-against-transactions-loss)
* [info.crunchydata.com: Crunchy PostgreSQL for Kubernetes 4.3 Released](https://info.crunchydata.com/news/crunchy-postgresql-for-kuberenetes-4.3) Crunchy #PostgreSQL for #Kubernetes 4.3 released! Now supports multi-Kubernetes deployments, easier customization + installation, TLS, pgAdmin 4, improved pgBouncer support, and much more!
* [info.crunchydata.com: Deploy pgAdmin4 with PostgreSQL on Kubernetes](https://info.crunchydata.com/blog/deploy-pgadmin4-with-postgresql-on-kubernetes)
* [info.crunchydata.com: Multi-Kubernetes Cluster PostgreSQL Deployments](https://info.crunchydata.com/blog/multi-kubernetes-cluster-postgresql-deployments)
* [info.crunchydata.com: Quickly Document Your Postgres Database Using psql Meta-Commands](https://info.crunchydata.com/blog/d-meta)
* [info.crunchydata.com: Fast CSV and JSON Ingestion in PostgreSQL with COPY](https://info.crunchydata.com/blog/fast-csv-and-json-ingestion-in-postgresql-with-copy)
* [info.crunchydata.com: Composite Primary Keys, PostgreSQL and Django](https://info.crunchydata.com/blog/composite-primary-keys-postgresql-and-django)
* [info.crunchydata.com: Getting Started with PostgreSQL Operator 4.3 in OpenShift](https://info.crunchydata.com/blog/getting-started-with-postgresql-operator-4.3-in-openshift)
* [info.crunchydata.com: Introducing the Postgres Prometheus Adapter](https://info.crunchydata.com/blog/using-postgres-to-back-prometheus-for-your-postgresql-monitoring-1)
* [info.crunchydata.com: Getting Started with PostgreSQL Operator 4.3 in OpenShift](https://info.crunchydata.com/blog/getting-started-with-postgresql-operator-4.3-in-openshift)
* [info.crunchydata.com: Deploying Active-Active PostgreSQL on Kubernetes](https://info.crunchydata.com/blog/active-active-on-kubernetes)
* [opensource.com: Scaling PostgreSQL with Kubernetes Operators 🌟](https://opensource.com/article/19/2/scaling-postgresql-kubernetes-operators) Operators let users create standardized interfaces for managing stateful applications, like PostgreSQL, across Kubernetes-enabled cloud environments.
* [info.crunchydata.com: Setup ora2pg for Oracle to Postgres Migration](https://info.crunchydata.com/blog/setup-ora2pg-for-oracle-to-postgres-migration)
* [info.crunchydata.com: pgBackRest - Performing Backups on a Standby Cluster](https://info.crunchydata.com/blog/pgbackrest-performing-backups-on-a-standby-cluster)
* [thenewstack.io: Advanced Kubernetes Namespace Management with the PostgreSQL Operator 🌟](https://thenewstack.io/advanced-kubernetes-namespace-management-with-the-postgresql-operator/)
* [postgresql.org: Crunchy PostgreSQL Operator 4.5: Enhanced Monitoring, Custom Annotations, PostgreSQL 13 🌟](https://www.postgresql.org/about/news/crunchy-postgresql-operator-45-enhanced-monitoring-custom-annotations-postgresql-13-2086/)
* [info.crunchydata.com: How to Setup PostgreSQL Monitoring in Kubernetes](https://info.crunchydata.com/blog/setup-postgresql-monitoring-in-kubernetes)
* [redhat.com: Crunchy Data PostgreSQL on Red Hat OpenShift Container Storage (Overview) 🌟](https://www.redhat.com/en/resources/crunchy-data-postgresql-overview)
* [info.crunchydata.com: PostgreSQL Monitoring for Application Developers: The DBA Fundamentals](https://info.crunchydata.com/blog/postgresql-monitoring-for-application-developers-dba-stats)
* [youtube: OCB: High Availability PostgreSQL and more on OpenShift - Jonathan Katz (Crunchy Data) 🌟](https://www.youtube.com/watch?v=9jbR9lZuSU0) Learn how the PostgreSQL Operator from Crunchy Data makes it easy to deploy high availability Postgres clusters on OpenShift. Beyond that, we'll look at how the Operator pattern makes it possible to run your own open source database-as-a-service and cover the essential features: provisioning, HA, disaster recovery, monitoring, and how to do it all securely!
* [info.crunchydata.com: Tuning Your Postgres Database for High Write Loads](https://info.crunchydata.com/blog/tuning-your-postgres-database-for-high-write-loads)
* [info.crunchydata.com: Using the PostgreSQL Operator with Rook Ceph Storage](https://info.crunchydata.com/blog/crunchy-postgresql-operator-with-rook-ceph-storage)
* [info.crunchydata.com: Multi-Kubernetes Cluster PostgreSQL Deployments](https://info.crunchydata.com/blog/multi-kubernetes-cluster-postgresql-deployments)
* [developer.ibm.com: Deploy a Crunchy PostgreSQL for Kubernetes Operator to an OpenShift cluster 🌟](https://developer.ibm.com/technologies/databases/tutorials/deploy-a-crunchy-posgresql-kubernetes-operator-red-hat-marketplace-openshift/) Follow these steps to deploy a supported Crunchy PostgreSQL for Kubernetes operator from Red Hat Marketplace to an OpenShift cluster
* [info.crunchydata.com: An Easy Recipe for Creating a PostgreSQL Cluster with Docker Swarm](https://info.crunchydata.com/blog/an-easy-recipe-for-creating-a-postgresql-cluster-with-docker-swarm)
* [info.crunchydata.com: Deploying the PostgreSQL Operator on GKE](https://info.crunchydata.com/blog/install-postgres-operator-kubernetes-on-gke-ansible)
* [info.crunchydata.com: Using GitOps to Self-Manage Postgres in Kubernetes 🌟](https://info.crunchydata.com/blog/gitops-postgres-kubernetes)
* [info.crunchydata.com: Kubernetes Pod Tolerations and Postgres Deployment Strategies](https://info.crunchydata.com/blog/kubernetes-pod-tolerations-and-postgresql-deployment-strategies)
* [blog.crunchydata.com: Helm, GitOps and the Postgres Operator](https://blog.crunchydata.com/blog/gitops-postgres-kubernetes-helm)
* [blog.crunchydata.com: Crunchy Postgres Operator 4.6.0 🌟](https://blog.crunchydata.com/blog/crunchy-postgres-operator-4.6.0)
* [blog.crunchydata.com: Deploy PostgreSQL With TLS in Kubernetes](https://blog.crunchydata.com/blog/set-up-tls-for-postgresql-in-kubernetes)
* [blog.crunchydata.com: Announcing Google Cloud Storage (GCS) Support for pgBackRest](https://blog.crunchydata.com/blog/announcing-google-cloud-storage-gcs-support-for-pgbackrest)
* [youtube: Install and use Crunchy PostgreSQLfor OpenShift operator for simple todo app on OpenShift 🌟](https://www.youtube.com/watch?v=9wuUXi6Qbis&ab_channel=MichaelBornholdtNielsen)
* [blog.crunchydata.com: Query Optimization in Postgres with pg_stat_statements](https://blog.crunchydata.com/blog/tentative-smarter-query-optimization-in-postgres-starts-with-pg_stat_statements)
* [blog.crunchydata.com: Kubernetes Pod Tolerations and Postgres Deployment Strategies 🌟](https://blog.crunchydata.com/blog/kubernetes-pod-tolerations-and-postgresql-deployment-strategies)
* [blog.crunchydata.com: Active-Active PostgreSQL Federation on Kubernetes](https://blog.crunchydata.com/blog/active-active-postgres-federation-on-kubernetes)
* [blog.crunchydata.com: Multi-Kubernetes Cluster PostgreSQL Deployments](https://blog.crunchydata.com/blog/multi-kubernetes-cluster-postgresql-deployments)
* [blog.crunchydata.com: Next Generation Crunchy Postgres for Kubernetes 5.0 Released](https://blog.crunchydata.com/news/next-generation-crunchy-postgres-for-kubernetes-released)
* [blog.crunchydata.com: pgBackRest Point-In-Time Recovery Using Crunchy PostgreSQL Operator](https://blog.crunchydata.com/blog/pgbackrest-point-in-time-recovery-using-crunchy-postgresql-operator)
* [blog.crunchydata.com: Using Cert Manager to Deploy TLS for Postgres on Kubernetes](https://blog.crunchydata.com/blog/using-cert-manager-to-deploy-tls-for-postgres-on-kubernetes)
* [dzone: PostgreSQL HA and Kubernetes](https://dzone.com/articles/postgresql-ha-and-kubernetes) I share my thoughts about how to set up a PostgreSQL Database in Kubernetes with some level of high availability, introducing 3 different architectural styles to do so.
* [blog.crunchydata.com: Can't Resize your Postgres Kubernetes Volume? No Problem!](https://blog.crunchydata.com/blog/resize-postgres-kubernetes-volume-instance-sets)
* [blog.crunchydata.com: Your Guide to Connection Management in Postgres 🌟](https://blog.crunchydata.com/blog/your-guide-to-connection-management-in-postgres)
* [==blog.crunchydata.com: PostgreSQL 14 on Kubernetes (with examples!)==](https://blog.crunchydata.com/blog/postgresql-14-on-kubernetes)
* [blog.crunchydata.com: Kubernetes + Postgres Cluster From Scratch on Rocky 8](https://blog.crunchydata.com/blog/kube-cluster-from-scratch-on-rocky-8)

### Crunchy Data Developer Portal
- [Announcing the Crunchy Data Developer Portal](https://info.crunchydata.com/blog/announcing-the-crunchy-data-developer-portal)
- [Crunchy Data Developer Portal](https://www.crunchydata.com/developers) Self-service tools for developers and data scientists to easily get productive with PostgreSQL and Crunchy Data products.

### Crunchy Data Postgres Operator in OpenShift 4. Overview & Proof of Concept
- In earlier days, Red Hat recommended running PostgreSQL database outside the Kubernetes cluster. Now, with [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) technology, you can run stateful database applications on Kubernetes.
- [Crunchy PostgreSQL Operator](https://github.com/CrunchyData/postgres-operator) extends Kubernetes to give you the power to easily  create, configure and manage PostgreSQL clusters at scale.  When combined with the [Crunchy PostgreSQL Container Suite](https://github.com/CrunchyData/crunchy-containers), the Crunchy PostgreSQL Operator provides an open source software solution for PostgreSQL scaling, high-availability, disaster recovery, monitoring, and more.  All of this capability comes with the repeatability and automation that comes from Operators on Kubernetes.
- Crunchy PostgreSQL Operator is open source and developed in close collaboration with users to support enterprise deployments of cloud agnostic PostgreSQL-as-a-Service capability. This release comes after extensive feedback from our customers and the community to ensure the scalability and security that sysadmins, DBAs, and developers have come to rely on.
- [Crunchy PostgreSQL and Openshift](https://www.openshift.com/blog/leveraging-the-crunchy-postgresql)
- Crunchy Postgres Solutions: 
    1. **[Postgres Operator Community Edition](https://github.com/CrunchyData/postgres-operator):**
        - ‘pgo’ CLI tool
        - Not certified by Red Hat
        - The Operator can be deployed by multiple methods including:
            - [The PostgreSQL Operator Installer with kubectl](https://access.crunchydata.com/documentation/postgres-operator/4.3.0/installation/postgres-operator/)
            - [Install Operator Using Bash (the one used in this overview)](https://access.crunchydata.com/documentation/postgres-operator/4.3.0/installation/other/bash/)
            - [Ansible playbook installation](https://access.crunchydata.com/documentation/postgres-operator/4.3.0/installation/other/ansible/)
            - CLI installation using OLM **(Deprecated)**: new CatalogSource added via “pgo.catalogsource.yaml”.
            - Openshift Console installation using OLM (OperatorHub):
                - New CatalogSource requirement. 
                - CLI settings required.
    2. **Certified Crunchydata Postgres Operator (OLM/OperatorHub):**
        - Openshift Console installation using OLM (OperatorHub): One-click deployment and Web based operation
        - **No ‘pgo’ CLI tool?** (compatibility issues: unable to find in github the version that matches the server API - Sept 2019)
        - Certified by Red Hat
        - Provided by CrunchyData
    3. Other non-certified installations (unsupported by Red Hat): with or without OLM, CLI, etc.
- **[Crunchy Containers Community Edition](https://github.com/CrunchyData/crunchy-containers):**
    - Installation:
        1. [Installation guide](https://access.crunchydata.com/documentation/crunchy-postgres-containers/latest/installation-guide/installation-guide/)
        2. [Pgadmin4 install](https://access.crunchydata.com/documentation/crunchy-postgres-containers/latest/examples/administration/pgadmin4/) (easy)
    - Not certified by Red Hat

<center>
![crunchdydata in operatorhub](images/crunchydata_operator_hub.png)
</center>

#### Crunchydata Postgres Operator 3.5
- Release date: Januay 2019
- pgBackRest Architecture Enhancements
- pgBackRest Point-In-Time-Recovery
- Fast Failover
- Archive Storage Configuration
- Preferred Failover Node Label
- pgo-scheduler

<center>
![crunchydata operator 3.5](images/crunchydata_operator_3_5.png)
</center>

#### Crunchydata Postgres Operator 4.0.1
- Release date: June 2019
- **Namespace Deployment Options:** Ability to deploy the operator its own namespace but manage PostgreSQL clusters in multiple namespace. The new namespace management features lets users create multi-tenant PostgreSQL environments that add further isolation and security to their deployments. 
- **Further Enhancements to pgBackRest Integration:** Perform pgBackRest backups to **Amazon S3**. This allows  users to create an automated, geographically distributed, and hybrid cloud disaster recovery strategy.
- Integrated PostgreSQL **Benchmarking**
- **Ansible** Playbook Based Installation
- **Operator Lifecycle Management (OLM):** The OLM project is a component of the Operator Framework, an open source toolkit to manage Operators, in an effective, automated, and scalable way. OLM concepts were included into Crunchy PostgreSQL Operator to assist in the deployment on Kubernetes using OLM integration.

<center>
![crunchdydata operator 4.0.1](images/crunchydata_operator_4_0_1.png)
</center>

#### Crunchydata Postgres Operator 4.0.1 Community Edition 
##### Service Accounts
- Service accounts give us flexibility to control access to API without sharing user’s credentials. 
- Service Accounts are also used by pods and other non-human actors to perform various actions and are a central vehicle by which their access to resources is managed. **By default, three service accounts are created in each project:**
    1. **Builder:** Used by build pods and assigned the **system:image-builder** role, which grants push capability into the internal registry to any image stream in the project.
    2. **Deployer:** Used by deploy pods and assigned the **system:deployer role**, which allows modifying replication controllers in the project.
    3. **Default:** Used by all other pods by default.
- You can see them by running the following command: 

```
oc get serviceaccounts
oc get sa
```

- **Running a Pod with a Different Service Account.** You can run a pod with a service account other than the default:
    - Edit the deployment configuration:  ```$ oc edit dc/<deployment_config>```
    - Add the serviceAccount and serviceAccountName parameters to the spec field, and specify the service account you want to use:

```
spec:
    securityContext: {}
    serviceAccount: <service_account>
    serviceAccountName: <service_account>
```

- Refs:
    - [ref1](https://docs.openshift.com/container-platform/4.1/authentication/using-service-accounts-in-applications.html)
    - [ref2](https://docs.okd.io/latest/dev_guide/deployments/basic_deployment_operations.html#run-pod-with-different-service-account) 
    - [ref3](https://dzone.com/articles/understanding-openshift-security-context-constrain) 

- Each service account is represented by the ServiceAccount resource and is associated with two additional secrets for access to the OpenShift API and the internal registry:

```
$ oc describe serviceaccounts/default
Name:                default
Namespace:           pgouser1
Labels:              <none>
Annotations:         <none>
Image pull secrets:  default-dockercfg-nrhwt
Mountable secrets:   default-token-vm8b5
                     default-dockercfg-nrhwt
Tokens:              default-token-p6rhz
                     default-token-vm8b5
Events:              <none>

```

- The service account can be created and deleted with a simple command: 
    - ```oc create sa myserviceaccount```
    - ```oc delete sa/myserviceaccount```  
- Every service account is also a member of two groups:
    - **system:serviceaccounts**, which includes all service accounts in the cluster
    - **system:serviceaccounts:<project\>**, which includes all service accounts in the project

##### Roles assigned to Service Accounts
- When you create a pod, if you do not specify a service account, it is automatically assigned the **default service account** in the same namespace. If you get the raw json or yaml for a pod you have created (e.g. ```oc get pods/podname -o yaml```), you can see the **spec.serviceAccountName** field has been automatically set.
- You can grant privileges to groups of service accounts, which will effectively grant those privileges to all accounts in the group:
  
```
$ oc adm policy add-role-to-group view system:serviceaccounts -n myproject
role "view" added: "system:serviceaccounts" 
```

- For example, to grant view privileges to all service accounts in the cluster in the project myproject:

```
$ oc adm policy remove-role-from-group view system:serviceaccounts –n myproject
role "view" removed: "system:serviceaccounts" 
```

##### Security Context Constraints (SCC)
- **Security Context Constraints (SCCs)** control what actions pods can perform and what resources they can access. 
- SCCs combine a set of security configurations into a single policy object that can be applied to pods. 
- These security configurations include, but are not limited to, Linux Capabilities, Seccomp Profiles, User and Group ID Ranges, and types of mounts. 
- OpenShift ships with several SCCs:
    - The most constrained is the **restricted SCC**, and the least constrained is the **privileged SCC**:
        - ```oc edit scc restricted```
        - ```oc edit scc privileged``` 
    - The other SCCs provide intermediate levels of constraint for various use cases. 
    - **The restricted SCC is granted to all authenticated users by default.**
    - **The default SCC for most pods should be the restricted SCC.**
- If required, a cluster administrator may **allow certain pods to run with different SCCs**. Pods should be run with the most restrictive SCC possible. **Pods inherit their SCC from the Service Account used to run the pod**. With the default project template, new projects get a **Service Account named default** that is used to run pods. This default service account is only granted the ability to run the restricted SCC.

<center>
![crunchdydata scc1](images/crunchydata_scc1.png) ![crunchdydata scc2](images/crunchydata_scc2.png)
</center>

###### SCC Recommendations
- Use OpenShift's Security Context Constraint feature, which has been contributed to Kubernetes as [Pod Security Policies (PSP)](https://kubernetes.io/docs/concepts/policy/pod-security-policy/). PSPs are still beta in Kubernetes 1.10, 1.11, 1.12, 1.13, 1.14, 1.15 .
- **Use the restricted SCC as the default** 
- For pods that require additional access, use the SCC that grants the least amount of additional privileges or create a custom SCC 
- Remediation: Apply the SCC with the least privilege required
- Audit: 
    - To show all available SCCs: ```oc describe scc``` 
    - To audit a single pod:  
  
```
oc describe pod <POD> | grep openshift.io\/scc
openshift.io/scc: restricted             
``` 

<center>
![crunchdydata scc3](images/crunchydata_scc3.png)
</center>

- **Problem:** Default SCC is “restricted” SCC -> Crunchydata Postgres Cluster PODs are not rolled out
    - ```oc get rs```: 

    <center>
    ![crunchdydata restricted scc](images/crunchydata_restricted_scc.png)
    </center>

    - ```oc describe rs mycluster5-lgyb-84b58f5dd9```: Warning **FailedCreate** 3m24s (x17 over 7m30s) **replicaset-controller Error creating: pods "mycluster5-lgyb-84b58f5dd9-" is forbidden: unable to validate against any security context constraint: [fsGroup: Invalid value: []int64{26}: 26 is not an allowed group]**

##### Add a SCC to a Project
- SCCs are not granted directly to a project. Instead, you add a service account to an SCC and either specify the service account name on your pod or, when unspecified, run as the **default** service account.
- **To add a SCC to a user:**  ```oc adm policy add-scc-to-group <scc_name> <group_name>```
- **To add a SCC to all service accounts in a namespace:**  
  ```oc adm policy add-scc-to-group <scc_name>  system:serviceaccounts:<serviceaccount_namespace>```
- If you are currently in the project to which the service account belongs, you can use the -z flag and just specify the **serviceaccount_name**:  
  ```oc adm policy add-scc-to-user <scc_name> -z <serviceaccount_name>```
- Examples:
    - ```oc describe scc anyuid```
    - ```oc adm policy add-scc-to-group anyuid system:serviceaccounts:pgouser1```
    - ‘default’ serviceAccount: 
  
        ```
        oc adm policy add-scc-to-user anyuid system:serviceaccounts:pgouser1:default
        ``` 

    - User registered in Identity Provider: 

        ```
        oc adm policy add-scc-to-user anyuid myuser
        ```    

    - Custom serviceAccount: 

        ```
        oc adm policy add-scc-to-user anyuid system:serviceaccounts:pgouser1:my-sa
        ```    

- Refs:
    - [ref1](https://docs.openshift.com/container-platform/3.6/admin_guide/manage_scc.html)
    - [ref2](https://docs.openshift.com/container-platform/3.6/admin_guide/manage_scc.html#add-scc-to-user-group-project)
    - [ref3 🌟](https://dzone.com/articles/understanding-openshift-security-context-constrain)

###### Workflow1 without custom Service Account and without DeploymentConfig

<center>
![crunchdydata scc workflow1](images/crunchydata_scc_workflow1.png)
</center>

###### Workflow2 with custom Service Account and without DeploymentConfig

<center>
![crunchdydata scc workflow2](images/crunchydata_scc_workflow2.png)
</center>

- Create a custom ServiceAccount and add a role to it within a Project:
    1. ```oc project pgouser1```
    2. ```oc get scc```
    3. ```oc create serviceaccount my-sa –n pgouser1```
    4. ```oc describe sa my-sa```
    5. ```oc get scc```
    6. ```oc adm policy add-scc-to-user anyuid system:serviceaccount:pgouser1:my-sa```
    7. ```oc policy add-role-to-user edit system:serviceaccount:pgouser1:my-sa```
    8. Alternative to step #6:
   
```
oc edit scc anyuid 
```

```    
users:
- system:serviceaccount:pgouser1:my-sa
```

- Other commands of interest:
    - ```oc get role```
    - ```oc describe role pgo-role```
    - ```oc edit role pgo-role``` 

- References:
    - [ref1](https://blog.openshift.com/understanding-service-accounts-sccs/)
    - [ref2](https://docs.openshift.com/container-platform/4.1/authentication/understanding-and-creating-service-accounts.html)
    - [ref3](https://docs.openshift.com/container-platform/4.1/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth)

###### Workflow3 with custom service Account and DeploymentConfig

<center>
![crunchdydata scc workflow3](images/crunchydata_scc_workflow3.png)
</center>

##### Environment setup. Port Forward and WSL
- Deployment method used in this presentation: [Install Operator Using Bash](https://access.crunchydata.com/documentation/postgres-operator/4.3.0/installation/other/bash/)
- Config files setup by installer are saved in:
    - “pgo” Project -> Deployments
    - “pgo” Project -> Deployment Configs (empty, openshift feature not provided by CrunchyData)
    - “pgo” Project -> Secrets
    - “pgo” Project -> Config Maps
- References:
    - [ref1](https://access.crunchydata.com/documentation/postgres-operator/latest/operatorcli/pgo-overview/)
    - [ref2](https://crunchydata.github.io/postgres-operator/latest/operatorcli/common-pgo-cli-operations/)
- WSL (Windows Subystem for Linux): **alog/olog/clog** functions must be adapted to be run in WSL's Ubuntu:
 
```
vim $HOME/.bashrc
```

```
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples
# If not running interactively, don't do anything
case $- in
    *i*) ;;
    *) return;;
esac
# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth
# append to the history file, don't overwrite it
shopt -s histappend
# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000
# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar
# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes
if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    # We have color support; assume it's compliant with Ecma-48
    # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
    # a case would tend to support setf rather than setaf.)
    color_prompt=yes
    else
    color_prompt=
    fi
fi
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt
# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi
fi
#########################################
# CRUNCHYDATA POSTGRES OPERATOR SETTINGS:
#########################################
# operator env vars
export PATH=$PATH:$HOME/odev/bin
export PGO_APISERVER_URL=https://127.0.0.1:18443
#export PGO_APISERVER_URL=https://172.25.212.138:8443
export PGO_CA_CERT=$HOME/odev/src/github.com/crunchydata/postgres-operator/conf/postgres-operator/server.crt
export PGO_CLIENT_CERT=$HOME/odev/src/github.com/crunchydata/postgres-operator/conf/postgres-operator/server.crt
export PGO_CLIENT_KEY=$HOME/odev/src/github.com/crunchydata/postgres-operator/conf/postgres-operator/server.key
#alias setip='export PGO_APISERVER_URL=https://`kubectl get service postgres-operator -o=jsonpath="{.spec.clusterIP}"`:18443'
#alias alog='kubectl logs `kubectl get pod --selector=name=postgres-operator -o jsonpath="{.items[0].metadata.name}"` -c apiserver'
#alias olog='kubectl logs `kubectl get pod --selector=name=postgres-operator -o jsonpath="{.items[0].metadata.name}"` -c operator'
#
export CCP_IMAGE_TAG=rhel7-11.1-2.3.0
export CCP_IMAGE_PREFIX=registry.connect.redhat.com/crunchydata
export PGO_CMD=oc
export PGO_BASEOS=rhel7
export PGO_VERSION=4.0.1
export PGO_NAMESPACE=pgo
export PGO_IMAGE_TAG=rhel7-4.0.1
export PGO_IMAGE_PREFIX=registry.connect.redhat.com/crunchydata
export GOPATH=$HOME/odev
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
# NAMESPACE is the list of namespaces the Operator will watch
export NAMESPACE=pgouser1,pgouser2
# PGO_OPERATOR_NAMESPACE is the namespace the Operator is deployed into
export PGO_OPERATOR_NAMESPACE=pgo
# PGO_CMD values are either kubectl or oc, use oc if Openshift
export PGO_CMD=kubectl
# the directory location of the Operator scripts
export PGOROOT=$GOPATH/src/github.com/crunchydata/postgres-operator
# the version of the Operator you run is set by these vars
export PGO_IMAGE_PREFIX=crunchydata
export PGO_BASEOS=centos7
export PGO_VERSION=4.0.1
export PGO_IMAGE_TAG=$PGO_BASEOS-$PGO_VERSION
# for the pgo CLI to authenticate with using TLS
export PGO_CA_CERT=$PGOROOT/conf/postgres-operator/server.crt
export PGO_CLIENT_CERT=$PGOROOT/conf/postgres-operator/server.crt
export PGO_CLIENT_KEY=$PGOROOT/conf/postgres-operator/server.key
# common bash functions for working with the Operator
function setip() { 
export PGO_APISERVER_URL=https://`$PGO_CMD -n "$PGO_OPERATOR_NAMESPACE" get service postgres-operator -o=jsonpath="{.spec.clusterIP}"`:18443 
export CO_APISERVER_URL=https://`$PGO_CMD -n "$PGO_OPERATOR_NAMESPACE" get service postgres-operator -o=jsonpath="{.spec.clusterIP}"`:18443 
}
function alog() {
$PGO_CMD  -n "$PGO_OPERATOR_NAMESPACE" logs `$PGO_CMD  -n "$PGO_OPERATOR_NAMESPACE" get pod --selector=name=postgres-operator -o jsonpath="{.items[0].metadata.name}"` -c apiserver
}
function olog () {
$PGO_CMD  -n "$PGO_OPERATOR_NAMESPACE" logs `$PGO_CMD  -n "$PGO_OPERATOR_NAMESPACE" get pod --selector=name=postgres-operator -o jsonpath="{.items[0].metadata.name}"` -c operator
}
function slog () {
$PGO_CMD  -n "$PGO_OPERATOR_NAMESPACE" logs `$PGO_CMD  -n "$PGO_OPERATOR_NAMESPACE" get pod --selector=name=postgres-operator -o jsonpath="{.items[0].metadata.name}"` -c scheduler
}
#export DOCKER_HOST=tcp://localhost:2375
# crunchy containers: https://github.com/CrunchyData/crunchy-containers/tree/2.4.1
export GOPATH=$HOME/cdev        # set path to your new Go workspace
export GOBIN=$GOPATH/bin        # set bin path 
export PATH=$PATH:$GOBIN        # add Go bin path to your overall path
export CCP_BASEOS=centos7       # centos7 for Centos, rhel7 for Redhat
export CCP_PGVERSION=10         # The PostgreSQL major version
export CCP_PG_FULLVERSION=10.9
export CCP_VERSION=2.4.1
export CCP_IMAGE_PREFIX=crunchydata # Prefix to put before all the container image names
export CCP_IMAGE_TAG=$CCP_BASEOS-$CCP_PG_FULLVERSION-$CCP_VERSION   # Used to tag the images
export CCPROOT=$GOPATH/src/github.com/crunchydata/crunchy-containers    # The base of the clone github repo
export CCP_SECURITY_CONTEXT=""
export CCP_CLI=oc          # kubectl for K8s, oc for OpenShift
export CCP_NAMESPACE=crunchy-containers       # Change this to whatever namespace/openshift project name you want to use
export CCP_SECURITY_CONTEXT='"fsGroup":26'
export CCP_STORAGE_CLASS=gp2
export CCP_STORAGE_MODE=ReadWriteOnce
export CCP_STORAGE_CAPACITY=400M
```
<br/>

- **port-forward** to reach postgres-operator POD with ‘pgo’ tool (18443 port defined in previous .bashrc): 

```
oc project pgo
oc get pod 
oc port-forward postgres-operator-844d8f9777-8d5k5 -n pgo 18443:8443
```

##### Cluster Deployment and Operation with pgo

```
pgo create cluster mycluster --pgpool -n pgouser1 --resources-config=small --replica-count=1
pgo show cluster --all -n pgouser1
pgo backup mycluster --backup-type=pgbackrest –n pgouser1
pgo failover mycluster --query –n pgouser1
pgo failover mycluster --target=mycluster-olvhy –n pgouser1
pgo test mycluster -n pgouser1
pgo create cluster somefastpg -n pgouser1 --node-label=speed=fast
pgo create cluster abouncer --pgbouncer  (sidecar pgbouncer added to this PG cluster)
pgo create cluster apgpool --pgpool 
pgo status cluster mycluster –n pgouser1
pgo ls mycluster –n pgouser1
pgo reload mycluster –n pgouser1
pgo scale mycluster –n pgouser1
```

PGO USER allows you to manage users and passwords across a set of clusters:

```
pgo user –-selector=name=mycluster --expired=300 –-update-password –n pgouser1
pgo user –-change-password=bob –n pgouser1 --selector=name=mycluster --password=newpass
```

##### Psql access from postgres operator POD

```
oc project pgo
oc get pods
oc rsh postgres-operator-844d8f9777-ppjv9
export PGPASSWORD=password
psql -h mycluster-pgpool.pgouser1 -U testuser -l
psql -h mycluster-pgpool.pgouser1 -U postgres -c "CREATE DATABASE testdb"
psql -h mycluster-pgpool.pgouser1 -U postgres testdb -c "CREATE TABLE test (ID CHAR(4) NOT NULL, name TEXT NOT NULL, PRIMARY KEY (id))"
psql -h mycluster-pgpool.pgouser1 -U postgres testdb -c "INSERT INTO test (id,name) VALUES (1, 'user01')"
psql -h mycluster-pgpool.pgouser1 -U postgres testdb -c "select * from test"
```

##### List Databases with psql

```
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF8 | en_US.UTF8 |
 template0 | postgres | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 userdb    | postgres | UTF8     | en_US.UTF8 | en_US.UTF8 | =Tc/postgres         +
           |          |          |            |            | postgres=CTc/postgres+
           |          |          |            |            | testuser=CTc/postgres+
           |          |          |            |            | user1=CTc/postgres
(4 rows)
```

##### Access from another POD within the cluster with psql client
For example with [this psql client](https://hub.docker.com/r/centos/postgresql-10-centos7)

```
oc rsh postgresql-10-centos7-1-pjh46
sh-4.2$ psql -p 5432 -h mycluster-pgpool.pgouser1 -U postgres postgres
psql (10.6, server 11.3)
WARNING: psql major version 10, server major version 11.
         Some psql features might not work.
Type "help" for help.

postgres=#
```

##### Access from another POD within the cluster with Pgadmin4 of Crunchy containers Community Edition
- [crunchy-pgadmin4](https://access.crunchydata.com/documentation/crunchy-postgres-containers/4.3.0/container-specifications/crunchy-pgadmin4/)
- [pgAdmin 4](https://access.crunchydata.com/documentation/crunchy-postgres-containers/4.3.0/examples/administration/pgadmin4/)

<center>
![crunchdydata pgadmin](images/crunchydata_pgadmin.png)
</center>

##### Debugging Crunchydata Postgres Operator 4.0.1 Community Edition
- Debug level logging in turned on by default when deploying the Operator.
- Sample bash functions are supplied in examples/envs.sh to view the Operator logs.
- You can view the Operator REST API logs with the **alog** bash function.
- You can view the Operator core logic logs with the **olog** bash function.
- You can view the Scheduler logs with the **slog** bash function.
- You can enable the pgo CLI debugging with the following flag:
    ```
    $ pgo version --debug
    ```
- You can set the REST API URL as follows after a deployment if you are developing on your local host by executing the **setip** bash function.
- “alog”, “olog”, “slog” and “setip” are defined in $HOME/.bashrc


#### Certified Crunchydata Postgres Operator (OLM/OperatorHub). Manual Setup
-  We will set this up manually:
    - StorageClass changed to “gp2” in YAML file (AWS)
    - ‘pgo’ tool compatibility issues

<center>
![crunchdydata operatorhub install2](images/crunchydata_operatorhub_install1.png)

![crunchdydata operatorhub install2](images/crunchydata_operatorhub_install2.png)
</center>

- NO PODs are deployed -> configuration needed:

<center>
![crunchdydata operatorhub install3](images/crunchydata_operatorhub_install3.png)

![crunchdydata operatorhub install4](images/crunchydata_operatorhub_install4.png)
</center>

- Replica Sets: where PODs should be launched

<center>
![crunchdydata operatorhub install5](images/crunchydata_operatorhub_install5.png)
</center>

- ReplicaSets (environment) and Deployment:

<center>
![crunchdydata operatorhub install6](images/crunchydata_operatorhub_install6.png)

![crunchdydata operatorhub install7](images/crunchydata_operatorhub_install7.png)
</center>

- Error detected. Solution: 

```
oc adm policy add-scc-to-user anyuid system:serviceaccount:pgophub:default
```

<center>
![crunchdydata operatorhub install8](images/crunchydata_operatorhub_install8.png)
</center>

- We see now a new POD being created:

<center>
![crunchdydata operatorhub install9](images/crunchydata_operatorhub_install9.png)
</center>

- New errors: “secrets” need to be setup:

<center>
![crunchdydata operatorhub install10](images/crunchydata_operatorhub_install10.png)

![crunchdydata operatorhub install11](images/crunchydata_operatorhub_install11.png)

![crunchdydata operatorhub install12](images/crunchydata_operatorhub_install12.png)
</center>

- New errors: 3 “secrets” need to be setup manually -> POD is started successfully and we have psql access.

<center>
![crunchdydata operatorhub install13](images/crunchydata_operatorhub_install13.png) ![crunchdydata operatorhub install14](images/crunchydata_operatorhub_install14.png)

![crunchdydata operatorhub install15](images/crunchydata_operatorhub_install15.png)

![crunchdydata operatorhub install16](images/crunchydata_operatorhub_install16.png)
</center>

## Oracle 12c on OpenShift Container Platform
- [medium: Running Oracle 12c on OpenShift Container Platform](https://medium.com/@pittar/running-oracle-12c-on-openshift-container-platform-ca471a9f7057) Oracle is now offering an Oracle 12c image on Docker Hub for dev/test purposes (license still required for Prod).
- [dockerhub: Oracle Database 12c Enterprise Edition](https://hub.docker.com/_/oracle-database-enterprise-edition) 

## Oracle Database Operator for Kubernetes
- https://github.com/oracle/oracle-database-operator
- [pasimoes.dev: Let the Oracle Database Operator for Kubernetes Do the Job](https://pasimoes.dev/p/oracle-db-k8s-oper-intro/)

## SQL Server
- [Expanding SQL Server Big Data Clusters capabilities, now on Red Hat OpenShift](https://cloudblogs.microsoft.com/sqlserver/2020/06/23/expanding-sql-server-big-data-clusters-capabilities-now-on-red-hat-openshift/)
- [devblogs.microsoft.com: DevOps for Azure SQL 🌟](https://devblogs.microsoft.com/azure-sql/devops-for-azure-sql/)

## MySQL
- [twindb.com: Verify MySQL Backups With TwinDB Backup Tool](https://twindb.com/verify-mysql-backups-with-twindb-backup-tool/)
- [blog.eduguru.in: mysql create index on table](https://blog.eduguru.in/mysql-2/mysql-create-index-on-table)
- [percona.com: MySQL 101: Parameters to Tune for MySQL Performance](https://www.percona.com/blog/2020/06/30/mysql-101-parameters-to-tune-for-mysql-performance/)
- [pub.towardsai.net: Step-by-Step Design of Enhanced Entity-Relationship (EER) in MySQL](https://pub.towardsai.net/step-by-step-design-of-enhanced-entity-relationship-eer-in-mysql-1e0f8b9fe5d4) Database schema relationships of tables
- [dbasecenter.com: The top 5 MySQL performance variables](https://dbasecenter.com/blog/the-top-5-mysql-performance-variables/)
- [opensource.com](https://opensource.com/article/21/5/mysql-query-tuning) Tune your MySQL queries like a pro. Optimizing your queries isn't a dark art; it's just simple engineering.
- [percona.com: MySQL on Kubernetes with GitOps 🌟](https://www.percona.com/blog/2021/06/23/mysql-on-kubernetes-with-gitops/)
- [Moco](https://cybozu-go.github.io/moco/) MOCO is a Kubernetes operator for MySQL created and maintained by Cybozu.
- [cloudsavvyit.com: How to Run PHPMyAdmin in a Docker Container](https://www.cloudsavvyit.com/13842/how-to-run-phpmyadmin-in-a-docker-container/)
- [percona.com: Storing JSON in Your Databases: Tips and Tricks For MySQL Part One](https://www.percona.com/blog/storing-json-in-your-databases-tips-mysql/)
- [tusacentral.com: MySQL on Kubernetes demystified](http://www.tusacentral.com/joomla/index.php/mysql-blogs/243-mysql-on-kubernetes-demystified)
- [dzone: PostgreSQL vs MySQL Performance](https://dzone.com/articles/postgresql-versus-mysql-performance)

## MariaDB
- [thenewstack.io: Maria DB Gets Reactive with a Non-Blocking Connector for Java](https://thenewstack.io/maria-db-gets-reactive-with-a-non-blocking-connector-for-java/)

## PostgreSQL
- [momjian.us: Mastering PostgreSQL Administration [pdf] ](https://momjian.us/main/writings/pgsql/administration.pdf)
- [9 High-Performance Tips when using PostgreSQL with JPA and Hibernate](https://vladmihalcea.com/9-postgresql-high-performance-performance-tips/)
- [dzone: A Guide to SQL Triggers: Setting up Database Tracking in PostgreSQL](https://dzone.com/articles/a-guide-to-sql-triggers-setting-up-database-tracking-in-postgresql) SQL triggers are less common but can be a great solution for certain situations. I'll show how to use triggers in Postgres to enforce data integrity and track changes to a database.
- [migops.com: pgBackRest – The Best Postgres Backup Tool with a very active community](https://www.migops.com/blog/2021/04/09/pgbackrest-the-best-postgres-backup-tool-with-a-very-active-community/)
- [towardsdatascience.com: Practical Introduction to PostgreSQL](https://towardsdatascience.com/practical-introduction-to-postgresql-5f73d3d394e)
- [percona.com: An Overview of Sharding in PostgreSQL and How it Relates to MongoDB’s](https://www.percona.com/blog/2019/05/24/an-overview-of-sharding-in-postgresql-and-how-it-relates-to-mongodbs/)
- [blog.crunchydata.com: How to Setup PostgreSQL Monitoring in Kubernetes](https://blog.crunchydata.com/blog/setup-postgresql-monitoring-in-kubernetes)
- [blog.flant.com: Comparing Kubernetes operators for PostgreSQL](https://blog.flant.com/comparing-kubernetes-operators-for-postgresql/)
- [blog.crunchydata.com: Cut Out the Middle Tier: Generating JSON Directly from Postgres](https://blog.crunchydata.com/blog/generating-json-directly-from-postgres)
- [percona.com: How to Adjust Linux Out-Of-Memory Killer Settings for PostgreSQL](https://www.percona.com/blog/2019/08/02/out-of-memory-killer-or-savior/)
- [Postgres.app](https://postgresapp.com/) The easiest way to get started with PostgreSQL on the Mac 
- [devopscube.com: How to Deploy PostgreSQL Statefulset in Kubernetes With High Availability](https://devopscube.com/deploy-postgresql-statefulset/)
- [blog.crunchydata.com: Quickly Document Your Postgres Database Using psql Meta-Commands](https://blog.crunchydata.com/blog/d-meta)
- **Why Postgres?**
    - Its fully open source, so control over destiny
    - Features are comparable to Oracle, so minimizes mental friction of the move
- [blog.crunchydata.com: Devious SQL: Message Queuing Using Native PostgreSQL](https://blog.crunchydata.com/blog/message-queuing-using-native-postgresql)
- [percona.com: Should I Create an Index on Foreign Keys in PostgreSQL?](https://www.percona.com/blog/should-i-create-an-index-on-foreign-keys-in-postgresql/)
- [percona.com: PostgreSQL 14 Database Monitoring and Logging Enhancements](https://www.percona.com/blog/postgresql-14-database-monitoring-and-logging-enhancements/)
- [theregister.com: MySQL a 'pretty poor database' says departing Oracle engineer](https://www.theregister.com/2021/12/06/mysql_a_pretty_poor_database/) PostgreSQL a better option for open source RDBMS, he claims
- [wanago.io: Creating views with PostgreSQL](https://wanago.io/2021/12/06/views-postgresql-typeorm/)
- [==percona/pg_stat_monitor==](https://github.com/percona/pg_stat_monitor) PostgreSQL Statistics Collector
- [==blog.crunchydata.com: A Postgres Primer for Oracle DBAs==](https://blog.crunchydata.com/blog/a-postgres-primer-for-oracle-dbas)
- [==blog.crunchydata.com: Postgres Indexes for Newbies==](https://blog.crunchydata.com/blog/postgres-indexes-for-newbies)

## Percona MySQL
- [Percona.com: Percona Kubernetes Operator for Percona XtraDB Cluster](https://www.percona.com/doc/kubernetes-operator-for-pxc/index.html)
- [medium: Upgrading MySQL (Percona Server) from 5.7 to 8.0](https://medium.com/flant-com/upgrading-mysql-percona-server-5-to-8-4bce53bdce5c)
- [percona.com: MySQL 101: How to Find and Tune a Slow SQL Query](https://www.percona.com/blog/2020/06/26/mysql-101-how-to-find-and-tune-a-slow-sql-query/)
- [percona.com: Storing Kubernetes Operator for Percona Server for MongoDB Secrets in Github](https://www.percona.com/blog/2021/03/22/storing-kubernetes-operator-for-percona-server-for-mongodb-secrets-in-github/)
- [percona.com: Migration of a MySQL Database to a Kubernetes Cluster Using Asynchronous Replication](https://www.percona.com/blog/migration-of-a-mysql-database-to-a-kubernetes-cluster-using-asynchronous-replication/)

## Percona PostgreSQL Operator
- [percona.com: Migrating PostgreSQL to Kubernetes](https://www.percona.com/blog/migrating-postgresql-to-kubernetes)

## Redis
- [RedisLabs/redis-enterprise-k8s-docs: Deploying Redis Enterprise on Kubernetes](https://github.com/RedisLabs/redis-enterprise-k8s-docs) This page describes how to deploy Redis Enterprise on Kubernetes using the Redis Enterprise Operator.
- [tech.trell.co: Redis Cluster Creation Automation](https://tech.trell.co/redis-cluster-creation-automation-5e71eedf0e56)
- [containiq.com: Deploying Redis Cluster on Kubernetes | Tutorial and Examples](https://www.containiq.com/post/deploy-redis-cluster-on-kubernetes)

## Rockset
- [rockset.com: Sequoia Capital: Why We Moved from Elasticsearch to Rockset](https://rockset.com/blog/sequoia-capital-elasticsearch-to-rockset/)

## Clickhouse
- [clickhouse.com](https://clickhouse.com) ClickHouse is a column-oriented database management system (DBMS) for online analytical processing of queries (OLAP).
- [Altinity/clickhouse-operator](https://github.com/Altinity/clickhouse-operator) The ClickHouse Operator creates, configures and manages ClickHouse clusters running on Kubernetes
- [radondb/radondb-clickhouse-kubernetes](https://github.com/radondb/radondb-clickhouse-kubernetes) Open Source，High Availability Cluster，based on ClickHouse
- [tech.marksblogg.com: Monitor ClickHouse column oriented database with Prometheus & Grafana](https://tech.marksblogg.com/clickhouse-prometheus-grafana.html)

## Apache Ignite
- [Apache Ignite](https://ignite.apache.org/) Distributed Database For High-Performance Computing With In-Memory Speed
- [dzone: Stateful Microservices With Apache Ignite](https://dzone.com/articles/stateful-microservices-with-apache-ignite) This article explains how to implement stateful microservices architecture for Spring Boot applications with distributed database Apache Ignite.
## Tools
- [SHMIG](https://github.com/mbucc/shmig) A database migration tool written in BASH consisting of just one file - shmig.
- [DATA-DOG/go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) Sql mock driver for golang to test database interactions

## Time-Series Database
- [thenewstack.io: You Don’t Need a Blockchain, You Need a Time-Series Database](https://thenewstack.io/you-dont-need-a-blockchain-you-need-a-time-series-database/)

## Data Analytics and Visualization Tools
- [opensource.com: Make your data boss-friendly with EDA - Enterprise Data Analytics](https://opensource.com/article/21/4/visualize-data-eda) - [EDA](https://eda.jortilles.com/en/jortilles-english/)
- [thenewstack.io: Kubernetes-Run Analytics at the Edge: Postgres, Kafka, Debezium](https://thenewstack.io/kubernetes-run-analytics-at-the-edge-postgres-kafka-debezium/)

## Data Lakes
- [unifieddatascience.com: Data lake design patterns on Azure (Microsoft) cloud](https://www.unifieddatascience.com/data-lake-design-patterns-on-azure-microsoft-cloud)
- [unifieddatascience.com: Data lake design patterns on AWS (Amazon) cloud](https://www.unifieddatascience.com/data-lake-design-patterns-on-aws-amazon-cloud)
- [unifieddatascience.com: Data lake design patterns on google (GCP) cloud](https://www.unifieddatascience.com/data-lake-design-patterns-on-google-cloud)

## Graph Databases
- [SQErzo: Tiny ORM for Graph databases](https://github.com/BBVA/sqerzo) Tiny ORM for graph databases: Neo4j, RedisGraph, AWS Neptune or Gremlin
- [towardsdatascience.com: At Its Core: How Is a Graph Database Different from a Relational One?](https://towardsdatascience.com/at-its-core-hows-a-graph-database-different-from-a-relational-8297ca99cb8f) It’s easy to come up with some answers by simply Googling the topic, however, as I found, most answers list benefits mostly superficially

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes has made huge improvements in the ability to run stateful workloads including databases and message queues, but I still prefer not to run them on Kubernetes.</p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/963413508300812295?ref_src=twsrc%5Etfw">February 13, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Postgres is what happens when tech gets so good, for so long, it becomes boring. Dope since the 80s. <a href="https://t.co/zeoagBfMvW">https://t.co/zeoagBfMvW</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1343617588262096896?ref_src=twsrc%5Etfw">December 28, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Stack Overflow&#39;s SQL Server is at 4% CPU with 500M queries/day <a href="https://t.co/wX9Od749ik">https://t.co/wX9Od749ik</a> <a href="https://t.co/1BAuEV9VgT">https://t.co/1BAuEV9VgT</a></p>&mdash; Lukas Eder (@lukaseder) <a href="https://twitter.com/lukaseder/status/1428025568461737996?ref_src=twsrc%5Etfw">August 18, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">PostgreSQL for relational.<br>PromQL for monitoring.<br><br>Two big alignments across the industry.</p>&mdash; Jaana Dogan at KubeCon ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1448084198418522113?ref_src=twsrc%5Etfw">October 13, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m super curious, how many people have successfully migrated their databases from Oracle to Postgres in production? I&#39;m talking 100% migration with Oracle being turned off at the end.</p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1455212853678338048?ref_src=twsrc%5Etfw">November 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes can only meet stateful services half way. We need direct changes in databases, message brokers, and other stateful systems if we want to see a future where Kubernetes becomes the preferred destination to run them. The <a href="https://twitter.com/VectorizedIO?ref_src=twsrc%5Etfw">@vectorizedio</a> team is doing their part. <a href="https://t.co/w94Q56nnXM">https://t.co/w94Q56nnXM</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1457828928022745090?ref_src=twsrc%5Etfw">November 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sometimes we work for a database and need to connect to another (<a href="https://twitter.com/hashtag/migration?src=hash&amp;ref_src=twsrc%5Etfw">#migration</a> ;) so I explained to a colleague the difference between Oracle SERVICE_NAME and SID. Pasting it here in case it helps 🧵</p>&mdash; Franck Pachot 🚀 (@FranckPachot) <a href="https://twitter.com/FranckPachot/status/1488796764014587909?ref_src=twsrc%5Etfw">February 2, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes Database Operator is useful for building scalable database servers as a database cluster. But migrating existing databases to k8s requires a lot of manual work due to having to create new artifacts.<br><br>At our next meetup, we&#39;ll demo an open-source tool to solve this. <a href="https://t.co/o55vnyITV2">pic.twitter.com/o55vnyITV2</a></p>&mdash; konveyor.io (@Konveyor_io) <a href="https://twitter.com/Konveyor_io/status/1489597744213897218?ref_src=twsrc%5Etfw">February 4, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>