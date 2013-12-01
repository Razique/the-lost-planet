# -*- coding: utf-8 -*-

"""The-lost-planet.py: A text-based interactive game."""

__author__ = "Razique Mahroua"
__copyright__ = "Copyright 20459, Planet GC-1450"

from game_manager import Utils
from scenes import SceneManager


class Engine(object):
    def __init__(self):
        pass

    # Scene init.
    @staticmethod
    def start(scene):
        SceneManager(scene)

# We launch the game!
game = Engine()

game.start("The Jetroom")
