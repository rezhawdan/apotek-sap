import sqlalchemy as sa
import uuid

from app.models import Base


class Rak(Base):
    __tablename__ = 'Rak'

    id_rak = sa.Column('id_rak', sa.String(length=36),primary_key=True, default=str(uuid.uuid4()))
    code_rak = sa.Column('code_rak', sa.String)
    nama_rak = sa.Column('nama_rak', sa.String)
