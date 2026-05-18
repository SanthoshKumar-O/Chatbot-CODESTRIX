from sentence_transformers import SentenceTransformer

# Load model globally to avoid reloading on every request
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed(text: str) -> list[float]:
    """Embed text into a vector."""
    return model.encode(text).tolist()
