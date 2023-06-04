from sqlalchemy.orm import Session

from src.infra.repositories.players import PlayersRepository


class PlayersUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = PlayersRepository(self.db)

    def get_all_players(self):
        self.repository.get_all()
