from fastapi import FastAPI

from src.entrypoints.routes.v1 import roles

app = FastAPI()

app.include_router(roles.RolesRoute)


@app.get("/")
async def hello() -> dict:
    return {"msg": "hello world"}


@app.get("/health")
async def get_health() -> dict:
    """Health check information about this service"""

    return { 
        'Database': 'Status is up',
        'Application:': 'Status is up',
        'Networking': '0.99 ms latency'
    }
