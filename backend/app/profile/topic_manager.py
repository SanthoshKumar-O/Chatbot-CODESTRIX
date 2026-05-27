from backend.app.models import TopicPerformance
def update_topic_score(
    db,
    user_id,
    topic,
    score
):
    performance = db.query(TopicPerformance).filter(
        TopicPerformance.user_id == user_id,
        TopicPerformance.topic == topic
    ).first()
    if not performance:
        performance = TopicPerformance(
            user_id=user_id,
            topic=topic,
            average_score=score,
            quizzes_taken=1,
            last_score=score
        )
        db.add(performance)
    else:
        total = (
            performance.average_score *
            performance.quizzes_taken
        )
        performance.quizzes_taken += 1
        performance.average_score = (
            total + score
        ) / performance.quizzes_taken

        performance.last_score = score

    db.commit()
    db.refresh(performance)
    return performance