import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak

class TambahRak(BaseModel):
    code_rak: str
    nama_rak: str

async def tambah_rak(data: TambahRak, session=Depends(get_db_session)):
    rak = Rak(
        code_rak=data.code_rak,
        nama_rak=data.nama_rak,
    )

    session.add(rak)
    session.commit()

    message = 'Data Rak berhasil dibuat.'
    return {'message': message,
            'data': {
                'code_rak': rak.code_rak,
                'nama_rak': rak.nama_rak
            }}