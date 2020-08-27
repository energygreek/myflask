from flask import Blueprint, render_template
from flask_login import current_user, login_required

home = Blueprint("home", __name__, template_folder="templates")


@home.route('/')
@login_required
def index():
    print('home')
    return render_template('home.html',username=current_user.username)