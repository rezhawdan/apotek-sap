import sqlalchemy as sa
from app.models import Base

class Produk(Base):
    __tablename__ = 'Produk'

    id = sa.Column('id', sa.Integer, primary_key=True)
    tipe_produk = sa.Column('tipe_produk', sa.String, nullable=False, default='Obat')
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
    status_penjualan = sa.Column('status_penjualan', sa.String, nullable=False, default='Dijual')
    perlu_resep = sa.Column('perlu_resep', sa.String, nullable=False, default='Tidak Wajib')
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
