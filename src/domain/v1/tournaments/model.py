from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from src.infra.adapters.database.base import Base


class TournamentsModel(Base):
    __tablename__ = "tournaments"

    tournament_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(60))
    image_url = Column(String(500), nullable=True)
    active = Column(Boolean, default=True, nullable=False)

    model = Column(String(500), nullable=True)

    team_winner = Column(Integer, nullable=True)
    team_vice = Column(Integer, nullable=True)
    team_third = Column(Integer, nullable=True)

    prize = Column(String(250), nullable=True)
    initial_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)

