import datetime
from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (verify_jwt_in_request, get_jwt_claims, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from functools import wraps
from api.auth.User import User, Role, UserSchema, RevokedTokenModel
from api import db, jwt

"""TODO:
get authorization header from the react app
and verify then allow it to access
token = request.headers['authorization'].split(" ")[1]
verify_jwt_token(token,'access_token')
then do staff
 """

# Custome JWT Decorator For Admin Users


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        role = Role.query.filter_by(name="Admin").first()
        # Check if if the current user is Admin
        current_user = User.query.filter_by(
            username=get_jwt_identity()).first()
        # Only then this we can perform admin tasks
        if current_user.role.name == role.name:
            return fn(*args, **kwargs)
        else:
            return {"msg": "You're NOT allowed to perform this action!"}, 403

    return wrapper


# Database Model Serializers
user_schema = UserSchema()
user_schemas = UserSchema(many=True)

# Reqparse
parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=False)
parser.add_argument('email', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)


# Check Blacklisted Tokens
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


class UsersAPI(Resource):
    @jwt_required
    def get(self, id):
        user = User.query.get(id)
        if user:
            user_data = user_schema.dump(user)
            return ({'success': True, **user_data}), 200
        return ({"success": False, "message": "User not found"}), 404

    @admin_required
    def delete(self, id):
        current_user = User.query.get(id)
        if current_user:
            current_user.delete()
            return ({"message": "User deleted sucessfully"}), 200

        return ({"message": "User not found"}), 404

    @admin_required
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

    @admin_required
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
            # expires = datetime.timedelta(days=5)  # Token Expiration
            # access_token = create_access_token(
            #     identity=current_user.id, expires_delta=expires)
            # refresh_token = create_refresh_token(identity=current_user.id)
            return {
                'success': True,
                'message': f'User {username} was created. Please log in',
            }, 201
            # return user_schema.jsonify(current_user)
        return {"success": False, "message": "could not add user to the database"}, 405


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        email = data['email']
        password = data['password']
        current_user = User.find_by_email(email)

        # set session http only

        # Check if email exists
        if not current_user:
            return {'message': 'Invalid email or password'}
        # Check if current user's password matches hashed password
        if User.verify_hash(current_user.password, password):
            # Create Access token if user created successfully
            # !Access token we need to access protected routes.
            #! Refresh token we need to reissue access token when it will expire.
            expires = datetime.timedelta(days=5)  # Token Expiration
            payload = {'payload': {
                'role': current_user.role.name,
                'id': current_user.id
            }}
            access_token = create_access_token(
                identity=payload, expires_delta=expires)
            refresh_token = create_refresh_token(
                identity=current_user.id)
            return {
                'success': True,
                'role': current_user.role.name,
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return {'success': False, 'message': 'Invalid email or password'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {
                'success': True,
                'message': 'Access token has been revoked'}, 200
        except:
            return {
                'success': False,
                'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    """ 
    tokens have an expiration date. By default, access tokens have 15 minutes lifetime, 
    refresh tokens — 30 days. In order not to ask users to log in too often after access 
    token expiration we can reissue new access token using refresh token
    """
    @jwt_refresh_token_required
    def post(self):
        """
            first of all, this resource has jwt_refresh_token_required decorator,
            which means that you can access this path only using refresh token.
            By the way, you cannot access jwt_required endpoints using refresh token,
            and you cannot access jwt_refresh_token_required endpoints using access token.
            This adds an additional layer of security. To identify user we use helper 
            function get_jwt_identity() which extract identity from refresh token. 
            Then we use this identity to generate a new access token and return it to the user.
        """
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }
