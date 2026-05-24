import json
from app.rag.generator import generate_response

def build_quiz_prompt(topic, difficulty):

    prompt = f"""
Generate five multiple choice quiz questions.

Topic: {topic}
Difficulty: {difficulty}

Requirements:
- Each question should have four options
- Only one correct answer
- Include explanation
- Return response in valid JSON format
- Output ONLY JSON

Format:

{{
    "questions":[
        {{
            "question":"...",
            "options":["...","...","...","..."],
            "answer":"...",
            "explanation":"..."
        }}
    ]
}}
"""

    return prompt


def generate_quiz(topic, difficulty):

    prompt = build_quiz_prompt(topic, difficulty)

    response = generate_response(prompt)
    response = response.strip()
    response = response.replace("```json", "")
    response = response.replace("```", "")
    print(response)
    quiz_data = json.loads(response)

    return quiz_data["questions"]