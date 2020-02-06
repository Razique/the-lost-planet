from unittest import TestCase
from game import game_lexicon


class TestGameLexicon(TestCase):
    def test_init(self):
        self.test_lexicon = game_lexicon.AssertLexicon()
        self.assertEqual(self.test_lexicon.lexicon("continue", test=True), [('action', 'continue')])
        self.assertEqual(self.test_lexicon.lexicon("fix", test=True), [('action', 'fix')])
        self.assertEqual(self.test_lexicon.lexicon("base", test=True), [('places', 'base')])
        self.assertEqual(self.test_lexicon.lexicon("go to jetroom", test=True), [('action', 'go'), ('action', 'to'),
                                                                                 ('places', 'jetroom')])




