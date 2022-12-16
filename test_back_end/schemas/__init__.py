from marshmallow import Schema, fields


class PaginationSchema(Schema):
    page = fields.Integer()
    per_page = fields.Integer()
    total_items = fields.Integer()
    pages = fields.Integer()
    items = fields.List(fields.Dict)
