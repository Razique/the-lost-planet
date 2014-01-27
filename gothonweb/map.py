import random


class Room(object):
    def __init__(self, name, description, helpme):
        self.name = name
        self.description = description
        self.helpme = helpme
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


def generic_death():
    deaths = [
        "You Died",
        "Unfortunately, you didn't make it, sorry bud",
        "Oh No ! Bad choice. You died!",
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    return Room("Death", random.choice(deaths), None)

central_corridor = Room("Central Corridor",
                        """
                The Gothons of Planet Percal #25 have invaded your ship and destroyed
                your entire crew. You are the last surviving member and your last
                mission is to get the neutron destruct bomb from the Weapons Armory,
                put it in the bridge, and blow the ship up after getting into an
                escape pod.

                You're running down the central corridor to the Weapons Armory when
                a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
                flowing around his hate filled body.  He's blocking the door to the
                Armory and about to pull a weapon to blast you...
                """,
                        """
                In this place you have several options - you can try to shoot the Gothon with your gun,
                you can also try to dodge him, of finall, you can even try to tell him a joke if you feel up to.
                So, what will be your call?...
                """)


laser_weapon_armory = Room("Laser Weapon Armory",
                           """
                Lucky for you they made you learn Gothon insults in the academy.
                You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
                The Gothon stops, tries not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in the head
                putting him down, then jump through the Weapon Armory door.

                You do a dive roll into the Weapon Armory, crouch and scan the room
                for more Gothons that might be hiding.  It's dead quiet, too quiet.
                You stand up and run to the far side of the room and find the
                neutron bomb in its container.  There's a keypad lock on the box
                and you need the code to get the bomb out.  If you get the code
                wrong 5 times then the lock closes forever and you can't
                get the bomb.  The code is 4 digits.
                """,
                           """
                   In this room, you need to figure out the right combination, it's a 4 digits code,
                   but try to find the right now, otherwise the lock will close forever,
                   and you won't be able to get the bomb. Do your best!
                """)

the_bridge = Room("The Bridge",
                  """
                The container clicks open and the seal breaks, letting gas out.
                You grab the neutron bomb and run as fast as you can to the
                bridge where you must place it in the right spot.

                You burst onto the Bridge with the netron destruct bomb
                under your arm and surprise 5 Gothons who are trying to
                take control of the ship.  Each of them has an even uglier
                clown costume than the last.  They haven't pulled their
                weapons out yet, as they see the active bomb under your
                arm and don't want to set it off.
                """,
                  """
                You are now on the bridge! you have some options here,
                especially given the fact you are 5 Gothons ou you. You can try to slowly place the bomb,
                use the secret weapon you might have or try to run away.
                What's your call?
                """)

escape_pod = Room("Escape Pod",
                  """
                You point your blaster at the bomb under your arm
                and the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then carefully
                place the bomb on the floor, pointing your blaster at it.
                You then jump back through the door, punch the close button
                and blast the lock so the Gothons can't get out.
                Now that the bomb is placed you run to the escape pod to
                get off this tin can.

                You rush through the ship desperately trying to make it to
                the escape pod before the whole ship explodes.  It seems like
                hardly any Gothons are on the ship, so your run is clear of
                interference.  You get to the chamber with the escape pods, and
                now need to pick one to take.  Some of them could be damaged
                but you don't have time to look.  There's 5 pods, which one
                do you take?
                """,
                  """
                Congrats! You made it to the Escape Pod! You see 5 pods around,
                but only one is not damaged, you don't have the time to look,
                try to focus and find the right one, pick fast, Gothons are all around you!
                """)

the_end_winner = Room("Final Scene",
                      """
                You jump into pod 2 and hit the eject button.
                The pod easily slides out into space heading to
                the planet below.  As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time.  You won!
                """,
                      """
                Congratulations! You made it to the end and you survived.
                This was not an easy one, but you made great!
                """)

the_end_loser = Room("The End",
                     """
                You jump into a random pod and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body
                into jam jelly.
                """,
                     """
                Unfortunately, this was not your day. For sure,
                all these Gothons did not made it easy for you,
                you'll beat them next time!
                """)

central_corridor.add_paths({
    'shoot': generic_death(),
    'dodge': generic_death(),
    'joke': laser_weapon_armory,
})

laser_weapon_armory.add_paths({
    '*': generic_death(),
    '0132': the_bridge,
})

the_bridge.add_paths({
    '*': generic_death(),
    'slowly place the bomb': escape_pod,
})

escape_pod.add_paths({
    '*': the_end_loser,
    '2': the_end_winner,
})

START = central_corridor