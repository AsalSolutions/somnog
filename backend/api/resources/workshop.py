from flask import request, jsonify
from flask_restful import Resource
from api.model.Workshop import Workshop, WorkshopModelSchema
from api import db


workshopSchema = WorkshopModelSchema()
workshopSchemas = WorkshopModelSchema(many=True)


class WorkshopAPI(Resource):
    # Get a Single Workshop
    def get(self, id):
        workshop = Workshop.query.get(id)
        if workshop:
            return workshopSchema.jsonify(workshop)
        return ({"message": "Workshop not found"}), 404

    # Delete a workshop by id
    def delete(self, id):
        workshop = Workshop.query.get(id)
        if workshop:
            workshop.delete()
            return ({"message": "workshop deleted successfully"}), 200
        return ({"message": "Workshop not found"}), 404

    def patch(self, id):
        workshop = Workshop.query.get_or_404(id)
        # if 'workshopTitle' in request.json['workshopTitle']:
        #     workshop.workshopTitle = request.json['workshopTitle']


class WorkshopListAPI(Resource):

    # List all workshops
    def get(self):
        workshops = Workshop.query.all()
        result = workshopSchemas.dump(workshops)
        return jsonify(result)

    # Add New Workshops
    def post(self):
        # Get Workshop Information
        workshopTitle = request.json['workshopTitle']
        description = request.json['description']
        # startDate = request.json['startDate']
        # endDate = request.json['endDate']
        location = request.json['location']
        course_image = request.json['course_image']
        lecturer_id = request.json['lecturer_id']

        # init object from Speaker class
        newWorkshop = Workshop(workshopTitle=workshopTitle, description=description,
                               location=location, course_image=course_image, lecturer_id=lecturer_id)
        if newWorkshop:
            # Save to database
            newWorkshop.save()
            return workshopSchema.jsonify(newWorkshop)
        return {"message": "could not add workshop to the database"}, 405
