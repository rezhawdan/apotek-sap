from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.get_db_session import get_db_session
from app.models.produk import Produk


def deleteProduk(produk_id: int, db: Session = Depends(get_db_session)):
    produk = db.query(Produk).filter(Produk.id == produk_id).first()
    if produk is None:
        raise HTTPException(
            status_code=404,
            detail="Data Produk berdasarkan ID tidak ditemukan."
        )

    db.delete(produk)
    db.commit()

    message = "Data Produk berhasil dihapus."
    return {"message": message}
