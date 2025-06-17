from sentence_transformers import SentenceTransformer
import numpy as np
from src.util import load_cards

data_file_path = 'data/default-cards-20250616213306.json'
file_path_embeddings = 'data/card_embeddings.npy'

def embed_texts(cards):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [card["text"] for card in cards]
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

if __name__ == "__main__":
    cards = load_cards(data_file_path)

    embeddings = embed_texts(cards)
    np.save(file_path_embeddings, embeddings)
