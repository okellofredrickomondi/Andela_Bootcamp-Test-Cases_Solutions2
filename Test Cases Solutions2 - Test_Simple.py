import unittest

class Simpletest(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(True)
    def test_if_false(self):
        self.assertFalse(False)

if __name__ == "__main__":
    unittest.main()
