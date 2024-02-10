import sqlalchemy as sa
import uuid

from app.models import Base


class Satuan(Base):
    __tablename__ = 'Satuan'

    id_satuan = sa.Column('id_satuan', sa.String(length=36),primary_key=True, default=str(uuid.uuid4()))
    code_satuan = sa.Column('code_satuan', sa.String)
    nama_satuan = sa.Column('nama_satuan', sa.String)
