import sqlalchemy as sa
import uuid
from app.models import Base


class Produk(Base):
    __tablename__ = 'Produk'

    id_produk = sa.Column('id_produk', sa.String(length=36), primary_key=True, default=str(uuid.uuid4()))
    tipe_produk = sa.Column('tipe_produk', sa.String)
    nama_produk = sa.Column('nama_produk', sa.String)
    sku = sa.Column('sku', sa.CHAR)
    nama_pabrik = sa.Column('nama_pabrik', sa.String)
    barcode = sa.Column('barcode', sa.CHAR)
    rak = sa.Column('rak', sa.CHAR)
    satuan = sa.Column('satuan', sa.CHAR)
    gudang = sa.Column('gudang', sa.CHAR)
    referensi_harga_beli = sa.Column('referensi_harga_beli', sa.Integer, nullable=True)
    harga_jual = sa.Column('harga_jual', sa.Integer, nullable=True)
    kategori = sa.Column('kategori', sa.CHAR)
    status_penjualan = sa.Column('status_penjualan', sa.String)
    perlu_resep = sa.Column('perlu_resep', sa.String,)
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
