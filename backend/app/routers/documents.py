from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from ..database import get_db
from .auth import get_current_user
from .. import models

router = APIRouter(
    prefix="/api/documents",
    tags=["documents"],
)

_documents_by_user = {}


def _bucket(user_id):
    return _documents_by_user.setdefault(str(user_id), [])


@router.get("/")
def list_documents(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return {"documents": _bucket(current_user.id)}


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    docs = _bucket(current_user.id)
    document = {
        "id": len(docs) + 1,
        "name": file.filename,
        "uploadedAt": __import__("datetime").datetime.utcnow().isoformat(),
        "status": "Indexed",
    }
    docs.append(document)
    return document


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    docs = _bucket(current_user.id)
    if document_id < 1 or document_id > len(docs):
        raise HTTPException(status_code=404, detail="Document not found")
    docs.pop(document_id - 1)
    return {"deleted": True}