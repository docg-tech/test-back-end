from typing import Union

from flask import Flask


def create_app(config: Union[str, object] = None) -> Flask:
    app = Flask(__name__)

    if config is not None and isinstance(config, str):
        app.config.from_pyfile(config)

    if config is not None and isinstance(config, object):
        app.config.from_object(config)

    from test_back_end.models import db

    db.init_app(app)

    return app
