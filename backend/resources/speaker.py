from flask import request, jsonify
from flask_restful import Resource
from model.Speaker import Speaker, SpeakerModelSchema
from db import db


speaker_schema = SpeakerModelSchema()
speaker_schemas = SpeakerModelSchema(many=True)


class SpeakerApi(Resource):
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


class GetAllSpeakers(Resource):
    '''Returns all speakers as a json format '''

    def get(self):
        speakers = Speaker.query.all()
        result = speaker_schemas.dump(speakers)
        return jsonify(result)


class AddSpeaker(Resource):
    # Add Speaker
    def post(self):

        # Get Speaker information
        fistName = request.json['firstName']
        lastName = request.json['lastName']
        email = request.json['email']
        phone = request.json['phone']
        description = request.json['description']
        companyName = request.json['companyName']
        jobTitle = request.json['jobTitle']
        photo = request.json['photo']
        socialAccount = request.json['socialAccount']

        # init object from Speaker class
        newSpeaker = Speaker(fistName, lastName, email, phone,
                             description, companyName, jobTitle, photo, socialAccount)
        if newSpeaker:
            # Save to database
            newSpeaker.save()
            return speaker_schema.jsonify(newSpeaker)
        return {"message": "could not add speaker to the database"}, 405
