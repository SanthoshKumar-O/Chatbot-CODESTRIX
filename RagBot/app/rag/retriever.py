from langchain_chroma import Chroma
from app.models.embedding import Embed_function

db=Chroma(persist_directory="app/db/chroma",embedding_function=Embed_function())

def retrieve_context(query,k=3):
    results=db.similarity_search(query,k=3)
    context=[]
    for r in results:
        context.append(r.page_content)
    return "\n\n".join(context)
