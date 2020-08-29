from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from myflask.util.user import User
from configs import configs

from myflask.blueprints.index import index
from myflask.blueprints.home.index import home
from myflask.blueprints.action.index import action
from myflask.blueprints.blog.index import blog

app = Flask(__name__)

app.config.from_object(configs["dev"])
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'action.login' # view endpoint

# 注册蓝图
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(action, url_prefix="/action")
app.register_blueprint(blog, url_prefix="/blog")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@login_manager.user_loader # define function for getting user
def load_user(user_id):
    return User.get(user_id)


# run in  cmd, for socket AF_net
def main():
    app.run()


if __name__ == '__main__':
    # for apache
    # WSGIServer(app).run()
    # for nginx, need to set conmunication sock between nginx and the cgiserver
    #WSGIServer(app, bindAddress='./myflask.socket').run()
    main()