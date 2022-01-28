import unittest
from soma import soma

class TestStringMethods(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(4, soma(2,2))

if __name__ == '__main__':
    unittest.main()