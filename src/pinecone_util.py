import os
from dotenv import load_dotenv
from itertools import islice
from pinecone import Pinecone

def init_pinecone(api_key: str, index_name: str):
    pc = Pinecone(
        api_key=api_key
    )
    return pc.Index(index_name)

def query_pinecone(embedding: list, top_k=5, filter=None):
    load_dotenv()
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("INDEX_NAME")
    index = init_pinecone(api_key, index_name)

    query_filter = {
        "$and": [
            {key: {"$in": values}} for key, values in filter.items() if values
        ]
    }

    query_response = index.query(
        vector=embedding.astype("float32").tolist(),
        top_k=top_k, 
        include_metadata=True,
        filter=query_filter
        )

    matches = query_response["matches"]

    results = []
    for match in matches:
        results.append({
            "id": match["id"],
            "score": match["score"],
            "metadata": match.get("metadata", {}),
            "image": match.get("metadata", {}).get("image", ""),
        })

    return results

def chunked(iterable, size):
    it = iter(iterable)
    while chunk := list(islice(it, size)):
        yield chunk

def upend_to_pinecone(cards, index):
    to_upsert = [
        (
            card["id"],
            card["embedding"],
            {k: v for k, v in card.items() if k not in {"id", "embedding"}}
        )
        for card in cards
    ]

    for batch in chunked(to_upsert, 100):
        index.upsert(batch)

if __name__=="__main__":
    from create_embeddings import embed_query

    query = "card"
    embedded_query = embed_query(query)

    result = query_pinecone(embedded_query, filter={"name": ["Phyrexian Arena"]})
    print(result)
