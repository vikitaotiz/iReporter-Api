import datetime
from flask_restful import Resource, reqparse
from app.api.v1.models.user_model import User
from flask_jwt_extended import create_access_token

parser = reqparse.RequestParser(bundle_errors=True)

class Login(Resource):
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank!')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank!')

    def post(self):
        data = parser.parse_args()
        usr = User.find_by_name(data["username"])

        if usr and usr.authenticated(password=data["password"]):
            expire_time = datetime.timedelta(minutes=60)
            token = create_access_token(usr.username, expires_delta=expire_time)
            return {"status": 200,
                    'token': token,
                    "data": [{
                        'message': f'Hello {usr.username}, you are logged in.'
                    }]}, 200

        return {"status": 400,
                "data": [{
                    "message": "This user doesn't exists"
                }]}, 400


class Register(Resource):
    parser.add_argument('firstname', type=str, default="", help='This field can be left blank!')
    parser.add_argument('lastname', type=str, default="", help='This field can be left blank!')
    parser.add_argument('othername', type=str, default="", help='This field can be left blank!')
    parser.add_argument('email', type=str, default="", help='This field can be left blank!')
    parser.add_argument('phonenumber', type=str, default="", help='This field can be left blank!')

    def post(self):
        data = parser.parse_args()
        usr = User.find_by_name(data["username"])

        if usr:
            return {"status": 400,
                    "data": [{
                        "message": "A user with that username already exists"
                    }]}, 400

        user = User(**data)
        user.save_to_db()

        return {"status": 201,
                "data": [{
                    "message": "User created Successfully."
                }]}, 201
