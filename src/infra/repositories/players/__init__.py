import datetime
from typing import List

from sqlalchemy.orm import Session

from src.domain.v1.players.model import PlayersModel
from src.schemas.players import PlayerSchema, PlayerSchemaInsertResponse, PlayerUpdateRequest


class PlayersRepository:

    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_one(self, player_id: int):
        response = self.db.query(PlayersModel).get(player_id)
        return response

    def get_all(self) -> List[PlayersModel] or List:
        response = self.db.query(PlayersModel).all()
        return response

    def insert(self, player: PlayerSchema) -> PlayerSchemaInsertResponse:
        create_object = PlayersModel(
            nickname=player.nickname,
            status=player.status,
            image_url=player.image_url,
            profile_desc=player.profile_desc,
            main_position=player.main_position,
            secondary_position=player.secondary_position,
            signed=player.signed,
            created_date=datetime.datetime.now(),
            updated_date=datetime.datetime.now(),
            user_id=player.user_id,
            team_id=player.team_id
        )
        self.db.add(create_object)
        self.db.commit()
        self.db.refresh(create_object)
        return create_object

    def update(self, player_id: int,  payload: PlayerUpdateRequest) -> PlayerUpdateRequest:
        old_object = self.db.query(PlayersModel).filter_by(player_id=player_id)
        actual_user_data = old_object[0]
        old_object.update(
            {
                "player_id": payload.player_id or actual_user_data.player_id,
                "nickname":  payload.nickname or actual_user_data.nickname,
                "status": payload.status or actual_user_data.status,
                "image_url": payload.image_url or actual_user_data.image_url,
                "profile_desc": payload.profile_desc or actual_user_data.profile_desc,
                "main_position": payload.main_position or actual_user_data.main_position,
                "secondary_position": payload.secondary_position or actual_user_data.secondary_position,
                "signed": payload.signed or actual_user_data.signed,
                "team_id": payload.team_id or actual_user_data.team_id,
                "updated_date": datetime.datetime.now()
            }
        )
        self.db.commit()
        return old_object[0]

    def delete(self, player_id: int):
        self.db.query(PlayersModel).filter_by(player_id=player_id).delete()
        self.db.commit()
        return

