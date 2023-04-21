from sqlalchemy import Column, Integer, String

from src.infra.adapters.database.base import Base


class RolesModel(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
