from flask_restful import Resource, reqparse
from app.api.v1.models.incidences_model import Incidences, incidences
from flask_jwt_extended import jwt_required
from app.api.v1.utils.validate_data import check_data


#Validate json data
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title', type=check_data, required=True, help="This field cannot be left blank." )
parser.add_argument('record_type', type=check_data, required=True, choices=("red-flag", "intervention"), 
                     help="This field cannot be left blank. Use either 'red-flag' OR 'intervention' : {error_msg}" )
parser.add_argument('location', type=check_data, help="This field can be left blank!" )
parser.add_argument('status', type=check_data, help="This field can be left blank!" )
parser.add_argument('images', type=check_data, action='append', help="This field can be left blank!" )
parser.add_argument('videos', type=check_data, action='append', help="This field can be left blank")
parser.add_argument('comment', type=check_data, required=True, help="This field cannot be left blank!" )

class IncidentRecords(Resource):
    # @jwt_required
    def get(self):
        if len(incidences) <= 0:
            return {"status" : 200, "Message" : "There are no incidence records."}, 200
        return { "status": 200, "data": [item.json_data() for item in Incidences.get_all()]}, 200
    
    # @jwt_required
    def post(self):
        data = parser.parse_args()

        new_record = Incidences(**data)
        new_record.save_to_incidences()

        return {"status": 201,
                "data": [{ "message": "Incident created Successfully.",
                    "id": new_record.id,
                    "title" : new_record.title,
                    "record_type" : new_record.record_type,
                    "location" : new_record.location,
                    "status" : new_record.status,
                    "images" : new_record.images,
                    "videos" : new_record.videos,
                    "comment" : new_record.comment
                }]}, 201


class IncidentRecord(Resource):
    # @jwt_required
    def get(self, incident_id):
        incident = Incidences.find_by_id(incident_id)
        if incident:
            return {"status": 200,
                    "data": [incident.json_data()]
                    }, 200

        return {"status": 404, "data": [{
                     "message": "Incident record does not exist."
                }]}, 404

    # @jwt_required
    def put(self, incident_id):
        data = parser.parse_args()
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.update_all(data["title"])
            incident.update_all(data['record_type'])
            incident.update_all(data['location'])
            incident.update_all(data['status'])
            incident.update_all(data['images'])
            incident.update_all(data['videos'])
            incident.save_to_incidences()
            return {
                      "status": 200,
                      "data": [{
                         "id": incident.id,  
                         "message": "Updated incident successfully."
                      }]
                    }, 200

        return {"status": 400, "data": [{
                    "message": "Incident record Not Found."
                }]}, 400


    def delete(self, incident_id):
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.delete_from_incidences()
            return {"status": 200, "data": [{ "id": incident.id,
                        "message": "Incident record has been deleted." 
                    }]}, 200

        return {"status": 400, "data": [{
                     "message": "Incident record Not Found."
                }]}, 400


class IncidentLocation(Resource):
    def patch(self, incident_id):
        data = parser.parse_args()
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.update_location(data["location"])
            incident.save_to_incidences()
            return {
                    "status": 200,
                    "data": [{ "message": "Incident updated Successfully.",
                    "id": incident.id,
                    "title" : incident.title,
                    "record_type" : incident.record_type,
                    "location" : incident.location,
                    "status" : incident.status,
                    "images" : incident.images,
                    "videos" : incident.videos,
                    "comment" : incident.comment
                    }]}, 200

        return {"status": 200, "data": [{
                    "message": "Incident record Not Found."
                }]}, 200


class IncidentComment(Resource):
    def patch(self, incident_id):
        data = parser.parse_args()
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.update_comment(data["comment"])
            incident.save_to_incidences()
            return {
                      "status": 200,
                        "data": [{ "message": "Incident updated Successfully.",
                        "id": incident.id,
                        "title" : incident.title,
                        "record_type" : incident.record_type,
                        "location" : incident.location,
                        "status" : incident.status,
                        "images" : incident.images,
                        "videos" : incident.videos,
                        "comment" : incident.comment
                      }]
                    }, 200

        return {"status": 400, "data": [{
                    "message": "Incident record Not Found."
                }]}, 400
