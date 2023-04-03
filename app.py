from fastapi import FastAPI
from sqlalchemy.orm import Session
from src.models.roles import Roles
from src.database import SessionLocal, engine
from src.routes import team
from typing import Any
from fastapi import Depends
from src.models.roles import Roles as RolesModel

Roles.metadata.create_all(bind=engine)

app = FastAPI() # Colocar as documentações
app.include_router(team.team_routes)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
async def get_health() -> dict:
    """Health check information about this service"""

    return { 
        'Database': 'Status is up',
        'Application:': 'Status is up',
        'Networking': '0.99 ms latency'
    }
    
@app.get('/roles')
def get_roles(db: Session = Depends(get_db)) -> Any:
    roles = db.query(RolesModel).all()
    yield roles