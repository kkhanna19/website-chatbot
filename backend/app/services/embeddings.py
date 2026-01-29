# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def embed_texts(texts):
#     return model.encode(texts, show_progress_bar=True)


from sentence_transformers import SentenceTransformer

# Change from all-MiniLM-L6-v2 to a lighter version
model = SentenceTransformer("paraphrase-MiniLM-L3-v2") 

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=True)