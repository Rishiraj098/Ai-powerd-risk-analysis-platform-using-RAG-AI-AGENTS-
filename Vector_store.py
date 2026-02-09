import faiss
import numpy as np

index = faiss.IndexFlatL2(384)
documents = []

def add_vectors(vectors, texts):
    index.add(np.array(vectors).astype("float32"))
    documents.extend(texts)

def search_vectors(vector, k=3):
    _, idx = index.search(np.array([vector]).astype("float32"), k)
    return [documents[i] for i in idx[0]]
