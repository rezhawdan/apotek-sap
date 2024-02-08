from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.user import User


def deleteUser(user_id: int, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Data User berdasarkan ID tidak ditemukan."
        )

    db.delete(user)
    db.commit()

    message = "Data User berhasil dihapus."
    return {"message": message}
