from app.api.v1.utils.time_util import get_time

incidences = []

class Incidences:
    incidence_id = 1

    def __init__(self, title, record_type, comment, location=None, status=None, images=None, videos=None):
        self.id = Incidences.incidence_id
        self.title = title
        self.record_type = record_type  
        self.location = location  
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

        Incidences.incidence_id += 1

    def json_data(self):
        return {"id": self.id,
                "title" : self.title,
                "record_type": self.record_type,
                "location": self.location,
                "status": self.status,
                "comment": self.comment,
                "images": self.images,
                "videos": self.videos,
                "createdOn" : get_time()
                }

    @staticmethod
    def find_by_id(incidence_id):
        for incidence in incidences:
            if incidence.id == incidence_id:
                return incidence
        return None

    def save_to_incidences(self):
        incidences.append(self)

    @staticmethod
    def get_all():
        return incidences

    def update_all(self, title, record_type, location, status, comment, images, videos):
        self.delete_from_incidences()
        self.title = title
        self.record_type = record_type
        self.location = location
        self.status = status
        self.comment = comment
        self.images = images
        self.videos = videos

    def update_location(self, location):
        self.delete_from_incidences()
        self.location = location

    def update_comment(self, comment):
        self.delete_from_incidences()
        self.comment = comment

    def delete_from_incidences(self):
        incidences.remove(self.find_by_id(self.id))
