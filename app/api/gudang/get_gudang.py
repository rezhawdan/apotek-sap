import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.get_db_session import get_db_session
from app.models.gudang import Gudang

def get_gudang(db: Session = Depends(get_db_session)):
    get_gudang = db.query(
        Gudang.id_gudang, 
        Gudang.nama_gudang
    ).all()
    message = "GET All data kategori berhasil."
    return {"message": message, "data": get_gudang}
