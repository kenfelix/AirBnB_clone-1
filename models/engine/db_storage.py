#!/usr/bin/python3
"""Defines the Database Storage engine."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base


class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize db storage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on current database session
        all objects depending on class name
        else return all
        """
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            data = self.__session.query(cls)
        else:
            data = self.__session.query(State).all()
            data.extend(self.__session.query(City).all())
            data.extend(self.__session.query(User).all())
            data.extend(self.__session.query(Place).all())
            data.extend(self.__session.query(Review).all())
            data.extend(self.__session.query(Amenity).all())
        return {"{}.{}".format(type(e).__name__, e.id): e for obj in data}

    def new(self, obj):
        """add the object obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the db session"""
        self.__session.remove()