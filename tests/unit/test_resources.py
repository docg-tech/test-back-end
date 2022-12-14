import flask
import pytest
from flask import current_app

from test_back_end.resources import BaseCRUD


class TestBaseCRUD:
    def test_paginate(self, client, db):
        """
        Test the pagination of the query results
        Test requisition parameters for pagination
        """
        from test_back_end.models.cliente import Cliente as ClienteModel
        from test_back_end.schemas.cliente import ClienteSchema

        base_crud = BaseCRUD(model=ClienteModel, schema=ClienteSchema)

        cliente1 = ClienteModel(
            **{
                "nome": "Aaron",
                "email": "aaron@email.com",
                "telefone": "41987654321",
            }
        )
        cliente2 = ClienteModel(
            **{
                "nome": "Zaquias",
                "email": "zaquias@email.com",
                "telefone": "11987654321",
            }
        )

        db.session.add_all([cliente1, cliente2])
        db.session.commit()

        query = ClienteModel.query

        pagination_params = {
            "page": 1,
            "per_page": 1,
        }

        with current_app.test_request_context(query_string=pagination_params):
            paginated_result = base_crud._paginate(query)

        assert len(paginated_result.items) == 1
