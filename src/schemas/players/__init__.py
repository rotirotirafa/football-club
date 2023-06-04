from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PlayerSchema(BaseModel):
    player_id: Optional[int]
    nickname: str
    status: str
    image_url: str
    profile_desc: str
    main_position: str
    secondary_position: str
    signed: bool
    created_date: datetime = None
    updated_date: datetime = None
    user_id: int
    team_id: Optional[int]
    goals_id: Optional[int]

    class Config:
        orm_mode = True
