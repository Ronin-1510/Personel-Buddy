# main.py (Backend with API + Console RAG)
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from loader import load_and_chunk_documents
from embedder import get_embedding
from vector_store import build_faiss_index, search
from answer_generation import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

chunks = load_and_chunk_documents("Documents")
print(f"✅ Loaded {len(chunks)} chunks")

embeddings = []
for chunk in chunks:
    text = chunk["text_content"]
    vector = get_embedding(text)
    if vector:
        embeddings.append(vector)
print(f"✅ Collected {len(embeddings)} embeddings")

if not embeddings:
    print("❌ No embeddings found. Something went wrong.")
    faiss_index = None
else:
    faiss_index = build_faiss_index(embeddings)
    print("✅ FAISS index built.")

chunk_metadata = [
    {"text": chunk["text_content"], "filename": chunk["filename"]}
    for chunk in chunks
]

@app.post("/ask")
def ask(query: Query):
    top_chunks = search(query.question, faiss_index, chunk_metadata, top_k=3)
    context = [text for text, _ in top_chunks]
    answer = generate_answer(context, query.question)
    return {"answer": answer, "chunks": top_chunks}





# # Save to readable .txt file
# with open("my_embeddings.txt", "w", encoding="utf-8") as file:
#     for i, item in enumerate(embeddings, 1):
#         file.write(f"Chunk {i} from {item['filename']}:\n")
#         file.write(f"Text: {item['text']}...\n")  # limit preview
#         file.write(f"Embedding: {item['embedding']}...\n\n")  # preview first 10 numbers






