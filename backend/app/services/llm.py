from transformers import pipeline
from app.core.config import HF_API_TOKEN
from app.core.prompt import SYSTEM_PROMPT

generator = pipeline(
    task="text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_API_TOKEN,
    max_new_tokens=300,
    temperature=0.2,
    do_sample=False
)

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}
"""
    response = generator(prompt)[0]["generated_text"]
    return response
