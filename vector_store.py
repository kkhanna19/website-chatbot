from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

DB_DIR = "chroma_db"


def create_vector_db(documents):
    """
    Create embeddings using OpenAI and store in ChromaDB.
    """

    embedding_model = OpenAIEmbeddings()

    texts = [doc["content"] for doc in documents]
    metadatas = [doc["metadata"] for doc in documents]

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embedding_model,
        persist_directory=DB_DIR,
        metadatas=metadatas
    )

    vectordb.persist()
    return vectordb
