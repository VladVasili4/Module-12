import unittest
import homework_12_1
import homework_12_2

homeST = unittest.TestSuite()
homeST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework_12_1.RunnerTest))
homeST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(homeST)