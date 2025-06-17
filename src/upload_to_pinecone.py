from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec
from util import load_card_with_embeddings
from pinecone_util import upend_to_pinecone

data_file_path = "data/default-cards-20250616213306.json"
file_path_embeddings = "data/card_embeddings.npy"

load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("INDEX_NAME")
region_name = os.getenv("REGION")

if __name__ == "__main__":
    pc = Pinecone(
        api_key=api_key
    )

    cards = load_card_with_embeddings(data_file_path, file_path_embeddings)
    embeddings_length = len(cards[0]["embedding"])
 
    print(pc.list_indexes())

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=embeddings_length,
            metric="euclidean",
            spec=ServerlessSpec(
                cloud="aws",
                region=region_name
            )
        )

    index = pc.Index(index_name)
    # index.delete(delete_all=True)

    upend_to_pinecone(cards[0:1000], index)
