from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from src.infra.adapters.database.base import Base


class TeamsModel(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(45))
    image_url = Column(String(500), nullable=True)
    profile_desc = Column(Text, nullable=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
    updated_date = Column(DateTime, default=datetime.now(), nullable=True)
