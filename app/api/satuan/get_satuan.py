import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.get_db_session import get_db_session
from app.models.satuan import Satuan

def get_satuan(db: Session = Depends(get_db_session)):
    get_satuan = db.query(
        Satuan.id_satuan, 
        Satuan.nama_satuan
    ).all()
    message  = "GET All data satuan berhasil."
    return {"message": message, "data": get_satuan}
