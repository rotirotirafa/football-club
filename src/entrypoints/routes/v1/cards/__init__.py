from fastapi import APIRouter

CardsRoute = APIRouter(
    prefix='/cards'
)


@CardsRoute.get('/')
def get_cards():
    pass


@CardsRoute.get('/{card_id}')
def get_card(card_id: int):
    pass


@CardsRoute.post('/')
def insert_card():
    pass


@CardsRoute.put('/{card_id')
def update_card():
    pass


@CardsRoute.delete('/{card_id')
def delete_card():
    pass
