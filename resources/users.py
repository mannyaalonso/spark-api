from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.user import User

    
class Users(Resource):
    @jwt_required()
    def get(self):
      current_user = get_jwt_identity()
      user = User.objects(email=current_user).first()
      if user:
        users = User.objects()
        return make_response(jsonify(users), 200)
      return {'message': 'Profile not found'}, 404
    
class SingleUser(Resource):
    @jwt_required()
    def get(self, id):
      current_user = get_jwt_identity()
      user = User.objects(email=current_user).first()
      id = User.objects(id=id)
      if user and id:
        return make_response(jsonify(id), 200)
      return {"message": "User id didn't match or user isn't authenticated"}, 404
      
    @jwt_required()
    def put(self, id):
      current_user = get_jwt_identity()
      user = User.objects(email=current_user).first()
      id = User.objects(id=id)
      if user and id:
        body = request.get_json()
        id.update(**body)
        return make_response(jsonify(id), 200)
      return {"message": "User id didn't match"}, 404

    @jwt_required()
    def delete(self, id):
      current_user = get_jwt_identity()
      user = User.objects(email=current_user).first()
      id = User.objects(id=id)
      if user and id:
        id.delete()
        return make_response(jsonify(id), 200)
      return {"message": "User id didn't match"}, 404
