from fastapi import FastAPI
from app.api.v1.chat import router as chat_router

app = FastAPI(title="Yojana Sahayak")

app.include_router(chat_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}
