# -*- coding : utf-8 -*-


class AssertLexicon(object):
    def __init__(self):
        pass

    @staticmethod
    def lexicon(user_sentence, room, test=False):
        lexicon = {
            'Central Corridor': ('shoot', 'dodge', 'joke'),
            'Laser Weapon Armory': ('*', '0132'),
            'The Bridge': ('*', 'slowly place the bomb'),
            'Escape Pod': ('*', '2'),
            'The End': ('a', 'b'),
            'Default': ''
        }
        result = False
        action = user_sentence.split()
        for i in action:
            # We limit the character size in order to avoid single letters match
            if (i.isalpha() and len(i) > 3) or i.isdigit():
                if i in lexicon[room][-1]:
                    result = lexicon[room][-1]
        return result


if __name__ == '__main__':
    launcher = AssertLexicon()
    launcher.lexicon('default', 'Default', test=False)