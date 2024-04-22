from flask import jsonify

def login_controller(username,password):
    print("login controller function triggered")
    print(username,password,"data of user")
    return jsonify({"Service" : True}), 200

def register_controller():
    print("register controller function triggered")
    return jsonify({"Service" : True})