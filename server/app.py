from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
from bson import json_util, ObjectId
from werkzeug.utils import secure_filename

from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  
mongo = PyMongo(app)

@app.route('/',methods=["GET"])
def started():
    return "<h1>Case Server Started"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@app.route("/data", methods=["POST"])
def create_data():
    data = request.json
    title = data.get("title") 
    if title is None:
        return jsonify({"error": "Title is required"}), 400  
    data.setdefault("totalFiles", [])
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
    # Convert the id string to an ObjectId
    obj_id = ObjectId(id)
    data = mongo.db.data.find_one({"_id": obj_id}, {"_id": 0})
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"message": "Data not found"}), 404

@app.route("/data/<id>", methods=["PUT"])
def update_data(id):
    data = request.json
    data["lastUploadedDate"] = datetime.now().strftime("%Y-%m-%d")
    data["lastUploadedTime"] = datetime.now().strftime("%H:%M:%S")

    # Check if the POST request has a file part
    if 'file' in request.files:
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Update MongoDB document with file details
            file_details = {
                "filename": filename,
                "filepath": filepath,
                "size": os.path.getsize(filepath),
                "type": file.content_type
            }
            result = mongo.db.data.update_one({"_id": ObjectId(id)}, {"$push": {"totalFiles": file_details}})
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

if __name__ == "__main__":
    app.run(debug=True, port=5123)
