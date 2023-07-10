from datetime import datetime

from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey

from src.domain.v1.team_management.teams import TeamsModel
from src.domain.v1.users.model import UsersModel
from src.infra.adapters.database.base import Base


class PlayersModel(Base):

    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True)

    nickname = Column(String(40))
    status = Column(String(40), nullable=True)
    image_url = Column(String(500), nullable=True)
    profile_desc = Column(Text, nullable=True)
    main_position = Column(String(30))
    secondary_position = Column(String(30))
    age = Column(Integer, nullable=True)
    signed = Column(Boolean, default=False)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
    # FK USER_ID, TEAM_ID, GOALS
    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    team_id = Column(ForeignKey("teams.team_id"), nullable=True)

    user = relationship(UsersModel, foreign_keys=[user_id])
    teams = relationship(TeamsModel, foreign_keys=[team_id])
