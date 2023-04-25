from flask import Flask, Blueprint
from flask_restful import Api

from helpers.cors import cors
from helpers.database import db, migrate

from resources.pessoa import PessoaResource, PessoasResource

# create the app
app = Flask(__name__)

# restful
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api')

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with the extension
db.init_app(app)
migrate.init_app(app, db)
cors.init_app(app)


api.add_resource(PessoaResource, '/pessoas')
api.add_resource(PessoasResource, '/pessoas/<pessoa_id>')

# Blueprints para Restful.
app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
