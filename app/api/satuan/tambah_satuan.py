import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.satuan import Satuan

class TambahSatuan(BaseModel):
    code_satuan: str
    nama_satuan: str

async def tambah_satuan(data: TambahSatuan, session=Depends(get_db_session)):
    satuan = Satuan(
        code_satuan=data.code_satuan,
        nama_satuan=data.nama_satuan,
    )

    session.add(satuan)
    session.commit()

    message = 'Data Satuan berhasil dibuat.'
    return {'message': message,
            'data': {
                'code_satuan': satuan.code_satuan,
                'nama_satuan': satuan.nama_satuan
            }}
    