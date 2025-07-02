import faiss
import numpy as np

def build_faiss_index(embeddings):
    dim = len(embeddings[0])  # Usually 1536 for Azure OpenAI embeddings
    index = faiss.IndexFlatL2(dim)  # L2 = Euclidean distance

    # Convert to float32 numpy array
    embedding_array = np.array(embeddings).astype("float32")

    # Add embeddings to index
    index.add(embedding_array)

    return index



from embedder import get_embedding
import numpy as np

def search(query, index, chunks, top_k=3):
    query_embedding = get_embedding(query)
    D, I = index.search(np.array([query_embedding]).astype("float32"), top_k)

    results = [(chunks[i]["text"], chunks[i]["filename"]) for i in I[0]]
    return results

