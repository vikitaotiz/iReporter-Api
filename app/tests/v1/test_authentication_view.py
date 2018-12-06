import json
from app.tests.v1.MainTest import MainTest
from app.api.v1.models.user_model import User


class UserTest(MainTest):
    def login(self):
        response = self.app.post("/api/v1/incidences/login",
                                 data=json.dumps({"username": "vikitaotiz", "password": "12345" }),
                                 headers={'content-type': 'application/json'})
        return response

    def register(self):
        user = {"firstname": "vikitaotiz",
                "lastname": "otiz",
                "email": "vikitaotiz@gmail.com",
                "username": "vikitaotiz",
                "password": "12345"
                }
        response = self.app.post("/api/v1/incidences/register",
                                 data=json.dumps(user),
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def test_user_register(self):
        self.register()
        self.assertIsNone(User.find_by_name("vikitaotiz"))

    # def test_user_register_User_exist(self):
    #     response = self.register()
    #     self.assertEqual(response.status_code, 400)
    #     self.assertDictEqual({"status": 400,
    #                           "data": [{
    #                                 "message": "This user already exists"
    #                             }]
    #                           },
    #                          json.loads(response.data))

    # def test_register_duplicate_user(self):
    #     self.register()
    #     user_b = self.register()

    #     self.assertEqual(user_b.status_code, 400)
    #     self.assertDictEqual({"status": 400,
    #                           "data": [
    #                               {
    #                                 "message": "This user already exists"
    #                               }
    #                           ]},
    #                          json.loads(user_b.data),
    #                          "The response data is not the same."
    #                          )

    # def test_user_login(self):
    #     response = self.login()

    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsNotNone(User.find_by_name("vikitaotiz"))

    # def test_user_login_user_not_exist(self):
    #     response = self.app.post("/api/v1/incidences/login",
    #                              data=json.dumps({"username": "vikitaotiz25",
    #                                               "password": "12345"
    #                                               }),
    #                              headers={'content-type': 'application/json'}
    #                              )

    #     self.assertEqual(response.status_code, 400)
    #     self.assertIsNone(User.find_by_name("vikitaotiz25"))
    #     self.assertDictEqual({"status": 404,
    #                           "data": [
    #                               {
    #                                   "message": "A user with that"
    #                                              " username doesn't exists"
    #                               }
    #                           ]},
    #                          json.loads(response.data),
    #                          "The response data is not the same."
    #                          )

    # def test_get_user_token(self):
    #     self.register()
    #     r = self.login()

    #     token = json.loads(r.data).get("token", None)

    #     self.assertEqual(r.status_code, 200)
    #     self.assertIsNotNone(token)
