from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.domain.v1.players.model import PlayersModel
from src.domain.v1.schools.model import SchoolsModel
from src.infra.adapters.database.base import Base


class ClassPlayersModel(Base):

    __tablename__ = "classplayers"

    class_player_id = Column(Integer, primary_key=True, index=True)

    class_id = Column(ForeignKey("classes.class_id"), nullable=False)
    player_id = Column(ForeignKey("players.player_id"), nullable=False)

    classes = relationship(SchoolsModel, foreign_keys=[class_id])
    player = relationship(PlayersModel, foreign_keys=[player_id])
