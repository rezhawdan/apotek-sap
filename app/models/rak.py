import sqlalchemy as sa
from app.models import Base

class Rak(Base):
    __tablename__ = 'Rak'
    
    id_rak = sa.Column('id_rak', sa.CHAR, primary_key=True)
    daftar_rak = sa.Column('daftar_rak', sa.String)
