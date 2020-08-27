from flask import Blueprint, redirect, request, url_for, render_template
from flask_login import login_user, login_required, logout_user

from myflask.util.loginform import LoginForm
from myflask.util.usermanager import get_user, create_user

action = Blueprint("action", __name__)


@action.route('/login/', methods=('GET','POST'))
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user = get_user(user_name) # get user data from db

        if user is None:
            emsg = 'error password or username'
        else:
            if user.verify_password(password):
                login_user(user, remember=True) # create session
                return redirect(request.args.get('next') or url_for('home.home'))
            else:
                emsg = 'username or password wrong'

    return render_template('login.html', form=form, emsg=emsg)


@action.route('/register/', methods=('GET','POST'))
def register():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name) # get user data from db

        if user_info is not None:
            emsg = 'username exist'
        else:
            create_user(user_name=user_name, password=password)
            return redirect(url_for('home.home'))
    return render_template('register.html', form=form, emsg=emsg)


@action.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('action.login'))