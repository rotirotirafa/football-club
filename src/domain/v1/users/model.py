from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, DateTime

from src.domain.v1.roles.model import RolesModel
from src.infra.adapters.database.base import Base


class UsersModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=60), nullable=False)
    email = Column(String(length=255), nullable=False, unique=True)
    phone = Column(String(length=15), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    status = Column(String(length=30))
    active = Column(Boolean, default=True, nullable=False)
    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)

    role_id = Column(ForeignKey("roles.role_id"), nullable=False)

    roles = relationship(RolesModel, foreign_keys=[role_id])
