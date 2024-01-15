# AWS RDS Databases

1. [Introduction](#introduction)
2. [AWS Database Migration Service DMS](#aws-database-migration-service-dms)
3. [AWS RDS Proxy](#aws-rds-proxy)
4. [AWS Schema Conversion Tool](#aws-schema-conversion-tool)
5. [AWS Redshift](#aws-redshift)
6. [AWS Data Mesh and Batch Data Processing](#aws-data-mesh-and-batch-data-processing)
7. [AWS NoSQL DynamoDB](#aws-nosql-dynamodb)

## Introduction

- [Tutorial: Restoring a DB Instance from a DB Snapshot](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.RestoringFromSnapshot.html)
- [Partitioning MySQL on RDS: "How We Partitioned Airbnb’s Main Database in Two Weeks"](https://medium.com/airbnb-engineering/how-we-partitioned-airbnb-s-main-database-in-two-weeks-55f7e006ff21)
- [Amazon RDS for SQL Server – Support for Windows Authentication](https://aws.amazon.com/blogs/aws/amazon-rds-for-sql-server-support-for-windows-authentication/)
- [Why Support of PostgreSQL 9.5 by Amazon RDS is Such Great News](http://blog.rubyroidlabs.com/2016/04/postgresql-9-5/)
- [AWS Tutorials: Create and Connect to a MySQL Database with Amazon RDS](https://aws.amazon.com/getting-started/tutorials/create-mysql-db/)
- [Migrating from MySQL (RDS) to Aurora with no downtime](http://cantrill.io/howto/aws/2016/06/06/migrating-from-mysql-to-aurora-with-almost-no-downtime.html)
- [Replicating Amazon Aurora DB Clusters Across AWS Regions](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Replication.CrossRegion.html)
- [Working with PostgreSQL, MySQL, and MariaDB Read Replicas - Amazon](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) Use RDS PostgreSQL cross-region Read Replicas to get data close to customers.
- [Working with an Amazon RDS DB Instance in a VPC](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)
- [Creating a DB Instance Running the Oracle Database Engine](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateOracleInstance.html) In RDS, create Oracle Standard Edition 2 DB instances with the License Included model.
- [Oracle Database on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/10/oracle-database-on-the-aws-cloud-quick-start-reference-deployment/)
- [besanttechnologies.com: AWS – Relational Database Service](https://www.besanttechnologies.com/amazon-web-services-relational-database)
- [Introducing the Aurora Storage Engine](https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine/)
- [dzone: AWS Relational Database Service (RDS): PostgreSQL in Cloud](https://dzone.com/articles/aws-relational-database-service-rds-postgresql-in) Today, we will go into details of Amazon RDS. We also set up a PostgreSQL instance using this service and connect to it using a tool Azure Data Studio.
- [sysadminxpert.com: How to Enable Slow Query Logs in AWS RDS MySQL](https://sysadminxpert.com/how-to-enable-slow-query-logs-in-aws-rds-mysql/)
- [New – Create Microsoft SQL Server Instances of Amazon RDS on AWS Outposts](https://aws.amazon.com/blogs/aws/new-create-microsoft-sql-server-instances-of-amazon-rds-on-aws-outposts/)
- [percona.com: The Benefits of Amazon RDS for MySQL](https://www.percona.com/blog/2019/12/19/the-benefits-of-amazon-rds-for-mysql/)
- [medium: AWS Backup Service for Amazon RDS](https://medium.com/avmconsulting-blog/aws-backup-service-for-amazon-rds-3e6f5827aa66)
- [migops.com: Is Aurora PostgreSQL really faster and cheaper than RDS PostgreSQL – Benchmarking](https://www.migops.com/blog/2021/11/26/is-aurora-postgresql-really-faster-and-cheaper-than-rds-postgresql-benchmarking/)
- [==dashbird.io: [Infographic] AWS RDS from a Serverless perspective==](https://dashbird.io/blog/aws-relational-database-rds/)
- [==Auditing for highly regulated industries using Amazon Aurora PostgreSQL==](https://aws.amazon.com/blogs/database/auditing-for-highly-regulated-industries-using-amazon-aurora-postgresql/)
- [New Amazon RDS for MySQL & PostgreSQL Multi-AZ Deployment Option: Improved Write Performance & Faster Failover](https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-db-cluster/)
- [Amazon Aurora PostgreSQL blue/green deployment using fast database cloning](https://aws.amazon.com/blogs/database/amazon-aurora-postgresql-blue-green-deployment-using-fast-database-cloning/)
- [Securely connect to an Amazon RDS or Amazon EC2 database instance remotely with your preferred GUI](https://aws.amazon.com/blogs/database/securely-connect-to-an-amazon-rds-or-amazon-ec2-database-instance-remotely-with-your-preferred-gui/)
- [Modernize database stored procedures to use Amazon Aurora PostgreSQL federated queries, pg_cron, and AWS Lambda](https://aws.amazon.com/blogs/database/modernize-database-stored-procedures-to-use-amazon-aurora-postgresql-federated-queries-pg_cron-and-aws-lambda/)
- [Let’s Architect! Architecting with Amazon DynamoDB](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-with-amazon-dynamodb/)
- [itnext.io: Manage Redis on AWS from Kubernetes](https://itnext.io/manage-redis-on-aws-from-kubernetes-eeadba7eb889)
- [thenewstack.io: Diving into AWS Databases: Amazon RDS and DynamoDB Explained](https://thenewstack.io/diving-into-aws-databases-amazon-rds-and-dynamodb-explained/) A look at the differences between these popular options, and between relational and nonrelational databases.

## AWS Database Migration Service DMS

- [AWS Database Migration Service](https://aws.amazon.com/blogs/aws/aws-database-migration-service/)
- [Whitepaper: Migrating Your Databases to AWS](https://aws.amazon.com/dms/learn-more/)
- [Replicate and transform data in Amazon Aurora PostgreSQL across multiple Regions using AWS DMS](https://aws.amazon.com/blogs/database/replicate-and-transform-data-in-amazon-aurora-postgresql-across-multiple-regions-using-aws-dms)
- [Amazon RDS for PostgreSQL Enhancements: Support for new minor versions, Logical Replication, and Amazon RDS PostgreSQL as a source for AWS DMS](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-rds-for-postgresql-enhancements-support-for-new-minor-versions-logical-replication-and-amazon-rds-postgresql-as-a-source-for-aws-dms/)
- [Migrating Oracle databases with near-zero downtime using AWS DMS](https://aws.amazon.com/blogs/database/migrating-oracle-databases-with-near-zero-downtime-using-aws-dms/)
- [Migrating a commercial database to open source with AWS SCT and AWS DMS](https://aws.amazon.com/blogs/database/migrating-a-commercial-database-to-open-source-with-aws-sct-and-aws-dms/)
- [revenuecat.com: Replicating a postgresql cluster to redshift](https://www.revenuecat.com/blog/replicating-a-postgresql-cluster-to-redshift)

## AWS RDS Proxy

- [Amazon RDS Proxy – Now Generally Available](https://aws.amazon.com/es/blogs/aws/amazon-rds-proxy-now-generally-available/) A fully managed, highly available database proxy for Amazon Relational Database Service (RDS) that makes applications more scalable, more resilient to database failures, and more secure.

## AWS Schema Conversion Tool

- [cloudacademy.com: Migrating Data to AWS Using the AWS Schema Conversion Tool: A Preview](http://cloudacademy.com/blog/migrating-data-to-aws/)
- [AWS Schema Conversion Tool now supports PostgreSQL as conversion target](http://aws.amazon.com/about-aws/whats-new/2016/01/aws-schema-conversion-tool-postgresql-support/)
- [Creating an AWS Schema Conversion Tool Project](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_SchemaConversionTool.Converting.CreateProject.html) Use SSL to connect to your source DB with the AWS Schema Conversion Tool.
- [AWS Schema Conversion Tool now supports conversions from Oracle DW and Teradata to Amazon Redshift, Embedded Code Conversion, and Cloud native Code Optimization](https://aws.amazon.com/es/about-aws/whats-new/2016/07/aws-schema-conversion-tool-now-supports-conversions-from-oracle-dw-and-teradata-to-amazon-redshift-embedded-code-conversion-and-cloud-native-code-optimization)

## AWS Redshift

- [Tutorial: Tuning Table Design](http://docs.aws.amazon.com/redshift/latest/dg/tutorial-tuning-tables.html) In this tutorial, you will learn how to optimize the design of your tables.

## AWS Data Mesh and Batch Data Processing

- [dev.to: Introduction to Data Mesh](https://dev.to/aws-builders/introduction-to-data-mesh-3f1b)
- [dev.to: Introduction to Batch Data Processing](https://dev.to/aws-builders/introduction-to-batch-data-processing-4k56)

## AWS NoSQL DynamoDB

- [Easily model your app data in a NoSQL database with AWS Mobile Hub](https://aws.amazon.com/es/about-aws/whats-new/2016/06/easily-model-your-app-data-in-a-nosql-database-with-aws-mobile-hub/)
- [medium: An Ultimate Guide to AWS Serverless database — DynamoDB](https://medium.com/javascript-in-plain-english/an-ultimate-guide-to-aws-serverless-database-dynamodb-aa048a62f2da) AWS DynamoDb is a fully managed, NoSQL, Single digit latency, a serverless database that can handle any kind of online workloads.