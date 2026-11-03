from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.main import main
    from app.routes.system import system
    from app.routes.api import api

    app.register_blueprint(main)
    app.register_blueprint(system)
    app.register_blueprint(api)

    return app