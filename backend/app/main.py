import warnings
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import ingest, chat, health

# 1. Ignore the Pydantic/Python 3.14 compatibility warning
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# 2. Suppress "UNEXPECTED" and status logs from transformers/sentence-transformers
logging.getLogger("transformers").setLevel(logging.ERROR)

app = FastAPI(title="Website RAG Chatbot")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(ingest.router, prefix="/ingest", tags=["Ingest"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run already handles the "Started server process" INFO log
    uvicorn.run(app, host="0.0.0.0", port=8000)