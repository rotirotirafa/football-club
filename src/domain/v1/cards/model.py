from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from src.infra.adapters.database.base import Base


class CardsModel(Base):

    __tablename__ = "cards"

    card_id = Column(Integer, primary_key=True, index=True)

    match_id = Column(ForeignKey("matches.match_id"))

    color = Column(String(1))  # Y or R

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
