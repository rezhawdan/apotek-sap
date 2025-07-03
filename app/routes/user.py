from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.auth.auth_handler import get_password_hash
from app.auth.auth_bearer import JWTBearer
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.username == user.username).first()
    if user_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/me", dependencies=[Depends(JWTBearer())], response_model=UserOut)
def get_me(token_data=Depends(JWTBearer()), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == token_data["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
