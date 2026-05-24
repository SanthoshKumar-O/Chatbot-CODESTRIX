import json
from app.rag.generator import generate_response

def classify_intent(user_query):

    prompt = f"""
You are an educational intent classifier.

Analyze the student's query.

Possible intents:

1. teach
- User wants explanation or learning.
- Examples:
  "Teach recursion"
  "Explain linked list"

2. quiz
- User wants assessment/testing/questions.
- Examples:
  "Test me on recursion"
  "Check my understanding"
  "Ask me questions"
  "Evaluate me"
  "See if I understood"

3. roadmap
- User wants learning path or study plan.
- Examples:
  "Give DSA roadmap"

4. doubt
- User asks a specific question or confusion.
- Examples:
  "Why recursion uses stack?"
  "What is base condition?"

Return ONLY valid JSON.

Format:
{{
    "intent":"...",
    "topic":"...",
    "difficulty":"..."
}}

User Query:
{user_query}
"""

    response = generate_response(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    return json.loads(response)