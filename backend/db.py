import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


load_dotenv()

# Get Database Details from .env file
dbName = os.getenv("DB_NAME")
dbUser = os.getenv("DB_USERNAME")
dbPassword = os.getenv("DB_PASSWORD")

# App
app = Flask(__name__)
bcrypt = Bcrypt(app)
# DB Configuration
# SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{dbUser}:{dbPassword}@localhost/{dbName}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
mm = Marshmallow(app)

# Configure Flask Migrate
migrate = Migrate(app, db)
