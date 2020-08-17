#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from src.myapp import app

if __name__ == '__main__':
    # for apache
    # WSGIServer(app).run()
    # for nginx, need to set conmunication sock between nginx and the cgiserver
    #WSGIServer(app, bindAddress='./myflask.socket').run()
    # for socket AF_net
    app.run()
