import flask
app = Flask(__name__)
flaskver = flask.__version__

@app.route('/')

def fver():
    return flaskver