from sqlalchemy import Column, Integer, String, DECIMAL

from src.infra.adapters.database.base import Base


class PlansModel(Base):
    """Planos de Assinatura"""

    __tablename__ = "plans"

    plan_id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String(50), nullable=False)
    plan_description = Column(String(500), nullable=True)
    plan_price = Column(DECIMAL, nullable=False)
