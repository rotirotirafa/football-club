from sqlalchemy import Column, Integer, String
from src.database import Base


class Roles(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    