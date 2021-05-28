class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def show_weight_of_asphalt(self, plate_thickness, weight_piece_asphalt):
        print(f'Масса асфальта, необходимая для покрытия дороги длиной - {self._length}м и шириной {self._width}м')
        print(f'{self._length}м * {self._width}м * {weight_piece_asphalt}кг * {plate_thickness}см = '
              f'{self._width * self._length * weight_piece_asphalt * plate_thickness}т')


first_road = Road(10000, 10)
first_road.show_weight_of_asphalt(25, 10)
