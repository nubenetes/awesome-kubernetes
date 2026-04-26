import json
import google.generativeai as genai
from pydantic import BaseModel, Field
from typing import List
from src.config import GEMINI_API_KEY, NUBENETES_CATEGORIES

class LinkEvaluationResult(BaseModel):
    is_exceptional_value: bool
    category_assignments: List[str]
    canonical_title: str
    technical_description: str
    evaluation_rationale: str

# Configuración del modelo
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def evaluate_extracted_assets(raw_assets: list[dict]) -> list[dict]:
    curated_assets = []
    
    system_instruction = (
        "Actúas como el Ingeniero Curador Principal de 'nubenetes/awesome-kubernetes'. "
        "Tu misión es filtrar recursos de altísima calidad sobre K8s, Agentes de IA, MCP y Cloud Native. "
        "Categorías válidas: " + ", ".join(NUBENETES_CATEGORIES) + ". "
        "Responde EXCLUSIVAMENTE en formato JSON siguiendo el esquema de LinkEvaluationResult."
    )

    for asset in raw_assets:
        prompt = (
            f"{system_instruction}\n\n"
            f"Evalúa este candidato:\nURL: {asset['url']}\nContexto: {asset['context']}\n"
            "Si el recurso no es de alta calidad o no encaja en las categorías, pon is_exceptional_value como false."
        )
        
        try:
            # Generación con restricción de formato (JSON)
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json"
                )
            )
            
            data = json.loads(response.text)
            # Validar con Pydantic para asegurar integridad
            ev = LinkEvaluationResult(**data)
            
            if ev.is_exceptional_value:
                for cat in ev.category_assignments:
                    if cat in NUBENETES_CATEGORIES:
                        curated_assets.append({
                            "url": asset["url"],
                            "title": ev.canonical_title,
                            "description": ev.technical_description,
                            "category": cat
                        })
        except Exception as e:
            print(f"[!] Error evaluando con Gemini: {e}")
            
    return curated_assets
