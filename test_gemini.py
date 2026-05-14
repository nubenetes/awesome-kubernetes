import asyncio
from src.gemini_utils import call_gemini_with_retry

async def test():
    try:
        res = await call_gemini_with_retry("Hola, responde con la palabra 'OK' si recibes esto.")
        print(f"Resultado: {res}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
