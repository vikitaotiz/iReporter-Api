from flask import Flask
from flask_restful import Api
from instance.config import config
from flask_jwt_extended import JWTManager

from app.api.v1.views.incidences_view import IncidentRecords, IncidentRecord, IncidentLocation, IncidentComment
from app.api.v1.views.authentication import Login, Register

jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    jwt.init_app(app)

    from app.api import api_bp as api_blueprint
    api = Api(api_blueprint)

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    api_endpoints(api)
    
    return app

def api_endpoints(api):
    api.add_resource(Login, "/incidences/login")
    api.add_resource(Register, "incidences/register")
    api.add_resource(IncidentRecords, "/incidences")
    api.add_resource(IncidentRecord, "/incidences/<int:incident_id>")
    api.add_resource(IncidentLocation, "/incidences/<int:incident_id>/location")
    api.add_resource(IncidentComment,  "/incidences/<int:incident_id>/comment")

    return None

