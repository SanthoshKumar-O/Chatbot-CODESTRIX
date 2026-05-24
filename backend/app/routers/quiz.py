from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_db
from ..models import QuizAttempt
from ..schemas import QuizAttemptCreate

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)

@router.post("/save")

def save_quiz_attempt(quiz: QuizAttemptCreate,db: Session = Depends(get_db)):
    attempt = QuizAttempt(
        user_id="PUT_USER_ID_LATER",
        topic=quiz.topic,
        difficulty=quiz.difficulty,
        score=quiz.score,
        total_questions=quiz.total_questions,
        accuracy=quiz.accuracy
    )

    db.add(attempt)

    db.commit()

    db.refresh(attempt)

    return {
        "message":"Quiz attempt saved",
        "quiz_id":attempt.id
    }