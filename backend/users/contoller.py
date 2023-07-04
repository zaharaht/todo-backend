from flask import Blueprint, jsonify, request
from backend.db import db
from backend.users.users import User
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint('users', __name__, url_prefix='/users')

# Get all users
@users.route("/")
def get_all_users():
    all_users = User.query.all()
    user_data = [user.serialize() for user in all_users]

    return jsonify({
        "success": True,
        "data": user_data,
        "total": len(user_data)
    }), 200

#get user by id
@users.route('/user/<user_id>',methods=['GET'])
def get_one_user(public_id):
    return jsonify({'user'})



# Creating a user
@users.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()

    if request.method == "POST":
        public_id = data.get('public_id')
        name = data.get('name')
        password = data.get('password')
        admin = data.get('admin')

        # Validations
        if not name:
            return jsonify({"error": 'Name is required'}), 400

        if User.query.filter_by(name=name).first() is not None:
            return jsonify({"error": 'User already exists, please login'}), 400

        if not password:
            return jsonify({"error": 'Password is required'}), 400

        if not public_id:
            return jsonify({"error": 'Please enter your ID'}), 400

        hashed_password = generate_password_hash(data['password'], method="sha256")

        new_user = User(public_id=str(uuid.uuid4()),name=data['name'],password=hashed_password,admin=False)

        # Inserting values
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'New user created successfully', }), 201

 
#Updating auser
@users.route('/user/<user_id>',methods=['PUT'])
def promote_user(public_id):
    
    User=User.query.filter_by(public_id=public_id).first()
    if not User:
     return jsonify({'message':'user not found'})
    

    User.admin=True
    db.session.commit()
    return jsonify({'message':'user promoted'})

#deleting auser

@users.route('/user/<user_id>',methods=['DELETE'])
def delete_user(public_id):
 
    User=User.query.filter_by(public_id=public_id).first()
    if not User:
     return jsonify({'message':'user not found'})
    
    
    db.session.delete(users)
    db.session.commit()
    return jsonify({'message':'user has been deletd'})


