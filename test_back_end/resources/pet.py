from flask import Flask, request
from flask_restful import Api, Resource

from test_back_end import db
from test_back_end.models.pet import Pet as PetModel
from test_back_end.resources import BaseCRUD
from test_back_end.schemas.pet import PetSchema

app = Flask(__name__)
api = Api(app)

STATUS_SUCCESS_200 = 200
STATUS_CREATED_SUCESS_201 = 201
STATUS_SUCCESS_NO_CONTENT_204 = 204


class PetResource(Resource, BaseCRUD):
    def __init__(self):
        super().__init__()
        self.model = PetModel
        self.schema = PetSchema
