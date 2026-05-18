from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from uuid import UUID

from .. import models, schemas
from ..database import get_db
from .auth import get_current_user
from ..rag.pipeline import pipeline

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
    # Verify session ownership
    session = db.query(models.Session).filter(
        models.Session.id == payload.session_id,
        models.Session.user_id == current_user.id
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
        
    # 1. Persist User Message immediately
    user_msg = models.Message(
        session_id=payload.session_id,
        role="user",
        content=payload.message
    )
    db.add(user_msg)
    db.commit()
    db.refresh(user_msg)
    
    # 2. Fetch past session history for conversation context (up to 10 previous messages)
    history_records = db.query(models.Message).filter(
        models.Message.session_id == payload.session_id
    ).order_by(models.Message.timestamp.asc()).all()
    
    # Build list of dicts for pipeline consumption
    history = [
        {"role": h.role, "content": h.content}
        for h in history_records
    ]
    
    # Return StreamingResponse using our async generator
    return StreamingResponse(
        pipeline(payload.message, history, payload.session_id),
        media_type="text/event-stream"
    )
