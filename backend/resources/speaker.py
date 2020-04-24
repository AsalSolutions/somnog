from flask import request, jsonify
from flask_restful import Resource
from model.Speaker import Speaker, SpeakerSchema
from db import db


speaker_schema = SpeakerSchema()
speaker_schemas = SpeakerSchema(many=True)


class SpeakerApi(Resource):
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
            db.session.delete(speaker)
            db.session.commit()
            return ({"message": "Speaker deleted sucessfully"}), 200
        return ({"message": "speaker not found"}), 404


class AddSpeaker(Resource):
    def validate(self):
        pass

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
        newSpeaker = Speaker(fistName, lastName, email, phone,
                             description, companyName, jobTitle, photo, socialAccount)
        # Save to database
        newSpeaker.save()
        return speaker_schema.jsonify(newSpeaker)


class GetAllSpeakers(Resource):
    def get(self):
        speakers = Speaker.query.all()
        result = speaker_schemas.dump(speakers)
        return jsonify(result)
