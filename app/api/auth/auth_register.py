import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from werkzeug.security import generate_password_hash

from app.dependencies.get_db_session import get_db_session
from app.models.user import User


class RegisterData(BaseModel):
    username: str
    full_name: str
    role: str
    password: str
    confirm_password: str


class UserData(BaseModel):
    username: str
    full_name: str
    role: str


async def auth_register(data: RegisterData, session=Depends(get_db_session)):
    if data.password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Konfirmasi password tidak sesuai")

    check_username = session.execute(
        sa.select(User.id_user).where(User.username == data.username)
    ).scalar()

    if check_username:
        raise HTTPException(status_code=400, detail="Username sudah digunakan.")

    encrypted_password = generate_password_hash(data.password)

    user = User(
        username=data.username,
        full_name=data.full_name,
        role=data.role,
        password=encrypted_password
    )

    session.add(user)
    session.commit()

    user_data = UserData(
        username=user.username,
        full_name=user.full_name,
        role=user.role
    )

    message = "Create data User berhasil."
    return {"message": message, "data": user_data}
