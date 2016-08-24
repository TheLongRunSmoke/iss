from app import app

@app.route("/getTle")
def index():
    return "Hello World!"
