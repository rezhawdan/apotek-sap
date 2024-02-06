import sqlalchemy as sa
from app.models import Base

class Kategori(Base):
    __tablename__ = 'Kategori'
    
    id_kategori = sa.Column('id_kategori', sa.CHAR, primary_key=True)
    nama_kategori = sa.Column('nama_kategori', sa.String)
