

from flask import redirect, render_template, url_for, session, current_app
from .. import db
from ..models import User, Role
from ..email import  send_simple_message
from .forms import NameForm
from . import main

@main.route('/')
def index():
    users = User.query.all()
    user_role =  Role.query.filter_by(name='User').first()
    return render_template('index.html', users=users)