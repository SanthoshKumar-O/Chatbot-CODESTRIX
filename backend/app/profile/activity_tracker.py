from datetime import date, timedelta
from backend.app.models import UserProfile


def track_user_activity(db, user_id):

    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        return
    today = date.today()
    if not profile.last_active_date:
        profile.days_active = 1
        profile.current_streak = 1
    else:
        difference = (today - profile.last_active_date).days
        if difference == 0:
            pass
        elif difference == 1:
            profile.days_active += 1
            profile.current_streak += 1
        else:
            profile.days_active += 1
            profile.current_streak = 1

    profile.last_active_date = today

    profile.total_messages += 1
    
    if profile.days_active > 0:
        profile.study_consistency=(profile.current_streak/profile.days_active)*100

    db.commit()