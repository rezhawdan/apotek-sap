import sqlalchemy as sa
from app.models import Base

class Gudang(Base):
    __tablename__ = 'Gudang'
    
    id_gudang = sa.Column('id_gudang', sa.CHAR, primary_key=True)
    nama_gudang = sa.Column('nama_gudang', sa.String)
