import os
from openai import AsyncOpenAI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str
    language: str = "en"

class GroqProvider:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY", "dummy_key")
        base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
        self.model = os.getenv("GROQ_MODEL", "llama3-8b-8192")
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    async def chat(self, messages, stream=True):
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=stream,
                temperature=0.1,
            )
            return response
        except Exception as e:
            return str(e)
