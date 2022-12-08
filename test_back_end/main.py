from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://paim:159632@localhost:3306/test_back_end"
db.init_app(app)


@app.route("/")
def index():
    return "<p>Hello World!</p>"
