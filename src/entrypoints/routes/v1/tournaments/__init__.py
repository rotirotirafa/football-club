from fastapi import APIRouter

TournamentsRoute = APIRouter(
    prefix='/tournaments'
)


@TournamentsRoute.get('/')
def get_tournaments():
    pass


@TournamentsRoute.get('/{tournament_id}')
def get_tournament(tournament_id: int):
    pass


@TournamentsRoute.post('/')
def insert_tournament():
    pass


@TournamentsRoute.put('/{tournament_id')
def update_tournament():
    pass


@TournamentsRoute.delete('/{tournament_id')
def delete_tournament():
    pass
