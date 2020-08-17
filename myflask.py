#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from src.myapp import app
import logging
from logging.handlers import RotatingFileHandler

ERROR_LOG_FILE='./error.log'
# create a log file
log = open(ERROR_LOG_FILE, 'w+')
log.seek(0)
log.truncate()
log.write("Web app log\n")
log.close()

log_handler=RotatingFileHandler(ERROR_LOG_FILE, maxBytes=1000000, backupCount=1)
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
    )
log_handler.setFormatter(formatter)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)

if __name__ == '__main__':
    # for apache
    # WSGIServer(app).run()
    # for nginx, need to set conmunication sock between nginx and the cgiserver
    WSGIServer(app, bindAddress='./myflask.sock',log=app.logger).run()
