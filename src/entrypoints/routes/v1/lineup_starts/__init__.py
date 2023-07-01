from fastapi import APIRouter

LineUpStartsRoute = APIRouter(
    prefix='/lineup-starts'
)


@LineUpStartsRoute.get('/')
def get_lineups():
    pass


@LineUpStartsRoute.get('/{lineup_id}')
def get_lineup(lineup_id: int):
    pass


@LineUpStartsRoute.post('/')
def insert_lineup():
    pass


@LineUpStartsRoute.put('/{lineup_id')
def update_lineup():
    pass


@LineUpStartsRoute.delete('/{lineup_id')
def delete_lineup():
    pass
