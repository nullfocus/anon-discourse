from flask_socketio import emit

def configure_sockets(log, socketio):

    @socketio.on_error() 
    def error_handler(e):
        log.error(e)

    @socketio.on('raise_question')
    def handle_question(json):
        log.debug('received question: ' + str(json))

        emit('ask_question', json, broadcast=True)

    @socketio.on('answer')
    def handle_answer(json):
        log.debug('received answer: ' + str(json))