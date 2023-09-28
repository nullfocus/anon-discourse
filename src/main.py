import logging
import sys
import os
from flask import Flask
from flask_socketio import SocketIO

import routes
import sockets

def configure_logging():
    file_handler = logging.FileHandler(filename='./log.txt')
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    handlers = [file_handler, stdout_handler]

    logging.basicConfig(level=logging.DEBUG, handlers=handlers)
    return logging.getLogger(os.path.basename(__file__))

def main():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['HOST'] = '0.0.0.0'
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    socketio = SocketIO(app)

    log = configure_logging()

    try:
        routes.configure_routes(log, app)
        sockets.configure_sockets(log, socketio)
        log.debug('starting socketio')
        socketio.run(app, allow_unsafe_werkzeug=True)
    except Exception as exc:
        log.error(exc)
        raise exc

if __name__ == '__main__':
    main()