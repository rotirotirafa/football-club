from datetime import datetime

from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.domain.v1.subscriptions.model import SubscriptionsModel
from src.infra.adapters.database.base import Base


class InvoicesModel(Base):
    """Faturas"""

    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(32), nullable=False)  # UUID (32 chars)
    amount = Column(DECIMAL, nullable=False)
    payment_status = Column(String(50), nullable=False)  # TODO Enum
    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    payment_date = Column(DateTime, nullable=True)

    subscription_id = Column(ForeignKey("subscriptions.subscription_id"), nullable=True)

    subscription = relationship(SubscriptionsModel, foreign_keys=[subscription_id])
