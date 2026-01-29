from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.retriever import retrieve
from app.services.llm import generate_answer

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    context_chunks = retrieve(request.question)
    context = "\n".join(context_chunks)
    answer = generate_answer(context, request.question)
    return {"answer": answer}