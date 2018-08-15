import unittest
import Complete as C

TESTING_NOW = 2

class TestCompleteChallengesYieldCorrectResults(unittest.TestCase):
    def test_assure_given_ok(self):
        challenge_number = str(TESTING_NOW)
        zeroes_padding = '0' * (3 - len(challenge_number))

        eval('assure_{}(self)'.format(zeroes_padding + challenge_number))

def assure_001(self):
    from Complete.E001 import result
    self.assertEqual(result, 233168)

def assure_002(self):
    from Complete.E002 import result
    self.assertEqual(result, 4613732)
