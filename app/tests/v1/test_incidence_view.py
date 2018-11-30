import unittest
import json

from app.api.v1.views.incidence_view import Incidences, Incidence
from app import app

class TestIncidences(unittest.TestCase):
    def setUp(self):
        self.tests = app.test_client()
        self.tests.testing = True

        incidence_info = json.dumps({
        "name" : "Name One",
    	"createdBy" : "vikita Otiz",
    	"type" : "Red Flag",
    	"location" : "1.234, 3.4567",
    	"status" : "Resolved",
    	"images" : "1111",
    	"videos" : "2222",
    	"comments" : "Was good"
        })

        self.create_product = self.tests.post('/api/v1/incidences', data = incidence_info, content_type="application/json")

    def tearDown(self):
        self.tests = None

    def test_get_incidences(self):
        result = self.tests.get("/api/v1/incidences", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_post_incidences(self):
        incidence_data = json.dumps({
            "name" : "Name One",
        	"createdBy" : "vikita Otiz",
        	"type" : "Red Flag",
        	"location" : "1.234, 3.4567",
        	"status" : "Resolved",
        	"images" : "1111",
        	"videos" : "2222",
        	"comments" : "Was good"
        })

        res = self.tests.post('/api/v1/incidences', data = incidence_data, content_type="application/json")
        self.assertEqual(res.status_code, 201)

    def test_post_incidences(self):
        incidence_data = json.dumps({
            "name" : "",
        	"createdBy" : "vikita Otiz",
        	"type" : "Red Flag",
        	"location" : "1.234, 3.4567",
        	"status" : "",
        	"images" : "1111",
        	"videos" : "2222",
        	"comments" : "Was good"
        })

        res = self.tests.post('/api/v1/incidences', data = incidence_data, content_type="application/json")
        self.assertEqual(res.status_code, 404)

    def test_get_incidence(self):
        result = self.tests.get("/api/v1/incidence/1", content_type="application/json")
        self.assertNotEqual(result.status_code, 404)
        self.assertEqual(result.status_code, 200)

    def test_get_incidence(self):
        result = self.tests.get("/api/v1/incidence/5", content_type="application/json")
        self.assertNotEqual(result.status_code, 404)

    def test_delete_incidence(self):
        result = self.tests.delete("/api/v1/incidence/1", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_delete_incidence(self):
        result = self.tests.delete("/api/v1/incidence/10", content_type="application/json")
        self.assertEqual(result.status_code, 404)

    def test_put_incidence(self):
        result = self.tests.put("/api/v1/incidence/1", content_type="application/json")
        self.assertEqual(result.status_code, 400)

    def test_put_incidence(self):
        result = self.tests.put("/api/v1/incidence/10", content_type="application/json")
        self.assertEqual(result.status_code, 404)
