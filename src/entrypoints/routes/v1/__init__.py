from fastapi import APIRouter

from src.config import API_VERSIONING
from src.entrypoints.routes.v1.players import PlayersRoute
from src.entrypoints.routes.v1.roles import RolesRoute
from src.entrypoints.routes.v1.users import UsersRoute

version = API_VERSIONING
api_router = APIRouter()

api_router.include_router(RolesRoute, tags=['Roles [Cargos]'], prefix=f'/{version}')
api_router.include_router(PlayersRoute, tags=['Players [Jogadores]'], prefix=f'/{version}')
api_router.include_router(UsersRoute, tags=['Users [Usuários]'], prefix=f'/{version}')
