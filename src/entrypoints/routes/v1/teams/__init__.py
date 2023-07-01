from fastapi import APIRouter

TeamsRoute = APIRouter(
    prefix='/teams'
)


@TeamsRoute.get('/')
def get_teams():
    pass


@TeamsRoute.get('/{team_id}')
def get_team():
    pass


@TeamsRoute.post('/')
def create_team():
    pass


@TeamsRoute.put('/{team_id}')
def update_team():
    pass


@TeamsRoute.delete('/{team_id}')
def delete_team():
    pass
