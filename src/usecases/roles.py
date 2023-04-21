from sqlalchemy.orm import Session

from src.domain.v1.roles.repository import RolesRepository
from src.domain.v1.roles.schema import RoleSchema


class RolesUseCase:
    #TODO
    """
    Tipar entradas e saídas
    Try catch com exception personalizada
    """

    def __init__(self,):
        self.db = get_db()
        self.repository = RolesRepository(self.db)

    async def get_all_roles(self):
        async with session() as session:
            items = await get_by_criteria(query, session)
    
        return self.repository.get_all()

    async def get_specific_role(self, role_id: int):
        return self.repository.get_one(role_id)

    async def update_specific_role(self, role_id: int, payload):
        return self.repository.update(role_id, payload)

    async def create_role(self, role: RoleSchema):
        return self.repository.insert(role)

    async def delete_role(self, role_id: int):
        return self.repository.delete(role_id)
