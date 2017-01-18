import unittest

class TestMessageFailure(unittest.TestCase):
    def test_fail(self):
        self.assertTrue(False, 'This is a failure message.')

if __name__ == '__main__':
unittest.main()