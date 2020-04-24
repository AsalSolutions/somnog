from flask_restful import Api
from db import app
from resources.speaker import SpeakerApi, GetAllSpeakers

# Init API
api = Api(app)

# Run Flask App


def runApp():
    app.run(debug=True)


def speakersApi():
    api.add_resource(SpeakerApi, '/api/v1/speakers/<id>')
    # Get all speakers
    api.add_resource(GetAllSpeakers, '/api/v1/speakers')
