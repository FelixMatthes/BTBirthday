from flask import Blueprint
from BTWeb.models import User
from BTWeb import db


crud = Blueprint('crud', __name__)


@crud.route('/create')
def create():
    user = User(username="Katja", email="k@g.de", password="hashed_password")
    db.session.add(user)
    db.session.commit()
    return 'create is done'
