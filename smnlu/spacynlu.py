from dataclasses import dataclass

from typing import Counter, TypedDict
import spacy
from spacy.matcher import Matcher

# class Intent(dataclasses):
#     intent_id: TypedDict("Intent", {"id":str, "confidence":float })


class SpacyNlu:
    def __init__(self, model: str) -> None:
        self.nlp = spacy.load(model)
        self.matcher = Matcher(self.nlp.vocab)

    def set_patterns(self, intent: str, pattern_match: list, pattern_stop: list) -> dict:
        self.matcher.add(intent, pattern_match)
        self.matcher.add(intent+'_stop', pattern_stop)

    def get_intents_weightned(self, utterance: str) -> dict:
        doc = self.nlp(utterance)
        matches = self.matcher(doc)

        intents_counter = Counter()
        intents_weight = dict()

        for match_id, start, end in matches:
            intent_id = self.nlp.vocab.strings[match_id]
            intents_counter.update({intent_id})
            intents_weight[intent_id] = intents_counter[intent_id] / sum(intents_counter.values())

        return intents_weight


# nlp = spacy.load("ru_core_news_sm")
# matcher = Matcher(nlp.vocab)
