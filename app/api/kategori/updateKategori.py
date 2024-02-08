from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.kategori import Kategori
from pydantic import BaseModel


class UpdateKategoriData(BaseModel):
    nama_kategori: str


def updateKategori(kategori_id: str, updated_data: UpdateKategoriData, db: Session = Depends(get_db_session)):
    kategori = db.query(Kategori).filter(Kategori.id_kategori == kategori_id).first()
    if kategori is None:
        raise HTTPException(status_code=404, detail="Data Kategori by ID tidak ditemukan.")
    
    kategori.nama_kategori = updated_data.nama_kategori
    
    db.commit()
    
    message = "Update data Kategori by ID berhasil"
    return {"message": message, "data": updated_data.dict()}
