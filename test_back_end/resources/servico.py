from datetime import datetime

from flask import Flask, request
from flask_restful import Api, Resource

from test_back_end import db
from test_back_end.models.servico import Servico as ServicoModel
from test_back_end.resources import BaseCRUD, paginate_query
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
        data_pesquisa = request.args.get("data")
        data_pesquisa = datetime.strptime(data_pesquisa, "%d/%m/%Y")

        # Get all servicos that matches the date without time
        servicos_query = ServicoModel.query.filter(
            ServicoModel.data_agendamento.between(
                data_pesquisa,
                data_pesquisa.replace(hour=23, minute=59, second=59),
            )
        )

        paginated_result = paginate_query(servicos_query, ServicoSchema)

        return paginated_result, STATUS_SUCCESS_200
