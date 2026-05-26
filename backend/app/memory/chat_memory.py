from backend.app import models

def save_message(db, session_id, role, content):

    message = models.Message(
        session_id=session_id,
        role=role,
        content=content
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message

def get_chat_history(db, session_id):

    messages = db.query(models.Message).filter(
        models.Message.session_id == session_id
    ).order_by(models.Message.timestamp.asc()).all()

    history = []

    for msg in messages:

        history.append({
            "role": msg.role,
            "content": msg.content
        })

    return history