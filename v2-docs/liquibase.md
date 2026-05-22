# Liquibase

!!! info "Architectural Context"
    Detailed reference for Liquibase in the context of Hardened Infrastructure.

## Cloud Infrastructure

### Kubernetes

#### Database Design

  - **(2021)** [**piotrminkowski.com: Blue-green deployment with a database on Kubernetes 🌟**](https://piotrminkowski.com/2021/02/18/blue-green-deployment-with-a-database-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An in-depth technical guide on achieving zero-downtime blue-green deployments on Kubernetes when database schema migrations are involved. It covers database backward compatibility, Liquibase integration, and rollout patterns to mitigate deployment risks.
## Software Architecture

### Database Design (1)

#### Database-as-a-Service

  - **(2023)** [**docs.planetscale.com: The PlanetScale workflow 🌟**](https://planetscale.com/docs/vitess/best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An architectural guide detailing the innovative non-blocking database branch and deployment workflow of PlanetScale (built on Vitess).

*   Explains how schema migrations can be isolated, tested, and applied safely.
*   Guarantees zero production downtime or database table locks.
#### GitOps

  - **(2026)** [==bytebase/bytebase==](https://github.com/bytebase/bytebase) <span class='md-tag md-tag--info'>⭐ 14049</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source, web-based database schema change and collaboration tool designed for developers and DBAs. Implementing a "Database GitOps" workflow, it provides multi-tenant database change management, visual SQL review, and centralized security compliance pipelines.
#### Migration Patterns

  - **(2026)** [==liquibase.org==](http://www.liquibase.org) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A leading open-source database schema migration tool that enables teams to track, version, and deploy database changes. It abstracts SQL schemas into XML, YAML, JSON, or plain SQL, facilitating seamless CI/CD integration and deployment across diverse environments.
  - **(2016)** [==martinfowler.com==](https://martinfowler.com/articles/evodb.html) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The classic foundational article on Evolutionary Database Design.

*   Defines how to apply Continuous Integration and automated database migrations within modern software lifecycles.
*   Establishes safe practices for database change control that are compatible with agile methodologies.
  - **(2020)** [percona: Database Schema Management Via Liquibase](https://www.percona.com/community-blog/2020/10/01/database-schema-management-via-liquibase)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical blog post by Percona illustrating step-by-step database schema version control using Liquibase. It highlights integration patterns with enterprise relational databases (MySQL, PostgreSQL) and demonstrates rollback strategies to ensure zero-downtime database upgrades.

---
💡 **Explore Related:** [Devsecops](./devsecops.md) | [Crossplane](./crossplane.md) | [Pulumi](./pulumi.md)

