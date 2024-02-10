from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.produk import Produk
from pydantic import BaseModel


class UpdateProdukData(BaseModel):
    tipe_produk: str = None
    nama_produk: str = None
    sku: str = None
    nama_pabrik: str = None
    barcode: str = None
    rak: str = None
    gudang: str = None
    satuan: str = None
    referensi_harga_beli: int = None
    harga_jual: int = None
    kategori: str = None
    status_penjualan: str = None
    perlu_resep: str = None


def updateProduk(produk_id: str, updated_data: UpdateProdukData, db: Session = Depends(get_db_session)):
    produk = db.query(Produk).filter(Produk.id_produk == produk_id).first()
    if produk is None:
        raise HTTPException(status_code=404, detail="Data Produk by ID tidak ditemukan.")
    
    if updated_data.tipe_produk is not None:
        produk.tipe_produk = updated_data.tipe_produk
    if updated_data.nama_produk is not None:
        produk.nama_produk = updated_data.nama_produk
    if updated_data.sku is not None:  
        produk.sku = updated_data.sku
    if updated_data.nama_pabrik is not None:    
        produk.nama_pabrik = updated_data.nama_pabrik
    if updated_data.barcode is not None:    
        produk.barcode = updated_data.barcode
    if updated_data.rak is not None:    
        produk.rak = updated_data.rak
    if updated_data.gudang is not None:    
        produk.gudang = updated_data.gudang
    if updated_data.satuan is not None:    
        produk.satuan = updated_data.satuan
    if updated_data.referensi_harga_beli is not None:    
        produk.referensi_harga_beli = updated_data.referensi_harga_beli
    if updated_data.harga_jual is not None:    
        produk.harga_jual = updated_data.harga_jual
    if updated_data.kategori is not None:    
        produk.kategori = updated_data.kategori
    if updated_data.status_penjualan is not None:    
        produk.status_penjualan = updated_data.status_penjualan
    if updated_data.perlu_resep is not None:    
        produk.perlu_resep = updated_data.perlu_resep
    
    db.commit()
    
    message = "Update data Produk by ID berhasil"
    return {"message": message,
            "data": {
                "tipe_produk": produk.tipe_produk,
                "nama_produk": produk.nama_produk,
                "sku": produk.sku,
                "nama_pabrik": produk.nama_pabrik,
                "barcode": produk.barcode,
                "rak": produk.rak,
                "gudang": produk.gudang,
                "satuan": produk.satuan,
                "referensi_harga_beli": produk.referensi_harga_beli,
                "harga_jual": produk.harga_jual,
                "kategori": produk.kategori,
                "status_penjualan": produk.status_penjualan,
                "perlu_resep": produk.perlu_resep,
            }}
