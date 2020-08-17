from flask import Blueprint

action = Blueprint("action", __name__, url_prefix="/action")


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
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = 'username or password wrong'

    return render_template('login.html', form=form, emsg=emsg)


@app.route('/register/', methods=('GET','POST'))
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
            return redirect(url_for('index'))
    return render_template('register.html', form=form, emsg=emsg)