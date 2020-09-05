from flask_restful import Api
from db import app
from resources.speaker import SpeakerAPI, SpeakerListAPI,TotalSpeakers
from resources.workshop import WorkshopAPI


# Init API
api = Api(app)

# Run Flask App


def runApp():
    app.run(debug=True)


def speakersAPI():
    # This api updates,deletes and gets single speaker information
    api.add_resource(SpeakerAPI, '/api/v1.0/speakers/<id>',endpoint="speaker")
    # Fetches All speakers and adds new speakers to the api
    api.add_resource(SpeakerListAPI, '/api/v1.0/speakers',endpoint="speakers")
    # Get Total Speaker Count
    api.add_resource(TotalSpeakers,'/api/v1.0/speakers/count')


def workshopsAPI():
    api.add_resource(WorkshopAPI,"/api/v1.0/workshops/<id>")


