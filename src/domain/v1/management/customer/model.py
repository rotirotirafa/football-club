from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from src.domain.v1.users.model import UsersModel
from src.infra.adapters.database.base import Base


class CustomersModel(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=True)
    image_url = Column(String(500), nullable=True)
    document = Column(String(11), nullable=True)
    cnpj = Column(String(14), nullable=True)
    active = Column(Boolean, default=True, nullable=True)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)

    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    user = relationship(UsersModel, foreign_keys=[user_id])
