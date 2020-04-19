import unittest
import random
import time

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_fails_quarter_time(self):
        if random.randint(1,4) == 1:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_variable_time(self):
        # Test that takes variable amount of time
        time.sleep(random.randint(0,10))
        self.assertEqual(True, True)

if __name__ == "__main__":
    unittest.main()
