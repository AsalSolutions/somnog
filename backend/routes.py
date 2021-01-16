from flask_restful import Api
from db import app
from resources.speaker import SpeakerAPI, SpeakerListAPI, TotalSpeakers
from resources.workshop import WorkshopAPI, WorkshopListAPI
from auth.resources import UsersAPI, GetAndPostUsers, UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, SecretResource


# Init API
api = Api(app)

# Run Flask App


def runApp():
    app.run(debug=True)


def speakersAPI():
    # This api updates,deletes and gets single speaker information
    api.add_resource(SpeakerAPI, '/api/v1.0/speakers/<id>')
    # Fetches All speakers and adds new speakers to the api
    api.add_resource(SpeakerListAPI, '/api/v1.0/speakers')


def users_endpoint():
    # This api updates,deletes and gets single user information
    api.add_resource(UsersAPI, '/api/v1.0/users/<id>')
    # Fetches All users and POSTs new users to the api
    api.add_resource(GetAndPostUsers, '/api/v1.0/users')
    # User Login Endpoint
    api.add_resource(UserLogin, '/api/v1.0/auth/login')
    # User Logout and Refreshers
    api.add_resource(UserLogoutAccess, '/api/v1.0/auth/logout/access')
    api.add_resource(UserLogoutRefresh, '/api/v1.0/auth/logout/refresh')
    api.add_resource(TokenRefresh, '/api/v1.0/auth/token/refresh')
    api.add_resource(SecretResource, '/api/v1.0/auth/secret')


def workshopsAPI():
    api.add_resource(WorkshopAPI, "/api/v1.0/workshops/<id>")
    api.add_resource(WorkshopListAPI, "/api/v1.0/workshops")
