import unittest
import Complete as C

TESTING_NOW = 1

class TestCompleteChallengesYieldCorrectResults(unittest.TestCase):
    def test_assure_given_ok(self):
        string = str(TESTING_NOW)
        n_zeroes = '0' * (3 - len(string))

        eval('assure_{}(self)'.format(n_zeroes + string))

def assure_001(self):
    from Complete.E001 import result
    self.assertEqual(result, 233168)
