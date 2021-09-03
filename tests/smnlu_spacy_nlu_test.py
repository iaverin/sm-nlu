from smnlu.spacynlu import Intent, SpacyNlu
import unittest


class SpacyNluTestSuite(unittest.TestCase):
    def setUp(self):

        intents = [
            Intent(
                id="test",
                patterns_match=[[{"lower": "test"}]],
                patterns_stop=[[{"lower": "error"}]]
            ),
            Intent(
                id="lorem_ipsum",
                patterns_match=[[{"lower": "lorem"}]],
                patterns_stop=[]
            )

        ]

        self.spacy_nlu = SpacyNlu("ru_core_news_sm", intents=intents)

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
