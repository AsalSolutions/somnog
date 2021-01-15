from flask_cors import CORS, cross_origin
from routes import speakersAPI, runApp, workshopsAPI, users_endpoint
from db import app

# !This should be removed on production
CORS(app)


@app.route("/")
def index():
    text = "SomNOG App Started ..."
    return {"name": "Somnog App", "description": text}


# Endpoints
# Speaker Api
speakersAPI()
workshopsAPI()
users_endpoint()


# Main
if __name__ == '__main__':
    runApp()
