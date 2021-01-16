from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from auth.User import User, Role, UserSchema
from db import db


user_schema = UserSchema()
user_schemas = UserSchema(many=True)


# Reqparse
parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=False)
parser.add_argument('email', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)


class UsersAPI(Resource):

    def get(self, id):
        user = User.query.get(id)
        if user:
            return user_schema.jsonify(user)
        return ({"message": "User not found"}), 404

    # !Permission required to modify this endpoint
    def delete(self, id):
        current_user = User.query.get(id)
        if current_user:
            current_user.delete()
            return ({"message": "User deleted sucessfully"}), 200

        return ({"message": "User not found"}), 404

    # !Permission required to modify this endpoint
    def put(self, id):

        current_user = User.query.get(id)
        data = parser.parse_args()
        username = data['username']
        email = data['email']

        # Check if user's username already exist
        if User.find_by_username(username):
            return {'message': f"User {username} already exists"}
        # Check if user's email already exist
        if User.find_by_email(email):
            return {'message': f"Email {email} already exists"}
        # If user exists update
        if current_user:
            current_user.username = username
            current_user.email = email
            current_user.password = User.generate_hash(data['password'])
            current_user.update()
            return user_schema.jsonify(current_user)
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
            return {'message': f"Email {email} already exists"}

        current_user = User(username=username, email=email,
                            password=User.generate_hash(data['password']))
        if current_user:
            # Get users role
            current_user.role = Role.query.filter_by(name="User").first()
            # Save to database
            current_user.save()
            # Create Access token if user created successfully
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return {
                'message': f'User {username} was created',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            # return user_schema.jsonify(current_user)
        return {"message": "could not add user to the database"}, 405


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        email = data['email']
        password = data['password']
        current_user = User.find_by_email(email)

        # Check if email exists
        if not current_user:
            return {'message': 'Invalid email or password'}
        # Check if current user's password matches hashed password
        if User.verify_hash(current_user.password, password):
            # Create Access token if user created successfully
            # !Access token we need to access protected routes.
            #! Refresh token we need to reissue access token when it will expire.
            access_token = create_access_token(identity=current_user.username)
            refresh_token = create_refresh_token(
                identity=current_user.username)
            return {
                'message': f'Logged in as {current_user.username}',
                'access_token': access_token,
                'refresh_token': refresh_token
            }

        else:
            return {'message': 'Invalid email or password'}


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
