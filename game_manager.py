# -*- coding : utf-8 -*-
"""The-lost-planet.py: A text-based interactive game."""

__author__ = "Razique Mahroua"
__copyright__ = "Copyright 20459, Planet GC-1450"


class Utils(object):
    def __init__(self):
        self.message = False

    # We loop on a prompt as long as the
    # user doesn't type YES or NO
    @staticmethod
    def prompt(message):
        first_decision = 0
        while first_decision != "no" and first_decision != "yes":
            print message
            first_decision = raw_input("Yes or No? >").lower()
        return True

    # We init the user items
    player_items = []
    has_the_code = False
    # List ot objects left in the ship
    items = [
        "laser gunfire",
        "flashlight",
        "knife",
        "screwdriver",
        "decoder",
        "portable quantum thruster"
    ]

    # That attribute checks the items
    # the user has and returns TRUE orFALSE
    def check_item(self, item):
        if item not in self.player_items:
            return False
        else:
            return True
