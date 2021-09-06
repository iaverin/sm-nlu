from smnlu.spacynlu import Intent, SpacyNlu, IntentPatternsWithDiscardMapping
import unittest


class SpacyNluTestSuite(unittest.TestCase):
    def setUp(self):
        self.lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        self.seddo = "sed do eiusmod tempor incididunt ut labore et dolore magna alqua."

        self.intents = [
            Intent(
                id="test",
                patterns_match=[[{"lower": "test"}]],
                patterns_discard=[[{"lower": "error"}]]
            ),
            Intent(
                id="lorem_ipsum",
                patterns_match=[[{"lower": "lorem"}]],
                patterns_discard=[]
            ),
            Intent(
                id="ipsum_single_lorem_context",
                patterns_match=[[{"lower": "ipsum"}]],
                patterns_discard=[],
                contexts={'lorem'}
            ),
            Intent(
                id="ipsum_with_dolor_and_sit_context",
                patterns_match=[[{"lower": "ipsum"}]],
                patterns_discard=[],
                contexts={'dolor', 'sit'}
            ),
            Intent(
                id='seddo_in_global_and_ipsum_context',
                patterns_match=[[{"lower": "sed"}]],
                patterns_discard=[],
                contexts={'ipsum', 'global'}
            )

        ]

        self.spacy_nlu = SpacyNlu("ru_core_news_sm", intents=self.intents,
                                  intent_patterns_matcher=IntentPatternsWithDiscardMapping())

    def test_intent(self):
        intent = self.spacy_nlu.intent(
            "Test this utterance for me. Test that.")
        self.assertEqual("test", intent.id)

        intent = self.spacy_nlu.intent(
            "Test this utterance for me. Test that. Error.")
        self.assertIsNone(intent)

        intent = self.spacy_nlu.intent(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
             sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

        self.assertEqual("lorem_ipsum", intent.id)

        intent = self.spacy_nlu.intent("Blah blah blah")
        self.assertIsNone(intent)

    def test_intent_with_context(self):
        self.assertEqual("ipsum_single_lorem_context", self.spacy_nlu.intent(self.lorem, contexts={'lorem'}).id)

        self.assertEqual("ipsum_with_dolor_and_sit_context", self.spacy_nlu.intent(self.lorem,
                                                                                   contexts={'dolor', 'sit'}).id)

        self.assertEqual("ipsum_with_dolor_and_sit_context", self.spacy_nlu.intent(self.lorem,
                                                                                   contexts={'dolor'}).id)

        self.assertEqual("ipsum_with_dolor_and_sit_context", self.spacy_nlu.intent(self.lorem,
                                                                                   contexts={'sit'}).id)

        self.assertEqual("ipsum_with_dolor_and_sit_context", self.spacy_nlu.intent(self.lorem,
                                                                                   contexts={'sit'}).id)

        self.assertEqual("seddo_in_global_and_ipsum_context", self.spacy_nlu.intent(self.seddo).id)

        self.assertEqual("seddo_in_global_and_ipsum_context", self.spacy_nlu.intent(self.seddo, contexts={'ipsum'}).id)
