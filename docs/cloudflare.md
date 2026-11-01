# Cloudflare Public Cloud

## Email Services
  - [How to Set Up a Custom Email with Cloudflare and Mailgun](https://www.freecodecamp.org/news/how-to-set-up-custom-email) - This article provides a step-by-step guide on how to set up a custom email address (e.g., info@yourdomain.com) for free using Cloudflare for DNS management and Mailgun for email services. It explains how to integrate these services to manage custom emails directly within a Gmail inbox, focusing on efficiency, reliability, and security.

- [cloudflare.com](https://www.cloudflare.com)
- [Cloudflare workers (Serverless)](https://www.cloudflare.com/products/workers)
- [venturebeat.com: Cloudflare acquires Linc to automate web app deployment](https://venturebeat.com/2020/12/22/cloudflare-acquires-linc-to-automate-web-app-deployment)
- [blog.cloudflare.com: Network Performance Update: Full Stack Week](https://blog.cloudflare.com/network-performance-update-full-stack-week)
- [blog.cloudflare.com: Guest Blog: k8s tunnels with Kudelski Security](https://blog.cloudflare.com/guest-blog-zero-trust-access-kubernetes)
- [blog.cloudflare.com: Zero Trust Private Networking Rules](https://blog.cloudflare.com/zero-trust-private-networking-rules)
  - **(2026)** [Cloudflare DMARC Management is now generally available](https://blog.cloudflare.com/dmarc-management-ga) 🌟 - Cloudflare's DMARC Management reaches General Availability, providing deeper email reporting and automated SPF auditing free to all customers.

## Serverless
  - **(2026)** [How we built saga rollbacks for Cloudflare Workflows](https://blog.cloudflare.com/rollbacks-for-workflows) 🌟 - Cloudflare introduces native saga rollbacks for its serverless Workflows engine to ensure transaction consistency.
  - **(2026)** [Temporary Cloudflare Accounts for AI agents](https://blog.cloudflare.com/temporary-accounts) 🌟 - Cloudflare introduces frictionless, ephemeral deployments via wrangler deploy --temporary to support autonomous AI agent workflows.

## Security
  - **(2026)** [The White House's post-quantum executive order is an important milestone. It's time to get to work](https://blog.cloudflare.com/post-quantum-eo-2026) 🌟 - An evaluation of US Executive Order 14412 on post-quantum encryption and Cloudflare's tactical migration playbook.
  - **(2026)** [Celebrating 12 years of Project Galileo](https://blog.cloudflare.com/celebrating-12-years-of-project-galileo) 🌟 - Cloudflare celebrates its humanitarian cybersecurity initiative with its first comprehensive annual report on attacks targeting civil society.
  - **(2026)** [Introducing the Cloudflare One stack: agent-powered deployment](https://blog.cloudflare.com/cloudflare-one-stack) 🌟 - Cloudflare introduces a native skill library enabling AI agents to plan, deploy, and govern Zero Trust SASE environments.
  - **(2026)** [Introducing Adaptive Intelligence: undermining the economics of every bot attack](https://blog.cloudflare.com/introducing-adaptive-intelligence) 🌟 - Cloudflare introduces Adaptive Intelligence, a system that continuously retrains its bot detection models to generate disposable rules based on live traffic.
  - **(2026)** [BotBase for Operators: A clearer path to joining Cloudflare's directory of bots and agents](https://blog.cloudflare.com/botbase-for-operators) 🌟 - Cloudflare launches BotBase for Operators, a dedicated dashboard offering status tracking and behavioral modeling for AI agents and bot operators.
  - **(2026)** [Say it once: introducing Bot Preference Sync](https://blog.cloudflare.com/bot-preference-sync) 🌟 - Bot Preference Sync automatically aligns a site's robots.txt file with the AI bot policies configured in the Cloudflare dashboard.
  - **(2026)** [Enforce positive security with Cloudflare Application Profiles](https://blog.cloudflare.com/application-profiles) 🌟 - Cloudflare Application Profiles learn HTTP request structures to enforce positive security and detect AI-generated attack payloads.
  - **(2026)** [Preventing quantum downgrade attacks against IPsec](https://blog.cloudflare.com/ipsec-downgrade-protection) 🌟 - Cloudflare and IETF's transcript authentication extension prevents quantum downgrade attacks on IPsec connections.
  - **(2026)** [DDoS threat report for 2026 Q3](https://blog.cloudflare.com/ddos-threat-report-2026-q3) 🌟 - Cloudflare's Q3 2026 DDoS threat report reveals the mitigation of 18.2 million network-layer attacks, noting a distinct shift toward short-duration, high-density swarms.
  - **(2026)** [Bringing post-quantum cryptography to geographically fenced key management](https://blog.cloudflare.com/post-quantum-geo-key-manager) 🌟 - Cloudflare's new post-quantum GeoKey Manager protects geographically fenced decryption keys from harvest now, decrypt later attacks.
  - **(2026)** [Introducing full transaction detection for Cloudflare WAF](https://blog.cloudflare.com/full-transaction-waf) 🌟 - Cloudflare introduces full transaction detection and response rules for WAF to identify and block exploits by evaluating HTTP requests alongside their responses.
  - **(2026)** [Cloudflare deploys protections against php2shell vulnerability](https://blog.cloudflare.com/php-vulnerabilities-waf-protection) 🌟 - Cloudflare successfully deployed multiple WAF mitigations for all customers to block the php2shell vulnerabilities (CVE-2026-109618, CVE-2026-109619) ahead of public disclosure.
  - **(2026)** [8 eMudhra certificates are compromised. Here's what you need to know](https://blog.cloudflare.com/emudhra-certificate-compromise) 🌟 - Cloudflare details the compromise of eight eMudhra intermediate certificates and outlines mitigation steps to prevent active exploitation across the Internet.
  - **(2026)** [Continuous accountability for Verified bots](https://blog.cloudflare.com/verified-bots-accountability) 🌟 - Cloudflare introduces a continuous evaluation system to ensure Verified bots strictly honor website preferences like robots.txt and HTTP 429s.
  - **(2026)** [A fully programmable secure web gateway](https://blog.cloudflare.com/programmable-gateway-dlp) 🌟 - Cloudflare integrates its Developer Platform with Gateway and Data Loss Prevention to enable programmable, custom inline security enforcement.

## Networking
  - **(2026)** [How we found a bug in the hyper HTTP library](https://blog.cloudflare.com/hyper-bug) 🌟 - Cloudflare engineers isolate and patch an elusive, multi-version connection pooling bug in Rust's open-source hyper library.
  - **(2026)** [Route public traffic to private applications with Cloudflare](https://blog.cloudflare.com/private-origins-dns-routing) 🌟 - Cloudflare launches Application Services for Private Origins, enabling secure routing of edge-protected traffic directly into private networks without public IPs or connectors.
  - **(2026)** [How we saved 100 terabytes of memory by optimizing 1.1.1.1's DNS cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111) 🌟 - Cloudflare reduced the per-entry memory footprint of its 1.1.1.1 DNS cache by 56%, saving 100 TB of RAM fleet-wide through low-level Rust optimizations.
  - **(2026)** [Cloudflare services for private origins is now generally available](https://blog.cloudflare.com/private-origins-public-to-private) 🌟 - Cloudflare announces general availability of services for private origins, allowing users to point a proxied record at a private IP via Cloudflare One without opening inbound firewalls.
  - **(2026)** [What Took the Internet Offline in Q3 2026](https://blog.cloudflare.com/q3-2026-internet-disruption-summary) 🌟 - Cloudflare Radar documents the root causes of major global internet disruptions in Q3 2026, covering power failures, natural disasters, and government shutdowns.

## Case Studies
  - **(2026)** [The Cloudflare Blog – Brought to you by EmDash](https://blog.cloudflare.com/cloudflare-blog-uses-emdash) 🌟 - Cloudflare migrated its official blog to EmDash, a new Astro-based CMS, achieving extreme resilience and native MCP integration.

## Domains
  - **(2026)** [Simplifying domains for people and agents](https://blog.cloudflare.com/simplifying-domains) 🌟 - Cloudflare Registrar launches a new fast search experience across 420+ extensions, accessible via Workers, WebSockets, and API/CLI for agent-based domain management.

## Developer Tools
  - **(2026)** [Introducing cf: the agentic CLI for the entire Cloudflare API](https://blog.cloudflare.com/cloudflare-cf-cli-launch) 🌟 - A next-generation CLI tailored for agentic development, exposing thousands of Cloudflare API endpoints natively.
  - **(2026)** [Deploy with Void - Cloudflare Blog](https://blog.cloudflare.com/deploy-with-void) 🌟 - Introducing Void: an open-source SDK, CLI, and self-hosted platform for building full-stack Vite apps and deploying them to Cloudflare.
