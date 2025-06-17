import json
import numpy as np
from card_types import card_classes
from datetime import datetime

def load_cards(file_path):
    with open(file_path, encoding="utf-8") as f:
        cards = json.load(f)

    return [
        {
            "id": c["id"],
            "name": c["name"],
            "text": c.get("oracle_text", ""),
            "image": c.get("image_uris", {}).get("normal", ""),
            "color_identity": c["color_identity"],
            "legalities": [format for format, legality in c["legalities"].items() if legality == 'legal'],
            "mana_cost": c["mana_cost"],
            "rarity": c["rarity"],
            "type_line": [card_classes.get(t, t) for t in c["type_line"].split(" — ")],
            "keywords": c["keywords"],
            "released_at": int(datetime.strptime(c["released_at"], "%Y-%m-%d").timestamp()),
        }
        for c in cards if c.get("oracle_text") and c["lang"] == "en"
    ]

def load_card_with_embeddings(file_path_cards, file_path_embeddings):
    cards = load_cards(file_path_cards)
    embeddings = np.load(file_path_embeddings)

    cards_with_embeddings = [
        {**card, "embedding": embedding}
        for card, embedding in zip(cards, embeddings)
    ]

    return cards_with_embeddings

if __name__=="__main__":
    cards = load_cards("data/default-cards-20250616213306.json")

    import pdb
    pdb.set_trace()
