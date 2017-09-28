from flask import request
from models import User, db

db.create_all()
db.session.commit()


@app.route("/",  methods=['POST'])
def index():
    user = User(request.form["email"])
    db.session.add(user)
    db.session.commit()
    return User.query.all()
