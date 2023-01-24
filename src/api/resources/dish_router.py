from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from api.schemas.schemes import DishCreate, Dish, DishUpdate
from db.database import get_db
from services import crud_dishes

router = APIRouter()


@router.post("/dishes",
             response_model=Dish,
             status_code=201,
             summary="create dish",
             tags=["dishes"])
def create_dish(menu_id: int,
                submenu_id: int,
                dish: DishCreate,
                db: Session = Depends(get_db)):
    db_dish = crud_dishes.get_dish_by_title(db=db,
                                            dish_title=dish.title)
    if db_dish:
        raise HTTPException(status_code=400, detail="dish already exist")
    else:
        return crud_dishes.create_dish(db=db,
                                       dish=dish,
                                       menu_id=menu_id,
                                       submenu_id=submenu_id)


@router.patch("/dishes/{dish_id}",
              response_model=Dish,
              summary="update dish",
              tags=["dishes"])
def update_dish(dish_id: int,
                dish: DishUpdate,
                db: Session = Depends(get_db)):
    db_dish = crud_dishes.get_dish_by_id(db=db, dish_id=dish_id)
    if dish:
        db_dish.title = dish.title
        db_dish.description = dish.description
        db_dish.price = dish.price
        return crud_dishes.update_dish(db=db, dish_id=dish_id)
    else:
        HTTPException(status_code=404, detail="dish not found")


@router.get("/dishes",
            response_model=List[Dish],
            summary="list dishes",
            tags=["dishes"])
def read_dishes(submenu_id: int,
                db: Session = Depends(get_db)):
    dishes = crud_dishes.get_dishes(db=db, submenu_id=submenu_id)
    return dishes


@router.get("/dishes/{dish_id}",
            response_model=Dish,
            summary="get dish by id",
            tags=["dishes"])
def read_dish(dish_id: int,
              db: Session = Depends(get_db)):
    dish = crud_dishes.get_dish_by_id(db=db, dish_id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return dish


@router.delete("/dishes/{dish_id}",
               summary="delete dish",
               tags=["dishes"])
def delete_dish(dish_id: int,
                menu_id: int,
                submenu_id: int,
                db: Session = Depends(get_db)):
    dish = crud_dishes.delete_dish(db=db,
                                   dish_id=dish_id,
                                   menu_id=menu_id,
                                   submenu_id=submenu_id)
    if dish is None:
        raise HTTPException(status_code=404, detail="dish already exist")
    return {"status": True, "message": "dish has been deleted"}

# @app.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
#           response_model=schemes.Dish,
#           status_code=201,
#           tags=["dishes"])
# def create_dish(menu_id: int, submenu_id: int, dish: schemes.DishCreate, db: Session = Depends(get_db)):
#     db_dish = crud.get_dish_by_title(db=db, dish_title=dish.title)
#     if db_dish:
#         raise HTTPException(status_code=400, detail="dish already exists")
#     else:
#         return crud.create_dish(db=db, dish=dish, menu_id=menu_id, submenu_id=submenu_id)


# Update dish
# @app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
#            response_model=schemes.Dish,
#            tags=["dishes"])
# def update_dish(menu_id: int, submenu_id: int, dish_id: int, dish: schemes.DishUpdate, db: Session = Depends(get_db)):
#     db_dish = crud.get_dish_by_id(db=db, dish_id=dish_id)
#     if db_dish:
#         db_dish.title = dish.title
#         db_dish.description = dish.description
#         db_dish.price = dish.price
#         return crud.update_dish(db=db, dish_id=dish_id)
#     else:
#         raise HTTPException(status_code=404, detail="dish not found")


# Get dishes list
# @app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
#          response_model=List[schemes.Dish],
#          tags=["dishes"])
# def read_dishes(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
#     dishes = crud.get_dishes(db=db, submenu_id=submenu_id)
#     return dishes


# Get dish by id
# @app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
#          response_model=schemes.Dish,
#          tags=["dishes"])
# def read_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
#     db_dish = crud.get_dish_by_id(db=db, dish_id=dish_id)
#     if db_dish is None:
#         raise HTTPException(status_code=404, detail="dish not found")
#     return db_dish

#
# # Delete dish by id
# @app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
#             tags=["dishes"])
# def delete_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
#     db_dish = crud.delete_dish(db=db, dish_id=dish_id, menu_id=menu_id, submenu_id=submenu_id)
#     if db_dish is None:
#         raise HTTPException(status_code=404, detail="dish not found")
#     return {"status": True, "message": "The dish has been deleted"}
