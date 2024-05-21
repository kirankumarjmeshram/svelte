from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_pymongo import PyMongo
from config import Config
from models import User
from bson import ObjectId

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mongo = PyMongo(app)
app.db = mongo.db

@app.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if User.find_by_email(email):
        return jsonify({'error':'User already exists'}), 400
    new_user = User(email=email, name=name, password=password)
    new_user.save()
    response = {
        'user':{
            'id':new_user.id,
            'email':new_user.email,
            'name':new_user.name
        }
    }

    res = make_response(jsonify(response), 200)
    res.header['Authorization'] = new_user.generate_auth_token()
    return res

@app.route('/users/sign_in', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.find_by_email(email)

    if user is None or not user.check_passord(password):
        return jsonify({'error':'Invalid email or password'}), 400
    
    response = {
        'user':{
            'id': user.id,
            'email':user.email,
            'name':user.name
        }
    }

    res = make_response(jsonify(response), 200)
    res.headers['Authorization'] = user.generate_auth_token()
    return res
if __name__ == '__main__':
    app.run(debug = True, port = 3000)
