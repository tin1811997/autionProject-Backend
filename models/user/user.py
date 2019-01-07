import datetime
import bcrypt

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from models.db import Base
from models.product.product import Product
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    # Attributes: with _ in forn of it , that is Attributes can get - set
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    _password = Column(String(250), nullable=False)
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
    product = relationship("Product", backref='user', lazy=True)
    # Method:
    # Getter - Setter:
    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, plain_password):
        self._password = bcrypt.hashpw(
            plain_password.encode(), bcrypt.gensalt()
        ).decode()

    @hybrid_property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # @hybrid_property
    # def avtUrl(self):
    #     return self._avtUrl
    
    # @avtUrl.setter
    # def avtUrl(self, avtUrl):
    #     self._avtUrl = avtUrl

    # Constructor:
    def __init__(self, username: str, password: str, name: str):
        self.username = username
        self.password = password
        self.name = name

    # To String:
    def __repr__(self):
        return "<User id={} username={} name={}>".format(self.id, self.username, self._name)

    # Class method:
    def to_json(self):
        return {
            "username": self.username
        }
    