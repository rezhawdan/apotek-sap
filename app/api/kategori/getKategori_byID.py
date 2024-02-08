from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.kategori import Kategori


def getKategori_byID(kategori_id: str, db: Session = Depends(get_db_session)):
    kategori = db.query(Kategori).filter(Kategori.id_kategori == kategori_id).first()
    if kategori is None:
        raise HTTPException(
            status_code=404, detail="Data kategori by ID tidak ditemukan.")

    kategori_data = {
        'id_kategori': kategori.id_kategori,
        'nama_kategori': kategori.nama_kategori
    }
    message = 'GET data kategori by ID berhasil'
    return {'message': message, 'data': kategori_data}
