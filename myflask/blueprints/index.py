from flask import Blueprint, render_template
from flask_login import current_user, login_required

index = Blueprint("/", __name__, template_folder="templates")


@index.route('/')
@login_required
def main():
    return render_template('index.html')