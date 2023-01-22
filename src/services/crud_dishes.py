from sqlalchemy.orm import Session

from api.schemas.schemes import DishCreate
from models.models import Dish
from services.crud_menu import get_menu_by_id
from services.crud_submenu import get_submenu_by_id


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(Dish).filter(Dish.id == dish_id).first()


def get_dish_by_title(db: Session, dish_title: str):
    return db.query(Dish).filter(Dish.title == dish_title).first()


def get_dishes(submenu_id: int, db: Session):
    return db.query(Dish).filter(Dish.submenu_id == submenu_id).all()


def create_dish(db: Session, dish: DishCreate, menu_id: int, submenu_id: int):
    db_dish = Dish(**dish.dict())
    db_dish.submenu_id = submenu_id
    get_menu_by_id(db=db, menu_id=menu_id).dishes_count += 1
    get_submenu_by_id(db=db, submenu_id=submenu_id).dishes_count += 1
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def delete_dish(db: Session, dish_id: int, menu_id: int, submenu_id: int):
    db_dish = get_dish_by_id(db, dish_id)
    if db_dish is None:
        return None
    else:
        get_menu_by_id(db=db, menu_id=menu_id).dishes_count -= 1
        get_submenu_by_id(db=db, submenu_id=submenu_id).dishes_count -= 1
        db.delete(db_dish)
        db.commit()
        return True


def update_dish(db: Session, dish_id: int):
    db.commit()
    return get_dish_by_id(db=db, dish_id=dish_id)
