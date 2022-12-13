from flask import Flask, request
from flask_restful import Api, Resource
from sqlalchemy import desc

from test_back_end import db
from test_back_end.models.cliente import Cliente as ClienteModel
from test_back_end.schemas.cliente import ClienteSchema

app = Flask(__name__)
api = Api(app)

STATUS_SUCCESS_200 = 200
STATUS_CREATED_SUCESS_201 = 201
STATUS_SUCCESS_NO_CONTENT_204 = 204


class ClienteResource(Resource):
    def __init__(self):
        self.model = ClienteModel

    def _paginate(self, query):
        pagination_params = {
            "page": request.args.get("page", 1, type=int),
            "max_per_page": request.args.get("limit", None, type=int),
            "per_page": request.args.get("per_page", None, type=int),
        }
        # Remove keys with None values
        pagination_params = {
            k: v for k, v in pagination_params.items() if v is not None
        }

        paginated_result = query.paginate(**pagination_params)

        return paginated_result

    def _filter_by(self, query):
        columns_filter = {}
        columns_keys = query.statement.columns.keys()
        for column in columns_keys:
            columns_filter[column] = request.args.get(column, None, type=str)

        query = query.filter_by(**columns_filter)

        return query

    def _order_by(self, query):
        order_by = request.args.get("order_by", None, type=str)

        if not order_by:
            return query

        if order_by[0] == "-":
            order_by = order_by[1:]
            query = query.order_by(desc(order_by))
            return query
        else:
            query = query.order_by(order_by)
            return query

    def _get_query(
        self,
    ):
        query = self.model.query
        query = self._filter_by(query)
        query = self._order_by(query)
        query = self._paginate(query)
        return query

    def get(self, cliente_id: int = None):
        """
        Retorna o cliente
        """

        if cliente_id is not None:
            cliente = ClienteModel.query.get_or_404(cliente_id).first()
            schema = ClienteSchema()
            json_cliente = schema.dumps(cliente)

        if cliente_id is None:
            paginated_result = self._get_query()
            schema = ClienteSchema(many=True)
            json_cliente = schema.dumps(paginated_result.items)

        return json_cliente, STATUS_SUCCESS_200

    def put(self):
        """
        Adiciona um cliente
        """
        data = request.get_json()

        schema = ClienteSchema()
        validated_data = schema.load(data)

        cliente = ClienteModel(**validated_data)

        db.session.add(cliente)
        db.session.commit()

        return_data = schema.dumps(cliente)
        return return_data, STATUS_CREATED_SUCESS_201

    def delete(self, cliente_id):
        """
        Remove um cliente
        """
        cliente = ClienteModel.query.get_or_404(cliente_id)

        db.session.delete(cliente)
        db.session.commit()

        return {}, STATUS_SUCCESS_NO_CONTENT_204

    def patch(self, cliente_id):
        """
        Atualiza os dados de um cliente
        """
        cliente = ClienteModel.query.get_or_404(cliente_id)

        data = request.get_json()

        schema = ClienteSchema()
        validated_client_data = schema.load(data)

        # Atualiza os dados do Model com os dados recebidos
        for key, value in validated_client_data.items():
            setattr(cliente, key, value)

        db.session.commit()
        db.session.refresh(cliente)

        return_data = schema.dumps(cliente)
        return return_data, STATUS_SUCCESS_200
