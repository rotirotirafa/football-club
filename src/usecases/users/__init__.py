from sqlalchemy.orm import Session

from src.infra.repositories.users import UsersRepository


class UsersUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = UsersRepository(self.db)

    def get_all_users(self):
        self.repository.get_all()
