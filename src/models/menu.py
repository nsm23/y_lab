from sqlalchemy import (Column, String,
                        Integer,)
from sqlalchemy.orm import relationship

from src.db.database import Base


class MenuModel(Base):
    __tablename__ = "menus"

    id = Column(Integer,
                primary_key=True,
                index=True,
                autoincrement=True)
    title = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    submenu_count = Column(Integer)
    dishes_count = Column(Integer)

    submenu = relationship("SubmenuModel",
                           back_populates="menu",
                           cascade="all, delete-orphan")
