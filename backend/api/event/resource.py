import datetime
from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (verify_jwt_in_request, get_jwt_claims, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from functools import wraps
from api.event.Event import Event, EventSchema
from api import db, jwt


# Custome JWT Decorator For Admin Users


# Database Model Serializers
event_schema = EventSchema()
event_schemas = EventSchema(many=True)

# Reqparse
parser = reqparse.RequestParser()
parser.add_argument(
    'name', help='This field cannot be blank', required=True)
parser.add_argument(
    'price', help='This field cannot be blank', required=True)
parser.add_argument(
    'start_date', help='This field cannot be blank', required=True)
parser.add_argument(
    'end_date', help='This field cannot be blank', required=True)


class EventAPI(Resource):
    # Admin required after testing this route
    def get(self, id):
        event = Event.query.get(id)
        if event:
            event_data = event_schema.dump(event)
            return ({'success': True, **event_data}), 200
        return ({"success": False, "message": "Event not found"}), 404

    def delete(self, id):
        event = Event.query.get(id)
        if event:
            event.delete()
            return ({"message": "Event deleted sucessfully"}), 200

        return ({"message": "Event not found"}), 404

    # @admin_required
    def put(self, id):
        event = Event.query.get(id)
        data = parser.parse_args()
        event_name = data['name']
        event_price = data['price']
        start_date = data['start_date']
        end_date = data['end_date']

        # Check if event already exist
        if Event.find_by_event_name(event_name):
            return {'message': f"Event {event_name} already exists"}
        # If user exists update
        if event:
            event.name = event_name
            event.start_date = start_date
            event.end_date = end_date
            event.price = event_price
            event.update()
            return event_schema.jsonify(event)
        return {"message": "Sorry! could NOT update Event"}, 405


class GetAndPostEvents(Resource):
    '''Returns all user as a json format '''

    def get(self):
        event = Event.query.all()
        data = event_schemas.jsonify(event)
        print(data)
        return {data}

    # @admin_required
    def post(self):
        data = parser.parse_args()
        event_name = data['name']
        event_price = data['price']
        start_date = data['start_date']
        end_date = data['end_date']

        # Check if user's username already exist
        if Event.find_by_event_name(event_name):
            return {'message': f"Event {event_name} already exists"}

        current_event = Event(name=event_name, price=event_price,
                              start_date=start_date, end_date=end_date)
        if current_event:
            # Save to database
            current_event.save()
            event_data = event_schema.dump(current_event)
            return {"success": True, **event_data}
        return {"success": False, "message": "could not add user to the database"}, 405
