from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=300
)

def generate_answer(context, question):
    prompt = f"""
Answer ONLY from the context below.
If not found, say:
"The answer is not available on the provided website."

Context:
{context}

Question:
{question}
"""
    result = generator(prompt)[0]["generated_text"]
    return result
