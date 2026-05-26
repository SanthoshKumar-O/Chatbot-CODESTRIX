from RagBot.app.skill.intent_classifier import classify_intent
from RagBot.app.quiz.quiz_engine import start_quiz
from RagBot.app.quiz.assessment import assess_skill
from RagBot.app.rag.generator import generate_response
from RagBot.app.skill.teaching_prompt import build_teaching_prompt
from backend.app.memory.chat_memory import (
    save_message,
    get_chat_history
)
def mentor_agent(user_query,db,session_id):

    analysis = classify_intent(user_query)
    save_message(
    db,
    session_id,
    "user",
    user_query
)
    history = get_chat_history(db, session_id)
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
        prompt = build_teaching_prompt(
            topic,
            difficulty,
            history,
            user_query
        )

        response = generate_response(prompt)
        save_message(
            db,
            session_id,
            "assistant",
            response
        )
        if needs_quiz:
            print("\nStarting assessment quiz...\n")
            quiz_result = start_quiz(topic, difficulty)
            return {
                "teaching": response,
                "quiz_result": quiz_result
            }

        return response
    return "I couldn't understand the request."