from RagBot.app.skill.intent_classifier import classify_intent
from RagBot.app.quiz.quiz_engine import start_quiz
from RagBot.app.rag.generator import generate_response
from RagBot.app.skill.teaching_prompt import build_teaching_prompt

from backend.app.memory.chat_memory import (
    save_message,
    get_chat_history
)

from backend.app.profile.behaviour_tracker import (
    track_learning_behavior
)

from backend.app.profile.activity_tracker import (
    track_user_activity
)

from backend.app.models import UserProfile


def mentor_agent(
    user_query,
    db,
    session_id,
    user_id
):

    
    # CLASSIFY USER INTENT
    

    analysis = classify_intent(user_query)

    intent = analysis.get(
        "intent",
        "teach"
    )

    topic = analysis.get(
        "topic",
        "general programming"
    )

    needs_quiz = analysis.get(
        "needs_quiz",
        False
    )

    
    # SAVE USER MESSAGE
    

    save_message(
        db,
        session_id,
        "user",
        user_query
    )

    
    # TRACK USER ACTIVITY
    

    track_user_activity(
        db,
        user_id
    )

    
    # TRACK LEARNING BEHAVIOR
    

    track_learning_behavior(
        db,
        user_id,
        intent,
        topic,
        user_query
    )

    
    # LOAD USER PROFILE
    

    profile = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    skill_label = "Newbie"

    if profile and profile.skill_label:

        skill_label = profile.skill_label

    
    # LOAD CHAT HISTORY
    

    history_records = get_chat_history(
        db,
        session_id
    )

    history = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in history_records
    ])

    
    # QUIZ REQUEST
    

    if intent == "quiz":

        return start_quiz(
            topic,
            skill_label,
            db,
            user_id
        )

    
    # TEACHING REQUEST
    

    elif intent == "teach":

        prompt = build_teaching_prompt(
            topic,
            skill_label,
            history,
            user_query
        )

        response = generate_response(prompt)

        
        # SAVE ASSISTANT RESPONSE
        

        save_message(
            db,
            session_id,
            "assistant",
            response
        )

        
        # OPTIONAL QUIZ AFTER TEACHING
        

        if needs_quiz:

            print("\nStarting assessment quiz...\n")

            quiz_result = start_quiz(
                topic,
                skill_label,
                db,
                user_id
            )

            return {

                "teaching": response,

                "quiz_result": quiz_result
            }

        return response

    # FALLBACK


    return "I couldn't understand the request."