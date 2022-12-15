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

        assert isinstance(paginated_result, dict)
        assert paginated_result["page"] == 1
        assert paginated_result["per_page"] == 1
        assert paginated_result["total_items"] == 2
        assert paginated_result["pages"] == 2
        assert len(paginated_result["items"]) == 1

    def test_order_by(self, client, db):
        """
        Test the ordering of the query results
        Test requisition parameters for ordering
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

        order_by_params = {"order_by": "nome"}

        with current_app.test_request_context(query_string=order_by_params):
            ordered_result = base_crud._order_by(query)

        assert ordered_result[0].nome == "Aaron"

    def test_filter_by(self, client, db):
        """
        Test the filtering of the query results
        Test requisition parameters for filtering
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

        filter_by_params = {"nome": "Aaron"}

        with current_app.test_request_context(query_string=filter_by_params):
            filtered_result = base_crud._filter_by(query)

        assert filtered_result[0].nome == "Aaron"
