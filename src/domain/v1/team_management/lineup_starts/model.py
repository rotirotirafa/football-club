from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, DateTime

from src.infra.adapters.database.base import Base


class LineUpStartsModel(Base):

    __tablename__ = "lineup_starts"

    lineup_start_id = Column(Integer, primary_key=True, index=True)

    lineup_id = Column(ForeignKey("lineups.lineup_id"), nullable=False)
    player_id = Column(ForeignKey("players.player_id"), nullable=False)
    """
    Mapper posições, X e Y do "campinho" no front
    """
    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
