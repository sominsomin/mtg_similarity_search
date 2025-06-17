import requests
import json

def scrape_cards(query="type:creature", limit=1000):
    url = f"https://api.scryfall.com/cards/search?q={query}"
    cards = []

    while url and len(cards) < limit:
        resp = requests.get(url).json()
        cards.extend(resp["data"])
        url = resp.get("next_page", None)

    with open("data/cards.json", "w") as f:
        json.dump(cards, f)
    
    print(f"Saved {len(cards)} cards.")

if __name__ == "__main__":
    scrape_cards()
