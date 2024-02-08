from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak
from pydantic import BaseModel


class UpdateRakData(BaseModel):
    daftar_rak: str


def updateRak(rak_id: str, updated_data: UpdateRakData, db: Session = Depends(get_db_session)):
    rak = db.query(Rak).filter(Rak.id_rak == rak_id).first()
    if rak is None:
        raise HTTPException(status_code=404, detail="Data Rak by ID tidak ditemukan.")
    
    rak.daftar_rak = updated_data.daftar_rak
    
    db.commit()
    
    message = "Update data Rak by ID berhasil"
    return {"message": message, "data": updated_data.dict()}
