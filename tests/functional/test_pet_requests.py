from test_back_end.models.pet import Pet as PetModel


class TestPet:
    def test_get(self, client, db):
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
        assert isinstance(response.get_json(), dict)

    def test_put(self, client, db):
        """ """
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

        response = client.put("/pet", json=pet_data)

        assert response.status_code == 201
        assert isinstance(response.get_json(), dict)

    def test_delete(self, client, db):
        """ """
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

        response = client.delete("/pet/1")

        assert response.status_code == 204
        assert PetModel.query.filter_by(id=1).count() == 0

    def test_patch(self, client, db):
        """ """
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

        new_pet_data = {
            "nome": "teste2",
        }
        response = client.patch("/pet/1", json=new_pet_data)

        assert response.status_code == 200
        assert isinstance(response.get_json(), dict)
