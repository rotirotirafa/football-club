from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.infra.adapters.database.make_session import get_db
from src.schemas.role import RoleSchema, RoleUpdateSchemaRequest
from src.usecases.roles import RolesUseCase
from src.utils.logs import Logs

RolesRoute = APIRouter(
    prefix='/roles'
)


@RolesRoute.get('/', response_model=List[RoleSchema])
def get_roles(db: Session = Depends(get_db)) -> List[RoleSchema]:
    try:
        roles_use_case = RolesUseCase(db)
        return roles_use_case.get_all_roles()
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: get_roles',
            exception=str(ex)
        )
        logs.error()
        raise ex


@RolesRoute.post('/', response_model=RoleSchema)
def post_role(role: RoleSchema, db: Session = Depends(get_db)) -> Any:
    try:
        roles_use_case = RolesUseCase(db)
        response = roles_use_case.create_role(role)
        return response
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisicao: post_role',
            exception=str(ex)
        )
        logs.error()
        raise ex


@RolesRoute.get('/{role_id}', response_model=RoleSchema)
def get_role(role_id: int, db: Session = Depends(get_db)) -> RoleSchema:
    try:
        roles_use_case = RolesUseCase(db)
        response = roles_use_case.get_specific_role(role_id)
        return response
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: get_role',
            exception=str(ex)
        )
        logs.error()
        raise ex


@RolesRoute.put('/{role_id}', response_model=RoleSchema)
def put_role(role_id: int, payload: RoleUpdateSchemaRequest, db: Session = Depends(get_db)) -> RoleSchema:
    try:
        roles_use_case = RolesUseCase(db)
        response = roles_use_case.update_specific_role(role_id, payload)
        return response
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: put_role',
            exception=str(ex)
        )
        logs.error()
        raise ex


@RolesRoute.delete('/{role_id}')
def delete_role(role_id: int, db: Session = Depends(get_db)) -> ORJSONResponse:
    try:
        roles_use_case = RolesUseCase(db)
        roles_use_case.delete_role(role_id)
        return ORJSONResponse({'message': 'Deletado com sucesso'})
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: delete_role',
            exception=str(ex)
        )
        logs.error()
        raise ex
