class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя сотрудника - {self.name} {self.surname}')


first_worker = Position('qwe', 'erty', 'boss', 1000, 100)
first_worker.get_full_name()
print(first_worker.name, first_worker.surname, first_worker.position)
