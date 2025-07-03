from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.auth.auth_handler import verify_password, create_access_token
from app.database import get_db

router = APIRouter(tags=["auth"])

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.username == user.username).first()
    if not user_db or not verify_password(user.password, user_db.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user_db.username, "id": user_db.id})
    return {"access_token": token, "token_type": "bearer"}
