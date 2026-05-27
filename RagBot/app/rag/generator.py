import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL") or os.getenv("GROQ_MODEL_NAME") or "llama-3.3-70b-versatile"
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


def _fallback_response(prompt):
    lower = prompt.lower()
    if "quiz" in lower:
        return '{"questions":[{"question":"What is active recall?","options":["A memorization method","A file format","A database","A deployment tool"],"answer":"A memorization method","explanation":"Active recall means retrieving information from memory to strengthen learning."}]}'
    if "roadmap" in lower or "teach" in lower:
        return "A good learning path is: foundations, guided practice, and a small project."
    return "I can help with that, but I am running in fallback mode because the LLM key is missing."

def generate_response(prompt):
    if client is None:
        return _fallback_response(prompt)

    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    except Exception:
        return _fallback_response(prompt)

    return response.choices[0].message.content
