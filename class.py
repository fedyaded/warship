class Tomato:

    states = {0: "ничего", 1: 'семя', 2: "зелёный", 3: "спелый"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помидор {self._index} еще {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []



class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print("Садовник работает...")
        self._plant.grow_all()
        print("Садовник закончил работу!")

    # Собираем урожай
    def harvest(self):
        print("Садовник собирает урожай...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Садовник закончил собирать урожай!")
        else:
            print("Еще рано! Они не созрели")

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print("Всего 3 стадии созревания томатов, еще цветок, зеленый и спелый! Садовник соберёт весь урожай только вам стоит дождаться пока он вырастет! ")


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(2)
    gardener = Gardener("Иван", great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

