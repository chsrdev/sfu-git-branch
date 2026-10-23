class Matrix:
    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            return

        self._width = width
        self._height = height
        self.matrix = [[0 for _ in range(width)] for _ in range(height)]
        print(self.matrix)
