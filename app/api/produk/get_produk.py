import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.get_db_session import get_db_session
from app.models.produk import Produk

def get_produk(db: Session = Depends(get_db_session)):
    get_produk = db.query(
        Produk.id_produk, 
        Produk.tipe_produk,
        Produk.nama_produk,
        Produk.sku,
        Produk.nama_pabrik,
        Produk.barcode,
        Produk.rak,
        Produk.gudang,
        Produk.satuan,
        Produk.referensi_harga_beli,
        Produk.harga_jual,
        Produk.kategori,
        Produk.status_penjualan,
        Produk.perlu_resep
    ).all()
    message = "GET All data Produk berhasil."
    return {"message": message, "data": get_produk}
