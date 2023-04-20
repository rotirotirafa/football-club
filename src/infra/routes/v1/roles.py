from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.domain.v1.roles.schema import RoleSchema, RoleUpdateSchemaRequest
from src.domain.v1.usecases.roles import RolesUseCase
from src.infra.database.make_session import get_db

RolesRoute = APIRouter(
    prefix='/roles',
    tags=["Roles"],
)


@RolesRoute.get('/', response_model=List[RoleSchema])
def get_roles(db: Session = Depends(get_db)) -> List[RoleSchema]:
    roles_use_case = RolesUseCase(db)
    response = roles_use_case.get_all_roles()
    return response


@RolesRoute.post('/', response_model=RoleSchema)
def post_role(role: RoleSchema, db: Session = Depends(get_db)) -> Any:
    roles_use_case = RolesUseCase(db)
    response = roles_use_case.create_role(role)
    return response


@RolesRoute.get('/{role_id}', response_model=RoleSchema)
def get_role(role_id: int, db: Session = Depends(get_db)) -> RoleSchema:
    roles_use_case = RolesUseCase(db)
    response = roles_use_case.get_specific_role(role_id)
    return response


@RolesRoute.put('/{role_id}', response_model=RoleSchema)
def put_role(role_id: int, payload: RoleUpdateSchemaRequest, db: Session = Depends(get_db)) -> RoleSchema:
    roles_use_case = RolesUseCase(db)
    response = roles_use_case.update_specific_role(role_id, payload)
    return response


@RolesRoute.delete('/{role_id}')
def delete_role(role_id: int, db: Session = Depends(get_db)) -> ORJSONResponse:
    roles_use_case = RolesUseCase(db)
    roles_use_case.delete_role(role_id)
    return ORJSONResponse({'message': 'Deletado com sucesso'})
