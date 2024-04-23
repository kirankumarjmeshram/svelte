from flask import Blueprint, request, jsonify
from ..controller import routes as route_controller
from flask_jwt_extended import get_jwt_identity, jwt_required

routes = Blueprint('routes',__name__)

#route to create a case
@routes.route('/create_case', methods=['POST','GET'])
def create_case():
    try:
        print("Create case function triggered")
        data = request.form
        # print(data,"data of user for case creation")
        victim_images = request.files.getlist('victim_images') if 'victim_images' in request.files else []
        suspect_images = request.files.getlist('suspect_images')if 'suspect_images' in request.files else []

        # print(files,"files data of user for case creation")
        result = route_controller.create_case_controller(data,victim_images,suspect_images)
        
        return result
    except Exception as error:
        return jsonify({"Service":"Create case","message" : str(error)}), 500

#route to list existing cases
@routes.route('/cases', methods=['POST','GET'])
def cases():
    try:
        print("Cases function triggered")
        result = route_controller.list_cases()
        return result
    except Exception as error:
        return jsonify({"Service":"Cases","message" : str(error)})

#route to upload data to a particular case
@routes.route('/data_upload', methods=['POST','GET'])
@jwt_required()
def data_upload():
    try:
        print("Data upload function triggered")
        user_cred = get_jwt_identity()
        print(user_cred,"user credentials")
        uploaded_images = request.files.getlist('uploaded_images') if 'uploaded_images' in request.files else []
        print(uploaded_images,"uploaded images")
        result = route_controller.data_upload_controller(uploaded_images,user_cred)
        return result
    except Exception as error:
        return jsonify({"Service":"Data uplaod","message" : str(error)}), 500

#route to analyse data 
@routes.route('/analyse', methods=['POST','GET'])
def analyse():
    try:
        print("Analyse function triggered")
        return jsonify({'Service' : "Analyse page","Status" : True})
    except Exception as error:
        return jsonify({"Service":"Analyse","message" : str(error)})