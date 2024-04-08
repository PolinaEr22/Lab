# Класс Tomato
class Tomato:
    states = {'unripe': 0, 'ripe': 1}

    # Словарь states определяет состояния помидора: незрелый и спелый
    def __init__(self, index):
        self._index = index
        self._state = self.states['unripe']
        # Инициализация объекта помидора с заданным индексом и начальным состоянием 'unripe' (=0)
        # Свойства _index и _state являются динамическими, _index передается параметром, _state получает значение 'unripe'

    def grow(self):
        # Метод для созревания помидора
        if self._state < len(self.states) - 1:
            self._state += 1
            # Увеличиваем состояние помидора на 1,
            # если оно меньше максимального значения в states

    def is_ripe(self):
        # Метод для проверки, созрел ли помидор
        return self._state == self.states['ripe']
    # Возвращяем True, если состояние помидора равно 'ripe' (1)

# Класс TomatoBush

class TomatoBush:
    def __init__(self, num_tomatoes):
        # Инициализация куста помидоров с заданным количеством
        self.tomatoes = [Tomato(index) for index in range(num_tomatoes)]
        # Создание списка помидоров в соответствии с заданным количеством

    def grow_all(self):
        # Метод для вызова метода grow() у каждого помидора в кусте
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Метод для проверки, все ли помидоры в кусте созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    # Возвращает True, если все помидоры созрели, иначе False

    def give_away_all(self):
        # Метод для сбора урожая путем удаления всех помидоров
        self.tomatoes = []
        # Очищаем список помидоров

# Класс Gardener

class Gardener:
    def __init__(self, name, plant):
        # Инициализация класса Садовод с указанием имени и объекта куста помидоров
        self.name = name
        self._plant = plant
        # Свойство name - публичное, свойство _plant - приватное, хранит объект TomatoBush

    def work(self):
        # Метод для работы с кустом помидоров, вызывает метод grow_all() у куста
        self._plant.grow_all()

    def harvest(self):
        # Метод для сбора урожая
        if self._plant.all_are_ripe():
            # Если все помидоры созрели
            self._plant.give_away_all()
            print("Собрали все помидоры!")
        else:
            print("Еще не все помидоры дозрели, продолжайте ухаживать за ними.")
            # Иначе выводим сообщение о том, что не все помидоры дозрели

    @staticmethod
    def knowledge_base():
        # Статический метод для вывода базы знаний по садоводству
        print("База знаний садоводства:")
        print("- Поливайте растения регулярно")
        print("- Обеспечьте правильное количество солнечного света")
        print("- Обратите внимание на вредителей и болезни")
        # Выводим советы по уходу за растениями


# Тесты

# 1) Вызов справки по садоводству
Gardener.knowledge_base()

# 2) Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener("Алиса", bush)

# 3) Поливка и уход за кустом с помидорами с помощью объекта класса Gardener
gardener.work()
gardener.work()

# 4) Попытка собрать урожай, когда помидоры еще не дозрели. Продолжайте ухаживать за ними
gardener.harvest()

# 5) Сбор урожая
gardener.work()
gardener.work()
gardener.harvest()
