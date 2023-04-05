from sqlalchemy.orm import Session

from src.domain.v1.roles.model import RolesModel
from src.domain.v1.roles.schema import RoleSchema


class RolesRepository:

    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_one(self):
        pass

    def get_all(self):
        response = self.db.query(RolesModel).all()
        return response

    def insert(self, role: RoleSchema) -> RoleSchema:
        create_object = RolesModel(
            name=role.name
        )
        self.db.add(create_object)
        self.db.commit()
        self.db.refresh(create_object)
        return create_object

    def update(self):
        pass

    def delete(self):
        pass
