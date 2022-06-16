#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models.place import Place
import models
from models.base_model import Base
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns the list of city instances with
            state_id equals to the current State.id
            """
            data = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    data.append(city)
            return data
