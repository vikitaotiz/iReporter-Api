from flask import Flask, request, Blueprint, make_response, jsonify
from flask_restplus import Resource, Api
from app.api.v1.utils.time_serve import get_time
# from flask_jwt_extended import JWTManager, jwt_required, get_jwt_claims
from jsonschema import validate

from app.api.v1.models.incidence_model import incidences, IncidenceModel

app = Flask(__name__)
api = Api(app, version='v 1.0', title='API Endpoints.', description='Incidences API Endpoints.')

api = api.namespace('api', description='Incidences operations')

api_incidences = Blueprint('api_incidences', __name__)
api_incidence = Blueprint('api_incidence', __name__)

@api.route('/v1/incidences')
class Incidences(Resource):
	# @jwt_required
	def get(self):
		'''Gets all the Incidences'''
		if len(incidences) <= 0 :
			return {"status" : 404, "Message" : "There are no incidences"}, 404
		return {"status" : 200, "Incidences" : incidences}, 200

	def post(self):
		'''Creates a new Incidence'''
		data = request.get_json()
		id = len(incidences) + 1
		name = data['name']
		createdOn = get_time()
		createdBy = data['createdBy']
		type = data['type']
		location = data['location']
		status = data['status']
		images = data['images']
		videos = data['videos']
		comments = data['comments']


		new_item = {
			"id" : id,
			"name" : name,
			"createdOn" : createdOn,
			"createdBy" : createdBy,
			"type" : type,
			"location" : location,
			"status" : status,
			"images" : images,
			"videos" : videos,
			"comments" : comments
		}

		check_data = IncidenceModel(name, createdBy, type, location, status, images, videos, comments)
		if not check_data.validate():
			incidences.append(new_item)
			return {"status" : 201, "Message" : "Incidence created successfully.", "Item" : new_item}, 201

@api.route('/v1/incidence/<int:id>')
class Incidence(Resource):
	def get(self, id):
		'''Gets a specific Incidence using the id'''
		inc = [incident for incident in incidences if incident['id'] == id]
		if inc:
			return {"status" : 200, "Incidence" : inc}, 200
		return {"status" : 404, "Message" : "Incidence #{} not found.".format(id)}

	def put(self, id):
		'''Updates a single Incidence'''
		inc = [incident for incident in incidences if incident['id'] == id]

		if inc:
			data = request.get_json()
			inc[0]['name'] = data['name']
			inc[0]['createdBy'] = data['createdBy']
			inc[0]['type'] = data['type']
			inc[0]['location'] = data['location']
			inc[0]['status'] = data['status']
			inc[0]['images'] = data['images']
			inc[0]['videos'] = data['videos']
			inc[0]['comments'] = data['comments']

			return {"status" : 200, "Message" : "Incidence updated successfully", "Incidence" : inc[0]}, 200
		return {"status" : 404, "Message" : "Incidence not found"}, 404


	def delete(self, id):
		'''Deletes a single Incidence'''
		inc = [incident for incident in incidences if incident['id'] == id]
		if inc:
			incidences.remove(inc[0])
			return {"status" : 200, "Message" : "Incident deleted successfully."}, 200
		return {"statu" : 404, "Message" : "Incidence not found, deletion failed"}, 404

