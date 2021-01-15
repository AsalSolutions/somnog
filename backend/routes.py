from flask_restful import Api
from db import app
from resources.speaker import SpeakerAPI, SpeakerListAPI, TotalSpeakers
from resources.workshop import WorkshopAPI, WorkshopListAPI
from auth.resource import UsersAPI, GetAndPostUsers


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


def workshopsAPI():
    api.add_resource(WorkshopAPI, "/api/v1.0/workshops/<id>")
    api.add_resource(WorkshopListAPI, "/api/v1.0/workshops")
