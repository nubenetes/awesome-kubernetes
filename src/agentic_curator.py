from pydantic import BaseModel, Field
from pydantic_ai import Agent
from typing import List, Optional
from src.config import NUBENETES_CATEGORIES

class LinkEvaluationResult(BaseModel):
    is_exceptional_value: bool = Field(description="¿Es un recurso avanzado o disruptivo para el ecosistema Kubernetes/SRE?")
    category_assignments: List[str] = Field(description="Lista de categorías donde encaja este recurso.", min_items=1)
    canonical_title: str = Field(description="Título formal y directo, omitiendo lenguaje de marketing.")
    technical_description: str = Field(description="Descripción técnica de máx 150 caracteres enfocada en la utilidad.")
    evaluation_rationale: str = Field(description="Razonamiento interno justificando la decisión de retener o purgar el enlace.")

# NOTA: En versiones recientes de pydantic-ai, result_type se pasa al ejecutar .run() 
# o se define en la configuración del agente según la versión. 
# Para máxima compatibilidad, lo definiremos aquí.

curation_agent = Agent(
    'google-gla:gemini-1.5-flash',
    system_prompt=(
        "Actúas como el Ingeniero Curador Principal de 'nubenetes/awesome-kubernetes'. "
        "Tu misión es filtrar recursos de altísima calidad sobre K8s, Agentes de IA, MCP y Cloud Native. "
        "Puedes asignar un recurso a MÁS DE UNA categoría si es estrictamente necesario, pero intenta ser preciso. "
        "Categorías válidas: " + ", ".join(NUBENETES_CATEGORIES)
    )
)

async def evaluate_extracted_assets(raw_assets: list[dict]) -> list[dict]:
    curated_assets = []
    for asset in raw_assets:
        cognitive_prompt = f"Evalúa este candidato:\nURL: {asset['url']}\nContexto: {asset['context']}"
        try:
            # Pasamos result_type aquí para evitar errores de inicialización
            response = await curation_agent.run(cognitive_prompt, result_type=LinkEvaluationResult)
            ev = response.data
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
            print(f"Error evaluando {asset['url']}: {str(e)}")
    return curated_assets
