from flask_socketio import emit, join_room
from flask import request
import threading
import time

# todo: shift locking and messages to separate modules

# https://stackoverflow.com/questions/70786158/flask-api-how-to-avoid-user-concurrency-in-a-function
CORE_LOCK = threading.Lock()
LOCKS = {}


def get_lock(name):
    with CORE_LOCK:
        lock = LOCKS.get(name, None)
        if not lock:
            lock = threading.Lock()
            LOCKS[name] = lock
        return lock


channel_history = {}

# dict storing lists of messages, by channel
#   message
#   original sid
#   timestamp


def add_message_to_history(channel, sid, message, timestamp):
    with get_lock("message_history"):
        history = channel_history.get(channel, None)

        if not history:
            history = []
            channel_history[channel] = history

        # todo: covert to object
        history.append({"message": message, "sid": sid, "timestamp": timestamp})

        channel_history[channel] = history


def get_message_history(channel):
    with get_lock("message_history"):
        history = channel_history.get(channel, None)

        if not history:
            history = []
            channel_history[channel] = history

        return history


def configure_sockets(log, socketio):
    @socketio.on_error_default
    def error_handler(e):
        log.error(e)

    @socketio.event
    def connect():
        channel = request.args.get("c")
        sid = request.sid

        log.debug(f"new client connected, sid [{sid}] channel [{channel}]")

        join_room(channel)

        history = get_message_history(channel)

        # todo: func to strip out identifiers from history
        emit("get_history", history, to=sid)

    @socketio.event
    def send_message(json):
        channel = json["channel"]
        sid = request.sid
        message = json["message"]
        timestamp = time.time()

        log.debug(f"new message, sid [{sid}] channel [{channel}] message [{message}]")

        add_message_to_history(channel, sid, message, timestamp)

        # todo: func to strip out identifiers from history
        # todo: use a class to get the same fields, this is dumb
        data = {"message": message, "timestamp": timestamp}

        emit("new_message", data, to=channel)
