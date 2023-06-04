from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.infra.adapters.database.make_session import get_db
from src.schemas.players import PlayerSchema
from src.usecases.players import PlayersUseCase
from src.utils.logs import Logs

PlayersRoute = APIRouter(
    prefix='/players',
    tags=["Players"],
)


@PlayersRoute.get('/', response_model=List[PlayerSchema])
def get_players(db: Session = Depends(get_db)) -> List[PlayerSchema] or None:
    try:
        players_usecase = PlayersUseCase(db)
        return players_usecase.get_all_players()
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: get_roles',
            exception=str(ex)
        )
        logs.error()
        raise ex

#
# @PlayersRoute.post('/', response_model=RoleSchema)
# def post_role(role: RoleSchema, db: Session = Depends(get_db)) -> Any:
#     try:
#         roles_use_case = RolesUseCase(db)
#         response = roles_use_case.create_role(role)
#         return response
#     except Exception as ex:
#         logs = Logs(
#             code=1000,
#             message='Erro ao processar a requisicao: post_role',
#             exception=str(ex)
#         )
#         logs.error()
#         raise ex
#
#
# @PlayersRoute.get('/{role_id}', response_model=RoleSchema)
# def get_role(role_id: int, db: Session = Depends(get_db)) -> RoleSchema:
#     try:
#         roles_use_case = RolesUseCase(db)
#         response = roles_use_case.get_specific_role(role_id)
#         return response
#     except Exception as ex:
#         logs = Logs(
#             code=1000,
#             message='Erro ao processar a requisição: get_role',
#             exception=str(ex)
#         )
#         logs.error()
#         raise ex
#
#
# @PlayersRoute.put('/{role_id}', response_model=RoleSchema)
# def put_role(role_id: int, payload: RoleUpdateSchemaRequest, db: Session = Depends(get_db)) -> RoleSchema:
#     try:
#         roles_use_case = RolesUseCase(db)
#         response = roles_use_case.update_specific_role(role_id, payload)
#         return response
#     except Exception as ex:
#         logs = Logs(
#             code=1000,
#             message='Erro ao processar a requisição: put_role',
#             exception=str(ex)
#         )
#         logs.error()
#         raise ex
#
#
# @PlayersRoute.delete('/{role_id}')
# def delete_role(role_id: int, db: Session = Depends(get_db)) -> ORJSONResponse:
#     try:
#         roles_use_case = RolesUseCase(db)
#         roles_use_case.delete_role(role_id)
#         return ORJSONResponse({'message': 'Deletado com sucesso'})
#     except Exception as ex:
#         logs = Logs(
#             code=1000,
#             message='Erro ao processar a requisição: delete_role',
#             exception=str(ex)
#         )
#         logs.error()
#         raise ex
