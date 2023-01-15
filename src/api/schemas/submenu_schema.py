from typing import Optional

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: Optional[str] = None


class Submenu(SubmenuBase):
    id: str
    dishes_count: int

    class Config:
        orm_mode = True


class SubmenuCreate(SubmenuBase):
    dishes_count: int = 0

    class Config:
        orm_mode = True


class SubmenuUpdate(SubmenuBase):
    pass

