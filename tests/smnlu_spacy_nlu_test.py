from smnlu.spacynlu  import SpacyNlu
import unittest


class SpacyNluTestSuite(unittest.TestCase):
    def setUp(self):
        self.spacy_nlu = SpacyNlu("ru_core_news_sm")

    def test_get_intent(self):
        print("E")
        self.spacy_nlu.set_patterns("test", [[{"lower":"test"}]], list())
        self.spacy_nlu.set_patterns("me", [[{"lower":"me"}]], list())

        intents = self.spacy_nlu.get_intents_weightned("Test this utterance for me. Test that.")

        print(intents)

      
    

