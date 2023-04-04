from flask_jwt_extended import JWTManager
from resources.users import Users, SingleUser, UserLocation
from resources.auth import Signin, Signup, Logout, CheckSession
from flask_session import Session
from dotenv import load_dotenv
from flask_restful import Api
from flask_cors import CORS, cross_origin
from mongoengine import *
from models.db import db
from flask import Flask
import datetime
import os


load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_URI = os.environ.get('MONGO_URI')


app = Flask(__name__)

CORS(app)
Session(app)
JWTManager(app)
api = Api(app)
db.init_app(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGODB_SETTINGS"] = {'DB': "spark", "host": MONGO_URI}
app.config['CORS_HEADERS'] = 'Content-Type'


api.add_resource(Users, '/users')
api.add_resource(Signup, '/signup')
api.add_resource(Signin, '/signin')
api.add_resource(Logout, '/logout')
api.add_resource(SingleUser, '/users/<id>')
api.add_resource(CheckSession, '/auth/session')
api.add_resource(UserLocation, '/users/location')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
