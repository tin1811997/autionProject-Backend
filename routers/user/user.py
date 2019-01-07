from models.user.user import User
from flask import Blueprint, request, jsonify
from models.db import db_session
from routers.user.user_schema import CREATE_SCHEMA, LOGIN_SCHEMA, EDIT_SCHEMA
import sqlalchemy
from voluptuous import MultipleInvalid
import bcrypt

bp = Blueprint("user", __name__)

@bp.route('/users', methods=['POST'])
def create():
    return handler.create()
 
@bp.route('/user/<id>', methods=['GET'])
def get_by_id(id):
    return handler.get_by_id(id)

@bp.route('/user/login', methods=['POST'])
def login():
    return handler.login()

@bp.route('/users/<id>', methods=['PUT'])
def edit(id):
    return handler.edit(id)
    
class handler:
    def create():
        try:
            data = CREATE_SCHEMA(request.get_json())
            user = User(data['username'], data['password'], data['name'])
            db_session.add(user)
            db_session.commit()
            return jsonify(user.to_json()), 201
        # Except bad request
        except MultipleInvalid as e:
            return jsonify({"Error":str(e)}), 400
        # User already exist
        except sqlalchemy.exc.IntegrityError:
            db_session.rollback()
            return jsonify({"Error":"User already exist"})
    def get_by_id(id):
        user = db_session.query(User).filter_by(id =id).first()
        if user is None:
            return jsonify({"Error":"User not exist"}), 404
        else:
            return jsonify(user.to_json())
    def login():
        try :
            data = LOGIN_SCHEMA(request.get_json())
            user = db_session.query(User).filter_by(username = data['username']).first()
            if user is None:
                return jsonify({"Error":"User not exist"}), 404
            else:
                if bcrypt.checkpw(data['password'].encode(),user.password.encode()):
                    return jsonify(user.to_json()), 200
                return jsonify({"Error":"Wrong password"}), 200
        # Except bad request
        except MultipleInvalid as e:
            return jsonify({"Error":str(e)}), 400
    def edit(id):
        try:
            data = EDIT_SCHEMA(request.get_json())
            user = db_session.query(User).filter_by(id =id).first()
            if user is None:
                return jsonify({"Error":"User not exist"}), 404
            else :
                if data["password"] == "":
                    user.name = data['name']
                else :
                    user.password = data['password']
                    user.name = data['name']
                db_session.add(user)
                db_session.commit()
                return jsonify(user.to_json()), 200
        # Except bad request
        except MultipleInvalid as e:
            return jsonify({"Error":str(e)}), 400
    
