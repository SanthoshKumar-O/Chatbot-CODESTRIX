def build_teaching_prompt(topic, difficulty, history, user_query):

    if difficulty == "beginner":

        style = """
- Explain using simple words
- Use beginner-friendly analogies
- Avoid heavy jargon
- Teach step-by-step
- Include basic examples
"""

    elif difficulty == "intermediate":

        style = """
- Explain concepts clearly
- Include practical coding examples
- Explain logic and workflow
- Introduce moderate technical terms
"""

    else:

        style = """
- Teach in depth
- Include optimization techniques
- Explain internal working
- Include edge cases
- Discuss complexity analysis
"""

    prompt = f"""
You are an AI programming mentor.

Previous Conversation:
{history}

Current User Question:
{user_query}

Topic:
{topic}

Student Skill Level:
{difficulty}

Teaching Style Instructions:
{style}

Rules:
- Continue naturally from previous conversation if relevant
- Do not restart the topic unnecessarily
- Adapt explanation to student skill level
- Keep response engaging and educational
"""

    return prompt