from flask_cors import CORS, cross_origin
from routes import speakerApi, runApp
from db import app

# This should be removed on production
CORS(app)


@app.route("/")
def index():
    text = "SomNOG App Started ..."
    return {"name": "Somnog App", "description": text}


# Speaker Api
speakerApi()

# Main
if __name__ == '__main__':
    runApp()
