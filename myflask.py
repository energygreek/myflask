from flask import Flask,render_template, redirect, request, url_for
from flask_login import LoginManager,current_user, login_required,\
    logout_user, login_user

from web.user import User
from web.loginform import LoginForm
from web.usermanager import create_user, get_user

from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # view endpoint 


@login_manager.user_loader # define function for getting user
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@login_required
def index():
    return render_template('index.html',username=current_user.username)


@app.route('/login/', methods=('GET','POST'))
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# 登出视图不需要模板，直接跳转到登录页，实际项目中可以增加一个登出页，展示些有趣的东西
if __name__ == '__main__':
    app.run()
