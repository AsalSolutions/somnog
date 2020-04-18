from routes import speakerApi, runApp
from db import app


@app.route("/")
def index():
    text = "SomNOG App Started ..."
    return {"name": "Somnog App", "description": text}


# Speaker Api
speakerApi()

# Main
if __name__ == '__main__':
    runApp()
