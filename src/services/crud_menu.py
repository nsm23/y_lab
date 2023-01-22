from sqlalchemy.orm import Session

from api.schemas.schemes import MenuCreate
from models.models import Menu


def get_menu_by_id(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def get_menu_by_title(db: Session, menu_title: str):
    return db.query(Menu).filter(Menu.title == menu_title).first()


def get_menus(db: Session):
    return db.query(Menu).all()


def create_menu(db: Session, menu: MenuCreate):
    db_menu = Menu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: int):
    db_menu = get_menu_by_id(db=db, menu_id=menu_id)
    if db_menu is None:
        return None
    else:
        db.delete(db_menu)
        db.commit()
        return True


def update_menu(db: Session, menu_id: int):
    db.commit()
    return get_menu_by_id(db=db, menu_id=menu_id)
