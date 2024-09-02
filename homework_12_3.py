import unittest
import tests_12_3


homeST = unittest.TestSuite()
homeST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
homeST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(homeST)