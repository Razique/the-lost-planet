# -*- coding : utf-8 -*-


class ListActions(object):
    def __init__(self):
        pass

    @staticmethod
    def actions(items):
        lexion = {
            'Central Corridor': ['shoot', 'dodge', 'tell a joke'],
            'Laser Weapon Armory': ['a', 'b'],
            'The Bridge': ['a', 'b'],
            'Escape Pod': ['a', 'b'],
            'The End': ['a', 'b'],

        }
        if items not in lexion:
            return lexion['Central Corridor']
        else:
            return lexion[items]

if __name__ == '__main__':
    launcher = ListActions()
    launcher.actions('Central Corridor')



