import unittest
import Complete as C

class TestCompleteChallengesYieldCorrectResults(unittest.TestCase):
    def test_assure_1_ok(self):
        import Complete.E001
        self.assertEqual(Complete.E001.result, 233168) 