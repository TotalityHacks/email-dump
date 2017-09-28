import os
import re
from flask import Flask, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
CORS(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Email %r>' % self.email

db.create_all()
db.session.commit()


@app.route("/",  methods=['POST'])
def index():
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    email = request.form.get("email")
    if pattern.match(email) is None:
        return "Invalid email", 400
    user = User(email)
    db.session.add(user)
    db.session.commit()
    return redirect("https://totalityhacks.com/")
