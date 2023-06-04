from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.infra.adapters.database.make_session import get_db
from src.schemas.users import UsersSchema
from src.usecases.users import UsersUseCase
from src.utils.logs import Logs

UsersRoute = APIRouter(
    prefix='/users',
    tags=["Users"],
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