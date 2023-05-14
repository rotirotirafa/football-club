from datetime import datetime

from sqlalchemy import DateTime, Column, Integer, ForeignKey

from src.infra.adapters.database.base import Base


class MatchesModel(Base):

    __tablename__ = "matches"

    match_id = Column(Integer, primary_key=True, index=True)

    team_home_id = Column(ForeignKey("teams.team_id"), nullable=False)
    team_away_id = Column(ForeignKey("teams.team_id"), nullable=False)
    tournament_id = Column(ForeignKey("tournaments.tournament_id"), nullable=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
