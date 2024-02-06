import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak

def get_rak(db: Session = Depends(get_db_session)):
    get_rak = db.query(
        Rak.id_rak, 
        Rak.daftar_rak
    ).all()
    message = "GET All data rak berhasil."
    return {"message": message, "data": get_rak}
