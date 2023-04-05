from pydantic import BaseModel
from typing import Optional


class RoleSchema(BaseModel):
    role_id: Optional[int]
    name: str

    class Config:
        orm_mode = True
