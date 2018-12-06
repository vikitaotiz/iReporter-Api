from flask_restful import Resource, reqparse
from app.api.v1.models.incidences_model import Incidences, incidences
from flask_jwt_extended import jwt_required

#Validate json data
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title', type=str, required=True, help="This field cannot be left blank." )
parser.add_argument('record_type', type=str, required=True, choices=("incidence", "intervention"), 
                     help="This field cannot be left blank. Use either 'incidence' OR 'intervention' : {error_msg}" )
parser.add_argument('location', type=str, help="This field can be left blank!" )
parser.add_argument('status', type=str, help="This field can be left blank!" )
parser.add_argument('images', action='append', help="This field can be left blank!" )
parser.add_argument('videos', action='append', help="This field can be left blank")
parser.add_argument('comment', type=str, required=True, help="This field cannot be left blank!" )

class IncidentRecords(Resource):
    @jwt_required
    def get(self):
        if len(incidences) <= 0:
            return {"status" : 200, "Message" : "There are no incidence records."}, 200
        return { "status": 200, "data": [item.json_data() for item in Incidences.get_all()]}, 200
    
    @jwt_required
    def post(self):
        data = parser.parse_args()

        new_record = Incidences(**data)
        new_record.save_to_incidences()

        return {"status": 201,
                "data": [{ "id": new_record.id,
                    "message": f"{new_record.record_type} incident created Successfully."
                }]}, 201


class IncidentRecord(Resource):
    @jwt_required
    def get(self, incident_id):
        incident = Incidences.find_by_id(incident_id)
        if incident:
            return {"status": 200,
                    "data": [incident.json_data()]
                    }, 200

        return {"status": 404, "data": [{
                     "message": "Incident record does not exist."
                }]}, 404

    @jwt_required
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
                      "status": 202,
                      "data": [{
                         "id": incident.id,  
                         "message": "Updated incident successfully."
                      }]
                    }, 202

        return {"status": 404, "data": [{
                    "message": "Incident record Not Found."
                }]}, 404


    def delete(self, incident_id):
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.delete_from_incidences()
            return {"status": 200, "data": [{ "id": incident.id,
                        "message": "Incident record has been deleted." 
                    }]}, 200

        return {"status": 404, "data": [{
                     "message": "Incident record Not Found."
                }]}, 404


class IncidentLocation(Resource):
    def patch(self, incident_id):
        data = parser.parse_args()
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.update_location(data["location"])
            incident.save_to_incidences()
            return {
                      "status": 202,
                      "data": [{ "id": incident.id,
                         "message": "Updated incident record’s location"
                    }]}, 202

        return {"status": 404, "data": [{
                    "message": "Incident record Not Found."
                }]}, 404


class IncidentComment(Resource):
    def patch(self, incident_id):
        data = parser.parse_args()
        incident = Incidences.find_by_id(incident_id)
        if incident:
            incident.update_comment(data["comment"])
            incident.save_to_incidences()
            return {
                      "status": 202,
                      "data": [{ "id": incident.id,
                         "message": "Updated incidence record’s comment."
                      }]
                    }, 202

        return {"status": 404, "data": [{
                    "message": "Incident record Not Found."
                }]}, 404
