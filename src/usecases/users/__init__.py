from sqlalchemy.orm import Session

from src.infra.repositories.users import UsersRepository
from src.schemas.users import UsersSchema, UserSchemaUpdateRequest


class UsersUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = UsersRepository(self.db)

    def get_all_users(self):
        try:
            return self.repository.get_all()
        except Exception as ex:
            print(ex)
            raise ex

    def get_one_user(self, user_id: int):
        try:
            return self.repository.get_one(user_id)
        except Exception as ex:
            print(ex)
            raise ex

    def create_user(self, payload: UsersSchema):
        try:
            return self.repository.insert(payload)
        except Exception as ex:
            print(ex)
            raise ex

    def update_user(self, user_id: int, payload: UserSchemaUpdateRequest):
        try:
            return self.repository.update(user_id, payload)
        except Exception as ex:
            print(ex)
            raise ex

    def delete_user(self, user_id: int):
        try:
            return self.repository.delete(user_id)
        except Exception as ex:
            print(ex)
            raise ex
