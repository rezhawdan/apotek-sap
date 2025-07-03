from fastapi import FastAPI
from app.routes import user, auth
from app.middleware.logging import log_requests

app = FastAPI()

app.middleware('http')(log_requests)
app.include_router(user.router, prefix="/api")
app.include_router(auth.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FastAPI is Running!!!"}
