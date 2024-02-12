from fastapi.exceptions import HTTPException
from werkzeug.security import check_password_hash
from app.models.user import User
from pydantic import BaseModel
from fastapi import Depends
from uuid import UUID
import sqlalchemy as sa
from app.dependencies.get_db_session import get_db_session
from app.models.user_login import UserLogin
from app.config import config
from app.utils.generate_refresh_token import generate_refresh_token
from app.utils.generate_access_token import generate_access_token


class LoginData(BaseModel):
    username: str
    password: str


class LoginDataResponseModel(BaseModel):
    user_id: UUID
    refresh_token: str
    access_token: str
    expired_at: int


class LoginResponseModel(BaseModel):
    message: str
    data: LoginDataResponseModel


async def auth_login(data: LoginData, session=Depends(get_db_session)):
    user = session.execute(
        sa.select(
            User.id_user,
            User.password
        ).where(
            User.username == data.username
        )
    ).fetchone()

    if not user or not check_password_hash(user.password, data.password):
        raise HTTPException(status_code=400, detail='Username atau password tidak ditemukan.')
    
    payload = {
        'uid': user.id_user,
        'username': data.username
    }

    refresh_token = generate_refresh_token(payload)

    user_login = UserLogin(
        user_id=user.id_user,
        refresh_token=refresh_token,
        expired_at=sa.func.TIMESTAMPADD(
            sa.text('SECOND'),
            config.REFRESH_TOKEN_EXPIRATION,
            sa.func.NOW()
        )
    )

    session.add(user_login)
    session.commit()
    
    access_token, access_token_expired_at = generate_access_token(payload)

    response_data = LoginDataResponseModel(
        user_id=user.id_user,
        refresh_token=refresh_token,
        access_token=access_token,
        expired_at=access_token_expired_at
    )

    return LoginResponseModel(message="Login berhasil", data=response_data)
