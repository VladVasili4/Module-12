import logging
import unittest

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
            # logger2.info('Неверная скорость для Runner')


    def run(self):
        self.distance += self.speed * 2
        # logging.info('Runner пробежал')

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walker = Runner('Вaся', speed=8)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Что-то не сходится в walk, сумма скоростей не совпадает', exc_info = True)

    # @unittest.skip
    def test_run(self):
        runer = Runner('Илья', speed = 10)
        try:
            for i in range(10):
                runer.run()
            self.assertEqual(runer.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Что-то не сходится в run, сумма скоростей не совпадает', exc_info = True)#

    # @unittest.skip
    def test_challenge (self):
        walker1 = Runner('Fedor')
        walker2 = Runner('Egor')
        for i in range(10):
            walker1.run()
            walker2.walk()
        self.assertNotEqual(walker1.distance, walker2.distance)

# first = Runner('Вaся', 10)
# first.run()
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())


