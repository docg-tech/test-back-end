from marshmallow import Schema, fields


class ClienteSchema(Schema):
    id = fields.Integer()
    nome = fields.String()
    email = fields.Email()
    telefone = fields.String()
