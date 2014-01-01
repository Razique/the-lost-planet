# -*- coding : utf-8 -*-


class AssertLexicon(object):
    def __init__(self):
        pass

    @staticmethod
    def lexicon(user_sentence, room, test=False):
        lexicon = {
            'Central Corridor': ['shoot', 'dodge', 'joke'],
            'Laser Weapon Armory': ['*', '0132'],
            'The Bridge': ['throw the bomb', 'slowly place the bomb'],
            'Escape Pod': ['2', '*'],
            'The End': ['a', 'b'],
            'Default': ['']

        }
        result = False
        action = user_sentence.split()
        for i in action:
            if i in lexicon[room][-1]:
                result = lexicon[room][-1]
        return result


class ListActions(object):
    def __init__(self):
        pass

    @staticmethod
    def actions(items):
        lexicon = {
            'Central Corridor': ['shoot', 'dodge', 'tell a joke'],
            'Laser Weapon Armory': ['0132', '*'],
            'The Bridge': ['throw the bomb', 'slowly place the bomb'],
            'Escape Pod': ['2', '*'],
            'The End': ['a', 'b'],
            'Default': ['']

        }
        if items not in lexicon:
            return lexicon['Default']
        else:
            return lexicon[items]

if __name__ == '__main__':
    launcher = ListActions()
    launcher.actions('Central Corridor')