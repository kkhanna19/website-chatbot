from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.retriever import retrieve
from app.services.llm import generate_answer
from app.core.memory import memory_manager

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    # 1. Get session and history
    session = memory_manager.get_session(request.session_id)
    chat_history = session.get_context()

    # 2. Retrieve chunks (traceability: retrieve now returns chunks)
    context_chunks = retrieve(request.question)
    context = "\n".join(context_chunks)

    # 3. Generate answer using history + current context
    answer = generate_answer(context, request.question, chat_history)

    # 4. Save to memory for next turn
    session.add(request.question, answer)

    return {
        "answer": answer,
        "sources": context_chunks[:2]  # Return first 2 chunks as sources
    }