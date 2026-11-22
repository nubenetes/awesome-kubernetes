import os
import re
import yaml
import asyncio
import httpx
from datetime import datetime
from src.config import GH_TOKEN, INVENTORY_PATH
from src.gemini_utils import normalize_url

# Dimensions mapping from v2_optimizer.py
DIMENSIONS = {
    "AI": ["enterprise-ai-platforms", "ai-agents-mcp", "ai-rag-okf", "ai", "chatgpt", "mlops"],
    "Architectural Foundations": ["introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", "matrix-table", "other-awesome-lists", "about"],
    "Platform & Site Reliability": ["sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering", "performance-testing-with-jenkins-and-jmeter", "project-management-methodology", "project-management-tools", "qa", "test-automation-frameworks", "testops"],
    "Hardened Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", "kubernetes-security", "aws-security", "oauth", "devsecops", "kustomize", "liquibase", "chef"],
    "Cloud Providers (Hyperscalers)": ["aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", "cloudflare", "scaleway", "managed-kubernetes-in-public-cloud", "public-cloud-solutions", "private-cloud-solutions", "edge-computing", "aws-architecture", "aws-security", "aws-networking", "aws-databases", "aws-storage", "aws-monitoring", "aws-iac", "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops", "aws-serverless", "aws-containers", "aws-backup", "aws-training", "aws-newfeatures", "aws-miscellaneous", "aws-pricing", "aws-spain"],
    "European Sovereign Cloud & Private DCs": [
        "eu-sovereign-cloud", "eu-cloud-spain", "eu-cloud-germany", "eu-cloud-france",
        "eu-cloud-italy", "eu-cloud-benelux", "eu-cloud-switzerland-dach",
        "eu-cloud-nordics", "eu-cloud-uk", "eu-cloud-iac-maturity",
        "eu-cloud-workloads-stack", "eu-cloud-resilience-sla",
    ],
    "Networking & Service Mesh": ["networking", "kubernetes-networking", "servicemesh", "istio", "caching", "web-servers", "cloudflare"],
    "The Container Stack": ["docker", "container-managers", "serverless", "kubernetes-autoscaling", "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring", "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise", "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases", "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher", "openshift", "ocp5", "ocp4", "ocp3", "noops"],
    "Data & Advanced Analytics": ["databases", "nosql", "newsql", "message-queue", "crunchydata", "yaml", "bigdata"],
    "Engineering Pipeline": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives", "openshift-pipelines", "sonarqube", "registries", "keptn", "stackstorm", "cicd-kubernetes-plugins"],
    "Developer Ecosystem": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "java_app_servers", "java-and-java-performance-optimization", "dotnet", "angular", "react", "web3", "api", "swagger-code-generator-for-rest-apis", "postman", "lowcode-nocode", "devel-sites", "dom", "linux-dev-env", "ChromeDevTools", "xamarin", "jvm-parameters-matrix-table", "maven-gradle", "embedded-servlet-containers"],
    "Career & Industry": ["recruitment", "hr", "finops", "freelancing", "remote-tech-jobs", "workfromhome", "interview-questions", "elearning", "digital-money", "appointment-scheduling", "newsfeeds"]
}

# Helper to find dimension of a category
def get_dimension_for_category(category: str) -> str:
    if not category:
        return "Architectural Foundations"
    for dim, cats in DIMENSIONS.items():
        if category in cats:
            return dim
    return "Architectural Foundations"

