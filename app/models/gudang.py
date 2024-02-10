import sqlalchemy as sa
import uuid

from app.models import Base

class Gudang(Base):
    __tablename__ = 'Gudang'
    
    id_gudang = sa.Column('id_gudang', sa.String(length=36), primary_key=True, default=str(uuid.uuid4()))
    code_gudang = sa.Column('code_gudang', sa.CHAR)
    nama_gudang = sa.Column('nama_gudang', sa.String)
