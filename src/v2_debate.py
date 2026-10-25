import asyncio
from datetime import datetime
import json
import os
import re
from typing import Dict, List, Tuple
from src.gemini_utils import call_gemini_with_retry, normalize_url
from src.logger import log_event
from src.mandate_ingestor import get_system_mandates

# Memory file to store resolved debates
DEBATE_MEMORY_FILE = "src/memory/health_learning.json"

async def run_debate_protocol(item: Dict, is_new_link: bool = False) -> Tuple[int, List[str], str, Dict]:
    """
    Executes a Multi-Agent Consensus & Debate Protocol for borderline resources.
    The panel of experts consists of:
    1. Security Architect (Vulnerabilities, Licensing, Supply-Chain)
    2. Cloud Native SRE (Production readiness, Scalability, Community activity)
    3. AI Platform Engineer (Developer experience, Agentic integrations)
    
    Returns:
        final_score: Resolved impact score (0-100)
        verified_tags: Consensus tags
        refined_summary: Refined high-density technical summary
        debate_data: Logs and details of the debate
    """
    url = item.get("url", "")
    title = item.get("title", "Unknown Resource")
    desc = item.get("description", item.get("ai_summary", ""))
    tags = item.get("tags", [])
    initial_score = item.get("impact_score", item.get("stars", 3) * 20) # Fallback mapping if stars is used
    
    # 0. Check cache using content hash (Recommendation #4)
    import hashlib
    raw_content = f"{title}||{desc}||{','.join(sorted(tags))}"
    content_hash = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
    
    if os.path.exists(DEBATE_MEMORY_FILE):
        try:
            with open(DEBATE_MEMORY_FILE, "r") as f:
                memory_data = json.load(f)
            cached = memory_data.get("resolved_debates", {}).get(normalize_url(url))
            if cached and cached.get("content_hash") == content_hash:
                log_event(f"    [⚖️] CACHE HIT: Skipping debate for '{title}'. Returning cached consensus.")
                return (
                    cached["final_consensus_score"],
                    cached.get("final_tags", tags),
                    cached.get("refined_summary", desc),
                    cached
                )
        except Exception as e:
            log_event(f"    [!] Error checking debate cache: {e}")

    log_event(f"  [⚖️] DEBATE TRIGGERED: '{title}' (Initial Score: {initial_score})", section_break=False)
    
    # 0. Check if mock mode is requested or required (no keys configured)
    from src.config import GEMINI_API_KEYS
    mock_enabled = os.environ.get("MOCK_DEBATE") == "true" or not GEMINI_API_KEYS
    
    if mock_enabled:
        log_event(f"    [⚖️] Bypassing Gemini API: Running Offline Mock Debate Simulator...")
        text_to_scan = (title + " " + desc + " " + " ".join(tags)).lower()
        
        # Security Architect
        if any(x in text_to_scan for x in ["secure", "hardened", "cryptography", "sign", "compliance", "license", "oauth", "token", "vault", "identity", "keycloak", "sops"]):
            sa_score = 90
            sa_just = "Strong security architecture, automated credential isolation, and supply-chain guarantees."
        else:
            sa_score = 70
            sa_just = "Standard security compliance with typical permission profiles; no specific zero-trust hardening."
            
        # Cloud Native SRE
        if any(x in text_to_scan for x in ["production", "scalable", "monitoring", "prometheus", "ha", "reliability", "redundant", "kubernetes", "operator", "helm", "flux", "argo", "k3s", "draino", "ebpf", "cilium", "opentelemetry", "crd", "gateway-api"]):
            sre_score = 92
            sre_just = "Excellent operational metrics, Kubernetes-native CRD/Operator lifecycle, and proven Day-2 recovery behavior."
        else:
            sre_score = 65
            sre_just = "Acceptable single-instance footprint, but lacks comprehensive scaling runbooks and observability probes."
            
        # AI Platform Engineer
        if any(x in text_to_scan for x in ["agent", "mcp", "llm", "ai", "intelligence", "model", "prompt", "backstage", "developer", "gpu", "vllm", "inference", "kuberay", "kueue", "volcano", "dra", "rag", "mlops"]):
            ai_score = 94
            ai_just = "Highly relevant for 2026 Cloud-Native AI architectures, supporting GPU/DRA scheduling, LLM inference serving, or MCP agentic orchestration."
        else:
            ai_score = 60
            ai_just = "Conventional software engineering resource with minimal alignment to agentic orchestration or AI workload patterns."
            
        scores = {
            "Security Architect": sa_score,
            "Cloud Native SRE": sre_score,
            "AI Platform Engineer": ai_score
        }
        justifications = {
            "Security Architect": sa_just,
            "Cloud Native SRE": sre_just,
            "AI Platform Engineer": ai_just
        }
        
        for name, score in scores.items():
            log_event(f"    [>] {name} rated: {score} (Justification: {justifications[name]})")
            
        max_score = max(scores.values())
        min_score = min(scores.values())
        divergence = max_score - min_score
        debate_transcript = []
        
        if divergence >= 15:
            log_event(f"    [⚖️] Divergence detected ({divergence} points). Starting Mock Debate Round...")
            scores["Security Architect"] = int((sa_score + 78) / 2)
            scores["Cloud Native SRE"] = int((sre_score + 80) / 2)
            scores["AI Platform Engineer"] = int((ai_score + 82) / 2)
            
            rebuttals = {
                "Security Architect": "We must prioritize baseline compliance and permission boundaries even if the developer tool yields high platform speed.",
                "Cloud Native SRE": "Agreed, but the active community checkins and robust recovery hooks significantly offset the operational risk.",
                "AI Platform Engineer": "Platform agility is paramount; wrapping this tool in an MCP server exposes its schema for cognitive agent orchestration."
            }
            for name, score in scores.items():
                debate_transcript.append(f"{name} (Score {score}): {rebuttals[name]}")
                log_event(f"    [>] {name} revised rating to {score}. Rebuttal: {rebuttals[name]}")
                
        final_score = int(sum(scores.values()) / len(scores))
        log_event(f"    [🏁] Consensus Score reached: {final_score}")
        
        refined_summary = desc + " — Consensus Audit: The panel aligned on its enterprise maturity, noting its role in streamlining cloud native operations."
        
        final_tags = set(tags)
        if final_score >= 85:
            final_tags.add("[DE FACTO STANDARD]")
            if "[COMMUNITY-TOOL]" in final_tags: final_tags.remove("[COMMUNITY-TOOL]")
        elif final_score >= 70:
            final_tags.add("[ENTERPRISE-STABLE]")
            if "[COMMUNITY-TOOL]" in final_tags: final_tags.remove("[COMMUNITY-TOOL]")
        else:
            final_tags.add("[COMMUNITY-TOOL]")
            
        if "ebpf" in text_to_scan: final_tags.add("[EBPF]")
        if "wasm" in text_to_scan: final_tags.add("[WASM]")
        if "gitops" in text_to_scan: final_tags.add("[GITOPS]")
        if "iac" in text_to_scan: final_tags.add("[IAC]")
        if "mcp" in text_to_scan: final_tags.add("[MCP]")
        if any(x in text_to_scan for x in ["gpu", "cuda", "dra", "nvidia", "mig"]): final_tags.add("[GPU]")
        if any(x in text_to_scan for x in ["llm", "vllm", "inference", "tgi", "rag"]): final_tags.add("[LLM]")
        if any(x in text_to_scan for x in ["mlops", "kubeflow", "kuberay", "kueue", "volcano"]): final_tags.add("[MLOPS]")
        if any(x in text_to_scan for x in ["agent", "mcp", "ai", "llm"]): final_tags.add("[AI]")
        
        debate_data = {
            "url": url,
            "title": title,
            "initial_score": initial_score,
            "final_consensus_score": final_score,
            "scores": scores,
            "justifications": justifications,
            "rebuttals": debate_transcript,
            "timestamp": datetime.now().isoformat(),
            "final_tags": sorted(list(final_tags)),
            "refined_summary": refined_summary,
            "content_hash": content_hash
        }
        
        try:
            memory_data = {}
            if os.path.exists(DEBATE_MEMORY_FILE):
                try:
                    memory_data = json.load(open(DEBATE_MEMORY_FILE, "r"))
                except Exception as e:
                    log_event(f"[WARN] load debate memory for mock persist: {str(e)[:100]}")
            memory_data.setdefault("resolved_debates", {})[normalize_url(url)] = debate_data
            with open(DEBATE_MEMORY_FILE, "w") as f:
                json.dump(memory_data, f, indent=2)
        except Exception as e:
            log_event(f"    [!] Failed to persist debate memory: {e}")

        return final_score, sorted(list(final_tags)), refined_summary, debate_data

    system_mandates = get_system_mandates()
    
    # Fast-Pass Evaluator call (Recommendation #3)
    fast_pass_prompt = (
        "You are the Nubenetes Fast-Pass Evaluator (2026).\n"
        f"Analyze the following resource details:\n"
        f"- Title: {title}\n"
        f"- URL: {url}\n"
        f"- Context: {desc}\n"
        f"- Proposed Tags: {tags}\n\n"
        f"{system_mandates}\n\n"
        "Evaluate this resource across three dimensions:\n"
        "1. Security & License Integrity (permissive OSS vs BSL/SSPL, supply chain security)\n"
        "2. Cloud-Native SRE & K8s Integration (CRDs/Operators, Helm, OpenTelemetry, Gateway API, Day-2 HA)\n"
        "3. 2026 AI Platform & Agentic Readiness (GPU/DRA scheduling, LLM inference serving, MCP server integration, developer velocity)\n"
        "Assign a composite score (0 to 100), generate a high-density O'Reilly-style technical summary (2-5 sentences covering Architectural Role, Production Trade-offs, and K8s Compatibility), and select appropriate tags.\n"
        "Respond ONLY in valid JSON format: {\"score\": int, \"justification\": \"string\", \"summary\": \"string\", \"tags\": [\"string\"]}"
    )
    
    fast_pass_score = int(initial_score)
    fast_pass_justification = "Failed to run fast-pass."
    fast_pass_summary = desc
    fast_pass_tags = tags
    
    try:
        res = await call_gemini_with_retry(fast_pass_prompt, prefer_flash=True, use_grounding=True, role="FastPass-Evaluator")
        fast_pass_score = min(max(int(res.get("score", 50)), 0), 100)
        fast_pass_justification = res.get("justification", "No justification provided.")
        fast_pass_summary = res.get("summary", desc)
        fast_pass_tags = res.get("tags", tags)
        log_event(f"    [🔍] Fast-Pass Evaluator rated score: {fast_pass_score}")
    except Exception as e:
        log_event(f"    [!] Fast-Pass Evaluator failed: {e}")
        
    # Check if the score falls outside the borderline uncertainty margin [60, 75]
    if fast_pass_score >= 76 or fast_pass_score <= 59:
        log_event(f"    [⚡] Fast-Pass Consensus reached ({fast_pass_score}). Skipping full debate panel!")
        
        debate_data = {
            "url": url,
            "title": title,
            "initial_score": initial_score,
            "final_consensus_score": fast_pass_score,
            "fast_pass": True,
            "justification": fast_pass_justification,
            "timestamp": datetime.now().isoformat(),
            "final_tags": fast_pass_tags,
            "refined_summary": fast_pass_summary,
            "content_hash": content_hash
        }
        
        try:
            memory_data = {}
            if os.path.exists(DEBATE_MEMORY_FILE):
                try:
                    memory_data = json.load(open(DEBATE_MEMORY_FILE, "r"))
                except Exception as e:
                    log_event(f"[WARN] load debate memory for fast-pass persist: {str(e)[:100]}")
            memory_data.setdefault("resolved_debates", {})[normalize_url(url)] = debate_data
            with open(DEBATE_MEMORY_FILE, "w") as f:
                json.dump(memory_data, f, indent=2)
        except Exception as e:
            log_event(f"    [!] Failed to persist debate memory: {e}")

        return fast_pass_score, fast_pass_tags, fast_pass_summary, debate_data
        
    log_event(f"    [⚖️] Borderline score detected ({fast_pass_score}). Escalating to full Multi-Agent Debate Panel...")

    # 1. Independent Evaluation Round
    personas = {
        "Security Architect": "Focus on licensing (MIT/Apache 2.0 vs BSL/SSPL), OpenSSF supply chain security, zero-trust RBAC, vulnerabilities, and enterprise compliance.",
        "Cloud Native SRE": "Focus on Kubernetes-native integration (CRDs, Operators, Helm, Gateway API), Day-2 observability (OpenTelemetry, eBPF), high-availability, and commit velocity.",
        "AI Platform Engineer": "Focus on 2026 Cloud-Native AI infrastructure (GPU/DRA scheduling, vLLM/KServe inference, KubeRay/Kueue batch orchestration), Model Context Protocol (MCP) exposure, and developer velocity."
    }
    
    scores = {}
    justifications = {}
    
    async def evaluate_persona(name: str, focus: str) -> Tuple[int, str]:
        prompt = (
            f"You are the Nubenetes {name}.\n"
            f"Your perspective: {focus}\n\n"
            f"{system_mandates}\n\n"
            f"Evaluate the following resource:\n"
            f"- Title: {title}\n"
            f"- URL: {url}\n"
            f"- Context: {desc}\n"
            f"- Proposed Tags: {tags}\n\n"
            "Assign an architectural impact score (0 to 100) and write a 1-2 sentence technical justification.\n"
            "Respond ONLY in valid JSON format: {\"score\": int, \"justification\": \"string\"}"
        )
        try:
            res = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role=f"Debater-{name.replace(' ', '')}")
            score = min(max(int(res.get("score", 50)), 0), 100)
            justification = res.get("justification", "No justification provided.")
            return score, justification
        except Exception as e:
            log_event(f"    [!] Persona {name} evaluation failed: {e}")
            return int(initial_score), "Failed to evaluate."

    # Run evaluations in parallel
    eval_tasks = [evaluate_persona(name, focus) for name, focus in personas.items()]
    eval_results = await asyncio.gather(*eval_tasks)
    
    for idx, (name, _) in enumerate(personas.items()):
        scores[name], justifications[name] = eval_results[idx]
        log_event(f"    [>] {name} rated: {scores[name]} (Justification: {justifications[name]})")
        
    # Check divergence: if max diff >= 15 points, run a debate round
    max_score = max(scores.values())
    min_score = min(scores.values())
    divergence = max_score - min_score
    
    debate_transcript = []
    
    if divergence >= 15:
        log_event(f"    [⚖️] Divergence detected ({divergence} points). Starting Debate Round...")
        
        async def run_rebuttal(name: str, focus: str) -> Tuple[int, str]:
            opponent_views = "\n".join([f"- {other}: Score {scores[other]} | Justification: {justifications[other]}" for other in personas if other != name])
            prompt = (
                f"You are the Nubenetes {name}.\n"
                f"Your perspective: {focus}\n\n"
                "The panel of experts disagrees on this resource. Here are the other views:\n"
                f"{opponent_views}\n\n"
                f"Resource details:\n"
                f"- Title: {title}\n"
                f"- URL: {url}\n"
                f"- Context: {desc}\n\n"
                "Reconsider your evaluation. You can either defend your initial score or adjust it.\n"
                "Respond ONLY in valid JSON format: {\"score\": int, \"rebuttal\": \"1-2 sentence response to other experts\"}"
            )
            try:
                res = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role=f"Debate-Rebuttal-{name.replace(' ', '')}")
                new_score = min(max(int(res.get("score", scores[name])), 0), 100)
                rebuttal = res.get("rebuttal", "No rebuttal provided.")
                return new_score, rebuttal
            except Exception as e:
                log_event(f"    [!] Persona {name} rebuttal failed: {e}")
                return scores[name], "No rebuttal provided."
        
        rebuttal_tasks = [run_rebuttal(name, focus) for name, focus in personas.items()]
        rebuttal_results = await asyncio.gather(*rebuttal_tasks)
        
        for idx, (name, _) in enumerate(personas.items()):
            scores[name], rebuttal = rebuttal_results[idx]
            debate_transcript.append(f"{name} (Score {scores[name]}): {rebuttal}")
            log_event(f"    [>] {name} revised rating to {scores[name]}. Rebuttal: {rebuttal}")
            
    # Compute Final Consensus
    final_score = int(sum(scores.values()) / len(scores))
    log_event(f"    [🏁] Consensus Score reached: {final_score}")
    
    # 2. Refined Curation/Tags Round
    refine_prompt = (
        "You are the Nubenetes Curation Synthesis Agent (2026).\n"
        f"Combine the following multi-agent expert reviews into a final technical decision.\n\n"
        f"Resource Title: {title}\n"
        f"URL: {url}\n"
        f"Consensus Score: {final_score}\n"
        f"Security Architect Score: {scores['Security Architect']} | Justification: {justifications['Security Architect']}\n"
        f"Cloud Native SRE Score: {scores['Cloud Native SRE']} | Justification: {justifications['Cloud Native SRE']}\n"
        f"AI Platform Engineer Score: {scores['AI Platform Engineer']} | Justification: {justifications['AI Platform Engineer']}\n\n"
        "Generate a final, high-density, professional technical summary (2-5 sentences, O'Reilly style covering Architectural Role, Production Trade-offs/Alternatives, and Kubernetes Compatibility).\n"
        "Select the appropriate subset of tags. You MUST include:\n"
        "1. Standard maturity tags from: [DE FACTO STANDARD], [ENTERPRISE-STABLE], [EMERGING], [GUIDE], [CASE STUDY], [COMMUNITY-TOOL], [LEGACY].\n"
        "2. Any relevant fine-grained technology stack tags from the content (e.g., [EBPF], [WASM], [GITOPS], [IAC], [SERVICE-MESH], [SERVERLESS], [MLOPS], [GPU], [LLM], [MCP], [AI], [DB]). Keep them uppercase and wrapped in brackets.\n"
        "Respond ONLY in valid JSON format: {\"summary\": \"refined summary...\", \"tags\": [\"...\"]}"
    )
    
    refined_summary = desc
    final_tags = tags
    try:
        res = await call_gemini_with_retry(refine_prompt, prefer_flash=False, use_grounding=False, role="Debate-Synthesis")
        refined_summary = res.get("summary", desc)
        final_tags = res.get("tags", tags)
    except Exception as e:
        log_event(f"    [!] Error during debate synthesis: {e}")
        
    debate_data = {
        "url": url,
        "title": title,
        "initial_score": initial_score,
        "final_consensus_score": final_score,
        "scores": scores,
        "justifications": justifications,
        "rebuttals": debate_transcript,
        "timestamp": datetime.now().isoformat(),
        "final_tags": final_tags,
        "refined_summary": refined_summary,
        "content_hash": content_hash
    }
    
    # Persist the resolved debate to memory log (Mandate 3.1)
    try:
        memory_data = {}
        if os.path.exists(DEBATE_MEMORY_FILE):
            try:
                memory_data = json.load(open(DEBATE_MEMORY_FILE, "r"))
            except Exception as e:
                log_event(f"[WARN] load debate memory for final persist: {str(e)[:100]}")

        memory_data.setdefault("resolved_debates", {})[normalize_url(url)] = debate_data

        # Keep blacklist and other fields intact
        with open(DEBATE_MEMORY_FILE, "w") as f:
            json.dump(memory_data, f, indent=2)
    except Exception as e:
        log_event(f"    [!] Failed to persist debate memory: {e}")
        
    return final_score, final_tags, refined_summary, debate_data
