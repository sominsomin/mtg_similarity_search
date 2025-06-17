from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec
from util import load_card_with_embeddings

data_file_path = 'data/default-cards-20250616213306.json'
file_path_embeddings = 'data/card_embeddings.npy'

load_dotenv()
api_key = os.getenv("pinecone_api_key")
index_name = "mtg-similarity-search"

pc = Pinecone(
    api_key=api_key
)

# if index_name not in pc.list_indexes().names():
#     pc.create_index(
#         name=index_name,
#         dimension=1536,
#         metric='euclidean',
#         spec=ServerlessSpec(
#             cloud='aws',
#             region='us-west-2'
#         )
#     )

cards = load_card_with_embeddings(data_file_path, file_path_embeddings)

# vectors = [
#     ("vec1", [0.1, 0.2, 0.3]),
#     ("vec2", [0.4, 0.5, 0.6]),
# ]

# index.upsert(vectors)

# query_result = index.query([0.1, 0.2, 0.3], top_k=1)
# print(query_result)