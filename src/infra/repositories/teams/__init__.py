import datetime
from typing import List

from sqlalchemy.orm import Session

from src.domain.v1.teams.model import TeamsModel
from src.schemas.teams import TeamSchema, TeamSchemaCreateRequest, TeamSchemaUpdate


class TeamsRepository:

    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_one(self, role_id: int):
        response = self.db.query(TeamsModel).get(role_id)
        return response

    def get_all(self) -> List[TeamsModel] or List:
        response = self.db.query(TeamsModel).all()
        return response

    def insert(self, team: TeamSchemaCreateRequest) -> TeamSchema:
        create_object = TeamsModel(
            name=team.name,
            image_url=team.image_url,
            profile_desc=team.profile_desc,
            created_date=datetime.datetime.now(),
            updated_date=datetime.datetime.now()
        )
        self.db.add(create_object)
        self.db.commit()
        self.db.refresh(create_object)
        return create_object

    def update(self, team_id: int,  team: TeamSchemaUpdate) -> TeamSchema:
        old_object = self.db.query(TeamsModel).filter_by(team_id=team_id)
        actual_user_data = old_object[0]
        old_object.update(
            {
                "name": team.name or actual_user_data.name,
                "image_url": team.image_url or actual_user_data.image_url,
                "profile_desc": team.profile_desc or actual_user_data.profile_desc,
                "updated_date": datetime.datetime.now()
            }
        )
        self.db.commit()
        return old_object[0]

    def delete(self, team_id: int) -> bool:
        team = self.db.query(TeamsModel).filter_by(team_id=team_id)
        if team.one_or_none():
            team.delete()
            self.db.commit()
            return True
        return False
