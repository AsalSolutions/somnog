from flask_restful import Api
from db import app
from resources.speaker import SpeakerApi, AddSpeaker, GetAllSpeakers

# Init API
api = Api(app)

# Run Flask App


def runApp():
    app.run(debug=True)


def speakersApi():
    # This api updates,deletes and gets single speaker information
    api.add_resource(SpeakerApi, '/api/v1/speakers/<id>')
    # This api Adds new speaker to speakers list
    api.add_resource(AddSpeaker, '/api/v1/speakers')
    # This api gets all speakers
    api.add_resource(GetAllSpeakers, '/api/v1/speakers')
