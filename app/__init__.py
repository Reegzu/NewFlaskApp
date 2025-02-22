from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
moment = Moment()

#funkcja tworząca / wytwórcza
def create_app(config_name):
    app = Flask(__name__)
    
    #uzycie ustawien danej konfiguracji
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #inicjacja uzytych rzeczy
    bootstrap.init_app(app)
    moment.init_app(app)

    #import schematow blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

