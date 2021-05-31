class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        return self.count_cell + other.count_cell

    def __sub__(self, other):
        result = self.count_cell - other.count_cell
        if result >= 0:
            return result
        else:
            raise ValueError('Результат не может быть отрицательным')

    def __mul__(self, other):
        return self.count_cell * other.count_cell

    def __floordiv__(self, other):
        return self.count_cell // other.count_cell

    def make_order(self, count_cells: int):
        for i in range(1, self.count_cell+1):
            if i % count_cells == 0:
                print('*')
            else:
                print('*', end='')


first_cell = Cell(15)
second_cell = Cell(200)
# print(first_cell - second_cell)
print(first_cell + second_cell)
print(first_cell * second_cell)
print(first_cell // second_cell)
first_cell.make_order(5)