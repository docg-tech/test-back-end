class TestCliente:
    def test_get(client, db):
        """
        DADO -
        QUANDO -
        ENTAO -
        """
        from test_back_end.models.cliente import Cliente as ClienteModel

        client_data = {
            "nome": "teste",
            "email": "teste@teste.com",
            "telefone": "11123456789",
        }
        test_client = ClienteModel(**client_data)
        db.session.add(test_client)
        db.session.commit()

        response = client.get("/cliente")
        # TODO: verificar response.get_json()
        assert response.status_code == 200

    def test_put(client, db):
        """ """
        client_data = {
            "nome": "teste",
            "email": "teste@teste.com",
            "telefone": "11123456789",
        }

        response = client.put("/cliente", json=client_data)

        assert response.status_code == 201

    def test_delete(client, db):
        """ """
        from test_back_end.models.cliente import Cliente as ClienteModel

        client_data = {
            "nome": "teste",
            "email": "teste@teste.com",
            "telefone": "11123456789",
        }
        db.session.add(ClienteModel(**client_data))
        db.session.commit()

        response = client.delete("/cliente/1")

        assert response.status_code == 204
        assert ClienteModel.query.filter_by(id=1).count() == 0

    def test_patch(client, db):
        """ """
        from test_back_end.models.cliente import Cliente as ClienteModel

        client_data = {
            "id": 1,
            "nome": "teste",
            "email": "teste@teste.com",
            "telefone": "11123456789",
        }
        patch_client_data = {
            "nome": "teste2",
        }
        db.session.add(ClienteModel(**client_data))
        db.session.commit()

        response = client.patch(
            f"/cliente/{client_data['id']}", json=patch_client_data
        )

        assert response.status_code == 200

        updated_client = ClienteModel.query.filter_by(
            id=client_data["id"]
        ).first()
        assert updated_client.nome == patch_client_data["nome"]
