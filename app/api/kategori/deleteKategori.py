from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.kategori import Kategori


def deleteKategori(kategori_id: str, db: Session = Depends(get_db_session)):
    kategori = db.query(Kategori).filter(Kategori.id_kategori == kategori_id).first()
    if kategori is None:
        raise HTTPException(
            status_code=404,
            detail="Data Kategori berdasarkan ID tidak ditemukan."
        )

    db.delete(kategori)
    db.commit()

    message = "Data Kategori berhasil dihapus."
    return {"message": message}
