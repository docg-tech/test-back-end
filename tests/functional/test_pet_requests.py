from test_back_end.models.pet import Pet as PetModel


def test_get(client, db):
    from test_back_end.models.cliente import Cliente as ClienteModel

    client_data = {
        "nome": "teste",
        "email": "teste@teste.com",
        "telefone": "11123456789",
    }
    test_client = ClienteModel(**client_data)
    db.session.add(test_client)
    db.session.commit()

    pet_data = {
        "nome": "teste",
        "especie": "gato",
        "raca": "laranja",
        "cliente_id": 1,
    }
    test_pet = PetModel(**pet_data)
    db.session.add(test_pet)
    db.session.commit()

    response = client.get("/pet")

    assert response.status_code == 200
