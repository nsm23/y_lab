from sqlalchemy.orm import Session
import models, schemes


# MENU CRUD
def get_menu_by_id(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_menu_by_title(db: Session, menu_title: str):
    return db.query(models.Menu).filter(models.Menu.title == menu_title).first()


def get_menus(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session, menu: schemes.MenuCreate):
    db_menu = models.Menu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: int):
    db_menu = get_menu_by_id(db, menu_id)
    if db_menu is None:
        return None
    else:
        db.delete(db_menu)
        db.commit()
        return True


def update_menu(db: Session, menu_id: int):
    db.commit()
    return get_menu_by_id(db=db, menu_id=menu_id)


# SUBMENU CRUD
def get_submenu_by_id(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


def get_submenu_by_title(db: Session, submenu_title: str):
    return db.query(models.Submenu).filter(models.Submenu.title == submenu_title).first()


def get_submenus(menu_id: int, db: Session):
    return db.query(models.Submenu).filter(models.Submenu.menu_id == menu_id).all()


def create_submenu(db: Session, submenu: schemes.SubmenuCreate, menu_id: int):
    db_submenu = models.Submenu(**submenu.dict())
    db_submenu.menu_id = menu_id
    get_menu_by_id(db=db, menu_id=menu_id).submenus_count += 1
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, menu_id: int, submenu_id: int):
    db_submenu = get_submenu_by_id(db, submenu_id)
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


# DISHES CRUD
def get_dish_by_title(db: Session, dish_title: str):
    return db.query(models.Dish).filter(models.Dish.title == dish_title).first()


def get_dishes(submenu_id: int, db: Session):
    return db.query(models.Dish).filter(models.Dish.submenu_id == submenu_id).all()


def create_dish(db: Session, dish: schemes.DishCreate, menu_id: int, submenu_id: int):
    db_dish = models.Dish(**dish.dict())
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


def get_submenus_count(db: Session, menu_id):
    return db.query(models.Submenu).filter(models.Submenu.menu_id == menu_id).count()


def get_dishes_count(db: Session, submenu_id):
    return db.query(models.Dish).filter(models.Dish.submenu_id == submenu_id).count()


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(models.Dish).filter(models.Dish.id == dish_id).first()
