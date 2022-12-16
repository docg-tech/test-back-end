from datetime import datetime as dt

from marshmallow import Schema, fields, pre_load


def check_date_without_time(date: str):
    try:
        dt.strptime(date, "%d/%m/%Y-%H:%M:%S")
        return False
    except ValueError:
        return True


class ServicoSchema(Schema):
    id = fields.Integer()
    titulo = fields.String()
    preco = fields.Decimal(places=2, as_string=True)
    data_agendamento = fields.DateTime(format="%d/%m/%Y-%H:%M:%S")
    pet_id = fields.Integer()

    @pre_load
    def format_data_agendamento(self, in_data, **kwargs):
        data_agendamento = in_data.get("data_agendamento", None)

        if data_agendamento and check_date_without_time(data_agendamento):
            data_agendamento = dt.strptime(data_agendamento, "%d/%m/%Y")
            data_agendamento = dt.strftime(
                data_agendamento, "%d/%m/%Y-%H:%M:%S"
            )
            in_data["data_agendamento"] = data_agendamento

        return in_data
