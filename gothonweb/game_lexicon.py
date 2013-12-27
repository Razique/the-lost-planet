# -*- coding : utf-8 -*-


class ListActions(object):
    def __init__(self):
        pass

    @staticmethod
    def actions(items):
        lexion = {
            'Central Corridor': ['shoot', 'dodge', 'tell a joke'],
            'Laser Weapon Armory': ['0132', '*'],
            'The Bridge': ['throw the bomb','slowly place the bomb'],
            'Escape Pod': ['2', '*'],
            'The End': ['a', 'b'],
            'Default': ['']

        }
        if items not in lexion:
            return lexion['Default']
        else:
            return lexion[items]

if __name__ == '__main__':
    launcher = ListActions()
    launcher.actions('Central Corridor')