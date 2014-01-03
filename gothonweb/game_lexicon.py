# -*- coding : utf-8 -*-


class AssertLexicon(object):
    def __init__(self):
        self.lexicon = {
            'Central Corridor': ('shoot', 'dodge', 'joke'),
            'Laser Weapon Armory': ('*', '0132'),
            'The Bridge': ('*', 'slowly place the bomb'),
            'Escape Pod': ('*', '2'),
            'The End': ('a', 'b'),
        }

    def parse_lexicon(self, user_sentence, room, test=False):
        #TODO Unit testing
        result = False
        action = user_sentence.split()
        for i in action:
            # We limit the character size in order to avoid single letters match
            if (i.isalpha() and len(i) > 3) or i.isdigit():
                if i in self.lexicon[room][-1]:
                    result = self.lexicon[room][-1]
        return result

    def return_rooms(self):
        rooms = []
        for i in sorted(self.lexicon.iterkeys()):
            rooms.append(i)
        return rooms

if __name__ == '__main__':
    launcher = AssertLexicon()
    launcher.parse_lexicon('default', 'Default', test=False)