# -*- coding: utf-8 -*-
"""The-lost-planet.py: A text-based interactive game."""

__author__ = "Razique Mahroua"
__copyright__ = "Copyright 20459, Planet GC-1450"

import base64
from game_manager import Utils
from sys import exit


class SceneManager(object):
    def __init__(self, next_scene):
        # We init. this value.
        # Depending where the user goes
        # he may have the code or not.
        self.next_scene = next_scene
        self.restart = False

        if next_scene in "Intro":
            Intro()
            exit(0)
        elif next_scene in "The Base":
            TheBase()
            exit(0)
        elif next_scene in "The Alley":
            TheAlley()
            exit(0)
        elif next_scene in "The Cell":
            TheCell()
            exit(0)
        elif next_scene in "The Pipes":
            ThePipes()
            exit(0)
        elif next_scene in "The Jetroom":
            TheJetroom()
            exit(0)
        elif next_scene in "Restart":
            Restart()
            exit(0)
        else:
            print next_scene
            print "Fallback to default value"

    # We instantiate the class Utils and Engine
    # in order to access to the items collection.)
    utils_inst = Utils()


class Intro(SceneManager):
    def __init__(self):
        self.intro_text()
        self.action()

    @staticmethod
    def intro_text():
        print """\t
         _    _             _              _            _                      _
        | |  | |           | |            | |          | |                    | |
        | |_ | |__    ___  | |  ___   ___ | |_   _ __  | |  __ _  _ __    ___ | |_
        | __|| '_ \  / _ \ | | / _ \ / __|| __| | '_ \ | | / _` || '_ \  / _ \| __|
        | |_ | | | ||  __/ | || (_) |\__ \| |_  | |_) || || (_| || | | ||  __/| |_
         \__||_| |_| \___| |_| \___/ |___/ \__| | .__/ |_| \__,_||_| |_| \___| \__|
                                                | |
                                                |_|

        Welcome !
            You are an astronaut, in a mission on the GC-1450 planet.
            Before landing, one of the thrusters suddenly ceases to work, but you are abe to make it up before you ship crashes.
            Before leaving you can only take 3 items. Choose them carefully.
            Hit 'ENTER' to confirm your item:
            """

    def action(self):
    # We iterate on items list
        for i in self.utils_inst.items[:]:
            print "\t 1 x", i

        # We loop as long as the user doesn't have 3 items.
        while len(self.utils_inst.player_items) != 3:
            prompt = raw_input("Pick your items > ").lower()

            # Does the user has typed an item that exists?
            if prompt not in self.utils_inst.items:
                print "That item doesn't exist! Please try again: \n"

            # if so...then we append it
            # to the user list and remove it
            # from the items list
            elif prompt not in self.utils_inst.player_items:
                self.utils_inst.player_items.append(prompt)
                self.utils_inst.items.remove(prompt)
            else:
                print "You already have chosen that item !"

            print "You have the", len(self.utils_inst.player_items), "following items with you:"
            for i in self.utils_inst.player_items:
                print "\t1 x", i

            print "Items left:"
            for i in self.utils_inst.items:
                print "\t1 x", i

            print "\n"

        print "You can now continue your space exploration..."
        SceneManager("The Base")


class TheBase(SceneManager):
    def __init__(self):
        self.intro_text()
        self.action()

    @staticmethod
    def intro_text():
        print """
        ------------ * The Base * ---------------
        You are then ready to continue your journey.
        You then move towards the contacting unit, ready to contact the planet Earth, but the radio seems to be broken.
        """

    def action(self):
        base_first_action = "Are you trying to fix it or do you continue your exploration ?"
        base_second_action = "Do you continue to fix the radio or do you decide to get closer to the sound?"
        base_first_decision = 0
        base_second_decision = 0

        while base_first_decision not in ("fix", "continue"):
            print base_first_action
            base_first_decision = raw_input("Fix or Continue? >").lower()
            print base_first_decision

        if base_first_decision == "fix":
            if self.utils_inst.check_item("knife") is False:
                print "Unfortunately, you don't have the knife with you, " \
                      "you need to move on, you continue to the alley..."
                SceneManager("The Base")
            else:
                print "You are trying to fix the radio, using your knife while all of a sudden,"
                print "you hear some mysterious noise coming from the alley behind."

                print base_second_action
                while base_second_decision not in ("continue", "get closer"):
                    base_second_decision = raw_input("Continue or Get closer ?").lower()
                    if base_second_decision == "continue":
                        print "You decide to ignore the crackling noise and keep trying to fix the radio."
                        print "The radio starts to work again, and you are able to contact the base..."
                        print "but before you have the time to notice, you get hit by something and faint.\n"
                        SceneManager("The Cell")

                    elif base_second_decision == "get closer":
                        SceneManager("The Alley")
        else:
            SceneManager("The Alley")


class TheAlley(SceneManager):
    def __init__(self):
        self.intro_text()
        self.action()

    @staticmethod
    def intro_text():
        print "------------ * The Alley * ---------------"

        print "You are now into the alley"
        print "You walking and doing your best to be quiet... "
        print "You can hear some aliens having some sort of a dialogue from the door next to you. "
        print "If you have taken the decoder, you can decode their dialogue."

    def action(self):
        first_action = "Did you take the decoder with you?"
        self.utils_inst.prompt(first_action)

        # Did the user took the decoder?
        if self.utils_inst.check_item("decoder"):
            print "You took your decoder! Through the decoder, you hear some aliens talking about " \
                  "the control of the whole galaxy."
            print "These aliens are now en route to the conquest of the planet. "
            print "Hopefully you have recorded their alien language."
            print "You continue and you see a room, you decide to enter...\n"

            # If so, the it gets the code and go to the jetroom
            self.utils_inst.has_the_code = True
            SceneManager("The Jetroom")

        else:
            print "Unfortunately, you left the decoder into the ship..."
            print "If you have taken the gunfire, you decide to hide near and wait form them to get out"
            message = "Do you have the laser gunfire with you?"
            self.utils_inst.prompt(message)

            # Did he take the gunfire w/ him?
            if self.utils_inst.check_item("gunfire"):
                print "Once they are out, you point your gun at them and tie them, ready to question them."
                print "Unfortunately, they don't tell a single word. "
                print "You will go back at them later, after exploring the base..."
                # But no code
                self.utils_inst.has_the_code = False
                SceneManager("The Jetroom")

            else:
                print "Unfortunately, you left the gunfire into the ship... you need to move on."
                SceneManager("The Jetroom")


