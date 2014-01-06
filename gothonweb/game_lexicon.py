# -*- coding : utf-8 -*-
import map


class AssertLexicon(object):
    def __init__(self):
        self.lexicon = {
            map.central_corridor.name: ('shoot', 'dodge', 'joke'),
            map.laser_weapon_armory.name: ('*', '0132'),
            map.the_bridge.name: ('*', 'slowly place the bomb'),
            map.escape_pod.name: ('*', '2'),
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

    def return_room_name(self, room):
        room_name = self.lexicon
        for i in self.lexicon[room]:
            print i[1]
        #return room_name
        #return room

if __name__ == '__main__':
    launcher = AssertLexicon()
    launcher.parse_lexicon('default', 'Default', test=False)