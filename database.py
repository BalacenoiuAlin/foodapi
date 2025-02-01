import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Încarcă variabilele din .env (doar pentru rulare locală)
load_dotenv()

# Citește DATABASE_URL din variabilele de mediu
DATABASE_URL = os.getenv("DATABASE_URL")

# Dacă folosești PostgreSQL, schimbă mysql+pymysql în postgresql+psycopg2
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")  # Fix pentru PostgreSQL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
