from app.skill.intent_classifier import classify_intent
from app.quiz.quiz_engine import start_quiz
from app.quiz.assessment import assess_skill
from app.rag.generator import generate_response
from app.skill.teaching_prompt import build_teaching_prompt

def mentor_agent(user_query):

    analysis = classify_intent(user_query)

    intent = analysis.get("intent", "teach")
    topic = analysis.get("topic", "general programming")
    difficulty = analysis.get("difficulty", "unknown")
    needs_quiz = analysis.get("needs_quiz", False)
    if difficulty.lower().strip() == "unknown":

        difficulty = assess_skill(topic)

        print(f"\nEstimated Skill Level: {difficulty}")


    if intent == "quiz":

        return start_quiz(topic, difficulty)


    elif intent == "teach":

        prompt = build_teaching_prompt(topic, difficulty)

        response = generate_response(prompt)

    
        if needs_quiz:

            print("\nStarting assessment quiz...\n")

            quiz_result = start_quiz(topic, difficulty)

            return {
                "teaching": response,
                "quiz_result": quiz_result
            }

        return response
    return "I couldn't understand the request."