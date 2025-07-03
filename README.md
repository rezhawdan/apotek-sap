## install
pip install "fastapi[all]" sqlalchemy psycopg2-binary python-dotenv passlib[bcrypt] python-jose werkzeug

## membuat db sesuai model
from app.database import Base, engine
Base.metadata.create_all(bind=engine)

## running fastAPI
python -m uvicorn app.main:app --reload