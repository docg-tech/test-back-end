from marshmallow import Schema, fields


class ServicoSchema(Schema):
    id = fields.Integer()
    titulo = fields.String()
    preco = fields.Decimal(places=2, as_string=True)
    data_agendamento = fields.DateTime(format="%d/%m/%Y")
    pet_id = fields.Integer()
