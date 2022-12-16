from flask import Flask, request
from flask_restful import Api, Resource
from sqlalchemy import desc

from test_back_end import db
from test_back_end.models.cliente import Cliente as ClienteModel
from test_back_end.resources import BaseCRUD
from test_back_end.schemas.cliente import ClienteSchema

app = Flask(__name__)
api = Api(app)

STATUS_SUCCESS_200 = 200
STATUS_CREATED_SUCESS_201 = 201
STATUS_SUCCESS_NO_CONTENT_204 = 204


class ClienteResource(Resource, BaseCRUD):
    def __init__(self):
        super().__init__()
        self.model = ClienteModel
        self.schema = ClienteSchema
