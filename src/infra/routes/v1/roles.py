from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from src.domain.v1.roles.model import RolesModel
from src.infra.database.make_session import get_db

RolesRoute = APIRouter(
    prefix='/roles'
)


@RolesRoute.get('/')
def get_roles(db: Session = Depends(get_db)) -> ORJSONResponse:
    roles = db.query(RolesModel).all()
    yield ORJSONResponse(roles)
