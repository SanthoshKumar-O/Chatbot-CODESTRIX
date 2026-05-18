import os
import json
from groq import Groq
from .vector_store import search
from .prompts import SYSTEM_PROMPT
from ..database import SessionLocal
from .. import models

# Init Groq Client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def format_context(search_results) -> str:
    """Format ChromaDB search results into a clean text block."""
    context_items = []
    if not search_results or 'documents' not in search_results or not search_results['documents']:
        return "No resource records found."
    
    docs = search_results['documents'][0]
    metas = search_results['metadatas'][0]
    
    for i in range(len(docs)):
        meta = metas[i]
        item = (
            f"Title: {meta.get('title')}\n"
            f"Topic: {meta.get('topic')}\n"
            f"Difficulty: {meta.get('difficulty')}\n"
            f"Source: {meta.get('source')}\n"
            f"URL: {meta.get('url')}\n"
            f"Description: {docs[i]}\n"
        )
        context_items.append(item)
    
    return "\n---\n".join(context_items)

async def pipeline(user_message: str, history: list[dict], session_id: str):
    """
    Async generator that queries vector store, streams LLM completions, and
    saves the final assistant response to the SQL database upon stream completion.
    """
    # Step 1: ChromaDB Search
    search_results = search(user_message, top_k=5)
    context = format_context(search_results)
    
    # Step 2: Build Messages Array
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT.format(context=context)}
    ]
    
    # Add last 10 turns of history
    for msg in history[-10:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
        
    # Add the current message
    messages.append({"role": "user", "content": user_message})
    
    # Step 3: Call Groq client stream
    model_name = os.getenv("GROQ_MODEL", "llama3-70b-8192")
    
    # We execute Groq stream in a non-blocking way using sync client (since Groq Python SDK stream is iterable)
    # We yield tokens one by one
    stream = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=True,
    )
    
    full_response = ""
    for chunk in stream:
        token = chunk.choices[0].delta.content or ''
        if token:
            full_response += token
            # Yield SSE formatted data
            yield f"data: {json.dumps({'token': token})}\n\n"
            
    # Step 4: Persist Assistant reply to Supabase SQL Database
    db = SessionLocal()
    try:
        assistant_message = models.Message(
            session_id=session_id,
            role="assistant",
            content=full_response
        )
        db.add(assistant_message)
        db.commit()
    except Exception as e:
        print(f"Error persisting assistant message: {e}")
        db.rollback()
    finally:
        db.close()
        
    yield "data: [DONE]\n\n"
