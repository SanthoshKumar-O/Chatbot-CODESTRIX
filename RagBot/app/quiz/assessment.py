from app.quiz.quiz_engine import start_quiz

def assess_skill(topic):

    print("\nSkill level not detected.")
    print("Starting quick assessment...\n")

    result = start_quiz(
        topic=topic,
        difficulty=2
    )

    accuracy = result["accuracy"]

    if accuracy >= 0.8:
        return "advanced"

    elif accuracy >= 0.5:
        return "intermediate"

    else:
        return "beginner"