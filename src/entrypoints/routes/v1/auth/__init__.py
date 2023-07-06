from fastapi import APIRouter

AuthRoute = APIRouter(
    prefix='/auth',
    tags=["Authenticate"],
)


@AuthRoute.post('/login')
def auth_user(email: str, password: str):
    pass

@AuthRoute.get('/verify')
def auth_user():
    pass

@AuthRoute.get('/renew')
def renew_auth_user():
    pass
