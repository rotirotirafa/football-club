from sqlalchemy.orm import Session

from src.infra.repositories.role import RolesRepository
from src.schemas.role import RoleSchema


class RolesUseCase:
    #TODO
    """
    Tipar entradas e saídas
    Try catch com exception personalizada
    """

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = RolesRepository(self.db)

    def get_all_roles(self):
        return self.repository.get_all()

    def get_specific_role(self, role_id: int):
        return self.repository.get_one(role_id)

    def update_specific_role(self, role_id: int, payload):
        return self.repository.update(role_id, payload)

    def create_role(self, role: RoleSchema):
        return self.repository.insert(role)

    def delete_role(self, role_id: int):
        return self.repository.delete(role_id)
