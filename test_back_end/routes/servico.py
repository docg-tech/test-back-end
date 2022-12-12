from flask import Flask, request
from flask_restful import Api, Resource

from test_back_end import db
from test_back_end.models.servico import Servico as ServicoModel
from test_back_end.schemas.servico import ServicoSchema

app = Flask(__name__)
api = Api(app)

STATUS_SUCCESS_200 = 200
STATUS_CREATED_SUCESS_201 = 201
STATUS_SUCCESS_NO_CONTENT_204 = 204


class ServicoResource(Resource):
    def get(self, servico_id: int = None):
        if servico_id is not None:
            servico = ServicoModel.query.get_or_404(servico_id).first()
            schema = ServicoSchema()
            json_cliente = schema.dumps(servico)

        else:
            servico = ServicoModel.query.all()
            schema = ServicoSchema(many=True)
            json_cliente = schema.dumps(servico)

        return json_cliente, STATUS_SUCCESS_200

    def put(self):
        """
        Adiciona um servico
        """
        data = request.get_json()

        schema = ServicoSchema()
        validated_data = schema.load(data)

        servico = ServicoModel(**validated_data)

        db.session.add(servico)
        db.session.commit()

        return_data = schema.dumps(servico)
        return return_data, STATUS_CREATED_SUCESS_201

    def delete(self, servico_id: int):
        """
        Remove um servico
        """
        servico = ServicoModel.query.get_or_404(servico_id)

        db.session.delete(servico)
        db.session.commit()

        return {}, STATUS_SUCCESS_NO_CONTENT_204

    def patch(self, servico_id: int):
        """
        Atualiza os dados de um servico
        """
        servico = ServicoModel.query.get_or_404(servico_id)

        data = request.get_json()

        schema = ServicoSchema()
        validated_data = schema.load(data)

        # Atualiza os dados do Model com os dados recebidos
        for key, value in validated_data.items():
            setattr(servico, key, value)

        db.session.commit()
        db.session.refresh(servico)

        return_data = schema.dumps(servico)
        return return_data, STATUS_SUCCESS_200


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
