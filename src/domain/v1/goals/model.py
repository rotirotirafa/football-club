from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime

from src.infra.adapters.database.base import Base


class GoalsModel(Base):

    __tablename__ = "goals"

    goal_id = Column(Integer, primary_key=True, index=True)

    match_id = Column(ForeignKey("matches.match_id"))
    player_id = Column(ForeignKey("players.player_id"))

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
