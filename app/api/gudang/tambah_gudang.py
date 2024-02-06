import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.gudang import Gudang

class TambahGudang(BaseModel):
    id_gudang: str
    nama_gudang: str

async def tambah_gudang(data: TambahGudang, session=Depends(get_db_session)):
    # Additional validation or checks can be added here before adding to the database.
    
    gudang = Gudang(
        id_gudang=data.id_gudang,
        nama_gudang=data.nama_gudang,
    )

    session.add(gudang)
    session.commit()

    return Response(status_code=201)