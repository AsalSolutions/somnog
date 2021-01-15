from flask import request, jsonify
from flask_restful import Resource
from auth.User import User, Role, UserSchema
from db import db


user_schema = UserSchema()
user_schemas = UserSchema(many=True)


class UsersAPI(Resource):
  # This api updates,deletes and gets single speaker information

    # Get Single Speaker
    def get(self, id):
        user = User.query.get(id)
        if user:
            return user_schema.jsonify(user)
        return ({"message": "User not found"}), 404

    # Delete Single Speaker
    def delete(self, id):
        user = User.query.get(id)
        if user:
            user.delete()
            return ({"message": "User deleted sucessfully"}), 200

        return ({"message": "User not found"}), 404

    # !Permission required to modify this endpoint
    def put(self, id):
        # Get speaker by Id
        user = User.query.get(id)
        # If user exists update
        if user:
            user.first_name = request.json['username']
            user.last_name = request.json['email']
            user.email = request.json['password']
            user.update(user)
            return user_schema.jsonify(user)
        return {"message": "Sorry! could NOT update user"}, 405


class GetAndPostUsers(Resource):
    '''Returns all user as a json format '''

    def get(self):
        user = User.query.all()
        result = user_schemas.dump(user)
        print(result)
        return jsonify(result)

    def post(self):

        user = User(
            username=request.json['username'], email=request.json['email'], password=request.json['password'])
        if user:
            # Get users role
            role = Role.query.filter_by(name="User").first()
            user.role = role
            # Hash Password
            hashed_pwd = user.generate_hash(request.json['password'])
            user.password = hashed_pwd
            # Save to database
            user.create()
            return user_schema.jsonify(user)
        return {"message": "could not add user to the database"}, 405
