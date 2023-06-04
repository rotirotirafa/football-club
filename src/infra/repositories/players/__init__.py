from typing import List

from sqlalchemy.orm import Session

from src.domain.v1.players.model import PlayersModel


class PlayersRepository:

    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_one(self, role_id: int):
        response = self.db.query(PlayersModel).get(role_id)
        return response

    def get_all(self) -> List[PlayersModel] or List:
        response = self.db.query(PlayersModel).all()
        return response
    #
    # def insert(self, role: RoleSchema) -> RoleSchema:
    #     create_object = RolesModel(
    #         name=role.name
    #     )
    #     self.db.add(create_object)
    #     self.db.commit()
    #     self.db.refresh(create_object)
    #     return create_object
    #
    # def update(self, role_id: int,  role: RoleUpdateSchemaRequest) -> RoleSchema:
    #     old_object = self.db.query(RolesModel).filter_by(role_id=role_id)
    #     old_object.update(
    #         {"name": role.name}
    #     )
    #     self.db.commit()
    #     return self.db.query(RolesModel).get(role_id)
    #
    # def delete(self, role_id: int):
    #     self.db.query(RolesModel).filter_by(role_id=role_id).delete()
    #     self.db.commit()
    #     return

