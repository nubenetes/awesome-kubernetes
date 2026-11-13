# 🎥 DevOps, IaC, and SRE

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/).

Welcome to the **DevOps, IaC, and SRE** section of the V2 Video Hub. Explore curated high-density videos with architectural summaries.

## Prometheus

??? note "🎬 Prometheus: The Documentary"
    !!! info "Architectural Summary"
        This documentary explores the architectural genesis of Prometheus at SoundCloud, detailing how the shift to microservices necessitated a fundamental pivot from host-based monitoring to a pull-based, multi-dimensional metric data model. In a 2026 cloud-native context, understanding these foundational design decisions—specifically the trade-offs of localized TSDB storage, HTTP pull mechanics, and PromQL—is vital for architecting self-healing, high-cardinality observability pipelines across distributed, edge, and hybrid-cloud environments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="rT4fJNbfe14" data-video-url="https://www.youtube.com/embed/rT4fJNbfe14" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/rT4fJNbfe14/hqdefault.jpg" alt="Prometheus: The Documentary" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform and Azure Verified Modules

??? note "🎬 Nubenetes Azure Verified Modules (AVM) Terraform Labs (Playlist)"
    !!! info "Architectural Summary"
        Hands-on implementation labs and end-to-end Terraform walkthrough for Microsoft Azure Verified Modules (AVM). Covers toolchain setup (VS Code, Azure CLI, Terraform), Log Analytics centralized telemetry sinks, Azure Key Vault secret management, Storage Account Customer-Managed Key (CMK) encryption, Private Endpoints network isolation, zero public IP VM access via Azure Bastion, System-Assigned Managed Identity RBAC, and deterministic infrastructure lifecycle automation.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLNKD2Ya-t0zM" title="Nubenetes Azure Verified Modules (AVM) Terraform Labs (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes Azure Landing Zones 2026: Enterprise CAF and Architecture Blueprint (Playlist)"
    !!! info "Architectural Summary"
        Comprehensive masterclass and enterprise reference architecture for Microsoft Cloud Adoption Framework (CAF) Azure Landing Zones (2026). Covers the retirement of the legacy monolithic CAF module in favor of Azure Verified Modules (AVM) and ALZ Library (2026.10.0), Management Groups hierarchy (Corp vs Online), Customer-Managed Hub-and-Spoke vs Microsoft-Managed Virtual WAN (vWAN), Private Endpoints vs Service Endpoints security perimeters, and Workload Identity Federation (OIDC) zero-secret CI/CD.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLCgDGrDt3kNU" title="Nubenetes Azure Landing Zones 2026: Enterprise CAF and Architecture Blueprint (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Azure Verified Modules Lab: Complete Terraform End-to-End Walkthrough"
    !!! info "Architectural Summary"
        Hands-on technical walkthrough demonstrating how to compose and deploy production Azure infrastructure using Terraform Azure Verified Modules (AVM), enforcing RBAC, private endpoints, and diagnostic telemetry out of the box.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="I4s0A1uXEUg" data-video-url="https://www.youtube.com/embed/I4s0A1uXEUg" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/I4s0A1uXEUg/hqdefault.jpg" alt="Azure Verified Modules Lab: Complete Terraform End-to-End Walkthrough" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 Retiring the CAF Monolith: Azure Verified Modules (AVM) and ALZ Library 2026"
    !!! info "Architectural Summary"
        Explains the architectural migration from the legacy monolithic CAF Enterprise-Scale Terraform module to the decoupled Azure Landing Zones (ALZ) library and composable Azure Verified Modules (AVM).

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="BNEGxzQgDB8" data-video-url="https://www.youtube.com/embed/BNEGxzQgDB8" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/BNEGxzQgDB8/hqdefault.jpg" alt="Retiring the CAF Monolith: Azure Verified Modules (AVM) and ALZ Library 2026" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 ALZ 2026 Masterclass: Modular Architecture and AVM Rebuild"
    !!! info "Architectural Summary"
        Comprehensive architectural masterclass analyzing the modular rebuild of Azure Landing Zones (ALZ) for 2026 using Terraform Azure Verified Modules (AVM) and policy-as-code guardrails.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="HjLte2SGCk0" data-video-url="https://www.youtube.com/embed/HjLte2SGCk0" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/HjLte2SGCk0/hqdefault.jpg" alt="ALZ 2026 Masterclass: Modular Architecture and AVM Rebuild" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 How Azure Key Vault Secures Infrastructure | AVM Secret Management"
    !!! info "Architectural Summary"
        Demonstrates how the Azure Verified Module for Key Vault (avm-res-keyvault-vault) provisions a hardened vault, generates cryptographic SSH keys in-cloud, and injects virtual machine credentials during Terraform deployments without exposing plaintext secrets on developer workstations.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="-JlLcd-4CIs" data-video-url="https://www.youtube.com/embed/-JlLcd-4CIs" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/-JlLcd-4CIs/hqdefault.jpg" alt="How Azure Key Vault Secures Infrastructure | AVM Secret Management" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 How Local Code Builds Azure Clouds | AVM Terraform Labs Toolchain"
    !!! info "Architectural Summary"
        Explains how platform engineers combine Visual Studio Code (with official Terraform schema validation), the Azure CLI (for authenticated Entra ID control-plane sessions), and the Terraform CLI to orchestrate deterministic Azure Verified Modules (AVM) deployments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="BnkctVGCD8A" data-video-url="https://www.youtube.com/embed/BnkctVGCD8A" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/BnkctVGCD8A/hqdefault.jpg" alt="How Local Code Builds Azure Clouds | AVM Terraform Labs Toolchain" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 How Azure Verified Modules Automate CMK Encryption | Storage and Key Vault"
    !!! info "Architectural Summary"
        Demonstrates how the Azure Verified Module for Storage Accounts (avm-res-storage-storageaccount) automates the Customer-Managed Key (CMK) cryptographic permission handshake in a single declarative Terraform block, provisioning Managed Identities and assigning Key Vault Crypto Officer roles automatically.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="-Bo6tLrseDo" data-video-url="https://www.youtube.com/embed/-Bo6tLrseDo" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/-Bo6tLrseDo/hqdefault.jpg" alt="How Azure Verified Modules Automate CMK Encryption | Storage and Key Vault" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform CI CD and GitOps

??? note "🎬 Day 0 to Day 2: Zero-Secret CI/CD Pipelines with GitHub Actions and OIDC"
    !!! info "Architectural Summary"
        Architectural deep-dive into building zero-secret Terraform CI/CD pipelines from Day 0 bootstrap to Day 2 continuous operations using GitHub Actions and OpenID Connect (OIDC) Workload Identity Federation on Azure.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="IcH7LalL5cc" data-video-url="https://www.youtube.com/embed/IcH7LalL5cc" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/IcH7LalL5cc/hqdefault.jpg" alt="Day 0 to Day 2: Zero-Secret CI/CD Pipelines with GitHub Actions and OIDC" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 Azure Landing Zones 2026: Automated Framework and Zero-Secret CI/CD"
    !!! info "Architectural Summary"
        Examines the automated bootstrap framework for Azure Landing Zones 2026, combining Terraform AVM starter modules with federated OIDC authentication and gated deployment environments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="mZ944GFanYc" data-video-url="https://www.youtube.com/embed/mZ944GFanYc" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/mZ944GFanYc/hqdefault.jpg" alt="Azure Landing Zones 2026: Automated Framework and Zero-Secret CI/CD" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform Enterprise

??? note "🎬 Standardizing infrastructure automation with Terraform Enterprise"
    !!! info "Architectural Summary"
        This presentation details AXA Group's cloud migration strategy (ATLAS) utilizing Terraform Enterprise as the cornerstone of their multi-cloud and private IaaS migration factory. It highlights how a highly regulated financial enterprise standardizes infrastructure-as-code (IaC) practices across multiple global subsidiaries to accelerate cloud adoption while maintaining governance. For a 2026 cloud-native landscape, this case study provides key insights into scaling self-service provisioning, implementing policy-as-code, and automating multi-tenant enterprise architectures at massive scale.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="PxyyY7TsCqs" data-video-url="https://www.youtube.com/embed/PxyyY7TsCqs?si=kzCRojDteESqork1" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/PxyyY7TsCqs/hqdefault.jpg" alt="Standardizing infrastructure automation with Terraform Enterprise" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform Testing and Validation

??? note "🎬 Azure Landing Zones Testing Strategies: Canary, Sandboxes and Non-Prod"
    !!! info "Architectural Summary"
        Details multi-stage testing strategies for enterprise Infrastructure as Code, including sandbox management groups, canary policy rollouts, and automated Terraform validation gates.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="N6PMQzmBwwE" data-video-url="https://www.youtube.com/embed/N6PMQzmBwwE" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/N6PMQzmBwwE/hqdefault.jpg" alt="Azure Landing Zones Testing Strategies: Canary, Sandboxes and Non-Prod" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## FinOps and Cloud Cost Optimization

??? note "🎬 Nubenetes Azure Hybrid IaaS FinOps Framework (Playlist)"
    !!! info "Architectural Summary"
        Enterprise FinOps architectural framework, mathematical break-even decision models, and continuous automation for hybrid Microsoft Azure IaaS environments (Windows Server, SQL Server on VMs, Hub-and-Spoke networking, ExpressRoute, and Azure Monitor). Covers Azure Hybrid Benefit (AHUB), Constrained vCPUs, Premium SSD v2 decoupling, edge log filtering via AMA and DCR, and sustainable cloud cost reduction ($173k to $39k/mo).

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLaNxiRbEBYJ8" title="Nubenetes Azure Hybrid IaaS FinOps Framework (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes Kubernetes Rightsizing and FinOps (Playlist)"
    !!! info "Architectural Summary"
        Pod failure analysis, container CPU/memory resource optimization, VPA/Goldilocks strategies, and AI-driven workload rightsizing for Kubernetes clusters.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLZ-bpd1sEISs" title="Nubenetes Kubernetes Rightsizing and FinOps (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## HashiCorp Stack Terraform Vault Consul Boundary

??? note "🎬 Building a developer platform? Ask these questions."
    !!! info "Architectural Summary"
        This session details how to build secure, scalable developer platforms by defining 'golden paths' using HashiCorp's suite of automation tools, including Terraform, Vault, Consul, and Boundary. It provides a strategic framework for resolving key platform engineering challenges such as Day 2 operations, infrastructure dependency mapping, secure access control, and seamless local-to-remote environment transitions. By abstracting cloud complexity, the session demonstrates how to deliver high-velocity self-service capabilities to development teams while ensuring governance and security compliance.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="1Fl25dR01pw" data-video-url="https://www.youtube.com/embed/1Fl25dR01pw?si=bJlQozIfT3J4rhN3" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/1Fl25dR01pw/hqdefault.jpg" alt="Building a developer platform? Ask these questions." class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## eBPF and OpenTelemetry

??? note "🎬 Nubenetes Kubernetes and Multi-Cloud Observability with OpenTelemetry eBPF (OBI) (Playlist)"
    !!! info "Architectural Summary"
        Architectural masterclass and production blueprints for multi-cloud Kubernetes observability using OpenTelemetry eBPF (OBI). Covers the multi-backend OpenTelemetry Collector routing blueprint, high-throughput tail-based sampling (80%-95% cost reduction), Grafana LGTM stack integration (tracesToLogsV2), and Zero-Grafana native observability across Red Hat OpenShift, Azure AKS, AWS, and GCP.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLRTV86SuuRbk" title="Nubenetes Kubernetes and Multi-Cloud Observability with OpenTelemetry eBPF (OBI) (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes eBPF Metrics and Telemetry: Kernel Maps, OBI and Prometheus (Playlist)"
    !!! info "Architectural Summary"
        Zero-code application RED metrics (Golden Signals), Linux kernel socket probes (sockops/tcp_recvmsg), self-monitoring eBPF map capacity, and Prometheus/Mimir Exemplars using OpenTelemetry eBPF (OBI). Covers multi-backend Collector pipelines, GitOps PrometheusRule alerting, multi-cloud architectures (OpenShift, AKS, EKS, GKE, SigNoz), and architectural boundaries.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLZhOsH66dFmw" title="Nubenetes eBPF Metrics and Telemetry: Kernel Maps, OBI and Prometheus (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes Browser to Kernel: Full-Stack eBPF Observability (OBI) (Playlist)"
    !!! info "Architectural Summary"
        Full-stack zero-code observability from client-side Single Page Applications (React, Angular) and Server-Side Rendering (Next.js, Node.js) down to Linux host kernel eBPF log enrichment using OpenTelemetry OBI. Covers W3C Trace Context (traceparent) propagation, frontend session correlation, and automated incident triage.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLIDgJtbMXQ6s" title="Nubenetes Browser to Kernel: Full-Stack eBPF Observability (OBI) (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes OpenTelemetry eBPF (OBI) Zero-Code Trace-Log Correlation (Playlist)"
    !!! info "Architectural Summary"
        Production-ready architecture, Linux kernel internals, and incident triage workflows for zero-code trace-log correlation using OpenTelemetry eBPF Instrumentation (OBI). Covers in-flight trace ID injection, write/writev syscall tracing, async runtime caveats, and downstream pipeline tuning with Fluent Bit, Vector, and OpenTelemetry Collector.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLYmAuttxFYjA" title="Nubenetes OpenTelemetry eBPF (OBI) Zero-Code Trace-Log Correlation (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## ArgoCD and GitOps

??? note "🎬 Nubenetes ArgoCD and GitOps Automation (Playlist)"
    !!! info "Architectural Summary"
        Declarative GitOps deployments, ArgoCD ApplicationSets, sync waves, multi-cluster architectures, and progressive delivery on Kubernetes and OpenShift.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLYbmzkhLGOtI" title="Nubenetes ArgoCD and GitOps Automation (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Azure DevOps and GitHub Actions

??? note "🎬 Panel: Azure DevOps vs. GitHub Actions"
    !!! info "Architectural Summary"
        This panel discussion provides a comprehensive architectural comparison between Azure DevOps and GitHub Actions, focusing on enterprise governance, extensibility, and CI/CD workflow migration strategies. It outlines decision frameworks for hybrid platform setups, highlighting how organizations can leverage GitHub Actions for modern cloud-native developer velocity while maintaining Azure DevOps for mature project management, test plans, and strict regulatory compliance. Essential for cloud architects planning long-term toolchain evolution, this session clarifies integration pathways and future-proof migration strategies.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="8g4qLzkpjeE" data-video-url="https://www.youtube.com/embed/8g4qLzkpjeE?si=xcfl3ugsMGZ8Kthg" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/8g4qLzkpjeE/hqdefault.jpg" alt="Panel: Azure DevOps vs. GitHub Actions" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## DevSecOps

??? note "🎬 What is DevSecOps? DevSecOps explained in 8 Mins"
    !!! info "Architectural Summary"
        This video details the transition from traditional, late-stage security audits to DevSecOps, explaining how shifting security left eliminates deployment bottlenecks in fast-paced delivery pipelines. It covers the automation of static analysis (SAST), software composition analysis (SCA), and container scanning directly within CI/CD workflows. In a 2026 cloud-native context, this paradigm is critical for securing ephemeral microservices and maintaining continuous compliance without sacrificing deployment velocity.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="nrhxNNH5lt0" data-video-url="https://www.youtube.com/embed/nrhxNNH5lt0?si=U5h1mbkbF6ZEOvlj" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/nrhxNNH5lt0/hqdefault.jpg" alt="What is DevSecOps? DevSecOps explained in 8 Mins" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## FinOps

??? note "🎬 The Brutal Truth Behind Tech Layoffs"
    !!! info "Architectural Summary"
        This analysis dissects the macroeconomic shift from hyper-growth talent hoarding to hyper-efficiency, highlighting the systemic collapse of bloated engineering teams in favor of lean, automated operations. For a 2026 cloud-native landscape, this underscores the critical role of platform engineering and robust FinOps architectures designed to maximize resource utilization while minimizing human-in-the-loop operational overhead. Architects must leverage these insights to build self-healing, highly automated platforms that successfully decouple organizational scale from headcount.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="hAwtrJlBVJY" data-video-url="https://www.youtube.com/embed/hAwtrJlBVJY?si=bnyptzNFx4jzOiEj" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/hAwtrJlBVJY/hqdefault.jpg" alt="The Brutal Truth Behind Tech Layoffs" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## GitOps

??? note "🎬 GitOps Guide to the Galaxy"
    !!! info "Architectural Summary"
        Every other Thursday at 3pm ET hosts Hilliary Lipsig and Jonathan Rickard dive into everything in the GitOps universe, from solutions to common problems in end-to-end CICD pipelines, to creating Git workflows. This series explores how GitOps enhances modern application delivery and discusses the latest news around best practices and Cloud Native architecture.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=zdATyq_E2wXN7AC6&amp;list=PLbMP1JcGBmSGKO8UreWpOBOhCqilejhtd" title="GitOps Guide to the Galaxy" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Jenkins

??? note "🎬 Jenkins Tutorials"
    !!! info "Architectural Summary"
        This comprehensive video series details core Jenkins CI/CD automation techniques, including Pipeline-as-Code implementations and system management best practices. In a 2026 cloud-native context, mastering Jenkins remains critical for orchestrating complex build pipelines, bridging the gap between legacy infrastructure and modern Kubernetes deployment targets. The tutorials provide foundational architectural patterns for establishing scalable, automated, and reproducible continuous integration workflows across distributed enterprise environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=GBJtqv36O8bslj9z&amp;list=PLvBBnHmZuNQJeznYL2F-MpZYBUeLIXYEe" title="Jenkins Tutorials" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Terraform Azure Verified Modules AVM

??? note "🎬 How Terraform Deploys Azure Verified Modules | AVM Lifecycle Short"
    !!! info "Architectural Summary"
        This technical overview examines the four-phase Terraform provisioning lifecycle (init, plan, apply, destroy) utilizing Azure Verified Modules (AVM) to manage complex infrastructure dependencies like private VNet-integrated storage accounts. By mapping architectural relationships into a deterministic state file, it ensures predictable deployment ordering and complete teardown execution. In a 2026 Cloud Native context, adopting standardized modules with strict lifecycle management is essential for preventing configuration drift, eliminating orphaned cloud resources, and enforcing FinOps cost governance.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="EsIyH6PSGrE" data-video-url="https://www.youtube.com/embed/EsIyH6PSGrE" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/EsIyH6PSGrE/hqdefault.jpg" alt="How Terraform Deploys Azure Verified Modules | AVM Lifecycle Short" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 Deploying Secure Azure Architecture with Verified Modules | AVM Labs"
    !!! info "Architectural Summary"
        This video demonstrates how to rapidly provision a hardened, zero-trust Azure foundation using Microsoft's pre-vetted Terraform Azure Verified Modules (AVM) instead of maintaining thousands of lines of custom IaC. It showcases composable patterns that integrate Virtual Networks, automated SSH key vaulting in Azure Key Vault, zero-public-IP compute access via Azure Bastion, and passwordless Storage Account interactions through System-Assigned Managed Identities. In a 2026 Cloud Native context, adopting standardized, vendor-backed IaC modules accelerates deterministic infrastructure delivery while enforcing enterprise-grade security, private endpoints, and RBAC compliance by default.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="xIkzOaSfB1c" data-video-url="https://www.youtube.com/embed/xIkzOaSfB1c" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/xIkzOaSfB1c/hqdefault.jpg" alt="Deploying Secure Azure Architecture with Verified Modules | AVM Labs" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Azure Private Link Terraform

??? note "🎬 How Azure Private Endpoints Lock Down Data | Private PaaS Security"
    !!! info "Architectural Summary"
        This video illustrates how Azure Private Endpoints secure cloud PaaS services like Azure Storage and Key Vault by projecting them directly into virtual network subnets using dedicated RFC 1918 private IP addresses. By integrating Private DNS Zones and eliminating public internet egress, this architecture ensures all sensitive data traffic remains locked within the internal cloud backbone. In a 2026 Cloud Native context, automating this zero-trust network isolation via Terraform and Azure Verified Modules (AVM) is critical for enforcing strict data perimeter compliance.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="xf5UNTUjYjY" data-video-url="https://www.youtube.com/embed/xf5UNTUjYjY" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/xf5UNTUjYjY/hqdefault.jpg" alt="How Azure Private Endpoints Lock Down Data | Private PaaS Security" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Azure Managed Identities Terraform

??? note "🎬 How Managed Identities Kill Passwords | Azure Zero-Secret Security"
    !!! info "Architectural Summary"
        This video illustrates how Azure Managed Identities eliminate static credentials and connection strings in cloud-native architectures by binding workloads directly to Microsoft Entra ID. Rather than embedding vulnerable access keys in configuration files, resources dynamically obtain short-lived, automatically rotated tokens governed by granular RBAC permissions. Implementing this zero-secret pattern with Azure Verified Modules (AVM) in Terraform ensures automated credential lifecycle management and enforces strict least-privilege security postures across cloud environments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="2YlxRtiYll4" data-video-url="https://www.youtube.com/embed/2YlxRtiYll4" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/2YlxRtiYll4/hqdefault.jpg" alt="How Managed Identities Kill Passwords | Azure Zero-Secret Security" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Azure Bastion

??? note "🎬 How Azure Bastion Secures Virtual Machines | Zero Public IP Access"
    !!! info "Architectural Summary"
        This video explains how Azure Bastion enforces zero-trust network architecture by providing secure, seamless RDP and SSH connectivity to virtual machines directly through the Azure portal over TLS, completely eliminating the need for public IP addresses. In a 2026 Cloud Native and Infrastructure as Code (IaC) context—particularly when deployed via Terraform and Azure Verified Modules (AVM)—this pattern mitigates port scanning and brute-force attack vectors while standardizing hardened perimeter security across enterprise cloud environments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="QeVoCsTMBOQ" data-video-url="https://www.youtube.com/embed/QeVoCsTMBOQ" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/QeVoCsTMBOQ/hqdefault.jpg" alt="How Azure Bastion Secures Virtual Machines | Zero Public IP Access" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Azure Managed Identities and Terraform

??? note "🎬 How Azure VMs Access Storage Without Passwords | Managed Identity RBAC"
    !!! info "Architectural Summary"
        Shows how an Azure Virtual Machine provisioned with Azure Verified Modules authenticates via its System-Assigned Managed Identity (az login --identity) against the Azure Instance Metadata Service (IMDS) to access encrypted Blob Storage using RBAC without storing static keys or connection strings.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="jwASueLUzhI" data-video-url="https://www.youtube.com/embed/jwASueLUzhI" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/jwASueLUzhI/hqdefault.jpg" alt="How Azure VMs Access Storage Without Passwords | Managed Identity RBAC" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform and Azure Verified Modules AVM

??? note "🎬 How Azure Centralizes Cloud Monitoring | AVM Log Analytics Workspace"
    !!! info "Architectural Summary"
        This video demonstrates a 'telemetry-first' infrastructure deployment pattern using Azure Verified Modules (AVM) with Terraform to provision a centralized Log Analytics Workspace prior to compute or networking resources. By leveraging AVM's native shared diagnostic parameters, downstream components such as Virtual Machines, Key Vaults, and Storage Accounts automatically inherit telemetry bindings without repetitive custom diagnostic code. In a 2026 Cloud Native landscape, this standardized observability-as-code approach ensures zero-day visibility, instant cross-system correlation, and automated compliance auditing from the exact moment infrastructure goes live.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="oBkA9k32ECQ" data-video-url="https://www.youtube.com/embed/oBkA9k32ECQ" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/oBkA9k32ECQ/hqdefault.jpg" alt="How Azure Centralizes Cloud Monitoring | AVM Log Analytics Workspace" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform AzAPI and AzureRM

??? note "🎬 Why Azure Platform Teams Choose AzAPI Complexity | ALZ 2026 Architecture"
    !!! info "Architectural Summary"
        This architectural overview explains why enterprise Azure platform teams strategically adopt the Terraform AzAPI provider alongside AzureRM to directly interface with the Azure Resource Manager (ARM) REST control plane. In a 2026 Cloud Native context, this dual-provider strategy eliminates upstream provider lag for day-zero security and compliance guardrails while leveraging plan-time OpenAPI schema validation. Central platform teams absorb the raw JSON complexity within Azure Verified Modules (AVM), empowering application teams with clean, composable abstractions for rapid deployment.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="ptetbW0C0P8" data-video-url="https://www.youtube.com/embed/ptetbW0C0P8" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/ptetbW0C0P8/hqdefault.jpg" alt="Why Azure Platform Teams Choose AzAPI Complexity | ALZ 2026 Architecture" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 How AVM and AzAPI Beat AzureRM Updates | ALZ 2026 Architecture Takeaway"
    !!! info "Architectural Summary"
        Explains how Azure Verified Modules (AVM) leverage the AzAPI provider under the hood to declare Azure Resource Manager (ARM) API properties directly, eliminating multi-month waiting periods for third-party provider updates while maintaining Microsoft-backed module interfaces.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="Q2fhHPqJnKk" data-video-url="https://www.youtube.com/embed/Q2fhHPqJnKk" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/Q2fhHPqJnKk/hqdefault.jpg" alt="How AVM and AzAPI Beat AzureRM Updates | ALZ 2026 Architecture Takeaway" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 How AzAPI Enables Day Zero Deployments | ALZ 2026 Architecture Takeaway"
    !!! info "Architectural Summary"
        Illustrates how the Terraform AzAPI provider enables Day-Zero deployments on Microsoft Azure by communicating directly with the Azure Resource Manager (ARM) REST control plane, allowing enterprise platform teams to adopt newly released Azure Landing Zone capabilities immediately.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="O_Mfirh5xqM" data-video-url="https://www.youtube.com/embed/O_Mfirh5xqM" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/O_Mfirh5xqM/hqdefault.jpg" alt="How AzAPI Enables Day Zero Deployments | ALZ 2026 Architecture Takeaway" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

??? note "🎬 How AzAPI Unlocks Day Zero Azure Features | ALZ 2026 Architecture Takeaway"
    !!! info "Architectural Summary"
        Details how platform engineers using Azure Verified Modules (AVM) and the AzAPI provider can pass raw ARM JSON payloads directly inside Terraform manifests to unlock preview and newly GA networking or security flags without provider bottlenecks.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="YWNUZfYelIM" data-video-url="https://www.youtube.com/embed/YWNUZfYelIM" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/YWNUZfYelIM/hqdefault.jpg" alt="How AzAPI Unlocks Day Zero Azure Features | ALZ 2026 Architecture Takeaway" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Azure Storage Compliance and IaC

??? note "🎬 Nubenetes Azure Storage WORM and ERP Compliance (Spain Central) (Playlist) [SPANISH CONTENT]"
    !!! info "Architectural Summary"
        Reference architecture and Infrastructure as Code (Terraform, Bicep, and Ansible) for immutable WORM storage on Azure Blob Storage (StorageV2) in the Spain Central (Madrid) region. Covers regulatory compliance with Article 30 of the Spanish Commercial Code (6-year legal retention), Anti-Fraud Law 11/2021, and VeriFactu Regulation (RD 1007/2023), achieving over 75% FinOps cost optimization via automated lifecycle tiering (Hot, Cool, Cold, Archive) and AEAT audit rehydration strategies. [SPANISH CONTENT]

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLc2WtEw1pojo" title="Nubenetes Azure Storage WORM and ERP Compliance (Spain Central) (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## SRE and Observability

??? note "🎬 Nubenetes SLAs and SLOs Observability (Playlist)"
    !!! info "Architectural Summary"
        Comprehensive engineering guide to Service Level Agreements (SLAs), Service Level Objectives (SLOs), Service Level Indicators (SLIs), Error Budgets, and tail latency (P99) observability. Covers why averages lie in distributed microservices, Linux CFS CPU quota throttling, PromQL percentile math, canary deployment SLO gates, tail-based distributed tracing, and enterprise observability platforms.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLBUzSeBwfM7M" title="Nubenetes SLAs and SLOs Observability (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes Enterprise Observability and Monitoring Platforms (Playlist)"
    !!! info "Architectural Summary"
        Comparative architecture, high-load stress testing, TCO modeling, and air-gapped monitoring strategies across 12 enterprise observability platforms.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLcUy0RRCT9fg" title="Nubenetes Enterprise Observability and Monitoring Platforms (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Nubenetes Datadog on OpenShift (Playlist)"
    !!! info "Architectural Summary"
        Deploying, tuning, and scaling the Datadog Agent and Operator on Red Hat OpenShift with Security Context Constraints (SCCs), edge log filtering, and FinOps ingestion cost control.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLR6nHneHUvqU" title="Nubenetes Datadog on OpenShift (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Zero-Trust IAM and OIDC

??? note "🎬 Nubenetes OAuth2, OIDC and Entra ID Identity on Azure (Playlist)"
    !!! info "Architectural Summary"
        Architectural masterclasses, deep-dive podcasts, and technical walkthroughs on OAuth 2.0, OpenID Connect (OIDC), Microsoft Entra ID App Registrations, On-Behalf-Of (OBO) token exchange, Workload Identity Federation, and secretless zero-trust governance on Microsoft Azure with Terraform.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLcCUAwooFb6s" title="Nubenetes OAuth2, OIDC and Entra ID Identity on Azure (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Jenkins and GitOps

??? note "🎬 Nubenetes Jenkins Pure GitOps (Without Git Parameter) (Playlist)"
    !!! info "Architectural Summary"
        Declarative pull-based GitOps architectures, multi-cluster delivery with ArgoCD, and automated canary rollouts eliminating manual Jenkins UI Git Parameter dropdowns.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLMiMCcgzkPpw" title="Nubenetes Jenkins Pure GitOps (Without Git Parameter) (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Jenkins CI CD Automation

??? note "🎬 Nubenetes Jenkins Git Parameter Automation (Playlist)"
    !!! info "Architectural Summary"
        Enterprise immutable promotion, SCM tagging, release validation, and CI/CD pipelines using the Jenkins Git Parameter plugin and GitOps delivery patterns.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLaqfcvWjZHso" title="Nubenetes Jenkins Git Parameter Automation (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## SRE and Decision Architecture

??? note "🎬 Nubenetes JevOps and System 1 Decision Models (Playlist)"
    !!! info "Architectural Summary"
        Reflexive System 1 decision models for cloud-native infrastructure, submillisecond log filtering, and production deployment patterns on Kubernetes and OpenShift.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLWwVdOapXzDc" title="Nubenetes JevOps and System 1 Decision Models (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Keycloak and Enterprise IAM

??? note "🎬 Nubenetes Keycloak and RHBK Enterprise IAM on OpenShift (Playlist)"
    !!! info "Architectural Summary"
        Enterprise identity architecture, Red Hat Build of Keycloak (RHBK), OAuth 2.1, OIDC federation, and multi-region high-availability replication on OpenShift.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLUt4PJvFTysY" title="Nubenetes Keycloak and RHBK Enterprise IAM on OpenShift (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Enterprise Modernization and GitOps

??? note "🎬 Nubenetes TIBCO BWCE Modernization and GitOps (Playlist)"
    !!! info "Architectural Summary"
        Enterprise containerization, canary rollouts, Linux CFS CPU throttling tuning, and GitOps delivery pipelines for TIBCO BusinessWorks Container Edition (BWCE) on Kubernetes.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?list=PLRz_DgUi73hc" title="Nubenetes TIBCO BWCE Modernization and GitOps (Playlist)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Azure AI Foundry

??? note "🎬 Microsoft Foundry Enterprise Controls: Security, VNet & Deadlines"
    !!! info "Architectural Summary"
        This architectural overview details enterprise governance and perimeter defense for Microsoft Azure AI Foundry workloads, emphasizing zero-trust network isolation via Azure Private Endpoints, disabled public ingress, and managed VNet outbound routing. It highlights robust data protection through Customer-Managed Keys (CMK) and Azure Managed Identities alongside operational lifecycle strategies to manage LLM deprecation via automated canary deployments. For 2026 enterprise cloud-native environments, these patterns provide a hardened blueprint for securely deploying generative AI and agentic systems while strictly complying with corporate security boundaries.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="i72ZvGizCEE" data-video-url="https://www.youtube.com/embed/i72ZvGizCEE" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/i72ZvGizCEE/hqdefault.jpg" alt="Microsoft Foundry Enterprise Controls: Security, VNet & Deadlines" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Red Hat OpenShift

??? note "🎬 How OpenShift 5 Secures Sovereign Clouds: Air-Gapped & Zero-Trust Governance"
    !!! info "Architectural Summary"
        This architectural brief outlines how Red Hat OpenShift 5 provides robust sovereign cloud governance through automated air-gapped installation profiles, image mirroring, and zero-trust security boundaries. In a 2026 cloud-native landscape shaped by strict geopolitical data residency and regulatory mandates, it demonstrates how organizations can enforce crypto-compliant operating system controls and strict operational isolation without sacrificing modern container orchestration workflows.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="u07rBU5fYTE" data-video-url="https://www.youtube.com/embed/u07rBU5fYTE" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/u07rBU5fYTE/hqdefault.jpg" alt="How OpenShift 5 Secures Sovereign Clouds: Air-Gapped & Zero-Trust Governance" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Confidential Containers CoCo OpenShift

??? note "🎬 How Confidential Containers Protect AI Models in Red Hat OpenShift 5 [Short]"
    !!! info "Architectural Summary"
        This architecture short examines how Confidential Containers (CoCo) in Red Hat OpenShift leverage hardware-enforced Trusted Execution Environments (TEEs) to protect proprietary LLM weights, training data, and inference prompts from memory dumps and hypervisor-level compromises. In a modern cloud-native paradigm, this enables zero-trust multi-tenant AI deployments on untrusted public cloud and shared bare-metal infrastructure, ensuring full data confidentiality even against privileged cluster administrators.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="MX505_pRGD0" data-video-url="https://www.youtube.com/embed/MX505_pRGD0" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/MX505_pRGD0/hqdefault.jpg" alt="How Confidential Containers Protect AI Models in Red Hat OpenShift 5 [Short]" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Kubernetes SPIFFE SPIRE TPM

??? note "🎬 How NVKE Secures Bare-Metal GPU Clusters: TPM, SPIFFE/SPIRE & etcd Encryption [Short]"
    !!! info "Architectural Summary"
        NVIDIA Kubernetes Engine (NVKE) establishes a hardware-rooted zero-trust architecture for bare-metal GPU clusters by combining TPM-based node attestation via SPIFFE/SPIRE with encrypted mTLS transport before granting cluster join credentials. It enforces multi-tenant cluster isolation using dedicated control planes, per-cluster etcd encryption at rest, fleet OIDC integration, and verifiable NVKR SBOMs. This design serves as a essential blueprint for securing high-performance AI/ML infrastructure and bare-metal GPU fleets in modern cloud-native environments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="SO6i_-fUero" data-video-url="https://www.youtube.com/embed/SO6i_-fUero" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/SO6i_-fUero/hqdefault.jpg" alt="How NVKE Secures Bare-Metal GPU Clusters: TPM, SPIFFE/SPIRE & etcd Encryption [Short]" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## NetBox

??? note "🎬 NetBox Zero To Hero"
    !!! info "Architectural Summary"
        NetBox serves as the foundational source of truth for modern network automation by integrating IP Address Management (IPAM) and Data Center Infrastructure Management (DCIM) into a unified database. In a 2026 Cloud Native ecosystem, it empowers Infrastructure as Code (IaC) pipelines to dynamically query and enforce intended network state via robust APIs, effectively eliminating configuration drift. This architectural approach bridges the gap between physical hardware tracking and automated, declarative network orchestration across complex hybrid environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=fJvBV63-mjQ6S-Ht&amp;list=PL7sEPiUbBLo_iTds-NV-9Tu05Gg2Aj8N7" title="NetBox Zero To Hero" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>
