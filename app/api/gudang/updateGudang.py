from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.gudang import Gudang
from pydantic import BaseModel


class UpdateGudangData(BaseModel):
    nama_gudang: str


def updateGudang(gudang_id: str, updated_data: UpdateGudangData, db: Session = Depends(get_db_session)):
    gudang = db.query(Gudang).filter(Gudang.id_gudang == gudang_id).first()
    if gudang is None:
        raise HTTPException(status_code=404, detail="Data Gudang by ID tidak ditemukan.")
    
    gudang.nama_gudang = updated_data.nama_gudang
    
    db.commit()
    
    message = "Update data Gudang by ID berhasil"
    return {"message": message, "data": updated_data.dict()}
