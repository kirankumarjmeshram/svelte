from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from bson import ObjectId


class User:

    def __init__(self, email, name, password=None, _id=None, db_password_hash=None):
        self.email = email
        self.name = name
        if password:
            # self.password_hash = generate_password_hash(password)
            self.set_password(password)
        self.id = _id
        self.db_password_hash = db_password_hash
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.db_password_hash, password)
    
    @staticmethod
    def find_by_email(email):
        user_data = app.db.users.find_one({'email': email})
        if user_data:
            # '**' Keyword Argument Unpacking
            # del user_data["_id"]
            # return User(**user_data)
            return User(email=user_data['email'], name=user_data['name'], db_password_hash=user_data.get('password_hash'), _id=str(user_data['_id']))
        
        return None
    
        #  user_data = app.db.users.find_one({'email': email})
        # if user_data:
        #     return User(
        #         email=user_data['email'],
        #         name=user_data['name'],
        #         password=user_data.get('password_hash'),
        #         _id=str(user_data['_id'])  # Correctly access the _id
        #     )
        # return None
    
    
    def save(self):
        user_data = {
            'email': self.email,
            'name': self.name,
            'password_hash': self.db_password_hash
        }
        if self.id:
            app.db.users.update_one({'_id':ObjectId(self.id)}, {'$set': user_data})
        else:
            result = app.db.users.insert_one(user_data)
            self.id = str(result.inserted_id)


    # def generate_auth_token(self, expires_in = 600):
    #     return jwt.encode(
    #         {
    #         'id': self.id,
    #         'exp': datetime.datetime.utcnow() +datetime.timedelta(seconds=expires_in)
    #         },
    #         app.config['SECRET_KEY'], algorithm='HS256'
    #     ).decode('utf-8')
    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {
                'id': str(self.id),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
            },
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
    
    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            return data['id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

