from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
from bson import json_util, ObjectId
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,  verify_jwt_in_request, decode_token
import uuid
from mongoengine import Document, StringField, connect

app = Flask(__name__)

CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/upload"
print(app.config['UPLOAD_FOLDER'])
mongo = PyMongo(app)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!
jwt = JWTManager(app)

connect(alias='MARVEL', host='mongodb://localhost:27017/mydatabase')


class Users(Document):
    _id = StringField(primary_key=True, required=False)
    username = StringField(required=True)
    hashed_pwd = StringField()
    status = StringField()

    meta = {'db_alias': 'MARVEL'}


@app.route('/', methods=["GET"])
def started():
    return "<h1>Case Server Started"


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    try:
        # Extract user identity from JWT token
        current_user_id = get_jwt_identity()

        # Debugging: Print received token
        auth_header = request.headers.get('Authorization')
        token = auth_header.split()[1]  # Extract token part after 'Bearer'
        print("Received token:", token)

        # Verify and decode token to inspect payload
        decoded_token = decode_token(token)
        print("Decoded token payload:", decoded_token)

        # Respond with success message and user identity
        return jsonify(message="Token is valid", user_id=current_user_id), 200

    except Exception as e:
        # Handle any errors or exceptions
        print("Error:", str(e))
        return jsonify(error="An error occurred while processing the request"), 500

# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     auth_header = request.headers.get('Authorization')
#     token = auth_header.split()[1]
#     decoded_token = decode_token(token)
#     user_id = decoded_token['identity']
#     return jsonify(message="Token is valid", user_id=user_id), 200


@app.route("/data", methods=["POST"])
def create_data():
    verify_jwt_in_request()  
    current_user_id = get_jwt_identity() 
    data = request.json
    title = data.get("title") 
    if title is None:
        return jsonify({"error": "Title is required"}), 400  
    data.setdefault("totalFiles", [])
    data["created_by"] = current_user_id
    data.setdefault("totalDocuments", [])  
    data["lastUploadedDate"] = datetime.now().strftime("%Y-%m-%d")
    data["lastUploadedTime"] = datetime.now().strftime("%H:%M:%S")
    result = mongo.db.data.insert_one(data)
    return jsonify({"message": "Data created successfully", "id": str(result.inserted_id)}), 201



@app.route("/data", methods=["GET"])
def get_all_data():
    data = list(mongo.db.data.find({}))[::-1]
    for document in data:
        document['_id'] = str(document['_id'])
    json_data = json_util.dumps(data)
    return json_data, 200


@app.route("/data/<id>", methods=["GET"])
def get_data(id):
    obj_id = ObjectId(id)
    data = mongo.db.data.find_one({"_id": obj_id}, {"_id": 0})
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"message": "Data not found"}), 404

    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx', 'xlsv'}


@app.route("/data/<id>", methods=["PUT"])
def update_data(id):
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            print(file.filename)
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            file_details = {
                "filename": filename,
                "filepath": filepath,
                "size": os.path.getsize(filepath),
                "type": file.content_type
            }
            result = mongo.db.data.update_one({"_id": ObjectId(id)}, {"$push": {"totalFiles": file_details}, "$set":{
                                                                        "lastUploadedDate" : datetime.now().strftime("%Y-%m-%d"),
                                                                        "lastUploadedTime" : datetime.now().strftime("%H:%M:%S")
                                                                    }})
            if result.modified_count:
                return jsonify({"message": "Data updated successfully"}), 200
            else:
                return jsonify({"message": "Data not found"}), 404
        else:
            return jsonify({"error": "Invalid file format"}), 400
    else:
        return jsonify({"error": "No file part in request"}), 400

    
@app.route("/data/<id>", methods=["DELETE"])
def delete_data(id):
    result = mongo.db.data.delete_one({"_id": id})
    if result.deleted_count:
        return jsonify({"message": "Data deleted successfully"}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

# Authentication Routes


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = Users.objects(username=username).first()
    if not user or not check_password_hash(user.hashed_pwd, password):
        return jsonify({"message": "Invalid username or password"}), 401

    access_token = create_access_token(identity=user._id)
    return jsonify(access_token=access_token), 200


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    passcode = data.get("passcode")

    if passcode != "12345":
        return jsonify({"message": "Invalid passcode"}), 400

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if Users.objects(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)
    user_id = str(uuid.uuid4())
    user = Users(_id=user_id, username=username, hashed_pwd=hashed_password)
    user.save()

    return jsonify({"message": "User created successfully", "user_id": user_id}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5124)
