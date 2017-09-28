from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
CORS(app)


@app.route("/",  methods=['POST'])
def index():
    return "Email: " + request.form["email"]
