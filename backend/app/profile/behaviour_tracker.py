from backend.app.models import UserProfile
from RagBot.app.cluster.cluster_skill import run_clustering

def track_learning_behavior(
    db,
    user_id,
    intent,
    topic,
    message
):

    profile = db.query(UserProfile).filter(
        UserProfile.user_id == user_id
    ).first()

    if not profile:
        return

    if intent == "teach":
        profile.teaching_requests += 1

    elif intent == "quiz":
        profile.quiz_requests += 1

    profile.preferred_topic = topic

    current_length = len(message.split())

    if profile.total_messages > 0:

        profile.average_message_length = (
            (
                profile.average_message_length
                * (profile.total_messages - 1)
            ) + current_length
        ) / profile.total_messages



    total_learning_actions = (
        profile.teaching_requests
        + profile.quiz_requests
    )

    if total_learning_actions > 0:

        teaching_ratio = (
            profile.teaching_requests
            / total_learning_actions
        )

        quiz_ratio = (
            profile.quiz_requests
            / total_learning_actions
        )


        if teaching_ratio >= 0.6:
            profile.learning_behavior = "theory_focused"

        elif quiz_ratio >= 0.6:
            profile.learning_behavior = "assessment_focused"

        else:
            profile.learning_behavior = "balanced"

    db.commit()
    run_clustering(db)