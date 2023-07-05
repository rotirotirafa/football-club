from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.infra.repositories.teams import TeamsRepository
from src.schemas.teams import TeamSchemaCreateRequest


class TeamsUseCase:
    #TODO
    """
    Tipar entradas e saídas
    Try catch com exception personalizada
    """

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = TeamsRepository(self.db)

    def get_all_teams(self):
        return self.repository.get_all()

    def get_specific_team(self, team_id: int):
        return self.repository.get_one(team_id)

    def update_specific_team(self, team_id: int, payload):
        return self.repository.update(team_id, payload)

    def create_team(self, team: TeamSchemaCreateRequest):
        return self.repository.insert(team)

    def delete_team(self, team_id: int):
        response = self.repository.delete(team_id)
        if response:
            return
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Time não encontrado')
