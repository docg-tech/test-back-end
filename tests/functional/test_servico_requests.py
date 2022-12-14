import datetime

import pytest

from test_back_end.factory import ClienteFactory
from test_back_end.models.servico import Servico as ServicoModel


@pytest.fixture
def add_cliente_to_db(db):
    """Add cliente to the database."""
    from test_back_end.models.cliente import Cliente as ClienteModel

    client_data = {
        "nome": "teste",
        "email": "teste@teste.com",
        "telefone": "11123456789",
    }
    test_client = ClienteModel(**client_data)
    db.session.add(test_client)
    db.session.commit()


@pytest.fixture
def add_pet_to_db(db, add_cliente_to_db):
    """Add pet to the database."""
    from test_back_end.models.pet import Pet as PetModel

    pet_data = {
        "nome": "teste",
        "especie": "gato",
        "raca": "laranja",
        "cliente_id": 1,
    }
    test_pet = PetModel(**pet_data)
    db.session.add(test_pet)
    db.session.commit()


@pytest.fixture
def add_servico_to_db(db, add_pet_to_db, dados_servico):
    dados_servico["data_agendamento"] = datetime.datetime.fromisoformat(
        "2022-12-12T12:34:56.123456"
    )
    servico = ServicoModel(**dados_servico)
    db.session.add(servico)
    db.session.commit()


@pytest.fixture
def dados_servico():
    dados = {
        "titulo": "Servico Teste",
        "preco": 52.50,
        "data_agendamento": "12/12/2022",
        "pet_id": 1,
    }
    yield dados


class TestServico:
    def test_get(self, client, db, add_servico_to_db):
        """ """
        response = client.get("/servico")

        assert response.status_code == 200

    def test_put(self, client, db, dados_servico, add_pet_to_db):
        """ """
        response = client.put("/servico", json=dados_servico)

        assert response.status_code == 201

    def test_delete(self, client, db, add_servico_to_db):
        """ """
        response = client.delete("/servico/1")

        assert response.status_code == 204
        assert ServicoModel.query.filter_by(id=1).count() == 0

    def test_patch(self, client, db, add_servico_to_db):
        """ """
        patch_servico_data = {
            "titulo": "teste2",
        }

        response = client.patch("/servico/1", json=patch_servico_data)

        assert response.status_code == 200

        updated_servico = ServicoModel.query.filter_by(id=1).first()
        assert updated_servico.titulo == patch_servico_data["titulo"]


class TestAgenda:
    def test_pesquisar_data(self, client, add_servico_to_db, dados_servico):
        """ """
        response = client.get("/agenda", query_string={"data": "12/12/2022"})

        assert response.status_code == 200