# Canonical human-readable display names for category slugs (single source of truth
# shared across V2 navigation, Topic Map, llms.txt, api/index.json, and fast_enrich).
DISPLAY_NAMES = {
    "GoogleCloudPlatform": "Google Cloud Platform (GCP)",
    "ChromeDevTools": "Chrome DevTools",
    "ai": "AI",
    "ai-agents-mcp": "AI Agents & MCP",
    "ai-rag-okf": "AI RAG & OKF",
    "enterprise-ai-platforms": "Enterprise AI Platforms",
    "chatgpt": "ChatGPT",
    "mlops": "MLOps",
    "api": "API",
    "aws": "AWS",
    "aws-iac": "AWS IaC",
    "aws-devops": "AWS DevOps",
    "aws-newfeatures": "AWS New Features",
    "aws-tools-scripts": "AWS Tools & Scripts",
    "bigdata": "Big Data",
    "cicd": "CI/CD",
    "cicd-kubernetes-plugins": "CI/CD Kubernetes Plugins",
    "cloud-arch-diagrams": "Cloud Architecture Diagrams",
    "crunchydata": "Crunchy Data",
    "devel-sites": "Developer Sites",
    "developerportals": "Developer Portals",
    "devops": "DevOps",
    "devops-tools": "DevOps Tools",
    "devsecops": "DevSecOps",
    "digitalocean": "DigitalOcean",
    "dotnet": ".NET",
    "elearning": "E-Learning",
    "eu-sovereign-cloud": "EU Sovereign Cloud Overview & TCO",
    "eu-cloud-spain": "Spain Sovereign Cloud & Private DCs",
    "eu-cloud-germany": "Germany Sovereign Cloud & Private DCs",
    "eu-cloud-france": "France Sovereign Cloud & Private DCs",
    "eu-cloud-italy": "Italy Sovereign Cloud & Private DCs",
    "eu-cloud-benelux": "Netherlands & Benelux Cloud & DCs",
    "eu-cloud-switzerland-dach": "Switzerland & Austria (Alpine Sovereign)",
    "eu-cloud-nordics": "Nordics Green Cloud & AI Factories",
    "eu-cloud-uk": "United Kingdom Sovereign Cloud & DCs",
    "eu-cloud-iac-maturity": "IaC Automation & Maturity vs Hyperscalers",
    "eu-cloud-workloads-stack": "Hypervisors, IaaS, K8s & Sovereign AI",
    "eu-cloud-resilience-sla": "RPO, RTO, SLAs, DRP & Replication",
    "faq": "FAQ",
    "finops": "FinOps",
    "gitops": "GitOps",
    "hr": "HR",
    "iac": "IaC",
    "ibm_cloud": "IBM Cloud",
    "java_app_servers": "Java App Servers",
    "java_frameworks": "Java Frameworks",
    "java-and-java-performance-optimization": "Java Performance & JVM Tuning",
    "javascript": "JavaScript",
    "kubectl-commands": "kubectl Commands",
    "kubernetes-backup-migrations": "Kubernetes Backup & Migrations",
    "kubernetes-based-devel": "Kubernetes Local Dev",
    "kubernetes-bigdata": "Kubernetes Big Data",
    "kubernetes-operators-controllers": "Kubernetes Operators & Controllers",
    "linux-dev-env": "Linux Dev Environment",
    "lowcode-nocode": "Low-Code & No-Code",
    "managed-kubernetes-in-public-cloud": "Managed Kubernetes (Public Cloud)",
    "maven-gradle": "Maven & Gradle",
    "mkdocs": "MkDocs",
    "newsfeeds": "Newsfeeds",
    "noops": "NoOps",
    "nosql": "NoSQL",
    "ocp3": "OCP 3",
    "ocp4": "OCP 4",
    "ocp5": "OCP 5",
    "openshift": "OpenShift",
    "openshift-pipelines": "OpenShift Pipelines",
    "oraclecloud": "Oracle Cloud (OCI)",
    "performance-testing-with-jenkins-and-jmeter": "Performance Testing (Jenkins & JMeter)",
    "qa": "QA",
    "securityascode": "Security as Code",
    "servicemesh": "Service Mesh",
    "sonarqube": "SonarQube",
    "sre": "SRE",
    "swagger-code-generator-for-rest-apis": "Swagger / OpenAPI Codegen",
    "testops": "TestOps",
    "web3": "Web3",
    "workfromhome": "Work From Home",
    "yaml": "YAML",
}

BOILERPLATE_SUMMARY_MARKERS = (
    "technical documentation and implementation reference for",
    "technical documentation and architectural reference for",
    "technical documentation and reference for",
    "a curated technical resource and architectural guide covering",
    "curated technical resource in",
)


