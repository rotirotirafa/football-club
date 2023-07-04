from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.infra.adapters.database.make_session import get_db
from src.schemas.users import UsersSchema, UsersSchemaResponse, UserSchemaUpdateRequest
from src.usecases.users import UsersUseCase
from src.utils.logs import Logs

UsersRoute = APIRouter(
    prefix='/users'
)


@UsersRoute.get('/', response_model=List[UsersSchema])
def get_users(db: Session = Depends(get_db)) -> List[UsersSchema] or None:
    try:
        users_use_case = UsersUseCase(db)
        return users_use_case.get_all_users()
    except Exception as ex:
        logs = Logs(
            code=1000,
            message='Erro ao processar a requisição: get_roles',
            exception=str(ex)
        )
        logs.error()
        raise ex


@UsersRoute.get('/{user_id}', response_model=UsersSchemaResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UsersSchemaResponse or None:
    try:
        users_use_case = UsersUseCase(db)
        return users_use_case.get_one_user(user_id)
    except Exception as ex:
        print(ex)
        raise ex


@UsersRoute.post('/', response_model=UsersSchemaResponse)
def post_user(user_payload: UsersSchema, db: Session = Depends(get_db)) -> UsersSchemaResponse or None:
    try:
        users_use_case = UsersUseCase(db)
        return users_use_case.create_user(user_payload)
    except Exception as ex:
        print(ex)
        raise ex


@UsersRoute.put('/{user_id}', response_model=UsersSchemaResponse)
def put_user(user_id: int, user_payload: UserSchemaUpdateRequest,  db: Session = Depends(get_db)) -> \
        UsersSchemaResponse or None:
    try:
        users_use_case = UsersUseCase(db)
        return users_use_case.update_user(user_id, user_payload)
    except Exception as ex:
        print(ex)
        raise ex


@UsersRoute.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)) -> ORJSONResponse:
    try:
        users_use_case = UsersUseCase(db)
        users_use_case.delete_user(user_id)
        return ORJSONResponse({'message': 'Deletado com sucesso'})
    except Exception as ex:
        print(ex)
        raise ex
