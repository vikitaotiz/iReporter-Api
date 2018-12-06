from app.tests.v1.MainTest import MainTest
from app.api.v1.models.incidences_model import Incidences
from app.api.v1.utils.time_util import get_time


class RecordTest(MainTest):
    incident = {
                "title" : "Sample One",
                "record_type": "intervention",
                "location": "1.43434, 9.2343",
                "status": "under-investigation",
                "images": {"path": "/photo/img-1.jpg"},
                "videos": {"path": "/video/vid-1.mkv"},
                "comment": "Armed robbers were caught while trying to steal."
               }

    update_incident = {
                "id" : 9,
                "title" : "Sample One",
                "record_type": "intervention",
                "location": "1.0000, 9.0000",
                "status": "under-investigation",
                "images": {"path": "/photo/img-1.jpg"},
                "videos": {"path": "/video/vid-1.mkv"},
                "comment": "Armed robbers were caught while trying to steal.",
                "createdOn" : get_time()
               }

    def test_create_record(self):
        record = Incidences(**RecordTest.incident)

        self.assertEqual(record.record_type, "intervention", "Name of the Incident after creation doesn't equal constructor argument.")
        self.assertEqual(record.location, "1.43434, 9.2343", "Name of the Incident after creation doesn't equal constructor argument.")
        self.assertEqual(record.status, "under-investigation", "Name of the Incident after creation doesn't equal constructor argument.")
        self.assertEqual(record.images, {"path": "/photo/img-1.jpg"}, "Name of the Incident after creation doesn't equal constructor argument.")
        self.assertEqual(record.videos, {"path": "/video/vid-1.mkv"}, "Name of the Incident after creation doesn't equal constructor argument.")
        self.assertEqual(record.comment, "Armed robbers were caught while trying to steal.",
                        "Name of the Incident after creation doesn't equal constructor argument.")

    def test_incident_json(self):
        record = Incidences(**RecordTest.incident)
        expected = {
                "id" : 2,
                "title" : "Sample One",
                "record_type": "intervention",
                "location": "1.43434, 9.2343",
                "status": "under-investigation",
                "images": {"path": "/photo/img-1.jpg"},
                "videos": {"path": "/video/vid-1.mkv"},
                "comment": "Armed robbers were caught while trying to steal.",
                "createdOn" : get_time()
               }

        self.assertEqual(record.json_data(), expected, "The JSON export of the Incident is incorrect."
                         f"Received {record.json_data()}, expected {expected}.")

    def test_incident_update_comment_and_location(self):
        record = Incidences(**RecordTest.incident)
        record.save_to_incidences()

        record.update_comment(RecordTest.update_incident["comment"])
        record.save_to_incidences()

        self.assertEqual(record.comment, RecordTest.update_incident["comment"],
                         "Update comment failed.")

        record.update_location(RecordTest.update_incident["location"])
        record.save_to_incidences()

        self.assertEqual(record.location, RecordTest.update_incident["location"],
                         "Update location failed.")
