from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PlayerSchema(BaseModel):
    player_id: Optional[int]
    nickname: str
    status: Optional[str]
    image_url: Optional[str]
    profile_desc: str
    main_position: str
    secondary_position: str
    signed: bool
    created_date: datetime = None
    updated_date: datetime = None
    user_id: int
    team_id: Optional[int]

    class Config:
        orm_mode = True


class PlayerSchemaInsertResponse(BaseModel):
    player_id: Optional[int]
    nickname: str
    status: Optional[str]
    image_url: Optional[str]
    profile_desc: str
    main_position: str
    secondary_position: str
    signed: bool
    created_date: datetime = None
    updated_date: datetime = None
    user_id: int
    team_id: Optional[int]

    class Config:
        orm_mode = True


class PlayerUpdateRequest(BaseModel):
    player_id: Optional[int]
    nickname: Optional[str]
    status: Optional[str]
    image_url: Optional[str]
    profile_desc: Optional[str]
    main_position: Optional[str]
    secondary_position: Optional[str]
    signed: Optional[bool]
    updated_date: datetime = None
    user_id: int
    team_id: Optional[int]

    class Config:
        orm_mode = True
