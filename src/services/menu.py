from sqlalchemy.orm import Session

from api.schemas.menu_schema import MenuCreate
from src.models.menu import MenuModel


def get_list_menu(db: Session):
    data = db.query(MenuModel).all()
    return data


def get_menu_by_title(db: Session, title: str):
    data = db.query(MenuModel).filter(MenuModel.title == title).first()
    return data


def get_menu_by_id(db: Session, id_: int):
    data = db.query(MenuModel).filter(MenuModel.id == id_).first()
    return data


def create_menu(db: Session, menu: MenuCreate):
    data = MenuModel(**menu.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_menu(db: Session, id_: int):
    db.commit()
    return get_menu_by_id(db=db, id_=id_)


def delete_menu(db: Session, id_: int):
    data = get_menu_by_id(db, id_)
    if data is None:
        return "Menu does not exist"
    else:
        db.delete(data)
        db.commit()
        return f"Menu - {id_} delete, ok!"
