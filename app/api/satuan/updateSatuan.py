from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.satuan import Satuan
from pydantic import BaseModel


class UpdateSatuanData(BaseModel):
    nama_satuan: str


def updateSatuan(satuan_id: str, updated_data: UpdateSatuanData, db: Session = Depends(get_db_session)):
    satuan = db.query(Satuan).filter(Satuan.id_satuan == satuan_id).first()
    if satuan is None:
        raise HTTPException(status_code=404, detail="Data Satuan by ID tidak ditemukan.")
    
    satuan.nama_satuan = updated_data.nama_satuan
    
    db.commit()
    
    message = "Update data Satuan by ID berhasil"
    return {"message": message, "data": updated_data.dict()}
