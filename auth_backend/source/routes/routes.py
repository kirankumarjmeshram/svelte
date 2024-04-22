from flask import Blueprint, request, jsonify
from ..controller import routes as route_controller
from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager

routes = Blueprint('routes',__name__)

# jwt = JWTManager()

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
        return jsonify({"Service":"Create case","message" : str(error)})

#route to list existing cases
@routes.route('/cases', methods=['POST','GET'])
def cases():
    print("Cases function triggered")
    result = route_controller.list_cases()

    return result

#route to upload data to a particular case
@routes.route('/data_upload', methods=['POST','GET'])
# @jwt_required()
def data_upload():
    print("Data upload function triggered")
    # user_cred = get_jwt_identity()
    # print(user_cred,"user credentials")
    uploaded_images = request.files.getlist('uploaded_images') if 'uploaded_images' in request.files else []
    print(uploaded_images,"uploaded images")
    return jsonify({'Service' : "Home page","Status" : True})

#route to analyse data 
@routes.route('/analyse', methods=['POST','GET'])
def analyse():
    print("Analyse function triggered")
    return jsonify({'Service' : "Analyse page","Status" : True})