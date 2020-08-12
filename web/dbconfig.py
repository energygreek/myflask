import os
from flask import  g, current_app
# ...

current_app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////' + os.path.join(g.app.root_path, 'data.db')