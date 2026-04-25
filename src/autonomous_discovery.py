from pydantic_ai import Agent
from pydantic import BaseModel, Field
import aiohttp
from src.config import NUBENETES_CATEGORIES

class DiscoveredResource(BaseModel):
    title: str
    url: str
    description: str
    category: str = Field(enum=NUBENETES_CATEGORIES)

class DiscoveryReport(BaseModel):
    new_high_value_resources: list[DiscoveredResource]

async def fetch_github_trending_k8s() -> str:
    url = "https://api.github.com/search/repositories?q=topic:kubernetes+stars:>500&sort=stars&order=desc"
    async with aiohttp.ClientSession() as session:
         async with session.get(url) as resp:
             if resp.status == 200:
                 data = await resp.json()
                 summaries = [f"{repo['name']} - {repo['html_url']} - {repo['description']}" for repo in data.get('items', [])[:10]]
                 return "\n".join(summaries)
             return "No se pudieron obtener resultados."

explorer_agent = Agent(
    'google-gla:gemini-2.0-flash-exp',
    result_type=DiscoveryReport,
    system_prompt=(
        "Descubre las 3 herramientas de Kubernetes más populares y recientes. "
        "Usa la herramienta 'fetch_github_trending_k8s'. "
        "Solo herramientas revolucionarias, categorizadas estrictamente."
    )
)
explorer_agent.tool(fetch_github_trending_k8s)

async def discover_trending_assets() -> list[dict]:
    try:
        response = await explorer_agent.run("Busca herramientas revolucionarias en el ecosistema.")
        return [dict(res) for res in response.data.new_high_value_resources]
    except Exception as e:
        print(f"Error en descubrimiento: {str(e)}")
        return []
