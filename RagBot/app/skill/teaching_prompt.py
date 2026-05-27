def build_teaching_prompt(topic, skill_label, history, user_query):

    if skill_label == "Newbie":

        style = """
- Teach like the student is completely new
- Use tiny examples
- Explain every term
- Avoid assumptions
- Use friendly analogies
-Don't use advanced technical terms if you use explain them as well
- Go step by step
"""

    elif skill_label == "Beginner":

        style = """
- Use beginner-friendly explanations
- Introduce coding terminology slowly
- Include simple practical examples
- Reinforce fundamentals
-Ensure concepts are clear before moving on
"""

    elif skill_label == "Intermediate":

        style = """
- Focus on logic building
- Include coding workflow explanations
- Use moderate technical depth
- Encourage problem solving
"""
    elif skill_label == "Advanced Intermediate":

        style = """
- Include optimization techniques
- Discuss edge cases
- Explain internal behavior
- Encourage scalable thinking
"""

    else:  # Advanced
        style = """
- Teach deeply and technically
- Include complexity analysis
- Discuss architecture decisions
- Explain tradeoffs and optimizations
- Focus on professional-level understanding
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
{skill_label}

Teaching Style Instructions:
{style}

Rules:
- Continue naturally from previous conversation if relevant
- Do not restart the topic unnecessarily
- Adapt explanation to student skill level
- Keep response engaging and educational
"""

    return prompt