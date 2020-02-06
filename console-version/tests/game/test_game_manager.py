from unittest import TestCase
from game import game_manager


class TestUtils(TestCase):
    def test_init(self):
        self.test_utils = game_manager.Utils()
        self.assertFalse(self.test_utils.message)
        self.assertEqual(self.test_utils.prompt("test_value", test=True), 0)
        self.assertFalse(self.test_utils.has_the_code)
        self.assertListEqual(self.test_utils.items, ['laser gunfire', 'flashlight', 'knife', 'screwdriver', 'decoder', 'portable quantum thruster'])
        self.assertFalse(self.test_utils.check_item("test_item"))




