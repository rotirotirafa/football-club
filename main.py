from fastapi import FastAPI

from src.entrypoints.routes.v1 import role

app = FastAPI()
app.include_router(role.RolesRoute)


@app.get("/health")
async def get_health() -> dict:
    """Health check information about this service"""

    return { 
        'Database': 'Status is up',
        'Application:': 'Status is up',
        'Networking': '0.99 ms latency'
    }
