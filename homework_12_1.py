import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    # def __init__(self):
    def setUp(self):
        print("go")

    def test_walk(self):
        walker = Runner('Ivan')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)


    def test_run(self):
        runer = Runner('Igor')
        for i in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    def test_challenge (self):
        walker1 = Runner('Fedor')
        walker2 = Runner('Egor')
        for i in range(10):
            walker1.run()
            walker2.walk()
        self.assertNotEqual(walker1.distance, walker2.distance)


if __name__ == "__main__":
  unittest.main()
test1 = RunnerTest.test_walk

