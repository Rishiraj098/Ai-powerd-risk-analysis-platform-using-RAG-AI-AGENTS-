from services.vector_store import add_vectors, search_vectors

def embed(text):
    # Dummy embedding (replace with real API later)
    return [0.01] * 384

def ingest_document(content):
    text = content.decode("utf-8", errors="ignore")
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    vectors = [embed(chunk) for chunk in chunks]
    add_vectors(vectors, chunks)

def process_query(question):
    query_vector = embed(question)
    context = search_vectors(query_vector)

    return {
        "risk_level": "Medium",
        "explanation": "Risk identified based on document context.",
        "reference": context[:1]
    }
