from fastapi import APIRouter

from src.entrypoints.routes.v1 import role

router = APIRouter()
router.include_route(role.router, prefix='/roles', tags=['role'])
