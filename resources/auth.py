from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, session, jsonify, make_response
from flask_cors import CORS, cross_origin
from flask_restful import Resource
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from models.user import User
import os

load_dotenv()

bcrypt = Bcrypt()

SALT_ROUNDS = os.environ.get('SALT_ROUNDS')

class Signup(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def post(self):
      body = request.get_json()
      email = User.objects(email=body.get("email")).first()
      if email:
          return {"message": "Email already exists"}, 500
      hashed = bcrypt.generate_password_hash(
          body.get("password"), int(SALT_ROUNDS))
      user = User()
      user.email = body.get("email")
      user.password = hashed
      user.save()
      return {"message": "User created"}, 200

class Signin(Resource):
    def post(self):
      body = request.get_json()
      user = User.objects(email=body.get("email")).first()
      if user:
        if bcrypt.check_password_hash(user["password"], body.get("password")):
          session['email'] = body.get('email')
          access_token = create_access_token(identity=body.get("email"))
          return make_response(jsonify(access_token=access_token, user=user, message="User logged in"), 200)
        return {"message": "Email & Password combination is wrong"}, 500
      return {"message": "User does not exist"}, 500
    
class CheckSession(Resource):
    @jwt_required()
    def get(self):
      current_user = get_jwt_identity()
      user = User.objects(email=current_user).first()
      if user:
        return make_response(jsonify(user), 200)
      return {"message": "User not authenticated"}, 404
       
class Logout(Resource):
    def post(self):
      session.pop("email", None)
      return {"message": "User logged out"}, 200