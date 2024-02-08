from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.produk import Produk
from pydantic import BaseModel


class UpdateProdukData(BaseModel):
    tipe_produk: str
    nama_produk: str
    sku: str
    nama_pabrik: str
    barcode: str
    rak: str
    gudang: str
    satuan_utama: str
    referensi_harga_beli: int
    harga_jual: int
    kategori: str
    status_penjualan: str
    perlu_resep: str


def updateProduk(produk_id: int, updated_data: UpdateProdukData, db: Session = Depends(get_db_session)):
    produk = db.query(Produk).filter(Produk.id == produk_id).first()
    if produk is None:
        raise HTTPException(status_code=404, detail="Data Produk by ID tidak ditemukan.")
    
    produk.tipe_produk = updated_data.tipe_produk
    produk.nama_produk = updated_data.nama_produk
    produk.sku = updated_data.sku
    produk.nama_pabrik = updated_data.nama_pabrik
    produk.barcode = updated_data.barcode
    produk.rak = updated_data.rak   
    produk.gudang = updated_data.gudang
    produk.satuan_utama = updated_data.satuan_utama
    produk.referensi_harga_beli = updated_data.referensi_harga_beli
    produk.harga_jual = updated_data.harga_jual
    produk.kategori = updated_data.kategori
    produk.status_penjualan = updated_data.status_penjualan
    produk.perlu_resep = updated_data.perlu_resep
    
    db.commit()
    
    message = "Update data Produk by ID berhasil"
    return {"message": message, "data": updated_data.dict()}
