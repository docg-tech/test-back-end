from typing import Union

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from test_back_end.models import db


def create_app(config: Union[str, object] = None) -> Flask:
    app = Flask(__name__)
    api = Api(app)

    if config is not None and isinstance(config, str):
        app.config.from_pyfile(config)
    if config is not None and isinstance(config, object):
        app.config.from_object(config)
    if config is None:
        from test_back_end import config as cfg

        app.config.from_object(cfg)

    from test_back_end.resources.cliente import ClienteResource
    from test_back_end.resources.pet import PetResource
    from test_back_end.resources.servico import AgendaResource, ServicoResource

    api.add_resource(
        ClienteResource,
        "/cliente",
        "/cliente/<int:_id>",
        endpoint="cliente",
    )
    api.add_resource(
        PetResource,
        "/pet",
        "/pet/<int:_id>",
        endpoint="pet",
    )
    api.add_resource(
        ServicoResource,
        "/servico",
        "/servico/<int:_id>",
        endpoint="servico",
    )
    api.add_resource(
        AgendaResource,
        "/agenda",
        endpoint="agenda",
    )

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)  # noqa: E402
    return app
