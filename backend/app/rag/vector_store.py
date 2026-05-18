import chromadb
from .embedder import embed
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'chroma_store')
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(
    name='learning_resources',
    metadata={'hnsw:space': 'cosine'}
)

def add_resources(resources: list[dict]):
    """
    resources: list of dicts with id, title, description, topic, difficulty, url, source
    """
    ids = []
    embeddings = []
    metadatas = []
    documents = []

    for r in resources:
        ids.append(str(r['id']))
        text_to_embed = f"{r['title']}. {r['description']}"
        embeddings.append(embed(text_to_embed))
        metadatas.append({
            'title': r['title'],
            'topic': r['topic'],
            'difficulty': r['difficulty'],
            'url': r['url'],
            'source': r['source']
        })
        documents.append(text_to_embed)

    if ids:
        collection.upsert(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )

def search(query_text: str, top_k: int = 5):
    vec = embed(query_text)
    results = collection.query(query_embeddings=[vec], n_results=top_k)
    return results
