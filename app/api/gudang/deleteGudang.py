from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.gudang import Gudang


def deleteGudang(gudang_id: str, db: Session = Depends(get_db_session)):
    gudang = db.query(Gudang).filter(Gudang.id_gudang == gudang_id).first()
    if gudang is None:
        raise HTTPException(
            status_code=404,
            detail="Data Gudang berdasarkan ID tidak ditemukan."
        )

    db.delete(gudang)
    db.commit()

    message = "Data Gudang berhasil dihapus."
    return {"message": message}
