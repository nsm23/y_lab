from sqlalchemy.orm import Session

from api.schemas.submenu_schema import SubmenuCreate
from src.models.submenu import SubmenuModel
from services.menu import get_menu_by_id


def get_list_submenu(db: Session, id_: int):
    data = db.query(SubmenuModel).filter(SubmenuModel.id == id_).all()
    return data


def get_submenu_by_title(db: Session, title: str):
    data = db.query(SubmenuModel).filter(SubmenuModel.title == title).first()
    return data


def get_submenu_by_id(db: Session, id_: int):
    data = db.query(SubmenuModel).filter(SubmenuModel.id == id_).first()
    return data


def create_submenu(db: Session, submenu: SubmenuCreate, menu_id: int):
    data = SubmenuModel(**submenu.dict())
    data.menus_id = menu_id
    get_menu_by_id(db=db, id_=menu_id).submenu_count += 1
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_submenu(db: Session, id_: int):
    db.commit()
    return get_submenu_by_id(db=db, id_=id_)


def delete_submenu(db: Session, id_: int):
    data = get_submenu_by_id(db,  id_)
    if data is None:
        return "Submenu does not exist"
    else:
        data_menu = get_menu_by_id(db=db, id_=id_)
        data_menu.submenu_count -= 1
        data_menu.dishes_count -= data.dishes_count
        db.delete(data)
        db.commit()
        return f"Submenu {id_} delete, ok!"




