from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.infra.adapters.database.make_session import get_db
from src.schemas.players import PlayerSchema, PlayerSchemaInsertResponse, PlayerUpdateRequest
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


@PlayersRoute.post('/', response_model=PlayerSchemaInsertResponse)
def post_role(player: PlayerSchema, db: Session = Depends(get_db)) -> PlayerSchemaInsertResponse:
    try:
        player_use_case = PlayersUseCase(db)
        response = player_use_case.create_player(player)
        return response
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisicao: post_role',
            exception=str(ex)
        )
        logs.error()
        raise ex


@PlayersRoute.get('/{player_id}', response_model=PlayerSchema or HTTPException)
def get_player(player_id: int, db: Session = Depends(get_db)) -> PlayerSchema or HTTPException:
    try:
        player_use_case = PlayersUseCase(db)
        response = player_use_case.get_one_player(player_id)
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Usuário não encontrado na base de dados"
            )
        return response
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: get_role',
            exception=str(ex)
        )
        logs.error()
        raise ex


@PlayersRoute.put('/{player_id}', response_model=PlayerUpdateRequest)
def put_role(player_id: int, payload: PlayerUpdateRequest, db: Session = Depends(get_db)) -> PlayerUpdateRequest:
    try:
        use_case = PlayersUseCase(db)
        response = use_case.update_player(player_id, payload)
        return response
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: put_role',
            exception=str(ex)
        )
        logs.error()
        raise ex


@PlayersRoute.delete('/{player_id}')
def delete_role(player_id: int, db: Session = Depends(get_db)) -> ORJSONResponse:
    try:
        use_case = PlayersUseCase(db)
        use_case.delete_player(player_id)
        return ORJSONResponse({'message': 'Deletado com sucesso'})
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: delete_role',
            exception=str(ex)
        )
        logs.error()
        raise ex
