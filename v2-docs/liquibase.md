# Liquibase

!!! info "Architectural Context"
    Detailed reference for Liquibase in the context of Hardened Infrastructure.

## Standard Reference

  - [Flyway](https://www.red-gate.com/products/flyway/community)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [wikipedia](https://en.wikipedia.org/wiki/Evolutionary_database_design)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: Introduction to Liquibase and Managing Your Database Source Code](https://dzone.com/articles/introduction-to-liquibase-and-managing-your-databa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: Managing Your Database With Liquibase and Gradle](https://dzone.com/articles/managing-your-database-with-liquibase-and-gradle)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: Executing Liquibase: 3 Use Cases](https://dzone.com/articles/executing-liquibase-3-use-cases)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: Build a Spring Boot App With Flyway and Postgres](https://dzone.com/articles/build-a-spring-boot-app-with-flyway-and-postgres)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Database version control — Liquibase versus Flyway](https://medium.com/@ruxijitianu/database-version-control-liquibase-versus-flyway-9872d43ee5a4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Infrastructure

### Kubernetes

#### Database Design

  - [piotrminkowski.com: Blue-green deployment with a database on Kubernetes' 🌟](https://piotrminkowski.com/2021/02/18/blue-green-deployment-with-a-database-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An in-depth technical guide on achieving zero-downtime blue-green deployments on Kubernetes when database schema migrations are involved. It covers database backward compatibility, Liquibase integration, and rollout patterns to mitigate deployment risks.
## Software Architecture

### Database Design (1)

#### Database-as-a-Service

  - **(2023)** [**docs.planetscale.com: The PlanetScale workflow 🌟**](https://planetscale.com/docs/vitess/best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An architectural guide detailing the innovative non-blocking database branch and deployment workflow of PlanetScale (built on Vitess).

*   Explains how schema migrations can be isolated, tested, and applied safely.
*   Guarantees zero production downtime or database table locks.
#### GitOps

  - [bytebase/bytebase](https://github.com/bytebase/bytebase) <span class='md-tag md-tag--info'>⭐ 14049</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An open-source, web-based database schema change and collaboration tool designed for developers and DBAs. Implementing a "Database GitOps" workflow, it provides multi-tenant database change management, visual SQL review, and centralized security compliance pipelines.
#### Migration Patterns

  - **(2026)** [==liquibase.org==](http://www.liquibase.org) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A leading open-source database schema migration tool that enables teams to track, version, and deploy database changes. It abstracts SQL schemas into XML, YAML, JSON, or plain SQL, facilitating seamless CI/CD integration and deployment across diverse environments.
  - [martinfowler.com](https://martinfowler.com/articles/evodb.html)  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The classic foundational article on Evolutionary Database Design.

*   Defines how to apply Continuous Integration and automated database migrations within modern software lifecycles.
*   Establishes safe practices for database change control that are compatible with agile methodologies.

---
💡 **Explore Related:** [Kubernetes Security](./kubernetes-security.md) | [Devsecops](./devsecops.md) | [Kustomize](./kustomize.md)

