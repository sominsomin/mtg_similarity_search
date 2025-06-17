import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.util import load_cards

def find_similar(query_text, top_k=5):
    cards = load_cards()
    embeddings = np.load("data/card_embeddings.npy")
    
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec = model.encode([query_text])

    sims = cosine_similarity(query_vec, embeddings)[0]
    top_indices = sims.argsort()[-top_k:][::-1]
    
    results = [(cards[i]["name"], cards[i]["text"], cards[i]["image"], round(sims[i], 3)) for i in top_indices]
    return results
