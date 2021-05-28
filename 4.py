from time import sleep


class Car:
    def __init__(self, name, color, speed, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            self.speed = int(input(f'С какой скоростью будет ехать {self.name}? '))
            print(f'{self.name} начинает движение')
            sleep(2)
            print(f'{self.name} разогналась до {self.speed}')
        elif self.speed > 0:
            print(f'{self.name} уже движется')
            message = input('Хотите изменить скорость?(y/n) ')
            if message == 'y':
                self.speed = int(input(f'С какой скоростью поедет {self.name}? '))
                print(f'Теперь {self.name} едет со скоростью {self.speed}')
            elif message == 'n':
                print(f'{self.name} продолжает движение со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась (скорость - {self.speed})')

    def turn(self):
        choice = input(f'Перед {self.name} перекресток, куда она поедет?(right, left, forward) ')
        if choice == 'forward':
            print(f'{self.name} поехала прямо')
        elif choice == 'left':
            print(f'{self.name} повернула налево')
        elif choice == 'right':
            print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 60:
            print(f'{self.name} превысила допустимую скорость')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 40:
            print(f'{self.name} превысила допустимую скорость')


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass



police_car = PoliceCar('Полицейская машина', 'Черный', 20, True)
work_car = WorkCar('Бетономешалка', 'Оранжевый', 0, False)
town_car = TownCar('BMW', 'Черный', 11, False)

work_car.go()
work_car.show_speed()
police_car.go()
police_car.show_speed()
town_car.go()
town_car.show_speed()
