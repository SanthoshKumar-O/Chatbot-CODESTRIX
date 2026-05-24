def build_teaching_prompt(topic, difficulty):

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
Teach the topic: {topic}

Student skill level:
{difficulty}

Teaching instructions:
{style}

Make the explanation engaging and structured.
"""

    return prompt