def is_boilerplate_summary(summary: str) -> bool:
    """Return True when an ai_summary is empty or matches a generic rule-based fallback."""
    if not summary or not isinstance(summary, str):
        return True
    low = summary.strip().lower()
    if len(low) < 25:
        return True
    return any(marker in low for marker in BOILERPLATE_SUMMARY_MARKERS)


# Helper to build readable category name
def get_readable_category(category: str) -> str:
    if not category:
        return "General"
    slug = category[:-3] if category.endswith(".md") else category
    if slug in DISPLAY_NAMES:
        return DISPLAY_NAMES[slug]
    title = slug.replace("_", " ").replace("-", " ").title()
    acronyms = {
        "Ai": "AI", "Mcp": "MCP", "Rag": "RAG", "Okf": "OKF", "Iac": "IaC",
        "Aws": "AWS", "Gcp": "GCP", "Api": "API", "Sre": "SRE", "Cicd": "CI/CD",
        "Ocp3": "OCP 3", "Ocp4": "OCP 4", "Ocp5": "OCP 5", "Jvm": "JVM",
        "Sql": "SQL", "Nosql": "NoSQL", "Chatgpt": "ChatGPT", "Mlops": "MLOps",
        "Devops": "DevOps", "Devsecops": "DevSecOps", "Gitops": "GitOps",
        "Finops": "FinOps", "Testops": "TestOps", "Noops": "NoOps",
        "Yaml": "YAML", "Faq": "FAQ", "Hr": "HR", "Qa": "QA", "Mkdocs": "MkDocs",
    }
    for k, v in acronyms.items():
        title = re.sub(rf"\b{k}\b", v, title)
    return title

async def fetch_github_metadata(client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore) -> tuple[str, dict]:
    default_meta = {
        "gh_stars": 0,
        "gh_pushed": None,  # date field: unknown = None, never the string "N/A"
        "gh_license": "N/A"
    }
    match = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if not match:
        return url, default_meta
    repo = match.group(1).split('#')[0].split('?')[0].rstrip('/')
    api_url = f"https://api.github.com/repos/{repo}"
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
        
    async with sem:
        try:
            resp = await client.get(api_url, headers=headers, timeout=10.0)
            if resp.status_code == 200:
                data = resp.json()
                lic = data.get("license")
                lic_id = lic.get("spdx_id", "N/A") if isinstance(lic, dict) else "N/A"
                return url, {
                    "gh_stars": data.get("stargazers_count", 0),
                    "gh_pushed": data.get("pushed_at"),
                    "gh_license": lic_id
                }
            elif resp.status_code == 404:
                return url, {
                    "gh_stars": 0,
                    "gh_pushed": None,
                    "gh_license": "N/A",
                    "status": "dead"
                }
            else:
                return url, {
                    "gh_stars": 0,
                    "gh_pushed": None,
                    "gh_license": "N/A",
                    "status": "unreachable"
                }
        except Exception as e:
            print(f"Error fetching metadata for {url}: {e}")
    return url, default_meta


from src.inventory_manager import load_inventory

