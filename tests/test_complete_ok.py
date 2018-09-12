import unittest
import subprocess
import os

TESTING_NOW = 61

def get_haskell_output(n):
    program = os.path.join(os.getcwd(), 'Complete', 'E{}'.format(n))
    return int(subprocess.check_output(program))

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

def assure_011(self):
    from Complete.E011 import result
    self.assertEqual(result, 70600674)

def assure_012(self):
    result = get_haskell_output('012')
    self.assertEqual(result, 76576500)

def assure_013(self):
    from Complete.E013 import result
    self.assertEqual(result, 5537376230)

def assure_014(self):
    from Complete.E014 import result
    self.assertEqual(result, 837799)

def assure_015(self):
    from Complete.E015 import result
    self.assertEqual(result, 137846528820)

def assure_016(self):
    from Complete.E016 import result
    self.assertEqual(result, 1366)

def assure_017(self):
    from Complete.E017 import result
    self.assertEqual(result, 21124)

def assure_018(self):
    from Complete.E018 import result
    self.assertEqual(result, 1074)

def assure_019(self):
    from Complete.E019 import result
    self.assertEqual(result, 171)

def assure_020(self):
    from Complete.E020 import result
    result2 = get_haskell_output('020')
    
    self.assertEqual(result, result2)
    self.assertEqual(result, 648)

def assure_021(self):
    result = get_haskell_output('021')
    self.assertEqual(result, 31626)

def assure_022(self):
    from Complete.E022 import result
    self.assertEqual(result, 871198282)

def assure_023(self):
    from Complete.E023 import result
    self.assertEqual(result, 4179871)

def assure_024(self):
    from Complete.E024 import result
    self.assertEqual(result, 2783915460)

def assure_025(self):
    from Complete.E025 import result
    self.assertEqual(result, 4782)

def assure_026(self):
    from Complete.E026 import result
    self.assertEqual(result, 983)

def assure_027(self):
    from Complete.E027 import result
    result2 = get_haskell_output('027')

    self.assertEqual(result, result2)
    self.assertEqual(result, -59231)

def assure_028(self):
    from Complete.E028 import result
    self.assertEqual(result, 669171001)

def assure_029(self):
    from Complete.E029 import result
    self.assertEqual(result, 9183)

def assure_030(self):
    from Complete.E030 import result
    self.assertEqual(result, 9183)

def assure_031(self):
    from Complete.E031 import result
    self.assertEqual(result, 73682)

def assure_032(self):
    from Complete.E032 import result
    self.assertEqual(result, 45228)

def assure_033(self):
    from Complete.E033 import result
    self.assertEqual(result, 100)

def assure_034(self):
    from Complete.E034 import result
    self.assertEqual(result, 40730)

def assure_035(self):
    result = get_haskell_output('035')
    self.assertEqual(result, 55)

def assure_036(self):
    from Complete.E036 import result
    self.assertEqual(result, 872187)

def assure_037(self):
    from Complete.E037 import result
    self.assertEqual(result, 748317)

def assure_038(self):
    from Complete.E038 import result
    self.assertEqual(result, 932718654)

def assure_039(self):
    from Complete.E039 import result
    self.assertEqual(result, 840)

def assure_040(self):
    result = get_haskell_output('039')
    self.assertEqual(result, 210)

def assure_042(self):
    from Complete.E042 import result
    self.assertEqual(result, 162)

def assure_043(self):
    from Complete.E043 import result
    self.assertEqual(result, 16695334890)

def assure_044(self):
    from Complete.E044 import result
    self.assertEqual(result, 5482660)

def assure_045(self):
    from Complete.E045 import result
    self.assertEqual(result, 1533776805)

def assure_046(self):
    from Complete.E046 import result
    self.assertEqual(result, 5777)

def assure_048(self):
    from Complete.E048 import result
    self.assertEqual(result, 9110846700)

def assure_049(self):
    from Complete.E049 import result
    self.assertEqual(result, 296962999629)

def assure_053(self):
    from Complete.E053 import result
    self.assertEqual(result, 4075)

def assure_055(self):
    from Complete.E055 import result
    self.assertEqual(result, 249)

def assure_056(self):
    from Complete.E056 import result
    self.assertEqual(result, 972)

def assure_057(self):
    from Complete.E057 import result
    result2 = get_haskell_output('057')

    self.assertEqual(result, result2)
    self.assertEqual(result, 153)

def assure_058(self):
    from Complete.E058 import result
    self.assertEqual(result, None)

def assure_061(self):
    from Complete.E061 import result
    self.assertEqual(result, 28684)

def assure_063(self):
    result = get_haskell_output('063')
    self.assertEqual(result, 49)

def assure_065(self):
    from Complete.E065 import result
    self.assertEqual(result, 272)

def assure_069(self):
    from Complete.E069 import result
    self.assertEqual(result, None)

def assure_075(self):
    from Complete.E075 import result
    self.assertEqual(result, 161667)

def assure_076(self):
    from Complete.E076 import result
    self.assertEqual(result, 190569291)

def assure_087(self):
    from Complete.E087 import result
    self.assertEqual(result, 1097343)

def assure_092(self):
    from Complete.E092 import result
    self.assertEqual(result, 8581146)

def assure_097(self):
    from Complete.E097 import result
    self.assertEqual(result, 8739992577)