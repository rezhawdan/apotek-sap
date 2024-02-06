import sqlalchemy as sa
from app.models import Base

class Satuan(Base):
    __tablename__ = 'Satuan'
    
    id_satuan = sa.Column('id_satuan', sa.CHAR, primary_key=True)
    nama_satuan = sa.Column('nama_satuan', sa.String)
