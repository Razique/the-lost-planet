# -*- coding: utf-8 -*-
"""The-lost-planet.py: A text-based interactive game."""

__author__ = "Razique Mahroua"
__copyright__ = "Copyright 20459, Planet GC-1450"

from scenes import SceneManager


class Engine(object, ):
    def __init__(self):
        pass

    # Scene init.
    @staticmethod
    def start(scene, test=False):
        if test is False:
            SceneManager(scene)
        else:
            init = SceneManager(scene)
            return init.no_scene()

# We launch the game!
if __name__ == "__main__":
    game = Engine()
    game.start("Intro")
