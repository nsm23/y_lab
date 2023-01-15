from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from db.database import db


class DishesModel(db):
    __tablename__ = "dishes"

    id = Column(Integer,
                primary_key=True,
                index=True,
                autoincrement=True)
    title = Column(String(128), nullable=False)
    description = Column(String(250),
                         nullable=False)
    price = Column(Numeric(7, 2))
    submenu_id = Column(ForeignKey("submenu.id"))

    submenu = relationship("SubmenuModel",
                           back_populates="dish")
