from flask import Flask, request
from flask_restful import Api, Resource

from test_back_end import db
from test_back_end.models.servico import Servico as ServicoModel
from test_back_end.resources import BaseCRUD
from test_back_end.schemas.servico import ServicoSchema

app = Flask(__name__)
api = Api(app)

STATUS_SUCCESS_200 = 200
STATUS_CREATED_SUCESS_201 = 201
STATUS_SUCCESS_NO_CONTENT_204 = 204


class ServicoResource(Resource, BaseCRUD):
    def __init__(self):
        super().__init__()
        self.schema = ServicoSchema
        self.model = ServicoModel


class AgendaResource(Resource):
    def get(self):
        """ """
        args = request.args
        servicos = ServicoModel.query.filter_by(
            data_agendamento=args.get("data")
        ).all()
        schema = ServicoSchema(many=True)
        return_servicos = schema.dumps(servicos)

        return return_servicos, STATUS_SUCCESS_200
