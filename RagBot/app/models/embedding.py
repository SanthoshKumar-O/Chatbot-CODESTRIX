from sentence_transformers import SentenceTransformer

embed_model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class Embed_function:
    def embed_documents(self,texts):
        embed=embed_model.encode(texts)
        return embed.tolist()
    
    def embed_query(self,texts):
        embed=embed_model.encode(texts)
        return embed.tolist()