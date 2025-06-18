import wget

url = "https://data.scryfall.io/default-cards/default-cards-20250618091105.json"
wget.download(url, "default-cards/default-cards-20250618091105.json")