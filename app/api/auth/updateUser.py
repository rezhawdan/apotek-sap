from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.user import User
from pydantic import BaseModel


class UpdateUserData(BaseModel):
    username: str
    full_name: str
    role: str


def updateUser(user_id: int, updated_data: UpdateUserData, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Data User by ID tidak ditemukan.")
    
    user.username = updated_data.username
    user.full_name = updated_data.full_name
    user.role = updated_data.role
    
    db.commit()
    
    message = "Update data User by ID berhasil"
    return {"message": message, "updated_data": updated_data.dict()}
