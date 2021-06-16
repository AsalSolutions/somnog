from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from api.configs import config


# Init App
app = Flask(__name__)

# Decide which config to load
if app.config["ENV"] == 'production':
    app.config.from_object(config.ProductionConfig)
elif app.config["ENV"] == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

# Init Bcrypt
bcrypt = Bcrypt(app)


# More setup for JWT Security
# app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/v1.0/'
# app.config['JWT_REFRESH_COOKIE_PATH'] = '/auth/logout/access'
# app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# Securing Session cookies


# Init Json Web Token
jwt = JWTManager(app)

# DB Configuration
# SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"

db = SQLAlchemy(app)
mm = Marshmallow(app)

# Configure Flask Migrate
migrate = Migrate(app, db)


# We want to create all tables
@app.before_first_request
def create_tables():
    db.create_all()
