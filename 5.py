class Stationery:
    def __init__(self, name):
        self.name = name

    def title(self):
        print(f'{self.name} - название канцелярской пренадлежности')

    def draw(self):
        print('Запуски отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.name} начал отрисовку,{self.name} оставляет тонкие линии синего цвета')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.name} начал отрисовку, {self.name} оставляет тонкие линии серого цвета')


class Handle(Stationery):
    def draw(self):
        print(f'{self.name} начал отрисовку, {self.name} оставляет толстые линии черного цвета')

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

pen.draw()
pencil.draw()
handle.draw()
