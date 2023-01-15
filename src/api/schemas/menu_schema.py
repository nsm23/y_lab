from typing import Optional

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: Optional[str] = None


class Menu(MenuBase):
    id: str
    submenu_count: int
    dishes_count: int

    class Config:
        orm_mode = True


class MenuCreate(MenuBase):
    submenu_count: int = 0
    dishes_count: int = 0

    class Config:
        orm_mode = True


class MenuUpdate(MenuBase):
    pass

    class Config:
        orm_mode = True

