import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.get_db_session import get_db_session
from app.models.kategori import Kategori


def get_kategori(db: Session = Depends(get_db_session)):
    get_kategori = db.query(
        Kategori.id_kategori,
        Kategori.code_kategori,
        Kategori.nama_kategori
    ).all()

    message = "GET All data kategori berhasil."
    return {"message": message, "data": get_kategori}
