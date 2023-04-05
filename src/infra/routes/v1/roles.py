from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.domain.v1.roles.schema import RoleSchema
from src.domain.v1.usecases.roles import RolesUseCase
from src.infra.database.make_session import get_db

RolesRoute = APIRouter(
    prefix='/roles',
    tags=["Roles"],
)


@RolesRoute.get('/', response_model=List[RoleSchema])
def get_roles(db: Session = Depends(get_db)) -> List[RoleSchema]:
    """
    db = Sessão do Banco de Dados
    response = [{"id": x, "name": "xpto"}, ...]
    """
    roles_use_case = RolesUseCase(db)
    response = roles_use_case.get_all_roles()
    return response


@RolesRoute.get('/{role_id}')
def get_role(role_id: int) -> ORJSONResponse:
    return ORJSONResponse(role_id)


@RolesRoute.post('/', response_model=RoleSchema)
def post_role(role: RoleSchema, db: Session = Depends(get_db)) -> Any:
    roles_use_case = RolesUseCase(db)
    response = roles_use_case.create_role(role)
    return response


@RolesRoute.put('/')
def put_role():
    pass


@RolesRoute.delete('/')
def delete_role():
    pass
