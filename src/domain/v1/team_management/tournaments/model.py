from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from src.infra.adapters.database.base import Base


class TournamentsModel(Base):
    __tablename__ = "tournaments"

    tournament_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(45))
    image_url = Column(String(500))
    active = Column(Boolean, default=True, nullable=False)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)

