from flask import request, jsonify
from flask_restful import Resource
from model.Workshop import Workshop, WorkshopModelSchema
from db import db


workshopSchema = WorkshopModelSchema()
workshopSchemas = WorkshopModelSchema(many=True)


class WorkshopAPI(Resource):
    def get(self,id):
        workshop = Workshop.query.get(id)
        if workshop:
            return workshopSchema.jsonify(workshop)
        return ({"message":"Workshop not found"}),404
    
    
class AddWorkshop(Resource):
    # Add Speaker
    def post(self):

        # Get Speaker information
        workshopTitle = request.json['workshopTitle']
        lastName = request.json['lastName']
        email = request.json['email']
        phone = request.json['phone']
        description = request.json['description']
        companyName = request.json['companyName']
        jobTitle = request.json['jobTitle']
        photo = request.json['photo']
        socialAccount = request.json['socialAccount']

        # init object from Speaker class
        newSpeaker = Speaker(firstName, lastName, email, phone,
                             description, companyName, jobTitle, photo, socialAccount)
        if newSpeaker:
            # Save to database
            newSpeaker.save()
            return speaker_schema.jsonify(newSpeaker)
        return {"message": "could not add speaker to the database"}, 405




