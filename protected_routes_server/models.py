from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from bson import ObjectId

class User:
    def __init__(self, email, name, password=None, _id=None):
        self.email = email
        self.name = name
        if password:
            self.password_hash = generate_password_hash(password)
        self.id = _id
    
    @staticmethod
    def find_by_email(email):
        user_data = app.db.users.find_one({'email': email})
        if user_data:
            # '**' Keyword Argument Unpacking
            del user_data["_id"]
            return User(**user_data)
        return None
    
    def save(self):
        user_data = {
            'email': self.email,
            'name': self.name,
            'password_hash': self.password_hash,
        }
        if self.id:
            app.db.users.update_one({'_id':ObjectId(self.id)}, {'$set': user_data})
        else:
            result = app.db.users.insert_one(user_data)
            self.id = str(result.inserted_id)

    def check_passord(self, password):
        return check_password_hash(self.password_hash, password)
    
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
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms='HS256')
            return data['id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

