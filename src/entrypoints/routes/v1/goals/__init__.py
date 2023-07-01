from fastapi import APIRouter

GoalsRoute = APIRouter(
    prefix='/goals'
)


@GoalsRoute.get('/')
def get_goals():
    pass


@GoalsRoute.get('/{goal_id}')
def get_goal(goal_id: int):
    pass


@GoalsRoute.post('/')
def insert_goal():
    pass


@GoalsRoute.put('/{goal_id')
def update_goal():
    pass


@GoalsRoute.delete('/{goal_id')
def delete_goal():
    pass
