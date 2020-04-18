from flask_restful import Api
from db import app
from resources.speaker import SpeakerApi, AddSpeaker, GetAllSpeakers

# Init API
api = Api(app)

# Run Flask App


def runApp():
    app.run(debug=True)


def speakerApi():
    api.add_resource(SpeakerApi, '/v1/speaker/<id>')
    # Add Speaker
    api.add_resource(AddSpeaker, '/v1/speaker')
    # Get all speakers
    api.add_resource(GetAllSpeakers, '/v1/speaker')
