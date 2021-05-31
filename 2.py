from abc import ABC, abstractmethod


# шаблон для создания класса каждого типа одежды
class Clothes(ABC):
    name = 'Осенняя одежда'

    @abstractmethod
    def count_material(self):  # абстрактный метод, который принуждает задать кол-во материала
        pass

    def __add__(self, other):
        return self.count_material + other.count_material


# класс пальто
class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.V = v

    @property
    def count_material(self):
        return self.V / 6.5 + 0.5


# класс костюм
class Suit(Clothes):
    def __init__(self, name: str, h: int):
        self.name = name
        self.H = h

    @property
    def count_material(self):
        return 2 * self.H + 0.3


# класс, для общего подсчета расхода ткани
class Result(ABC):
    def __init__(self, suit: Suit, coat: Coat):
        self.result = suit + coat

    @property
    def show_result(self):
        return self.result


dress1 = Suit('Костюм', 190)
dress2 = Coat('Пальто', 90)
print(dress1 + dress2)
print(dress1.count_material)
print(dress2.count_material)

result = Result(suit=dress1, coat=dress2)
print(result.show_result)
