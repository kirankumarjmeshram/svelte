import os
import uuid
from flask import jsonify, current_app
from ..models.marvel import Users, Cases
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_case_controller(data,victim_images,suspect_images):
    try:
        print("create case controller function triggered")
        print(data,"data of user")
        casename = data['case_name']
        current_directory = os.getcwd()
        upload_f = os.path.join(current_directory,current_app.config['UPLOAD_FOLDER'])
        # print(upload_f,"upload fodler path")
        victim_f = os.path.join(current_directory,current_app.config['VICTIM_FOLDER'])
        # print(victim_f,"victim fodler path")
        suspect_f = os.path.join(current_directory,current_app.config['SUSPECT_FOLDER'])
        # print(suspect_f,"suspect fodler path")
        # print(current_directory,"current working directory")
        # print("list of images",victim_images)
        # print("list of suspect images",suspect_images)
        victim_result_list = save_files(victim_images,victim_f)
        print(victim_result_list,"result list of victim")
        suspect_result_list = save_files(suspect_images,suspect_f)
        print(suspect_result_list,"result list of suspect")
        db_entry = {
            "_id"               : str(uuid.uuid4()),
            "user_id"           : "",
            "case_name"          : casename,
            "victim_images"     : victim_result_list,
            "suspect_images"    : suspect_result_list
        }
        print(db_entry,"object of db entry")
        case = Cases(**db_entry)
        case.save()
        return jsonify({"Service" : "Create case", "Status" : True}), 200
    except Exception as error:
        return jsonify({"Service" : "Create case", "Message" : str(error)})

def save_files(list_array,folder):
    result_list = []
    for file in list_array:
        if file.filename == '':
            continue
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            if not os.path.exists(folder):
                os.makedirs(folder)
            file_path = os.path.join(folder, filename)
            # print(file_path,"file path before saving")
            file.save(file_path)
            result_list.append(file_path)
        else:
            return 'Invalid file format for files'
    
    return result_list

def list_cases():
    all_documents = Cases.objects()
    cases = [doc.to_json() for doc in all_documents]
    return jsonify({"Service" : "Cases", "data" : cases}), 200

def data_upload_controller(uploaded_data,user_cred):
    try:
        print("data upload controller fucntion is triggered")
        current_directory = os.getcwd()
        uploaded_data_f = os.path.join(current_directory,current_app.config['UPLOADED_DATA_FOLDER'])
        result = save_files(uploaded_data,uploaded_data_f)
        print(result,"result for ")
        user_case = Cases.objects(user_id=user_cred).update(set__uploaded_data=result)
        print(user_case,"result of user ")
        return jsonify({"Service" : "Data upload","Status" : True})
    except Exception as error:
        return jsonify({"Service" : "Data upload","Message" : str(error)})