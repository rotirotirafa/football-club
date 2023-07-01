from fastapi import APIRouter

MatchesRoute = APIRouter(
    prefix='/matches'
)


@MatchesRoute.get('/')
def get_matches():
    pass


@MatchesRoute.get('/{match_id}')
def get_match(match_id: int):
    pass


@MatchesRoute.post('/')
def insert_match():
    pass


@MatchesRoute.put('/{match_id')
def update_match():
    pass


@MatchesRoute.delete('/{match_id')
def delete_match():
    pass
