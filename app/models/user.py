import sqlalchemy as sa
import uuid

from app.models import Base


class User(Base):
    __tablename__ = 'User'

    id_user = sa.Column('id_user', sa.String(length=36), primary_key=True, default=str(uuid.uuid4()))
    username = sa.Column('username', sa.String)
    password = sa.Column('password', sa.String)
    full_name = sa.Column('full_name', sa.String)
    role = sa.Column('role', sa.String)
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
