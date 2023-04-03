from fastapi import APIRouter

team_routes = APIRouter(
    prefix='/team'
)

@team_routes.get('/')
def teste_time() -> dict:
    return {'time': 'x'}