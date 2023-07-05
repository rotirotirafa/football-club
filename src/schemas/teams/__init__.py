from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TeamSchema(BaseModel):
    team_id: int
    name: str
    image_url: str
    profile_desc: str
    created_date: datetime = None
    updated_date: datetime = None

    class Config:
        orm_mode = True


class TeamSchemaCreateRequest(BaseModel):
    name: str
    image_url: Optional[str]
    profile_desc: Optional[str]
    created_date: datetime = None
    updated_date: datetime = None

    class Config:
        orm_mode = True


class TeamSchemaUpdate(BaseModel):
    name: Optional[str]
    image_url: Optional[str]
    profile_desc: Optional[str]

    class Config:
        orm_mode = True