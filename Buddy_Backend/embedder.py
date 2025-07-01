# utils/embedder.py

from sentence_transformers import SentenceTransformer

# Load embedding model (BGE, MiniLM, etc. — smaller = faster)
model = SentenceTransformer("all-MiniLM-L6-v2")  # 384 dimensions

def get_embedding(text):
    embedding = model.encode(text)
    return embedding.tolist()  # return as list (like OpenAI does)



