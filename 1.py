from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self, count_switch):
        switches = 0  # сколько будет переключений цветов

        def init_color(color):
            """Функция, которая определяет какой цвет горит на светофоре"""
            if color == 'red':
                print(f'Горит {color}')
                print('Красный будет гореть 7 секунд')
            elif color == 'green':
                print(f'Горит {color}')
                print('Зеленый будет гореть 12 секунд')
            elif color == 'yellow':
                print(f'Горит {color}')
                print('Желтый будет гореть 2 секунд')

        while switches != count_switch:
            if self.__color == 'red':
                init_color(self.__color)
                sleep(7)
                self.__color = 'yellow'

            elif self.__color == 'green':
                init_color(self.__color)
                sleep(12)
                self.__color = 'red'

            elif self.__color == 'yellow':
                init_color(self.__color)
                sleep(2)
                self.__color = 'green'
            switches += 1


first = TrafficLight('yellow')
first.running(3)
