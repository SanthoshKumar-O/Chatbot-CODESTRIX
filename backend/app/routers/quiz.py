from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import QuizAttempt
from ..schemas import QuizAttemptCreate
from .auth import get_current_user
from .. import models

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)

@router.post("/save")
def save_quiz_attempt(
    quiz: QuizAttemptCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    attempt = QuizAttempt(
        user_id=current_user.id,
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
        "message": "Quiz attempt saved",
        "quiz_id": attempt.id
    }