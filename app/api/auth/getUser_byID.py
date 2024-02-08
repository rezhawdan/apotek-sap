from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.user import User


def getUser_byID(user_id: int, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Data User by ID tidak ditemukan.")
    
    user_data = {
        "id_user": user.id,
        "username": user.username,
        "full_name": user.full_name,
        "role": user.role
    }
    message = "GET data User by ID berhasil"
    return {"message": message, "data": user_data}
