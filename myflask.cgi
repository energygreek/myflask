#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from main import app

if __name__ == '__main__':
    # for apache
    # WSGIServer(app).run()
    # for nginx, need to set conmunication sock between nginx and the cgiserver
    WSGIServer(app, bindAddress='/var/sockets/myflask-fcgi.sock').run()