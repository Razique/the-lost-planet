# -*- coding : utf-8 -*-
"""The-lost-planet.py: A text-based interactive game."""

__author__ = "Razique Mahroua"
__copyright__ = "Copyright 20459, Planet GC-1450"

# This class compares the user input against a tuple of pre-defined words and actions
# Returns stop if we don't understand the word request, otherwise we return the tuple


class AssertLexicon(object):
    def __init__(self):
        pass

    @staticmethod
    def lexicon(user_entry=[''], test=False):
        action_lexicon = ('action', 'use', 'fix', 'continue', 'get', 'go', 'closer', 'move', 'to')
        items_lexicon = ('items', 'laser gunfire', 'flashlight', 'knife', 'screwdriver', 'decoder',
                         'portable quantum thruster')

        places_lexicon = ('places', 'base', 'alley', 'cell', 'pipes', 'jetroom')
        lexicons_group = action_lexicon+items_lexicon+places_lexicon
        table = []

        if test is False:
            user_input = raw_input('> ').lower()
            action = user_input.split()
        else:
            action = user_entry.split()

        for i in action:
            if i in lexicons_group:
                if i in action_lexicon:
                    table.append((action_lexicon[0], i))
                elif i in items_lexicon:
                    table.append((items_lexicon[0], i))
                else:
                    table.append((places_lexicon[0], i))
            else:
                table.append(('stop', i))

        if test is True:
            return table
        else:
            print table

if __name__ == '__main__':
    launcher = AssertLexicon()
    launcher.lexicon()



