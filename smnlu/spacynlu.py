from dataclasses import dataclass

from typing import Counter, List, TypedDict, Union
import spacy
from spacy.matcher import Matcher

# class Intent(dataclasses):
#     intent_id: TypedDict("Intent", {"id":str, "confidence":float })


class Intent():
    PATTERN_STOP_SUFFIX = "_int_stop"

    def __init__(self, id: str, patterns_match: List, patterns_stop: List):
        self.id = id
        self.patterns_match = patterns_match
        self.patterns_stop = patterns_stop

    def match_pattern_id(self):
        return self.id

    def stop_patten_id(self):
        return self.id+self.PATTERN_STOP_SUFFIX
    
    def fits_patterns(self, matched_patterns: List[str]) -> bool:
        if self.match_pattern_id() in matched_patterns and \
            self.stop_patten_id() not in matched_patterns:
            return True
        
        return False



class SpacyNlu:

    def __init__(self, model: str, intents: List[Intent]) -> None:
        self.nlp = spacy.load(model)
        self.matcher = Matcher(self.nlp.vocab)
        self.intents: List[Intent] = self._init_intents(intents)

    def intent(self, utterance: str) -> Union[Intent, None]:
        matched_patterns = self._get_matched_patterns(utterance)
        for intent in self.intents:
            if intent.fits_patterns(matched_patterns):
                return intent
        return None

    # private supplementary methods 
    def _init_intents(self, intents: List[Intent]) -> List[Intent]:
        for intent in intents:
            self.matcher.add(intent.match_pattern_id(), intent.patterns_match)
            self.matcher.add(intent.stop_patten_id(), intent.patterns_stop)
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



# nlp = spacy.load("ru_core_news_sm")
# matcher = Matcher(nlp.vocab)
