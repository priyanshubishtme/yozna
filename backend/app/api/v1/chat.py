from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.llm.providers import GroqProvider, ChatRequest
import json
import asyncio

router = APIRouter()
groq_provider = GroqProvider()

async def mock_stream(query):
    yield "data: " + json.dumps({"token": "Thinking"}) + "\n\n"
    await asyncio.sleep(0.5)
    yield "data: " + json.dumps({"token": " about "}) + "\n\n"
    await asyncio.sleep(0.5)
    yield "data: " + json.dumps({"token": query}) + "\n\n"
    yield "data: [DONE]\n\n"

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # If key is dummy, use a mock stream for demonstration.
    if groq_provider.client.api_key == "dummy_key":
         return StreamingResponse(mock_stream(request.query), media_type="text/event-stream")

    # Real interaction when configured
    messages = [{"role": "user", "content": request.query}]
    try:
        response = await groq_provider.chat(messages, stream=True)

        async def stream_generator():
            async for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield f"data: {json.dumps({'token': chunk.choices[0].delta.content})}\n\n"
            yield "data: [DONE]\n\n"

        return StreamingResponse(stream_generator(), media_type="text/event-stream")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
