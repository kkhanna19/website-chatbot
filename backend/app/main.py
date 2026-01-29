from fastapi import FastAPI
from app.api.routes import ingest, chat, health

app = FastAPI(title="Website RAG Chatbot")

app.include_router(health.router)
app.include_router(ingest.router, prefix="/ingest")
app.include_router(chat.router, prefix="/chat")
