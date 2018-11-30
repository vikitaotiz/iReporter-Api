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

	