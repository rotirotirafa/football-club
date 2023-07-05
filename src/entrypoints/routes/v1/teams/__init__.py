from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.infra.adapters.database.make_session import get_db
from src.schemas.teams import TeamSchema, TeamSchemaCreateRequest, TeamSchemaUpdate
from src.usecases.teams import TeamsUseCase
from src.utils.logs import Logs

TeamsRoute = APIRouter(
    prefix='/teams'
)


@TeamsRoute.get('/', response_model=List[TeamSchema])
def get_teams(db: Session = Depends(get_db)) -> List[TeamSchema] or None:
    try:
        teams_use_case = TeamsUseCase(db)
        return teams_use_case.get_all_teams()
    except HTTPException as ex:
        raise HTTPException(ex.status_code, ex.detail)

    except Exception as ex:
        raise ex


@TeamsRoute.get('/{team_id}')
def get_team(team_id: int, db: Session = Depends(get_db)) -> TeamSchema:
    try:
        teams_use_case = TeamsUseCase(db)
        response = teams_use_case.get_specific_team(team_id)
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


@TeamsRoute.post('/')
def create_team(team: TeamSchemaCreateRequest, db: Session = Depends(get_db)) -> TeamSchema:
    try:
        teams_use_case = TeamsUseCase(db)
        response = teams_use_case.create_team(team)
        return response
    except Exception as ex:
        raise ex


@TeamsRoute.put('/{team_id}', response_model=TeamSchema)
def update_team(team_id: int, payload: TeamSchemaUpdate, db: Session = Depends(get_db)) -> TeamSchema:
    try:
        teams_use_case = TeamsUseCase(db)
        response = teams_use_case.update_specific_team(team_id, payload)
        return response
    except Exception as ex:
        raise ex


@TeamsRoute.delete('/{team_id}')
def delete_team(team_id: int, db: Session = Depends(get_db)) -> ORJSONResponse:
    try:
        team_use_case = TeamsUseCase(db)
        team_use_case.delete_team(team_id)
        return ORJSONResponse({'message': 'Deletado com sucesso'})

    except HTTPException as ex:
        return ORJSONResponse({'message': ex.detail})

    except Exception as ex:
        raise ex
