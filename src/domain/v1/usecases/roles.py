from sqlalchemy.orm import Session

from src.domain.v1.roles.repository import RolesRepository
from src.domain.v1.roles.schema import RoleSchema


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

    def update_specific_role(self):
        pass

    def create_role(self, role: RoleSchema):
        return self.repository.insert(role)

    def delete_role(self, role_id: int):
        return self.repository.delete(role_id)
