from flask import Flask
from myflask.blueprints import home
from myflask.blueprints import action

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(home)
app.register_blueprint(action)
