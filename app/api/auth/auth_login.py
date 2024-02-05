from fastapi.exceptions import HTTPException
from werkzeug.security import check_password_hash
from app.models.user import User
from pydantic import BaseModel
from fastapi import Depends
import sqlalchemy as sa
from app.dependencies.get_db_session import get_db_session
from app.api_models.base_response import BaseResponseModel
from app.models.user_login import UserLogin
from app.config import config

class LoginData(BaseModel):
    username: str
    password: str

class LoginDataResponseModel(BaseModel):
    user_id: int
    refresh_token: str
    access_token: str
    expired_at: int

class LoginResponseModel(BaseResponseModel):
    data: LoginDataResponseModel

async def auth_login(data: LoginData, session=Depends(get_db_session)):
    # check username
    user = session.execute(
        sa.select(
            User.id,
            User.password
        ).where(
            User.username == data.username
        )
    ).fetchone()

    if not user or not check_password_hash(user.password, data.password):
        raise HTTPException(400, detail='Username or password does not found.')

    # Simulasikan nilai hardcoded untuk refresh_token dan access_token
    refresh_token = 'abcdefghi'
    access_token = 'jklmnopqr'
    access_token_expired_at = 123456

    # Simpan data ke database
    user_login = UserLogin(
        user_id=user.id,
        refresh_token=refresh_token,
        expired_at=sa.func.TIMESTAMPADD(
            sa.text('SECOND'),
            config.REFRESH_TOKEN_EXPIRATION,
            sa.func.NOW()
        )
    )

    session.add(user_login)
    session.commit()

    return LoginResponseModel(
        data=LoginDataResponseModel(
            user_id=user.id,
            refresh_token=refresh_token,
            access_token=access_token,
            expired_at=access_token_expired_at
        )
    )
