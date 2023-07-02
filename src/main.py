import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.entrypoints.routes.v1 import api_router
from src.utils.logs import Logs


logger = logging.getLogger(__name__)
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Logging request path={request.url.path}")
    logs = Logs(message=f"Logging request path={request.url.path}")
    logs.info()

    response = await call_next(request)
    return response


@app.get("/")
async def hello() -> dict:
    logger.info(f"Hello World")
    return {"msg": "hello world"}


@app.get("/health")
async def get_health() -> dict:
    """Health check information about this service"""
    return {
        'message': 'Up & Running'
    }
