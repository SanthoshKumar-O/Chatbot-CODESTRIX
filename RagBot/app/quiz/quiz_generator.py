import json
from RagBot.app.rag.generator import generate_response

def build_quiz_prompt(
    topic,
    difficulty,
    previous_questions=None
):

    previous_block = ""

    if previous_questions:

        previous_block = f"""
AVOID GENERATING THESE QUESTIONS AGAIN:

{previous_questions}
"""

    prompt = f"""
You are an expert programming quiz generator.

Generate exactly 5 multiple-choice questions.

TOPIC:
{topic}

DIFFICULTY:
{difficulty}

{previous_block}

RULES:
- Return ONLY valid JSON
- No markdown
- No extra text
- No code block markers
- Avoid repeating old questions
- Questions must test understanding
- Each question must contain:
    - question
    - 4 options
    - answer
    - explanation
- Only ONE correct answer
- Explanations must be educational

JSON FORMAT:

{{
  "questions": [
    {{
      "question": "Example question",
      "options": [
        "A",
        "B",
        "C",
        "D"
      ],
      "answer": "A",
      "explanation": "Explanation"
    }}
  ]
}}

IMPORTANT:
Return ONLY JSON.
"""

    return prompt


def generate_quiz(
    topic,
    difficulty,
    previous_questions=None
):
    prompt = build_quiz_prompt(
        topic,
        difficulty,
        previous_questions
    )
    response = generate_response(prompt)
    response = response.strip()
    response = response.replace("```json","")
    response = response.replace("```","")
    
    try:
        quiz_data = json.loads(response)
        return quiz_data["questions"]
    except json.JSONDecodeError:
        print("\nInvalid JSON from LLM\n")
        print(response)
        raise Exception(
            "Quiz generation failed"
        )