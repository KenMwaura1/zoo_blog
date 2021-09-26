import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Parent class for the configuration of the app
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    """
    development child class
    """
    DEBUG = True


class ProdConfig(Config):
    """
    production sub class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """
    testing sub class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
