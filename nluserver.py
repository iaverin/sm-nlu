from flask import Flask, request, jsonify, Response
import logging
from server import core
from logging.config import dictConfig
import json
from smnlu.spacynlu import SpacyNlu, IntentPatternsWithDiscardMapping
import intents

LANGUAGE_MODEL = "ru_core_news_sm"

config = None


def create_app():
    global config

    app = Flask(__name__)

    print("===========")

    # todo: use Flask's native config loading

    json.ensure_ascii = False

    dictConfig(core.logger_config)
    log = logging.getLogger("application")

    core.init(config, log)

    core.logger.info("")
    core.logger.info("================ sm-nlu server launched ==================")
    core.logger.info("Привет")

    core.logger.info(f'Language model:{LANGUAGE_MODEL}')

    nlu = SpacyNlu(LANGUAGE_MODEL, intents.INTENTS, IntentPatternsWithDiscardMapping())

    core.logger.info("NLU initialized....")

    @app.route('/')
    def hello_world():
        core.log("test_user", "SMNLU", "event_test", {"payload": "test"})
        return 'SM-NLU service'

    @app.route('/intent', methods=['POST'])
    def intent():
        request.get_json(force=True)

        text: str = request.json.get("text", "")
        context = request.json.get("context", None)

        core.log("", "SMNLU", "MESSAGE_RECEIVED", text)

        intent = nlu.intent(text, context)

        if intent is not None:
            return Response(response=json.dumps({
                "text": text,
                "intent": intent.id,
                "context": context}),
                status=200,
                mimetype="application/json")

        return Response(response=json.dumps({
            "text": text,
            "intent": None,
            "context": context}),
            status=200,
            mimetype="application/json")

    return app


if __name__ == "__main__":
    # execute only if run as a script
    create_app()
