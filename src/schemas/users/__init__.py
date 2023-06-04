from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from src.schemas.role import RoleSchema


class UsersSchema(BaseModel):

    user_id: Optional[int]
    role_id: List[RoleSchema] = []
    name: str
    email: str
    phone: str
    password: str
    status: str
    active: bool
    created_date: datetime = None
    updated_date: datetime = None

    class Config:
        orm_mode = True
