from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from src.infra.adapters.database.base import Base


class LineUpsModel(Base):

    __tablename__ = "lineups"

    lineup_id = Column(Integer, primary_key=True, index=False)

    match_id = Column(ForeignKey("matches.match_id"))

    formation = Column(String(10))

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
