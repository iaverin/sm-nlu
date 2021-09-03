from dataclasses import dataclass

from typing import Counter, List, TypedDict, Union
import spacy
from spacy.matcher import Matcher


# class Intent(dataclasses):
#     intent_id: TypedDict("Intent", {"id":str, "confidence":float })


class Intent:

    def __init__(self, id: str, patterns_match: List, patterns_stop: List):
        self.id = id
        self.patterns_match = patterns_match
        self.patterns_stop = patterns_stop


class SpacyNlu:
    PATTERN_STOP_SUFFIX = "_int_stop"

    def __init__(self, model: str, intents: List[Intent]) -> None:
        self.nlp = spacy.load(model)
        self.matcher = Matcher(self.nlp.vocab)
        self.intents: List[Intent] = self._init_intents(intents)

    def intent(self, utterance: str) -> Union[Intent, None]:
        matched_patterns = self._get_matched_patterns(utterance)
        for intent in self.intents:
            if self._intent_fits_patterns(intent, matched_patterns):
                return intent
        return None

    # private supplementary methods 
    def _init_intents(self, intents: List[Intent]) -> List[Intent]:
        for intent in intents:
            self.matcher.add(self._intent_match_pattern_id(intent), intent.patterns_match)
            self.matcher.add(self._intent_stop_pattern_id(intent), intent.patterns_stop)
        return intents

    def _get_matched_patterns(self, utterance: str) -> list[str]:
        doc = self.nlp(utterance)
        matches = self.matcher(doc)
        matched_patterns = list()
        for match in matches:
            pattern_id = self.nlp.vocab.strings[match[0]]
            if pattern_id not in matched_patterns:
                matched_patterns.append(pattern_id)

        return matched_patterns

    def _intent_match_pattern_id(self, intent: Intent):
        return intent.id

    def _intent_stop_pattern_id(self, intent: Intent):
        return intent.id + self.PATTERN_STOP_SUFFIX

    def _intent_fits_patterns(self, intent: Intent, matched_patterns: List[str]) -> bool:
        if self._intent_match_pattern_id(intent) in matched_patterns and \
                self._intent_stop_pattern_id(intent) not in matched_patterns:
            return True
        return False

# nlp = spacy.load("ru_core_news_sm")
# matcher = Matcher(nlp.vocab)
