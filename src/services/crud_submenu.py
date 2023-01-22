from sqlalchemy.orm import Session

from api.schemas.schemes import SubmenuCreate
from models.models import Submenu, Dish
from services.crud_menu import get_menu_by_id


def get_submenu_by_id(db: Session, submenu_id: int):
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()


def get_submenu_by_title(db: Session, submenu_title: str):
    return db.query(Submenu).filter(Submenu.title == submenu_title).first()


def get_submenus(menu_id: int, db: Session):
    return db.query(Submenu).filter(Submenu.menu_id == menu_id).all()


def create_submenu(db: Session, submenu: SubmenuCreate, menu_id: int):
    db_submenu = Submenu(**submenu.dict())
    db_submenu.menu_id = menu_id
    get_menu_by_id(db=db, menu_id=menu_id).submenus_count += 1
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, menu_id: int, submenu_id: int):
    db_submenu = get_submenu_by_id(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        return None
    else:
        db_menu = get_menu_by_id(db=db, menu_id=menu_id)
        db_menu.submenus_count -= 1
        db_menu.dishes_count -= db_submenu.dishes_count
        db.delete(db_submenu)
        db.commit()
        return True


def update_submenu(db: Session, submenu_id: int):
    db.commit()
    return get_submenu_by_id(db=db, submenu_id=submenu_id)


def get_submenus_count(db: Session, menu_id):
    return db.query(Submenu).filter(Submenu.menu_id == menu_id).count()


def get_dishes_count(db: Session, submenu_id):
    return db.query(Dish).filter(Dish.submenu_id == submenu_id).count()

