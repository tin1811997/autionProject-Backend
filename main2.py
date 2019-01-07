from models.db import Base,engine
from models.user.user import User
from models.product.product import Product

Base.metadata.create_all(engine)

