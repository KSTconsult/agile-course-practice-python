import unittest

from my_set.model.my_set import MySet


class TestSetClass(unittest.TestCase):
    def test_can_init_with_default_constructor(self):
        test_set = MySet()
        self.assertTrue(isinstance(test_set, MySet))
