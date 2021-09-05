from dataclasses import dataclass
from enum import Enum
import collections
from typing import Counter, List, TypedDict, Union, Any
import spacy
from spacy.matcher import Matcher

DEFAULT_INTENT_CONTEXT = "global"


@dataclass
class Pattern:
    id: str
    pattern: list


class Intent:
    def __init__(self, id: str, patterns_match: List, patterns_discard: List, contexts: set[str] = None):
        self.id = id
        self.patterns_match = patterns_match
        self.patterns_discard = patterns_discard
        self.contexts: set = set(_default_value_if_none(contexts, {DEFAULT_INTENT_CONTEXT}))


class InterfaceIntentPatternsMapping:
    def __init__(self):
        pass

    def pattern_ids_from_intent(self, intent: Intent) -> List[Pattern]:
        pass

    def intent_fits_patterns(self, intent: Intent, patterns: List[str]) -> bool:
        pass


class IntentPatternsWithDiscardMapping(InterfaceIntentPatternsMapping):
    PATTERN_NAME_PREFIX = "_p_"
    PATTERN_STOP_SUFFIX = "_p_stop_"

    def _pattern_id_to_match(self, intent: Intent) -> str:
        return self.PATTERN_NAME_PREFIX + intent.id

    def _pattern_id_to_discard_matching(self, intent: Intent) -> str:
        return self.PATTERN_STOP_SUFFIX + intent.id

    def pattern_ids_from_intent(self, intent: Intent) -> List[Pattern]:
        return list([
            Pattern(id=self._pattern_id_to_match(intent), pattern=intent.patterns_match),
            Pattern(id=self._pattern_id_to_discard_matching(intent), pattern=intent.patterns_discard)])

    def intent_fits_patterns(self, intent: Intent, matched_patterns: List[str]) -> bool:
        if self._pattern_id_to_match(intent) in matched_patterns and \
                self._pattern_id_to_discard_matching(intent) not in matched_patterns:
            return True
        return False


class SpacyNlu:

    def __init__(self, model: str, intents: List[Intent], intent_patterns_matcher: InterfaceIntentPatternsMapping):
        self.nlp: spacy.Language = spacy.load(model)
        self.matcher = Matcher(self.nlp.vocab)
        self.intents: List[Intent] = intents
        self._intent_patterns_matcher: InterfaceIntentPatternsMapping = intent_patterns_matcher

        self._add_intents_patterns_to_matcher(intents)

    def intent(self, utterance: str, contexts: set[str] = None) -> Union[Intent, None]:
        contexts_to_match = set(_default_value_if_none(contexts, {DEFAULT_INTENT_CONTEXT}))
        matched_patterns = self._get_matched_patterns(utterance)
        for intent in self.intents:
            if self._intent_patterns_matcher.intent_fits_patterns(intent, matched_patterns) \
                    and intent.contexts.intersection(contexts_to_match):
                return intent
        return None

    def _add_intents_patterns_to_matcher(self, intents: List[Intent]) -> None:
        matcher = self.matcher
        intent_pattern_matcher = self._intent_patterns_matcher

        for intent in intents:
            patterns_to_add = intent_pattern_matcher.pattern_ids_from_intent(intent)
            for pattern in patterns_to_add:
                matcher.add(pattern.id, pattern.pattern)

    def _get_matched_patterns(self, utterance: str) -> list[str]:
        doc = self.nlp(utterance)
        matches = self.matcher(doc)
        matched_patterns = list(set([self.nlp.vocab.strings[x[0]] for x in matches]))

        return matched_patterns


def _default_value_if_none(value, default_value):
    if value is None:
        return default_value
    return value

# nlp = spacy.load("ru_core_news_sm")
# matcher = Matcher(nlp.vocab)
