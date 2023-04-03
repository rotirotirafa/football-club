from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

SQLALCHEMY_DATABASE_URL = URL.create(
    'mysql+pymysql',
    username='user',
    password='password',
    host='localhost',
    port=3306,
    database='football-club'
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
print(engine)
