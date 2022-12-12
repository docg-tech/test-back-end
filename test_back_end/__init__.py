from typing import Union

from flask import Flask
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

    from test_back_end.routes.cliente import ClienteResource

    api.add_resource(
        ClienteResource,
        "/cliente",
        "/cliente/<int:cliente_id>",
        endpoint="cliente",
    )

    db.init_app(app)
    return app
