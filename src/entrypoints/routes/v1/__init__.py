from fastapi import APIRouter

from src.config import API_VERSIONING

from src.entrypoints.routes.v1.assists import AssistsRoute
from src.entrypoints.routes.v1.cards import CardsRoute
from src.entrypoints.routes.v1.goals import GoalsRoute
from src.entrypoints.routes.v1.lineup_starts import LineUpStartsRoute
from src.entrypoints.routes.v1.lineups import LineUpsRoute
from src.entrypoints.routes.v1.matches import MatchesRoute
from src.entrypoints.routes.v1.teams import TeamsRoute
from src.entrypoints.routes.v1.players import PlayersRoute
from src.entrypoints.routes.v1.roles import RolesRoute
from src.entrypoints.routes.v1.tournaments import TournamentsRoute
from src.entrypoints.routes.v1.users import UsersRoute

version = f'/{API_VERSIONING}'
api_router = APIRouter()

api_router.include_router(RolesRoute, tags=['Roles [Cargos]'], prefix=version)
api_router.include_router(PlayersRoute, tags=['Players [Jogadores]'], prefix=version)
api_router.include_router(UsersRoute, tags=['Users [Usuários]'], prefix=version)

#TODO
api_router.include_router(TeamsRoute, tags=['Teams [Times]'], prefix=version)
api_router.include_router(AssistsRoute, tags=['Assists [Assistências]'], prefix=version)
api_router.include_router(CardsRoute, tags=['Cards [Cartões]'], prefix=version)
api_router.include_router(GoalsRoute, tags=['Goals [Gols]'], prefix=version)
api_router.include_router(LineUpStartsRoute, tags=['LineUp Starts [Escalação Inicial]'], prefix=version)
api_router.include_router(LineUpsRoute, tags=['Lineups [Escalação]'], prefix=version)
api_router.include_router(MatchesRoute, tags=['Matches [Partidas]'], prefix=version)
api_router.include_router(TournamentsRoute, tags=['Tournaments [Torneios]'], prefix=version)


