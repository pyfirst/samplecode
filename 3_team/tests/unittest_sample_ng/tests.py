import unittest

class Test(unittest.TestCase):
    def test_it(self):
        import sample
        value = sample.add(1, 1)
        self.assertEqual(2, value)
