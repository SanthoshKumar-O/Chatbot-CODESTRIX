from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from .auth import get_current_user
from RagBot.app.skill.mentor_agent import mentor_agent

router = APIRouter(
    prefix="/api/chat",
    tags=["chat"],
)

@router.post("/stream")
async def chat_stream(
    payload: schemas.ChatRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    session = db.query(models.Session).filter(
        models.Session.id == payload.session_id,
        models.Session.user_id == current_user.id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    response = mentor_agent(
        payload.message,
        db,
        payload.session_id
    )

    return {
        "response": response
    }