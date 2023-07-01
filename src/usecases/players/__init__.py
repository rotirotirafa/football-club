from sqlalchemy.orm import Session

from src.infra.repositories.players import PlayersRepository
from src.schemas.players import PlayerSchema, PlayerSchemaInsertResponse, PlayerUpdateRequest


class PlayersUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = PlayersRepository(self.db)

    def get_all_players(self):
        return self.repository.get_all()

    def get_one_player(self, player_id: int) -> PlayerSchema:
        return self.repository.get_one(player_id)

    def create_player(self, payload: PlayerSchema) -> PlayerSchemaInsertResponse:
        return self.repository.insert(payload)

    def update_player(self, player_id: int, payload: PlayerUpdateRequest):
        return self.repository.update(player_id, payload)

    def delete_player(self, player_id: int):
        return self.repository.delete(player_id)
