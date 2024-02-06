import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator
from app.dependencies.get_db_session import get_db_session
from app.models.rak import Rak

class TambahRak(BaseModel):
    id_rak: str
    daftar_rak: str

async def tambah_rak(data: TambahRak, session=Depends(get_db_session)):
    # Additional validation or checks can be added here before adding to the database.
    
    rak = Rak(
        id_rak=data.id_rak,
        daftar_rak=data.daftar_rak,
    )

    session.add(rak)
    session.commit()

    return Response(status_code=201)