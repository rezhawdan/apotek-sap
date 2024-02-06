import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.produk import Produk

class ProductRegistrationData(BaseModel):
    tipe_produk: str
    nama_produk: str
    sku: str
    nama_pabrik: str
    barcode: str
    rak: str
    satuan_utama: str
    gudang: str
    referensi_harga_beli: int
    harga_jual: int
    kategori: str
    status_penjualan: str
    perlu_resep: str

async def tambah_produk(data: ProductRegistrationData, session=Depends(get_db_session)):
    # Additional validation or checks can be added here before adding to the database.
    
    product = Produk(
        tipe_produk=data.tipe_produk,
        nama_produk=data.nama_produk,
        sku=data.sku,
        nama_pabrik=data.nama_pabrik,
        barcode=data.barcode,
        rak=data.rak,
        satuan_utama=data.satuan_utama,
        gudang=data.gudang,
        referensi_harga_beli=data.referensi_harga_beli,
        harga_jual=data.harga_jual,
        kategori=data.kategori,
        status_penjualan=data.status_penjualan,
        perlu_resep=data.perlu_resep
    )

    session.add(product)
    session.commit()

    return Response(status_code=201)
