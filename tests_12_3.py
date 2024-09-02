import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()                               # благодаря этой строке __eq__ в Runner не имеет смысла
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name         # добавил в конце ".name"
                    place += 1
                    self.participants.remove(participant)

        return finishers



if __name__=='__main__':
    unittest.main()

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



@unittest.skip('Тесты в этом кейсе заморожены')
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)


    def test_Tournament1(self):
        self.t1 = Tournament(90, self.r1, self.r3)
        self.all_results = self.t1.start()
        self.assertTrue(self.all_results[2] == 'Ник')

    def test_Tournament2(self):
        self.t2 = Tournament(90, self.r2, self.r3)
        self.all_results = self.t2.start()
        self.assertTrue(self.all_results[2] == 'Ник')

    def test_Tournament3(self):
        self.t3 = Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = self.t3.start()
        self.assertTrue(self.all_results[3] == 'Ник')

    def tearDown(self):
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)