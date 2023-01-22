from fastapi import Depends, APIRouter, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
from api.schemas.schemes import (Submenu,
                                 SubmenuCreate,
                                 SubmenuUpdate)
from db.database import get_db
from services import crud_submenu

router = APIRouter()


@router.post("/submenus",
             response_model=Submenu,
             summary="create submenu",
             status_code=201,
             tags=["submenu"])
def create_submenu(menu_id: int, submenu: SubmenuCreate,
                   db: Session = Depends(get_db)):
    db_submenu = crud_submenu.get_submenu_by_title(db=db,
                                                   submenu_title=submenu.title)
    if db_submenu:
        raise HTTPException(status_code=400, detail="submenu already exist")
    else:
        return crud_submenu.create_submenu(db=db, submenu=submenu, menu_id=menu_id)


@router.patch("/submenus/{submenu_id}",
              response_model=Submenu,
              summary="update submenu",
              tags=["submenu"])
def update_submenu(submenu_id: int,
                   submenu: SubmenuUpdate,
                   db: Session = Depends(get_db)):
    db_submenu = crud_submenu.get_submenu_by_id(db=db,
                                                submenu_id=submenu_id)
    if db_submenu:
        db_submenu.title = submenu.title
        db_submenu.description = submenu.description
        return crud_submenu.update_submenu(db=db,
                                           submenu_id=submenu_id)
    else:
        raise HTTPException(status_code=404, detail="submenu not found")


@router.get("/submenus",
            response_model=List[Submenu],
            summary="list submenus",
            tags=["submenu"])
def read_submenus(menu_id: int,
                  db: Session = Depends(get_db)):
    submenus = crud_submenu.get_submenus(db=db, menu_id=menu_id)
    return submenus


@router.get("submenus/{submenu_id}",
            response_model=Submenu,
            summary="get submenu by id",
            tags=["submenu"])
def read_submenu(submenu_id: int,
                 db: Session = Depends(get_db)):
    submenu = crud_submenu.get_submenu_by_id(db=db,
                                             submenu_id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return submenu


@router.delete("/submenus/{submenu_id}",
               summary="delete submenu",
               tags=["submenu"])
def delete_submenu(menu_id: int,
                   submenu_id: int,
                   db: Session = Depends(get_db)):
    submenu = crud_submenu.delete_submenu(db=db,
                                          menu_id=menu_id,
                                          submenu_id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return {"status": True, "message": "submenu has been deleted"}

# @app.post("/api/v1/menus/{menu_id}/submenus",
#           response_model=Submenu,
#           status_code=201,
#           tags=["submenu"])
# def create_submenu(menu_id: int, submenu: schemes.SubmenuCreate, db: Session = Depends(get_db)):
#     db_submenu = crud.get_submenu_by_title(db=db, submenu_title=submenu.title)
#     if db_submenu:
#         raise HTTPException(status_code=400, detail="submenu already exists")
#     else:
#         return crud.create_submenu(db=db, submenu=submenu, menu_id=menu_id)


# Update submenu
# @app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
#            response_model=schemes.Submenu,
#            tags=["submenu"])
# def update_submenu(menu_id: int, submenu_id: int, submenu: schemes.SubmenuUpdate, db: Session = Depends(get_db)):
#     db_submenu = crud.get_submenu_by_id(db=db, submenu_id=submenu_id)
#     if db_submenu:
#         db_submenu.title = submenu.title
#         db_submenu.description = submenu.description
#         return crud.update_submenu(db=db, submenu_id=submenu_id)
#     else:
#         raise HTTPException(status_code=404, detail="submenu not found")
#

# Get submenus list
# @app.get("/api/v1/menus/{menu_id}/submenus",
#          response_model=List[schemes.Submenu],
#          tags=["submenu"])
# def read_submenus(menu_id: int, db: Session = Depends(get_db)):
#     submenus = crud.get_submenus(db=db, menu_id=menu_id)
#     return submenus


# Get submenu by id
# @app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
#          response_model=schemes.Submenu,
#          tags=["submenu"])
# def read_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
#     db_submenu = crud.get_submenu_by_id(db=db, submenu_id=submenu_id)
#     if db_submenu is None:
#         raise HTTPException(status_code=404, detail="submenu not found")
#     return db_submenu


# Delete submenu by id
# @app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
#             tags=["submenu"])
# def delete_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
#     db_submenu = crud.delete_submenu(db=db, menu_id=menu_id, submenu_id=submenu_id)
#     if db_submenu is None:
#         raise HTTPException(status_code=404, detail="submenu not found")
#     return {"status": True, "message": "The submenu has been deleted"}
