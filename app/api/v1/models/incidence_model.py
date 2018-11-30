from flask import request
from flask_restplus import abort

incidences = []


class IncidenceModel(object):
    def __init__(self, name, createdBy, type, location, status, images, videos, comments):
        self.name = name
        self.createdBy = createdBy
        self.type = type
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comments = comments

    def validate(self):
        if self.name == '' or type(self.name) != str:
            abort(404, {"Message" : "Error: Name is not of type string"})

        elif self.createdBy == '' and type(self.createdBy) != 'str':
            abort(404, {"Message" : "Error: Created by is not a string"})

        elif self.type == '' and type(self.type) != 'str':
            abort(404, {"Message" : "Error: Type is not a string"})

        elif self.location == '' and type(self.location) != 'str':
            abort(404, {"Message" : "Error: Location is not a string"})

        elif self.status == '' and type(self.status) != 'str':
            abort(404, {"Message" : "Error: Status is not a string"})

        elif self.images == '' and type(self.images) != 'str':
            abort(404, {"Message" : "Error: Images is not a string"})

        elif self.videos == '' and type(self.videos) != 'str':
            abort(404, {"Message" : "Error: Videos is not a string"})

        elif self.comments == '' or type(self.comments) != str:
            abort(404, {"Message" : "Error: Comments is not of type string"})
