from flask_restful import Api
from api import app
from api.resources.speaker import SpeakerAPI, SpeakerListAPI, TotalSpeakers
from api.resources.workshop import WorkshopAPI, WorkshopListAPI
from api.auth.resources import UsersAPI, GetAndPostUsers, UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, SecretResource
from api.event.resource import EventAPI, GetAndPostEvents


# Init API
api = Api(app)
BASE_URL = '/api/v1.0/'


def speakers_endpoint():
    # This api updates,deletes and gets single speaker information
    api.add_resource(SpeakerAPI, BASE_URL + 'speakers/<id>')
    # Fetches All speakers and adds new speakers to the api
    api.add_resource(SpeakerListAPI, BASE_URL + 'speakers')


def users_endpoint():
    # This api updates,deletes and gets single user information
    api.add_resource(UsersAPI, BASE_URL + 'users/<id>')
    # Fetches All users and POSTs new users to the api
    api.add_resource(GetAndPostUsers, BASE_URL + 'users')
    # User Login Endpoint
    api.add_resource(UserLogin, BASE_URL + 'auth/login')
    # User Logout and Refreshers
    api.add_resource(UserLogoutAccess, BASE_URL + 'auth/logout/access')
    api.add_resource(UserLogoutRefresh, BASE_URL + 'auth/logout/refresh')
    api.add_resource(TokenRefresh, BASE_URL + 'auth/token/refresh')
    api.add_resource(SecretResource, BASE_URL + 'auth/secret')


def events_endpoint():
    api.add_resource(EventAPI, BASE_URL + "events/<id>")
    api.add_resource(GetAndPostEvents, BASE_URL + "events")


def workshops_endpoint():
    api.add_resource(WorkshopAPI, BASE_URL + "workshops/<id>")
    api.add_resource(WorkshopListAPI, BASE_URL + "workshops")
