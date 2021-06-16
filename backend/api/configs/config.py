import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

load_dotenv()

# Get Database Details from .env file
dbName = os.getenv("DB_NAME")
dbUser = os.getenv("DB_USERNAME")
dbPassword = os.getenv("DB_PASSWORD")


class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET")
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret"
    SESSION_COOKIE_SECURE = True  # Only send cookies if the connection is secure
    SESSION_COOKIE_HTTPONLY = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql://{dbUser}:{dbPassword}@localhost/{dbName}"
    FLASK_RUN_PORT = 8000
    # blacklisting TOKENS   When Users LoggedOut
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class DevelopmentConfig(Config):

    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///news.db"
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///production.db"
    pass
