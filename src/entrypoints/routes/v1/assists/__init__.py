from fastapi import APIRouter

AssistsRoute = APIRouter(
    prefix='/assists'
)


@AssistsRoute.get('/')
def get_assists():
    pass


@AssistsRoute.get('/{assist_id}')
def get_assist():
    pass


@AssistsRoute.post('/')
def insert_assist():
    pass


@AssistsRoute.put('/{assist_id')
def update_assist():
    pass


@AssistsRoute.delete('/{assist_id}')
def delete_assist():
    pass
