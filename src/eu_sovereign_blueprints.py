"""Pre-sales & solution-architecture blueprints for the European Sovereign Cloud & Private DCs pillar."""

EU_SOVEREIGN_BLUEPRINTS: dict[str, str] = {
    "eu-sovereign-cloud.md": """## Executive Architecture: European Sovereign Cloud vs US Hyperscalers (2026)

1. [European Country and Regional Pre-Sales Hubs](#european-country-and-regional-pre-sales-hubs)
2. [The 4 Levels of Cloud Sovereignty](#the-4-levels-of-cloud-sovereignty)
3. [EU Regulatory and Compliance Justification Matrix](#eu-regulatory-and-compliance-justification-matrix)
4. [Pre-Sales Architecture Decision Flow](#pre-sales-architecture-decision-flow)
5. [EUR Cost and TCO Benchmarks vs Hyperscalers](#eur-cost-and-tco-benchmarks-vs-hyperscalers)
6. [When Does Each Cloud Tier Win (Pre-Sales Playbook)](#when-does-each-cloud-tier-win-pre-sales-playbook)

### European Country and Regional Pre-Sales Hubs

Nubenetes V2 provides dedicated field guides for every major European cloud jurisdiction, interconnection hub, and technical cross-cutting architecture:

<div class="eu-hub-grid" aria-label="European Country and Regional Sovereign Cloud Guides">
  <a class="eu-hub-link" href="/eu-cloud-spain/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇪🇸</span>
        <span class="eu-hub-title">Spain</span>
        <span class="eu-hub-badge">ENS Alto</span>
      </header>
      <p>Arsys · Gigas · Alhambra IT · Telefonica Tech · Stackscale · ESpanix</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-germany/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇩🇪</span>
        <span class="eu-hub-title">Germany</span>
        <span class="eu-hub-badge">BSI C5 · KRITIS</span>
      </header>
      <p>STACKIT · IONOS · Hetzner · Open Telekom · PlusServer · DE-CIX</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-france/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇫🇷</span>
        <span class="eu-hub-title">France</span>
        <span class="eu-hub-badge">SecNumCloud 3.2</span>
      </header>
      <p>OVHcloud · Scaleway · 3DS OUTSCALE · Cloud Temple · Clever Cloud · Marseille</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-italy/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇮🇹</span>
        <span class="eu-hub-title">Italy</span>
        <span class="eu-hub-badge">ACN QC3 / AI3</span>
      </header>
      <p>Aruba Cloud · Seeweb · WIIT · ReeVo · PSN · MIX Milan</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-benelux/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇳🇱</span>
        <span class="eu-hub-title">Netherlands &amp; Benelux</span>
        <span class="eu-hub-badge">AMS-IX · DORA</span>
      </header>
      <p>Nebius AI · Leaseweb · Cyso · Leafcloud · LuxConnect · Proximus NXT</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-switzerland-dach/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇨🇭</span>
        <span class="eu-hub-title">Switzerland &amp; Austria</span>
        <span class="eu-hub-badge">FINMA · FADP</span>
      </header>
      <p>Exoscale · cloudscale.ch · VSHN APPUiO · Infomaniak · Anexia</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-nordics/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇸🇪</span>
        <span class="eu-hub-title">Nordics</span>
        <span class="eu-hub-badge">3-AZ · Green AI</span>
      </header>
      <p>Elastx · Cleura · UpCloud · Safespring · atNorth · Green Mountain</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-uk/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🇬🇧</span>
        <span class="eu-hub-title">United Kingdom</span>
        <span class="eu-hub-badge">NCSC · G-Cloud</span>
      </header>
      <p>Civo Sovereign · Pulsant · Brightbox · Redcentric · Nscale · LINX</p>
      <footer><span class="eu-hub-cta">Explore guide →</span></footer>
    </article>
  </a>
</div>

<div class="eu-hub-grid eu-hub-grid--pillars" aria-label="Cross-Cutting European Cloud Engineering Guides">
  <a class="eu-hub-link" href="/eu-cloud-iac-maturity/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🏗️</span>
        <span class="eu-hub-title">IaC Automation &amp; Maturity</span>
        <span class="eu-hub-badge">OpenTofu · CAPI</span>
      </header>
      <p>Coverage scorecard vs hyperscalers (100% baseline) and OpenStack/vCD/Proxmox portability</p>
      <footer><span class="eu-hub-cta">Open scorecard →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-workloads-stack/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">⚙️</span>
        <span class="eu-hub-title">Hypervisors, K8s &amp; Sovereign AI</span>
        <span class="eu-hub-badge">Post-Broadcom</span>
      </header>
      <p>Proxmox VE · OpenStack · OpenShift 5 · European NVIDIA H200/B200 AI factories</p>
      <footer><span class="eu-hub-cta">Open stack guide →</span></footer>
    </article>
  </a>
  <a class="eu-hub-link" href="/eu-cloud-resilience-sla/">
    <article class="eu-hub-card">
      <header>
        <span class="eu-hub-flag" aria-hidden="true">🛡️</span>
        <span class="eu-hub-title">RPO, RTO, SLAs &amp; DRP</span>
        <span class="eu-hub-badge">DORA Exit</span>
      </header>
      <p>3-AZ reality check, Veeam/Zerto/PBS/CNPG/Velero and 3-2-1-1-0 ransomware vaults</p>
      <footer><span class="eu-hub-cta">Open resilience guide →</span></footer>
    </article>
  </a>
</div>

| Country / Architecture Hub | Regulatory Regime & Anchor IXP | Top Sovereign Providers & Private DC Ecosystem | Pre-Sales Deep-Dive |
| :--- | :--- | :--- | :--- |
| **Germany** | **BSI C5 Type 2**, KRITIS, TISAX · **DE-CIX Frankfurt** | **STACKIT, IONOS, Hetzner, Open Telekom Cloud, PlusServer, SysEleven/secunet, noris, gridscale, Cloud&Heat, Delos**, maincubes / JUPITER | [Germany Sovereign Cloud](/eu-cloud-germany/) |
| **France** | **ANSSI SecNumCloud 3.2**, HDS · **France-IX & Marseille Subsea** | **OVHcloud, Scaleway, 3DS OUTSCALE, Cloud Temple, Clever Cloud, Ikoula, Bleu, S3NS**, Mistral AI, DATA4 Paris-Saclay, Jean Zay | [France Sovereign Cloud](/eu-cloud-france/) |
| **Spain** | **ENS Alto (RD 311/2022)** · **ESpanix / DE-CIX Madrid** | **Arsys, Gigas, Alhambra IT, Telefonica Tech, Stackscale, Acens, cdmon**, Merlin-Edged, Digital Realty/Equinix/Nabiax, MareNostrum 5 | [Spain Sovereign Cloud](/eu-cloud-spain/) |
| **Italy** | **ACN QC3 / AI3**, PSN · **MIX Milan** | **Aruba Cloud, Seeweb, WIIT, ReeVo, TIM Enterprise/Noovle, PSN**, Equinix Milan, CINECA Leonardo | [Italy Sovereign Cloud](/eu-cloud-italy/) |
| **Netherlands & Benelux** | Dutch **BIO / NEN 7510**, EU DORA · **AMS-IX** | **Nebius AI, Leaseweb, Cyso Cloud, Leafcloud, TransIP, Proximus NXT, LuxConnect, Gcore**, NorthC, Equinix/Digital Realty AMS | [Netherlands & Benelux](/eu-cloud-benelux/) |
| **Switzerland & Austria (Alpine)** | **FINMA**, Swiss FADP (**revDSG**), Zero CLOUD Act · **SwissIX / VIX** | **Exoscale, Infomaniak, cloudscale.ch, Swisscom, VSHN/APPUiO, Anexia**, Green Datacenter, CSCS Alps | [Switzerland & Austria](/eu-cloud-switzerland-dach/) |
| **Nordics (SE / FI / NO / IS)** | **eSam / Schrems II**, 100% Hydro/Geothermal · **Netnod** | **UpCloud, Elastx 3-AZ, Cleura SCS, GleSYS, Safespring, evroc, Green Mountain, atNorth, Verne, Bulk**, LUMI | [Nordics Green Cloud](/eu-cloud-nordics/) |
| **United Kingdom** | **NCSC 14 Principles**, G-Cloud, UK GDPR, FCA · **LINX London** | **Civo UK Sovereign, Pulsant, Brightbox, Redcentric, Nscale**, Telehouse Docklands, Equinix Slough/LD | [United Kingdom Sovereign Cloud](/eu-cloud-uk/) |
| **Cross-Cutting Engineering** | Multi-Provider IaC, Post-Broadcom Virtualization, DORA RPO/RTO | OpenTofu (`openstack`/`vcd`/`bpg/proxmox`), CAPI, Crossplane, Proxmox/OpenStack/OpenShift 5, Veeam/Zerto/PBS/CNPG/Velero | [IaC Maturity](/eu-cloud-iac-maturity/) · [Stacks & AI](/eu-cloud-workloads-stack/) · [RPO/RTO & DRP](/eu-cloud-resilience-sla/) |

### The 4 Levels of Cloud Sovereignty

!!! warning "Pre-Sales Distinction: European Region != European Sovereignty"
    Deploying in **AWS (`Frankfurt` / `Paris` / `Madrid`)**, **Azure (`West Europe` / `France Central` / `Spain Central`)**, or **GCP (`Frankfurt` / `Milan` / `Madrid`)** satisfies **Level 1 (Data Residency)**, but US-headquartered hyperscalers remain legally subject to **US extraterritorial statutes (US CLOUD Act / FISA 702)**. Pre-sales architects MUST classify every workload into one of four maturity levels before recommending a provider:

| Level | Sovereignty Tier | Technical and Legal Guarantees | Example Providers and Architectures |
| :---: | :--- | :--- | :--- |
| **L1** | **Data Residency Only** | Data physically stored inside European borders; US parent retains control plane and legal compulsion exposure. | Standard AWS (`eu-central-1`, `eu-west-3`, `eu-south-2`), Azure (`West Europe`, `Spain Central`), GCP (`europe-west3`, `europe-west8`) |
| **L2** | **Operational Sovereignty** | Data + control-plane staff isolated inside the EU; local audit logs; customer-approvable support access (BYOK). | **AWS European Sovereign Cloud (Brandenburg)**, Google Sovereign Controls, Telefonica + Google Data Boundary |
| **L3** | **Cryptographic Sovereignty (HYOK)** | Hardware HSM keys held outside cloud provider perimeter (**Hold Your Own Key** / Confidential Computing); provider cannot decrypt payloads. | **S3NS** (Thales + GCP), **Bleu** (Capgemini/Orange Azure), **Arsys / IONOS KMS + HSM**, private HSM + Kubernetes |
| **L4** | **Full Legal and Jurisdictional Sovereignty** | **100% European-headquartered & owned legal entity**, European operations, European physical DCs; zero non-EU parent exposure + national security clearance. | **DE:** STACKIT, IONOS, Hetzner, Open Telekom · **FR:** Outscale (SecNumCloud 3.2), OVHcloud, Scaleway, Cloud Temple · **ES:** Arsys, Gigas, Alhambra IT, Stackscale · **IT:** Aruba (ACN QC3), Seeweb, WIIT · **NL/LU:** Nebius, Cyso, Leaseweb, LuxConnect · **CH/AT:** Exoscale, cloudscale.ch, VSHN · **Nordics:** Elastx, Cleura, UpCloud · **UK:** Civo, Pulsant |

### EU Regulatory and Compliance Justification Matrix

| Regulation / Standard | Deadline and Scope | Mandatory Technical Requirements | Impact on Cloud Selection (Pre-Sales Justification) |
| :--- | :--- | :--- | :--- |
| **GDPR + Schrems II** | Active (All EU personal data) | Lawful transfer mechanism; Supplementary Measures; sub-processor transparency. | Eliminates cross-border legal friction when using L4 EU-owned providers across DE, FR, ES, IT, NL, and Nordics. |
| **DORA (EU 2022/2554)** | Enforced since **Jan 17, 2025** (Banking, Insurance, Critical ICT) | Full ICT Third-Party register; **Articles 28–30 mandatory tested Exit Plans**; **Concentration Risk** avoidance; pen-testing (TLPT). | Justifies **multi-provider architecture** (e.g., primary on Hyperscaler or National Tier IV DC + tested warm DR/exit on EU Sovereign Cloud using OpenTofu/Velero). |
| **NIS2 Directive** | Enforced (Energy, Health, Telco, Digital Infra, MSPs) | Supply-chain risk governance, 24h incident reporting, verified backup segmentation, zero unpatched exposure. | Mandates immutable offsite backups and verified regional MSP certifications (**ENS Medio/Alto**, **ISO 27001**, **BSI C5**). |
| **EU Data Act (EU 2023/2854)** | Switching cap now; **Zero switching fees on Jan 12, 2027** (Art. 29) | Open APIs for functional portability; free migration egress on cloud exit. **Note:** ongoing daily internet egress stays billable! | Use **zero-egress EU clouds** (OVHcloud, Scaleway free tiers, Hetzner 20 TB, Stackscale, Alhambra IT) when daily outbound traffic drives hyperscaler bill shock. |
| **EU AI Act** | Phased 2025–2027 (High-risk AI, foundation models) | Data lineage, model card documentation, sovereign training/inference auditability, privacy-preserving RAG. | Favors **Nebius, Scaleway, OVHcloud, Seeweb, Civo UK, Telefonica/MareNostrum 5**, or private on-prem GPU clusters for sensitive corporate weights/RAG. |
| **ENS Alto (Spain)** | Mandatory for Spanish Public Sector and supply chain | 75+ strict CCN-CERT controls (Confidentiality, Integrity, Traceability, Authenticity, Availability) audited locally. | **Arsys, Gigas, Alhambra IT, Telefonica Tech** win Spanish public tenders immediately over generic global hosting. |
| **SecNumCloud 3.2 (France)** | ANSSI highest EU sovereign standard | Strict non-EU ownership shareholding cap (<24% aggregated non-EU) + French operational isolation. | **3DS Outscale** (full scope), **OVHcloud Bare Metal / Hosted Private Cloud**, **Cloud Temple**; Bleu and S3NS targeting 3.2 Parity. |
| **BSI C5 Type 2 (Germany)** | German Federal Cloud baseline | Continuous annual audited security controls across compute, storage, IAM, and physical facilities. | **IONOS Cloud, STACKIT, Open Telekom Cloud, PlusServer, noris network** (plus AWS ESC). |
| **ACN QC3 / AI3 (Italy)** | Mandatory for Italian Public Administration & critical AI | Italian National Cybersecurity Agency cloud & AI workload qualification levels. | **Aruba Cloud** (QC3 + AI3), **Polo Strategico Nazionale (PSN)**, **Seeweb**, **WIIT**. |
| **FINMA / revDSG (Switzerland)** | Swiss banking outsourcing & revised Federal Data Protection Act | Swiss audit rights, strict third-country transfer prohibitions, operational continuity & exit verification. | **Exoscale, cloudscale.ch, Infomaniak, Swisscom, VSHN/APPUiO** (zero US CLOUD Act exposure). |
| **UK NCSC / FCA-PRA** | UK public sector (G-Cloud) & financial operational resilience | 14 NCSC Cloud Security Principles, UK GDPR residency, tested impact-tolerance exits. | **Civo UK Sovereign, Pulsant, Brightbox, Redcentric, Nscale**. |

### Pre-Sales Architecture Decision Flow

```mermaid
%%{init: {'themeVariables': {'fontSize': '13px'}, 'flowchart': {'htmlLabels': false, 'nodeSpacing': 20, 'rankSpacing': 68, 'padding': 12}}}%%
flowchart LR
    A(["Workload<br/>Assessment"]) --> B{{"L4 Legal<br/>Sovereignty?"}}

    B -->|"Yes"| C{{"European<br/>Region?"}}
    C -->|"Core / Alpine"| C1{{"DE · FR ·<br/>NL · CH"}}
    C -->|"Med / North / UK"| C2{{"ES · IT ·<br/>SE/FI · UK"}}

    C1 -->|"DE · BSI C5"| D1["Germany Sovereign<br/>STACKIT · IONOS · Hetzner<br/>Open Telekom · PlusServer"]
    C1 -->|"FR · SecNum"| D2["France Sovereign<br/>3DS OUTSCALE · OVHcloud<br/>Scaleway · Cloud Temple"]
    C1 -->|"NL/LU · DORA"| D3["Netherlands & Benelux<br/>Nebius · Leaseweb · Cyso<br/>Leafcloud · LuxConnect"]
    C1 -->|"CH/AT · FINMA"| D4["Switzerland & Austria<br/>Exoscale · cloudscale.ch<br/>VSHN · Infomaniak · Anexia"]

    C2 -->|"ES · ENS Alto"| D5["Spain Sovereign<br/>Arsys · Gigas · Alhambra<br/>Telefonica · Stackscale"]
    C2 -->|"IT · ACN QC3"| D6["Italy Sovereign<br/>Aruba Cloud · Seeweb<br/>WIIT · ReeVo · PSN"]
    C2 -->|"Nordics · eSam"| D7["Nordics 3-AZ & Green<br/>Elastx · Cleura · UpCloud<br/>Safespring · atNorth"]
    C2 -->|"UK · NCSC"| D8["United Kingdom<br/>Civo · Pulsant · Brightbox<br/>Redcentric · Nscale"]

    B -->|"No"| F{{"Proprietary<br/>Cloud PaaS?"}}
    F -->|"Yes"| G["Hyperscaler L1 / L2<br/>+ EU Sovereign DR Vault<br/>(DORA / FCA Exit Plan)"]
    F -->|"No"| H{{"Primary<br/>Driver?"}}

    H -->|"High Egress"| I["EU Cloud / Bare Metal<br/>Hetzner · OVH · Scaleway<br/>Leaseweb · UpCloud"]
    H -->|"NVIDIA GPU"| J["EU AI Factories<br/>Nebius · Scaleway · OVH<br/>Seeweb · atNorth · Nscale"]
    H -->|"VMware Exit"| K["Hypervisor Migration<br/>Proxmox VE · OpenStack<br/>CloudStack · OpenShift 5"]
```

### EUR Cost and TCO Benchmarks vs Hyperscalers

*Indicative 2026 monthly production run-rate comparisons (EUR/month, list on-demand/committed baselines without opaque enterprise NDA discounts):*

| Workload Scenario | Reference Spec (24x7 Monthly) | US Hyperscaler Baseline (AWS / Azure / GCP EU) | EU Tier-1 Alternative (OVHcloud / Scaleway / Hetzner / STACKIT) | National Sovereign MSP (Arsys · STACKIT · Cloud Temple · Aruba · WIIT · Exoscale) | Pre-Sales Savings & Commercial Root Cause |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Production Kubernetes Cluster (Medium SaaS)** | 6x 8 vCPU / 32 GB nodes + 2 TB NVMe block + 2 LBs + **25 TB outbound egress** | **EUR 3,450 – 4,200 / mo** *(~EUR 2,100 egress alone at ~EUR 0.085/GB!)* | **EUR 420 – 1,050 / mo** *(Hetzner Cloud EUR 420; OVH MKS ~EUR 850 zero egress)* | **EUR 1,150 – 2,150 / mo** *(Includes local L3 managed SLA & ENS/BSI/ACN/FINMA compliance)* | **55–88% cheaper** — EU providers eliminate hyperscaler egress taxes and control-plane fees. |
| **2. Legacy VMware Consolidation (Post-Broadcom)** | 128 physical cores, 2 TB RAM, 80 TB NVMe SAN (100+ VMs) | **EUR 9,500 – 14,000 / mo** *(VMware on Hyperscaler or IaaS refactor)* | **EUR 3,200 – 5,500 / mo** *(Bare Metal Proxmox VE + Ceph or OpenStack KVM)* | **EUR 4,500 – 7,800 / mo** *(Managed VCSP / Sovereign Private Cloud EUR/CHF OPEX)* | **45–68% cheaper** — avoids Broadcom VCF core-bundle shock via Proxmox/OpenStack or MSP pooled VCSP licensing. |
| **3. Private Enterprise RAG and vLLM Inference Node** | 1x dedicated 8x NVIDIA H100 (80 GB) node + 10 TB NVMe + 50 TB egress | **EUR 24,000 – 32,000 / mo** *(p5/NDv5 on-demand + data transfer)* | **EUR 11,500 – 16,500 / mo** *(Nebius / Scaleway / OVHcloud H100)* | **EUR 13,000 – 18,500 / mo** *(Sovereign GPU lease via Seeweb / Scaleway / Merlin-Edged / Nscale)* | **45–55% cheaper** with sovereign model-weight residency and zero cross-region prompt leakage. |
| **4. 100 TB Sovereign Backup & WORM Vault** | 100 TB S3 Object Storage with Object Lock (immutability) + 3x full DR restores/yr | **EUR 2,400 – 3,100 / mo** + **EUR 2,500+ per restore test** | **EUR 600 – 900 / mo** *(OVH / Scaleway / Hetzner / Exoscale SOS S3)* | **EUR 950 – 1,500 / mo** *(Certified national S3 Object Lock via Arsys / IONOS / Aruba / WIIT)* | **60–75% cheaper** and makes **DORA quarterly restore tests** financially viable. |

### When Does Each Cloud Tier Win (Pre-Sales Playbook)

| Customer Scenario | Winning Choice | Why It Wins | Pre-Sales Red Flag to Surface Early |
| :--- | :--- | :--- | :--- |
| **Regulated National Public Sector, Health, or Defense** | **DE:** STACKIT / Open Telekom / Delos · **FR:** 3DS OUTSCALE / Cloud Temple · **ES:** Arsys / Gigas / Alhambra / Telefonica · **IT:** PSN / Aruba · **CH:** cloudscale.ch / Swisscom · **UK:** Redcentric / Civo | Turnkey national security clearance (**BSI C5, SecNumCloud 3.2, ENS Alto, ACN QC3, FINMA, G-Cloud**), local contract/billing, zero foreign control chain. | Never pitch uncertified commodity VPS hosts for public tenders unless wrapped inside an accredited national sovereign MSP layer. |
| **Bank / FinTech / Insurer Under DORA or FCA-PRA** | **Dual-Cloud Multi-Country (Hyperscaler + L4 EU Secondary, or DE+ES / FR+NL / CH+AT Sovereign Pairs)** | Satisfies DORA Art. 28–30 **tested exit plan** & eliminates single-vendor concentration risk across independent power grids. | Beware claiming "2 AZs inside 1 hyperscaler region" satisfies DORA exit — regulators require cross-provider portability. |
| **High-Bandwidth SaaS, Streaming, CDN Origin, or AI Dataset Hub** | **OVHcloud, Scaleway, Hetzner, Leaseweb, Stackscale, or UpCloud** | Zero or massively included egress eliminates 50–80% of monthly cloud bills across Europe. | Verify inter-region vs internet egress fine print (some providers meter inter-DC private trunking differently). |
| **Pure GitOps / Kubernetes Platform Team (Terraform + Argo + Talos)** | **Scaleway, OVHcloud, STACKIT, IONOS, Exoscale, Cleura, Elastx, Civo, or Hetzner** | Mature OpenTofu/CAPI/Crossplane providers (75–85% parity) + Managed K8s or bare metal with Talos Linux. | Confirm OIDC workload identity and BGP LoadBalancer automation before committing to zero-touch pipelines. |
| **Enterprise With Heavy Serverless / Event-Driven / BigQuery Dependency** | **Keep AWS / Azure / GCP** (+ S3 sovereign EU backup vault) | Managed PaaS depth (Lambda, DynamoDB, BigQuery, Foundry/Bedrock) saves 3–6 FTE platform engineers. | Never underestimate the refactoring cost of proprietary managed DBs/queues during a rushed "lift-and-exit" pitch. |
""",
    "eu-cloud-spain.md": """## Pre-Sales Field Guide: Spain Sovereign Cloud and Private Data Centers

1. [Why Spain Is Southern Europe's Strategic Cloud Hub](#why-spain-is-southern-europes-strategic-cloud-hub)
2. [Comprehensive Spanish Cloud and Data Center Pre-Sales Matrix](#comprehensive-spanish-cloud-and-data-center-pre-sales-matrix)
3. [Spanish Hyperscaler Regions vs Local ENS Alto Providers](#spanish-hyperscaler-regions-vs-local-ens-alto-providers)
4. [Spanish Enterprise Pre-Sales Playbooks](#spanish-enterprise-pre-sales-playbooks)

### Why Spain Is Southern Europe's Strategic Cloud Hub

Spain has become one of Europe's top-tier digital sovereignty and interconnection gateways due to:

- **Submarine Cable Landing Advantage:** High-capacity fiber routes linking **Madrid, Barcelona, Bilbao (Marea/Grace Hopper/EllaLink), and Lisbon** connect Latin America, North/West Africa, and Northern Europe with ultra-low latency.
- **Dense Neutral Interconnection (ESpanix and DE-CIX Madrid):** Peering across **Digital Realty MAD1–4**, **Equinix MD1/MD2/MD6**, **Nabiax (Alcala)**, and **DATA4 (Alcobendas)** enables **sub-2 ms** optical connectivity between private enterprise cages and Spanish sovereign clouds.
- **Zero-Water Liquid Cooling & Iberian Solar PPAs:** **Merlin-Edged** campuses across Madrid-Getafe, Barcelona, and Bilbao-Arasur and **Barcelona Supercomputing Center (MareNostrum 5)** make Spain uniquely cost-competitive on industrial power and sovereign NVIDIA AI rack hosting.
- **Regulatory Pull (ENS Alto):** Under Royal Decree 311/2022 (**Esquema Nacional de Seguridad — ENS Alto**), any public sector organization or private vendor integrating with Spanish administrations requires verifiable ENS compliance and strict EU/Spanish operational traceability.

### Comprehensive Spanish Cloud and Data Center Pre-Sales Matrix

| Provider / Operator | HQ and DC Locations in Spain | Compliance and Certs | Core Platforms and Hypervisors | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Arsys (IONOS Group)** | Logrono (Spain) + Madrid; IONOS EU DCs | **Full-Portfolio ENS Alto**, ISO 27001, ISO 27017/27018, GDPR | VMware Cloud Director, Enterprise Cloud (KVM/IONOS stack), **Managed Kubernetes**, Bare Metal | **~65–80%** via IONOS CloudAPI/Terraform + `vmware/vcd` provider | 99.95–99.99% SLA; Dual-DC Logrono–Madrid replication & Veeam/Acronis DR | Regulated Spanish SMB/mid-market, public-sector tenders needing full ENS Alto + predictable EUR invoices |
| **Gigas** | Madrid + Lisbon/Europe multi-DC footprint | **ENS Alto**, ISO 27001, ISO 27017, ISO 20000, PCI-DSS | Sovereign VMware Cloud Director + OpenStack options, converged telco, Cloud Datacenter | **~55–65%** via `vmware/vcd` + OpenStack/API + Ansible | 99.95% SLA; Geo-redundant Metro DRaaS (Zerto/Veeam CDP), Telco MPLS | Mid-market enterprises wanting combined **Telco + Cybersecurity + Sovereign Cloud + 24x7 Spanish L3 support** |
| **Alhambra IT** | Madrid (Multi-DC Tier III+/IV facilities) | **ENS Alto**, ISO 27001, ISO 27018, ISO 22301, GDPR | Dedicated Private Cloud (VMware / KVM-Proxmox options), Managed Kubernetes/OpenShift | **~50–65%** via `vmware/vcd` / Ansible / custom OpenTofu pipelines | Bespoke contractual SLAs up to 99.99%; Active-Active Madrid stretch clusters; zero egress surprises | Banking, insurance, healthcare needing **customized contracts, DORA audit cooperation, and direct architect access** |
| **Telefonica Tech** | Madrid, Alcala, global telco POPs | **ENS Alto**, ISO 27001, DORA-aligned, Sovereign KMS custody | **Telefonica Tech VDC**, OpenShift/K8s, Telco Edge, plus **Google Cloud Sovereign Alliance (E2E Data Boundary)** | **~60–90%** (`vcd`/Terraform on VDC; 95%+ on Sovereign Google Cloud) | Enterprise Telco SLAs (up to 99.995%); Multi-DC DR + RedIRIS/MPLS fiber | IBEX-35, ministries, healthcare systems bridging legacy mainframe/VMware + managed hyperscaler capabilities under Telefonica billing |
| **Stackscale (Grupo Aire)** | Madrid (2 DCs) + Amsterdam (Active-Active cross-country) | ISO 27001, ISO 27017/27018, GDPR, ENS-aligned infrastructure | **OpenStack + KVM Bare Metal**, NetApp AFF NVMe shared storage, customer K8s/OpenShift | **~75%** via **standard `openstack` Terraform provider** + Ansible + OpenStack API | High-availability SLA; Dual-Madrid or Madrid–Amsterdam active replication; **zero traffic/egress billing traps** | SaaS vendors, AdTech, AI/data platforms escaping hyperscaler egress tolls with open OpenStack/K8s standards |
| **Acens (Telefonica Group)** | Madrid data centers | ISO 27001, GDPR, Telefonica group security | Enterprise VMware VDC, Managed Databases, Dedicated Bare Metal | **~50%** (portal/API + `vcd` for Cloud Datacenter tiers) | 99.95% SLA; Madrid Metro backup/replication | Spanish SMBs needing Turnkey Managed Cloud inside Telefonica's ecosystem |
| **cdmon / Dinahosting / Raiola** | Barcelona (cdmon), Santiago de Compostela (Dinahosting), Lugo/Madrid (Raiola) | ISO 27001 / GDPR / 100% Spanish legal jurisdiction | KVM VPS, Managed Hosting, Dedicated Bare Metal | **~25–40%** (Ansible + SSH/Cloud-init; basic REST APIs) | High uptime SMB SLAs; local snapshots & offsite EU backup | Digital agencies, regional e-commerce, and SMB SaaS wanting 100% Spanish ownership & native support |
| **Digital Realty / Equinix / Nabiax / DATA4 / Merlin-Edged** | Madrid (MAD1–4, MD1–6, Alcala, Alcobendas, Getafe), Barcelona, Bilbao | Tier III+ / Tier IV, Uptime Institute, ISO 27001/50001, liquid-cooled AI (Merlin-Edged) | **Customer-Owned Private Stack:** Bare Metal + **Proxmox VE / OpenShift 5 / OpenStack SCS** + Private NVIDIA GB200 racks | **~70–90%** depending on customer stack (`bpg/proxmox`, MAAS, CAPI, OpenStack) | Up to **99.999% power/cooling SLA**; dark fiber between 2 Madrid campuses; Equinix Fabric on-ramps | **Cloud Repatriation**, banks/telcos with >300 VMs or dedicated NVIDIA AI clusters requiring physical rack isolation |

### Spanish Hyperscaler Regions vs Local ENS Alto Providers

*When comparing US hyperscalers hosted physically inside Spain (`AWS eu-south-2 Aragon`, `Azure Spain Central Madrid`, `GCP europe-southwest1 Madrid`) against native Spanish providers:*

| Evaluation Criterion | Hyperscalers in Spain (AWS Aragon / Azure Madrid / GCP Madrid) | Native Spanish Sovereign Clouds (Arsys / Gigas / Alhambra / Telefonica VDC / Stackscale) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Jurisdiction and CLOUD Act** | US corporate parent remains exposed to extraterritorial disclosure orders | **100% Spanish / EU legal ownership and governance** | Mandatory differentiator in defense, justice, health, and public tenders. |
| **PaaS and AI Breadth** | **100%** (Bedrock, Foundry, Vertex, DynamoDB, serverless queues) | **30–55%** (Focus on IaaS, VMs, Bare Metal, Managed K8s, S3, Postgres) | Keep serverless/AI control planes on Hyperscaler if app architecture depends on it; place heavy steady compute in Spain. |
| **Outbound Traffic (Egress)** | **~EUR 0.08–0.09 / GB** (massive cost driver for media/SaaS/APIs) | **Included TB bundles or Flat-Rate / Zero Egress** (Stackscale/Alhambra) | Any workload pushing **>10–15 TB/month** typically pays for itself in Spain sovereign cloud within 60 days. |
| **Account Management and Support** | Ticket-based + costly Enterprise Support (**~10% of monthly spend**) | Named Technical Account Manager (TAM), Spanish phone/Slack L3 included | Mid-market Spanish IT teams gain direct senior architect escalation without 5-figure support retainers. |
| **Broadcom VMware Licensing Impact** | Heavy hyperscaler VMware solution premiums (AVS / GCVE) | Flexible VCSP pooled pricing OR turnkey migration to OpenStack/Proxmox/KubeVirt | Huge commercial lever in 2026–2027 renewal cycles. |

### Spanish Enterprise Pre-Sales Playbooks

!!! success "5 Repeatable Deals in the Spanish Market"
    1. **Public Sector / Municipal / University Tender (`ENS Alto` mandatory):** Lead with **Arsys**, **Gigas**, **Alhambra IT**, or **Telefonica Tech**. Highlight certified ENS Alto scope, Spanish invoicing, zero foreign jurisdiction risk, and Veeam/Acronis immutable backups.
    2. **DORA-Regulated Spanish Bank / Fintech Exit Plan:** Keep core Azure/AWS/GCP in Spain (`Spain Central` / `eu-south-2`) while establishing a **verified warm-standby OpenTofu + CloudNativePG/Velero cluster** on **Stackscale**, **Alhambra IT**, or **Digital Realty Madrid** interconnected via ESpanix/Equinix Fabric (<2 ms latency).
    3. **Broadcom VMware Renewal Crisis (50–500 VMs):** Avoid panic hardware buys. Pitch a phased 90-day transition into either managed **VCSP Cloud Director** (Arsys/Gigas/Alhambra) to buy 24 months of stability, or direct greenfield repatriation onto **Proxmox VE + Ceph / OpenShift Virtualization 5** in **Stackscale** or **DATA4/Interxion** racks.
    4. **High-Egress Spanish B2B SaaS / MarTech / Streaming:** Benchmark their current AWS/GCP Data Transfer line item. Migrating static APIs, Kubernetes workers, and object storage onto **Stackscale / OVHcloud / UpCloud (`es-mad1`) / Scaleway** commonly slashes monthly OPEX by **45–65%**.
    5. **Spanish Enterprise GenAI with Confidential IP:** Host **Mistral / Llama / EuroLLM / Salamandra** open-weight inference via `vLLM` + `llm-d` on dedicated liquid-cooled GPU nodes at **Merlin-Edged** or **Seeweb/Scaleway/Nebius**, feeding **OpenShift AI** or **OKF/RAG** pipelines without leaving EU boundaries.
""",
    "eu-cloud-germany.md": """## Pre-Sales Field Guide: Germany Sovereign Cloud and Private Data Centers

1. [Why Germany Anchors Europe's Industrial Sovereign Cloud](#why-germany-anchors-europes-industrial-sovereign-cloud)
2. [Comprehensive German Cloud and Data Center Pre-Sales Matrix](#comprehensive-german-cloud-and-data-center-pre-sales-matrix)
3. [US Hyperscaler Regions in Frankfurt vs German BSI C5 Providers](#us-hyperscaler-regions-in-frankfurt-vs-german-bsi-c5-providers)
4. [German Enterprise Pre-Sales Playbooks](#german-enterprise-pre-sales-playbooks)

### Why Germany Anchors Europe's Industrial Sovereign Cloud

Germany represents continental Europe's largest enterprise cloud market, combining strict statutory auditing with open-source federation standards:

- **BSI C5 Type 2 and KRITIS Enforcement:** The German Federal Office for Information Security (**BSI**) requires **C5 Type 2** attestations across healthcare (SGB V), regulated finance, and **KRITIS** critical infrastructure operators.
- **DE-CIX Frankfurt Core Peering:** As the world's largest Internet Exchange (**17+ Tbps** peak throughput), **DE-CIX Frankfurt** sits directly adjacent to Tier III+/IV campuses (**Equinix, Digital Realty, maincubes**), giving hybrid private-cloud designs sub-2 ms interconnect latency.
- **Sovereign Cloud Stack (SCS) Standardization:** Funded by the German government and backed by OSBA, **STACKIT, PlusServer, Cleura, and SysEleven/secunet** implement modular, auditable open-source **OpenStack + Kubernetes + Ceph** standards so Mittelstand and public-sector buyers never swap hyperscaler lock-in for local lock-in.
- **Cost Floor vs Enterprise Scale:** Germany uniquely spans both extremes of TCO — from **Hetzner's** unbeatable bare-metal/VM price floor (65–75% below AWS) to industrial-scale German retail/telecom hyperscalers (**STACKIT**, **IONOS**, **Open Telekom Cloud**).

### Comprehensive German Cloud and Data Center Pre-Sales Matrix

| Provider / Operator | HQ and German DC Footprint | Sovereignty and Certs | Core Platforms and Hypervisors | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **STACKIT (Schwarz Digits)** | Neckarsulm; multiple German Tier III+ 3-AZ regions | **L4 EU Sovereign**, **BSI C5 Type 2**, ISO 27001/27017/27018, DORA/NIS2 | OpenStack IaaS + **SAP Gardener Managed Kubernetes (SKE)** + DBaaS (PG/MariaDB/Redis) + S3 Object Lock | **~75%** (`stackitcloud/stackit` OpenTofu/Terraform + Gardener CRDs) | Multi-DC German AZ SLA; transparent EUR egress & intra-DE replication | German Mittelstand, retail, automotive, and public sector wanting **enterprise PaaS parity under pure German ownership** |
| **IONOS Cloud (United Internet)** | Montabaur/Berlin; Frankfurt, Berlin, Logrono (Arsys sister), Paris, London | **L4 EU Sovereign**, **BSI C5 Type 2**, ISO 27001, DORA-aligned | Custom KVM Enterprise Cloud, **Data Center Designer**, Managed K8s, DBaaS, NVIDIA H200 | **~80%** (Official Terraform + **Native Crossplane** + **CAPMOX Proxmox CAPI**) | Multi-zone Frankfurt/Berlin replication; predictable EUR bandwidth | Cross-border **Germany + Spain** groups (unified with **Arsys**) & Crossplane-driven platform teams |
| **Hetzner** | Gunzenhausen; Falkenstein, Nuremberg, Helsinki (+ US/SG opt-in) | **L4 German Owned**, ISO 27001, green hydro energy, strict GDPR | Cloud VMs (**CX/CPX/CAX/CCX**), **Dedicated Root Servers**, Storage Boxes, Private Networks | **~75% IaaS** (`hcloud` + **Syself CAPH** + `kube-hetzner`); 0% managed PaaS | High-uptime DC SLAs; **20 TB included traffic/VM** (~EUR 1/TB overage) | Platform engineering teams running **Talos/RKE2/K3s**, CI/CD runners, high-bandwidth SaaS at maximum savings |
| **Open Telekom Cloud (T-Systems)** | Frankfurt/Bonn; **Biere and Magdeburg** twin German DCs | **L4 EU Controlled**, **BSI C5**, **TISAX (Automotive)**, KRITIS, ISO 27001 | Enterprise OpenStack IaaS, **Cloud Container Engine (CCE)**, RDS, ModelArts, KMS | **~75%** (`opentelekomcloud` Terraform + full OpenStack REST compatibility) | Dual-city Biere–Magdeburg active/passive DR (>80 km split); enterprise telco SLA | **German automotive (TISAX)**, statutory healthcare, and KRITIS utilities migrating legacy SAP/ERP |
| **secunet Cloud / SysEleven** | Essen / Berlin; multi-AZ German sovereign DCs | **L4 German Cybersecurity Group**, **BSI C5**, ISO 27001, **SCS aligned** | OpenStack IaaS + **MetaKube (Kubermatic) Managed Kubernetes** | **~75%** (`openstack` Terraform + MetaKube/CAPI + Ansible) | 99.95–99.99% cluster SLA; 3-AZ German synchronous etcd/quorum | SaaS, FinTech, and defense-adjacent engineering teams wanting **BSI-hardened 24x7 Managed Kubernetes** |
| **PlusServer** | Cologne; German Tier III+ sovereign DCs | **L4 EU Sovereign**, **BSI C5**, ISO 27001, **SCS founder** | Sovereign Cloud Stack (OpenStack + K8s), **VMware VCSP Cloud Director**, Bare Metal | **~65–75%** (`openstack` / `vmware/vcd` Terraform + GitOps) | Multi-DC German geo-replication; Veeam/Zerto managed DRaaS | Mid-market German Broadcom VMware exits and regulated SaaS needing managed hybrid operations |
| **noris network / Cloud&Heat / Delos** | Nuremberg/Munich (noris), Dresden (Cloud&Heat), German public sector (Delos) | **BSI C5**, **TISAX**, ISO 27001/22301; SAP/Microsoft German sovereign (Delos) | Private Tier III+ clouds, liquid-cooled AI compute (**Cloud&Heat**), German public sector sovereign cloud (**Delos**) | **~60–80%** (Terraform/OpenStack/Ansible; Azure APIs on Delos) | High-availability private cages + zero-water/hot-water green cooling | **Federal/State government (Delos)**, Tier-1 Munich banking/insurance (**noris**), and low-PUE green AI (**Cloud&Heat**) |
| **Equinix / Digital Realty / maincubes + JUPITER** | Frankfurt (**FR1–FR8, FRA**), Berlin, Nuremberg | Tier III+/IV, ISO 27001/50001, **EN 50600**, **DE-CIX** direct peering | **Private Bare Metal + Proxmox VE / OpenStack SCS / OpenShift 5**; **JUPITER 24k GH200 EuroHPC** (Juelich) | **~75–90%** (`bpg/proxmox`, `CAPO`, `CAPMOX`, Ansible) | Up to **99.999% power/cooling** across dual Frankfurt metro zones | Wholesale repatriation (>300 VMs), DE-CIX financial low-latency trading, and EuroHPC foundation model AI |

### US Hyperscaler Regions in Frankfurt vs German BSI C5 Providers

*Evaluating Frankfurt hyperscalers (`AWS eu-central-1` / `AWS European Sovereign Cloud Brandenburg`, `Azure Germany West Central`, `GCP europe-west3 Frankfurt`) against native German L4 providers:*

| Evaluation Criterion | US Hyperscalers (AWS / Azure / GCP Frankfurt + AWS ESC) | German Sovereign Clouds (STACKIT / IONOS / Hetzner / Open Telekom / PlusServer) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Ownership and CLOUD Act Exposure** | US parent remains bound by **US CLOUD Act / FISA 702** (AWS ESC isolates EU ops to L2) | **100% German/EU corporate ownership** — zero US corporate control chain | Mandatory win factor for German ministries, hospitals, KRITIS, and defense suppliers. |
| **Monthly Compute and Egress Cost** | Full hyperscaler list pricing (**+15–30% Sovereign isolation premium** on AWS ESC); **~EUR 0.085/GB egress** | **Hetzner 65–75% lower**; **IONOS / STACKIT / OTC 35–55% lower** with generous/predictable EUR traffic | Benchmark egress + idle VM over-provisioning: typical SaaS saves **EUR 2,000–12,000/month** on migration. |
| **Open Source Portability (SCS / OpenStack)** | Proprietary IAM, KMS, DynamoDB, CloudFormation lock-in | **Sovereign Cloud Stack / OpenStack / SAP Gardener** — standardized APIs | Protects against single-vendor fee hikes (matching **EU Data Act / DORA Art. 28** mandates). |
| **SAP and Industrial Integration** | Managed SAP HANA options on Azure/AWS | Native **STACKIT / Delos / Open Telekom Cloud** German industrial & SAP ecosystem | German automotive & retail frequently prefer native sovereign hosting alongside **RISE / Gardener**. |

### German Enterprise Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in Germany"
    1. **Automotive Supply Chain (`TISAX`) and Mittelstand ERP:** Lead with **Open Telekom Cloud** (Biere + Magdeburg active/passive DR) or **noris network** + **PlusServer**. Highlight TISAX, BSI C5 Type 2, and clean **VMware VCSP -> OpenStack** migration paths.
    2. **DORA Financial Institution Needing OpenTofu + Crossplane:** Pitch **IONOS Cloud** (native Crossplane + BSI C5) or **STACKIT** (SAP Gardener SKE + BSI C5) as either primary sovereign platform or tested EU Exit Target behind **DE-CIX Frankfurt** peering.
    3. **Cost-Crushed SaaS / AI Inference Platform (High Egress):** Migrate Kubernetes stateless workers and CI/CD pipelines onto **Hetzner Cloud / Dedicated Root Servers** via **Syself CAPH / Talos Linux** (saving 65–75%), optionally pairing PostgreSQL/WORM backups on **STACKIT** or **OVHcloud**.
    4. **Unified German + Spanish Corporate Group:** Leverage the **IONOS Cloud (DE) + Arsys (ES)** corporate umbrella so CTOs gain **BSI C5 Type 2 in Frankfurt/Berlin** alongside **ENS Alto in Madrid/Logrono** under consistent CloudAPIv6 Terraform governance.
    5. **German Public Health / Federal Agency (`BSI C5 + KRITIS`):** Position **secunet Cloud / SysEleven**, **STACKIT**, or **Delos Cloud** (for mandatory Microsoft M365/Azure workloads) alongside verified air-gapped Veeam/S3 Object Lock vaults.
""",
    "eu-cloud-france.md": """## Pre-Sales Field Guide: France Sovereign Cloud and Private Data Centers

1. [Why France Leads European Legal Sovereignty (SecNumCloud 3.2)](#why-france-leads-european-legal-sovereignty-secnumcloud-32)
2. [Comprehensive French Cloud and Data Center Pre-Sales Matrix](#comprehensive-french-cloud-and-data-center-pre-sales-matrix)
3. [French Hyperscaler JVs (Bleu and S3NS) vs Native L4 French Clouds](#french-hyperscaler-jvs-bleu-and-s3ns-vs-native-l4-french-clouds)
4. [French Enterprise Pre-Sales Playbooks](#french-enterprise-pre-sales-playbooks)

### Why France Leads European Legal Sovereignty (SecNumCloud 3.2)

France has built Europe's most stringent legal and architectural sovereignty ecosystem, combining **ANSSI SecNumCloud 3.2**, massive homegrown scale (**OVHcloud**, **Scaleway**), and continental AI leadership (**Mistral AI**):

- **ANSSI SecNumCloud 3.2 Legal Shield:** Unlike generic ISO 27001 certifications, **SecNumCloud 3.2** explicitly audits both deep technical hardening AND corporate shareholding rules (capping non-EU ownership below blocking thresholds) to immunize French data against US CLOUD Act subpoenas.
- **HDS (Hebergement de Donnees de Sante):** French healthcare workloads require strict **HDS** accreditation alongside GDPR, widely supported by **3DS OUTSCALE, OVHcloud, Scaleway, Cloud Temple, and Clever Cloud**.
- **Paris + Marseille Dual Gateway:** **Paris-Saclay / Saint-Denis (DATA4, Equinix PA, OVH Paris 3-AZ)** anchors Europe's largest domestic zero-egress cloud core, while **Marseille (Digital Realty MRS1–MRS4, France-IX)** ranks among the world's top subsea-cable interconnection hubs linking Europe, Africa, the Middle East, and Asia.
- **Open-Weight AI Powerhouse:** With **Mistral AI**, **Scaleway NVIDIA B200/H100 clusters**, and **GENCI Jean Zay**, France lets enterprises build completely non-US GenAI pipelines end-to-end.

### Comprehensive French Cloud and Data Center Pre-Sales Matrix

| Provider / Operator | HQ and French DC Footprint | Sovereignty and Certs | Core Platforms and Hypervisors | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OVHcloud** | Roubaix; **3-AZ Paris**, Gravelines, Strasbourg, Roubaix (+ DE/PL/UK) | **L4 French Listed**, **SecNumCloud 3.2** (Hosted Private Cloud / Bare Metal), ISO 27001, HDS, PCI-DSS | OpenStack Public Cloud, **Managed K8s (MKS — free control plane)**, VMware Bare Metal, Managed DBs, S3 KMS | **~80%** (`ovh/ovh` + `openstack` Terraform, Pulumi, Ansible, vRack APIs) | **0 EUR internet egress** on Public Cloud & Bare Metal; unlimited private vRack L2 | #1 European hyperscaler alternative when **massive zero-egress TCO + multi-AZ scale** matter |
| **Scaleway (Iliad Group)** | Paris; **3-AZ Paris (PAR1–PAR3)**, Amsterdam, Warsaw | **L4 French Owned**, ISO 27001, HDS, EU Data Act pioneer, Sovereign AI | **Kubernetes Kapsule** & multi-cloud **Kosmos**, Serverless Containers/Jobs, Bare Metal, **H100/B200/L40S GPUs & AI Endpoints** | **~85%** (#1 EU DevOps DX: Terraform, **Official Crossplane**, Pulumi, Ansible) | High-availability 3-AZ Paris regions; generous free egress quotas | Cloud-native SaaS, **Platform/Terraform teams**, and **elastic European NVIDIA GPU / Mistral inference** |
| **3DS OUTSCALE (Dassault Systemes)** | Saint-Cloud; **3 isolated French regions** | **L4 French Owned**, **Full-scope ANSSI SecNumCloud 3.2** across IaaS, HDS, ISO 27001 | Proprietary sovereign IaaS with **AWS EC2/IAM-compatible API** (**Cockpit**), **OKS Managed K8s**, DirectLink | **~75%** (`outscale/outscale` Official Terraform + AWS-like semantics + Ansible) | True multi-region French resilience (Paris/EU zones); hardened air-gap ready | **Defense, ministries, central banking, healthcare, aerospace** requiring zero-compromise SecNumCloud 3.2 |
| **Cloud Temple** | Paris-La Defense; multiple French Tier III+/IV regions | **L4 French Independent**, **SecNumCloud 3.2 IaaS**, HDS, ISO 27001 | Sovereign Private IaaS, Dedicated Bare Metal, Managed **OpenShift / Kubernetes**, sovereign GPU rooms | **~65–75%** (`terraform` / OpenShift GitOps / Ansible enterprise playbooks) | Dual-DC active replication; 24x7 French-cleared NOC & SOC | CAC-40 regulated financial, healthcare & public agencies demanding high-touch French MSP SLAs |
| **Clever Cloud** | Nantes; French & European sovereign DC footprints (+ Materia) | **L4 French Independent**, SecNumCloud-aligned architecture, ISO 27001 | Zero-ops Git-push PaaS (Heroku/Vercel alternative), auto-scaling runtimes, Managed PG/Redis/S3, Materia K/V | **~70%** (`clevercloud` Terraform provider + Clever CLI GitOps pipelines) | Multi-zone Paris automated failover; predictable per-second compute billing | Engineering orgs replacing US PaaS (**Heroku / Render / Vercel**) with turnkey European sovereignty |
| **Ikoula / DATA4 / Digital Realty / Equinix** | Reims/Eppes (Ikoula), **Paris-Saclay (DATA4)**, **Marseille (Digital Realty MRS)**, **Paris (Equinix PA)** | **Tier III+/IV**, ISO 27001/50001, **France-IX** peering, 100% renewable PPAs | **Customer Private Cloud:** Bare Metal + **Proxmox VE / OpenShift 5 / OpenStack**, wholesale AI racks, EMEA subsea PoPs | **~70–90%** (`bpg/proxmox`, MAAS, CAPI, Ansible) | **99.999%** power/cooling SLA; direct Marseille EMEA submarine handoffs | Repatriated private clouds (>300 VMs), AI colocation in Paris-Saclay, & Mediterranean traffic hubs |
| **Bleu and S3NS** | Isolated French regions (**Bleu**: Capgemini+Orange -> Azure; **S3NS**: Thales -> Google Cloud) | **L3/L4-targeted French JVs** engineered for **ANSSI SecNumCloud 3.2 qualification** | Sovereign Azure/AKS + M365 (**Bleu**); Sovereign GCP/GKE/Vertex (**S3NS**) | **~90–95%** (Azure/GCP Terraform subsets inside sovereign French control planes) | French-staffed isolated ops & Thales/French encryption key custody | Public agencies & CAC-40 firms locked into **Microsoft Azure/M365** or **GCP BigQuery/Vertex** under French governance |

### French Hyperscaler JVs (Bleu and S3NS) vs Native L4 French Clouds

*Decision framework when a French/EU client compares `AWS eu-west-3` / `Bleu (Azure)` / `S3NS (GCP)` against native French L4 champions (`OVHcloud`, `Scaleway`, `3DS OUTSCALE`):*

| Decision Factor | Native French L4 (`OVHcloud` / `Scaleway` / `OUTSCALE` / `Cloud Temple`) | French Sovereign JVs (`Bleu` / `S3NS`) | Standard US Regions (`AWS Paris eu-west-3` / `Azure France Central`) |
| :--- | :--- | :--- | :--- |
| **Legal Immunity & Ownership** | **100% French-owned & governed today**; full SecNumCloud 3.2 available now | Independent French equity structures designed to isolate ops & IP licensing | **L1 only** — US parent remains legally subject to US CLOUD Act |
| **API and Platform Ecosystem** | OpenStack / Kubernetes / AWS-like Cockpit / Crossplane (~75–85% Terraform parity) | Microsoft Azure M365/AKS (**Bleu**) & Google Cloud/GKE (**S3NS**) parity | 100% latest AWS/Azure/GCP proprietary PaaS & AI releases |
| **Monthly Run-Rate TCO** | **40–70% cheaper** (especially with OVH zero-egress & free K8s control plane) | Hyperscaler rates **+ Sovereign JV operational premium** | Full list hyperscaler pricing + **EUR 0.085/GB egress** |
| **Recommended Pre-Sales Strategy** | **Default recommendation** for K8s, VMs, S3, Open-Weight AI, & EU portability | Recommend when **existing Microsoft M365/Azure or GCP estate refactor cost exceeds 24 months** | Avoid for regulated public/HDS/OIV workloads requiring French sovereignty |

### French Enterprise Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in France"
    1. **Strict Ministry / OIV / Defense (`SecNumCloud 3.2 Mandatory Now`):** Lead with **3DS OUTSCALE**, **OVHcloud SecNumCloud Hosted Private Cloud**, or **Cloud Temple**. Highlight zero foreign equity exposure, HDS readiness, and French-cleared personnel.
    2. **Modern SaaS / Terraform / Crossplane Teams Migrating from AWS EKS:** Pitch **Scaleway Kubernetes Kapsule + Official Crossplane + Managed PostgreSQL/S3**. Teams keep clean declarative GitOps while cutting egress/control-plane bloat.
    3. **High-Bandwidth Video / SaaS / Backup Origin:** Migrate onto **OVHcloud Public Cloud (3-AZ Paris) or Bare Metal vRack**. Zero internet egress on Public Cloud/Metal instantly eliminates multi-thousand-euro AWS CloudFront/NAT transfer bills.
    4. **European GenAI with Confidentiality (`Mistral + B200/H100`):** Run **Mistral / Codestral / Llama** inside **Scaleway GPU/AI Endpoints**, **OVHcloud AI**, or dedicated **DATA4 Paris-Saclay** GPU cages via `vLLM` + `llm-d` without touching US LLM endpoints.
    5. **CAC-40 Hybrid M365 + Sovereign Kubernetes Split:** Retain sovereign collaboration/legacy Azure/GCP inside **Bleu / S3NS**, while running stateless high-egress microservices and DORA warm-standby vaults on **OVHcloud / Scaleway / Clever Cloud**.
""",
    "eu-cloud-italy.md": """## Pre-Sales Field Guide: Italy Sovereign Cloud and Private Data Centers

1. [Italy Cloud Sovereignty Strategy (ACN QC3, AI3 and PSN)](#italy-cloud-sovereignty-strategy-acn-qc3-ai3-and-psn)
2. [Comprehensive Italian Cloud and Data Center Pre-Sales Matrix](#comprehensive-italian-cloud-and-data-center-pre-sales-matrix)
3. [Local Hyperscaler Milan Regions vs ACN Qualified Italian Providers](#local-hyperscaler-milan-regions-vs-acn-qualified-italian-providers)
4. [Italian Enterprise Pre-Sales Playbooks](#italian-enterprise-pre-sales-playbooks)

### Italy Cloud Sovereignty Strategy (ACN QC3, AI3 and PSN)

Italy enforces one of Europe's clearest regulatory classification models via the **Agenzia per la Cybersicurezza Nazionale (ACN)** and the **Polo Strategico Nazionale (PSN)**:

- **ACN Cloud Qualification Matrix (`QC1` – `QC3` & `AI1` – `AI3`):** Data is explicitly graded into **Ordinary**, **Critical**, and **Strategic** tiers. Critical/Strategic Italian Public Administration and healthcare workloads demand **ACN QC3/AI3 qualified** providers with verifiable Italian operational sovereignty and encryption custody.
- **Milan (`MIX`) and Northern/Central Resilience Split:** Milan hosts **Equinix ML2–ML5, Aruba IT3 (Bergamo Tier IV, ~50 km northeast of Milan), WIIT Tier IV, and MIX Milan**, while **Rome (Aruba IT4 Tecnopolo Tiburtino)** and **Frosinone (Seeweb)** provide seismic/grid-independent geographic DR pairs (>450 km split).
- **Bologna EuroHPC AI Anchor:** Italy hosts **CINECA Leonardo** (13,800+ NVIDIA A100 GPUs) and European AI Factory capacity, complemented commercially by **Seeweb** and **Aruba**.

### Comprehensive Italian Cloud and Data Center Pre-Sales Matrix

| Provider / Operator | HQ and Italian Campus Footprint | Sovereignty and ACN Certs | Core Platforms and Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Aruba Cloud / Aruba Enterprise** | Bergamo/Arezzo; **IT3 Ponte San Pietro (Milan Tier IV)**, **IT4 Rome**, Arezzo IT1/IT2 | **L4 Italian Owned**, **ACN QC3 + AI3**, ISO 27001/27017/27018/22301, Tier IV Design/Facility | VMware Enterprise Private Cloud, OpenStack/KVM Cloud Server, **Managed Kubernetes**, Bare Metal, Sovereign AI | **~60–75%** (`vmware/vcd` + Aruba Cloud API + OpenStack Terraform / Ansible) | **99.995%** Tier IV campus SLA; active Milan–Rome geo-DR; 100% hydro/solar energy | Italian public tenders, **enterprise VMware VCSP migrations**, banks, and dual-city Milan–Rome architectures |
| **Seeweb** | Frosinone; Milan (Caldera), Rome, Lugano | **L4 Italian Independent**, **Consorzio Italia Cloud**, ISO 27001, EU AI Act focus | KVM Cloud, **Dedicated NVIDIA H100/L40S/A100 GPU clusters**, Kubernetes AI nodes, Private Cloud | **~55–70%** (REST API / Ansible / GPU K8s automation) | Multi-DC Frosinone–Milan replication; **zero hyperscaler egress surprises** | **Italian and Southern EU GenAI/LLM startups**, Sovereign GPU inference, zero-egress K8s nodes |
| **Polo Strategico Nazionale (PSN)** | Qualified Tier IV Italian campuses (TIM, Leonardo, CDP, Sogei consortium) | Maximum **ACN Strategic** national qualification for State & Healthcare | Isolated Sovereign Private Cloud + localized enterprise OpenShift & hyperscaler sovereign planes | **~65–85%** (Enterprise OpenShift/GitOps + Terraform via system integrators) | State-grade geo-redundant Active-Active Italian replication | **Mandatory venue for Italian central ministries, ASL regional healthcare, and strategic state entities** |
| **WIIT** | Milan; Milan Tier IV (`WIIT Cloud`), plus German sovereign DCs | **L4 Listed Italian**, ISO 27001/22301/20000, **DORA & SAP Certified** | Ultra-secure Managed Cloud, **Mission-Critical SAP S/4HANA & ERP hosting**, Private Cloud, DRaaS | **~55–70%** (`vmware/vcd` + Ansible + SAP automation pipelines) | Contractual **Zero-RPO synchronous DR** options between Milan Tier IV sites | Italian **manufacturing, banking (DORA), luxury retail, and SAP ERP systems** requiring near-zero downtime |
| **ReeVo** | Milan; Italian Tier IV campuses across Milan & Rome zones | **L4 Italian Sovereign**, ISO 27001/27017/27018, DORA/NIS2 focused | Hybrid IaaS, Immutable Backup-as-a-Service, Managed SOC/MDR cybersecurity | **~50–65%** (vCD / Ansible / Veeam immutable automation) | Geo-redundant Italian ransomware-proof vaulting & DRaaS | Italian **mid-market companies** bundling sovereign IaaS + 24x7 managed SOC/MDR + immutable backups |
| **TIM Enterprise / Noovle** | Rome/Milan; Tier IV Italian DC network (PSN founding partner) | **L4 Italian Telco**, ACN qualified, strict national telco resilience | Enterprise Hybrid Cloud, Multi-Cloud orchestration, IoT/Telco Edge, sovereign Kubernetes | **~60–80%** (Terraform + OpenShift + Telco MPLS integration) | Carrier-grade national fiber backbone + multi-region Italian recovery | Large multi-branch Italian enterprises uniting SD-WAN/5G private connectivity with sovereign DCs |

### Local Hyperscaler Milan Regions vs ACN Qualified Italian Providers

*Evaluating `AWS eu-south-1 (Milan)`, `Azure Italy North (Milan)`, and `GCP europe-west8 (Milan)` vs Italian L4 providers:*

| Criterion | US Hyperscalers in Milan (`AWS` / `Azure` / `GCP`) | Native Italian Champions (`Aruba` / `Seeweb` / `WIIT` / `PSN`) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Public Administration Eligibility (ACN)** | Standard commercial regions lack strategic **L4 ownership sovereignty** (US parent) | Native **ACN QC3 / AI3** qualification & **PSN** eligibility out-of-the-box | Required differentiator on almost all Italian PA, health trust, and defense tenders. |
| **Dedicated Sovereign SAP & Legacy Support** | Self-managed or SI-billed enterprise support (~10% of spend) | **WIIT & Aruba** deliver turnkey Italian SAP Basis / VMware engineering SLAs | Mid-to-large industrial firms save FTE headcount alongside predictable EUR OPEX. |
| **Bandwidth & GPU Availability** | Heavy `eu-south-1` egress costs (~EUR 0.09/GB) & GPU quota friction | **Seeweb** & **Aruba** eliminate egress traps & supply dedicated **H100/L40S GPUs in Italy** | **40–55% cheaper** for 24x7 Italian LLM inference and high-traffic SaaS/e-commerce. |

### Italian Enterprise Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in Italy"
    1. **Italian Ministry, Municipality, or Healthcare (`ACN QC3/AI3` or `PSN`):** Position **Polo Strategico Nazionale (PSN)** for strategic state tiers or **Aruba Cloud (`ACN QC3+AI3`)** for regional administrations, universities, and regulated SaaS vendors.
    2. **Italian Financial Sector (`DORA Exit Strategy`) & Zero-RPO SAP:** Place mission-critical SAP/ERP and banking workloads in **WIIT Milan Tier IV** or **Aruba IT3/IT4**, pairing **MIX Milan** low-latency fiber for cross-provider warm standby.
    3. **Sovereign Italian GenAI (`Mistral / Llama / Modello Italia`):** Deploy **Seeweb NVIDIA H100/L40S Kubernetes pools** for low-latency private RAG inference in Italy without token leakage outside EU borders.
    4. **Northern Italy VMware Broadcom Consolidation:** Repatriate costly hyperscaler or Broadcom VMs to **Aruba Enterprise VCSP** (pooled licensing stability) or bare-metal **Proxmox/OpenStack** in **Aruba IT3 / Equinix ML5**.
    5. **Mediterranean Cross-Border Resilience (`Milan + Madrid`):** Pair **Aruba IT3 Milan / Seeweb** with **Stackscale / Arsys / DATA4 Madrid** (~25 ms RTT) for true multi-country Southern European disaster recovery free of US hyperscalers.
""",
    "eu-cloud-benelux.md": """## Pre-Sales Field Guide: Netherlands, Belgium and Luxembourg Cloud and Data Centers

1. [Benelux Interconnection Core (AMS-IX, FLAP-D and Luxembourg DORA)](#benelux-interconnection-core-ams-ix-flap-d-and-luxembourg-dora)
2. [Comprehensive Benelux Cloud, AI and Data Center Pre-Sales Matrix](#comprehensive-benelux-cloud-ai-and-data-center-pre-sales-matrix)
3. [US Hyperscalers in Amsterdam and Brussels vs Benelux Specialists](#us-hyperscalers-in-amsterdam-and-brussels-vs-benelux-specialists)
4. [Benelux Enterprise and AI Factory Pre-Sales Playbooks](#benelux-enterprise-and-ai-factory-pre-sales-playbooks)

### Benelux Interconnection Core (AMS-IX, FLAP-D and Luxembourg DORA)

The Benelux triangle anchors both **Europe's highest-capacity Internet peering** and **continental Europe's premier AI & DORA financial ecosystems**:

- **AMS-IX (Amsterdam) FLAP-D Dominance:** Amsterdam sits alongside Frankfurt, London, and Paris as a core European backbone hub, hosting dense **Equinix (Science Park / Schiphol)**, **Digital Realty**, **NorthC**, and **Leaseweb** footprints with sub-5 ms proximity to Belgium and Western Germany.
- **Home to Europe's Flagship AI Hyperscaler (`Nebius`):** Headquartered in **Amsterdam**, **Nebius** leads Europe in mega-scale InfiniBand-interconnected **NVIDIA H100, H200, and Blackwell B200** cloud superclusters across Finland and France — delivering true CoreWeave/AWS `p5` parity under European corporate leadership.
- **Dutch Sector Standards (`BIO` & `NEN 7510`) + Heat Reuse:** Dutch public institutions enforce **BIO** (Baseline Informatiebeveiliging Overheid) and healthcare requires **NEN 7510**, met natively by OpenStack champions **Cyso Cloud** and **Leafcloud**.
- **Luxembourg Tier IV Data Embassies (`LuxConnect` & `Gcore`):** Built for European banking, investment funds (**CSSF/DORA**), and sovereign state "data embassies," Luxembourg combines dual-site **LuxConnect Tier IV** resilience with dark-fiber loops into Brussels, Paris, and Frankfurt.

### Comprehensive Benelux Cloud, AI and Data Center Pre-Sales Matrix

| Provider / Operator | HQ and Benelux / EU Footprint | Sovereignty and Certs | Core Platforms and AI Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Nebius** | **Amsterdam HQ**; Mantsala (Finland), Paris, Iceland EU AI clusters | **European AI Hyperscaler**, SOC 2 Type II, ISO 27001, GDPR | Massive InfiniBand **NVIDIA H100/H200/B200 clusters**, **Managed K8s (MK8s)**, Slurm, Shared Filesystem, Sovereign S3 | **~70–75%** (`nebius` Official Terraform + gRPC/CLI + MK8s GPU GitOps) | Multi-MW hydro/cool European regions; predictable GPU reservation SLAs | #1 European hyperscaler alternative for **LLM training, distributed fine-tuning, and heavy multi-node AI** |
| **Leaseweb** | **Amsterdam HQ**; Amsterdam, Haarlem, Frankfurt, London (+ Global) | **L4 Dutch Owned**, ISO 27001, PCI-DSS, SOC 1/2, NEN 7510 options | **Single-Tenant Bare Metal**, CloudStack/VMware Private Cloud, Dedicated Storage, CDN | **~65%** (`leaseweb` Terraform provider + REST API + Ansible bare-metal PXE) | Direct **AMS-IX** low-latency throughput; massive **25–100 TB/server bandwidth** bundles | AdTech, streaming, gaming, and high-throughput SaaS escaping hyperscaler network egress fees |
| **Cyso Cloud** | **Alkmaar (NL)**; 100% Dutch data centers + EU expansion | **L4 Dutch Owned**, ISO 27001, **NEN 7510 (Healthcare)**, **BIO (Dutch Gov)**, GDPR | 100% **OpenStack IaaS + Cyso Managed Kubernetes**, S3 Object Storage, Managed DBs | **~75%** (`openstack` Terraform provider + Cyso K8s API + Ansible) | High-availability multi-rack Dutch zones; predictable EUR utility billing | Dutch **healthcare (NEN 7510), municipalities (BIO)**, and SaaS teams wanting pure OpenStack without US ties |
| **Leafcloud** | **Amsterdam (NL)**; distributed green urban server rooms across NL | **L4 Dutch Owned**, ISO 27001, **District Heating Circular Energy**, OpenStack Foundation | **Eco OpenStack Public Cloud**, Managed Kubernetes, Sovereign **NVIDIA GPU Nodes** | **~75%** (`openstack` standard Terraform + CAPI `CAPO` compatibility) | Negative/minimal cooling overhead; transparent EUR compute/GPU rates | Green-mandated European AI startups, **ESG-driven enterprises**, and portable OpenStack workloads |
| **Proximus NXT (Telindus)** | **Brussels & Luxembourg**; Tier III+/IV Belgian & Luxembourgish DCs | **L4 Belgian/LU Telecom**, ISO 27001, **DORA/CSSF Financial**, NATO/EU cleared staff | Enterprise Private Cloud, Sovereign Microsoft/VMware/OpenShift platforms, Telco Edge | **~55–75%** (`vmware/vcd` + OpenShift GitOps + Enterprise Ansible) | Active-Active Brussels–Luxembourg fiber rings; strict banking SLAs | **EU institutions in Brussels**, Benelux ministries, and banks operating under strict Belgian/CSSF rules |
| **LuxConnect & Gcore** | **Bettembourg / Bissen / Contern (LU HQ)** + 180+ global Edge PoPs | **State-backed Luxembourg Tier IV** (`LuxConnect`); **LU-HQ Edge/AI** (`Gcore`) | Colocation/Data Embassies (`LuxConnect`); Bare Metal, Managed K8s & **Edge L40S/H100 AI** (`Gcore`) | **~70–85%** (`gcore` Terraform/API; full customer control in LuxConnect cages) | **99.999% Tier IV** dual-site dark-fiber metro rings across Luxembourg | **CSSF/DORA banking resilience**, European Data Embassies, and pan-European Edge AI inference |
| **TransIP / NorthC / Equinix AMS / Digital Realty AMS** | Amsterdam Science Park, Schiphol, Rotterdam, Eindhoven, Brussels | Tier III+/IV, **AMS-IX / NL-ix** direct peering, Climate Neutral DC Pact | Developer VPS (`TransIP`); Regional Edge Colo (`NorthC`); Carrier-Neutral AI/Cloud cages (`Equinix`/`DLR`) | **~45–90%** (`bpg/proxmox`, MAAS, Ansible on bare-metal colo; REST API on VPS) | **<1 ms** peering across FLAP-D optical ring + redundant power grids | High-frequency connectivity, Amsterdam regional disaster recovery, and wholesale Proxmox/OpenShift builds |

### US Hyperscalers in Amsterdam and Brussels vs Benelux Specialists

*Comparing `Azure West Europe (Amsterdam)` / `GCP europe-west4 (Eemshaven)` / `GCP europe-west9/west1 (St-Ghislain Belgium)` against native Benelux platforms:*

| Dimension | US Hyperscalers (`Azure West Europe` / `GCP St-Ghislain`) | Native Benelux Champions (`Nebius` / `Leaseweb` / `Cyso` / `Leafcloud` / `LuxConnect`) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **AI GPU Scale & Cost (`H100 / H200 / B200`)** | Scarce West Europe GPU quotas + high on-demand hourly rates + costly InfiniBand premiums | **Nebius** delivers deep EU **B200/H200/H100** InfiniBand capacity at **40–55% lower cost** | **Nebius + Amsterdam HQ** is the runaway winner for any serious European LLM training/inference RFP. |
| **AMS-IX Egress Economics** | ~EUR 0.08–0.09/GB outbound internet transfer | **Leaseweb & TransIP** bundle **25–100 TB+** on bare metal; **Cyso/Leafcloud** offer predictable EUR rates | Heavy content/CDN origin/SaaS teams cut monthly cloud bills by **50–75%** on Amsterdam metal. |
| **Dutch BIO / NEN 7510 / LU Financial Audits** | US parent CLOUD Act legal conflict requires complex supplementary legal memos | Native **NL/LU corporate domicile**, direct OpenStack auditability, CSSF/BIO familiarity | Smooth procurement approval for Dutch municipalities, hospitals, and Luxembourg asset managers. |

### Benelux Enterprise and AI Factory Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in the Benelux Region"
    1. **Distributed European AI Training & Batch (`H200 / B200`):** Lead with **Nebius** (`MK8s` + Slurm + Sovereign S3). Highlight Amsterdam corporate HQ, green Finnish power economics, InfiniBand RDMA fabric, and clean Terraform pipelines.
    2. **High-Traffic AdTech / Gaming / Streaming in Amsterdam (`>50 TB/mo Egress`):** Anchor heavy workloads on **Leaseweb Single-Tenant Bare Metal** behind **AMS-IX**, layering Proxmox VE or Talos Linux K8s at **60%+ lower TCO** than Azure West Europe.
    3. **Dutch Healthcare & Municipal Cloud (`BIO + NEN 7510`):** Position **Cyso Cloud** or **Leafcloud** (zero-lock-in OpenStack + Managed K8s + heat reuse), meeting Dutch compliance audits without US hyperscaler exposure.
    4. **Luxembourg Fund / Bank Under DORA (`CSSF Exit Strategy`):** Deploy dual-site infrastructure across **LuxConnect Bettembourg & Bissen** (or **Proximus NXT + OVHcloud/STACKIT Frankfurt** cross-border standby) using OpenTofu (`openstack`/`bpg/proxmox`) + Velero/CNPG.
    5. **Dual-Country Iberia + Amsterdam Active-Active:** Combine **Madrid (`Stackscale`)** and **Amsterdam (`Stackscale AMS` or `Leaseweb`/`Scaleway NL`)** on unified OpenStack APIs for ~25 ms EU North–South active replication.
""",
    "eu-cloud-switzerland-dach.md": """## Pre-Sales Field Guide: Switzerland and Austria (Alpine Sovereign Cloud)

1. [Alpine Neutrality: Swiss FADP, FINMA and Zero CLOUD Act](#alpine-neutrality-swiss-fadp-finma-and-zero-cloud-act)
2. [Comprehensive Swiss and Austrian Cloud Pre-Sales Matrix](#comprehensive-swiss-and-austrian-cloud-pre-sales-matrix)
3. [Local AWS and Azure Zurich Regions vs Swiss L4 Sovereign Clouds](#local-aws-and-azure-zurich-regions-vs-swiss-l4-sovereign-clouds)
4. [Alpine Financial and Pharma Pre-Sales Playbooks](#alpine-financial-and-pharma-pre-sales-playbooks)

### Alpine Neutrality: Swiss FADP, FINMA and Zero CLOUD Act

Switzerland (and neighboring **Austria** as DACH/CEE bridge) commands unique enterprise demand across private banking, wealth management, pharmaceuticals, and international NGOs:

- **Non-EU Neutrality + Revised FADP (`revDSG`):** Switzerland is neither an EU/EEA member nor US-aligned on intelligence compulsion, making **100% Swiss-owned cloud providers** (`cloudscale.ch`, `Infomaniak`, `Swisscom`, `VSHN`) immune to extraterritorial foreign subpoenas when coupled with Swiss operational staff.
- **FINMA Circular 2018/3 & Operational Resilience:** Swiss banks and insurers face mandatory **FINMA auditability**, verifiable Swiss/Alpine data residency, and board-level outsourcing exit capabilities directly comparable to EU **DORA**.
- **Swiss–Austrian Cross-Border Continuity:** Combining Swiss sovereignty (**Zurich / Geneva / Lupfig**) with **Austrian EU-resident zones (`Vienna` via Exoscale / Anexia + `VIX`)** gives DACH enterprises simultaneous Swiss banking compliance and seamless EU Single Market reach under **12 ms latency**.
- **Hydro Sustainability & Alps EuroHPC:** Swiss grids run nearly carbon-free (**hydro + nuclear**), anchoring **Green Datacenter**, **Infomaniak heat recovery**, and the **CSCS Alps NVIDIA GH200** national AI supercomputer in Lugano.

### Comprehensive Swiss and Austrian Cloud Pre-Sales Matrix

| Provider / Operator | HQ and Alpine/EU Footprint | Sovereignty and Certs | Core Platforms and Kubernetes Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Exoscale (A1 Group)** | **Lausanne (CH)**; **Zurich, Geneva, Vienna, Frankfurt, Munich, Sofia** | **L4 Swiss/Austrian EU Backing**, ISO 27001, HDS, FINMA-aligned, Zero US ties | CloudStack/KVM VMs, **SKS Managed Kubernetes**, Managed DBs (PG/Kafka/OpenSearch), **SOS S3**, GPUs | **~75%** (`exoscale/exoscale` Official Terraform, CAPI, Pulumi, Ansible) | Transparent CHF/EUR billing; multi-country CH–AT–DE active/passive peering | Financial, SaaS & DACH DevOps needing **both Swiss zones + Vienna/Frankfurt EU zones under one API** |
| **cloudscale.ch** | **Zurich (CH)**; **Zurich & Lupfig** independent Tier III+ DCs | **100% Swiss privately owned & operated**, ISO 27001/27017/27018, FINMA-ready | Pure **Swiss OpenStack Public & Dedicated Cloud** (VMs, Volumes, Private Networks, S3 Objects) | **~75%** (`cloudscale-ch/cloudscale` Official Terraform + OpenStack API + Ansible) | Physically separated Zurich–Lupfig fault zones; **FINMA clean audit trail** | **Swiss banks, insurers, cantons, and healthcare** demanding 100% Swiss shareholding & zero foreign ownership |
| **VSHN and APPUiO Cloud** | **Zurich (CH)**; runs managed PaaS atop **cloudscale.ch** & **Exoscale** | **100% Swiss Managed Service**, ISO 27001, FINMA-aligned operations | **APPUiO Managed OpenShift 4/5**, Managed Kubernetes (**AppCat** DBaaS/queues), GitOps SRE | **~85–90%** (**Native Crossplane / AppCat / ArgoCD / OpenTofu** declarative PaaS) | 24x7 Swiss-based SRE SLA across Swiss sovereign IaaS zones | Swiss enterprises wanting **Managed Red Hat OpenShift + DBaaS strictly on Swiss-owned cloud metal** |
| **Infomaniak** | **Geneva (CH)**; multiple Geneva 100% hydro DCs (Waste-heat district export) | **100% Swiss Independent**, ISO 27001/50001/14001, zero US subsidiary | **Swiss OpenStack Public Cloud** (Compute, Cinder, Swift S3, Load Balancers), kDrive/Swiss Backup | **~70%** (**Standard `openstack` Terraform provider** + OpenStack CLI/Ansible) | Competitive PAYG Swiss Franc pricing; zero vendor lock-in | Eco-focused **Swiss SMEs, NGOs, SaaS teams** standardizing on portable OpenStack APIs |
| **Swisscom Enterprise Cloud** | **Bern/Zurich (CH)**; Tier IV bank-grade Swiss data centers | **Swiss National Telecom**, FINMA bank outsourcing cleared, ISO 27001 | Swisscom Enterprise Cloud, **Managed OpenShift**, sovereign banking & healthcare enclaves | **~60–75%** (Enterprise OpenShift/GitOps + VMware vCD/Ansible) | Highest national SLA + private dark-fiber financial interchanges | Top-tier **Swiss cantonal banks, insurers, federal agencies, and hospitals** requiring national telecom accountability |
| **Anexia (Austria HQ)** | **Klagenfurt / Vienna (AT)**; Vienna, Munich, Zurich, global Edge PoPs | **L4 Austrian EU Sovereign**, ISO 27001/9001, GDPR strict | Enterprise IaaS **Anexia Engine**, **Managed Kubernetes**, Bare Metal, Managed Services | **~70%** (`anexia-it/anxcloud` Official Terraform + Crossplane/Ansible) | Dual-city Austria/DACH redundancy + **VIX Vienna** CEE peering | Austrian/CEE enterprises needing **high-touch DACH SLA, clean ANX Terraform, and EU data residency** |
| **Green Datacenter / Equinix CH / SwissIX / CSCS Alps** | **Zurich, Lupfig, Geneva, Vienna (VIX), Lugano (CSCS)** | Tier III+/IV, **FINMA colocation**, **SwissIX / VIX** peering, EuroHPC | High-density enterprise cages (`Green`/`Equinix`); **CSCS Alps (GH200)** Swiss AI supercomputer | **~75–90%** (`bpg/proxmox`, `CAPO`, OpenShift GitOps on customer hardware) | **99.999%** dual-campus power; Zurich–Geneva–Vienna <12 ms optical rings | Wholesale Swiss bank repatriation, private Proxmox/OpenShift stacks, and sovereign Swiss AI research |

### Local AWS and Azure Zurich Regions vs Swiss L4 Sovereign Clouds

*When Swiss CISOs evaluate `AWS Zurich (eu-central-2)` / `Azure Switzerland North` / `GCP europe-west6` vs `cloudscale.ch` / `Exoscale` / `Infomaniak` / `VSHN`:*

| Decision Factor | US Hyperscalers in Zurich (`AWS` / `Azure` / `GCP`) | Native Swiss Sovereign Clouds (`cloudscale.ch` / `Exoscale` / `Infomaniak` / `VSHN`) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Legal Immunity (US CLOUD Act)** | US corporate parent remains exposed to extraterritorial legal demands despite physical Swiss DCs | **Zero US parent / zero CLOUD Act jurisdictional reach** (`cloudscale.ch`, `Infomaniak`, `VSHN`) | Critical win condition for Swiss wealth management, biotech IP, law firms, and federal data. |
| **CHF Pricing & Egress Overhead** | Swiss hyperscaler region **carries a +10–15% Swiss regional premium** on top of US list prices | Predictable CHF/EUR billing (`Exoscale`, `cloudscale.ch`, `Infomaniak`) with clean OpenStack transparency | Teams routinely trim **35–55%** off Zurich AWS/Azure run-rates for Kubernetes and DB tiers. |
| **OpenShift / Kubernetes PaaS Parity** | EKS / AKS managed control planes + AWS/Azure proprietary DB lock-in | **VSHN APPUiO Managed OpenShift** & **Exoscale SKS** deliver complete CNCF/Red Hat parity natively in Switzerland | Keeps regulated apps **100% portable** between Swiss public clouds and on-prem Green Datacenter racks. |

### Alpine Financial and Pharma Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in Switzerland and Austria"
    1. **FINMA-Regulated Swiss Bank / Wealth Manager (`Zero Foreign Control`):** Combine **cloudscale.ch (Zurich + Lupfig)** or **Swisscom** IaaS with **VSHN APPUiO Managed OpenShift** and **Green Datacenter** physical custody for ironclad FINMA outsourcing auditability.
    2. **DACH Multi-Country SaaS (`Switzerland + EU Combined`):** Standardize on **Exoscale** (`Zurich` + `Geneva` + `Vienna` + `Frankfurt`), giving engineering a single `exoscale` Terraform/SKS pipeline with clean country-level data-boundary isolation.
    3. **Cost-Optimized OpenStack & ESG Mandate (`Geneva`):** Deploy stateless apps and S3 workloads onto **Infomaniak Public Cloud** using portable `openstack` Terraform modules, leveraging 100% Swiss hydroelectricity and district heat recovery.
    4. **Austrian Mittelstand & CEE Gateway (`Vienna`):** Lead with **Anexia** (`anexia-it/anxcloud` Terraform) or **Exoscale Vienna** peaked at **VIX**, keeping operations strictly inside Austrian/EU legal borders.
    5. **Confidential Swiss Pharma / Legal RAG:** Run open-weight **Mistral / Llama / Apertus** models on dedicated **Swiss private OpenShift AI** clusters in **Green Datacenter Lupfig / Equinix ZH4** — zero prompt telemetry ever leaves Switzerland.
""",
    "eu-cloud-nordics.md": """## Pre-Sales Field Guide: Nordics Green Cloud and AI Factories

1. [Why the Nordics Lead Europe in Green Compute and AI PUE](#why-the-nordics-lead-europe-in-green-compute-and-ai-pue)
2. [Comprehensive Nordic Cloud, 3-AZ OpenStack and AI Factory Matrix](#comprehensive-nordic-cloud-3-az-openstack-and-ai-factory-matrix)
3. [US Hyperscaler Nordic Regions vs Nordic 3-AZ Sovereign Clouds](#us-hyperscaler-nordic-regions-vs-nordic-3-az-sovereign-clouds)
4. [Nordic Enterprise and Green AI Pre-Sales Playbooks](#nordic-enterprise-and-green-ai-pre-sales-playbooks)

### Why the Nordics Lead Europe in Green Compute and AI PUE

Sweden, Finland, Norway, and Iceland combine Europe's cleanest energy grid with pioneering open-source **3-Availability-Zone OpenStack** engineering:

- **100% Renewable Hydro/Geothermal Power & Sub-1.20 PUE:** Industrial Nordic power prices run **30–55% cheaper** than Central Europe (Frankfurt/Amsterdam), while ambient Arctic/fjord free-cooling drops data center **PUE to 1.08–1.20** — cutting AI GPU training total TCO by **35–50%**.
- **Genuine 3-AZ European OpenStack (`Elastx` & `Cleura`):** Unlike single-DC European VPS vendors, Swedish pioneers **Elastx (Stockholm 3-AZ)** and **Cleura** engineered physically separated three-zone OpenStack & Kubernetes clusters capable of true **3-way quorum** (etcd, PostgreSQL Patroni/CNPG, Kafka) without AWS.
- **Public Sector Schrems II Rigor (`eSam` Sweden):** Swedish and Norwegian public agencies strictly enforce the **eSam framework**, systematically disqualifying US-owned hyperscalers for citizen/health systems and favoring **Safespring, Cleura, Elastx, and GleSYS**.
- **Cross-European Bridge (`UpCloud Madrid` + `Nebius Mantsala` + `LUMI`):** Nordic cloud infrastructure powers workloads across the entire continent — from **UpCloud's `es-mad1` Madrid region** (paired with Helsinki) to **Nebius's Finnish H200/B200 clusters** and **CSC's LUMI EuroHPC**.

### Comprehensive Nordic Cloud, 3-AZ OpenStack and AI Factory Matrix

| Provider / Operator | HQ and Nordic / EU Footprint | Sovereignty and Certs | Core Platforms and AI Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Elastx** | **Stockholm (SE)**; **3 physically separated Stockholm AZs** | **100% Swedish Owned**, 100% hydro energy, ISO 27001/27017/27018, DORA-aligned | Enterprise **3-AZ OpenStack**, **Elastx Kubernetes (OKD/upstream)**, Managed PG/Kafka/RabbitMQ, S3 | **~75–80%** (`openstack` Terraform + `CAPO` + Managed DB automation) | True **3-AZ synchronous Stockholm quorum**; transparent EUR/SEK pricing | **Nordic fintech, healthcare, e-commerce** needing genuine 3-AZ resilience off AWS `eu-north-1` |
| **Cleura** | **Karlskrona (SE)**; **3-AZ Sweden**, Karlskrona, Frankfurt, Munich | **100% EU Owned (Iver group)**, **Sovereign Cloud Stack (SCS)** leader, ISO 27001, DORA/NIS2 | Compliant OpenStack Public & Dedicated Cloud + **SAP Gardener Managed Kubernetes** | **~75–80%** (`openstack` Terraform + Gardener Shoot API + SCS conformance) | Multi-region **Sweden + Germany** OpenStack portability; strong EU exit guarantees | Regulated European enterprises demanding **SCS-compliant OpenStack + Gardener Kubernetes** across Nordics & DACH |
| **UpCloud** | **Helsinki (FI)**; Helsinki, **Madrid (`es-mad1`)**, Frankfurt, Amsterdam, Warsaw, London | **L4 Finnish Owned**, ISO 27001, GDPR strict, **MaxIOPS (~100k IOPS)** | High-IOPS Cloud Servers, **Managed Kubernetes (UKS)**, Managed Databases, SDN Private Networks, Object Storage | **~75%** (`UpCloudLtd/upcloud` Official Terraform + Packer + Ansible) | Sub-millisecond NVMe local quorum; cross-EU SDN replication including Madrid | Database-heavy European SaaS wanting **Madrid (`es-mad1`) + Helsinki/Frankfurt** under one Finnish API |
| **GleSYS** | **Falkenberg (SE)**; owned DCs in Falkenberg, Stockholm, Oulu (FI) | **100% Swedish Independent**, ISO 27001/14001, 100% renewable power, heat reuse | OpenStack/VMware Cloud Infrastructure, Bare Metal, Private Racks, Colocation | **~65–70%** (REST/Terraform automation + Ansible + private cloud APIs) | Owned dual-country SE–FI infrastructure + unlimited generous regional bandwidth | Swedish/Nordic SMB & mid-market platforms needing custom **VMware-to-Linux/K8s + colocation** |
| **Safespring** | **Stockholm / Oslo**; 100% Swedish & Norwegian academic/public DCs | **eSam / Schrems II Public Compliant**, zero non-Nordic ownership, 100% hydro | **Pure OpenStack IaaS + High-Throughput S3**, tailored for Sunet/academic & public clouds | **~75%** (Pure `openstack` Terraform + Ansible + standard Swift/S3 APIs) | Multi-site SE–NO research/public federation; strict zero commercial data mining | **Nordic universities, municipalities, hospitals, research institutes** bound by eSam/Schrems II |
| **Green Mountain / atNorth / Verne / Bulk + LUMI** | **Norway, Iceland, Finland, Sweden, Denmark** (Stavanger, Keflavik, Kajaani LUMI, NO1) | **100% Hydro / Geothermal**, PUE **1.08–1.18**, ISO 27001/50001, heat export | Ultra-dense **Liquid-Cooled NVIDIA AI Colo** (50–150+ kW/rack), **LUMI EuroHPC**, **evroc** sovereign EU cloud | **~75–90%** (`bpg/proxmox`, Slurm, OpenShift AI, KubeRay on dedicated GPU clusters) | Gigawatt renewable grid resilience + **Netnod** peering + transatlantic dark fiber | **Large-scale LLM training, HPC batch AI, ESG-mandated enterprise AI factories** |

### US Hyperscaler Nordic Regions vs Nordic 3-AZ Sovereign Clouds

*Evaluating `AWS eu-north-1 (Stockholm)` / `Azure Sweden Central (Gavle)` / `GCP europe-north1 (Hamina Finland)` vs Nordic sovereign champions:*

| Dimension | US Hyperscalers (`AWS Stockholm` / `Azure Sweden` / `GCP Finland`) | Native Nordic Platforms (`Elastx` / `Cleura` / `UpCloud` / `Safespring` / `atNorth`) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Public Sector / `eSam` Eligibility** | Disqualified for many sensitive Swedish/Norwegian citizen & healthcare systems due to US CLOUD Act | **100% cleared** under Swedish `eSam`, **DORA**, and open **Sovereign Cloud Stack** rules | Decisive winner in public tenders and academic/research clouds. |
| **3-AZ OpenStack Parity** | Proprietary AWS AZ constructs + high inter-AZ data transfer fees (~EUR 0.02/GB each way) | **Elastx** & **Cleura** run true **3-AZ physical Stockholm DCs** on standard OpenStack + Gardener | Delivers HA multi-AZ resilience **without AWS lock-in or inter-AZ surprise invoices**. |
| **Large-Scale Liquid-Cooled AI Economics** | Hyperscaler GPU regions mark up energy, cooling, and egress | **atNorth, Green Mountain, Verne, Nebius Mantsala** pass Nordic hydro cost floor directly to customers | **35–50% total TCO savings** on sustained LLM pre-training, distillation, & synthetic data generation. |

### Nordic Enterprise and Green AI Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in the Nordics"
    1. **True 3-AZ AWS `eu-north-1` Exit (`Sweden FinTech / SaaS`):** Migrate EKS + RDS workloads onto **Elastx Stockholm 3-AZ** (`Managed K8s + PostgreSQL + OpenStack Terraform`), keeping 3-zone synchronous quorum with 100% Swedish jurisdiction.
    2. **European Cross-Border OpenStack (`Nordics + Germany`):** Standardize on **Cleura** (Sweden 3-AZ + Frankfurt/Munich), exploiting identical **OpenStack + SAP Gardener** APIs for DORA-compliant sovereign portability.
    3. **Spanish-to-Nordic Database + Latency Pairing (`Madrid + Helsinki`):** Run low-latency API & MaxIOPS PostgreSQL nodes in **UpCloud `es-mad1` (Madrid)** with encrypted warm replication to **Helsinki/Frankfurt** using one Terraform provider.
    4. **AI Model Training Factory (`>1 MW or Multi-Node H200/B200`):** Host latency-insensitive training/fine-tuning in **Nebius Finland**, **atNorth Iceland/Finland**, **Green Mountain**, or **Verne**, streaming LoRA weights south to Paris/Madrid/Milan inference nodes.
    5. **Nordic Municipality / University Research Cloud (`eSam + Schrems II`):** Deploy **Safespring** or **GleSYS** on standardized OpenStack + OpenTofu templates, meeting strict public procurement law cleanly.
""",
    "eu-cloud-uk.md": """## Pre-Sales Field Guide: United Kingdom Sovereign Cloud and Private Data Centers

1. [Post-Brexit UK Sovereignty: NCSC, G-Cloud and FCA Resilience](#post-brexit-uk-sovereignty-ncsc-g-cloud-and-fca-resilience)
2. [Comprehensive UK Sovereign Cloud and Data Center Matrix](#comprehensive-uk-sovereign-cloud-and-data-center-matrix)
3. [AWS and Azure London Regions vs UK Sovereign Alternatives](#aws-and-azure-london-regions-vs-uk-sovereign-alternatives)
4. [United Kingdom Enterprise and Public Sector Playbooks](#united-kingdom-enterprise-and-public-sector-playbooks)

### Post-Brexit UK Sovereignty: NCSC, G-Cloud and FCA Resilience

Although outside the EU legal bloc, the **United Kingdom** forms one of Europe's largest cloud and interconnection markets (**FLAP-D's London Docklands & Slough** corridor) with strict domestic compliance rules:

- **UK GDPR + NCSC 14 Cloud Security Principles:** British government departments, **NHS Health and Social Care Network (HSCN)** contractors, and defense suppliers enforce the **National Cyber Security Centre (NCSC)** cloud principles, Cyber Essentials Plus, and **G-Cloud** framework compliance.
- **FCA / PRA Operational Resilience (DORA Equivalent):** UK banks, clearing houses, and insurers face parallel UK Bank of England / FCA requirements for **exit plans**, impact tolerances, and multi-provider operational resilience across UK sites.
- **London Docklands (`Telehouse` / `Equinix` / `LINX`) + Regional Spine:** **LINX** runs dual independent London peering LANs plus Manchester and Scotland IXPs, allowing active-active England–Scotland designs (**London + Manchester + Edinburgh**) for national grid fault isolation.
- **EU + UK Dual-Residency Reality:** European multinationals serving British and EU customers cannot rely solely on a UK region for EU data-residency compliance (or vice versa in regulated UK government bids) — requiring **clean IaC portability across UK + Continental EU**.

### Comprehensive UK Sovereign Cloud and Data Center Matrix

| Provider / Operator | HQ and UK Campus Footprint | Sovereignty and Certs | Core Platforms and Kubernetes Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Civo** | **London / Stevenage (UK)**; **London (`LON1`)**, **UK Sovereign Dedicated**, Frankfurt, India, US | **L4 UK Headquartered**, **UK Sovereign Cloud Tier**, ISO 27001, Cyber Essentials Plus | Fast **K3s / Talos Managed Kubernetes** (90s boot), Managed DBs, S3, **Civo AI (NVIDIA H100/B200)** | **~75%** (`civo/civo` Official Terraform + Pulumi + GitOps + K8s CAPI) | Flat transparent UK billing with generous included egress & zero surprise NAT fees | UK **FinTech, GovTech contractors, and Kubernetes-first AI engineering teams** replacing costly AWS `eu-west-2` EKS |
| **Pulsant** | **Reading (UK)**; **12+ UK Edge Data Centers** (London, Manchester, Edinburgh, Milton Keynes, Reading, etc.) | **UK Owned**, ISO 27001, PCI-DSS, UK National Critical Resilience | Sovereign Private Cloud (VMware/KVM), High-Availability Colocation, National DRaaS & Edge Interconnect | **~50–65%** (`vmware/vcd` + Ansible + Private Fabric automation) | North–South England–Scotland geo-redundant UK DR rings + **LINX** peering | Distributed **UK enterprises & financial firms** meeting FCA/PRA regional disaster recovery rules |
| **Redcentric** | **Harrogate (UK)**; owned UK Tier III DCs + **HSCN Health Network** | **UK AIM-Listed**, **G-Cloud Framework**, ISO 27001/22301, Cyber Essentials Plus, NHS HSCN | Sovereign Managed IaaS, UK Private Cloud, Managed Immutable Backup/DR, Healthcare Platforms | **~50–65%** (Enterprise VCSP/API + Ansible managed onboarding) | Carrier-connected UK multi-DC failover + 24x7 UK-vetted support | **UK NHS Trusts, central/local councils, and G-Cloud public-sector suppliers** |
| **Brightbox** | **Manchester (UK)**; dual geographically distinct UK zones | **100% British Owned**, ISO 27001, strict UK data residency, GDPR/UK-GDPR | High-availability UK Cloud Servers, Load Balancers, Orbit Object Storage, Private VLANs | **~70–75%** (`brightbox/brightbox` Official Terraform + Ruby/REST CLI + Ansible) | Transparent GBP pricing; independent UK zones with clean API parity | British **SaaS, e-commerce, and engineering teams** seeking simple, long-tenured UK cloud infrastructure |
| **Nscale** | **London HQ (UK)**; UK & Northern European green renewable AI campuses | **UK-headquartered AI Hyperscaler**, sovereign UK/EU AI infrastructure compliance | Large-scale **NVIDIA H100/B200 AI Clusters**, Kubernetes + Slurm orchestration, high-speed parallel storage | **~65–75%** (Terraform/Slurm/K8s GPU automation + vLLM/KServe stacks) | Predictable reserved GPU SLAs powered by renewable Nordic/UK PPAs | UK & European enterprises running **sovereign LLM training, inference, and national AI workloads** |
| **Telehouse London / Equinix UK / LINX** | **London Docklands (North/West/South), Slough, Manchester** | **Tier III+/IV**, ISO 27001/50001, **LINX London & Manchester** peering hubs | Colocation cages supporting **Proxmox VE / OpenShift 5 / OpenStack** + direct Equinix Fabric on-ramps | **~75–90%** (`bpg/proxmox`, `CAPO`, CAPI on customer metal) | **99.999% power/cooling**, Europe's densest transatlantic & European fiber core | Financial low-latency Slough/Docklands workloads and **wholesale AWS `eu-west-2` repatriation** |

### AWS and Azure London Regions vs UK Sovereign Alternatives

*Evaluating `AWS London (eu-west-2)` / `Azure UK South (London) & UK West (Cardiff)` / `GCP europe-west2 (London)` against native UK Sovereign providers:*

| Criterion | US Hyperscalers (`AWS eu-west-2` / `Azure UK South`) | Native UK Providers (`Civo` / `Pulsant` / `Redcentric` / `Brightbox` / `Nscale`) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Pricing Predictability & EKS Egress Costs** | High London regional pricing + expensive AWS NAT Gateway + ~GBP 0.08/GB internet egress | **Civo & Brightbox** eliminate control-plane bloat & surprise transfer fees (**45–65% cheaper**) | Kubernetes SaaS & B2B APIs leaving `eu-west-2` recover engineering ROI quickly. |
| **NHS HSCN & G-Cloud Specialization** | Generic hyperscaler SKUs require complex partner wrappers & UK security overlays | **Redcentric** & **Civo Sovereign** are architected natively for **G-Cloud / HSCN / NCSC** compliance | Clear audit advantage for UK healthcare, justice, policing, and local authorities. |
| **FCA/PRA Cross-Provider Operational Resilience** | Single-cloud dependency inside AWS/Azure fails exit-portability stress tests | **Civo / Pulsant / Telehouse** provide true cross-vendor **Terraform / Velero** UK exit targets | Helps Chief Risk Officers pass Bank of England / FCA third-party resilience audits. |

### United Kingdom Enterprise and Public Sector Playbooks

!!! success "5 High-Conversion Deals in the United Kingdom"
    1. **UK FinTech Migrating Off Expensive AWS `eu-west-2` EKS:** Move stateless Kubernetes clusters and managed PostgreSQL to **Civo UK Sovereign (`LON1`)** using the official `civo` Terraform provider — trimming monthly infra + egress spend by **50%+**.
    2. **FCA/PRA Financial Operational Resilience (London + Scotland Split):** Anchor core enterprise recovery across **Pulsant London & Edinburgh/Manchester** or pair **AWS `eu-west-2`** with a tested warm-standby **Proxmox/OpenShift** cluster in **Telehouse / Equinix LD**.
    3. **NHS HealthTech & Public Sector Supplier (`G-Cloud + HSCN`):** Lead with **Redcentric UK Sovereign Cloud**, bundling HSCN connectivity, UK-vetted support, and verified immutable DRaaS.
    4. **UK Sovereign Enterprise AI (`UK + Green Nordic Compute`):** Use **Nscale** or **Civo Sovereign AI (H100/B200)** to train/fine-tune regulated models under UK corporate governance without queueing for scarce `eu-west-2` GPUs.
    5. **Post-Brexit Dual EU + UK Compliance Split:** Use portable **OpenTofu + Kubernetes** stacks deploying UK-citizen data to **Civo London / Brightbox** and EU-citizen data simultaneously to **Amsterdam (`Cyso`/`Scaleway NL`)** or **Dublin/Paris (`OVHcloud`)**.
""",
    "eu-cloud-iac-maturity.md": """## Pre-Sales Analysis: IaC Automation and Coverage vs Hyperscalers (100% Baseline)

1. [Master IaC Coverage Scorecard (vs AWS/Azure/GCP = 100%)](#master-iac-coverage-scorecard-vs-awsazuregcp-100)
2. [The API Portability Hack: Standardizing on OpenStack, vCD and Proxmox](#the-api-portability-hack-standardizing-on-openstack-vcd-and-proxmox)
3. [Sovereign OpenTofu State Architecture (Zero US Dependency)](#sovereign-opentofu-state-architecture-zero-us-dependency)
4. [The 6 Real IaC Gaps vs Hyperscalers (and How to Mitigate Them)](#the-6-real-iac-gaps-vs-hyperscalers-and-how-to-mitigate-them)

### Master IaC Coverage Scorecard (vs AWS/Azure/GCP = 100%)

A critical pre-sales honesty check: **AWS, Azure, and GCP maintain ~98–100% IaC API coverage** across every service from day one. European Sovereign Clouds cover **45% to 85%** natively — which is more than enough for **90% of IaaS + Kubernetes + DBaaS workloads** *if you design around the gaps upfront*:

| Provider / Platform | Terraform / OpenTofu Score | Crossplane Support | Cluster API (CAPI) | Pulumi / Ansible | Underlying Standard API Layer | Real Pre-Sales Coverage Assessment |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Scaleway** | **85%** | Official (`crossplane-provider-scaleway`) | Community / Kosmos | Official Pulumi + Ansible | Custom REST + S3 | **EU Leader for DevOps DX:** Covers IAM, Kapsule K8s, DBaaS, S3, Serverless, VPCs cleanly. |
| **OVHcloud** | **80%** | Community / Upjet (`provider-terraform`) | Community / Bare Metal | Pulumi bridge + Ansible | OpenStack + OVH v6 API | Great coverage for Public Cloud, MKS K8s, vRack, DBs; legacy Bare Metal parts mix OVH v6 APIs. |
| **IONOS Cloud** | **80%** | **Official Native Crossplane** | **Built `CAPMOX` (Proxmox)** | Pulumi + Official Ansible | IONOS CloudAPIv6 | Strong enterprise automation for VDCs, K8s, S3, DBaaS; Crossplane support is top-tier in EU. |
| **STACKIT** | **75%** | Via Upjet / `provider-terraform` | Gardener Shoot CRDs | Official Ansible / OpenTofu | OpenStack + STACKIT REST | Very clean OpenTofu for SKE (Gardener K8s), OpenStack VMs, Postgres/MariaDB, Observability. |
| **Hetzner** | **75% IaaS / 40% Total** | Community / Upjet | **Best-in-Class (`CAPH` Syself)** | Pulumi + `hcloud` Ansible | Hetzner Cloud REST | **100% coverage of its narrow IaaS scope**, but zero managed K8s/DBaaS — you automate those with Talos/K3s/CNPG. |
| **Exoscale** | **75%** | Upjet / `provider-terraform` | Community | Pulumi + Ansible | CloudStack-rooted REST + S3 | Clean, fast Terraform for Compute, SKS Kubernetes, DBaaS, Security Groups, SOS S3. |
| **cloudscale.ch** | **75%** | Upjet / `provider-terraform` | OpenStack / VSHN APPUiO | OpenTofu + Ansible | Swiss OpenStack + REST | Pure Swiss-owned API covering VMs, volumes, private networks, & S3 cleanly. |
| **Leaseweb** | **65%** | Upjet / `provider-terraform` | Bare Metal / K8s PXE | OpenTofu + Ansible | Leaseweb REST + CloudStack | Automates NL/EU dedicated bare metal, private networking, & bandwidth bags cleanly. |
| **Anexia** | **70%** | Native Crossplane + Upjet | Anexia Kubernetes Service | Official Terraform + Ansible | AnxCloud REST | Mature Austrian/DACH Terraform & Crossplane coverage (`anexia-it/anxcloud`). |
| **UpCloud** | **75%** | Upjet / `provider-terraform` | Community | Ansible + OpenTofu | UpCloud REST + S3 | Full lifecycle for Madrid (`es-mad1`)/EU VMs, MaxIOPS, Managed K8s, Managed DBs, SDN routers. |
| **Open Telekom Cloud** | **75%** | Upjet / OpenStack CRDs | OpenStack `CAPO` compatible | Official Ansible + OpenTofu | OpenStack + Huawei/OTC APIs | Mature coverage for VPCs, CCE Kubernetes, RDS, KMS, EVSs; slower feature velocity than Scaleway. |
| **Civo (UK)** | **75%** | Upjet / `provider-terraform` | K3s/Talos native | Pulumi + Ansible | Civo REST + S3 | Built specifically for Terraform + Kubernetes-first automation; tiny IaaS surface makes 75%+ easy. |
| **Nebius** | **70%** | Upjet / `provider-terraform` | MK8s GPU pools | OpenTofu + Ansible | Nebius API + gRPC | Rapidly maturing Terraform coverage for H100/H200 clusters, Shared Filesystems, MK8s, S3. |
| **Arsys (Spain)** | **55–75%** *(tier dependent)* | Via IONOS Crossplane (Public) / Upjet | Via `CAPVCD` (Enterprise Cloud) | `vcd` + IONOS Ansible | **IONOS CloudAPI** (Public) + **VMware vCD** (Enterprise) | Use **Enterprise/IONOS-backed API tiers**, NOT legacy SMB VPS panels; unlocks full Terraform/vCD automation. |
| **Gigas (Spain)** | **50–65%** | Via `provider-terraform` (`vcd`) | **`CAPVCD` / `CAPO`** | Ansible + `vmware/vcd` | **VMware Cloud Director / OpenStack** | VMs, vApps, NSX Edge firewall/NAT, disks are scriptable via `vmware/vcd`; telco MPLS/cross-connects remain ticketed. |
| **Alhambra IT (Spain)** | **45–65%** | Via `provider-terraform` | `CAPVCD` / Proxmox `CAPMOX` | **Ansible + OpenTofu** | **VMware vCD / Proxmox / K8s** | Compute & Kubernetes layers automate cleanly; contractual bespoke firewall/BGP changes involve MSP change tickets. |
| **Telefonica Tech VDC** | **50–65%** *(95% on Google Sov.)* | Via `provider-terraform` | `CAPVCD` / Anthos | Ansible + Terraform (`vcd` / `google`) | **VMware vCD / OpenStack / GCP** | Use `vmware/vcd` for VDC; if near-100% hyperscaler IaC is non-negotiable, Telefonica + Google Sovereign wins. |
| **Private DC (Proxmox / OpenStack)** | **75–90%** | Upjet / OpenStack CRDs | **`CAPMOX` / `CAPO` / `CAPC`** | **Ansible + `bpg/proxmox` / `openstack`** | **Proxmox VE / OpenStack / CloudStack API** | **Best long-term portability:** Customer owns 100% of APIs from physical switch/VLAN (Ansible/NetBox) to K8s CAPI. |

### The API Portability Hack: Standardizing on OpenStack, vCD and Proxmox

!!! success "How Senior Architects Beat Proprietary Cloud Lock-In (80–90% Module Reuse)"
    Never write custom glue against 5 different niche Spanish/European portals. Anchor your **OpenTofu modules** and **Cluster API (CAPI) fleets** on one of Europe's **three universal infrastructure API standards**:

    1. **OpenStack Standard (`terraform-provider-openstack` + `CAPO`):** Write ONE network/security-group/VM/Cinder module and deploy identically across **Stackscale (Madrid/Amsterdam), Cleura (Sweden/Germany), Elastx (Sweden), OVHcloud Public Cloud (PCI layer), STACKIT core, Open Telekom Cloud, and Infomaniak**.
    2. **VMware Cloud Director Standard (`vmware/vcd` + `CAPVCD`):** Standardize on `vmware/vcd` OrgVDC + NSX-T Edge Gateway resources to deploy consistently across **Arsys, Gigas, Alhambra IT, Telefonica Tech VDC, Acens, PlusServer, and Aruba VCSP**.
    3. **Proxmox VE API Standard (`bpg/proxmox` + IONOS `CAPMOX`):** Standardize private bare-metal colocation in **Digital Realty, Equinix, Nabiax, DATA4, or Hetzner/OVH Metal** on Proxmox VE 8/9 + Ceph, getting clean cloud-init VMs, SDN VXLANs, and declarative Kubernetes node lifecycle at **zero per-core hypervisor tax**.

### Sovereign OpenTofu State Architecture (Zero US Dependency)

Avoid storing European sovereign OpenTofu state in AWS S3 or HashiCorp Cloud (`HCP`). Store remote state and locking inside an **EU-owned S3 Object Lock backend** (OpenTofu >= 1.10 native S3 lockfile `use_lockfile = true`, or DynamoDB-free locking):

```hcl
terraform {
  required_version = ">= 1.10.0"

  backend "s3" {
    bucket                      = "acme-es-sovereign-tfstate-mad"
    key                         = "prod/platform-core/terraform.tfstate"
    region                      = "eu-south-mad" # or rbx / fr-par / de-fra
    use_lockfile                = true           # Native S3 conditional lock (zero DynamoDB needed)
    skip_credentials_validation = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    skip_s3_checksum            = true
    endpoints = {
      s3 = "https://s3.fr-par.scw.cloud"         # Or OVH / IONOS / Arsys / MinIO Sovereign Madrid
    }
  }
}
```

### The 6 Real IaC Gaps vs Hyperscalers (and How to Mitigate Them)

| IaC Gap Category | What Breaks Coming From AWS/Azure/GCP | Practical Mitigation Pattern (2026 Pre-Sales Design) |
| :--- | :--- | :--- |
| **1. Workload IAM & OIDC Federation** | Fewer fine-grained resource-policy IAM JSON engines (like AWS IAM Policies / Azure RBAC) for micro-services. | Standardize app & CI auth inside Kubernetes via **Keycloak / Dex OIDC**, **External Secrets Operator + OpenBao/Vault**, and GitHub Actions OIDC -> Envoy/WireGuard. |
| **2. Ticket-Driven BGP, MPLS & VLANs** | In Spanish MSPs (Gigas, Alhambra, Telefonica VDC), telco MPLS cross-connects or L2 trunk changes often still require a human NOC ticket. | Treat physical/BGP edge as an **immutable Level-0 landing zone** provisioned once at onboarding; manage all dynamic app routing inside NSX/SDN or **Cilium BGP**. |
| **3. Managed DB / Kafka Day-2 Parity** | Some local providers lack Terraform resources for point-in-time recovery triggers, read-replica promotion, or extension flags. | Run **CloudNativePG** + **Strimzi Kafka** directly inside your Managed/Talos Kubernetes cluster on NVMe volumes — **100% GitOps-controlled across every provider**. |
| **4. Missing Native Crossplane Providers** | Upbound officially maintains AWS/Azure/GCP Crossplane providers; smaller EU clouds lack first-party Go providers. | Use **Crossplane `provider-opentofu` / Upjet** wrapping official OpenTofu providers, OR delegate infrastructure lifecycle cleanly to **OpenTofu (Landing Zone) + Argo CD + CAPI (Clusters)**. |
| **5. Golden Image Pipelines** | Fewer cloud-native AMIs/Marketplace images pre-hardened to CIS/ENS Alto on smaller MSPs. | Run **HashiCorp Packer + Ansible CIS/ENS Lockdown** (or **Talos Linux Image Factory**) exporting immutable QCOW2/OVA/Raw images uploaded via API. |
| **6. Granular FinOps / Showback Tagging APIs** | Billing APIs rarely match AWS Cost & Usage Reports (CUR) granularity at sub-resource tag level. | Install **OpenCost + Prometheus** inside every Kubernetes cluster and scrape provider billing CSV/APIs into a central Grafana FinOps dashboard. |
""",
    "eu-cloud-workloads-stack.md": """## Pre-Sales Engineering Guide: Hypervisors, IaaS, Kubernetes and Sovereign AI Stacks

1. [Post-Broadcom Hypervisor Modernization Matrix](#post-broadcom-hypervisor-modernization-matrix)
2. [Virtualized IaaS vs Dedicated Bare Metal (When Metal Wins)](#virtualized-iaas-vs-dedicated-bare-metal-when-metal-wins)
3. [European Managed Kubernetes vs Declarative DIY Stack](#european-managed-kubernetes-vs-declarative-diy-stack)
4. [Sovereign AI and NVIDIA GPU Factories in Europe (2026)](#sovereign-ai-and-nvidia-gpu-factories-in-europe-2026)

### Post-Broadcom Hypervisor Modernization Matrix

With Broadcom's **VMware Cloud Foundation (VCF)** per-core subscription shifts raising renewal TCO by 2x–4x across Europe, pre-sales architects must clearly position the 7 production hypervisor architectures available in EU Sovereign Clouds and Private Data Centers:

| Hypervisor / Stack | Licensing & Commercial Model | Storage & HA Capabilities | IaC and Kubernetes Integration | Enterprise Support & Maturity | When to Recommend (Pre-Sales Rule) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Proxmox VE + Ceph + PBS** | **Open Source (AGPLv3)**; optional **EUR 110–1,050 / socket / yr** Enterprise support (Vienna HQ) | Native **Ceph HCI**, ZFS local/replication, live migration, SDN VXLAN/EVPN | **`bpg/proxmox`** Terraform + **IONOS `CAPMOX`** Cluster API + Packer | Huge European partner ecosystem (Spain/DE MSPs) | **#1 Default VMware exit** for SMB & mid-market private DCs / Hetzner / OVH Metal needing 70–85% license savings |
| **OpenStack (SCS / Sunbeam / Kolla)** | Open Source (Apache-2.0); Commercial SLAs via **STACKIT, Stackscale, Cleura, Elastx, Canonical** | **Ceph RBD**, NetApp Cinder, OVN multi-tenant SDN, L3/BGP routing | **Standard `openstack` Terraform** + **`CAPO` Cluster API** | Industrial-scale proven across Europe's largest public clouds | **Service providers, telcos, and >20-rack enterprises** building an internal multi-tenant AWS-like private cloud |
| **Red Hat OpenShift Virtualization 5 (KubeVirt)** | Enterprise Red Hat per-core/node subscription (**RHCOS 10 / RHEL 10.2**, **K8s 1.36**) | Ceph / ODF / Trident / Portworx CSI + live VM migration inside K8s pods | **100% GitOps YAML / K8s API / Crossplane / Argo CD** | Top-tier enterprise SLA; **MTV Migration Toolkit** from vSphere | **Mission-critical banking/telco/public sector** unifying VMs and containers on ONE Red Hat platform + RHOAI |
| **Apache CloudStack** | Open Source (Apache-2.0); Commercial support via ShapeBlue | Supports KVM, XCP-ng, NFS, Ceph, StorPool, SANs | **Official CloudStack Terraform + `CAPC` Cluster API** | Very lightweight control plane (~10% op complexity of OpenStack) | Regional MSPs and enterprises wanting AWS-style VPC/zone IaaS with minimal SRE headcount |
| **SUSE Harvester (KubeVirt + Longhorn)** | Open Source (Apache-2.0); Optional SUSE Rancher Prime support | Native **Longhorn** distributed NVMe block + VLAN trunking | Rancher Terraform + **CAPI / Fleet GitOps** | Rapidly adopted by edge/telco & Kubernetes-first teams | Edge campuses, factories, retail stores running unified **Rancher + K8s + light VMs** |
| **VMware Cloud Director (EU VCSP)** | **Broadcom VCSP Partner Program** pooled RAM/core OPEX model | vSAN / NetApp / Dell PowerStore; **Zerto / Veeam CDP** DRaaS | **`vmware/vcd` Terraform + `CAPVCD`** | Highest zero-refactoring stability (familiar vCenter/NSX) | **Time-boxed 12–36 month bridge:** customer has Oracle/ERP appliances that cannot be migrated before hardware EOL |
| **Nutanix AHV** | Per-core HCI subscription (usually 25–40% below aggressive VCF tiers) | Distributed AOS HCI + native asynchronous Metro HA | Official **Nutanix Terraform** + NKP | Turnkey 1-click upgrades; easiest vSphere GUI parallel | Risk-averse private DC teams wanting **VMware-like appliance simplicity** without managing Linux/Ceph internals |

### Virtualized IaaS vs Dedicated Bare Metal (When Metal Wins)

Do **not** blindly put every workload on virtualized cloud instances. Pitch **Dedicated Bare Metal** (on **OVHcloud Metal, Scaleway Elastic Metal, Hetzner Robot, Stackscale Bare Metal, or Arsys Dedicated**) whenever ANY of these 4 triggers applies:

1. **Core-Licensed Commercial Software (Oracle DB, Microsoft SQL Server Enterprise, SAP):** Physical bare-metal core pinning cuts software licensing exposure compared to vCPU sprawl on shared public clouds.
2. **Sustained High Storage IOPS / Low Tail Latency (<1 ms):** Dedicated dual-NVMe RAID or local Ceph eliminates noisy-neighbor hypervisor I/O jitter.
3. **Hyperconverged Private K8s / VM Fleet (>32 vCPUs / >128 GB RAM per node):** Running **Talos Linux** or **Proxmox VE** directly on **EUR 180–450/month bare-metal hosts** with 10–25 Gbps unmetered private networking delivers **2.5x–3.5x better compute density per EUR** than public IaaS VMs.
4. **Physical Hardware Compliance Isolation (PCI-DSS L1 / Banking / Defense):** Dedicated single-tenant chassis guarantees physical isolation and auditability without paying hyperscaler `Dedicated Host` 200% markups.

### European Managed Kubernetes vs Declarative DIY Stack

| Platform | Provider / Origin | Control Plane Cost | Multi-AZ / HA Maturity | Networking (CNI) & Load Balancers | GPU Worker Support | Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OVHcloud MKS** | OVHcloud (FR) | **Free** | **3-AZ** in Paris; Multi-node etcd | Cilium / Calico + OVH Octavia LB | L40S, A100, H100 | Default zero-control-plane-tax EU Managed K8s |
| **Scaleway Kapsule / Kosmos** | Scaleway (FR) | **Free** (Ded. paid tier) | **3-AZ** Paris + Multi-Cloud **Kosmos** | Cilium eBPF + Scaleway LB | **L4, L40S, H100, B200** | Best developer UX + hybrid **Kosmos** nodes (attach Hetzner/Arsys nodes into Scaleway!) |
| **STACKIT SKE** | STACKIT (DE — Gardener) | Transparent metered | **3-AZ** Germany | **Cilium eBPF** + OpenStack Octavia LB | NVIDIA AI SKUs | German enterprise stability; automated Gardener self-healing |
| **IONOS Managed K8s** | IONOS (DE) | **Free** control plane | Multi-DC EU (Frankfurt/Berlin/Spain link) | Calico + IONOS NLB | NVIDIA H200 / Enterprise VMs | Pairs cleanly with **Arsys Spain** & native Crossplane workflows |
| **SysEleven MetaKube** | SysEleven (DE — Kubermatic) | Managed tier | **3-AZ** Germany | Cilium/Calico + LB | Dedicated / OpenStack GPU | SLA-backed production German DevOps clusters |
| **Exoscale SKS** | Exoscale (CH/AT) | Free Starter / SLA Pro | Multi-zone CH/EU | Calico + NLB | NVIDIA RTX / A100 / H100 | Swiss/Austrian regulated K8s simplicity |
| **Civo K8s / Talos** | Civo (UK) | Very low fixed node cost | Multi-region UK / EU | Cilium / Flannel + LB | H100 / B200 GPU instances | Sub-2-minute spin-up for CI/CD, UK Sovereign K8s & AI |
| **Arsys Managed K8s** | Arsys (ES) | Node-based EUR pricing | **Spain ENS Alto** | Managed CNI + LB | Enterprise IaaS GPUs | Spanish public-sector & ENS Alto container workloads |
| **DIY: Talos Linux + Cilium + CAPI** | Any Bare Metal (Hetzner / OVH / Stackscale / Proxmox) | **$0** | 3-DC or 3-AZ customer-controlled | **Cilium eBPF + BGP Gateway API** | **Full NVIDIA DRA / GPU Operator** | Maximum TCO victory (60–75% cheaper than EKS/AKS) for teams with 2+ Kubernetes SREs |

### Sovereign AI and NVIDIA GPU Factories in Europe (2026)

| EU AI Platform / Host | GPU Catalog & Interconnect | Jurisdictional Protection | Software & Serving Stack (`2026`) | Typical Pre-Sales Sweet Spot |
| :--- | :--- | :--- | :--- | :--- |
| **Nebius AI Cloud** | **H100, H200, Blackwell B200** clusters w/ **3.2 Tbps InfiniBand NDR** | **Amsterdam HQ (L4 EU)** + Finland/France clean energy | Managed Kubernetes (MK8s), Slurm, S3, `vLLM`, Ray, Terraform | Multi-node foundation model training, LoRA fine-tuning, high-throughput batch AI in Europe |
| **Scaleway AI & Serverless** | **L4, L40S, H100 SXM, B200/B300** + Serverless AI Endpoints | **French/EU L4** + GDPR / EU AI Act alignment | Kapsule K8s, Managed Inference (`vLLM`), **Mistral/Llama EU APIs** | Fastest elastic GPU spin-up + pay-per-token EU serverless inference with zero US transit |
| **OVHcloud AI** | L40S, H100, AI Deploy, AI Notebooks | **French/EU L4** + SecNumCloud roadmap | MKS K8s, Triton/vLLM containers, **zero egress** for training datasets | Dataset-heavy vision/RAG pipelines moving TBs of European files without egress fees |
| **Seeweb (Italy)** | Dedicated **H100 / L40S / A100** pods & K8s nodes | **Italy/EU L4** (GDPR + EU AI Act ready) | K8s GPU nodes, bare-metal inference, custom RAG stacks | Southern European / Italian enterprises requiring bespoke dedicated GPU servers in EU |
| **Merlin-Edged & Spain Colocation** | Liquid-cooled **100 kW+ racks** ready for **NVIDIA GB200 NVL72** | **100% Spanish Private Facility (`ENS Alto` capable)** | **Red Hat OpenShift AI (RHOAI) + `llm-d` + Mistral/EuroLLM/OKF** | Sovereign Spanish banking, defense, telco AI factories requiring physical air-gap / direct rack custody |
| **MareNostrum 5 (BSC Barcelona)** | Thousands of **NVIDIA Hopper H100** GPUs | **European / Spanish EuroHPC Public AI Factory** | Slurm, PyTorch, **Salamandra / ALIA** multilingual European models | R&D consortia, European SMEs (AI Factory grants), Iberian/European sovereign foundation model training |
""",
    "eu-cloud-resilience-sla.md": """## Pre-Sales Engineering Guide: RPO, RTO, SLAs, Multi-DC DRP and Replication

1. [The 3-AZ Reality Check: Hyperscalers vs European Providers](#the-3-az-reality-check-hyperscalers-vs-european-providers)
2. [Tiered RPO, RTO and SLA Reference Architecture Matrix](#tiered-rpo-rto-and-sla-reference-architecture-matrix)
3. [Contractual SLAs and DORA Fine-Print vs Hyperscalers](#contractual-slas-and-dora-fine-print-vs-hyperscalers)
4. [VM and Kubernetes Replication Stacks (Veeam, Zerto, PBS, CNPG, Velero)](#vm-and-kubernetes-replication-stacks-veeam-zerto-pbs-cnpg-velero)
5. [DORA 3-2-1-1-0 Cross-Provider Ransomware Vault Blueprint](#dora-3-2-1-1-0-cross-provider-ransomware-vault-blueprint)

### The 3-AZ Reality Check: Hyperscalers vs European Providers

A common trap in cloud migrations is assuming every European provider has 3 physically separate Availability Zones (<5 ms RTT apart) like `AWS us-east-1` or `eu-south-2`. **Pre-sales architects MUST match database/cluster quorum topology to the actual DC topology:**

| Topology Pattern | Physical Reality & Inter-DC Latency | Providers Offering This Today | Quorum & Data Safety Implications |
| :--- | :--- | :--- | :--- |
| **True 3-AZ Synchronous Region** | **3 independent buildings/power grids**, 5–30 km apart, **0.5–2 ms fiber RTT**. | **Hyperscalers** + **OVHcloud Paris (eu-west-par)**, **Scaleway Paris**, **STACKIT Germany**, **Elastx Stockholm**, **Cleura Sweden** | Supports synchronous **Ceph**, **etcd 3-member spread**, and **CloudNativePG quorum HA** (`RPO = 0`) surviving total loss of 1 data center. |
| **Dual-DC Metro Stretch (Active-Active)** | **2 independent Madrid/Milan/German DCs**, <1.5 ms RTT, **needs a 3rd tiny Witness DC/node**. | **Alhambra IT Madrid, Telefonica Tech VDC, Gigas, Arsys (Logrono–Madrid), Stackscale (Madrid–Madrid), Aruba Italy, Open Telekom Cloud** | With an **external 3rd-site Witness/Arbiter** (`<20 ms` away), delivers `RPO = 0` Active-Active HA. **Without** a 3rd witness, automatic failover risks Split-Brain! |
| **Multi-Region Asynchronous (`2+` Cities)** | **2 distinct countries/cities** (>10 ms RTT, e.g., Madrid <-> Paris or Madrid <-> Amsterdam). | **Stackscale (Madrid <-> Amsterdam)**, **UpCloud (Madrid <-> Frankfurt)**, **OVH (Gravelines <-> Strasbourg)**, **IONOS + Arsys** | **Cannot** run synchronous storage stretch (too much latency). Requires **async WAL / Ceph RBD / Veeam CDP replication** (`RPO = 5s–15m`). |
| **Single-DC Campus + Offsite Vault** | Single primary campus (e.g., Hetzner Falkenstein vs Nuremberg) + cross-city S3 backup. | **Hetzner**, single-site colocation cages, SMB VPS hosts | **Never place a single-datacenter etcd or database without cross-city replication!** Use Hetzner multi-location clusters (`FSN1` + `NBG1` + `HEL1` via WireGuard/Cilium) or pair with OVH/Scaleway DR. |

### Tiered RPO, RTO and SLA Reference Architecture Matrix

| Business Tier | Target RPO | Target RTO | Target Composite SLA | Proven European Technical Architecture | Cost Overhead vs Single DC |
| :--- | :---: | :---: | :---: | :--- | :---: |
| **Tier 0 — Mission Critical Core (Banking, Payments, Hospital ER)** | **0 sec** *(zero data loss)* | **< 2 min** *(automated)* | **99.995% – 99.999%** *(<26 min downtime/yr)* | **3-AZ Regional Stretch** (`OVH Paris / Scaleway / STACKIT / Elastx`) OR **2 Spanish Metro DCs + 3rd-City Witness** (CloudNativePG sync quorum + Cilium BGP/Anycast LB + NetApp/SAN Sync) + **Cross-Provider Warm DR in FR/DE** | **+95% to +135%** |
| **Tier 1 — Revenue SaaS & Regulated Enterprise ERP** | **5 sec – 5 min** | **15 – 45 min** | **99.95% – 99.99%** | **Dual-DC Async Replication:** Zerto / Veeam CDP for VMs OR **CloudNativePG Continuous WAL + Warm Standby Replica** in secondary EU city + **Velero/GitOps K8s state sync** | **+35% to +55%** |
| **Tier 2 — Standard Corporate Apps & Backoffice** | **1 – 4 hours** | **2 – 6 hours** | **99.9%** *(~8.7 hr/yr)* | Hourly snapshots / **Proxmox Backup Server (PBS) pull sync** OR Veeam hourly backup to secondary DC + **OpenTofu "Cold-Standby IaC Rebuild" pipeline** | **+15% to +25%** |
| **Tier 3 — Dev / Test / Stateless Analytics** | **24 hours** | **12 – 24 hours** | **99.5%** | Daily automated S3 Object Lock backup + 100% declarative recreation via **OpenTofu + Argo CD** from Git | **+5% to +10%** |

### Contractual SLAs and DORA Fine-Print vs Hyperscalers

| SLA / Governance Clause | US Hyperscalers (Standard Click-Wrap Contracts) | European Sovereign Cloud MSPs (Alhambra, Gigas, Arsys, Telefonica, STACKIT, OVH) | Pre-Sales Negotiation Takeaway |
| :--- | :--- | :--- | :--- |
| **Remedy for Breached SLA** | **Capped service credits (10%–25% of affected service only)**; zero consequential damages; burdensome claim window. | **Negotiable bilateral Enterprise SLAs**, real penalty schedules in public/enterprise contracts, holistic VM+Network+Backup SLA coverage. | Hyperscaler "99.99%" SLA only returns a partial credit note — never covers SLA impact to *your* customers. |
| **DORA Audit & Pen-Test Rights (TLPT)** | Standardized SOC2/ISO PDFs; custom on-site regulatory audits heavily restricted or priced steeply. | Direct cooperation with **Bank of Spain / EBA / BaFin / ACPR DORA inspections** + custom Data Processing Agreements (Spanish/EU law). | Huge sales closer in European financial sector deals where compliance blocks generic click-wrap cloud terms. |
| **Production Support Escalation Cost** | AWS/Azure Enterprise Support = **~10% of total cloud spend** (min EUR 1,500–15,000/mo extra) just to talk to senior engineers. | Included or flat low-cost **24x7 Spanish/Local L3 TAM & NOC escalation** (<15 min P1 response). | Always add the **10% AWS/Azure Enterprise Support tax** into TCO comparisons for honest apples-to-apples pricing. |

### VM and Kubernetes Replication Stacks (Veeam, Zerto, PBS, CNPG, Velero)

| Workload Layer | Leading EU Sovereign Tooling | Replication Mechanism | Achievable RPO / RTO | Key Engineering Best Practice |
| :--- | :--- | :--- | :--- | :--- |
| **VMware / Hypervisor VMs** | **Zerto** / **Veeam CDP** / **NetApp SnapMirror** | Hypervisor I/O filter journal replication (CDP) or SAN array-level sync/async replication | **RPO: 5–15 sec** / **RTO: 5–20 min** (orchestrated boot order) | Enforce isolated **Zero-Trust DR management plane** + automated monthly non-disruptive sandbox DR failover tests (DORA compliance). |
| **Proxmox VE Private Clouds** | **ZFS Replication + Proxmox Backup Server (PBS)** or **Ceph RBD Mirroring** | Asynchronous ZFS delta send (1–5 min) + **PBS Pull Sync** into secondary isolated DC | **RPO: 1–15 min** / **RTO: 15–45 min** | **Always configure PBS Pull Mode** from the vault to production (never Push from prod) so compromised prod root keys cannot wipe backups! |
| **Kubernetes Databases (PostgreSQL)** | **CloudNativePG (`CNPG`)** + **Barman Cloud** | Streaming physical replication within region + **Continuous WAL archiving** to cross-provider EU S3 + declarative `ReplicaCluster` | **RPO: <5–30 sec** / **RTO: <3 min** | Pair **Madrid Primary CNPG** with **Paris/Frankfurt ReplicaCluster** streaming from WORM-enabled sovereign S3 buckets. |
| **Kubernetes Cluster State & PVCs** | **Argo CD (GitOps) + Velero / OADP** + **Longhorn / Rook-Ceph Mirror** | Git stores stateless manifests (`0` RPO); Velero/CSI or Rook RBD mirrors PVCs asynchronously | **RPO: 15–60 min** / **RTO: 10–30 min** | Never rely on Velero to restore giant >500 GB databases; let **CNPG/native DB WAL** replicate data and let **Argo CD + Velero** handle manifests & small PVCs. |
| **Multi-Cluster K8s Service Mesh / DNS** | **Cilium ClusterMesh + ExternalDNS / Anycast BGP** | Cross-cluster eBPF WireGuard encryption + health-checked global DNS/Anycast VIP failover | **RTO: 10–60 sec** (network cutover) | Set low DNS TTLs (30s) or terminate Anycast BGP at **Equinix/Cloudflare/DE-CIX** edge to decouple traffic routing from single-DC IP space. |

### DORA 3-2-1-1-0 Cross-Provider Ransomware Vault Blueprint

!!! danger "Why Single-Provider Immutability Fails DORA Concentration Checks"
    If an attacker compromises your primary tenant Root/Org Admin credentials (or a provider billing lock/outage hits), backups sitting inside the *same cloud account or vendor* may become unreachable or deletable. Follow the **3-2-1-1-0 Sovereign Pattern**:

    1. **3 Copies** of production data across **2 media/storage tiers**.
    2. **1 Offsite Copy** inside the primary EU country (e.g., **Arsys Logrono <-> Madrid**, or **Alhambra MAD-DC2**).
    3. **1 Immutable Air-Gapped Cross-Vendor Copy (`WORM` S3 Object Lock — Compliance Mode):** Push Veeam / PBS / CNPG WAL backups via separate **scoped write-only credentials** to a **different EU corporate entity in another EU country** (e.g., primary in **Spain [Stackscale/Alhambra/Arsys]** -> immutable WORM Vault in **France [OVHcloud / Scaleway]** or **Germany [IONOS / Hetzner Storage Box / STACKIT]**).
    4. **0 Recovery Errors Verified:** Automate weekly Ephemeral Sandbox restore drills checking backup integrity (`CNPG recovery`, `Veeam SureBackup`, `PBS verify`), producing signed audit PDFs for **DORA / ENS Alto / NIS2** inspectors.
""",
}
