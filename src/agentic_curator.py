from pydantic import BaseModel, Field
from pydantic_ai import Agent
from typing import List, Optional
from src.config import NUBENETES_CATEGORIES

class LinkEvaluationResult(BaseModel):
    is_exceptional_value: bool = Field(description="¿Es un recurso avanzado o disruptivo?")
    category_assignment: Optional[str] = Field(description="Categoría asignada.", enum=NUBENETES_CATEGORIES)
    canonical_title: str = Field(description="Título formal.")
    technical_description: str = Field(description="Descripción técnica corta.")
    evaluation_rationale: str = Field(description="Razonamiento de la decisión.")

curation_agent = Agent(
    'google-gla:gemini-2.0-flash-exp',
    result_type=LinkEvaluationResult,
    system_prompt=(
        "Actúas como el Ingeniero Curador Principal para 'nubenetes/awesome-kubernetes'. "
        "Descarta tutoriales genéricos. Privilegia automatización, GitOps, Service Meshes y operadores. "
        "Usa una categoría existente. Redacta descripciones asépticas y técnicas."
    )
)

async def evaluate_extracted_assets(raw_assets: list[dict]) -> list[dict]:
    curated_assets = []
    for asset in raw_assets:
        cognitive_prompt = f"Evalúa este candidato:\nURL: {asset['url']}\nContexto: {asset['context']}"
        try:
            response = await curation_agent.run(cognitive_prompt)
            evaluation = response.data
            if evaluation.is_exceptional_value and evaluation.category_assignment:
                curated_assets.append({
                    "url": asset["url"],
                    "title": evaluation.canonical_title,
                    "description": evaluation.technical_description,
                    "category": evaluation.category_assignment
                })
        except Exception as e:
            print(f"Error evaluando {asset['url']}: {str(e)}")
    return curated_assets
