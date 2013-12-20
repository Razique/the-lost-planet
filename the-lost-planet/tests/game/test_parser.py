from unittest import TestCase
from game import parser


class TestParser(TestCase):
    def test_peek(self):
        self.sentence = [('noun', 'princess'), ('verb', 'kill'), ('direction', 'jetroom')]
        test_init = parser.peek(self.sentence)
        #print test_init
        self.assertEquals(test_init, 'noun')

    def test_match(self):
        self.sentence = [('noun', 'princess')]
        test_init = parser.match(self.sentence, 'noun')
        self.assertEquals(test_init, ('noun', 'princess'))

    def test_skip(self):
        self.sentence = [('stop', 'inexistant')]
        test_init = parser.skip(self.sentence, 'stop')
        self.assertEqual(test_init, None)

    def test_parse_verb(self):
        self.sentence = [('verb', 'kill')]
        test_init = parser.parse_verb(self.sentence)
        self.assertEqual(test_init, ('verb', 'kill'))

    def test_parse_object(self):
        self.sentence = [('noun', 'princess')]
        test_init = parser.parse_object(self.sentence)
        self.assertEqual(test_init, ('noun', 'princess'))

    def test_parse_subject(self):
        self.sentence = [('verb', 'kill'), ('noun', 'princess'), ('verb', 'jump')]
        self.subject = ('noun', 'me')
        test_init = parser.parse_subject(self.sentence, self.subject)
        self.assertEqual(test_init.subject, 'me')
        self.assertEqual(test_init.verb, 'kill')
        self.assertEqual(test_init.object, 'princess')

    def test_parse_sentence(self):
        self.sentence = [('verb', 'kill'), ('noun', 'princess'), ('verb', 'kill')]
        # Test word list for parser to parse
        word_list = [('verb', 'verb'), ('stop', 'stop'), ('noun', 'noun')]
        test_init = parser.parse_sentence(word_list)
        self.assertEqual(test_init, parser.Sentence(('nfoun', 'player'), ('verb', 'verb'), ('noun', 'noun')))
