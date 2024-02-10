from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak


def getRak_byID(rak_id: str, db: Session = Depends(get_db_session)):
    rak = db.query(Rak).filter(Rak.id_rak == rak_id).first()
    if rak is None:
        raise HTTPException(
            status_code=404, detail="Data Rak by ID tidak ditemukan.")

    rak_data = {
        'id_rak': rak.id_rak,
        'code_rak': rak.code_rak,
        'daftar_rak': rak.nama_rak
    }
    message = 'GET data rak by ID berhasil'
    return {'message': message, 'data': rak_data}
