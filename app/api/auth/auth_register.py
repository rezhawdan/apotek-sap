import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from werkzeug.security import generate_password_hash

from app.dependencies.get_db_session import get_db_session
from app.models.user import User

class RegisterData(BaseModel):
    username: str
    full_name: str
    role: str
    password: str
    confirm_password: str
    
    @validator('confirm_password', pre=True, always=True)
    def validate_confirm_password(cls, value, values):
        password = values.get('password')
        if value != password:
            raise ValueError('Confirm password does not match.')
        return value

async def auth_register(data: RegisterData, session = Depends(get_db_session)):
    check_username = session.execute(
        sa.select(User.id).where(User.username == data.username)
    ).scalar()
    
    if check_username:
        raise HTTPException(400, detail='Username already exist.')
    
    encypted_password = generate_password_hash(data.password)
    
    user = User(
        username=data.username,
        full_name=data.full_name,
        role=data.role,
        password=encypted_password
    )
    
    session.add(user)
    session.commit()
    
    return Response(status_code=201)
