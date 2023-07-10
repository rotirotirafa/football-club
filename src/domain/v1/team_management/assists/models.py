from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime

from src.infra.adapters.database.base import Base


class AssistsModel(Base):

    __tablename__ = "assists"

    assist_id = Column(Integer, primary_key=True, index=True)

    match_id = Column(ForeignKey("matches.match_id"), nullable=True)
    player_id = Column(ForeignKey("players.player_id"), nullable=False)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
