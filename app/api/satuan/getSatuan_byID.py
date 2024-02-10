from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.satuan import Satuan


def getSatuan_byID(satuan_id: str, db: Session = Depends(get_db_session)):
    satuan = db.query(Satuan).filter(Satuan.id_satuan == satuan_id).first()
    if satuan is None:
        raise HTTPException(
            status_code=404, detail="Data Satuan by ID tidak ditemukan.")

    satuan_data = {
        'id_satuan': satuan.id_satuan,
        'code_satuan': satuan.code_satuan,
        'nama_satuan': satuan.nama_satuan
    }
    
    message = 'GET data Satuan by ID berhasil'
    return {'message': message, 'data': satuan_data}
