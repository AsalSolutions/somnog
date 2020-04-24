from flask import request, jsonify
from flask_restful import Resource
from model.Speaker import SpeakerModel, SpeakerSchema
from db import db

#

speaker_schema = SpeakerSchema()
speaker_schemas = SpeakerSchema(many=True)


class SpeakerApi(Resource):

    # Add Speaker
    def post(self):

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
        newSpeaker = SpeakerModel(fistName, lastName, email, phone,
                                  description, companyName, jobTitle, photo, socialAccount)
        # Save to database
        newSpeaker.save()
        return speaker_schema.jsonify(newSpeaker)

    # Get Single Speaker
    def get(self, id):
        speaker = SpeakerModel.query.get(id)
        if speaker:
            return speaker_schema.jsonify(speaker)
        return ({"message": "Speaker not found"}), 404

    # Delete Single Speaker
    def delete(self, id):
        speaker = SpeakerModel.query.get(id)
        if speaker:
            speaker.delete()
            # db.session.delete(speaker)
            # db.session.commit()
            return ({"message": "Speaker deleted sucessfully"}), 200
        return ({"message": "speaker not found"}), 404


class GetAllSpeakers(Resource):
    def get(self):
        speakers = SpeakerModel.query.all()
        result = speaker_schemas.dump(speakers)
        return jsonify(result)
