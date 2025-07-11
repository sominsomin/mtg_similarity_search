# About

This project enables semantic search for Magic: The Gathering cards using sentence embeddings and a vector database. With this tool, you can search for cards based on natural language queries (e.g., "draw a card", "gain life") and apply filters such as:
    - Color
    - Card type (Creature, Artifact, etc.)
    - Format (Standard, Modern, etc.)

A user-friendly interface is provided through a Streamlit app.
    - [Live App](https://sominsomin-mtg-similarity-search-srcstreamlit-app-g87txa.streamlit.app/)

![Screenshot](images/screenshot2.png)

# Process

Card texts are embedded using a SentenceTransformer from huggingface. They are then uploaded to pinecone, to host the vectordatabase. This requires a pinecone account.
Search results can be accessed via a streamlit app, either running locally or deploying online.

For running it locally, you need to create a .streamlit/secrets.toml file in the project root with the following values:

````
[secrets]
PINECONE_API_KEY=your_pinecone_api_key
INDEX_NAME=your_index_name
REGION=your_pinecone_region
````

## Installation

`pip install -r requirements.txt`

## Download current Data from Scryfall

Either do this for a current file:
````
python data/get_data.py
````
Or do it manually by going to [Scryfall Bulk Data](https://scryfall.com/docs/api/bulk-data)

## Create Embeddings

Create the embeddings:
````
python src/create_embeddings.py
````
This will create a file in data/card_embeddings.npy

## Upload to pinecone

````
python src/upload_to_pinecone.py
````
Uploads embeddings to pinecone.

# Streamlit

Run streamlit app:
````
streamlit run src/streamlit_app.py
````