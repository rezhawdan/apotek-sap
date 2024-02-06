import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.kategori import Kategori

class TambahKategori(BaseModel):
    id_kategori: str
    nama_kategori: str

async def tambah_kategori(data: TambahKategori, session=Depends(get_db_session)):
    # Additional validation or checks can be added here before adding to the database.
    
    kategori = Kategori(
        id_kategori=data.id_kategori,
        nama_kategori=data.nama_kategori,
    )

    session.add(kategori)
    session.commit()

    return Response(status_code=201)