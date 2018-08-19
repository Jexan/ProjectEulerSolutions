import unittest

TESTING_NOW = 65

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

def assure_003(self):
    from Complete.E003 import result
    self.assertEqual(result, 6857)

def assure_004(self):
    from Complete.E004 import result
    self.assertEqual(result, 906609)

def assure_005(self):
    from Complete.E005 import result
    self.assertEqual(result, 232792560)

def assure_006(self):
    from Complete.E006 import result
    self.assertEqual(result, 25164150)

def assure_007(self):
    from Complete.E007 import result
    self.assertEqual(result, 104743)

def assure_008(self):
    from Complete.E008 import result
    self.assertEqual(result, 23514624000)

def assure_009(self):
    from Complete.E009 import result
    self.assertEqual(result, 31875000)

def assure_010(self):
    from Complete.E010 import result
    self.assertEqual(result, 142913828922)

def assure_013(self):
    from Complete.E013 import result
    self.assertEqual(result, 5537376230)

def assure_015(self):
    from Complete.E015 import result
    self.assertEqual(result, 137846528820)

def assure_016(self):
    from Complete.E016 import result
    self.assertEqual(result, 1366)

def assure_017(self):
    from Complete.E017 import result
    self.assertEqual(result, 21124)

def assure_022(self):
    from Complete.E022 import result
    self.assertEqual(result, 871198282)

def assure_026(self):
    from Complete.E026 import result
    self.assertEqual(result, 983)

def assure_034(self):
    from Complete.E034 import result
    self.assertEqual(result, 40730)

def assure_043(self):
    from Complete.E043 import result
    self.assertEqual(result, 16695334890)

def assure_065(self):
    from Complete.E065 import result
    self.assertEqual(result, 272)