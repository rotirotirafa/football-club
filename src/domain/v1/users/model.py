from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, DateTime

from src.infra.adapters.database.base import Base


class UsersModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    role_id = Column(ForeignKey("roles.role_id"), nullable=False)
    name = Column(String(length=60), nullable=False)
    email = Column(String(length=255), nullable=False)
    phone = Column(String(length=15), nullable=False)
    password = Column(Text, nullable=False)
    status = Column(String(length=30))
    active = Column(Boolean, default=True, nullable=False)
    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
