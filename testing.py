import os
os.environ["OPENAI_API_KEY"] = "sk-XXXXXXXXXXXXXXXXXXXXXXXX"

from vector_store import create_vector_db

docs = [{'content':'hello world','metadata':{'source':'test','title':'t'}}]
db = create_vector_db(docs)
print("Vector DB Working")
