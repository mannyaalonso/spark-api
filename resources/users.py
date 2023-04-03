from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.user import User
from mongoengine import *
from geojson import Point, Feature, FeatureCollection

    
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
    
class UserLocation(Resource):
  @jwt_required()
  def get(self):
    current_user = get_jwt_identity()
    user = User.objects(email=current_user).first()
    if user:
      latitude = request.args.get('lat')
      longitude = request.args.get('long')
      distance_in_meters = float(request.args.get('distance', 10000))

      point = Point((float(longitude), float(latitude)))
      query = {'location': {
          '$near': {'$geometry': point, '$maxDistance': distance_in_meters}}}

      features = []
      for document in User.objects(__raw__=query):
        feature = Feature(geometry=document.location,
                          properties={'id': str(document.id), 'vitals': document.vitals, 'vices': document.vices, 'virtues': document.virtues, 'prompts': document.prompts, 'images': document.images, 'location': document.location})
        features.append(feature)

      feature_collection = FeatureCollection(features)
      return make_response(jsonify(feature_collection))

