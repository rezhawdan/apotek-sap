from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak


def deleteRak(rak_id: str, db: Session = Depends(get_db_session)):
    rak = db.query(Rak).filter(Rak.id_rak == rak_id).first()
    if rak is None:
        raise HTTPException(
            status_code=404,
            detail="Data Rak berdasarkan ID tidak ditemukan."
        )

    db.delete(rak)
    db.commit()

    message = "Data Rak berhasil dihapus."
    return {"message": message}
