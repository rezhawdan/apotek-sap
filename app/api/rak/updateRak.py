from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak
from pydantic import BaseModel


class UpdateRakData(BaseModel):
    code_rak: str = None
    nama_rak: str = None


def updateRak(rak_id: str, updated_data: UpdateRakData, db: Session = Depends(get_db_session)):
    rak = db.query(Rak).filter(Rak.id_rak == rak_id).first()
    if rak is None:
        raise HTTPException(
            status_code=404, detail="Data Rak by ID tidak ditemukan.")

    if updated_data.code_rak is not None:
        rak.code_rak = updated_data.code_rak
    if updated_data.nama_rak is not None:
        rak.nama_rak = updated_data.nama_rak

    db.commit()

    message = "Update data Kategori by ID berhasil"
    return {"message": message,
            "data": {
                "code_rak": rak.code_rak,
                "nama_kategori": rak.nama_rak
            }}
