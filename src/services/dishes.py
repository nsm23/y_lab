from sqlalchemy.orm import Session

from api.schemas.dishes_schema import DishesCreate
from src.models.dishes import DishesModel
from services.menu import get_menu_by_id
from services.submenu import get_submenu_by_id


def get_list_dishes(db: Session, submenu_id: int):
    data = db.query(DishesModel).filter(DishesModel.submenu_id == submenu_id).all()
    return data


def get_dishes_by_title(db: Session, title):
    data = db.query(DishesModel).filter(DishesModel.title == title).first()
    return data


def get_dishes_by_id(db: Session, id_: int):
    data = db.query(DishesModel).filter(DishesModel.id == id_).first()
    return data


def create_dishes(db: Session, dish: DishesCreate, menu_id: int, submenu_id):
    data = DishesModel(**dish.dict())
    data.submenu_id = submenu_id
    get_menu_by_id(db=db, id_=menu_id).dishes_count += 1
    get_submenu_by_id(db=db, id_=submenu_id).dishes_count += 1
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_dishes(db: Session, id_: int):
    db.commit()
    return get_dishes_by_id(db=db, id_=id_)


def delete_dishes(db: Session,
                  dish_id: int,
                  submenu_id: int,
                  menu_id: int):
    data = get_dishes_by_id(db, id_=dish_id)
    if data is None:
        return "This dish does not exist"
    else:
        get_menu_by_id(db=db, id_=menu_id).dishes_count -= 1
        get_submenu_by_id(db=db, id_=submenu_id).dishes_count -= 1
        db.delete(data)
        db.commit()
        return f"Dish - {dish_id} delete, ok!"

