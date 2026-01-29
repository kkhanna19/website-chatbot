import faiss
import pickle
import os

VECTOR_PATH = "data/vector_store/index.faiss"
META_PATH = "data/vector_store/meta.pkl"

def save_vector_store(vectors, texts):
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(vectors)

    faiss.write_index(index, VECTOR_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(texts, f)

def load_vector_store():
    index = faiss.read_index(VECTOR_PATH)
    with open(META_PATH, "rb") as f:
        texts = pickle.load(f)
    return index, texts
