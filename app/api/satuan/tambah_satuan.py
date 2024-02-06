import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.satuan import Satuan

class TambahSatuan(BaseModel):
    id_satuan: str
    nama_satuan: str

async def tambah_satuan(data: TambahSatuan, session=Depends(get_db_session)):
    # Additional validation or checks can be added here before adding to the database.
    
    satuan = Satuan(
        id_satuan=data.id_satuan,
        nama_satuan=data.nama_satuan,
    )

    session.add(satuan)
    session.commit()

    return Response(status_code=201)