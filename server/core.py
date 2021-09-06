import copy
import requests
import logging
from pprint import pformat
import threading
import json

logger_config = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s:%(threadName)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },

        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default',
            'level': 'INFO'},

        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'smnlu.log',
            'formatter': 'default',
            'level': 'INFO',
            'encoding': 'UTF-8',
            'maxBytes': 100000000,
            'backupCount': 5
        }

    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
    },
    'loggers': {
        'application': {
            'propagate': False,
            'handlers': ['console', 'file'],
        }
    }
}

logger = None
config = None


def init(configuration, logger_to_use=None):
    global config
    global logger

    config = configuration

    if logger_to_use:
        logger = logger_to_use
    else:
        logger = logging.getLogger()



def _format_log_string(user_id="", component="", event="", message=""):
    decoded_msg = ""

    try:
        decoded_msg = json.dumps(message, ensure_ascii=True)

    except:
        decoded_msg = message

    out = "userId: {user} component: {component} {event}: {msg}".format(user=user_id, component=component, event=event,
                                                                        msg=decoded_msg)
    return out


def log(user_id="", component="", event="", message: str = None):
    logger.info(_format_log_string(user_id, component, event, message))


def log_error(user_id="", component="", event="", message=None):
    logger.error(_format_log_string(user_id, component, event, message))
