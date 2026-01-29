from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import the middleware
from app.api.routes import ingest, chat, health

app = FastAPI(title="Website RAG Chatbot")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (your local frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include routes
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(ingest.router, prefix="/ingest", tags=["Ingest"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)