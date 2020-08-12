import os

#wskazanie miejsca gdzie znajduja sie wszystkie moduly/aplikacje wykorzystywane dla strony
basedir = os.path.abspath(os.path.dirname(__file__))

#ustawienia dla konfiguracji zgodne dla wszystkich ponizej np DevelopmentConfig
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

#Ustawienia konfiguracji, zmieniamy w zaleznosci od potrzeby pamietac zeby po zmianie configu na nowo ustawić FLASK_APP
class DevelopmentConfig(Config):
    DEBUG = True
    
class Nigger(Config):
    DEBUG = False
    print('nigger')

#ustawienia domyślne
config = {
    'default': DevelopmentConfig,
    'test': Nigger
}
