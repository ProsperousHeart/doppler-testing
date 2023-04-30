import unittest
import main as script

class BaseTests(unittest.TestCase):
    def test_get_env(self):
        '''
        Testing to confirm doppler secret
        '''
        result = script.get_env()
        self.assertIsNotNone(result, "Are secrets loaded properly?")
        self.assertEqual(result, "Kassandra")
    
    def test_getUN(self):
        '''
        Checking Doppler trick for referencing secrets
        '''
        result = script.get_un()
        self.assertIsNotNone(result, "Are secrets loaded properly?")
        self.assertEqual(result, "USER.Kassandra")

if __name__ == "__main__":
    unittest.main()
