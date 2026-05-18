import json
from app.rag.generator import generate_response

def build_quiz_prompt(topic,difficulty):
    prompt=f"""
        Generate five multiple choice quiz questions.
        Topic: {topic}
        Difficulty: {difficulty}

        Reqirements:
        - Each question should have four options.
        - Only one correct answer.
        - Explanation based on difficulty level.
        - return JSON format.

        Format:
        {{
            "Question_no.":"...",
            "question":"...",
            "options":["...","...","...","..."],
            "answer":"...",
            "explanation":"..."
        }}
            """

    return prompt

def generate_quiz(topic,difficulty):
    prompt=build_quiz_prompt(topic,difficulty)
    response=generate_response(prompt)
    quiz_data=json.loads(response)
    
    return quiz_data