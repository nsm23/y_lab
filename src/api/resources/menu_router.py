from typing import Optional, List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api.schemas.schemes import MenuCreate, MenuUpdate, Menu
from db.database import get_db
from services import crud_menu

router = APIRouter()


@router.post("/menus",
             response_model=Menu,
             summary="create menu",
             status_code=201,
             tags=["menu"])
def create_menu(menu: MenuCreate,
                db: Session = Depends(get_db)):
    db_menu = crud_menu.get_menu_by_title(db=db, menu_title=menu.title)
    if db_menu:
        raise HTTPException(status_code=400, detail="menu already exist")
    else:
        return crud_menu.create_menu(db=db, menu=menu)


@router.patch("/menus/{menu_id}",
              response_model=Menu,
              summary="update menu",
              tags=["menu"])
def update_menu(menu_id,
                menu: MenuUpdate,
                db: Session = Depends(get_db)):
    db_menu = crud_menu.get_menu_by_id(db=db, menu_id=menu_id)
    if db_menu:
        db_menu.title = menu.title
        db_menu.description = menu.description
        return crud_menu.update_menu(db=db, menu_id=menu_id)
    else:
        raise HTTPException(status_code=404, detail="menu not found")


@router.get("/menus",
            response_model=List[Menu],
            summary="list menu",
            tags=["menu"])
def read_menus(db: Session = Depends(get_db)):
    menu = crud_menu.get_menus(db=db)
    return menu


@router.get("/menus/{menu_id}",
            response_model=Menu,
            summary="get menu by id",
            tags=["menu"])
def read_menu(menu_id: int,
              db: Session = Depends(get_db)):
    menu = crud_menu.get_menu_by_id(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu


@router.delete("/menus/{menu_id}",
               summary="delete menu",
               tags=["menu"])
def delete_menu(menu_id: int,
                db: Session = Depends(get_db)):
    menu = crud_menu.delete_menu(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return {"status": True, "message": "menu delete, ok!"}

# @app.post("/api/v1/menus/",
#           response_model=schemes.Menu,
#           status_code=201,
#           tags=["menu"])
# def create_menu(menu: schemes.MenuCreate, db: Session = Depends(get_db)):
#     db_menu = crud.get_menu_by_title(db=db, menu_title=menu.title)
#     if db_menu:
#         raise HTTPException(status_code=400, detail="menu already exists")
#     else:
#         return crud.create_menu(db=db, menu=menu)


# Update menu
# @app.patch("/api/v1/menus/{menu_id}",
#            response_model=schemes.Menu,
#            tags=["menu"])
# def update_menu(menu_id: int, menu: schemes.MenuUpdate, db: Session = Depends(get_db)):
#     db_menu = crud.get_menu_by_id(db=db, menu_id=menu_id)
#     if db_menu:
#         db_menu.title = menu.title
#         db_menu.description = menu.description
#         return crud.update_menu(db=db, menu_id=menu_id)
#     else:
#         raise HTTPException(status_code=404, detail="menu not found")


# Get menus list
# @app.get("/api/v1/menus/",
#          response_model=List[schemes.Menu],
#          tags=["menu"])
# def read_menus(db: Session = Depends(get_db)):
#     menus = crud.get_menus(db=db)
#     return menus
#

# Get menu by id
# @app.get("/api/v1/menus/{menu_id}",
#          response_model=schemes.Menu,
#          tags=["menu"])
# def read_menu(menu_id: int, db: Session = Depends(get_db)):
#     db_menu = crud.get_menu_by_id(db=db, menu_id=menu_id)
#     if db_menu is None:
#         raise HTTPException(status_code=404, detail="menu not found")
#     return db_menu
#

# Delete menu by id
# @app.delete("/api/v1/menus/{menu_id}",
#             tags=["menu"])
# def delete_menu(menu_id: int, db: Session = Depends(get_db)):
#     db_menu = crud.delete_menu(db=db, menu_id=menu_id)
#     if db_menu is None:
#         raise HTTPException(status_code=404, detail="menu not found")
#     return {"status": True, "message": "The menu has been deleted"}
