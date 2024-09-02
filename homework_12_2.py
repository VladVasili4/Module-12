"""Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами."""

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