import pytest

from test_back_end import create_app


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture
def app():
    app = create_app(TestConfig)

    app.app_context().push()
    yield app


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def db(app):
    from test_back_end import db

    db.create_all()

    yield db
    db.session.remove()
    db.drop_all()
