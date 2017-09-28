from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Email %r>' % self.email


@app.route("/",  methods=['POST'])
def index():
    user = User(request.form["email"])
    db.session.add(user)
    db.session.commit()
    return User.query.all()
