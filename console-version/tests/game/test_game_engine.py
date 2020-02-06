from unittest import TestCase
from game import game_engine


class TestEngine(TestCase):
    def test_init(self):
        self.test_launch = game_engine.Engine()
        self.assertEqual(self.test_launch.start("test_ok", test=True), "test_ok")
