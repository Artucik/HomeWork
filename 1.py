class Matrix:
    def __init__(self, d_massive):
        self.matrix = [[i for i in massive] for massive in d_massive]

    def show_matrix(self):
        for i in self.matrix:
            print(i)


matrix = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matrix.show_matrix()
