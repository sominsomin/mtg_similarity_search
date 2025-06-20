# About

This project enables semantic search for Magic: The Gathering cards using sentence embeddings and a vector database. With this tool, you can search for cards based on natural language queries (e.g., "draw a card", "gain life") and apply filters such as:
    - Color
    - Card type (Creature, Artifact, etc.)
    - Format (Standard, Modern, etc.)

A user-friendly interface is provided through a Streamlit app.
    - Live App: [Insert link here]

# Process

Card texts are embedded using a SentenceTransformer from huggingface. They are then uploaded to pinecone, to host the vectordatabase. This requires a pinecone account.
Search results can be accessed via a streamlit app, either running locally or deploying online.

Create a .env file in the project root with the following values:

PINECONE_API_KEY=your_pinecone_api_key
INDEX_NAME=your_index_name
REGION=your_pinecone_region

# Installation

pip install -r requirements.txt

# Streamlit

streamlit run src/streamlit_app.py