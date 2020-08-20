from flask import Blueprint, render_template
from flask_login import current_user, login_required

home = Blueprint("home", __name__, template_folder="templates")


@home.route('/')
@login_required
def index_handler():
    print('index')
    return render_template('index.html',username=current_user.username)