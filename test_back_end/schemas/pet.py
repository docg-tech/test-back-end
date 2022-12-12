from marshmallow import Schema, fields


class PetSchema(Schema):
    id = fields.Integer()
    nome = fields.String()
    especie = fields.String()
    raca = fields.String()
    cliente_id = fields.Integer()
