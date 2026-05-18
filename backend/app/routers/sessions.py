from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from datetime import datetime, timezone

from .. import models, schemas
from ..database import get_db
from .auth import get_current_user

router = APIRouter(
    prefix="/api/sessions",
    tags=["sessions"],
)

@router.get("/", response_model=List[schemas.SessionResponse])
def get_sessions(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    sessions = db.query(models.Session).filter(models.Session.user_id == current_user.id).order_by(models.Session.created_at.desc()).all()
    return sessions

@router.post("/", response_model=schemas.SessionResponse)
def create_session(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    title = f"Chat {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}"
    new_session = models.Session(user_id=current_user.id, title=title)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@router.get("/{session_id}/messages/", response_model=List[schemas.MessageResponse])
def get_session_messages(session_id: UUID, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    session = db.query(models.Session).filter(models.Session.id == session_id, models.Session.user_id == current_user.id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    messages = db.query(models.Message).filter(models.Message.session_id == session_id).order_by(models.Message.timestamp.asc()).all()
    return messages

@router.delete("/{session_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(session_id: UUID, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    session = db.query(models.Session).filter(models.Session.id == session_id, models.Session.user_id == current_user.id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    db.delete(session)
    db.commit()
    return None
