from RagBot.app.quiz.quiz_generator import generate_quiz
from backend.app.profile.topic_manager import update_topic_score
from backend.app.models import TopicPerformance,QuizAttempt
from RagBot.app.quiz.quiz_generator import generate_quiz
from RagBot.app.cluster.cluster_skill import run_clustering
def start_quiz(
    topic,
    difficulty=None,
    db=None,
    user_id=None
):

    previous_score = None

    previous_questions = []

    if db and user_id:

        performance = db.query(
            TopicPerformance
        ).filter(
            TopicPerformance.user_id == user_id,
            TopicPerformance.topic == topic
        ).first()

        if performance:

            previous_score = performance.average_score

            if previous_score < 40:
                difficulty = "beginner"

            elif previous_score < 75:
                difficulty = "intermediate"

            else:
                difficulty = "advanced"

        old_attempts = db.query(
            QuizAttempt
        ).filter(
            QuizAttempt.user_id == user_id,
            QuizAttempt.topic == topic
        ).all()

        for attempt in old_attempts:

            if attempt.questions:

                previous_questions.extend(
                    attempt.questions
                )

    if not difficulty:
        difficulty = "beginner"

    quiz_data = generate_quiz(
        topic,
        difficulty,
        previous_questions
    )

    return {
        "topic": topic,
        "difficulty": difficulty,
        "previous_score": previous_score,
        "questions": quiz_data
    }
def submit_quiz(topic,answers,questions,db=None,user_id=None):
    
    score = 0
    results = []
    for i, q in enumerate(questions):
        correct_answer = q["answer"]
        user_answer = answers[i]
        is_correct = user_answer == correct_answer
        if is_correct:
            score += 1
        results.append({
            "question": q["question"],
            "correct_answer": correct_answer,
            "your_answer": user_answer,
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })
    percentage = (score / len(questions)) * 100
    if db and user_id:
        update_topic_score(
            db,
            user_id,
            topic,
            percentage
        )

        attempt = QuizAttempt(
            user_id=user_id,
            topic=topic,
            score=score,
            total_questions=len(questions),
            accuracy=percentage,
            questions=questions,
            results=results
        )

        db.add(attempt)
        db.commit()
        db.refresh(attempt)
    run_clustering(db)

    return {
        "score": score,
        "total": len(questions),
        "percentage": percentage,
        "results": results
    }