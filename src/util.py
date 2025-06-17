import json
import numpy as np

def load_cards(file_path):
    with open(file_path, encoding='utf-8') as f:
        cards = json.load(f)

    return [
        {
            "id": c["id"],
            "name": c["name"],
            "text": c.get("oracle_text", ""),
            "image": c.get("image_uris", {}).get("normal", "")
        }
        for c in cards if c.get("oracle_text")
    ]

def load_card_with_embeddings(file_path_cards, file_path_embeddings):
    cards = load_cards(file_path_cards)
    embeddings = np.load(file_path_embeddings)

    cards_with_embeddings = [
        {**card, "embedding": embedding}
        for card, embedding in zip(cards, embeddings)
    ]

    return cards_with_embeddings
