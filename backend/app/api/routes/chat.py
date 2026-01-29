from fastapi import APIRouter
from app.services.retriever import retrieve
from app.services.llm import generate_answer

router = APIRouter()

@router.post("/")
def chat(question: str):
    context_chunks = retrieve(question)
    context = "\n".join(context_chunks)
    answer = generate_answer(context, question)
    return {"answer": answer}