class TheCell(SceneManager):
    def __init__(self):
        self.intro_text()
        self.action()

    @staticmethod
    def intro_text():
        print "------------ * The Cell * ---------------"

        print "You wake up and you find yourself, all locked up... but there is a trapdoor."
        print "If you have the screwdriver or knife with you can cut the ropes and escape"

    def action(self):
        first_action = "Do you think you have on of these items with you?"
        self.utils_inst.prompt(first_action)
        # Did the took either the screwdriver or the knife?
        if self.utils_inst.check_item("screwdriver") or self.utils_inst.check_item("knife"):
            print "Hooray, you find a sharp tool in your pocket! You untie yourself and open the trapdoor " \
                  "and get in there.\n"
            SceneManager("The Pipes")

        else:
            print "Unfortunately, you left the knife into the ship.. "
            print "You try to escape, but 5 minutes later, one weird alien appears and kills at you."
            print "You die in no time..."
            SceneManager("Restart")


class ThePipes(SceneManager):
    def __init__(self):
        self.text_intro()
        self.action()

    @staticmethod
    def text_intro():
        print "------------ * The Pipes * ---------------"

        print "It's dark in there. If you have the flashlight, you can use it."""

    def action(self):
        first_action = "Do you think you have the pocket lamp with you?"
        self.utils_inst.prompt(first_action)

        if self.utils_inst.check_item("flashlight"):
            print "You can see where you are heading to, and fortunately avoid a gap under you. "
            print "You see a launching base, and a small jet. You go there..."
            # Unfortunately, no code!
            self.utils_inst.has_the_code = False
            SceneManager("The Jetroom")

        else:
            print "Unfortunately, you don't have the flashlight.."
            print "You are walking and you fall into a gap you haven't seen...\n"
            SceneManager("The Alley")


class TheJetroom(SceneManager):
    def __init__(self):
        self.intro_text()
        self.action()

    @staticmethod
    def intro_text():
        print "------------ * The Jet Room * ---------------"

        print "Inside that Jet room, find a small jet. You look around and try to power it on."

    def action(self):
        message = "But one thruster is missing. Do you have the portable one ?"
        self.utils_inst.prompt(message)
        if self.utils_inst.check_item("portable quantum thruster"):
            print "Hopefully you have it with you...You plug it into and power the engine on."

            if self.utils_inst.has_the_code:
                print "Using the decoder, you are able to find the sequence."
                print "You set the coordinates into the console and initiate the launching sequence"
                print "The aliens are coming to you, but you are already into the vessel, and safe. Congratulations ! "
                print"""
                 _    _      _ _       _
                | |  | |    | | |     | |
                | |  | | ___| | |   __| | ___  _ __   ___
                | |/\| |/ _ \ | |  / _` |/ _ \| '_ \ / _ \\
                \  /\  /  __/ | | | (_| | (_) | | | |  __/
                 \/  \/ \___|_|_|  \__,_|\___/|_| |_|\___
                """
                exit(0)
            else:
                passcode = ".¨¨M:=/iuiiD + Cap%`::Oui%> "
                password = base64.b64decode("VGhpcyBpcyBub3QgdGhlIHBhc3N3b3JkISBHb29kIGNhdGNoIQ==")
                base64.b64decode("sdsd")

                print "You log into the main console, and it requires a passcode. The hint now says: %s " % passcode
                print "Can you figure the passcode?\n"
                chances = 3
                while chances != 0:
                    print "\n"
                    print "%d F%%sdEwUii left" % chances
                    print "-----------------"
                    action = raw_input(passcode)
                    chances -= 1

            print "\n ...Unfortunately, the aliens are now coming to you are now pointing at you " \
                  "your gunfire they took you."
            SceneManager("Restart")

        else:
            print "Unfortunately, you left it to your ship, and try to get it."
            print "But before you realize, the aliens have untied themselves and are pointing at you a laser beam..." \
                  "BAM!"
            SceneManager("Restart")


# Game over....
class Restart(SceneManager):
    def __init__(self):
        self.intro_text()
        self.action()

    @staticmethod
    def intro_text():
        print """
           ___                         ___
          / _ \__ _ _ __ ___   ___    /___\__   _____ _ __
         / /_\/ _` | '_ ` _ \ / _ \  //  //\ \ / / _ \ '__|
        / /_\\\\ (_| | | | | | |  __/ / \_//  \ V /  __/ |
        \____/\__,_|_| |_| |_|\___| \___/    \_/ \___|_|


                                                       """
    @staticmethod
    def action():
        message = "As Bastet, we believe you have 9 lives. Would you try again?"

        print message
        action = raw_input("Yes or No? >").lower()

        while action not in ["yes", "no"]:
            action = raw_input("Yes or No? >").lower()
        if action == "yes":
            # We restore the items list and reset the player list
            Utils.items.extend(Utils.player_items)
            Utils.player_items = []
            SceneManager("Intro")
        else:
            print "Adios amigos!"