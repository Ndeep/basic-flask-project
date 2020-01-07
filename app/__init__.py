from flask import Flask, request
from flask.cli import load_dotenv


load_dotenv()
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.before_request
    def manipulate_req():
        print(request.args)
    
    @app.after_request
    def manipulate_res(response):
        print(response)
        return response

    from .blueprints import main, users

    app.register_blueprint(main.bp)
    app.register_blueprint(users.bp)

    return app
