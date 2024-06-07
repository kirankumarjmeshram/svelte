from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from config import Config
from models import User
# import jwt
# import datetime
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# from db import mongodata as mongo
# db = mongo().db
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# mongo = PyMongo(app)
# app.db = mongo.db

# Initialize MongoDB client
client = MongoClient(app.config['MONGO_URI'])
app.db = client[app.config['MONGO_DBNAME']]


# @app.route('/users', methods=['POST'])
# def signup():
#     # coll = db['users']
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     name = data.get('name')
#     print(list(data))

#     if User.find_by_email(email):
#         return jsonify({'error':'User already exists'}), 400

#     # if coll.find_one({'email':email}):
#     #     return jsonify({'error':'User already exists'}), 400
#     # coll.insert_one({
#     #     'email' : email,
#     #     'name' : name,
#     #     'password' : generate_password_hash(password),
#     # })
#     new_user = User(email=email, name=name, password=password)
#     new_user.save()
#     response = {
#         'user':{
#             'id':new_user.id,
#             'email':new_user.email,
#             'name':new_user.name
#         }
#     }

#     res = make_response(jsonify(response), 200)
#     res.headers['Authorization'] = new_user.generate_auth_token()
#     return res
#     # return jsonify({'msg' : 'user creation done.....!'})

@app.route('/users', methods=['POST'])
def signup():
    try:
        #Received data:  {'user': {'email': 'kirankumar1@gmail.com', 'password': '123', 'name': 'kkd'}}
        #Received data:  None None None
        data = request.get_json()
        # print("Received data: ",data)
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        # print("Received data: ",email, password, name)

        if not email or not password:
            return jsonify({'error': 'Email and password are required.'}), 400

        if User.find_by_email(email):
            return jsonify({'error': 'User already exists.'}), 400

        new_user = User(email=email, name=name, password=password)
        new_user.save()

        response = {
            'user': {
                'id': str(new_user.id),
                'email': new_user.email,
                'name': new_user.name
            }
        }

        res = make_response(jsonify(response), 200)
        res.headers['Authorization'] = new_user.generate_auth_token()
        return res

    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({'error': 'An unknown error occurred.'}), 500


@app.route('/users/sign_in', methods=['POST'])
def signin():
    # coll = db['users']
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print("Email",email,"password",password)

    user = User.find_by_email(email)
    print("data",data)

    # user = User.find_by_email(email)
    # # user = coll.find_one({'email':email})
    # checkpass = check_password_hash(user['password'], password)
    # if user is None and checkpass:
    #     return jsonify({'error':'Invalid email or password'}), 400
    
    if user is None:
        print("User not found")
    elif not user.check_password(password):
        print("Password check failed")
    
    if user is None or not user.check_password(password):
        return jsonify({'error':'Invalid email or password'}), 400
    
    response = {
        'user':{
            'id': user.id,
            'email':user.email,
            'name':user.name
        }
    }
    # response = {
    #         'id': str(user['_id']),
    #         'email':user['email'],
    #         'name':user['name']
    #     }

    res = make_response(jsonify(response), 200)
    res.headers['Authorization'] = user.generate_auth_token()
    # expires_in=6000
    # res.headers['Authorization'] = jwt.encode(
    #         {
    #             'id': str(user['_id']),
    #             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    #         },
    #         app.config['SECRET_KEY'],
    #         algorithm='HS256'
    #     )
    return res
if __name__ == '__main__':
    app.run(debug = True, port = 3000)
