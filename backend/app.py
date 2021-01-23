from flask_cors import CORS, cross_origin
from routes import speakers_endpoint, workshops_endpoint, users_endpoint
from db import app

# !This should be removed on production
CORS(app)


@app.route("/")
def index():
    text = "SomNOG App Started ..."
    return {"name": "Somnog App", "description": text}


# API Endpoints
speakers_endpoint()
workshops_endpoint()
users_endpoint()


# Main
if __name__ == '__main__':
    app.run(debug=True)
