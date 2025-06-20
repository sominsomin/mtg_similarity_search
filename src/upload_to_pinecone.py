from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from util import load_card_with_embeddings
from pinecone_util import upend_to_pinecone

data_file_path = "data/default-cards-20250616213306.json"
file_path_embeddings = "data/card_embeddings.npy"

PINECONE_API_KEY = st.secrets['PINECONE_API_KEY']
INDEX_NAME = st.secrets("INDEX_NAME")
REGION = st.secret("REGION")

if __name__ == "__main__":
    pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

    cards = load_card_with_embeddings(data_file_path, file_path_embeddings)
    embeddings_length = len(cards[0]["embedding"])
 
    print(pc.list_indexes())

    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=embeddings_length,
            metric="euclidean",
            spec=ServerlessSpec(
                cloud="aws",
                region=REGION
            )
        )

    index = pc.Index(INDEX_NAME)
    # index.delete(delete_all=True)

    upend_to_pinecone(cards, index)
