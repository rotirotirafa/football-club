from fastapi import APIRouter

LineUpsRoute = APIRouter(
    prefix='/lineups'
)


@LineUpsRoute.get('/')
def get_lineups():
    pass


@LineUpsRoute.get('/{lineup_id}')
def get_lineup(lineup_id: int):
    pass


@LineUpsRoute.post('/')
def insert_lineup():
    pass


@LineUpsRoute.put('/{lineup_id')
def update_lineup():
    pass


@LineUpsRoute.delete('/{lineup_id')
def delete_lineup():
    pass
