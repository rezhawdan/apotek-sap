import sqlalchemy as sa
from sqlalchemy import Enum
from app.models import Base

class Produk(Base):
    __tablename__ = 'Produk'

    class TipeProdukEnum(Enum):
        UMUM = 'Umum'
        OBAT = 'Obat'
        ALKES = 'Alkes'
        JASA = 'Jasa'
    
    class StatusPenjualanEnum(Enum):
        DIJUAL = 'Dijual'
        TIDAKDIJUAL = 'Tidak Dijual'
        
    class PerluResepEnum(Enum):
        WAJIB = 'Wajib'
        TIDAKWAJIB = 'Tidak Wajib'

    id = sa.Column('id', sa.Integer, primary_key=True)
    tipe_produk = sa.Column('tipe_produk', TipeProdukEnum, nullable=False, default=TipeProdukEnum.UMUM)
    nama_produk = sa.Column('nama_produk', sa.String)
    sku = sa.Column('sku', sa.CHAR)
    nama_pabrik = sa.Column('nama_pabrik', sa.String)
    barcode = sa.Column('barcode', sa.CHAR)
    rak = sa.Column('rak', sa.CHAR)
    satuan_utama = sa.Column('satuan_utama', sa.CHAR)
    gudang = sa.Column('gudang', sa.CHAR)
    referensi_harga_beli = sa.Column('referensi_harga_beli', sa.Integer, nullable=True)
    harga_jual = sa.Column('harga_jual', sa.Integer, nullable=True)
    kategori = sa.Column('kategori', sa.CHAR)
    status_penjualan = sa.Column('status_penjualan', StatusPenjualanEnum, nullable=False, default=StatusPenjualanEnum.DIJUAL)
    perlu_resep = sa.Column('perlu_resep', PerluResepEnum, nullable=False, default=PerluResepEnum.TIDAKWAJIB)
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
