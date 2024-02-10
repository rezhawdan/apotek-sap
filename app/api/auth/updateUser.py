from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.user import User
from pydantic import BaseModel


class UpdateUserData(BaseModel):
    username: str = None
    full_name: str = None
    role: str = None


def updateUser(user_id: str, updated_data: UpdateUserData, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id_user == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=404, detail="Data User by ID tidak ditemukan.")

    if updated_data.username:
        user.username = updated_data.username
    if updated_data.full_name:
        user.full_name = updated_data.full_name
    if updated_data.role:
        user.role = updated_data.role

    db.commit()

    updated_data_dict = updated_data.dict(exclude_unset=True)
    if not updated_data_dict:
        updated_data_dict = {
            "username": user.username,
            "full_name": user.full_name,
            "role": user.role
        }

    message = "Update data User by ID berhasil"
    return {"message": message, "data": updated_data_dict}
