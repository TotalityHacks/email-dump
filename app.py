import os
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
CORS(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Email %r>' % self.email

db.create_all()
db.session.commit()


@app.route("/",  methods=['POST'])
def index():
    user = User(request.form["email"])
    db.session.add(user)
    db.session.commit()
    return " ".join([str(u) for u in User.query.all()])
