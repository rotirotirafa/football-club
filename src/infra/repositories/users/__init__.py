import datetime
from typing import List

from sqlalchemy.orm import Session

from src.domain.v1.users.model import UsersModel
from src.schemas.users import UsersSchema, UserSchemaUpdateRequest


class UsersRepository:

    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_one(self, user_id: int):
        try:
            response = self.db.query(UsersModel).get(user_id)
            return response
        except Exception as ex:
            print(ex)
            raise ex

    def get_all(self) -> List[UsersModel] or List:
        try:
            response = self.db.query(UsersModel).all()
            return response
        except Exception as ex:
            print(ex)
            raise ex

    def insert(self, user_payload: UsersSchema) -> UsersSchema:
        try:
            create_object = UsersModel(
                name=user_payload.name,
                role_id=user_payload.role_id,
                email=user_payload.email,
                phone=user_payload.phone,
                password=user_payload.password,#TODO criptografar
                status=user_payload.status,
                active=user_payload.active,
                created_date=datetime.datetime.now(),
                updated_date=datetime.datetime.now()
            )
            self.db.add(create_object)
            self.db.commit()
            self.db.refresh(create_object)
            return create_object
        except Exception as ex:
            print(ex)
            raise ex

    def update(self, user_id: int,  user_payload: UserSchemaUpdateRequest) -> UsersSchema:
        try:
            old_object = self.db.query(UsersModel).filter_by(user_id=user_id)
            actual_user_data = old_object[0]
            old_object.update(
                {
                    "role_id": user_payload.role_id or actual_user_data.role_id,
                    "name":  user_payload.name or actual_user_data.name,
                    "email": user_payload.email or actual_user_data.email,
                    "phone": user_payload.phone or actual_user_data.phone,
                    "status": user_payload.status or actual_user_data.status,
                    "active": user_payload.active or actual_user_data.active,
                    "updated_date": datetime.datetime.now()
                }
            )
            self.db.commit()
            return old_object[0]
        except Exception as ex:
            print(ex)
            raise ex

    def delete(self, user_id: int):
        try:
            self.db.query(UsersModel).filter_by(user_id=user_id).delete()
            self.db.commit()
            return
        except Exception as ex:
            print(ex)
            raise ex

