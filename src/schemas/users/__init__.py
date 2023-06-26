from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from src.schemas.role import RoleSchema


class UsersSchema(BaseModel):

    user_id: Optional[int]
    role_id: int
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


class UsersSchemaResponse(BaseModel):

    user_id: Optional[int]
    role_id: int
    name: str
    email: str
    phone: str
    status: str
    active: bool
    created_date: datetime = None
    updated_date: datetime = None

    class Config:
        orm_mode = True


class UserSchemaUpdateRequest(BaseModel):

    role_id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    # sem password aqui, recuperação ou troca de senha apenas via recuperação de senha
    status: Optional[str]
    active: Optional[bool]


class UserPasswordRecovery(BaseModel):

    password: str
