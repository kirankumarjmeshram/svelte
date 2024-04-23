import os
import json
from flask import Flask 
from mongoengine import connect
from flask_jwt_extended import JWTManager


def load_config():
    current_directory = os.getcwd()
    config_path = os.path.join(current_directory, 'config.json')
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def create_folders(app):
    # Check if upload folder exists, if not, create it
    upload_folder = app.config['UPLOAD_FOLDER']
    victim_folder = os.path.join(upload_folder, app.config['VICTIM_FOLDER'])
    suspect_folder = os.path.join(upload_folder, app.config['SUSPECT_FOLDER'])
    uploaded_data_folder = os.path.join(upload_folder, app.config['UPLOADED_DATA_FOLDER'])
    print(upload_folder)
    print(victim_folder)
    print(suspect_folder)
    print(uploaded_data_folder)
    app.config['VICTIM_FOLDER'] = victim_folder
    app.config['SUSPECT_FOLDER'] = suspect_folder
    app.config['UPLOADED_DATA_FOLDER'] = uploaded_data_folder


    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    # Check if victim folder exists inside upload, if not, create it
    if not os.path.exists(victim_folder):
        os.makedirs(victim_folder)
    
    # Check if suspect folder exists inside upload, if not, create it
    if not os.path.exists(suspect_folder):
        os.makedirs(suspect_folder)

    # Check if suspect folder exists inside upload, if not, create it
    if not os.path.exists(uploaded_data_folder):
        os.makedirs(uploaded_data_folder)

def create_app(config=None):

    

    app = Flask(__name__)
    

    

    # Load configuration from JSON file
    if config is None:
        app.config.update(load_config())
    else:
        app.config.update(config)

    app.config['UPLOAD_FOLDER'] = 'upload'
    app.config['VICTIM_FOLDER'] = 'victim'
    app.config['SUSPECT_FOLDER'] = 'suspect'
    app.config['UPLOADED_DATA_FOLDER'] = 'uploaded_data'
    app.config['JWT_SECRET_KEY'] = '123asd,./'

    JWTManager(app)

    create_folders(app)

    #Database connection using 
    database = app.config['DATABASE']
    mongo_uri = app.config['MONGODB_URI']
    mongo_port = app.config['MONGO_PORT']
    connect(host=mongo_uri, db=database, port=mongo_port, alias='MARVEL')

    #Adding auth routes for authentication
    from .routes.auth import auth_routes
    app.register_blueprint(auth_routes)

    #Adding additional routes
    from .routes.routes import routes
    app.register_blueprint(routes)

    return app