async def run_enrichment():
    print("[*] Loading inventory database...")
    inventory = load_inventory()

    print(f"[*] Loaded {len(inventory)} total entries.")
    
    # 1. IDENTIFY GAPS
    v2_links = []
    github_missing = []
    unenriched = []
    
    for url, meta in inventory.items():
        if url.startswith("INTRO:"):
            continue
        
        # Check if candidate for V2 (meaning it has v2_locations)
        if meta.get("v2_locations"):
            v2_links.append(url)
            
            # Check if missing GitHub metadata
            if "github.com" in url:
                if meta.get("gh_stars") is None:
                    github_missing.append(url)
            
            # Check if unenriched (missing hierarchy or ai_summary)
            if not meta.get("hierarchy") or not meta.get("ai_summary"):
                unenriched.append(url)

    print(f"[*] Total V2 Candidates: {len(v2_links)}")
    print(f"[*] GitHub links missing metadata: {len(github_missing)}")
    print(f"[*] Candidates missing AI Enrichment: {len(unenriched)}")

    # 2. BATCH FETCH GITHUB METADATA (Concurrent)
    if github_missing:
        print(f"\n[*] Starting concurrent GitHub API metadata retrieval for {len(github_missing)} repos...")
        sem = asyncio.Semaphore(15)
        async with httpx.AsyncClient() as client:
            tasks = [fetch_github_metadata(client, url, sem) for url in github_missing]
            results = await asyncio.gather(*tasks)
            
            fetched_count = 0
            for url, gh_data in results:
                if gh_data:
                    norm = normalize_url(url)
                    if norm in inventory:
                        inventory[norm].update(gh_data)
                        fetched_count += 1
        print(f"[+] Successfully fetched metadata for {fetched_count} GitHub repositories.")

    # 3. LOCAL ENRICHMENT (Rule-based Fallback)
    print(f"\n[*] Applying local rule-based enrichment to {len(unenriched)} unenriched links...")
    enriched_count = 0
    for url in unenriched:
        meta = inventory.get(url)
        if not meta:
            continue
            
        category = meta.get("category")
        if not category:
            v1_locs = meta.get("v1_locations") or []
            v2_locs = meta.get("v2_locations") or []
            loc_str = (v1_locs[0] if v1_locs else (v2_locs[0] if v2_locs else ""))
            if loc_str:
                category = os.path.basename(loc_str).replace(".md", "")
            else:
                category = "kubernetes-tools"
            meta["category"] = category
        dim = get_dimension_for_category(category)
        readable_cat = get_readable_category(category)
        
        # 3.1. Build Hierarchy
        if not meta.get("hierarchy"):
            meta["hierarchy"] = [dim, readable_cat, "General Reference"]
            
        # 3.2. Build AI Summary
        if not meta.get("ai_summary"):
            desc = (meta.get("description") or "").strip()
            # If standard V1 description contains markdown links or is empty, build a clean text summary
            if desc and len(desc) > 15:
                # Remove markdown links text and use description
                clean_desc = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', desc)
                meta["ai_summary"] = clean_desc
            else:
                raw_title = (meta.get("title") or "").replace("==", "").strip()
                if not raw_title:
                    # Derive human-readable title from URL slug rather than bare domain
                    slug = url.rstrip("/").split("/")[-1].replace("-", " ").replace("_", " ").strip()
                    raw_title = slug.title() if len(slug) > 3 else url.split("//")[-1].split("/")[0]
                    meta["title"] = raw_title
                meta["ai_summary"] = f"Technical documentation and reference for {raw_title} in {readable_cat}."
                
        # 3.3. Populate other missing metadata fields to ensure compliance
        lang_val = meta.get("language")
        if not lang_val or str(lang_val).strip().lower() in ("none", "n/a", "null", "unknown"):
            meta["language"] = "English"
        yr_val = meta.get("year")
        if not yr_val or str(yr_val).strip().lower() in ("none", "null", "unknown"):
            meta["year"] = "N/A"
        if not meta.get("resource_type") or str(meta.get("resource_type")).lower() == "none":
            meta["resource_type"] = "Reference"
        if not meta.get("complexity") or str(meta.get("complexity")).lower() == "none":
            meta["complexity"] = "Intermediate"
        if not meta.get("tags"):
            meta["tags"] = ["[GUIDE]"] if any(d in url for d in ("learn.microsoft.com", "docs.", "kubernetes.io/docs")) else ["[COMMUNITY-TOOL]"]
            
        inventory[url] = meta
        enriched_count += 1
        
    print(f"[+] Successfully enriched {enriched_count} resources locally.")

    # 4. SAVE DATABASE
    print("\n[*] Saving updated inventory to disk...")
    from src.inventory_manager import save_inventory
    save_inventory(inventory)
    print("[+] Database saved successfully.")

if __name__ == "__main__":
    asyncio.run(run_enrichment())
