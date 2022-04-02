# Databases on Kubernetes. Database DevOps
- [Introduction](#introduction)
- [How to choose the right database for your service](#how-to-choose-the-right-database-for-your-service)
- [Database Load Balancer](#database-load-balancer)
- [SQL](#sql)
    - [Alternatives to SQL](#alternatives-to-sql)
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
- [Videos](#videos)
- [Tweets](#tweets)

## Introduction
- [thenewstack.io: How Database Load Balancing Completes the 3-Tiered Architecture 🌟](https://thenewstack.io/database-load-balancing-and-the-delusion-of-3-tiered-architecture/)
- [sqlshack.com: SQL Database on Kubernetes: Considerations and Best Practices 🌟](https://www.sqlshack.com/sql-database-on-kubernetes-considerations-and-best-practices/)
- [thenewstack.io: Just How Challenging Is State in Kubernetes? 🌟](https://thenewstack.io/just-how-challenging-is-state-in-kubernetes/)
- [theregister.com: 75% of databases to be cloud-hosted by 2022, says Gartner while dishing on the weak points of each provider](https://www.theregister.com/2020/12/02/gartner_cloud_dbms/)
- [thenewstack.io: What Is Data Management in the Kubernetes Age?](https://thenewstack.io/what-is-data-management-in-the-kubernetes-age/)
- [==thenewstack.io: A Case for Databases on Kubernetes from a Former Skeptic==](https://thenewstack.io/a-case-for-databases-on-kubernetes-from-a-former-skeptic/)
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
* [intellipaat.com: Difference between DBMS and RDBMS](https://intellipaat.com/blog/dbms-vs-rdbms-difference/) DBMS and RDBMS sound very similar, but can be confusing to those who are completely new to the database domain. Both of them are based on the technology of storing data. However, we will dive into this DBMS vs RDBMS blog to learn the difference between them.
* [==betterprogramming.pub: Multi-Tenancy Support With Spring Boot, Liquibase, and PostgreSQL==](https://betterprogramming.pub/multi-tenancy-support-with-spring-boot-liquibase-and-postgresql-d41942dc0639) A step-by-step guide on how to implement multi-tenancy.
* [==thenewstack.io: How Kubernetes and Database Operators Drive the Data Revolution==](https://thenewstack.io/how-kubernetes-and-database-operators-drive-the-data-revolution/)
* [thenewstack.io: How Radical API Design Changed the Way We Access Databases](https://thenewstack.io/how-radical-api-design-changed-the-way-we-access-databases/)

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
- [vladmihalcea.com: SQL LEFT JOIN – A Beginner’s Guide](https://vladmihalcea.com/sql-left-join/)
- [vladmihalcea.com: SQL JOIN USING – A Beginner’s Guide](https://vladmihalcea.com/sql-join-using/)
- [gcreddy.com: SQL Step by Step Videos](https://www.gcreddy.com/2021/05/sql-step-by-step-videos.html)

### Alternatives to SQL
- [infoworld.com: Beyond SQL: 8 new languages for data querying](https://www.infoworld.com/article/3654909/beyond-sql-8-new-languages-for-data-querying.html) SQL has dominated data querying for decades. Newer query languages offer more elegance, simplicity, and flexibility for modern use cases.

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
* [==Cockroach==](https://www.cockroachlabs.com/docs/stable/orchestration.html)

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
- [Crunchy Data PostgreSQL Operator](crunchydata.md)

## Oracle 12c on OpenShift Container Platform
- [medium: Running Oracle 12c on OpenShift Container Platform](https://medium.com/@pittar/running-oracle-12c-on-openshift-container-platform-ca471a9f7057) Oracle is now offering an Oracle 12c image on Docker Hub for dev/test purposes (license still required for Prod).
- [dockerhub: Oracle Database 12c Enterprise Edition](https://hub.docker.com/_/oracle-database-enterprise-edition) 

## Oracle Database Operator for Kubernetes
- https://github.com/oracle/oracle-database-operator
- [pasimoes.dev: Let the Oracle Database Operator for Kubernetes Do the Job](https://pasimoes.dev/p/oracle-db-k8s-oper-intro/)

## SQL Server
- [Expanding SQL Server Big Data Clusters capabilities, now on Red Hat OpenShift](https://cloudblogs.microsoft.com/sqlserver/2020/06/23/expanding-sql-server-big-data-clusters-capabilities-now-on-red-hat-openshift/)
- [devblogs.microsoft.com: DevOps for Azure SQL 🌟](https://devblogs.microsoft.com/azure-sql/devops-for-azure-sql/)
- [khalidabuhakmeh.com: Running SQL Server Queries In Docker](https://khalidabuhakmeh.com/running-sql-server-queries-in-docker)

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
- [thenewstack.io: Deploy MySQL and phpMyAdmin with Docker](https://thenewstack.io/deploy-mysql-and-phpmyadmin-with-docker/)

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
- [dev.to: REST Data Service on YugabyteDB / PostgreSQL](https://dev.to/yugabyte/rest-data-service-on-yugabytedb-postgresql-5f2h)
- [==orgrim/pg_back: Simple backup tool for PostgreSQL==](https://github.com/orgrim/pg_back) pg_back dumps databases from PostgreSQL
- [sqlrevisited.blogspot.com: MySQL vs PostgreSQL? Pros and Cons](https://sqlrevisited.blogspot.com/2022/03/mysql-vs-postgresql-pros-and-cons.html)

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
- [blog.devgenius.io: How to use Redis Pub/Sub in your Python Application 🌟](https://blog.devgenius.io/how-to-use-redis-pub-sub-in-your-python-application-b6d5e11fc8de)

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

## Videos
??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/OqCK95AS-YE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/SxsMgHFNvWg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/W_Knpfhv0Qg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/OJySfiMKXLs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>

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