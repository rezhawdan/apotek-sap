import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.gudang import Gudang


class TambahGudang(BaseModel):
    code_gudang: str
    nama_gudang: str


async def tambah_gudang(data: TambahGudang, session=Depends(get_db_session)):
    gudang = Gudang(
        code_gudang=data.code_gudang,
        nama_gudang=data.nama_gudang,
    )

    session.add(gudang)
    session.commit()

    message = 'Data Gudang berhasil dibuat.'
    return {'message': message,
            'data': {
                'code_gudang': gudang.code_gudang,
                'nama_gudang': gudang.nama_gudang
            }}
    
