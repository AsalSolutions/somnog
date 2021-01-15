from flask import request, jsonify
from flask_restful import Resource
from model.Speaker import Speaker, SpeakerModelSchema
from db import db


speaker_schema = SpeakerModelSchema()
speaker_schemas = SpeakerModelSchema(many=True)


class SpeakerAPI(Resource):
  # This api updates,deletes and gets single speaker information

    # Get Single Speaker
    def get(self, id):
        speaker = Speaker.query.get(id)
        if speaker:
            return speaker_schema.jsonify(speaker)
        return ({"message": "Speaker not found"}), 404

    # Delete Single Speaker
    def delete(self, id):
        speaker = Speaker.query.get(id)
        if speaker:
            speaker.delete()
            return ({"message": "Speaker deleted sucessfully"}), 200
        return ({"message": "speaker not found"}), 404

    def put(self, id):
        # Get speaker by Id
        speaker = Speaker.query.get(id)
        # If speaker exists update
        if speaker:
            speaker.first_name = request.json['first_name']
            speaker.last_name = request.json['last_name']
            speaker.email = request.json['last_name']
            speaker.phone = request.json['phone']
            speaker.last_name = request.json['last_name']
            speaker.last_name = request.json['last_name']
            speaker.description = request.json['description']
            speaker.speaker_photo = request.json['speaker_photo']
            speaker.website = request.json['website']
            Speaker.update(speaker)
            return speaker_schema.jsonify(speaker)
        return {"message": "Sorry! could NOT update speaker"}, 405


# Get Total Number of Speakers
class TotalSpeakers(Resource):
    def get(self):
        count = Speaker.query.count()
        return {"speakerCount": count}


class SpeakerListAPI(Resource):
    '''Returns all speakers as a json format '''

    def get(self):
        speakers = Speaker.query.all()
        result = speaker_schemas.dump(speakers)
        print(result)
        return jsonify(result)

    def post(self):
        # Get Speaker information

        # init object from Speaker class
        speaker = Speaker(first_name=request.json['first_name'], last_name=request.json['last_name'], email=request.json['email'], phone=request.json['phone'],
                          description=request.json['description'], company_name=request.json['company_name'], job_title=request.json['job_title'], speaker_photo=request.json['speaker_photo'], website=request.json['website'])
        if speaker:
            # Save to database
            speaker.save()
            return speaker_schema.jsonify(speaker)
        return {"message": "could not add speaker to the database"}, 405
