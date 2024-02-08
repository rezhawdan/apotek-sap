from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.produk import Produk


def getProduk_byID(produk_id: str, db: Session = Depends(get_db_session)):
    produk = db.query(Produk).filter(Produk.id == produk_id).first()
    if produk is None:
        raise HTTPException(
            status_code=404, detail="Data produk by ID tidak ditemukan.")

    produk_data = {
        'id_produk': produk.id,
        'tipe_produk': produk.tipe_produk,
        'nama_produk': produk.nama_produk,
        'sku': produk.sku,
        'nama_pabrik': produk.nama_pabrik,
        'barcode': produk.barcode,
        'rak': produk.rak,
        'gudang': produk.gudang,
        'satuan_utama': produk.satuan_utama,
        'referensi_harga_beli': produk.referensi_harga_beli,
        'harga_jual': produk.harga_jual,
        'kategori': produk.kategori,
        'status_penjualan': produk.status_penjualan,
        'perlu_resep': produk.perlu_resep,
    }
    message = 'GET data produk by ID berhasil'
    return {'message': message, 'data': produk_data}
