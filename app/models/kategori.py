import sqlalchemy as sa
import uuid

from app.models import Base

class Kategori(Base):
    __tablename__ = 'Kategori'
    
    id_kategori = sa.Column('id_kategori', sa.String(length=36), primary_key=True, default=str(uuid.uuid4()))
    code_kategori = sa.Column('code_kategori', sa.String)
    nama_kategori = sa.Column('nama_kategori', sa.String)
