from flask import Flask, request, jsonify, Response
import logging
from server import core
from logging.config import dictConfig
import json
from smnlu.spacynlu import SpacyNlu, IntentPatternsWithDiscardMapping
import intents

# Language model for spacy
LANGUAGE_MODEL = "ru_core_news_sm"

json.ensure_ascii = False


def create_app():
    app = Flask(__name__)

    dictConfig(core.logger_config)
    log = logging.getLogger("application")

    core.init(configuration=None, logger_to_use=log)

    core.logger.info("================ sm-nlu server launched ==================")
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
        context: set = set(request.json.get("context", []))

        core.log("", "SMNLU", "MESSAGE_RECEIVED", text)

        intent_from_text = nlu.intent(text, context)

        if intent_from_text is not None:
            return Response(response=json.dumps({
                "text": text,
                "intent": intent_from_text.id,
                "context": list(context)}),
                status=200,
                mimetype="application/json")

        return Response(response=json.dumps({
            "text": text,
            "intent": None,
            "context": list(context)}),
            status=200,
            mimetype="application/json")

    return app


if __name__ == "__main__":
    # execute only if run as a script
    create_app()
