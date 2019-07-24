from flask import Flask
app = Flask(__name__)

def create_app():

    from FlaskServer.app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app