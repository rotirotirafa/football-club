import logging
import string
import sentry_sdk
from datetime import time
from random import random



from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.entrypoints.routes.v1 import api_router

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

sentry_sdk.init(
    dsn="https://35b55970326e4017aae536df3b07ce64@o4505484767068160.ingest.sentry.io/4505484768575488",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)


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

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

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
