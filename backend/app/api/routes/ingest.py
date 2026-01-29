from fastapi import APIRouter
from app.schemas.ingest import IngestRequest, IngestResponse
from app.services.crawler import crawl_website
from app.services.chunker import chunk_text
from app.services.embeddings import embed_texts
from app.services.vectorstore import save_vector_store

router = APIRouter()

@router.post("/", response_model=IngestResponse)
def ingest(request: IngestRequest):
    # Use the validated URL from the request body
    text = crawl_website(str(request.url))
    chunks = chunk_text(text)
    vectors = embed_texts(chunks)
    save_vector_store(vectors, chunks)
    return {"status": "indexed", "chunks": len(chunks)}