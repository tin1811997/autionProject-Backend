from models.product.product import Product
from flask import Blueprint, request, jsonify
from models.db import db_session
from routers.product.product_schema import CREATE_SCHEMA, EDIT_SCHEMA
import sqlalchemy
from voluptuous import MultipleInvalid
from routers.user.user import handler as user_handler
from sqlalchemy import exc

bp = Blueprint("product", __name__)

@bp.route('/products', methods = ['POST'])
def create():
    return handler.create()
    
@bp.route('/users/<user_id>/products', methods = ['GET'])
def get_products_by_user_id(user_id):
    return handler.get_products_by_user_id(user_id)

@bp.route('/products/<id>', methods = ['GET'])
def get_product_by_id(id):
    return handler.get_product_by_id(id)

@bp.route('/products/<id>', methods = ['PATCH'])
def edit(id):
    return handler.edit(id)

class handler:
    def create():
        try:
            data = CREATE_SCHEMA(request.get_json())
            product = Product(data["name"], data["user_id"])
            db_session.add(product)
            db_session.commit()
            return jsonify(product.to_json()), 201
        # Except bad request
        except MultipleInvalid as e:
            return jsonify({"Error":str(e)}), 400
        # UserId don't exist
        except sqlalchemy.exc.IntegrityError:
            db_session.rollback()
            return jsonify({"Error":"UserId don't exist"})
    def get_products_by_user_id(user_id):
        user_handler.get_by_id(user_id)
        products = db_session.query(Product).filter_by(_user_id=user_id)
        if products is None:
            return jsonify({"Error":"NULL"}), 404
        else :
            list_product = []
            for product in products:
                list_product.append(product.to_json())
            return jsonify(list_product)
    def get_product_by_id(id):
        product = db_session.query(Product).filter_by(id = id).first()
        if product is None:
            return jsonify({"Error":"Product Not Found"}), 404
        else :
            return jsonify(product.to_json())
    def edit(id):
        try:
            data = EDIT_SCHEMA(request.get_json())
            product = db_session.query(Product).filter_by(id = id).first()
            if product is None:
                return jsonify({"Error":"Product Not Found"}), 404
            else :
                if data["user_id"] == "":
                    product.name = data["name"]
                else:
                    product.user_id = data["user_id"]
                    product.name = data["name"]
                db_session.add(product)
                db_session.commit()
                return jsonify(product.to_json()), 200
        # Except bad request
        except MultipleInvalid as e:
            return jsonify({"Error":str(e)}), 400
        # Except User Id not exit
        except exc.IntegrityError as e:
            db_session.rollback()
            return jsonify({"Error":"User ID not exist"}), 404
            