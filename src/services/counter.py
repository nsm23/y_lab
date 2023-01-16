from typing import Optional
from sqlalchemy.orm import Session
from src.models.submenu import SubmenuModel
from src.models.dishes import DishesModel


def submenu_count(db: Session, menu_id: int) -> Optional[int]:
    data = db.query(SubmenuModel).filter(SubmenuModel.id == menu_id).count()
    return data


def submenu_dishes(db: Session, dish_id: int) -> Optional[int]:
    data = db.query(DishesModel).filter(DishesModel.id == dish_id).count()
    return data

