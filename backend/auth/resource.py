from flask import request, jsonify
from flask_restful import Resource, reqparse
from auth.User import User, Role, UserSchema
from db import db


user_schema = UserSchema()
user_schemas = UserSchema(many=True)


# Reqparse
parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=True)
parser.add_argument('email', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)


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
        # data
        data = parser.parse_args()
        # If user exists update
        if user:
            user.first_name = data['username']
            user.last_name = data['email']
            user.email = data['password']
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
        data = parser.parse_args()
        username = data['username']
        email = data['email']

        # Check if user's username already exist
        if User.find_by_username(username):
            return {'message': f"User {username} already exists"}
        # Check if user's email already exist
        if User.find_by_email(email):
            return {'message': f"User {email} already exists"}

        user = User(username=username, email=email,
                    password=User.generate_hash(data['password']))
        if user:
            # Get users role
            user.role = Role.query.filter_by(name="User").first()
            # Save to database
            user.create()
            return user_schema.jsonify(user)
        return {"message": "could not add user to the database"}, 405


class UserLogin(Resource):
    def post(self):
        pass


class UserLogout(Resource):
    def post(self):
        pass
