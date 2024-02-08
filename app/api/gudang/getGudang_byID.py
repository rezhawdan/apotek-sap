from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.gudang import Gudang


def getGudang_byID(gudang_id: str, db: Session = Depends(get_db_session)):
    gudang = db.query(Gudang).filter(Gudang.id_gudang == gudang_id).first()
    if gudang is None:
        raise HTTPException(
            status_code=404, detail="Data gudang by ID tidak ditemukan.")

    gudang_data = {
        'id_gudang': gudang.id_gudang,
        'nama_gudang': gudang.nama_gudang
    }
    message = 'GET data gudang by ID berhasil'
    return {'message': message, 'data': gudang_data}
