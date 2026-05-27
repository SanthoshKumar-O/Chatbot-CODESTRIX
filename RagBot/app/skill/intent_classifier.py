import json
from RagBot.app.rag.generator import generate_response

def classify_intent(user_query):
    lowered = user_query.lower()
    if any(word in lowered for word in ["quiz", "test me", "check my understanding", "evaluate me"]):
        return {"intent": "quiz", "topic": "general", "difficulty": "beginner"}
    if any(word in lowered for word in ["roadmap", "plan", "teach", "explain", "learn"]):
        return {"intent": "teach", "topic": "general programming", "difficulty": "beginner"}
    return {"intent": "teach", "topic": "general programming", "difficulty": "beginner"}