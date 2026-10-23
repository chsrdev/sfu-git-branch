from random import randint

class Matrix:
    def __init__(self, width: int, height: int):
        if width <= 0 or height <= 0:
            raise ValueError("Размер матрицы не может быть отрицательным или нулевым")

        self._width = width
        self._height = height
        self._matrix = [[0 for _ in range(width)] for _ in range(height)]

    @property
    def matrix(self):
        return self._matrix

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    def set_number(self, i: int, j: int, num: int):
        if i >= 0 and i < self._height and j >= 0 and j < self._width:
            self._matrix[i][j] = num
        else:
            raise IndexError("Заданные координаты находятся вне пределов матрицы")
        
    def fill_random(self):
        for i in range(self._height):
            for j in range(self._width):
                self._matrix[i][j] = randint(0, 100)

    def __str__(self) -> str:
        max_len = max(len(str(num)) for row in self._matrix for num in row)
        lines = []
        for row in self._matrix:
            formatted_row = " ".join(f"{num:<{max_len}}" for num in row)
            lines.append(formatted_row)

        return "\n".join(lines)

    def function_16(self) -> list[int]:
        """Возвращает номера тех строк массива, в которых есть хотя бы один элемент, равный 10."""
        res = []
        for i in range(len(self._matrix)):
            if any(n == 10 for n in self._matrix[i]):
                res.append(i+1)
        return res