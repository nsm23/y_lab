from sqlalchemy import (Column, String,
                        Integer, ForeignKey)
from sqlalchemy.orm import relationship

from src.db.database import Base


class SubmenuModel(Base):
    __tablename__ = "submenu"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                index=True)
    title = Column(String(128),
                   nullable=False)
    description = Column(String(128),
                         nullable=False)
    menus_id = Column(Integer,
                      ForeignKey("menus.id"))
    dishes_count = Column(Integer)

    menu = relationship("MenuModel",
                        back_populates='submenu')
    dish = relationship("DishesModel",
                        back_populates='submenu',
                        cascade="all, delete-orphan")