#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                           Column('place_id', String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True, nullable=False),
                           Column('amenity_id', String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False))
    
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """returns review instances"""
            data = []
            all_objs = models.storage.all(Review)
            for review in all_objs.values():
                if review.place_id == self.id:
                    data.append(review)
            return data

        @property
        def amenities(self):
            """returns amenity instances"""
            data = []
            all_objs = models.storage.all(Amenity)
            for amenity in all_objs.values():
                if amenity.place_id == self.id:
                    data.append(amenity)
            return data

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding
            an Amenity.id to the attribute amenity_ids
            """
            if obj:
                if isinstance(obj, Amenity):
                    self.amenity_ids.append(obj.id)
