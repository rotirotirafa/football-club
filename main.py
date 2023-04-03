from src.database import SessionLocal, engine
from src.models.roles import Roles as RolesModel
from src.schemas.roles import Roles as RolesSchema
from sqlalchemy.orm import session
from sqlalchemy import MetaData
from typing import Callable, Iterator
from contextlib import AbstractContextManager
from fastapi import Depends

from sqlalchemy.orm import Session

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

datadb = get_db()

def create_role(role: RolesSchema, database: Session):
    db_user = RolesModel(name=role.name)
    database.add(db_user)
    database.commit()
    return 'Ok'

create_role(role=RolesSchema(name="teste"), database=datadb)