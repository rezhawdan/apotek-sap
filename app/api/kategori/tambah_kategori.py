import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.kategori import Kategori

class TambahKategori(BaseModel):
    code_kategori: str
    nama_kategori: str

async def tambah_kategori(data: TambahKategori, session=Depends(get_db_session)):
    kategori = Kategori(
        code_kategori=data.code_kategori,
        nama_kategori=data.nama_kategori,
    )

    session.add(kategori)
    session.commit()

    message = 'Data Kategori berhasil dibuat.'
    return {'message': message,
            'data': {
                'code_kategori': kategori.code_kategori,
                'nama_kategori': kategori.nama_kategori
            }}