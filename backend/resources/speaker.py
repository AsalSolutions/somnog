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
        updateSpeaker = Speaker.query.get(id)
        # updateSpeaker = request.form['data']
    
        # Get information from user
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        email = request.json['email']
        phone = request.json['phone']
        description = request.json['description']
        companyName = request.json['companyName']
        jobTitle = request.json['jobTitle']
        speakerPhoto = request.json['speakerPhoto']
        website = request.json['website']
        print(firstName,lastName,email,phone,description,companyName,jobTitle,speakerPhoto,website)
        

        if updateSpeaker:
            updateSpeaker.firstName = firstName
            updateSpeaker.lastName = lastName
            updateSpeaker.email = email
            updateSpeaker.phone = phone
            updateSpeaker.companyName = companyName
            updateSpeaker.jobTitle = jobTitle
            updateSpeaker.description = description
            updateSpeaker.speakerPhoto = speakerPhoto
            updateSpeaker.website = website
           
            Speaker.update(updateSpeaker)
            return speaker_schema.jsonify(updateSpeaker)
        return {"message": "Sorry! could NOT update speaker"}, 405


# Get Total Number of Speakers
class TotalSpeakers(Resource):
    def get(self):
        count = Speaker.query.count()
        return {"speakerCount":count}

class SpeakerListAPI(Resource):
    '''Returns all speakers as a json format '''

    def get(self):
        speakers = Speaker.query.all()
        result = speaker_schemas.dump(speakers)
        return jsonify(result)
    
    def post(self):
        # Get Speaker information
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        email = request.json['email']
        phone = request.json['phone']
        description = request.json['description']
        companyName = request.json['companyName']
        jobTitle = request.json['jobTitle']
        speakerPhoto = request.json['speakerPhoto']
        website = request.json['website']

        # init object from Speaker class
        newSpeaker = Speaker(firstName=firstName, lastName=lastName, email=email, phone=phone,
                             description=description, companyName=companyName, jobTitle=jobTitle, speakerPhoto=speakerPhoto, website=website)
        if newSpeaker:
            # Save to database
            newSpeaker.save()
            return speaker_schema.jsonify(newSpeaker)
        return {"message": "could not add speaker to the database"}, 405

        




    