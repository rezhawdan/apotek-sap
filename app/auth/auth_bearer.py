from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decode_access_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            try:
                payload = decode_access_token(credentials.credentials)
                return payload
            except:
                raise HTTPException(status_code=403, detail="Invalid or expired token")
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
