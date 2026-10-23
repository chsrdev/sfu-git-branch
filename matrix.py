from random import randint

class Matrix:
    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            return

        self._width = width
        self._height = height
        self._matrix = [[0 for _ in range(width)] for _ in range(height)]

    def get_height(self) -> int:
        return self._height

    def get_width(self) -> int:
        return self._width

    def set_number(self, i: int, j: int, num: int):
        if i >= 0 and i < self._height and j >= 0 and j < self._width:
            self._matrix[i][j] = num
        else:
            raise IndexError("Заданные координаты находятся вне пределов матрицы")

    def get_matrix(self):
        return self._matrix

    def fill_random(self):
        for i in range(self._height):
            for j in range(self._width):
                self._matrix[i][j] = randint(0, 100)