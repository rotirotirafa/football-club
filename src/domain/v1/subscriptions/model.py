from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.domain.v1.customer.model import CustomersModel
from src.domain.v1.plans.model import PlansModel
from src.domain.v1.users.model import UsersModel
from src.infra.adapters.database.base import Base
from src.utils.functions import get_trial_date_expiration


class SubscriptionsModel(Base):
    """Assinaturas"""

    __tablename__ = "subscriptions"
    subscription_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=True)
    start_date = Column(DateTime, default=datetime.now(), nullable=True)
    expiration_date = Column(DateTime, default=get_trial_date_expiration(datetime.now()), nullable=True)
    # FK USER_ID
    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    customer_id = Column(ForeignKey("customers.customer_id"), nullable=True)
    plan_id = Column(ForeignKey("plans.plan_id"), nullable=True)

    # Relationships
    user = relationship(UsersModel, foreign_keys=[user_id])
    plan = relationship(PlansModel, foreign_keys=[plan_id])
    customer = relationship(CustomersModel, foreign_keys=[customer_id])
