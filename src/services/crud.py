# import json
#
# from sqlalchemy.orm import Session
# from fastapi import Depends
# from api.schemas.schemes import MenuCreate, SubmenuCreate, DishCreate
# from db.database import get_db
# from models.models import Menu, Submenu, Dish
# from services.mixins import ServiceMixin
#
#
# class MenuServices(ServiceMixin):
#     def __init__(self, session: Session):
#         super().__init__(session=session)
#
#     def get_menu_by_id(self, menu_id: int):
#         menu = self.session.query(Menu).filter(Menu.id == menu_id).first()
#         return menu
#
#     def get_menu_by_title(self, menu_title: str):
#         menu = self.session.query(Menu).filter(Menu.title == menu_title).first()
#         return menu
#
#     def get_menus(self):
#         menus = self.session.query(Menu).all()
#         return menus
#
#     def create_menu(self, menu: MenuCreate):
#         data = Menu(**menu.dict())
#         self.session.add(data)
#         self.session.commit()
#         self.session.refresh(data)
#         return data
#
#     def delete_menu(self, menu_id: int):
#         data = self.get_menu_by_id(menu_id=menu_id)
#         if data is None:
#             return None
#         else:
#             self.session.delete(data)
#             self.session.commit()
#             return True
#
#     def update_menu(self, menu_id: int):
#         self.session.commit()
#         menu = self.get_menu_by_id(menu_id=menu_id)
#         return menu
#
#
# def get_menu_service(session: Session = Depends(get_db)):
#     return MenuServices(session=session)
#
#
# # MENU CRUD
#
#
# class SubmenuServices(ServiceMixin):
#     def __init__(self, session: Session, menu: MenuServices):
#         self.menu = menu
#         super().__init__(session=session)
#
#     def get_submenu_by_id(self, submenu_id: int):
#         submenu = self.session.query(Submenu).filter(Submenu.id == submenu_id).first()
#         return submenu
#
#     def get_submenu_by_title(self, submenu_title: str):
#         submenu = self.session.query(Submenu).filter(Submenu.title == submenu_title).first()
#         return submenu
#
#     def get_submenus(self, menu_id: int):
#         submenus = self.session.query(Submenu).filter(Submenu.menu_id == menu_id).all()
#         return submenus
#
#     def create_submenu(self, submenu: SubmenuCreate, menu_id: int):
#         data = Submenu(**submenu.dict())
#         data.menu_id = menu_id
#         self.menu.get_menu_by_id(menu_id=menu_id).submenus_count += 1
#         self.session.add(data)
#         self.session.commit()
#         self.session.refresh(data)
#         return data
#
#     def delete_submenu(self, menu_id: int, submenu_id: int):
#         data_submenu = self.get_submenu_by_id(submenu_id=submenu_id)
#         if data_submenu is None:
#             return None
#         else:
#             data_menu = self.menu.get_menu_by_id(menu_id=menu_id)
#             data_menu.submenus_count -= 1
#             data_menu.dishes_count -= data_submenu.dishes_count
#             self.session.delete(data_submenu)
#             self.session.commit()
#             return True
#
#     def update_submenu(self, submenu_id: int):
#         self.session.commit()
#         submenus = self.get_submenu_by_id(submenu_id=submenu_id)
#         return submenus
#
#
# # SUBMENU CRUD
#
#
# class DishesServices(ServiceMixin):
#     def __init__(self, session: Session,
#                  menu: MenuServices,
#                  submenu: SubmenuServices):
#         self.menu = menu
#         self.submenu = submenu
#         super().__init__(session=session)
#
#     def get_dish_by_id(self, dish_id: int):
#         dish = self.session.query(Dish).filter(Dish.id == dish_id).first()
#         return dish
#
#     def get_dish_by_title(self, dish_title: str):
#         dish = self.session.query(Dish).filter(Dish.title == dish_title).filter()
#         return dish
#
#     def get_dishes(self, submenu_id: int):
#         dishes = self.session.query(Dish).filter(Dish.submenu_id == submenu_id).all()
#         return dishes
#
#     def create_dish(self, dish: DishCreate, menu_id: int, submenu_id: int):
#         data_dish = Dish(**dish.dict())
#         data_dish.submenu_id = submenu_id
#         self.menu.get_menu_by_id(menu_id=menu_id).dishes_count += 1
#         self.submenu.get_submenu_by_id(submenu_id=submenu_id).dishes_count += 1
#         self.session.add(data_dish)
#         self.session.commit()
#         self.session.refresh(data_dish)
#         return data_dish
#
#     def delete_dish(self, dish_id: int,
#                     submenu_id: int,
#                     menu_id: int):
#         data_dish = self.get_dish_by_id(dish_id=dish_id)
#         if data_dish is None:
#             return None
#         else:
#             self.menu.get_menu_by_id(menu_id=menu_id).dishes_count -= 1
#             self.submenu.get_submenu_by_id(submenu_id=submenu_id).dishes_count -= 1
#             self.session.delete(data_dish)
#             self.session.commit()
#             return True
#
#     def update_dish(self, dish_id):
#         self.session.commit()
#         dish = self.get_dish_by_id(dish_id=dish_id)
#         return dish
#
#
# def get_submenu_service(session: Session = Depends(get_db()),
#                         menu: MenuServices = Depends(get_db())):
#     return SubmenuServices(session=session, menu=menu)
#
#
# def get_dish_service(session: Session = Depends(get_db()),
#                      menu: MenuServices = Depends(get_db()),
#                      submenu: SubmenuServices = Depends(get_db())):
#     return DishesServices(session=session, menu=menu, submenu=submenu)
#
#
# # DISHES CRUD
#
#
#
