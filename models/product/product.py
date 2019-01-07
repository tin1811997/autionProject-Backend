import datetime
import bcrypt

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from models.db import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'product'
    # Attributes: with _ in forn of it , that is Attributes can get - set
    id = Column(Integer, primary_key=True)
    _name = Column(String(250), nullable=False)
    # _avtUrl = Column(String(250)
    create_at = Column(
        DateTime, 
        default=datetime.datetime.now, 
        onupdate=datetime.datetime.now, 
        nullable=False
    )
    update_at = Column (
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False
    )
    # Relation:
    _user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # Method:
    # Getter - Setter:
    @hybrid_property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @hybrid_property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    # Constructor:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

    # To String:
    def __repr__(self):
        return "<Product id={} name={}>".format(self.id, self.name)

    # Class method:
    def to_json(self):
        return {
            "username": self.name,
            "user_id":self.user_id
        }
    