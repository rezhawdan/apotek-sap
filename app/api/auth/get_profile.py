import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.get_db_session import get_db_session
from app.models.user import User

def get_users(db: Session = Depends(get_db_session)):
    users = db.query(
        User.id_user, 
        User.username, 
        User.full_name, 
        User.role
    ).all()
    message = "GET All data user berhasil."
    return {"message": message, "data": users}
