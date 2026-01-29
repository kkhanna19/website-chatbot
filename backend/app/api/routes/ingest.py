from fastapi import APIRouter
from app.services.crawler import crawl_website
from app.services.chunker import chunk_text
from app.services.embeddings import embed_texts
from app.services.vectorstore import save_vector_store

router = APIRouter()

@router.post("/")
def ingest(url: str):
    text = crawl_website(url)
    chunks = chunk_text(text)
    vectors = embed_texts(chunks)
    save_vector_store(vectors, chunks)
    return {"status": "indexed", "chunks": len(chunks)}
