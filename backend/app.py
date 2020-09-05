from flask_cors import CORS, cross_origin
from routes import speakersAPI, runApp, workshopsAPI
from db import app

# This should be removed on production
CORS(app)


@app.route("/")
def index():
    text = "SomNOG App Started ..."
    return {"name": "Somnog App", "description": text}


# Get routes  Api 
# Speaker Api
speakersAPI()
workshopsAPI()


# Main
if __name__ == '__main__':
    runApp()
