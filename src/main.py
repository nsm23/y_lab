from fastapi import FastAPI

from models import models
import uvicorn
from db.database import engine
from api.resources import menu_router, submenu_router, dish_router
from core import config

models.Base.metadata.create_all(bind=engine)


app = FastAPI(title=config.PROJECT_NAME,
              version=config.VERSION,
              docs_url="/api/openapi",
              redoc_url="/api/redoc",
              openapi_url="/api/openapi.json")

app.include_router(menu_router.router,
                   prefix="/api/v1")
app.include_router(submenu_router.router,
                   prefix="/api/v1/menus/{menu_id}")
app.include_router(dish_router.router,
                   prefix="/api/v1/menus/{menu_id}/submenus/{submenu_id}")

# Dependency


# API MENU
# Create menu
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
#
#
# # Update menu
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
#
#
# # Get menus list
# @app.get("/api/v1/menus/",
#          response_model=List[schemes.Menu],
#          tags=["menu"])
# def read_menus(db: Session = Depends(get_db)):
#     menus = crud.get_menus(db=db)
#     return menus
#
#
# # Get menu by id
# @app.get("/api/v1/menus/{menu_id}",
#          response_model=schemes.Menu,
#          tags=["menu"])
# def read_menu(menu_id: int, db: Session = Depends(get_db)):
#     db_menu = crud.get_menu_by_id(db=db, menu_id=menu_id)
#     if db_menu is None:
#         raise HTTPException(status_code=404, detail="menu not found")
#     return db_menu
#
#
# # Delete menu by id
# @app.delete("/api/v1/menus/{menu_id}",
#             tags=["menu"])
# def delete_menu(menu_id: int, db: Session = Depends(get_db)):
#     db_menu = crud.delete_menu(db=db, menu_id=menu_id)
#     if db_menu is None:
#         raise HTTPException(status_code=404, detail="menu not found")
#     return {"status": True, "message": "The menu has been deleted"}


# API SUBMENU
# Create submenu
# @app.post("/api/v1/menus/{menu_id}/submenus",
#           response_model=schemes.Submenu,
#           status_code=201,
#           tags=["submenu"])
# def create_submenu(menu_id: int, submenu: schemes.SubmenuCreate, db: Session = Depends(get_db)):
#     db_submenu = crud.get_submenu_by_title(db=db, submenu_title=submenu.title)
#     if db_submenu:
#         raise HTTPException(status_code=400, detail="submenu already exists")
#     else:
#         return crud.create_submenu(db=db, submenu=submenu, menu_id=menu_id)
#
#
# # Update submenu
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
#
# # Get submenus list
# @app.get("/api/v1/menus/{menu_id}/submenus",
#          response_model=List[schemes.Submenu],
#          tags=["submenu"])
# def read_submenus(menu_id: int, db: Session = Depends(get_db)):
#     submenus = crud.get_submenus(db=db, menu_id=menu_id)
#     return submenus
#
#
# # Get submenu by id
# @app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
#          response_model=schemes.Submenu,
#          tags=["submenu"])
# def read_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
#     db_submenu = crud.get_submenu_by_id(db=db, submenu_id=submenu_id)
#     if db_submenu is None:
#         raise HTTPException(status_code=404, detail="submenu not found")
#     return db_submenu
#
#
# # Delete submenu by id
# @app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
#             tags=["submenu"])
# def delete_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
#     db_submenu = crud.delete_submenu(db=db, menu_id=menu_id, submenu_id=submenu_id)
#     if db_submenu is None:
#         raise HTTPException(status_code=404, detail="submenu not found")
#     return {"status": True, "message": "The submenu has been deleted"}


# API DISHES
# Create dish
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
#
#
# # Update dish
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
#
#
# # Get dishes list
# @app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
#          response_model=List[schemes.Dish],
#          tags=["dishes"])
# def read_dishes(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
#     dishes = crud.get_dishes(db=db, submenu_id=submenu_id)
#     return dishes
#
#
# # Get dish by id
# @app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
#          response_model=schemes.Dish,
#          tags=["dishes"])
# def read_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
#     db_dish = crud.get_dish_by_id(db=db, dish_id=dish_id)
#     if db_dish is None:
#         raise HTTPException(status_code=404, detail="dish not found")
#     return db_dish
#
#
# # Delete dish by id
# @app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
#             tags=["dishes"])
# def delete_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
#     db_dish = crud.delete_dish(db=db, dish_id=dish_id, menu_id=menu_id, submenu_id=submenu_id)
#     if db_dish is None:
#         raise HTTPException(status_code=404, detail="dish not found")
#     return {"status": True, "message": "The dish has been deleted"}
#

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
