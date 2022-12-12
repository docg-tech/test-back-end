from flask import Flask, request
from flask_restful import Api, Resource

from test_back_end import db
from test_back_end.models.pet import Pet as PetModel
from test_back_end.schemas.pet import PetSchema

app = Flask(__name__)
api = Api(app)

STATUS_SUCCESS_200 = 200
STATUS_CREATED_SUCESS_201 = 201
STATUS_SUCCESS_NO_CONTENT_204 = 204


class PetResource(Resource):
    def get(self, pet_id: int = None):
        """ """
        if pet_id is not None:
            pet = PetModel.query.filter_by(id=pet_id).first()
            schema = PetSchema()
            json_pet = schema.dumps(pet)

        if pet_id is None:
            pet = PetModel.query.all()
            schema = PetSchema(many=True)
            json_pet = schema.dumps(pet)

        return json_pet, STATUS_SUCCESS_200

    def put(self):
        """ """
        data = request.get_json()

        schema = PetSchema()
        validated_data = schema.load(data)

        pet = PetModel(**validated_data)

        db.session.add(pet)
        db.session.commit()

        return_data = schema.dumps(pet)

        return return_data, STATUS_CREATED_SUCESS_201

    def delete(self, pet_id: int):
        """ """
        pet = PetModel.query.get_or_404(pet_id)

        db.session.delete(pet)
        db.session.commit()

        return {}, STATUS_SUCCESS_NO_CONTENT_204

    def patch(self, pet_id: int):
        """ """
        pet = PetModel.query.get_or_404(pet_id)

        data = request.get_json()

        schema = PetSchema()
        validated_data = schema.load(data)

        for key, value in validated_data.items():
            setattr(pet, key, value)

        db.session.commit()
        db.session.refresh(pet)

        return_data = schema.dumps(pet)
        return return_data, STATUS_SUCCESS_200
