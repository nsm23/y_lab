from typing import Optional

from pydantic import BaseModel


class DishesBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[str] = None


class Dishes(DishesBase):
    id: str

    class Config:
        orm_mode = True


class DishesCreate(DishesBase):
    pass


class DishesUpdate(DishesBase):
    pass
