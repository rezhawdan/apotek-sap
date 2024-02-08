from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.satuan import Satuan


def deleteSatuan(satuan_id: str, db: Session = Depends(get_db_session)):
    satuan = db.query(Satuan).filter(Satuan.id_satuan == satuan_id).first()
    if satuan is None:
        raise HTTPException(
            status_code=404,
            detail="Data Satuan berdasarkan ID tidak ditemukan."
        )

    db.delete(satuan)
    db.commit()

    message = "Data Satuan berhasil dihapus."
    return {"message": message}
