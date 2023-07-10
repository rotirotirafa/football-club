from sqlalchemy import Column, Integer, String, DECIMAL

from src.infra.adapters.database.base import Base


class PlansModel(Base):
    """Planos de Assinatura"""

    __tablename__ = "plans"

    plan_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(DECIMAL, nullable=False)
