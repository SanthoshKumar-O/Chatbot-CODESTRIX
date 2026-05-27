from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from RagBot.app.cluster.cluster_skill import run_clustering
from .. import models, schemas, auth_utils
from ..database import get_db

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)


def ensure_guest_user(db: Session):
    guest_email = "guest@codestrix.local"
    guest = db.query(models.User).filter(models.User.email == guest_email).first()
    if guest:
        return guest

    hashed_password = "guest"
    guest = models.User(email=guest_email, hashed_password=hashed_password)
    db.add(guest)
    db.commit()
    db.refresh(guest)

    profile = models.UserProfile(user_id=guest.id)
    db.add(profile)
    db.commit()
    return guest

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    if not token:
        return ensure_guest_user(db)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, auth_utils.SECRET_KEY, algorithms=[auth_utils.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        return ensure_guest_user(db)
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if user is None:
        return ensure_guest_user(db)
    return user

@router.post("/register", response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = auth_utils.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    profile = models.UserProfile(
    user_id=new_user.id)   
    db.add(profile)
    db.commit()
    run_clustering(db)
    
    access_token_expires = timedelta(minutes=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_utils.create_access_token(
        data={"sub": new_user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()
    if not user or not auth_utils.verify_password(
        form_data.password,
        user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = auth_utils.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
}