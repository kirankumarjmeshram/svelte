import uuid
from flask import Blueprint, jsonify, request, current_app
from flask_bcrypt import generate_password_hash, check_password_hash
from ..models.marvel import Users
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
import flask_cors
import jwt
from datetime import datetime, timedelta
cors_allowed_ip = "*"

from ..controller import auth

auth_routes = Blueprint('auth',__name__)

@auth_routes.route("/login", methods = ["POST", "GET"])
def login():
    try:
        print("login function triggered")
        data = request.json
        username = data.get("username")
        password = data.get("password")
        
        if username is None or password is None:
            return jsonify({"message" : "User credentials not found"}), 404
        print("line 24")
        if not Users.objects(username=username).first():
            return jsonify({"Service" : "Login","message" : "User not existed"}), 404
        
        print("line 28")
        user_data = Users.objects(username=username).first()
        print("line 30")
        if user_data['status'] == 'pending':
            return jsonify({"Service": "Login","message": "Please contact admin for approval"}), 404
        hashed_password = user_data['hashed_pwd']
        print(hashed_password,"hashed password")
        result = check_password_hash(hashed_password, password)
        print(current_app.config['SECRET_KEY'],"secret key ")
        if result:
            token = jwt.encode({
                    "username": username,
                    "exp": datetime.utcnow() + timedelta(minutes = 60)
                },
                current_app.config["SECRET_KEY"],
                "HS256"
            )
            return jsonify({"Service" : "Login","message" : "User login is successful","token": token}),200
        # auth.login_controller(username,password)
        return jsonify({"Service": True,"message" : result}), 200
    except Exception as Error:
        print("Error in registration",str(Error))
        return jsonify({"Service" : "Register","message" : str(Error)}), 500

@auth_routes.route("/register", methods = ["POST", "GET"])
def register():
    try:
        print("Register function triggered")
        data = request.json
        username = data.get("username")
        password = data.get("password")
        code = data.get("passcode")
        if code == "12345":
            if Users.objects(username=username).first():
                return jsonify({"Service":"Register","message": "User alredy existed"})
            hashed_password = generate_password_hash(password).decode('utf-8')
            user_data = {
                "_id"           : str(uuid.uuid4()),
                "username"      : username,
                "hashed_pwd"    : hashed_password,
                "status"        : "pending"
            }
            user = Users(**user_data)
            user.save()
            auth.register_controller()
            return jsonify({"Service": True,"message" : "User registered, contact admin for approval"})
        else:
            return jsonify({"Service" : "Register","Status": "Failed"})
    except Exception as Error:
        print("Error in registration",str(Error))
        return jsonify({"Service" : "Register","message" : str(Error)}), 500