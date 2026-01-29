import numpy as np
from app.services.embeddings import embed_texts
from app.services.vectorstore import load_vector_store

def retrieve(query, k=3):
    index, texts = load_vector_store()
    query_vec = embed_texts([query])
    _, idxs = index.search(query_vec, k)
    return [texts[i] for i in idxs[0]]
