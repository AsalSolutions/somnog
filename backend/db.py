import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


load_dotenv()

# Get Database Details from .env file
dbName = os.getenv("DB_NAME")
dbUser = os.getenv("DB_USERNAME")
dbPassword = os.getenv("DB_PASSWORD")

# Init App
app = Flask(__name__)
# Init Bcrypt
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET")
# Init Json Web Token
jwt = JWTManager(app)
# DB Configuration
# SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{dbUser}:{dbPassword}@localhost/{dbName}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
mm = Marshmallow(app)

# Configure Flask Migrate
migrate = Migrate(app, db)


# We want to create all tables
@app.before_first_request
def create_tables():
    db.create_all()
