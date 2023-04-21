from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.domain.v1.roles.schema import RoleSchema, RoleUpdateSchemaRequest
from src.domain.v1.usecases.roles import RolesUseCase
from src.infra.databases.make_session import get_db

router = APIRouter()

@router.get(path='', name='Listagem de cargos',status_code=HTTP_Status.OK, response_model=List[RoleSchema])
async def _get_roles(db: Session = Depends(get_db)) -> List[RoleSchema]:
    roles_use_case = RolesUseCase(db)
    response = await roles_use_case.get_all_roles()
    return response


@router.post('/', name='Criar cargo',status_code=HTTP_Status.OK, response_model=RoleSchema)
async def _create_role(role: RoleSchema, db: Session = Depends(get_db)) -> Any:
    roles_use_case = RolesUseCase(db)
    response = await roles_use_case.create_role(role)
    return response


@router.get('/{role_id}', name='Busca um cargo através do id' response_model=RoleSchema)
async def _get_role(role_id: int, db: Session = Depends(get_db)) -> RoleSchema:
    roles_use_case = RolesUseCase(db)
    response = await roles_use_case.get_specific_role(role_id)
    return response


@router.put('/{role_id}', response_model=RoleSchema)
async def _update_role(role_id: int, payload: RoleUpdateSchemaRequest, db: Session = Depends(get_db)) -> RoleSchema:
    roles_use_case = RolesUseCase(db)
    response = await roles_use_case.update_specific_role(role_id, payload)
    return response


@router.delete('/{role_id}')
async def _delete_role(role_id: int, db: Session = Depends(get_db)) -> None:
    roles_use_case = RolesUseCase(db)
    await roles_use_case.delete_role(role_id)
