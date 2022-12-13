import pytest


def test_get_order_by(client, db):
    """ """
    from test_back_end.models.cliente import Cliente as ClienteModel

    cliente1 = ClienteModel(
        nome="abc", email="foo@bar.com", telefone="11987654321"
    )
    cliente2 = ClienteModel(
        nome="cde", email="goo@bar.com", telefone="22987654321"
    )
    db.session.add_all([cliente1, cliente2])
    db.session.commit()

    response = client.get("/cliente", query_string={"nome": "abc"})

    assert response.status_code == 200
